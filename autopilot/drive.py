"""drive.py — autonomous homework-build orchestrator.

Run interactively with no args and the script prompts you for subject, grade,
theme/lesson, language, and textbook PDF (auto-listed from
``Automation/textbooks/``). Or pass everything via CLI flags for headless /
batch use.

The orchestrator itself does NOT call Claude — that happens in
``autopilot.agent_runner.run_plan``, which shells out to
``claude --print --dangerously-skip-permissions --model <model>`` once per
build. The spawned Claude session reads the per-subject prompts under
``server/prompts/<subject>/``, walks the phase flow end-to-end, and writes
``content.json`` to the build dir. After the subprocess exits, drive.py POSTs
that JSON to the running NETS server (``/api/homeworks`` + ``PUT``).

Mode (easy vs hard) is decided by the spawned Claude at build time by reading
``classify.md`` for subjects in ``pipelines.NEEDS_CLASSIFY``. Subjects in
``ALWAYS_HARD`` skip classification and use the hard pipeline.

CLI:
    # Interactive (recommended)
    python -m autopilot.drive build

    # Headless / scripted
    python -m autopilot.drive build --grade 8 --subject biology \\
        --language uz --lesson-ref "Grade 7 Biologiya, §12 Fotosintez" \\
        --pdf textbooks/7-sinf_Biologiya_2024.pdf

    # Inspection / CI
    python -m autopilot.drive build ... --dry-run        # no agents, just DB + folders
    python -m autopilot.drive build ... --planner        # print the plan, exit 0
    python -m autopilot.drive show --homework-id HW-...  # status report
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from . import orchestrator_db as odb
from . import pipelines, runlog, validate

REPO_ROOT = Path(__file__).resolve().parents[2]
AUTOMATION_ROOT = Path(__file__).resolve().parents[1]
BUILDS_ROOT = AUTOMATION_ROOT / "builds"
TEXTBOOKS_ROOT = AUTOMATION_ROOT / "textbooks"
PROMPTS_ROOT = REPO_ROOT / "server" / "prompts"
AGENTS_ROOT = AUTOMATION_ROOT / "autopilot" / "agents"
CONTRACTS_PATH = REPO_ROOT / "CONTRACTS.md"
FIXTURES_ROOT = REPO_ROOT / "fixtures"


# ---------------------------------------------------------------------------
# Build context — what every agent invocation needs
# ---------------------------------------------------------------------------


@dataclass
class BuildContext:
    homework_id: str
    grade: int
    subject_id: str
    language: str
    mode: str  # 'easy' | 'hard'
    lesson_ref: str
    pdf_path: Path
    build_dir: Path
    instruction_path: Path
    fixture_path: Path | None
    textbook_label: str | None = None
    confirmed_phase_paths: list[Path] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Agent-invocation plan — one entry per spawn
# ---------------------------------------------------------------------------


@dataclass
class AgentSpawn:
    """One agent invocation. The agent runner (Openclaw / claude --headless)
    executes this; the orchestrator records before/after into DB + run.log."""
    role: str                      # extractor | classifier | phase_worker | validator | assembler
    phase: str                     # 'extraction' | 'classify' | <phase_name> | 'assembler' | 'validate:<phase>'
    attempt: int                   # 0 for first attempt, 1 for retry
    agent_definition_path: Path    # autopilot/agents/<role>.md
    output_path: Path              # where the agent writes its result
    inputs: dict[str, str]         # named path/string inputs interpolated into the spawn prompt

    def as_jsonl(self) -> str:
        return json.dumps({
            "role": self.role,
            "phase": self.phase,
            "attempt": self.attempt,
            "agent_definition": str(self.agent_definition_path.relative_to(REPO_ROOT)),
            "output_path": str(self.output_path),
            "inputs": self.inputs,
        }, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Plan construction — pure (no IO, no agent calls)
# ---------------------------------------------------------------------------


def plan_pre_classify(ctx: BuildContext) -> list[AgentSpawn]:
    """Steps that run before classification: extractor + its validator."""
    extraction_path = ctx.build_dir / "extraction.md"
    return [
        AgentSpawn(
            role="extractor",
            phase="extraction",
            attempt=0,
            agent_definition_path=AGENTS_ROOT / "extractor.md",
            output_path=extraction_path,
            inputs={
                "PDF_PATH": str(ctx.pdf_path),
                "LESSON_REF": ctx.lesson_ref,
                "SUBJECT": ctx.subject_id,
                "GRADE": str(ctx.grade),
                "LANGUAGE": ctx.language,
                "INSTRUCTION_PATH": str(ctx.instruction_path),
                "OUTPUT_PATH": str(extraction_path),
            },
        ),
        _validator_spawn(
            ctx,
            phase="extraction",
            worker_output=extraction_path,
            rubric=AGENTS_ROOT / "extractor.md",
            attempt=0,
        ),
    ]


def plan_classify(ctx: BuildContext, extraction_path: Path) -> list[AgentSpawn]:
    """Classifier + its validator. Skipped when subject is always-hard."""
    if ctx.subject_id not in pipelines.NEEDS_CLASSIFY:
        return []
    classify_path = ctx.build_dir / "classify.md"
    classify_prompt = PROMPTS_ROOT / ctx.subject_id / "classify.md"
    return [
        AgentSpawn(
            role="classifier",
            phase="classify",
            attempt=0,
            agent_definition_path=AGENTS_ROOT / "classifier.md",
            output_path=classify_path,
            inputs={
                "EXTRACTION_PATH": str(extraction_path),
                "CLASSIFY_PROMPT_PATH": str(classify_prompt),
                "LESSON_REF": ctx.lesson_ref,
                "SUBJECT": ctx.subject_id,
                "OUTPUT_PATH": str(classify_path),
            },
        ),
        _validator_spawn(
            ctx,
            phase="classify",
            worker_output=classify_path,
            rubric=classify_prompt,
            attempt=0,
        ),
    ]


def plan_phase(ctx: BuildContext, phase_idx: int, phase_spec: pipelines.PhaseSpec) -> list[AgentSpawn]:
    """Worker + validator for one phase."""
    extraction_path = ctx.build_dir / "extraction.md"
    output_path = ctx.build_dir / f"phase-{phase_idx}-{phase_spec.name}.md"
    prompt_path = PROMPTS_ROOT / ctx.subject_id / phase_spec.prompt_file  # type: ignore[arg-type]
    return [
        AgentSpawn(
            role="phase_worker",
            phase=phase_spec.name,
            attempt=0,
            agent_definition_path=AGENTS_ROOT / "phase-worker.md",
            output_path=output_path,
            inputs={
                "PHASE_PROMPT_PATH": str(prompt_path),
                "EXTRACTION_PATH": str(extraction_path),
                "INSTRUCTION_PATH": str(ctx.instruction_path),
                "PRIOR_PHASES_PATHS": "\n".join(str(p) for p in ctx.confirmed_phase_paths),
                "LESSON_REF": ctx.lesson_ref,
                "SUBJECT": ctx.subject_id,
                "GRADE": str(ctx.grade),
                "LANGUAGE": ctx.language,
                "MODE": ctx.mode,
                "OUTPUT_PATH": str(output_path),
                "RETRY_FEEDBACK": "",
            },
        ),
        _validator_spawn(
            ctx,
            phase=phase_spec.name,
            worker_output=output_path,
            rubric=prompt_path,
            attempt=0,
        ),
    ]


def plan_assembler(ctx: BuildContext) -> list[AgentSpawn]:
    """Assembler + final validator (schema conformance + master checklist)."""
    json_path = ctx.build_dir / "content.json"
    md_path = ctx.build_dir / "assembled.md"
    return [
        AgentSpawn(
            role="assembler",
            phase="assembler",
            attempt=0,
            agent_definition_path=AGENTS_ROOT / "assembler.md",
            output_path=json_path,
            inputs={
                "BUILD_DIR": str(ctx.build_dir),
                "EXTRACTION_PATH": str(ctx.build_dir / "extraction.md"),
                "CONTRACTS_PATH": str(CONTRACTS_PATH),
                "FIXTURE_PATH": str(ctx.fixture_path) if ctx.fixture_path else "",
                "LESSON_REF": ctx.lesson_ref,
                "SUBJECT": ctx.subject_id,
                "GRADE": str(ctx.grade),
                "LANGUAGE": ctx.language,
                "MODE": ctx.mode,
                "OUTPUT_JSON_PATH": str(json_path),
                "OUTPUT_MD_PATH": str(md_path),
            },
        ),
        _validator_spawn(
            ctx,
            phase="assembler",
            worker_output=json_path,
            rubric=CONTRACTS_PATH,
            attempt=0,
        ),
    ]


def _validator_spawn(
    ctx: BuildContext,
    *,
    phase: str,
    worker_output: Path,
    rubric: Path,
    attempt: int,
) -> AgentSpawn:
    output_path = ctx.build_dir / f"validator-{phase}-attempt{attempt}.md"
    return AgentSpawn(
        role="validator",
        phase=f"validate:{phase}",
        attempt=attempt,
        agent_definition_path=AGENTS_ROOT / "validator.md",
        output_path=output_path,
        inputs={
            "WORKER_OUTPUT_PATH": str(worker_output),
            "RUBRIC_PATH": str(rubric),
            "EXTRACTION_PATH": str(ctx.build_dir / "extraction.md"),
            "INSTRUCTION_PATH": str(ctx.instruction_path),
            "PRIOR_PHASES_PATHS": "\n".join(str(p) for p in ctx.confirmed_phase_paths),
            "PHASE_NAME": phase,
            "LESSON_REF": ctx.lesson_ref,
            "SUBJECT": ctx.subject_id,
            "GRADE": str(ctx.grade),
            "LANGUAGE": ctx.language,
            "MODE": ctx.mode,
            "OUTPUT_PATH": str(output_path),
        },
    )


def fixture_for(subject_id: str, mode: str) -> Path | None:
    """Best-match same-subject fixture under repo/fixtures/. Returns None if absent."""
    candidates = [
        FIXTURES_ROOT / f"{subject_id}-g8-{mode}.json",
        FIXTURES_ROOT / f"{subject_id}-{mode}.json",
        FIXTURES_ROOT / f"{subject_id}.json",
    ]
    for c in candidates:
        if c.is_file():
            return c
    # Fallback: first file matching subject prefix
    for f in sorted(FIXTURES_ROOT.glob(f"{subject_id}-*.json")):
        return f
    return None


# ---------------------------------------------------------------------------
# Top-level commands
# ---------------------------------------------------------------------------


def _interactive_collect(args: argparse.Namespace) -> argparse.Namespace:
    """Fill in any missing build inputs by prompting on stdin.

    Called from cmd_build when the operator runs `python -m autopilot.drive build`
    with no flags. Skips any field that's already set on `args`, so partial CLI
    invocations stay valid (e.g. `--subject biology` then prompts for the rest).
    """
    print("\n=== NETS Autopilot — interactive build ===\n")

    # ---- Subject ----
    if not args.subject:
        subjects = sorted(pipelines.SUBJECT_FAMILY.keys())
        print("Subjects:")
        for i, s in enumerate(subjects, 1):
            family = pipelines.SUBJECT_FAMILY[s]
            tag = " (always-hard)" if s in pipelines.ALWAYS_HARD else ""
            print(f"  {i:2d}. {s:18s}  family={family}{tag}")
        while True:
            raw = input("Subject (number or id): ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(subjects):
                args.subject = subjects[int(raw) - 1]
                break
            if raw in pipelines.SUBJECT_FAMILY:
                args.subject = raw
                break
            print(f"  invalid: {raw!r}")
        print(f"  -> subject = {args.subject}")

    # ---- Grade ----
    if args.grade is None:
        while True:
            raw = input("Grade (1-12): ").strip()
            try:
                g = int(raw)
                if 1 <= g <= 12:
                    args.grade = g
                    break
            except ValueError:
                pass
            print(f"  invalid grade: {raw!r}")
        print(f"  -> grade = {args.grade}")

    # ---- Theme / lesson reference ----
    if not args.lesson_ref:
        print('Theme/lesson reference (e.g. "§12 Fotosintez" or "Ottoman Empire"):')
        while True:
            raw = input("> ").strip()
            if raw:
                args.lesson_ref = raw
                break

    # ---- Language ----
    if not args.language:
        raw = input("Language [uz/ru/en] (default uz): ").strip().lower() or "uz"
        if raw not in ("uz", "ru", "en"):
            print(f"  unknown language {raw!r}; defaulting to uz")
            raw = "uz"
        args.language = raw
        print(f"  -> language = {args.language}")

    # ---- PDF path ----
    if not args.pdf:
        pdfs = sorted(TEXTBOOKS_ROOT.glob("*.pdf")) if TEXTBOOKS_ROOT.is_dir() else []
        if pdfs:
            print(f"\nTextbooks in {TEXTBOOKS_ROOT}:")
            for i, p in enumerate(pdfs, 1):
                size_mb = round(p.stat().st_size / 1024 / 1024, 1)
                print(f"  {i:2d}. {p.name}  ({size_mb} MB)")
            print("   P. paste an absolute path")
        else:
            print(f"  (no PDFs found in {TEXTBOOKS_ROOT}; paste a path)")
        while True:
            raw = input("Pick textbook (number, P, or path): ").strip().strip('"')
            if not raw:
                continue
            if raw.lower() in ("p", "paste"):
                p = Path(input("  Path: ").strip().strip('"'))
                if p.is_file():
                    args.pdf = str(p)
                    break
                print(f"  not a file: {p}")
                continue
            if raw.isdigit() and pdfs and 1 <= int(raw) <= len(pdfs):
                args.pdf = str(pdfs[int(raw) - 1])
                break
            # Try as a literal path
            p = Path(raw)
            if p.is_file():
                args.pdf = str(p)
                break
            print(f"  invalid: {raw!r}")
        print(f"  -> pdf = {args.pdf}")

    # ---- Textbook label (optional, surfaces only if not set) ----
    if args.label is None:
        raw = input("Textbook label (optional, press Enter to skip): ").strip()
        args.label = raw or None

    print()  # spacer before build kicks off
    return args


def cmd_build(args: argparse.Namespace) -> int:
    # ---- Per-worker isolation (convenience for parallel windows) ----
    # `--worker N` derives both --builds-dir and --db when not explicitly set,
    # so each window gets its own filesystem + DB lane.
    if args.worker is not None:
        if args.builds_dir is None:
            args.builds_dir = AUTOMATION_ROOT / f"builds-w{args.worker}"
        if args.db is None:
            args.db = AUTOMATION_ROOT / "db" / f"hw-w{args.worker}.sqlite"

    # Drop into interactive collection if the core fields aren't all set.
    if not (args.subject and args.grade and args.language and args.lesson_ref and args.pdf):
        try:
            args = _interactive_collect(args)
        except (KeyboardInterrupt, EOFError):
            print("\nbuild cancelled.", file=sys.stderr)
            return 130

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.exists():
        print(f"error: PDF not found: {pdf_path}", file=sys.stderr)
        return 2

    # Resolve the final builds-dir: --builds-dir flag → NETS_BUILDS_DIR env → default
    builds_root = (
        Path(args.builds_dir).resolve() if args.builds_dir
        else Path(os.environ["NETS_BUILDS_DIR"]).resolve() if os.environ.get("NETS_BUILDS_DIR")
        else BUILDS_ROOT
    )
    builds_root.mkdir(parents=True, exist_ok=True)

    # Pipeline registry self-test before any DB writes — catches missing prompts early.
    errs = pipelines.selftest()
    if errs:
        print("pipeline registry errors (orchestrator refuses to start):", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 3

    # Mode is a placeholder for the autopilot DB. The agent decides the real
    # mode at build time by reading classify.md (for NEEDS_CLASSIFY subjects)
    # and writes the verdict into content.json.meta.mode. We seed with the
    # superset (hard) so plan_phase()'s pre-classify plan listing is complete
    # — the agent ignores phases its classify verdict eliminates.
    mode = "hard"

    instruction_path = PROMPTS_ROOT / args.subject / "instruction.md"
    if not instruction_path.is_file():
        print(f"error: missing instruction.md for subject {args.subject!r}: {instruction_path}", file=sys.stderr)
        return 3

    # DB setup + manual theme_link bootstrap
    conn = odb.open_db(args.db)
    theme_link_id = odb.ensure_manual_theme_link(
        conn,
        grade_id=args.grade,
        subject_id=args.subject,
        textbook_label=args.label,
        language=args.language,
        raw_title=args.lesson_ref,
    )
    homework_id = odb.create_homework(
        conn,
        grade_id=args.grade,
        subject_id=args.subject,
        theme_link_id=theme_link_id,
        mode=mode,
    )

    build_dir = builds_root / homework_id
    build_dir.mkdir(parents=True, exist_ok=True)
    log = runlog.RunLog(build_dir)
    log.event(
        "homework_created",
        homework_id=homework_id,
        grade=args.grade,
        subject=args.subject,
        language=args.language,
        mode=mode,
        lesson_ref=args.lesson_ref,
        pdf=str(pdf_path),
        build_dir=str(build_dir),
        theme_link_id=theme_link_id,
    )

    ctx = BuildContext(
        homework_id=homework_id,
        grade=args.grade,
        subject_id=args.subject,
        language=args.language,
        mode=mode,
        lesson_ref=args.lesson_ref,
        pdf_path=pdf_path,
        build_dir=build_dir,
        instruction_path=instruction_path,
        fixture_path=fixture_for(args.subject, mode),
        textbook_label=args.label,
    )

    # ----- Build the agent invocation plan -----
    plan: list[AgentSpawn] = []
    plan.extend(plan_pre_classify(ctx))
    plan.extend(plan_classify(ctx, ctx.build_dir / "extraction.md"))
    # Phase steps depend on classifier verdict at runtime; pre-classify mode
    # gives us a default plan we can re-shape after classify executes. The
    # planner mode below prints the default-mode plan so operators can see the
    # full shape; the actual runtime adjusts after classify.
    pipeline = pipelines.get_pipeline(args.subject, mode)
    for idx, spec in enumerate(pipeline, start=1):
        plan.extend(plan_phase(ctx, idx, spec))
    plan.extend(plan_assembler(ctx))

    # ----- Dispatch -----
    if args.planner:
        print(f"# Plan for {homework_id} ({args.subject} g{args.grade} {args.language} {mode})")
        print(f"# {len(plan)} agent invocations")
        for spawn in plan:
            print(spawn.as_jsonl())
        odb.set_homework_status(conn, homework_id, "queued",
                                last_error="planner-mode: no agents invoked")
        return 0

    if args.dry_run:
        # Mark each step as 'done' + 'confirmed' for state tracking, but never
        # call any agent. Used to verify DB writes + folder layout in CI.
        odb.set_homework_status(conn, homework_id, "extracting", current_phase="extraction")
        for spawn in plan:
            if spawn.role == "validator":
                continue  # validators are paired with their workers; we record one phase_run per worker
            phase_run_id = odb.start_phase_run(
                conn,
                homework_id=homework_id,
                language=args.language,
                phase=spawn.phase,
                attempt=spawn.attempt,
            )
            odb.record_phase_result(
                conn,
                phase_run_id=phase_run_id,
                status="done",
                validator_state="confirmed",
                output_excerpt=f"[dry-run] {spawn.role}: {spawn.output_path.name}",
            )
            log.event("agent_spawn", role=spawn.role, phase=spawn.phase,
                      attempt=spawn.attempt, dry_run=True)
            log.event("verdict", phase=spawn.phase, attempt=spawn.attempt,
                      verdict="confirmed", dry_run=True)
        odb.set_homework_status(conn, homework_id, "ready")
        log.event("homework_ready", homework_id=homework_id, dry_run=True)
        print(f"[dry-run] homework {homework_id} would invoke {len(plan)} agents.")
        print(f"[dry-run] state recorded; build dir: {build_dir}")
        return 0

    # ----- Live mode: hand off to the subprocess driver in agent_runner -----
    from .agent_runner import run_plan

    api_url = args.api_url or os.environ.get("NETS_API_URL", "http://sigmaai.local:8000")
    model = args.model or "claude-opus-4-7"
    return run_plan(
        conn=conn,
        ctx=ctx,
        plan=plan,
        log=log,
        model=model,
        api_url=api_url,
    )


def cmd_show(args: argparse.Namespace) -> int:
    conn = odb.open_db(args.db)
    hw = conn.execute("SELECT * FROM homeworks WHERE id=?", (args.homework_id,)).fetchone()
    if hw is None:
        print(f"unknown homework_id: {args.homework_id}", file=sys.stderr)
        return 1
    print(f"=== {hw['id']} ===")
    for k in ("grade_id", "subject_id", "mode", "status", "current_phase",
              "attempts", "last_error", "created_at", "updated_at"):
        print(f"  {k:14s}: {hw[k]}")
    print()
    print("=== phase_runs ===")
    for r in conn.execute(
        """SELECT phase, attempts, status, validator_state, started_at, finished_at, output_excerpt
           FROM phase_runs WHERE homework_id=? ORDER BY id""",
        (args.homework_id,),
    ):
        print(f"  {r['phase']:18s} attempt={r['attempts']} status={r['status']:8s} "
              f"validator={r['validator_state']:10s} started={r['started_at']}")
        if r["output_excerpt"]:
            print(f"     -> {r['output_excerpt']}")
    pl = conn.execute(
        "SELECT language, schema_version, validated_at, validator_score FROM homework_payloads WHERE homework_id=?",
        (args.homework_id,),
    ).fetchall()
    if pl:
        print()
        print("=== homework_payloads ===")
        for p in pl:
            print(f"  language={p['language']} schema={p['schema_version']} "
                  f"validated={p['validated_at']} score={p['validator_score']}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="NETS Autopilot — autonomous homework build orchestrator")
    sub = p.add_subparsers(dest="cmd", required=True)

    pb = sub.add_parser("build", help="build one homework end-to-end")
    pb.add_argument("--grade", type=int, default=None,
                    help="grade 1-12 (interactive prompt if omitted)")
    pb.add_argument("--subject", default=None,
                    help="CONTRACTS.md subject id (interactive prompt if omitted)")
    pb.add_argument("--language", choices=["uz", "ru", "en"], default=None,
                    help="content language (interactive prompt if omitted)")
    pb.add_argument("--lesson-ref", default=None,
                    help="canonical lesson reference, e.g. \"§15 Bir noma'lumli tengsizliklar\"")
    pb.add_argument("--pdf", default=None, help="path to the textbook PDF")
    pb.add_argument("--label", default=None, help="textbook label (e.g. 'Jahon Tarixi' for history)")
    pb.add_argument("--api-url", default=None,
                    help="NETS server base URL (env NETS_API_URL or http://sigmaai.local:8000)")
    pb.add_argument("--model", default=None,
                    help="Claude CLI model id (default claude-opus-4-7)")
    pb.add_argument("--db", type=Path, default=None, help="override homework_db.sqlite path")
    pb.add_argument("--builds-dir", type=Path, default=None,
                    help="override the directory where build dirs are created (default: Automation/builds/). "
                         "Use distinct values for parallel runs to avoid filesystem collisions.")
    pb.add_argument("--worker", type=int, default=None,
                    help="convenience flag for parallel windows: sets --builds-dir to "
                         "Automation/builds-w<N>/ and --db to Automation/db/hw-w<N>.sqlite "
                         "(only when those flags aren't already set). Pass distinct N per window.")
    pb.add_argument("--dry-run", action="store_true",
                    help="record DB rows + create folders but invoke no agents")
    pb.add_argument("--planner", action="store_true",
                    help="print the agent invocation plan as JSONL and exit")
    pb.set_defaults(func=cmd_build)

    ps = sub.add_parser("show", help="status report for one homework")
    ps.add_argument("--homework-id", required=True)
    ps.add_argument("--db", type=Path, default=None)
    ps.set_defaults(func=cmd_show)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
