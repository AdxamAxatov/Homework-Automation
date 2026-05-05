# Prompt: Reflection — History (O'zbekiston Tarixi + Jahon Tarixi)

You are building the Reflection phase (Phase 7) for a History homework session. This is silent analytics + a quiet closing — no scoring, no pressure. Summarize what was learned, mirror the student's opening goal, ask one thinking question, schedule spaced review, close with a mode-appropriate message.

## Input

- Textbook lesson content (extracted in orchestrator Step 1)
- All previous phase outputs (Preview through Boss)
- Phase 6 Boss outcome (score %, stars, HP remaining, hints used)
- Grade: G5–G11
- Subject: `O'zbekiston Tarixi` or `Jahon Tarixi`
- Milliylik intensity: `high` or `low`

## Output

Student-facing: **5 parts, ~2 minutes total.**

Plus: silent analytics documentation (what the pipeline collects — not student-facing).

**Not scored.**

---

## Student-facing — 5 parts

### 1. Summary (3–5 sentences)

What the student learned in this specific lesson. Include:
- 2–4 key figures with their role
- The 1 dominant causal framework (from Preview Panel 2)
- 1–3 modern-relevance hooks (from Preview Panel 6)

Open with: *"Bugun Siz [lesson topic] ni oʻrgandingiz..."*

### 2. BOST goal mirror

Resurface the learning goal the student wrote at the end of Preview Panel 6.

> *"Eslatma: Phase 0-A Panel 6 da Siz shunday savolga javob bergansiz: 'Bugun Siz [topic] haqida aynan nimani bilmoqchi edingiz?' Javobingizni qayta koʻring. Yetdingizmi?"*

Options: **Ha** / **Qisman** / **Hali emas**

Not scored. Logged for teacher dashboard as aggregate theme only.

### 3. One thinking question

Rotate across sessions. Pick ONE of these History-appropriate prompts:

- *"Agar [key figure] [key decision]ni qilmasdan, boshqacha yoʻl tanlaganda — qaysi oʻzgarish bo'lardi?"* (counterfactual)
- *"Bu bobdagi qaysi shaxs bilan shaxsan uchrashishni xohlar edingiz? Qanday savolni berar edingiz?"* (personal)
- *"Bu darsdagi qaysi voqea Sizni eng koʻp hayratga soldi? Nega?"* (affective)
- *"Bugungi dunyoda bu darsning izlari qayerda koʻrinadi?"* (continuity)

Minimum 10 characters when enabled. Not auto-graded. Teacher dashboard shows aggregate themes only.

### 4. Spaced repetition schedule

Propose a 1-day / 3-day / 7-day review schedule:

| Muddat | Taxmini sana | Takrorlash turi |
|---|---|---|
| 1 kun | Ertaga | Flash Cards + Memory Palace quick walkthrough |
| 3 kun | 3 kundan keyin | 2–3 Boss questions re-attempted |
| 7 kun | 7 kundan keyin | Full Memory Palace walkthrough (Phase 5 re-run) |

List **2–3 specific concepts** from this session the student should focus on (pulled from Boss performance — the concepts they got wrong or used hints on).

### 5. Closing line

**IF `overall_score_pct ≥ 60`:**

Choose based on Milliylik intensity ratio for this subject:
- `milliylik_intensity: high` → 55% national / 45% global
  - *National:* *"Sizning tarixiy fikrlashingiz — Uchinchi Renessans poydevori. [topic]ni tushungan talaba bugungi Oʻzbekistonni chuqurroq his qiladi."*
  - *Global:* *"Sizning manbalarni tahlil qilish va ramkalarni qoʻllash qobiliyatingiz jahon tarixchilari standartlariga mos keladi."*
- `milliylik_intensity: low` → 20% national / 80% global (mostly use global variant)

**IF `overall_score_pct < 60`:**

TEFCAS framing — **never punitive, never "failed":**

> *"Hali emas! Har bir urinish miyangizni kuchaytiradi. Ertaga davom etamiz — Phase 0-A va 0-B ga qaytib, keyin Boss bilan yangidan uchrashamiz."*

---

## Silent analytics (pipeline-only, student does NOT see)

Document the 4 data layers collected invisibly. The output should include a separate `## Silent analytics` section that lists:

### Layer 1 — Per-question
- `question_id`, `phase_id` (0a / 0b / 1 / 3 / 5 / 6 / 7)
- `bloom_level`, `pisa_level`, `pisa_domain` (Reading / Creative Thinking)
- `skill_tags` (Memory / Critical Thinking / Application / etc.)
- `correct` (boolean), `time_seconds`, `attempts`, `hints_used`, `difficulty`

### Layer 2 — Per-phase
- `phase_score_pct`, `phase_time_seconds`, `phase_completed`
- `phase_skill_breakdown` (percentage per skill axis)

### Layer 3 — Per-session
- `session_id`, `lesson_id`
- `overall_score_pct` = (Phase 1 × 10%) + (Phase 3 × 50%) + (Phase 6 × 40%)
- `passed` = `overall_score_pct ≥ 60`
- `vs_student_avg` (delta from student's subject average)
- `skill_deltas`

### Layer 4 — Routing decision
```
IF overall_score_pct < 60:
    → identify weakest phase + failed standards
    → queue remediation: relevant Preview panels → Flash Cards → failed Boss Qs (easier variants)
    → mark lesson "remediation-required"
ELIF overall_score_pct ≥ 60 AND > student_subject_avg:
    → advance to next History lesson
    → update student_subject_avg
ELSE:
    → advance; flag regression signal (teacher-only)
```

---

## Rules

- **5 student-facing parts** in order: Summary → BOST mirror → Thinking question → Spaced repetition → Closing line.
- **Not scored** — no HP, no XP, no grade.
- **BOST mirror references the actual Phase 0-A Panel 6 goal** — do not invent a new goal.
- **Closing line format depends on `overall_score_pct`** — Milliylik 55/45 (or 20/80) on pass; TEFCAS on fail.
- **Thinking questions rotate** — do not use the same one every session; vary across counterfactual / personal / affective / continuity.
- **Spaced repetition concepts are specific** — derived from what the student struggled with in Boss, not generic "study the chapter."
- **Silent analytics** — document the 4 layers + routing logic. Student does NOT see this section rendered; it's for the pipeline.
- **Language:** Uzbek, `Siz` always. Never `sen`. Never "failed" / "Notoʻgʻri" in closing — TEFCAS framing only.
- **~2 minutes** student-facing time.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "summary": "string",
  "question": "string",
  "spaced_rep": "string",
  "closing": "string"
}
```
