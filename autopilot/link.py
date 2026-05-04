"""link_themes — pair UZ↔RU lesson rows into ``theme_links`` for one (grade, subject[, label]).

For ``bilingual_distinct`` subjects the orchestrator joins each UZ lesson to its
RU twin using the exact triple ``(ordinal_start, ordinal_end, start_page)``.
Pairs that match get ``match_status='matched'`` + ``match_method='ordinal_page_exact'``;
unmatched UZ→ ``uz_only``, unmatched RU → ``ru_only``. Matches with mismatched
``ordinal_end`` (bundle disagreement) but matching ``start_page`` get
``match_status='reordered'``.

For ``monolingual_shared`` subjects (currently only ``english``) we link each
shared theme to itself with ``match_method='single_source'`` and language=null.

Every produced row starts in ``validator_state='proposed'`` — the upper-level
validator agent is what flips them to ``confirmed`` before homeworks are
allowed to enqueue against them.

Usage:
    python -m autopilot.link --grade 8 --subject history --label "Jahon Tarixi"
    python -m autopilot.link --grade 8 --subject geometriya-g7-11
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .db import DEFAULT_DB_PATH, connect, init_schema


def link(
    *,
    grade: int,
    subject_id: str,
    textbook_label: str | None,
    db_path: Path,
) -> dict:
    conn = connect(db_path)
    init_schema(conn)

    coverage_row = conn.execute("SELECT coverage_mode FROM subjects WHERE id=?", (subject_id,)).fetchone()
    if coverage_row is None:
        raise SystemExit(f"unknown subject {subject_id!r}")
    coverage_mode = coverage_row["coverage_mode"]

    # Wipe existing proposed/confirmed links for this scope so re-runs are idempotent.
    conn.execute(
        """
        DELETE FROM theme_links
        WHERE grade_id=? AND subject_id=? AND IFNULL(textbook_label,'')=IFNULL(?,'')
        """,
        (grade, subject_id, textbook_label),
    )

    if coverage_mode == "monolingual_shared":
        # Pull the single textbook (language NULL) and emit one link per lesson.
        textbook_row = conn.execute(
            """SELECT id FROM textbooks WHERE grade_id=? AND subject_id=? AND language IS NULL
               AND IFNULL(textbook_label,'')=IFNULL(?,'')""",
            (grade, subject_id, textbook_label),
        ).fetchone()
        if textbook_row is None:
            raise SystemExit(
                f"no monolingual_shared textbook ingested for grade={grade} subject={subject_id!r} "
                f"label={textbook_label!r}"
            )
        themes = conn.execute(
            "SELECT id FROM themes WHERE textbook_id=? AND theme_kind IN ('lesson','unit') ORDER BY ordinal_start",
            (textbook_row["id"],),
        ).fetchall()
        for t in themes:
            # Reuse uz_theme_id slot for the singleton id; ru is null.
            conn.execute(
                """INSERT INTO theme_links(
                       grade_id, subject_id, textbook_label, uz_theme_id, ru_theme_id,
                       match_status, match_method, match_confidence, validator_state
                   ) VALUES (?,?,?,?,NULL,'matched','single_source',1.0,'proposed')""",
                (grade, subject_id, textbook_label, t["id"]),
            )
        return _summary(conn, grade, subject_id, textbook_label)

    # bilingual_distinct
    uz_book = conn.execute(
        """SELECT id FROM textbooks WHERE grade_id=? AND subject_id=? AND language='uz'
           AND IFNULL(textbook_label,'')=IFNULL(?,'')""",
        (grade, subject_id, textbook_label),
    ).fetchone()
    ru_book = conn.execute(
        """SELECT id FROM textbooks WHERE grade_id=? AND subject_id=? AND language='ru'
           AND IFNULL(textbook_label,'')=IFNULL(?,'')""",
        (grade, subject_id, textbook_label),
    ).fetchone()

    if uz_book is None and ru_book is None:
        raise SystemExit(
            f"no UZ or RU textbook ingested for grade={grade} subject={subject_id!r} label={textbook_label!r}"
        )

    uz_lessons = (
        conn.execute(
            """SELECT id, ordinal_start, ordinal_end, start_page, raw_title FROM themes
               WHERE textbook_id=? AND theme_kind='lesson' ORDER BY ordinal_start""",
            (uz_book["id"],),
        ).fetchall()
        if uz_book else []
    )
    ru_lessons = (
        conn.execute(
            """SELECT id, ordinal_start, ordinal_end, start_page, raw_title FROM themes
               WHERE textbook_id=? AND theme_kind='lesson' ORDER BY ordinal_start""",
            (ru_book["id"],),
        ).fetchall()
        if ru_book else []
    )

    # Index RU lessons by their join key.
    ru_by_exact: dict[tuple[int, int, int], int] = {}
    ru_by_page: dict[tuple[int, int], int] = {}      # (ordinal_start, start_page)
    for r in ru_lessons:
        ru_by_exact[(r["ordinal_start"], r["ordinal_end"], r["start_page"])] = r["id"]
        ru_by_page[(r["ordinal_start"], r["start_page"])] = r["id"]

    matched_ru_ids: set[int] = set()
    proposed = 0

    for u in uz_lessons:
        key_exact = (u["ordinal_start"], u["ordinal_end"], u["start_page"])
        key_page = (u["ordinal_start"], u["start_page"])
        ru_id = ru_by_exact.get(key_exact)
        if ru_id is not None:
            conn.execute(
                """INSERT INTO theme_links(
                       grade_id, subject_id, textbook_label, uz_theme_id, ru_theme_id,
                       match_status, match_method, match_confidence, validator_state
                   ) VALUES (?,?,?,?,?,'matched','ordinal_page_exact',1.0,'proposed')""",
                (grade, subject_id, textbook_label, u["id"], ru_id),
            )
            matched_ru_ids.add(ru_id)
            proposed += 1
            continue
        ru_id = ru_by_page.get(key_page)
        if ru_id is not None:
            # Same lesson number + same start page but bundle range differs —
            # treat as matched-with-caveat for the validator to look at.
            conn.execute(
                """INSERT INTO theme_links(
                       grade_id, subject_id, textbook_label, uz_theme_id, ru_theme_id,
                       match_status, match_method, match_confidence, validator_state, validator_notes
                   ) VALUES (?,?,?,?,?,'reordered','ordinal_only',0.7,'proposed',
                       'ordinal_start+start_page match, but ordinal_end differs (bundle disagreement)')""",
                (grade, subject_id, textbook_label, u["id"], ru_id),
            )
            matched_ru_ids.add(ru_id)
            proposed += 1
            continue
        # No RU twin — UZ-only link.
        conn.execute(
            """INSERT INTO theme_links(
                   grade_id, subject_id, textbook_label, uz_theme_id, ru_theme_id,
                   match_status, match_method, match_confidence, validator_state
               ) VALUES (?,?,?,?,NULL,'uz_only','ordinal_page_exact',0.0,'proposed')""",
            (grade, subject_id, textbook_label, u["id"]),
        )
        proposed += 1

    for r in ru_lessons:
        if r["id"] in matched_ru_ids:
            continue
        conn.execute(
            """INSERT INTO theme_links(
                   grade_id, subject_id, textbook_label, uz_theme_id, ru_theme_id,
                   match_status, match_method, match_confidence, validator_state
               ) VALUES (?,?,?,NULL,?,'ru_only','ordinal_page_exact',0.0,'proposed')""",
            (grade, subject_id, textbook_label, r["id"]),
        )
        proposed += 1

    return _summary(conn, grade, subject_id, textbook_label)


def _summary(conn, grade: int, subject_id: str, textbook_label: str | None) -> dict:
    rows = conn.execute(
        """SELECT match_status, COUNT(*) AS n FROM theme_links
           WHERE grade_id=? AND subject_id=? AND IFNULL(textbook_label,'')=IFNULL(?,'')
           GROUP BY match_status""",
        (grade, subject_id, textbook_label),
    ).fetchall()
    return {row["match_status"]: row["n"] for row in rows}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Pair UZ↔RU themes into theme_links (proposed state)")
    p.add_argument("--grade", type=int, required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--label", default=None)
    p.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    args = p.parse_args(argv)

    summary = link(
        grade=args.grade,
        subject_id=args.subject,
        textbook_label=args.label,
        db_path=args.db,
    )
    parts = [f"{k}={v}" for k, v in sorted(summary.items())]
    print(f"theme_links proposed: {' '.join(parts) if parts else '(none)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
