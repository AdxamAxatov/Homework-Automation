"""Orchestrator-side DB helpers.

These functions are what ``drive.py`` calls between agent invocations.
Single-writer pattern: the orchestrator process is the only writer to
``homework_db.sqlite``. All writes go through autocommit transactions.

Kept in a separate module from ``db.py`` so the schema-init module stays small
and can be imported by tests/CLIs without pulling in orchestrator code.
"""
from __future__ import annotations

import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from .db import DEFAULT_DB_PATH, connect, init_schema

# ---------------------------------------------------------------------------
# Time helpers
# ---------------------------------------------------------------------------

def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# Homework lifecycle
# ---------------------------------------------------------------------------

def mint_homework_id(conn: sqlite3.Connection, when: datetime | None = None) -> str:
    """Generate ``HW-YYYYMMDD-NNN`` matching CONTRACTS.md::Homework Record id format.

    Sequence is per-day, derived from the current count of homeworks created
    today. Collisions are not possible under the single-writer assumption.
    """
    when = when or datetime.now(UTC)
    date_token = when.strftime("%Y%m%d")
    prefix = f"HW-{date_token}-"
    n = conn.execute(
        "SELECT COUNT(*) FROM homeworks WHERE id LIKE ?", (prefix + "%",)
    ).fetchone()[0]
    return f"{prefix}{n + 1:03d}"


