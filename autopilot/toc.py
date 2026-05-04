"""TOC extraction from textbook PDFs.

Two extraction profiles map to the structural patterns we observed in the G8 corpus:

* **flat** — history-style books with a single ``MUNDARIJA / СОДЕРЖАНИЕ`` listing
  whose lines look like ``11-mavzu. Title ............. 66`` or
  ``Тема 11. Title ............. 66``.

* **three_level** — math/geometry-style books with a 3-level hierarchy
  ``BOB / Глава → § → mavzu / Тема``, including bundled lessons such as
  ``5-6-mavzu`` and ancillary lines like ``Тест``, ``Контрольная работа``,
  ``Исторические сведения`` that we tag with ``theme_kind`` other than
  ``lesson`` so the orchestrator skips them.

The extractor reads the PDF as text via ``pypdf``, applies CP1251 mojibake
recovery if needed, locates the TOC marker, then parses lines.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .textwork import maybe_recover_text, normalize_title


# ---------------------------------------------------------------------------
# Public dataclass — one row per parsed TOC entry
# ---------------------------------------------------------------------------


@dataclass
class TocEntry:
    chapter_ordinal: str | None
    chapter_title: str | None
    section_ordinal: str | None
    section_title: str | None
    ordinal_start: int
    ordinal_end: int
    raw_title: str
    normalized_title: str
    start_page: int
    theme_kind: str  # lesson | control_work | test | historical_aside | practical_exercise | appendix | answers | intro | review | unit


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------


def _require(binary: str) -> str:
    found = shutil.which(binary)
    if not found:
        raise RuntimeError(f"{binary!r} not found on PATH (install poppler: `brew install poppler`)")
    return found


def read_pdf_text(pdf_path: Path) -> tuple[str, str | None, int]:
    """Return (full_text, encoding_quirk, page_count) by shelling out to poppler.

    pypdf's ``extract_text`` loses TOC layout on these multi-column textbooks.
    ``pdftotext -layout`` preserves dot-leader alignment so the line-based parser
    can find ``Title ........ 66`` reliably. ``pdfinfo`` gives the page count.
    """
    pdftotext = _require("pdftotext")
    pdfinfo = _require("pdfinfo")

    out = subprocess.run(
        [pdftotext, "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
        check=True,
        capture_output=True,
    )
    text = out.stdout.decode("utf-8", errors="replace")
    text, quirk = maybe_recover_text(text)

    info = subprocess.run([pdfinfo, str(pdf_path)], check=True, capture_output=True, text=True)
    page_count = 0
    for line in info.stdout.splitlines():
        if line.startswith("Pages:"):
            page_count = int(line.split(":", 1)[1].strip())
            break
    return text, quirk, page_count


# Markers that delimit the TOC section in either language.
_TOC_MARKERS_RE = re.compile(r"^\s*(MUNDARIJA|СОДЕРЖАНИЕ|ОГЛАВЛЕНИЕ|MUNDARÎJA)\b", re.MULTILINE)


def _slice_toc(text: str) -> str:
    """Return the substring starting at the TOC marker through end-of-text or the next form-feed-bounded section.

    If no marker is found, return the full text (some books inline lessons without
    a labeled TOC; the per-line parser is robust to that).
    """
    match = _TOC_MARKERS_RE.search(text)
    if not match:
        return text
    return text[match.start() :]


# Per-line parsing patterns. Each captures: ordinal_start, optional ordinal_end,
# title, dot-leader, page number. Whitespace and unicode dashes are tolerated.

_DASH = r"[‐-―\-]"
_TITLE_BODY = r"(?P<title>.+?)"
_DOT_LEADER = r"[.…\s]+"  # supports both "..." and "…"
_PAGE = r"(?P<page>\d{1,4})"

# History flat: "11-mavzu." or "11- mavzu." (UZ); "Тема 11."; "Темы 5-6." (RU bundled)
_RE_UZ_MAVZU = re.compile(
    rf"^\s*(?P<a>\d+)\s*(?:{_DASH}\s*(?P<b>\d+))?\s*-\s*mavzu\.?\s*{_TITLE_BODY}{_DOT_LEADER}{_PAGE}\s*$",
    re.IGNORECASE,
)
_RE_RU_TEMA = re.compile(
    rf"^\s*Тем(?:а|ы)\s+(?P<a>\d+)(?:\s*{_DASH}\s*(?P<b>\d+))?\.?\s*{_TITLE_BODY}{_DOT_LEADER}{_PAGE}\s*$",
    re.IGNORECASE,
)

# Chapter and section headers (geometry-style)
_RE_BOB = re.compile(rf"^\s*(?P<ord>[IVX]+)\s*BOB\.?\s*(?P<title>.+?)\s*{_DOT_LEADER}{_PAGE}\s*$")
_RE_GLAVA = re.compile(rf"^\s*Глава\s+(?P<ord>[IVX0-9]+)\.?\s*(?P<title>.+?)\s*{_DOT_LEADER}{_PAGE}\s*$", re.IGNORECASE)

# Ancillary kinds — pages we DO record but tag as non-lesson so the orchestrator skips them.
_NONLESSON_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^\s*(\d+\s*-?\s*)?test\b.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "test"),
    (re.compile(r"^\s*Тест\s*\d*.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "test"),
    (re.compile(r"^\s*tarixiy\s+ma'lumotlar.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "historical_aside"),
    (re.compile(r"^\s*Историчес.*?сведения.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "historical_aside"),
    (re.compile(r"^\s*nazorat\s+ishi.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "control_work"),
    (re.compile(r"^\s*Контрольная\s+работа.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "control_work"),
    (re.compile(r"^\s*Ilova\b.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "appendix"),
    (re.compile(r"^\s*Приложение.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "appendix"),
    (re.compile(r"^\s*Javoblar\b.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "answers"),
    (re.compile(r"^\s*Ответы\b.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "answers"),
    (re.compile(r"^\s*Kirish\b.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "intro"),
    (re.compile(r"^\s*Введение\b.*?" + _DOT_LEADER + _PAGE, re.IGNORECASE), "intro"),
]


def _classify_nonlesson(line: str) -> str | None:
    for pat, kind in _NONLESSON_PATTERNS:
        if pat.search(line):
            return kind
    return None


# Kind hints checked AGAINST a parsed lesson's title — flips e.g. a
# "13-14-mavzu. 1-nazorat ishi" row from 'lesson' to 'control_work'.
_TITLE_KIND_HINTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bnazorat\s+ishi\b", re.IGNORECASE), "control_work"),
    (re.compile(r"Контрольная\s+работа", re.IGNORECASE), "control_work"),
    (re.compile(r"Yakuniy\s+nazorat", re.IGNORECASE), "control_work"),
    (re.compile(r"Итоговая\s+контроль", re.IGNORECASE), "control_work"),
    (re.compile(r"\bAmaliy\s+mashq\b", re.IGNORECASE), "practical_exercise"),
    (re.compile(r"\bПрактическ\w+\s+задани", re.IGNORECASE), "practical_exercise"),
    (re.compile(r"\btest\b\s*\d", re.IGNORECASE), "test"),
    (re.compile(r"\bТест\b\s*\d", re.IGNORECASE), "test"),
]


def _refine_lesson_kind(title: str) -> str:
    for pat, kind in _TITLE_KIND_HINTS:
        if pat.search(title):
            return kind
    return "lesson"


def parse_toc(text: str, profile: str) -> list[TocEntry]:
    """profile in {'flat','three_level','auto'}.

    auto picks ``three_level`` if a ``BOB`` or ``Глава`` header is present in the
    sliced TOC; otherwise ``flat``.
    """
    toc = _slice_toc(text)

    if profile == "auto":
        profile = "three_level" if (_RE_BOB.search(toc) or _RE_GLAVA.search(toc)) else "flat"

    entries: list[TocEntry] = []
    cur_chapter_ord: str | None = None
    cur_chapter_title: str | None = None
    cur_section_ord: str | None = None
    cur_section_title: str | None = None

    # Pre-glue wrapped lines: a TOC line that contains a lesson/section/chapter
    # marker but does NOT end with whitespace+digits is almost certainly wrapped
    # to its successor. Concatenate (with a single space) so the regex sees the
    # canonical "Title ........... NN" shape.
    raw_lines = [l.rstrip() for l in toc.splitlines()]
    # Only glue lesson markers — chapter/section headers can legitimately span
    # multiple lines without page numbers and gluing them eats the next Тема.
    wrap_marker_re = re.compile(r"(?:mavzu|Тем(?:а|ы))", re.IGNORECASE)
    # Page tail: optional dot-leader run, then 1-4 digits, then optional trailing
    # whitespace. Some publishers omit the space between the leader and the page
    # number, so allow either ``.`` or whitespace immediately before the digits.
    page_tail_re = re.compile(r"[.\s]\d{1,4}\s*$")
    # Walk forward up to 3 continuation lines, but stop if the next line is
    # itself a lesson/chapter/section marker — that'd mean cur's page truly
    # isn't there and we should leave it un-glued (regex will skip it).
    glued: list[str] = []
    i = 0
    while i < len(raw_lines):
        cur = raw_lines[i]
        if cur.strip() and wrap_marker_re.search(cur) and not page_tail_re.search(cur):
            consumed = 0
            j = i + 1
            new = cur
            while j < len(raw_lines) and consumed < 3:
                nxt = raw_lines[j]
                if not nxt.strip():
                    j += 1
                    continue
                # If the next line opens a new lesson/chapter/section, abort glue.
                if wrap_marker_re.search(nxt) or re.match(r"^\s*(?:[IVX]+\s*BOB|Глава\s+[IVX0-9]+|\d+\s*-?\s*§|§\s*\d+)\b", nxt):
                    break
                new = new + " " + nxt.strip()
                consumed += 1
                if page_tail_re.search(new):
                    break
                j += 1
            if page_tail_re.search(new):
                glued.append(new)
                i = j + 1
                continue
        glued.append(cur)
        i += 1

    for raw_line in glued:
        line = raw_line
        if not line.strip():
            continue

        # Chapter headers (only meaningful in three_level mode but harmless in flat).
        if profile == "three_level":
            m = _RE_BOB.match(line) or _RE_GLAVA.match(line)
            if m:
                cur_chapter_ord = m.group("ord")
                cur_chapter_title = m.group("title").strip()
                cur_section_ord = None
                cur_section_title = None
                continue
            sec = re.match(rf"^\s*(?P<ord>\d+\s*-?\s*§|§\s*\d+)\.?\s*(?P<title>.+?)\s*{_DOT_LEADER}{_PAGE}\s*$", line)
            if sec:
                cur_section_ord = sec.group("ord").replace(" ", "")
                cur_section_title = sec.group("title").strip()
                continue

        # Lesson lines
        m = _RE_UZ_MAVZU.match(line) or _RE_RU_TEMA.match(line)
        if m:
            ord_a = int(m.group("a"))
            ord_b = int(m.group("b")) if m.group("b") else ord_a
            title = m.group("title").strip()
            page = int(m.group("page"))
            entries.append(
                TocEntry(
                    chapter_ordinal=cur_chapter_ord,
                    chapter_title=cur_chapter_title,
                    section_ordinal=cur_section_ord,
                    section_title=cur_section_title,
                    ordinal_start=ord_a,
                    ordinal_end=ord_b,
                    raw_title=title,
                    normalized_title=normalize_title(title),
                    start_page=page,
                    theme_kind=_refine_lesson_kind(title),
                )
            )
            continue

        # Non-lesson rows we still record (rare, but keeps the TOC complete)
        kind = _classify_nonlesson(line)
        if kind is not None:
            page_match = re.search(rf"{_DOT_LEADER}{_PAGE}\s*$", line)
            if page_match:
                # Use a sentinel negative ordinal so ordinal_page_exact matching
                # never picks ancillary rows up against a real lesson.
                page = int(page_match.group("page"))
                entries.append(
                    TocEntry(
                        chapter_ordinal=cur_chapter_ord,
                        chapter_title=cur_chapter_title,
                        section_ordinal=cur_section_ord,
                        section_title=cur_section_title,
                        ordinal_start=-len(entries) - 1,
                        ordinal_end=-len(entries) - 1,
                        raw_title=line.strip(),
                        normalized_title=normalize_title(line),
                        start_page=page,
                        theme_kind=kind,
                    )
                )

    return entries


# ---------------------------------------------------------------------------
# Convenience
# ---------------------------------------------------------------------------


def extract_textbook(pdf_path: Path, profile: str = "auto") -> tuple[list[TocEntry], str | None, int]:
    """Read a PDF, extract its TOC, return (entries, encoding_quirk, page_count)."""
    text, quirk, page_count = read_pdf_text(pdf_path)
    entries = parse_toc(text, profile=profile)
    return entries, quirk, page_count
