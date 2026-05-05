# Prompt: Memory Sprint — Biology (Biologiya G5-11)

You are building the Memory Sprint (Phase 1) for a Biology homework session. Quick warm-up — tap-only, under 2 minutes. The student just finished Preview and Flash Cards. Now you activate what they learned with fast recognition questions.

NOT real practice. No open-ended reasoning, no multi-step analysis. Just: do you recognize this organism, structure, process, or classification?

## Input

- Textbook page (image or text)
- Preview output + Flash Cards output
- Grade: G5-11 (Biologiya)
- Mode: Easy → **5 items** | Hard → **7 items**

## Output

5 or 7 items. Each item is one of 3 formats. Must use at least 2 different formats.

---

## 3 Formats (ONLY these)

### Multiple Choice (MC)
- Question + 4 options. 1 correct, 3 wrong.
- Wrong options must come from real student mistakes:
  - Confused organism kingdom (called a fungus a plant)
  - Mixed up structure and function (said mitochondria makes proteins)
  - Wrong classification level (said "oila" when the answer is "turkum")

Biology-specific question types for MC:
- Diagram recognition: describe a structure in brackets and ask what it is
- Process identification: what does this process produce?
- Organism classification: which kingdom/phylum does this belong to?

Example:
> [Yashil, oval, ichida tilakoidlar bo'lgan organoid — diagramda ko'rsatilgan]
> Bu organoid nima deb ataladi?
> A) Xloroplast ✓  B) Mitoxondriya  C) Vakuola  D) Yadro

### True / False (T/F)
- Test a PROCESS RULE or common MISCONCEPTION — not trivial name facts.
- BAD: "Fotosintez o'simliklarda bo'ladi — To'g'ri yoki Noto'g'ri?" (trivial)
- GOOD: "Fotosintez faqat yorug'likda amalga oshadi — To'g'ri yoki Noto'g'ri?" (misconception check — To'g'ri)
- GOOD: "Barcha bakteriyalar kasallik qo'zg'atadi — To'g'ri yoki Noto'g'ri?" (misconception — Noto'g'ri)

### Yes / No / Not Given (YNNG)
- Statement about THIS chapter's content.
- Include at least 1 "Aytilmagan" answer.

Example:
> "Bobda aytilganiga ko'ra, har bir hujayrada yadro mavjud — Ha / Yo'q / Aytilmagan"

---

## Item distribution

**5 items (Easy):** 3 MC + 1 T/F + 1 YNNG

**7 items (Hard):** 3 MC + 2 T/F + 2 YNNG

Most important concept (or most commonly confused structure/process) as item 1.

---

## Biology-specific question guidance

- **Taxonomy/classification chapter:** MC on kingdom/phylum placement, T/F on classification rules
- **Process chapter (photosynthesis, digestion, mitosis):** MC on what is produced, T/F on conditions required
- **Structure chapter (cell, organ systems):** MC on structure-function matching, YNNG on whether a fact was stated in this chapter
- **When referencing a diagram or structure:** describe it in brackets before the question, e.g., `[Dumaloq, ikki membranali, o'z DNAsi bor organoid]`

---

## Rules

- **Tap only.** No typing, no drag-and-drop, no fill-in-blank, no open-ended questions.
- **2 minutes max.**
- **Current chapter only.**
- **No hints.**
- **Wrong answer feedback:** one line explaining WHY the correct answer is correct.
- **Every item tagged:** `[Bloom: LX | PISA: LX]`
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
