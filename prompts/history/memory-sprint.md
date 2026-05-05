# Prompt: Memory Sprint — History (O'zbekiston Tarixi + Jahon Tarixi)

You are building the Memory Sprint (Phase 1) for a History homework session. This is a quick warm-up — tap-only, under 2 minutes. The student just finished Preview and Flash Cards. Now you activate what they learned with fast recognition questions.

This is NOT real practice. No reasoning chains, no source analysis, no multi-step inference. Just: do you remember the key figures, dates, terms, and claims from this lesson?

## Input

- Textbook lesson content (extracted in orchestrator Step 1)
- Preview output + Flash Cards output (from previous steps)
- Grade: G5–G11
- Subject: `O'zbekiston Tarixi` or `Jahon Tarixi`

## Output

**7 items.** Must use at least 2 of the 3 approved formats.

**Distribution:** 3 MC + 2 T/F + 2 YNNG.

Place the most foundational/identity-anchoring item FIRST (**Buzan Primacy** — the brain locks in what it sees first).

All items in Uzbek, formal "Siz" if addressing the student.

---

## 3 Formats — ONLY these

### Multiple Choice (MC)

Question + 4 options. 1 correct, 3 wrong.

Wrong options must come from **real confusions a student could make** — not random:

- **Figure confusion** — wrong ruler, scholar, or dynasty attributed to a fact
- **Date confusion** — adjacent year, or wrong reign period
- **Attribution confusion** — wrong reform attributed to wrong person
- **Family/succession confusion** — wrong son, heir, or successor
- **Era confusion** — event placed in wrong century

Example:
> 1321-yilgi "kepaki" pul islohoti qaysi hukmdor tomonidan amalga oshirilgan?
> A) Chigʻatoyxon  B) Masʼudbek Yalavoch  C) Kebekxon ✓  D) Alouddin Tarmashirinxon
> (A = wrong era; B = did 1271 reform, not 1321; D = made Islam official, not coins.)

### True / False (T/F)

A statement. Student taps Toʻgʻri or Notoʻgʻri.

Must test a **rule** or **common misconception** — not trivial facts.

- BAD: *"Chigʻatoyxon 1242-yili vafot etgan."* (trivial fact)
- GOOD: *"Chigʻatoy ulusidagi barcha xonlar Yasoqqa sodiq qolgan."* (tests misconception — Tarmashirin is counter-example)

### Yes / No / Not Given (YNNG)

Statement about THIS chapter's content. Student taps Ha / Yoʻq / Aytilmagan.

"Aytilmagan" means the chapter doesn't address this claim. **At least 1 item** per sprint must have "Aytilmagan" as the correct answer.

Example:
> "Bobga koʻra, Kebekxon arab alifbosini Chigʻatoy ulusida joriy qilgan."
> — Ha / Yoʻq / **Aytilmagan** ✓
> (Chapter discusses Kebek's tuman, kepaki, and capital move — but nothing about alphabet reform.)

---

## Item tagging

Every item carries inline tags on its own line:

```
[Bloom: LX | PISA: Reading/Creative Thinking LX | Skill: Memory/Critical Thinking/... | Standard: UZ-TARIX-G-TOPIC-##]
```

Bloom range L1–L3 for Sprint — recognition warm-up, not analysis.

---

## Rules

- **Tap only.** No typing, drag-and-drop, fill-in-blank, or open-ended.
- **2 minutes max.** Read and tap fast.
- **Current chapter only.** No items drawing from prior or future chapters.
- **No hints.** Help is not available in Sprint.
- **Forward-leak ban:** no items referencing content that hasn't been introduced in Preview or Flash Cards.
- **Textbook fidelity:** every correct answer verifiable from the source lesson.
- **Wrong-answer feedback:** show WHY the correct answer is correct in one line. Don't just reveal the answer.
- **Format mix:** use ≥2 of the 3 formats.
- **Primacy ordering:** most foundational item first.
- **Standards reference** on every item: `UZ-TARIX-G-TOPIC-##`.
- **PISA tag MUST include L level.** Write `Reading L1`, `Reading L2`, `Creative Thinking L2`, etc. Never just `Reading` or `Creative Thinking` alone.
- **Language:** Uzbek, `Siz` when addressing student. Never `sen`.
- **No calculation.** History is non-calc — no arithmetic, no formulas, no numeric computation required of the student.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
[
  {
    "type": "KO|TF|YNNG",
    "prompt": "string",
    "subtitle": "",
    "tags": "[Bloom: LX | PISA: LX]",
    "explain": "string",
    "options": ["string", "string"],
    "correct": 0
  }
]
```