def ensure_manual_theme_link(
    conn: sqlite3.Connection,
    *,
    grade_id: int,
    subject_id: str,
    textbook_label: str | None,
    language: str,
    raw_title: str,
    start_page: int = 0,
    ordinal: int = 0,
) -> int:
    """Create (or fetch) a one-off ``theme_links`` row for a lesson that wasn't
    pre-ingested via ``ingest.py`` + ``link.py``.

    The orchestrator calls this when an operator drives a build by handing it
    a raw lesson reference (e.g. for the very first algebra autonomous build,
    before the algebra TOC is ingested). The row is created in
    ``validator_state='confirmed'`` because the operator's intent is the
    confirmation. ``match_method`` is recorded as ``'manual'`` so a later
    audit can find these.

    A throwaway ``themes`` row is also created for FK satisfaction. It is
    flagged with ``theme_kind='lesson'`` and ``textbook_id=NULL``-style
    handling via a sentinel textbook lookup.
    """
    # Find or create a "manual" textbook record per (grade, subject, language).
    # We need a textbooks row because themes.textbook_id is NOT NULL.
    file_path_sentinel = f"manual:{subject_id}:g{grade_id}:{language}"
    tb = conn.execute(
        "SELECT id FROM textbooks WHERE file_path=?", (file_path_sentinel,)
    ).fetchone()
    if tb is None:
        cur = conn.execute(
            """INSERT INTO textbooks(grade_id, subject_id, language, textbook_label,
                                      file_path, publisher, edition_year, page_count,
                                      encoding_quirk, themes_extracted_at)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (grade_id, subject_id, language, textbook_label, file_path_sentinel,
             "manual", None, None, None, _now()),
        )
        textbook_id = cur.lastrowid
    else:
        textbook_id = tb["id"]

    # Find or create the theme row for this exact lesson reference.
    theme = conn.execute(
        """SELECT id FROM themes
           WHERE textbook_id=? AND raw_title=? AND ordinal_start=? AND start_page=?""",
        (textbook_id, raw_title, ordinal, start_page),
    ).fetchone()
    if theme is None:
        cur = conn.execute(
            """INSERT INTO themes(textbook_id, ordinal_start, ordinal_end,
                                  raw_title, normalized_title, start_page, theme_kind)
               VALUES (?,?,?,?,?,?,'lesson')""",
            (textbook_id, ordinal, ordinal, raw_title, raw_title.lower(), start_page),
        )
        theme_id = cur.lastrowid
    else:
        theme_id = theme["id"]

    # Find or create the theme_link row.
    uz_id = theme_id if language == "uz" else None
    ru_id = theme_id if language == "ru" else None
    link = conn.execute(
        """SELECT id FROM theme_links
           WHERE grade_id=? AND subject_id=? AND IFNULL(textbook_label,'')=IFNULL(?,'')
             AND IFNULL(uz_theme_id,0)=IFNULL(?,0) AND IFNULL(ru_theme_id,0)=IFNULL(?,0)""",
        (grade_id, subject_id, textbook_label, uz_id, ru_id),
    ).fetchone()
    if link is not None:
        return link["id"]

    status = "uz_only" if language == "uz" else "ru_only"
    cur = conn.execute(
        """INSERT INTO theme_links(grade_id, subject_id, textbook_label,
                                    uz_theme_id, ru_theme_id,
                                    match_status, match_method, match_confidence,
                                    validator_state, validator_notes)
           VALUES (?,?,?,?,?,?,'manual',1.0,'confirmed',?)""",
        (grade_id, subject_id, textbook_label, uz_id, ru_id, status,
         f"manual ad-hoc link created by orchestrator for {raw_title!r}"),
    )
    return cur.lastrowid


def create_homework(
    conn: sqlite3.Connection,
    *,
    grade_id: int,
    subject_id: str,
    theme_link_id: int,
    mode: str,
) -> str:
    """Insert a fresh ``homeworks`` row in status='queued'. Returns the new id."""
    homework_id = mint_homework_id(conn)
    conn.execute(
        """INSERT INTO homeworks(id, grade_id, subject_id, theme_link_id, mode, status)
           VALUES (?,?,?,?,?,'queued')""",
        (homework_id, grade_id, subject_id, theme_link_id, mode),
    )
    return homework_id


def set_homework_status(
    conn: sqlite3.Connection,
    homework_id: str,
    status: str,
    *,
    current_phase: str | None = None,
    last_error: str | None = None,
) -> None:
    """Move the homework through its lifecycle: queued/extracting/building/validating/ready/error/patched."""
    conn.execute(
        """UPDATE homeworks SET status=?, current_phase=COALESCE(?, current_phase),
                                last_error=?, updated_at=? WHERE id=?""",
        (status, current_phase, last_error, _now(), homework_id),
    )


def increment_homework_attempts(conn: sqlite3.Connection, homework_id: str) -> None:
    conn.execute(
        "UPDATE homeworks SET attempts = attempts + 1, updated_at=? WHERE id=?",
        (_now(), homework_id),
    )


# ---------------------------------------------------------------------------
# Phase lifecycle
# ---------------------------------------------------------------------------

def start_phase_run(
    conn: sqlite3.Connection,
    *,
    homework_id: str,
    language: str,
    phase: str,
    attempt: int,
) -> int:
    """Insert a ``phase_runs`` row for a fresh worker invocation. Returns the row id.

    ``attempt`` is 0-indexed (0 for the first try, 1 for the retry).
    """
    cur = conn.execute(
        """INSERT INTO phase_runs(homework_id, language, phase, status, attempts,
                                   validator_state, started_at)
           VALUES (?,?,?,'running',?,'proposed',?)""",
        (homework_id, language, phase, attempt, _now()),
    )
    return cur.lastrowid


def record_phase_result(
    conn: sqlite3.Connection,
    *,
    phase_run_id: int,
    status: str,                 # 'done' | 'failed'
    validator_state: str,        # 'proposed' | 'confirmed' | 'rejected'
    output_excerpt: str | None,  # max ~200 chars; truncated below
) -> None:
    if output_excerpt is not None and len(output_excerpt) > 200:
        output_excerpt = output_excerpt[:197] + "..."
    conn.execute(
        """UPDATE phase_runs SET status=?, validator_state=?, output_excerpt=?,
                                  finished_at=? WHERE id=?""",
        (status, validator_state, output_excerpt, _now(), phase_run_id),
    )


def latest_phase_attempt(
    conn: sqlite3.Connection,
    *,
    homework_id: str,
    language: str,
    phase: str,
) -> sqlite3.Row | None:
    """Most recent ``phase_runs`` row for this (homework, language, phase) tuple."""
    return conn.execute(
        """SELECT * FROM phase_runs
           WHERE homework_id=? AND language=? AND phase=?
           ORDER BY attempts DESC, id DESC LIMIT 1""",
        (homework_id, language, phase),
    ).fetchone()


# ---------------------------------------------------------------------------
# Payload write (final assembler output)
# ---------------------------------------------------------------------------

def write_payload(
    conn: sqlite3.Connection,
    *,
    homework_id: str,
    language: str,
    content_json_text: str,
    schema_version: str,
    validator_score: float | None = None,
    validator_notes: str | None = None,
) -> None:
    """Insert (or replace) the ``homework_payloads`` row for one (homework, language)."""
    conn.execute(
        """INSERT INTO homework_payloads(homework_id, language, content_json,
                                          schema_version, validated_at,
                                          validator_score, validator_notes)
           VALUES (?,?,?,?,?,?,?)
           ON CONFLICT(homework_id, language) DO UPDATE SET
               content_json=excluded.content_json,
               schema_version=excluded.schema_version,
               validated_at=excluded.validated_at,
               validator_score=excluded.validator_score,
               validator_notes=excluded.validator_notes""",
        (homework_id, language, content_json_text, schema_version, _now(),
         validator_score, validator_notes),
    )


# ---------------------------------------------------------------------------
# Convenience: open + init in one call (for orchestrator startup)
# ---------------------------------------------------------------------------

def open_db(db_path: Path | str | None = None) -> sqlite3.Connection:
    conn = connect(db_path or DEFAULT_DB_PATH)
    init_schema(conn)
    return conn
