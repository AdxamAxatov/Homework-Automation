-- NETS Autopilot — homework_db schema (SQLite)
-- Multilayered: grades > subjects > textbooks > themes > theme_links > homeworks > homework_payloads
-- Operational metadata only. The live nets.db remains the source of truth for served homeworks.

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- ============================================================================
-- Reference tables
-- ============================================================================

CREATE TABLE IF NOT EXISTS grades (
    id    INTEGER PRIMARY KEY,
    label TEXT NOT NULL UNIQUE         -- '1','2',...,'11'
);

CREATE TABLE IF NOT EXISTS subjects (
    id            TEXT PRIMARY KEY,    -- matches CONTRACTS.md::SUBJECTS slug
    family        TEXT NOT NULL,       -- aniq-fanlar | tabiy-fanlar | til-fanlar | ijtimoiy-fanlar
    always_hard   INTEGER NOT NULL DEFAULT 0,
    coverage_mode TEXT NOT NULL CHECK (coverage_mode IN ('bilingual_distinct','monolingual_shared','pending'))
);

CREATE TABLE IF NOT EXISTS languages (
    code TEXT PRIMARY KEY              -- 'uz' | 'ru'
);

-- ============================================================================
-- Sources: one row per textbook PDF
-- ============================================================================

CREATE TABLE IF NOT EXISTS textbooks (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    grade_id            INTEGER NOT NULL REFERENCES grades(id),
    subject_id          TEXT    NOT NULL REFERENCES subjects(id),
    language            TEXT             REFERENCES languages(code),  -- NULL for monolingual_shared
    textbook_label      TEXT,                                          -- distinguishes 'O''zbekiston Tarixi' vs 'Jahon Tarixi' within `history`; NULL otherwise
    file_path           TEXT    NOT NULL UNIQUE,
    publisher           TEXT,
    edition_year        INTEGER,
    page_count          INTEGER,
    encoding_quirk      TEXT,                                          -- e.g. 'cp1251_mojibake'
    notion_page_id      TEXT,
    themes_extracted_at TEXT,                                          -- ISO 8601
    created_at          TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_textbooks_lookup ON textbooks(grade_id, subject_id, language);

-- ============================================================================
-- Theme registry — extracted from each textbook's TOC
-- ============================================================================

CREATE TABLE IF NOT EXISTS themes (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    textbook_id      INTEGER NOT NULL REFERENCES textbooks(id) ON DELETE CASCADE,
    chapter_ordinal  TEXT,                  -- 'I','II',... or NULL for flat
    chapter_title    TEXT,
    section_ordinal  TEXT,                  -- '§1','§2',... or NULL
    section_title    TEXT,
    ordinal_start    INTEGER NOT NULL,      -- 11 for '11-mavzu'; 5 for '5-6-mavzu'
    ordinal_end      INTEGER NOT NULL,      -- 11 normal; 6 for bundled '5-6-mavzu'
    raw_title        TEXT NOT NULL,
    normalized_title TEXT NOT NULL,
    start_page       INTEGER NOT NULL,
    theme_kind       TEXT NOT NULL CHECK (theme_kind IN
                       ('lesson','control_work','test','historical_aside','practical_exercise','appendix','answers','intro','review','unit'))
);

CREATE INDEX IF NOT EXISTS idx_themes_lookup       ON themes(textbook_id, ordinal_start, start_page);
CREATE INDEX IF NOT EXISTS idx_themes_kind         ON themes(textbook_id, theme_kind);
CREATE INDEX IF NOT EXISTS idx_themes_normalized   ON themes(normalized_title);

-- ============================================================================
-- Cross-language theme alignment
-- One row per logical lesson; for bilingual_distinct subjects this joins UZ↔RU themes.
-- ============================================================================

CREATE TABLE IF NOT EXISTS theme_links (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    grade_id          INTEGER NOT NULL REFERENCES grades(id),
    subject_id        TEXT    NOT NULL REFERENCES subjects(id),
    textbook_label    TEXT,                              -- distinguishes textbooks within multi-textbook subjects (history)
    uz_theme_id       INTEGER REFERENCES themes(id),
    ru_theme_id       INTEGER REFERENCES themes(id),
    match_status      TEXT NOT NULL CHECK (match_status IN ('matched','uz_only','ru_only','reordered','unconfirmed')),
    match_method      TEXT NOT NULL CHECK (match_method IN ('ordinal_page_exact','ordinal_only','translation_fuzzy','manual','single_source')),
    match_confidence  REAL NOT NULL DEFAULT 0.0,
    validator_state   TEXT NOT NULL DEFAULT 'proposed' CHECK (validator_state IN ('proposed','confirmed','rejected')),
    validator_notes   TEXT,
    created_at        TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at        TEXT NOT NULL DEFAULT (datetime('now')),
    -- One language-specific theme participates in at most one link per (subject, textbook_label).
    UNIQUE (subject_id, textbook_label, uz_theme_id),
    UNIQUE (subject_id, textbook_label, ru_theme_id)
);

CREATE INDEX IF NOT EXISTS idx_theme_links_routing ON theme_links(grade_id, subject_id, validator_state);

-- ============================================================================
-- Homework lifecycle (the orchestrator's job queue)
-- ============================================================================

CREATE TABLE IF NOT EXISTS homeworks (
    id              TEXT PRIMARY KEY,                 -- 'HW-20260502-001' (matches nets.db convention)
    grade_id        INTEGER NOT NULL REFERENCES grades(id),
    subject_id      TEXT    NOT NULL REFERENCES subjects(id),
    theme_link_id   INTEGER NOT NULL REFERENCES theme_links(id),
    mode            TEXT    NOT NULL CHECK (mode IN ('easy','hard')),
    status          TEXT    NOT NULL CHECK (status IN
                      ('queued','extracting','building','validating','ready','error','patched')),
    attempts        INTEGER NOT NULL DEFAULT 0,
    current_phase   TEXT,
    last_error      TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_homeworks_status ON homeworks(status, created_at);

-- ============================================================================
-- Homework payloads — one per (homework, language)
-- For monolingual_shared subjects there is exactly one row.
-- ============================================================================

CREATE TABLE IF NOT EXISTS homework_payloads (
    id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    homework_id              TEXT    NOT NULL REFERENCES homeworks(id) ON DELETE CASCADE,
    language                 TEXT    NOT NULL REFERENCES languages(code),
    content_json             TEXT,                                  -- the CONTRACTS.md schema payload
    schema_version           TEXT,
    validated_at             TEXT,
    validator_score          REAL,
    validator_notes          TEXT,
    patched_to_nets_db_at    TEXT,
    UNIQUE (homework_id, language)
);

-- ============================================================================
-- Per-phase audit (resume-from-where-we-left-off)
-- ============================================================================

CREATE TABLE IF NOT EXISTS phase_runs (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    homework_id     TEXT NOT NULL REFERENCES homeworks(id) ON DELETE CASCADE,
    language        TEXT NOT NULL REFERENCES languages(code),
    phase           TEXT NOT NULL,                                  -- '0a-preview' .. '7-reflection'
    status          TEXT NOT NULL CHECK (status IN ('pending','running','done','failed')),
    attempts        INTEGER NOT NULL DEFAULT 0,
    output_excerpt  TEXT,
    validator_state TEXT NOT NULL DEFAULT 'proposed' CHECK (validator_state IN ('proposed','confirmed','rejected')),
    started_at      TEXT,
    finished_at     TEXT,
    UNIQUE (homework_id, language, phase, attempts)
);

CREATE INDEX IF NOT EXISTS idx_phase_runs_progress ON phase_runs(homework_id, language, phase);

-- ============================================================================
-- Seed the reference tables
-- ============================================================================

INSERT OR IGNORE INTO languages(code) VALUES ('uz'), ('ru');

INSERT OR IGNORE INTO grades(id, label) VALUES
    (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),
    (6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11');

-- Mirrors CONTRACTS.md::SUBJECTS, SUBJECT_TO_FAMILY, ALWAYS_HARD.
INSERT OR IGNORE INTO subjects(id, family, always_hard, coverage_mode) VALUES
    ('math-algebra',     'aniq-fanlar',     0, 'bilingual_distinct'),
    ('geometriya-g7-11', 'aniq-fanlar',     0, 'bilingual_distinct'),
    ('physics',          'tabiy-fanlar',    0, 'bilingual_distinct'),
    ('biology',          'tabiy-fanlar',    0, 'bilingual_distinct'),
    ('kimyo-g7-11',      'tabiy-fanlar',    0, 'bilingual_distinct'),
    ('english',          'til-fanlar',      1, 'monolingual_shared'),
    ('history',          'ijtimoiy-fanlar', 1, 'bilingual_distinct');
