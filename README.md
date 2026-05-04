# NETS Autopilot

Autonomous homework-builder for the NETS LMS. You give it a textbook PDF and a lesson reference; it spawns one Claude Opus 4.7 session, walks the per-subject build playbook end-to-end, and pushes the finished homework to the running NETS server. One command in → one share URL out.

---

## ⚠ Currently-dead source files

These files are checked in but **not imported by the live build path**. Nothing in `drive.py` / `agent_runner.py` reads them right now. They survive because the capabilities they represent might come back later — deleting them would mean rewriting from scratch if those features return.

| File | What it was for | Why it's dead now |
|---|---|---|
| `autopilot/ingest.py` | Batch-ingesting textbook PDFs into the autopilot DB (pre-cataloging titles + sections) | Current flow has Claude read PDFs directly via the `Read` tool; no pre-cataloging needed |
| `autopilot/toc.py` | Parsing textbook TOCs out of PDFs | Only imported by `ingest.py` (which is dead) |
| `autopilot/textwork.py` | Title normalization + OCR recovery utilities | Only imported by `toc.py` (which is dead) |
| `autopilot/link.py` | Linking matching uz ↔ ru theme rows across editions | No live caller; the autopilot doesn't push bilingual variants today |
| `autopilot/validate.py` | Parsing the validator agent's `VERDICT:` markdown | Designed for the multi-agent fan-out architecture that was abandoned in favor of one-Claude-per-build |

**None of these files affect a live build.** If you ever want batch ingestion, bilingual linking, or a return to multi-agent validation, these are starting points rather than scratch.

---

## What it does, in plain English

You give the autopilot three things:

1. A subject and grade (e.g. `biology`, grade `8`).
2. A lesson reference (e.g. `"§3. Hujayra va organizmning hayotiy xossalari"`).
3. A textbook PDF.

It does the rest:

1. **Spawns Claude Code** in headless mode with a master prompt.
2. The Claude session **reads the per-subject playbook** from `Homework-builder/server/prompts/`, **opens the PDF**, locates the lesson, and **decides EASY or HARD** difficulty (only for subjects that need classification — others have their mode pre-set).
3. It **walks the chosen pipeline** (5 to 9 phases depending on subject and mode), generating preview panels, flashcards, memory-sprint quizzes, game-break content, real-life scenarios, a consolidation phase, a boss fight, and a reflection.
4. It **assembles all phase outputs into one `content.json`** that conforms to `CONTRACTS.md §1` — the binding schema for NETS homework content.
5. The autopilot **picks the JSON back up**, **POSTs to NETS** to mint a homework ID, then **PUTs the content** into it.
6. It **prints the share URL**: `http://sigmaai.local:8000/h/HW-...`.

A typical Opus 4.7 build takes **8–15 minutes** for hard subjects.

---

## Quickstart

### Prerequisites

- **Python 3.10+** — the autopilot uses only the Python standard library, so there's no `pip install` step.
- **Claude Code CLI** installed and on your `PATH`. Verify with `claude --version`.
- **A running NETS server** reachable at the URL you'll point at (default `http://sigmaai.local:8000`).
- **The Homework-builder repo cloned** at `../Homework-builder/` relative to this folder. The autopilot reads per-subject prompts and the content schema from there. See [Path dependency](#path-dependency-on-homework-builder).
- **A textbook PDF** placed in a local `textbooks/` directory (this directory is gitignored — you populate it on each machine).

### Running a build

**Interactive** (recommended for first-time use):

```powershell
cd Homework-builder\Automation
python -m autopilot.drive build
```

You'll be prompted for subject, grade, theme/lesson, language, and textbook PDF (the picker auto-lists what's in `textbooks/`).

**Headless** (all flags supplied):

```powershell
python -m autopilot.drive build `
  --grade 8 `
  --subject biology `
  --language uz `
  --lesson-ref "Grade 8 Biologiya §3. Hujayra va organizmning hayotiy xossalari" `
  --pdf "textbooks\8-sinf_odam_va_uning_salomatligi_2019.pdf"
