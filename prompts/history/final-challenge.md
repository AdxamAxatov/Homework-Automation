# Prompt: Final Challenge (Boss) — History (O'zbekiston Tarixi + Jahon Tarixi)

You are building the Final Challenge (Phase 6) for a History homework session. This is the boss fight — HP combat. The student proves mastery of this lesson's figures, frameworks, and primary source(s).

## Input

- Textbook lesson content (extracted in orchestrator Step 1)
- All previous phase outputs (Preview, Flash Cards, Sprint, Games, Consolidation)
- Grade: G5–G11
- Subject: `O'zbekiston Tarixi` or `Jahon Tarixi`

## Output

**5 questions** with HP damage tags. Mix of difficulty tiers.

---

## HP and Damage

| Grade band | HP |
|---|:-:|
| G1–G4 | 50 |
| G5–G8 | **100** |
| G9–G11 | 150 |

| Difficulty | Damage | Distribution (per 5 Qs) |
|---|:-:|:-:|
| Easy | −10 HP | 40% (2 Qs) |
| Medium | −20 HP | 40% (2 Qs) |
| Hard | −30 HP | 20% (1 Q) |

**Damage values are FIXED** — Easy = **exactly −10 HP**, Medium = **exactly −20 HP**, Hard = **exactly −30 HP**. Never use −15, −25, −40, or any other value. If you need different total HP for G1–4 (50 HP) or G9–11 (150 HP), adjust the question COUNT, not the damage values.

Total damage across 5 questions = 100 HP = full boss defeat for G5–G8.

---

## Question Construction

Every question carries inline tags: `[Bloom: LX | PISA: Reading/Creative Thinking LX | Skill: ... | Damage: -XX HP | Standard: UZ-TARIX-G-TOPIC-B-##]`

**Must include in the set of 5:**
- ≥1 **primary source analysis** question (quote the source, ask 2-part: principle + causal consequence). This is the signature History Boss item — from `family-ijtimoiy-fanlar.md`.
- ≥1 **causal-framework application** (apply the framework named in Preview Panel 2 to explain a specific lesson event).
- ≥1 **evaluation/synthesis** question at the Hard tier (judge success/failure of a figure or decision with evidence from multiple sources).

**Question type restrictions by grade band:**

| Grade band | Allowed formats |
|---|---|
| G1–G4 | Multiple choice + short answer (up to 30% MC) |
| **G5–G11** | **Short answer + open reasoning. NO multiple choice.** |

For G5–G11 (our default), every question is open response. No MC.

**Difficulty scaling:**
- **Easy (−10):** direct recall or single-step understanding (identify a figure, name a reform, date recognition)
- **Medium (−20):** 2-step reasoning (causal analysis, primary source interpretation, source comparison)
- **Hard (−30):** multi-step synthesis (evaluate-with-evidence, counterfactual reasoning, multi-source judgment)

---

## Example set (G8 — 100 HP)

*(Numbers refer to a generic History lesson. Actual content comes from the specific lesson.)*

> **Q1** `[Bloom: L2 | PISA: Reading L2 | Skill: Memory | Damage: -10 HP]`
> Direct recall of 3 specific reforms/events from the lesson.
>
> **Q2** `[Bloom: L3 | PISA: Reading L3 | Skill: Memory + Application | Damage: -10 HP]`
> Trace a 3-step causal chain from lesson content.
>
> **Q3** `[Bloom: L4 | PISA: Reading L4 | Skill: Critical Thinking | Damage: -20 HP]`
> Primary source analysis (2-part): (a) what principle does the source embody? (b) what causal consequence did it trigger?
>
> **Q4** `[Bloom: L4 | PISA: Creative Thinking L2 | Skill: Critical Thinking + Application | Damage: -20 HP]`
> Apply the causal framework from Preview Panel 2 to explain why a specific lesson event unfolded as it did.
>
> **Q5** `[Bloom: L5 | PISA: Reading L5 + Creative Thinking L2 | Skill: Critical Thinking + Metacognition | Damage: -30 HP]`
> 2-part evaluation: (a) list evidence on both sides of a judgment; (b) take a position and justify with sources + framework + consequences.

---

## Hint ladder (3 hints per question, −5 HP each)

Every question offers up to 3 hints. Costs −5 HP each.

| Tier | Purpose | Form |
|---|---|---|
| **Hint 1** | Reference | Point to the specific Phase 0-A panel, Flash Card, or Memory Palace station that contains the relevant content |
| **Hint 2** | Frame | Categorize or give structure — "this is a 3-step chain," "this asks for both sides" |
| **Hint 3** | **Diagnostic questions, NEVER an answer template** | 3–4 self-questions that guide the student to construct the answer themselves. DO NOT provide a fill-in-blank skeleton. |

**Hint 3 rule — critical.** Never write "Javob skeleti: X bo'lgani uchun Y, Z" — that hands the student the structure. Instead, write "Oʻzingizga savol bering: (1) ..., (2) ..., (3) ..." — diagnostic questions that nudge toward the answer without giving it.

---

## Failure flow (Boss not defeated)

If student HP reaches 0 before all questions correct:

1. **Identify** which standards failed (by question tags)
2. **Socratic Tutoring** (TEFCAS framing):
   - *"Hali emas! Miyangiz Feedback oldi."*
   - **CHECK:** *"Keling, tekshiramiz — savol qaysi Preview panelini yoki qaysi kartani talab qilardi?"*
   - **ADJUST:** *"Buni boshqacha qaysi yondashuvdan koʻrsa boʻladi?"*
   - AI **does not give the answer** — only guides
3. **Regenerate** questions — same standards, different context (e.g., different figure, different date, different source)
4. Student re-attempts → success → Phase 7.

**Failure language:** **"Hali emas!"** — never "Notoʻgʻri" or "Xato."

---

## Mastery Stars

| Stars | Criteria |
|---|---|
| ⭐ | Boss defeated (any number of attempts) |
| ⭐⭐ | Defeated in ≤2 attempts, HP > 50% remaining |
| ⭐⭐⭐ | First attempt, no hints used, HP > 80% remaining |

---

## Rules

- **Exactly 5 questions** with 40/40/20 distribution (2 Easy + 2 Medium + 1 Hard).
- **G5–G11: no multiple choice.** Open response only.
- **≥1 primary source analysis question** required for History.
- **≥1 causal-framework application** required.
- **Hard question** must require synthesis (evaluation, counterfactual, multi-source) — not just harder recall.
- **Every question tagged** with Bloom / PISA / Skill / Damage / Standard.
- **Every question has a 3-hint ladder** with the tiered pattern above. Hint 3 uses **diagnostic questions, never answer templates.**
- **Failure language:** "Hali emas!" — never "Notoʻgʻri."
- **Textbook fidelity** — every correct answer verifiable from the source lesson.
- **Language:** Uzbek, `Siz`. Never `sen`.
- **Cross-reference previous phases** — hints point back to specific Preview panels, Flash Cards, or Memory Palace stations.
- **Weight:** Phase 6 = 40% of session score.
- **PISA tag MUST include L level.** Write `Reading L1`, `Reading L2`, `Creative Thinking L2`, etc. Never just `Reading` or `Creative Thinking` alone.
- **Output ONLY Phase 6 content.** Do NOT include Phase 7 Reflection, closing messages, XP awards, or Milliylik statements. Phase 7 is a separate prompt invocation with its own output.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
[
  {
    "q": "string",
    "tags": "[Bloom: LX | PISA: LX | Damage: -XX HP]",
    "ans": ["string", "string"],
    "hint": "string",
    "dmg": 10
  }
]
```
