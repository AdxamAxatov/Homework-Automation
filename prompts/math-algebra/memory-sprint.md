# Prompt: Memory Sprint — Math + Algebra

You are building the Memory Sprint (Phase 1) for a Math/Algebra homework session. This is a quick warm-up — tap-only, under 2 minutes. The student just finished Preview and Flash Cards. Now you activate what they learned with fast recognition questions.

This is NOT real practice. No calculation, no multi-step solving. Just: do you remember the key terms and rules?

## Input

- Textbook page (image or text)
- Preview output + Flash Cards output (from previous steps)
- Grade: G5-6 (Matematika) or G7-9 (Algebra)
- Mode: Easy → **5 items** | Hard → **7 items**

## Output

5 or 7 items. Each item is one of 3 formats. Must use at least 2 different formats.

---

## 3 Formats (ONLY these — nothing else)

### Multiple Choice (MC)
- Question + 4 options. 1 correct, 3 wrong.
- Each wrong option must come from a real student mistake — not random:
  - Wrong operation (added instead of multiplied)
  - Sign or place-value error (forgot a zero, wrong digit)
  - Partial answer (stopped one step early)

Example:
> 43 × 20 = ?
> A) 860 ✓  B) 86  C) 8600  D) 830
> (B = forgot ×10, C = extra zero, D = arithmetic error)

### True / False (T/F)
- A statement. Student taps To'g'ri or Noto'g'ri.
- Must test a RULE or common MISCONCEPTION — not trivial arithmetic.
- BAD: "43 × 2 = 86 — To'g'ri yoki Noto'g'ri?" (trivial)
- GOOD: "68 × 400 ni hisoblashda avval 400 ni 4 × 100 ga ajratish mumkin — To'g'ri yoki Noto'g'ri?"

### Yes / No / Not Given (YNNG)
- Statement about THIS chapter's content. Student taps Ha / Yo'q / Aytilmagan.
- "Aytilmagan" means the chapter doesn't address this claim.
- Include at least 1 item with "Aytilmagan" as correct answer.

Example:
> "Bobda aytilganiga ko'ra, minglikka ko'paytirishda uchta nol qo'shiladi — Ha / Yo'q / Aytilmagan"

---

## Item distribution

**5 items (Easy):** 3 MC + 1 T/F + 1 YNNG

**7 items (Hard):** 3 MC + 2 T/F + 2 YNNG

Put the most important concept as item 1. The brain remembers what it sees first.

---

## Rules

- **Tap only.** No typing, no drag-and-drop, no fill-in-blank, no open-ended.
- **2 minutes max.** Keep items fast — read and tap.
- **Current chapter only.** No items from other chapters.
- **No hints.** No help available in this phase.
- **No calculation.** If solving the item requires pen and paper, it doesn't belong here.
- **Wrong answer feedback:** Show WHY the correct answer is correct in one line. Don't just reveal the answer.
- Language: Uzbek, "Siz" formal.


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
