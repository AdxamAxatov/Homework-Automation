"""ingest_textbook — register a PDF and stamp its themes into homework_db.

Usage:
    python -m autopilot.ingest --grade 8 --subject history --language uz \\
        --label "Jahon Tarixi" --profile flat path/to/textbook.pdf

    python -m autopilot.ingest --grade 8 --subject geometriya-g7-11 --language ru \\
        --profile three_level path/to/geometry_ru.pdf

Behavior:
    * Reads the PDF (CP1251 mojibake auto-recovered).
    * Parses the TOC according to the chosen profile (or 'auto').
    * Inserts/updates the ``textbooks`` row keyed by file_path.
    * Replaces all ``themes`` rows for that textbook.
    * Prints a summary and exits 0 on success.
"""
from __future__ import annotations

import argparse
import sys
from datetime import UTC, datetime
from pathlib import Path

from .db import DEFAULT_DB_PATH, connect, init_schema
from .toc import extract_textbook


def ingest(
    *,
    pdf_path: Path,
    grade: int,
    subject_id: str,
    language: str | None,
    textbook_label: str | None,
    profile: str,
    publisher: str | None,
    edition_year: int | None,
    notion_page_id: str | None,
    db_path: Path,
) -> dict:
    pdf_path = pdf_path.resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    entries, encoding_quirk, page_count = extract_textbook(pdf_path, profile=profile)

    conn = connect(db_path)
    init_schema(conn)

    # Validate FKs early with friendlier errors.
    if not conn.execute("SELECT 1 FROM grades WHERE id=?", (grade,)).fetchone():
        raise SystemExit(f"unknown grade {grade!r} (expected 1..11)")
    if not conn.execute("SELECT 1 FROM subjects WHERE id=?", (subject_id,)).fetchone():
        raise SystemExit(f"unknown subject {subject_id!r} (must match CONTRACTS.md SUBJECTS)")
    if language is not None and not conn.execute("SELECT 1 FROM languages WHERE code=?", (language,)).fetchone():
        raise SystemExit(f"unknown language {language!r} (expected 'uz' or 'ru')")

    # Enforce coverage_mode ↔ language consistency
    coverage_mode = conn.execute("SELECT coverage_mode FROM subjects WHERE id=?", (subject_id,)).fetchone()["coverage_mode"]
    if coverage_mode == "monolingual_shared" and language is not None:
        raise SystemExit(
            f"subject {subject_id!r} has coverage_mode=monolingual_shared; pass --language '' (omit) "
            f"or use --language unset; this textbook serves both UZ and RU schools."
        )
    if coverage_mode == "bilingual_distinct" and language is None:
        raise SystemExit(f"subject {subject_id!r} has coverage_mode=bilingual_distinct; --language is required")

    now = datetime.now(UTC).isoformat(timespec="seconds")

    conn.execute("BEGIN")
    try:
        # Upsert textbook by file_path (the natural unique key).
        existing = conn.execute("SELECT id FROM textbooks WHERE file_path=?", (str(pdf_path),)).fetchone()
        if existing:
            textbook_id = existing["id"]
            conn.execute(
                """
                UPDATE textbooks SET
                    grade_id=?, subject_id=?, language=?, textbook_label=?,
                    publisher=?, edition_year=?, page_count=?, encoding_quirk=?,
                    notion_page_id=?, themes_extracted_at=?
                WHERE id=?
                """,
                (
                    grade, subject_id, language, textbook_label,
                    publisher, edition_year, page_count, encoding_quirk,
                    notion_page_id, now, textbook_id,
                ),
            )
            conn.execute("DELETE FROM themes WHERE textbook_id=?", (textbook_id,))
        else:
            cur = conn.execute(
                """
                INSERT INTO textbooks(
                    grade_id, subject_id, language, textbook_label, file_path,
                    publisher, edition_year, page_count, encoding_quirk,
                    notion_page_id, themes_extracted_at
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    grade, subject_id, language, textbook_label, str(pdf_path),
                    publisher, edition_year, page_count, encoding_quirk,
                    notion_page_id, now,
                ),
            )
            textbook_id = cur.lastrowid

        for e in entries:
            conn.execute(
                """
                INSERT INTO themes(
                    textbook_id, chapter_ordinal, chapter_title,
                    section_ordinal, section_title,
                    ordinal_start, ordinal_end,
                    raw_title, normalized_title,
                    start_page, theme_kind
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    textbook_id,
                    e.chapter_ordinal, e.chapter_title,
                    e.section_ordinal, e.section_title,
                    e.ordinal_start, e.ordinal_end,
                    e.raw_title, e.normalized_title,
                    e.start_page, e.theme_kind,
                ),
            )

        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise

    summary = {
        "textbook_id": textbook_id,
        "page_count": page_count,
        "encoding_quirk": encoding_quirk,
        "themes_total": len(entries),
        "themes_lessons": sum(1 for e in entries if e.theme_kind == "lesson"),
        "kinds": {},
    }
    for e in entries:
        summary["kinds"][e.theme_kind] = summary["kinds"].get(e.theme_kind, 0) + 1
    return summary


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Ingest a textbook PDF into homework_db")
    p.add_argument("pdf_path", type=Path)
    p.add_argument("--grade", type=int, required=True)
    p.add_argument("--subject", required=True, help="subject ID from CONTRACTS.md (e.g. 'history')")
    p.add_argument("--language", choices=["uz", "ru"], default=None,
                   help="omit for subjects with coverage_mode=monolingual_shared (e.g. english)")
    p.add_argument("--label", default=None,
                   help="optional textbook label (e.g. 'Jahon Tarixi' vs 'O''zbekiston Tarixi' within history)")
    p.add_argument("--profile", choices=["flat", "three_level", "auto"], default="auto")
    p.add_argument("--publisher", default=None)
    p.add_argument("--year", type=int, default=None, dest="edition_year")
    p.add_argument("--notion-page-id", default=None)
    p.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    args = p.parse_args(argv)

    summary = ingest(
        pdf_path=args.pdf_path,
        grade=args.grade,
        subject_id=args.subject,
        language=args.language,
        textbook_label=args.label,
        profile=args.profile,
        publisher=args.publisher,
        edition_year=args.edition_year,
        notion_page_id=args.notion_page_id,
        db_path=args.db,
    )
    print(
        f"ingested textbook_id={summary['textbook_id']} "
        f"pages={summary['page_count']} quirk={summary['encoding_quirk']} "
        f"themes={summary['themes_total']} lessons={summary['themes_lessons']}"
    )
    print(f"  kinds: {summary['kinds']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
