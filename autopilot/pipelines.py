"""Pipeline registry — maps (subject, mode) to the ordered list of phases the
worker must run, plus the prompt filename to load for each phase.

Mirrors ``CONTRACTS.md::PHASE_PIPELINE``. If you change CONTRACTS.md you must
update this file (and vice versa). The ``selftest`` function below verifies that
every prompt file referenced here exists in ``repo/server/prompts/<subject>/``.

Why this is hard-coded rather than parsed from each subject's flow.md:
flow.md is human prose with a markdown table that is too easy to break with
formatting changes, while a Python dict is checkable at module load time. The
trade-off is documented in our design review.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PROMPTS_ROOT = REPO_ROOT / "server" / "prompts"


@dataclass(frozen=True)
class PhaseSpec:
    """One step in a build pipeline.

    name        — canonical phase ID (matches CONTRACTS.md PHASE_PIPELINE token)
    prompt_file — markdown file under server/prompts/<subject>/ that defines
                  the worker's rubric. None means the step is orchestrator-only
                  (e.g. classify, extraction).
    can_skip    — phase may legitimately emit a SKIP signal (consolidation only)
    """
    name: str
    prompt_file: str | None
    can_skip: bool = False


# Always-on subject metadata. Must stay aligned with CONTRACTS.md.
SUBJECT_FAMILY: dict[str, str] = {
    "math-algebra":     "aniq-fanlar",
    "geometriya-g7-11": "aniq-fanlar",
    "physics":          "tabiy-fanlar",
    "biology":          "tabiy-fanlar",
    "kimyo-g7-11":      "tabiy-fanlar",
    "english":          "til-fanlar",
    "history":          "ijtimoiy-fanlar",
}

ALWAYS_HARD: frozenset[str] = frozenset({"english", "history"})

# Subjects that require a classifier step before the build branch is decided.
# History and English are always-hard so classification is unnecessary.
NEEDS_CLASSIFY: frozenset[str] = frozenset({
    "math-algebra", "geometriya-g7-11", "physics", "biology", "kimyo-g7-11",
})


# ---------------------------------------------------------------------------
# Per-subject phase pipelines.
# Keys: (subject_id, mode) where mode ∈ {"easy","hard"}.
# Value: ordered list of PhaseSpec — the worker runs them in order.
# ---------------------------------------------------------------------------

# Aniq-fanlar / tabiy-fanlar share the same pipeline shape and use
# split preview-easy.md / preview-hard.md prompts.
_ANIQ_TABIY_EASY = (
    PhaseSpec("preview",         "preview-easy.md"),
    PhaseSpec("flashcards",      "flashcards.md"),
    PhaseSpec("memory_sprint",   "memory-sprint.md"),
    PhaseSpec("game_breaks",     "game-breaks.md"),
    PhaseSpec("reflection",      "reflection.md"),
)

_ANIQ_TABIY_HARD = (
    PhaseSpec("preview",         "preview-hard.md"),
    PhaseSpec("flashcards",      "flashcards.md"),
    PhaseSpec("memory_sprint",   "memory-sprint.md"),
    PhaseSpec("game_breaks",     "game-breaks.md"),
    PhaseSpec("real_life",       "real-life.md"),
    PhaseSpec("consolidation",   "consolidation.md", can_skip=True),
    PhaseSpec("final_challenge", "final-challenge.md"),
    PhaseSpec("reflection",      "reflection.md"),
)

# History uses one preview.md and skips real_life.
_HISTORY_HARD = (
    PhaseSpec("preview",         "preview.md"),
    PhaseSpec("flashcards",      "flashcards.md"),
    PhaseSpec("memory_sprint",   "memory-sprint.md"),
    PhaseSpec("game_breaks",     "game-breaks.md"),
    PhaseSpec("consolidation",   "consolidation.md", can_skip=True),
    PhaseSpec("final_challenge", "final-challenge.md"),
    PhaseSpec("reflection",      "reflection.md"),
)

# English is always-hard, uses preview-hard.md, and adds a reading.md phase
# between memory_sprint and game_breaks.
_ENGLISH_HARD = (
    PhaseSpec("preview",         "preview-hard.md"),
    PhaseSpec("flashcards",      "flashcards.md"),
    PhaseSpec("memory_sprint",   "memory-sprint.md"),
    PhaseSpec("reading",         "reading.md"),
    PhaseSpec("game_breaks",     "game-breaks.md"),
    PhaseSpec("real_life",       "real-life.md"),
    PhaseSpec("consolidation",   "consolidation.md", can_skip=True),
    PhaseSpec("final_challenge", "final-challenge.md"),
    PhaseSpec("reflection",      "reflection.md"),
)


PIPELINES: dict[tuple[str, str], tuple[PhaseSpec, ...]] = {
    ("math-algebra",     "easy"): _ANIQ_TABIY_EASY,
    ("math-algebra",     "hard"): _ANIQ_TABIY_HARD,
    ("geometriya-g7-11", "easy"): _ANIQ_TABIY_EASY,
    ("geometriya-g7-11", "hard"): _ANIQ_TABIY_HARD,
    ("physics",          "easy"): _ANIQ_TABIY_EASY,
    ("physics",          "hard"): _ANIQ_TABIY_HARD,
    ("biology",          "easy"): _ANIQ_TABIY_EASY,
    ("biology",          "hard"): _ANIQ_TABIY_HARD,
    ("kimyo-g7-11",      "easy"): _ANIQ_TABIY_EASY,
    ("kimyo-g7-11",      "hard"): _ANIQ_TABIY_HARD,
    ("history",          "hard"): _HISTORY_HARD,
    ("english",          "hard"): _ENGLISH_HARD,
}


def get_pipeline(subject_id: str, mode: str) -> tuple[PhaseSpec, ...]:
    if subject_id in ALWAYS_HARD and mode != "hard":
        raise ValueError(f"subject {subject_id!r} is always-hard; got mode={mode!r}")
    key = (subject_id, mode)
    if key not in PIPELINES:
        raise KeyError(f"no pipeline for subject={subject_id!r} mode={mode!r}")
    return PIPELINES[key]


def selftest() -> list[str]:
    """Return a list of human-readable error messages. Empty list = all good.

    Verifies that every prompt file referenced by every pipeline exists on disk
    under repo/server/prompts/. Run this in CI and at orchestrator startup.
    """
    errors: list[str] = []
    for (subject, mode), phases in PIPELINES.items():
        subj_dir = PROMPTS_ROOT / subject
        if not subj_dir.is_dir():
            errors.append(f"missing prompt directory: {subj_dir}")
            continue
        instr = subj_dir / "instruction.md"
        if not instr.is_file():
            errors.append(f"missing {instr.relative_to(REPO_ROOT)}")
        if subject in NEEDS_CLASSIFY:
            cls = subj_dir / "classify.md"
            if not cls.is_file():
                errors.append(f"missing {cls.relative_to(REPO_ROOT)}")
        for phase in phases:
            if phase.prompt_file is None:
                continue
            f = subj_dir / phase.prompt_file
            if not f.is_file():
                errors.append(
                    f"missing {f.relative_to(REPO_ROOT)} (referenced by {subject}/{mode}/{phase.name})"
                )
    return errors


if __name__ == "__main__":
    import sys
    errs = selftest()
    if errs:
        print("PIPELINE REGISTRY ERRORS:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    print("OK — all 12 pipelines reference existing prompt files.")
    for (subject, mode), phases in sorted(PIPELINES.items()):
        names = " -> ".join(p.name for p in phases)
        print(f"  {subject:18s} {mode:4s} ({len(phases)} phases): {names}")
