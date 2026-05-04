"""Encoding detection / CP1251 mojibake recovery + light text normalization.

Some Russian textbook PDFs in this curriculum (e.g. the 2019 geometry RU edition
from Yangiyo'l poligraf service) store text in legacy Windows-1251 / KOI8-style
fonts that pdftotext misinterprets as Latin-1, producing mojibake like
``Òåìà 1. Ñóììà ...`` instead of ``Тема 1. Сумма ...``.

`recover_cp1251_mojibake` reverses that round-trip when detected. We also expose
a tiny title normalizer used by the matcher.
"""
from __future__ import annotations

import re
import unicodedata


# Bytes a pdftotext extraction emits when the source was actually CP1251
# Cyrillic but the extractor treated each byte as Latin-1, then we read it as
# UTF-8. After that double-mistake every original Cyrillic byte 0x80..0xFF
# becomes a UTF-8 sequence ``0xC2 0x?? `` or ``0xC3 0x??``. The string therefore
# has lots of "Â", "Ã", "Ð" characters and very few legitimate Cyrillic
# letters. We use that as the heuristic.

_MOJIBAKE_HINTS = ("Ã", "Ð", "Î", "Ï", "Ñ", "Ò")
_CYRILLIC_RE = re.compile(r"[Ѐ-ӿ]")


def looks_like_cp1251_mojibake(text: str) -> bool:
    """Heuristic: text has many more mojibake hint chars than real Cyrillic letters.

    We scan the WHOLE text (not just the head) because covers/title pages can
    be rendered in proper Unicode while the body uses CP1251 fonts.
    """
    if not text:
        return False
    hint_count = sum(text.count(c) for c in _MOJIBAKE_HINTS)
    cyrillic_count = len(_CYRILLIC_RE.findall(text))
    return hint_count >= 200 and hint_count >= 10 * cyrillic_count


def recover_cp1251_mojibake(text: str) -> str:
    """Reverse latin-1 -> cp1251 round-trip. Lossy on chars outside Latin-1 (replaced)."""
    return text.encode("latin-1", errors="replace").decode("cp1251", errors="replace")


# Dash-like and quote-like characters that appear in legacy textbook PDFs and
# should normalize to ASCII for matcher / display purposes. The 0x91-0x97 range
# is CP1252 left-overs (smart quotes + en/em-dash) that survive as control chars
# after extraction.
_TEXT_NORMALIZE = str.maketrans({
    chr(0x91): "'",   # CP1252 left single quote
    chr(0x92): "'",   # CP1252 right single quote
    chr(0x93): '"',   # CP1252 left double quote
    chr(0x94): '"',   # CP1252 right double quote
    chr(0x96): "-",   # CP1252 en-dash
    chr(0x97): "-",   # CP1252 em-dash
    chr(0x2018): "'",  # left single quote
    chr(0x2019): "'",  # right single quote
    chr(0x201C): '"',  # left double quote
    chr(0x201D): '"',  # right double quote
    chr(0x02BB): "'",  # modifier letter turned comma (Uzbek O')
    chr(0x02BC): "'",  # modifier letter apostrophe
    chr(0x2010): "-",  # hyphen
    chr(0x2011): "-",  # non-breaking hyphen
    chr(0x2012): "-",  # figure dash
    chr(0x2013): "-",  # en-dash
    chr(0x2014): "-",  # em-dash
    chr(0x2015): "-",  # horizontal bar
    chr(0x2212): "-",  # minus
})


def maybe_recover_text(text: str) -> tuple[str, str | None]:
    """Return (text, encoding_quirk) where encoding_quirk is 'cp1251_mojibake' or None.

    Always:
      * strips soft hyphens (U+00AD) — publisher line-break hints
      * normalizes assorted Unicode dashes, smart quotes, and CP1252 leftovers
    """
    if looks_like_cp1251_mojibake(text):
        text = recover_cp1251_mojibake(text)
        quirk = "cp1251_mojibake"
    else:
        quirk = None
    text = text.replace(chr(0x00AD), "")  # soft hyphens
    text = text.translate(_TEXT_NORMALIZE)
    return text, quirk


# ---------------------------------------------------------------------------
# Title normalization for matcher and de-duplication.
# ---------------------------------------------------------------------------

_PUNCT_RE = re.compile(r"[‐-―‘-‟\"'`.,;:!?()\[\]{}<>«»\\/—–-]+")
_WS_RE = re.compile(r"\s+")


def normalize_title(raw: str) -> str:
    """Lowercase, NFKC-normalize, strip punctuation and collapse whitespace.

    Locale-agnostic — works for Uzbek (Latin) and Russian (Cyrillic) titles.
    """
    s = unicodedata.normalize("NFKC", raw or "").lower()
    s = _PUNCT_RE.sub(" ", s)
    s = _WS_RE.sub(" ", s).strip()
    return s
