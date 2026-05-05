"""Subprocess driver for the autonomous build.

drive.py builds the BuildContext + an inspectable phase plan, then hands off to
``run_plan`` here. We compose ONE thin master prompt that routes the spawned
Claude session to the per-subject prompts under ``Automation/prompts/<subject>/``
in their correct order, have it write ``content.json`` to the build dir, then
POST + PUT that JSON to the running NETS server.

The master prompt is intentionally a thin router: it surfaces job parameters
+ absolute paths to the per-subject prompts + success/failure markers. It
does NOT prescribe extraction format, content rules, classify output schema,
or any per-subject guidance — those live in the per-subject prompts and
CONTRACTS.md. Editorialising in the master prompt was the cause of the
"runner-prompt corruption" symptom; do not re-introduce it.

The Claude session is invoked headless via:

    claude --print --dangerously-skip-permissions --model <model>

with the master prompt fed on stdin. Output is teed to
``<build_dir>/runner.log`` and the full prompt is persisted at
``<build_dir>/runner-prompt.md`` so any build is reproducible by hand.
"""
from __future__ import annotations

import json
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING

from . import orchestrator_db as odb
from . import pipelines

if TYPE_CHECKING:
    from .drive import AgentSpawn, BuildContext
    from .runlog import RunLog


SUCCESS_MARKER = "BUILD_COMPLETE:"
FAILURE_MARKER = "BUILD_FAILED:"


# ---------------------------------------------------------------------------
# Public entry — drive.py imports this
# ---------------------------------------------------------------------------


