"""Append-only run log per build folder.

Every agent invocation, every verdict, every status transition records one
line. Format is human-readable JSONL — easy to tail, easy to grep, easy to
post-process if we ever want to compute fleet-level metrics.

The log lives at ``<build_dir>/run.log``. It is the single source of truth
for "what did the orchestrator do during this build" — the DB has the
*current* state, the run log has the *history*.
"""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class RunLog:
    """Append-only event log for one build."""

    def __init__(self, build_dir: Path) -> None:
        self.path = Path(build_dir) / "run.log"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def event(self, kind: str, **fields: Any) -> None:
        """Write one event line.

        Standard fields the orchestrator emits:
          - kind='homework_created' homework_id, grade, subject, language, lesson_ref
          - kind='status_change' from, to
          - kind='agent_spawn' role, phase, attempt, prompt_chars, paths
          - kind='agent_complete' role, phase, attempt, output_path, output_chars
          - kind='verdict' phase, attempt, verdict, reasons, fixes
          - kind='retry' phase, reason
          - kind='halt' reason
          - kind='homework_ready' homework_id, payload_path
        """
        record = {"ts": datetime.now(UTC).isoformat(timespec="seconds"), "kind": kind, **fields}
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
