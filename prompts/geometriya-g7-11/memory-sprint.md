# Prompt: Memory Sprint — Geometry

You are building the Memory Sprint (Phase 1) for a Geometry homework session. This is a quick warm-up — tap-only, under 2 minutes. The student just finished Preview and Flash Cards. Now you activate what they learned with fast recognition questions.

This is NOT real practice. No proofs, no multi-step solving. Just: do you recognize the theorem, the shape, or the angle type?

## Input

- Textbook page (image or text)
- Preview output + Flash Cards output (from previous steps)
- Grade: G7-9 (Geometriya)
- Mode: Easy → **5 items** | Hard → **7 items**

## Output

5 or 7 items. Each item is one of 3 formats. Must use at least 2 different formats.

> **SVG Rule:** Diagram Tap (DT) questions and any question that references a shape or angle must include actual SVG code immediately after the bracket description. Use `instruction.md` → SVG Output Rule. Wrong-answer feedback must show the diagram with the correct element highlighted in green SVG.

---

## 4 Formats (ONLY these — nothing else)

### Multiple Choice (MC)
- Question + 4 options. 1 correct, 3 wrong.
- Each wrong option must come from a real student mistake — not random:
  - Wrong theorem applied (SSS instead of SAS)
  - Confused angle types (obtuse vs reflex)
  - Misread diagram (wrong vertex labeling)
- When a shape or angle is involved, reference a diagram using Visual Layer notation: `[Diagram: ...]`

Example:
> `[Diagram: triangles ABC and DEF, one tick on AB and DE (blue), single arc at ∠B and ∠E (blue), one tick on BC and EF (blue)]`
> Bu uchburchaklar qaysi belgi asosida teng?
> A) SAS ✓  B) SSS  C) ASA  D) Teng emas

### True / False (T/F)
- A statement. Student taps To'g'ri or Noto'g'ri.
- Must test a THEOREM or common MISCONCEPTION — not trivial naming.
- BAD: "To'g'ri burchak 90° ga teng — To'g'ri yoki Noto'g'ri?" (trivial)
- GOOD: "Har qanday teng yonli uchburchakning asosi burchaklari teng — To'g'ri yoki Noto'g'ri?"

### Yes / No / Not Given (YNNG)
- Statement about THIS chapter's content. Student taps Ha / Yo'q / Aytilmagan.
- "Aytilmagan" means the chapter doesn't address this claim.
- Include at least 1 item with "Aytilmagan" as correct answer.

Example:
> "Bobda aytilganiga ko'ra, har qanday uchburchakning tashqi burchagi ichki burchaklar yig'indisiga teng — Ha / Yo'q / Aytilmagan"

### Diagram Tap (DT) — Geometry only
- Show a labeled diagram. Student taps ONE element (a side, an angle, a vertex, a mark) that answers a specific question.
- The diagram uses full Visual Layer notation — marks already shown, one element highlighted with orange question mark.
- No typing, no dragging — single tap on the correct element.
- Used for: "Qaysi tomon tengligini isbot qilish kerak?", "Qaysi burchak berilmagan?", "Nechta o'tkir burchak bor?"

Example:
> `[Diagram: triangle ABC with angles ∠A = 50°, ∠B labeled with "?", ∠C = 70°, orange question mark on ∠B]`
> ∠B ni toping.
> (Student taps the angle — then types or selects the value: 60°)

Example:
> `[Diagram: complex figure with 4 triangles formed by two intersecting lines, triangles not labeled — student must count]`
> Bu rasmda nechta uchburchak bor?
> A) 2  B) 3  C) 4 ✓  D) 6

**Diagram Tap is mandatory: ≥1 DT item per sprint.** This is the format that directly trains the diagram-reading skill used in Panel 5 and Real-Life.

---

## Geometry-specific additions (mandatory)

- Include 1-2 **diagram-reading questions** — reference a labeled figure and ask to identify a shape type, angle type, or count elements
- Every question involving a shape MUST reference a diagram using Visual Layer notation
- Wrong answer feedback: show the annotated diagram with the correct element highlighted in green — one sentence explaining why

---

## Item distribution

**5 items (Easy):** 2 MC + 1 T/F + 1 YNNG + 1 DT

**7 items (Hard):** 2 MC + 1 T/F + 1 YNNG + 2 DT + 1 MC or T/F

Put the most important theorem or concept as item 1. The brain remembers what it sees first.

---

## Rules

- **Tap only.** No typing, no drag-and-drop, no fill-in-blank, no open-ended.
- **2 minutes max.** Keep items fast — read and tap.
- **Current chapter only.** No items from other chapters.
- **No hints.** No help available in this phase.
- **No proofs.** If answering requires a written logical argument, it doesn't belong here.
- **Every shape or angle question references a diagram** described in brackets.
- **Wrong answer feedback:** Show WHY the correct answer is correct in one line with diagram reference.
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
