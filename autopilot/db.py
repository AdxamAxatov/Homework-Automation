"""SQLite handle + schema initialization for the autopilot homework_db."""
from __future__ import annotations

import sqlite3
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT.parent / "db" / "homework_db.sqlite"
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def connect(db_path: Path | str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path, isolation_level=None)  # autocommit; we manage txns explicitly
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.executescript(sql)


if __name__ == "__main__":
    import sys

    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DB_PATH
    conn = connect(target)
    init_schema(conn)
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    print(f"DB: {target}")
    print("Tables:", ", ".join(r["name"] for r in rows))
    print(
        "Subjects:",
        conn.execute("SELECT count(*) FROM subjects").fetchone()[0],
        "| Grades:",
        conn.execute("SELECT count(*) FROM grades").fetchone()[0],
        "| Languages:",
        conn.execute("SELECT count(*) FROM languages").fetchone()[0],
    )
