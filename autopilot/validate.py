"""Validator verdict parsing + retry policy.

The validator agent (``autopilot/agents/validator.md``) writes a markdown file
whose first non-empty line is one of:

    VERDICT: confirmed
    VERDICT: rejected_with_fixes
    VERDICT: rejected

Followed by ``## Reasons`` and (for ``rejected_with_fixes``) ``## Fixes``.

This module parses that file into a typed verdict and exposes the orchestrator's
retry policy: **one retry per phase** on ``rejected_with_fixes``; halt on
``rejected`` or on second rejection.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

VerdictKind = Literal["confirmed", "rejected_with_fixes", "rejected"]

MAX_RETRIES = 1  # one retry per phase max — see drive.py


@dataclass(frozen=True)
class Verdict:
    kind: VerdictKind
    reasons: list[str]
    fixes: list[str]
    raw_path: Path

    @property
    def passed(self) -> bool:
        return self.kind == "confirmed"

    @property
    def retryable(self) -> bool:
        return self.kind == "rejected_with_fixes"


_VERDICT_RE = re.compile(r"^VERDICT:\s*(confirmed|rejected_with_fixes|rejected)\s*$", re.MULTILINE)
_REASONS_RE = re.compile(r"^##\s+Reasons\s*$", re.MULTILINE)
_FIXES_RE = re.compile(r"^##\s+Fixes\s*$", re.MULTILINE)


def parse_verdict(path: Path) -> Verdict:
    """Parse the validator's output markdown file. Raises on malformed verdicts."""
    text = path.read_text(encoding="utf-8")

    m = _VERDICT_RE.search(text)
    if not m:
        raise ValueError(
            f"validator file {path} has no parseable VERDICT line — "
            f"expected one of: 'VERDICT: confirmed', 'VERDICT: rejected_with_fixes', 'VERDICT: rejected'"
        )
    kind: VerdictKind = m.group(1)  # type: ignore[assignment]

    reasons = _extract_section(text, _REASONS_RE)
    fixes = _extract_section(text, _FIXES_RE)

    if kind == "rejected_with_fixes" and not fixes:
        raise ValueError(
            f"validator file {path} returned 'rejected_with_fixes' but no '## Fixes' section found"
        )

    return Verdict(kind=kind, reasons=reasons, fixes=fixes, raw_path=path)


def _extract_section(text: str, header_re: re.Pattern[str]) -> list[str]:
    """Pull bullet items from a `## <Header>` section until the next `## ` header or EOF."""
    m = header_re.search(text)
    if not m:
        return []
    body = text[m.end() :]
    next_header = re.search(r"^##\s+", body, re.MULTILINE)
    if next_header:
        body = body[: next_header.start()]
    items: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("- ", "* ", "• ")):
            items.append(stripped[2:].strip())
        elif items and (stripped[0].isalpha() or stripped[0].isdigit()):
            # Continuation line — append to previous bullet.
            items[-1] = items[-1] + " " + stripped
    return items


def format_retry_feedback(verdict: Verdict) -> str:
    """Render a verdict's reasons + fixes as the ``RETRY_FEEDBACK`` payload the
    phase-worker agent receives on its second attempt."""
    lines = ["The validator rejected your previous attempt. Address every fix below verbatim, then re-emit the phase output to the same OUTPUT_PATH."]
    if verdict.fixes:
        lines.append("")
        lines.append("## Required fixes")
        lines.extend(f"- {f}" for f in verdict.fixes)
    if verdict.reasons:
        lines.append("")
        lines.append("## Reasons cited")
        lines.extend(f"- {r}" for r in verdict.reasons)
    return "\n".join(lines)
