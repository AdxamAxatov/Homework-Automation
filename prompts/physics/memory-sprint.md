# Prompt: Memory Sprint — Physics

You are building the Memory Sprint (Phase 1) for a Physics homework session. Quick warm-up — tap-only, under 2 minutes. The student just finished Preview and Flash Cards. Now you activate what they learned with fast recognition questions.

NOT real practice. No calculation, no multi-step solving. Just: do you remember the key terms, laws, and units?

## Input

- Textbook page (image or text)
- Preview output + Flash Cards output
- Grade: G7-11 (Fizika)
- Mode: Easy → **5 items** | Hard → **7 items**

## Output

5 or 7 items. Each item is one of 3 formats. Must use at least 2 different formats.

---

## 3 Formats (ONLY these)

### Multiple Choice (MC)
- Question + 4 options. 1 correct, 3 wrong.
- Wrong options must come from real student mistakes:
  - Wrong unit (Newton instead of Joule)
  - Wrong formula applied (used v=s/t instead of F=ma)
  - Confused quantity (mixed up mass and weight)

Example:
> Kuchning o'lchov birligi nima?
> A) Nyuton (N) ✓  B) Joul (J)  C) Vatt (W)  D) Paskal (Pa)

### True / False (T/F)
- Test a LAW or common MISCONCEPTION — not trivial facts.
- BAD: "Nyuton ingliz olimi — To'g'ri yoki Noto'g'ri?" (trivia)
- GOOD: "Og'ir jism yengil jismdan tezroq tushadi — To'g'ri yoki Noto'g'ri?" (misconception — Noto'g'ri)

### Yes / No / Not Given (YNNG)
- Statement about THIS chapter's content.
- Include at least 1 "Aytilmagan" answer.

Example:
> "Bobda aytilganiga ko'ra, magnit maydoni faqat temirga ta'sir qiladi — Ha / Yo'q / Aytilmagan"

---

## Item distribution

**5 items (Easy):** 3 MC + 1 T/F + 1 YNNG

**7 items (Hard):** 3 MC + 2 T/F + 2 YNNG

Most important concept as item 1.

---

## Rules

- **Tap only.** No typing, no drag-and-drop, no fill-in-blank.
- **2 minutes max.**
- **Current chapter only.**
- **No hints.**
- **No calculation.** If it needs pen and paper, it doesn't belong here.
- **Wrong answer feedback:** one line explaining WHY the correct answer is correct.
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