```

---

## How a build flows, step by step

```
You run drive.py
  ├── (interactive prompts fill any missing args)
  ├── creates Automation/builds/HW-YYYYMMDD-NNN/   (autopilot's local id sequence)
  ├── composes a master prompt (~9 KB) → runner-prompt.md
  └── spawns: claude --print --output-format json
                     --dangerously-skip-permissions
                     --model claude-opus-4-7
                                                                              ┐
       ↓                                                                      │
       Claude reads instruction.md, flow.md, CONTRACTS.md                     │
       ↓                                                                      │
       Claude opens the PDF, locates the lesson                               │
       ↓                                                                      │
       Claude writes extraction.md (working notes)                            │ Single
       ↓                                                                      │ Claude
       (if subject NEEDS_CLASSIFY)                                            │ session,
       Claude reads classify.md → writes verdict to classify.md               │ ~10 min
       ↓                                                                      │ on Opus
       Claude walks each phase prompt:                                        │ 4.7
         preview → flashcards → memory_sprint → game_breaks                   │
         → real_life → consolidation → final_challenge → reflection           │
       Each phase writes phase-N-<name>.md                                    │
       ↓                                                                      │
       Claude assembles everything into content.json                          │
       ↓                                                                      │
       Claude prints "BUILD_COMPLETE: <path> mode=<easy|hard>"                ┘

drive.py picks back up
  ├── parses Claude's JSON envelope (tokens, duration, num_turns)
  ├── reads content.json
  ├── POST  http://<api>/api/homeworks       → mints NETS HW-id
  ├── PUT   http://<api>/api/homeworks/<id>  → fills content_json
  ├── writes metrics.json (wall-clock + token usage)
  └── prints share URL: http://<api>/h/<id>
```

---

## CLI reference

### `python -m autopilot.drive build`

| Flag | Default | Notes |
|---|---|---|
| `--grade <int>` | (interactive prompt) | 1–12 |
| `--subject <id>` | (interactive prompt) | `biology` / `geometriya-g7-11` / `kimyo-g7-11` / `math-algebra` / `physics` / `english` / `history` |
| `--language <code>` | (interactive prompt) | `uz` / `ru` / `en` |
| `--lesson-ref <text>` | (interactive prompt) | Free-text reference; used both as the homework title and the lookup key inside the PDF |
| `--pdf <path>` | (interactive prompt) | Path to the textbook PDF (auto-listed from `textbooks/` in interactive mode) |
| `--label <text>` | none | Optional textbook label (e.g. `"Jahon Tarixi"`) |
| `--api-url <url>` | env `NETS_API_URL`, or `http://sigmaai.local:8000` | NETS server base URL |
| `--model <id>` | `claude-opus-4-7` | Claude CLI model id |
| `--db <path>` | (default DB) | Override the autopilot's local SQLite path |
| `--dry-run` | off | Records DB rows + creates folders but invokes no agents (for CI / state-check) |
| `--planner` | off | Prints the legacy multi-agent plan as JSONL and exits — for human inspection only |

### `python -m autopilot.drive show --homework-id HW-...`

Prints a status report for a build: `queued` / `building` / `ready` / `error`, the current phase, recent phase runs, and payload metadata.

---

## Build directory layout

Each build creates a directory under `builds/` named `HW-YYYYMMDD-NNN`. This is the **autopilot's local sequence**, separate from the NETS server's homework IDs.

```
builds/HW-20260504-002/
├── runner-prompt.md     ← The master prompt fed to Claude (~9 KB). Useful for repro.
├── extraction.md        ← Claude's working notes from reading the PDF.
├── classify.md          ← Claude's verdict: VERDICT: EASY|HARD + one-sentence reason.
├── phase-1-preview.md   ← Per-phase scratch markdown (5–9 of these).
├── phase-2-flashcards.md
├── ...
├── phase-N-reflection.md
├── content.json         ← THE DELIVERABLE. Conforms to CONTRACTS.md §1.
├── runner.log           ← Raw Claude CLI output envelope (JSON).
├── run.log              ← Orchestrator events, one JSON per line (JSONL).
└── metrics.json         ← Wall-clock + token usage. See below.
```

The phase markdowns are working scratch — they help Claude assemble the final JSON and aid debugging. **Only `content.json` gets pushed to NETS.**

---

## metrics.json — what's tracked

Written on every build, success OR failure. Sample:

```json
{
  "homework_id": "HW-20260504-002",         // local autopilot id
  "nets_homework_id": "HW-20260504-005",    // id minted by NETS server (null if push failed)
  "subject": "biology",
  "grade": 8,
  "language": "uz",
  "mode": "hard",                            // classify verdict, lower-case
  "started_at": "2026-05-04T17:20:24+00:00",
  "finished_at": "2026-05-04T17:31:48+00:00",
  "total_seconds": 684.27,
  "rc": 0,                                   // 0 = success, non-zero = failure code
  "input_tokens": 142310,
  "output_tokens": 8724,
  "cache_creation_input_tokens": 20978,
  "cache_read_input_tokens": 64500,
  "num_turns": 23,                           // Claude turns inside the one CLI call
  "duration_ms": 681840,                     // Claude's own duration measure
  "session_id": "8f3e...",
  "is_error": null,                          // true → Claude internal error
  "terminal_reason": "completed",
  "stop_reason": "end_turn",
  "api_error_status": null
}
```

**`num_turns`** is a useful health signal. A normal build is ~15–30 turns. Spikes (60+) usually mean Claude got into a re-read or retry loop — check `runner.log` to see what tripped it up.

---

## Subjects + pipelines

| Subject ID | Family | Mode | Phase count |
|---|---|---|---|
| `biology` | tabiy-fanlar | classify | easy=5, hard=8 |
| `geometriya-g7-11` | aniq-fanlar | classify | easy=5, hard=8 |
| `kimyo-g7-11` | tabiy-fanlar | classify | easy=5, hard=8 |
| `math-algebra` | aniq-fanlar | classify | easy=5, hard=8 |
| `physics` | tabiy-fanlar | classify | easy=5, hard=8 |
| `english` | til-fanlar | always-hard | 9 |
| `history` | ijtimoiy-fanlar | always-hard | 7 |

**Standard phase order** (subjects vary slightly):

```
preview → flashcards → memory_sprint → [reading: English only]
       → game_breaks → real_life (hard only) → consolidation (hard only, can-skip)
       → final_challenge (hard only) → reflection
```

For subjects with `classify` mode, Claude reads `classify.md` mid-build and chooses easy or hard. For `always-hard` subjects (English, History), there's no classify step — mode is hard by rule.

The full registry lives in `autopilot/pipelines.py`.

---

## Configuration

| Setting | Where to set | Default |
|---|---|---|
| NETS server URL | `--api-url` flag, or `NETS_API_URL` env var | `http://sigmaai.local:8000` |
| Claude model | `--model` flag | `claude-opus-4-7` |
| Autopilot DB path | `--db` flag | `db/homework_db.sqlite` (next to `autopilot/`) |
| Build output dir | (none) | `builds/<homework_id>/` |
| Textbook source dir | (none) | `textbooks/` |

---

## Path dependency on Homework-builder

The autopilot reads two things from the parent NETS-server source tree:

1. `Homework-builder/server/prompts/<subject>/*.md` — the per-subject playbooks (`instruction.md`, `flow.md`, `classify.md`, plus 5–9 per-phase prompts) that tell Claude how to build each phase.
2. `Homework-builder/CONTRACTS.md` — the schema that `content.json` must conform to.

The path constants in `autopilot/drive.py` and `autopilot/pipelines.py` resolve via:

```python
REPO_ROOT = Path(__file__).resolve().parents[2]   # = Homework-builder/
```

This assumes the autopilot lives at `Homework-builder/Automation/autopilot/`.

**If you clone this repo to a different location** (no `Homework-builder/` parent), the path constants will resolve to wrong directories and the build will fail at startup with `pipeline registry errors`. To run the autopilot somewhere else, you'd need to either:
- Keep the autopilot inside `Homework-builder/Automation/` (the supported layout).
- Or patch the path constants to read from a `NETS_REPO_ROOT` env var (small change, not yet implemented).

---

## What is NOT in this repo

These directories are gitignored — they're per-machine local state:

- `textbooks/` — Copyrighted PDF source materials. Place yours here locally.
- `builds/` — Per-homework output dirs (textbook-derived content; can be large).
- `db/` — Local SQLite orchestrator database.
- `extracted/` — Working files (TOC comparisons, etc.).
- `autopilot/.venv/` — Python virtual env (not actually needed since no third-party deps).
- `__pycache__/` — Python bytecode.

---

## Architecture notes

**One Claude invocation per build.** Earlier designs fanned out across 14 worker spawns + validators. The current design composes one master prompt per build (~9 KB) and runs `claude --print --output-format json --dangerously-skip-permissions --model <model>` exactly once. The agent does extraction, classification, all phases, and assembly inside that single call.

**Two SQLite databases, intentionally separate:**

- The **autopilot DB** at `db/homework_db.sqlite` tracks build orchestration state (`queued` / `building` / `ready` / `error`), payload snapshots, and a manual theme/textbook mapping for ad-hoc lessons.
- The **NETS server DB** (inside the Homework-builder repo) holds published homework content for students.

These have **independent `HW-YYYYMMDD-NNN` ID sequences**. The autopilot's HW-id is local-only; the NETS server mints its own HW-id when content is POSTed.

**Why `--output-format json`?** It's the only mode where Claude CLI exposes structured token usage and duration. The trade-off is the CLI buffers all output until the end (no token-by-token streaming during the build). You still see file appearances in `builds/<id>/` while Claude works — that's how you monitor progress.

**Failure modes** are handled by `agent_runner.run_plan`:

| What goes wrong | Result |
|---|---|
| Claude subprocess returns rc != 0 | `error` status, `last_error` populated, `metrics.json` still written |
| Claude exits clean but flags `is_error: true` (internal LLM failure, context overflow, etc.) | Same |
| Claude prints `BUILD_FAILED: <reason>` instead of `BUILD_COMPLETE:` | Same |
| `content.json` missing or malformed | `error` status, content not pushed |
| NETS API push fails (server down, 4xx/5xx) | `error` status, `content.json` stays local for manual push, autopilot prints a curl recipe |

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `pipeline registry errors (orchestrator refuses to start)` | Path constants don't resolve to a Homework-builder root with `server/prompts/` | Verify the autopilot lives at `Homework-builder/Automation/autopilot/` |
| `error: 'claude' CLI not found on PATH` | Claude Code CLI not installed | Install Claude Code; verify `claude --version` |
| `error: PDF not found: ...` | Textbook path is wrong | Use the interactive picker (no `--pdf` flag) to list real options |
| Build completes but `metrics.json` shows `is_error: true` | Claude internal failure mid-build | Check `runner.log` for the envelope; retry the build |
| `local build OK but NETS push failed: ... 10061 ...` | NETS server not running or wrong URL | Start the server, or pass the correct `--api-url http://...:8000` |
| `is_error: false` but `content.json` missing | Claude finished but didn't write the JSON | Check `runner.log` and the latest phase markdown to see where it stopped |
| Repeated builds re-extract the same PDF | Expected — Claude reads the PDF fresh each invocation, no shared cache | None; this is by design |

---

## Manual NETS push

If a build's auto-push fails but `content.json` is on disk:

```powershell
$buildDir = "builds\HW-20260504-002"
$apiUrl   = "http://sigmaai.local:8000"
$content  = Get-Content "$buildDir\content.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$title    = $content.meta.title

$createBody  = @{ title=$title; subject="biology"; grade=8; mode="hard" } | ConvertTo-Json -Compress
$createBytes = [Text.Encoding]::UTF8.GetBytes($createBody)
$create = Invoke-RestMethod -Method POST -Uri "$apiUrl/api/homeworks" -ContentType "application/json" -Body $createBytes
"minted: $($create.id)"

$putBody  = @{ title=$title; content_json=$content } | ConvertTo-Json -Depth 50 -Compress
$putBytes = [Text.Encoding]::UTF8.GetBytes($putBody)
Invoke-RestMethod -Method PUT -Uri "$apiUrl/api/homeworks/$($create.id)" -ContentType "application/json" -Body $putBytes | Out-Null
"share URL: $apiUrl/h/$($create.id)"
```

The `[Text.Encoding]::UTF8.GetBytes(...)` step is required on Windows PowerShell 5.1 to avoid mangling non-ASCII characters in the body.