def run_plan(
    conn: sqlite3.Connection,
    ctx: "BuildContext",
    plan: list["AgentSpawn"],
    log: "RunLog",
    *,
    model: str,
    api_url: str,
) -> int:
    """Spawn one Claude session that walks the build, then push to NETS API.

    Returns a process-style exit code: 0 = success, non-zero = failure with
    DB status set to ``error`` and ``last_error`` populated.

    Wall-clock + token usage are written to ``<build_dir>/metrics.json`` on
    every exit path (success or failure) for later inspection.
    """
    started_at = datetime.now(UTC).isoformat(timespec="seconds")
    t_start = time.perf_counter()
    claude_metrics: dict = {}
    final_mode: str | None = None
    nets_id: str | None = None
    rc_final: int = 0

    try:
        odb.set_homework_status(conn, ctx.homework_id, "building", current_phase="extraction")
        log.event("inline_mode_engaged", homework_id=ctx.homework_id, model=model,
                  api_url=api_url, plan_steps=len(plan))

        # ----- Compose + persist the master prompt -----
        prompt = _build_master_prompt(ctx)
        prompt_path = ctx.build_dir / "runner-prompt.md"
        prompt_path.write_text(prompt, encoding="utf-8")
        log.event("master_prompt_written", path=str(prompt_path), chars=len(prompt))

        # ----- Spawn Claude headless -----
        rc, result_text, claude_metrics = _spawn_claude(
            prompt=prompt, ctx=ctx, model=model, log=log,
        )
        if rc != 0:
            odb.set_homework_status(conn, ctx.homework_id, "error",
                                    last_error=f"claude subprocess exited rc={rc}")
            log.event("subprocess_failed", rc=rc)
            rc_final = rc
            return rc

        # The CLI can exit rc=0 but flag is_error=true (internal LLM failure,
        # context overflow, terminated turn, etc.). Treat those as failures
        # before we go looking for content.json.
        if claude_metrics.get("is_error"):
            reason = (claude_metrics.get("api_error_status")
                      or claude_metrics.get("terminal_reason")
                      or "claude reported is_error=true")
            odb.set_homework_status(conn, ctx.homework_id, "error",
                                    last_error=f"claude internal error: {reason}")
            log.event("claude_internal_error", reason=reason,
                      terminal_reason=claude_metrics.get("terminal_reason"),
                      stop_reason=claude_metrics.get("stop_reason"))
            rc_final = 4
            return 4

        # ----- Verify the agent's success marker + content.json -----
        last_lines = [ln for ln in result_text.strip().splitlines() if ln.strip()][-5:]
        last_blob = "\n".join(last_lines)
        if FAILURE_MARKER in last_blob:
            reason = _extract_marker_payload(last_blob, FAILURE_MARKER) or "agent reported failure"
            odb.set_homework_status(conn, ctx.homework_id, "error", last_error=reason)
            log.event("agent_reported_failure", reason=reason)
            rc_final = 5
            return 5
        if SUCCESS_MARKER not in last_blob:
            odb.set_homework_status(conn, ctx.homework_id, "error",
                                    last_error="agent did not emit BUILD_COMPLETE marker")
            log.event("missing_success_marker", tail=last_blob)
            rc_final = 6
            return 6

        content_path = ctx.build_dir / "content.json"
        if not content_path.is_file():
            odb.set_homework_status(conn, ctx.homework_id, "error",
                                    last_error=f"missing content.json at {content_path}")
            log.event("missing_content_json", path=str(content_path))
            rc_final = 7
            return 7

        try:
            content = json.loads(content_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            odb.set_homework_status(conn, ctx.homework_id, "error",
                                    last_error=f"content.json malformed: {exc}")
            log.event("content_json_malformed", error=str(exc))
            rc_final = 8
            return 8

        # Pull mode + title from the agent's output (it sets meta.mode after classify)
        meta = content.get("meta") or {}
        title = meta.get("title") or ctx.lesson_ref
        final_mode = meta.get("mode") or _infer_mode_from_classify_md(ctx)
        if final_mode not in ("easy", "hard"):
            # Fall back to the always-hard rule for safety
            final_mode = "hard"

        log.event("content_json_validated",
                  chars=len(json.dumps(content)),
                  mode=final_mode,
                  title=title)

        # ----- Persist payload to autopilot DB -----
        odb.write_payload(
            conn,
            homework_id=ctx.homework_id,
            language=ctx.language,
            content_json_text=json.dumps(content, ensure_ascii=False),
            schema_version="1.0",
        )

        # ----- Push to NETS server -----
        try:
            nets_id, hw_url = _push_to_nets(
                api_url=api_url,
                title=title,
                subject=ctx.subject_id,
                grade=ctx.grade,
                mode=final_mode,
                content=content,
            )
        except _NetsApiError as exc:
            odb.set_homework_status(conn, ctx.homework_id, "error",
                                    last_error=f"NETS API push failed: {exc}")
            log.event("nets_api_failed", error=str(exc))
            print(f"\nlocal build OK but NETS push failed: {exc}", file=sys.stderr)
            print(f"content.json is at {content_path} — push manually with:")
            print(f"  curl -X POST {api_url}/api/homeworks "
                  f"-H 'Content-Type: application/json' "
                  f"-d '{{\"title\":{json.dumps(title)},\"subject\":\"{ctx.subject_id}\","
                  f"\"grade\":{ctx.grade},\"mode\":\"{final_mode}\"}}'")
            rc_final = 9
            return 9

        odb.set_homework_status(conn, ctx.homework_id, "ready", current_phase="published")
        log.event("homework_ready",
                  homework_id=ctx.homework_id,
                  nets_id=nets_id,
                  url=hw_url)

        # Build-complete summary is printed below (in finally) so it always
        # comes after the metrics.json write.
        rc_final = 0
        return 0
    finally:
        # ----- Always write metrics.json + print summary -----
        total_seconds = round(time.perf_counter() - t_start, 2)
        finished_at = datetime.now(UTC).isoformat(timespec="seconds")
        metrics = {
            "homework_id": ctx.homework_id,
            "nets_homework_id": nets_id,
            "subject": ctx.subject_id,
            "grade": ctx.grade,
            "language": ctx.language,
            "mode": final_mode,
            "started_at": started_at,
            "finished_at": finished_at,
            "total_seconds": total_seconds,
            "rc": rc_final,
            **{k: claude_metrics.get(k) for k in (
                "input_tokens",
                "output_tokens",
                "cache_creation_input_tokens",
                "cache_read_input_tokens",
                "num_turns",
                "duration_ms",
                "session_id",
                "is_error",
                "terminal_reason",
                "stop_reason",
                "api_error_status",
            )},
        }
        metrics_path = ctx.build_dir / "metrics.json"
        try:
            metrics_path.write_text(
                json.dumps(metrics, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        except OSError:
            pass  # build_dir might not exist on early failures; don't crash the finally
        log.event("metrics_written", path=str(metrics_path), **metrics)

        # Print summary (success or failure)
        print()
        if rc_final == 0:
            print(f"build complete in {_fmt_duration(total_seconds)}.")
            print(f"  autopilot id : {ctx.homework_id}")
            if nets_id:
                print(f"  NETS id      : {nets_id}")
                print(f"  share URL    : {api_url.rstrip('/')}/h/{nets_id}")
            print(f"  content.json : {ctx.build_dir / 'content.json'}")
        else:
            print(f"build failed (rc={rc_final}) after {_fmt_duration(total_seconds)}.")
        print(f"  metrics.json : {metrics_path}")
        _print_token_summary(claude_metrics)


# ---------------------------------------------------------------------------
# Master prompt composer
# ---------------------------------------------------------------------------


def _build_master_prompt(ctx: "BuildContext") -> str:
    """Assemble the orchestration prompt the spawned Claude executes against.

    This is a thin router. It surfaces the job parameters, lists the per-subject
    prompts in the order Claude must read them, and defines the success/failure
    markers drive.py greps for. It does NOT prescribe extraction format,
    content rules, classify output schema, or assembly schema — those live in
    the per-subject prompts (instruction.md, flow.md, classify.md, phase
    prompts) and CONTRACTS.md respectively.
    """
    from .drive import CONTRACTS_PATH, PROMPTS_ROOT  # avoid circular at module load

    subject_dir = PROMPTS_ROOT / ctx.subject_id
    flow_path = subject_dir / "flow.md"
    classify_prompt = subject_dir / "classify.md"
    needs_classify = ctx.subject_id in pipelines.NEEDS_CLASSIFY
    classify_output = ctx.build_dir / "classify.md"

    if needs_classify:
        easy_pipeline = pipelines.PIPELINES.get((ctx.subject_id, "easy"))
        hard_pipeline = pipelines.PIPELINES[(ctx.subject_id, "hard")]
        classify_block = (
            f"3. classify.md — `{classify_prompt}`\n"
            f"   Apply this rubric to the lesson. Follow the output schema "
            f"defined inside classify.md exactly. Write the result to "
            f"`{classify_output}`. The verdict (easy or hard) selects which "
            f"pipeline you run in step 4."
        )
        if easy_pipeline:
            pipeline_block = (
                f"4. Phase prompts — read each in order, follow each prompt exactly,\n"
                f"   write each phase's output as markdown at the path shown. Phase\n"
                f"   markdowns are working scratch; they help you assemble content.json\n"
                f"   in step 5.\n"
                f"\n"
                f"   ### EASY pipeline ({len(easy_pipeline)} phases) — use if classify verdict is EASY\n"
                f"{_format_phase_listing(easy_pipeline, subject_dir, ctx.build_dir)}\n"
                f"\n"
                f"   ### HARD pipeline ({len(hard_pipeline)} phases) — use if classify verdict is HARD\n"
                f"{_format_phase_listing(hard_pipeline, subject_dir, ctx.build_dir)}"
            )
        else:
            pipeline_block = (
                f"4. Phase prompts — read each in order, follow each prompt exactly,\n"
                f"   write each phase's output as markdown at the path shown. Phase\n"
                f"   markdowns are working scratch; they help you assemble content.json\n"
                f"   in step 5.\n"
                f"\n"
                f"   ### HARD pipeline ({len(hard_pipeline)} phases)\n"
                f"{_format_phase_listing(hard_pipeline, subject_dir, ctx.build_dir)}"
            )
    else:
        hard_pipeline = pipelines.PIPELINES[(ctx.subject_id, "hard")]
        classify_block = (
            f"3. No classify step — this subject is always-HARD by rule "
            f"(`pipelines.ALWAYS_HARD`). Skip directly to the HARD pipeline below."
        )
        pipeline_block = (
            f"4. Phase prompts — read each in order, follow each prompt exactly,\n"
            f"   write each phase's output as markdown at the path shown. Phase\n"
            f"   markdowns are working scratch; they help you assemble content.json\n"
            f"   in step 5.\n"
            f"\n"
            f"   ### HARD pipeline ({len(hard_pipeline)} phases)\n"
            f"{_format_phase_listing(hard_pipeline, subject_dir, ctx.build_dir)}"
        )

    label_line = f"- textbook_label: {ctx.textbook_label}\n" if ctx.textbook_label else ""

    return f"""# NETS Autonomous Homework Build

You are running a one-shot autonomous build of a NETS homework session for the
Uzbekistan curriculum. You have full filesystem access via Read / Write / Glob
/ Grep / Bash and `--dangerously-skip-permissions` is on. Work end-to-end
without asking for input — there is no interactive operator.

## Job parameters

- build_dir: `{ctx.build_dir}`
- subject: `{ctx.subject_id}`
- grade: {ctx.grade}
- language: `{ctx.language}`
- lesson_ref: {ctx.lesson_ref!r}
- pdf_path: `{ctx.pdf_path}`
{label_line}- homework_id (autopilot-local, NOT the NETS server id): `{ctx.homework_id}`

## Prompts to follow

Read these in order. Follow each prompt exactly as written. Do NOT add,
paraphrase, override, or inject anything not specified by the prompts
themselves. The per-subject prompts + CONTRACTS.md are the complete
specification of the build — this file only routes you to them.

1. instruction.md — `{ctx.instruction_path}`
   The per-subject builder playbook. This is the source of truth for the
   entire build, including how to extract from the textbook PDF and what
   `extraction.md` must contain.

2. flow.md — `{flow_path}`
   Phase order + format expectations.

{classify_block}

{pipeline_block}

5. CONTRACTS.md — `{CONTRACTS_PATH}`
   The final JSON schema. After every phase markdown is written, assemble all
   phase outputs into ONE JSON object that conforms exactly to CONTRACTS.md
   section 1, and write it to:

       {ctx.build_dir / 'content.json'}

## Markers (drive.py greps for these — emit exactly as shown)

When `content.json` is written and parses as valid JSON, print this as the
very last line of your output (mode in lower-case, matching your classify
verdict — `easy` or `hard`):

    {SUCCESS_MARKER} {ctx.build_dir / 'content.json'} mode=<easy|hard>

If you cannot complete the build (textbook missing the lesson, irrecoverable
error), instead print this exact line and exit:

    {FAILURE_MARKER} <one-line reason>
"""


def _format_phase_listing(
    phases: tuple,
    subject_dir: Path,
    build_dir: Path,
) -> str:
    """Render a numbered phase listing with absolute prompt + output paths."""
    lines = []
    for idx, spec in enumerate(phases, start=1):
        prompt = subject_dir / spec.prompt_file if spec.prompt_file else None
        output = build_dir / f"phase-{idx}-{spec.name}.md"
        skip = " (can_skip)" if spec.can_skip else ""
        lines.append(f"{idx}. **{spec.name}**{skip}")
        if prompt:
            lines.append(f"   - prompt: `{prompt}`")
        lines.append(f"   - output: `{output}`")
    return "\n".join(lines)


def _infer_mode_from_classify_md(ctx: "BuildContext") -> str | None:
    """Read build_dir/classify.md as a fallback if meta.mode is missing.

    Per-subject ``classify.md`` prompts define their own output schema; current
    schema is a JSON object ``{"mode": "easy|hard", "level": ..., "reason": ...}``
    (possibly inside a fenced ```json``` block). Older builds emitted a plain
    ``VERDICT: <EASY|HARD>`` line — fall back to that for compatibility with
    archived builds.
    """
    p = ctx.build_dir / "classify.md"
    if not p.is_file():
        return None
    text = p.read_text(encoding="utf-8")

    # Try JSON first (current schema). Tolerant of fenced blocks + leading prose.
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            parsed = json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            parsed = None
        if isinstance(parsed, dict):
            mode = parsed.get("mode")
            if isinstance(mode, str) and mode.lower() in ("easy", "hard"):
                return mode.lower()

    # Legacy fallback — `VERDICT: <EASY|HARD>` line.
    for line in text.splitlines():
        line = line.strip()
        if line.upper().startswith("VERDICT:"):
            verdict = line.split(":", 1)[1].strip().lower()
            if verdict in ("easy", "hard"):
                return verdict
    return None


def _extract_marker_payload(text: str, marker: str) -> str | None:
    for line in text.splitlines():
        if marker in line:
            return line.split(marker, 1)[1].strip()
    return None


def _fmt_duration(seconds: float) -> str:
    """Render a wall-clock duration as e.g. '11m 24s' or '1h 03m 12s'."""
    s = int(round(seconds))
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    if h:
        return f"{h}h {m:02d}m {sec:02d}s"
    if m:
        return f"{m}m {sec:02d}s"
    return f"{sec}s"


def _print_token_summary(claude_metrics: dict) -> None:
    """Print a one-line tokens summary if metrics are present."""
    inp = claude_metrics.get("input_tokens")
    out = claude_metrics.get("output_tokens")
    cache_read = claude_metrics.get("cache_read_input_tokens") or 0
    cache_create = claude_metrics.get("cache_creation_input_tokens") or 0
    turns = claude_metrics.get("num_turns")
    if inp is None and out is None:
        return
    parts = []
    if inp is not None:
        parts.append(f"{inp:,} in")
    if out is not None:
        parts.append(f"{out:,} out")
    line = "  tokens       : " + " / ".join(parts)
    if cache_read or cache_create:
        line += f"  (cache: {cache_read:,} read, {cache_create:,} write)"
    print(line)
    if turns is not None:
        print(f"  num_turns    : {turns}")


# ---------------------------------------------------------------------------
# Subprocess plumbing
# ---------------------------------------------------------------------------


def _spawn_claude(
    *,
    prompt: str,
    ctx: "BuildContext",
    model: str,
    log: "RunLog",
) -> tuple[int, str, dict]:
    """Run `claude --print --output-format json --dangerously-skip-permissions ...` once.

    The prompt is fed via stdin. stdout is captured (it's a single JSON
    envelope when the run finishes) and saved to ``runner.log``.

    Returns ``(returncode, result_text, metrics)`` where:
      - ``result_text`` is the agent's textual output (envelope.result), the
        thing we grep for ``BUILD_COMPLETE``;
      - ``metrics`` carries token usage + duration_ms + num_turns + session_id.
        Empty dict on parse failure.
    """
    from .drive import REPO_ROOT

    claude_bin = shutil.which("claude") or shutil.which("claude.cmd")
    if not claude_bin:
        log.event("claude_cli_missing", searched_path=True)
        print("error: `claude` CLI not found on PATH. Install Claude Code first.",
              file=sys.stderr)
        return 127, "", {}

    cmd = [
        claude_bin,
        "--print",
        "--dangerously-skip-permissions",
        "--output-format", "json",
        "--model", model,
    ]
    log.event("subprocess_spawn", cmd=cmd, prompt_chars=len(prompt))

    runner_log = ctx.build_dir / "runner.log"
    print(f"\n[autopilot] spawning {model} — output will arrive at end of build")
    print(f"[autopilot] file progress is visible in {ctx.build_dir}")

    try:
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=str(REPO_ROOT),
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError as exc:
        log.event("subprocess_spawn_failed", error=str(exc))
        print(f"error: could not spawn claude: {exc}", file=sys.stderr)
        return 126, "", {}

    # Feed prompt via stdin, collect everything via communicate(). With
    # --output-format json the CLI emits one envelope at the end, so there's
    # no useful streaming — communicate() blocks until completion.
    try:
        stdout, _ = proc.communicate(input=prompt)
    except KeyboardInterrupt:
        proc.kill()
        log.event("subprocess_interrupted")
        return 130, "", {}

    rc = proc.returncode
    log.event("subprocess_complete", rc=rc, stdout_chars=len(stdout))

    # Persist the raw envelope (or fallback raw stdout) for debugging.
    with runner_log.open("a", encoding="utf-8") as log_fh:
        log_fh.write(f"\n\n===== build {ctx.homework_id} (rc={rc}) =====\n")
        log_fh.write(stdout)

    # Parse the envelope. Claude Code's --output-format json emits one object
    # with at least: result, usage{...}, duration_ms, num_turns, session_id.
    try:
        envelope = json.loads(stdout) if stdout.strip() else {}
    except json.JSONDecodeError as exc:
        log.event("envelope_parse_failed", error=str(exc), stdout_chars=len(stdout))
        # Fall back to treating the raw stdout as the result text. The caller
        # will grep it for BUILD_COMPLETE; if the agent finished its work
        # before some unrelated CLI crash, we can still recover.
        return rc, stdout, {}

    result_text = envelope.get("result") or ""
    usage = envelope.get("usage") or {}
    metrics = {
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
        "duration_ms": envelope.get("duration_ms"),
        "num_turns": envelope.get("num_turns"),
        "session_id": envelope.get("session_id"),
        "is_error": envelope.get("is_error"),
        "terminal_reason": envelope.get("terminal_reason"),
        "stop_reason": envelope.get("stop_reason"),
        "api_error_status": envelope.get("api_error_status"),
    }
    log.event("envelope_parsed",
              result_chars=len(result_text),
              **{k: v for k, v in metrics.items() if v is not None})
    return rc, result_text, metrics


# ---------------------------------------------------------------------------
# NETS server push
# ---------------------------------------------------------------------------


class _NetsApiError(RuntimeError):
    pass


def _push_to_nets(
    *,
    api_url: str,
    title: str,
    subject: str,
    grade: int,
    mode: str,
    content: dict,
) -> tuple[str, str]:
    """POST a fresh homework, then PUT the content_json into it.

    Returns (nets_homework_id, share_url).

    Raises _NetsApiError on any HTTP / network failure.
    """
    api_url = api_url.rstrip("/")

    # ----- POST /api/homeworks -----
    create_body = json.dumps({
        "title": title,
        "subject": subject,
        "grade": grade,
        "mode": mode,
    }).encode("utf-8")
    create_req = urllib.request.Request(
        url=f"{api_url}/api/homeworks",
        data=create_body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(create_req, timeout=30) as resp:
            create_payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise _NetsApiError(f"POST /api/homeworks → HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise _NetsApiError(f"POST /api/homeworks → {exc.reason}") from exc

    nets_id = create_payload.get("id")
    if not nets_id:
        raise _NetsApiError(f"POST /api/homeworks did not return an id: {create_payload!r}")

    # ----- PUT /api/homeworks/{id} -----
    update_body = json.dumps({
        "title": title,
        "content_json": content,
    }, ensure_ascii=False).encode("utf-8")
    update_req = urllib.request.Request(
        url=f"{api_url}/api/homeworks/{nets_id}",
        data=update_body,
        headers={"Content-Type": "application/json"},
        method="PUT",
    )
    try:
        with urllib.request.urlopen(update_req, timeout=60) as resp:
            resp.read()  # drain
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise _NetsApiError(f"PUT /api/homeworks/{nets_id} → HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise _NetsApiError(f"PUT /api/homeworks/{nets_id} → {exc.reason}") from exc

    return nets_id, f"{api_url}/h/{nets_id}"
