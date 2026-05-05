# Prompt: Game Breaks — Physics

You are building the Game Breaks (Phase 3) for a Physics homework session. Real practice starts here — the student applies what they learned through gamified repetition.

## Input

- Textbook page + all previous phase outputs
- Grade: G7-11 (Fizika)
- Mode: Easy → **2 games** | Hard → **3 games**

## Output

2 or 3 games. Each game has 5-8 items. Every item tagged with `[Bloom: LX | PISA: LX]`.

---

## Available Games (v1 — pick from these only)

| Game | How it works | Physics use |
|------|-------------|------------|
| **Adaptive Quiz** | Question → answer → difficulty adjusts. Notebook Capture built in for calculation steps. | Formula application, unit conversion, problem solving |
| **Tile Match** | Drag pairs to match. 6-8 pairs. | Formula ↔ name, quantity ↔ unit, law ↔ discoverer, diagram ↔ concept |
| **Memory Match** | 4×4 flip grid, find matching pairs. | Term ↔ definition, symbol ↔ quantity, unit ↔ measurement |
| **Sentence Fill** | Statement with gap, student selects missing piece. | Missing variable in formula, missing unit, missing step in derivation |

## Game Selection

**Mandatory:** Adaptive Quiz in one slot (Notebook Capture on every calculation step).

**Easy (2 games):** Adaptive Quiz + pick 1.

**Hard (3 games):** Adaptive Quiz + pick 2. Vary the type.

Pick based on chapter:
- Formula-heavy chapter → Sentence Fill (fill missing variable: F = ___ × a)
- Terminology chapter → Memory Match (term ↔ definition pairs)
- Multi-concept chapter → Tile Match (formula ↔ quantity ↔ unit connections)

---

## Construction per game

### Adaptive Quiz
- 5-8 questions from THIS chapter
- Difficulty scales: first 2 easy, next 2-3 medium, last 1-2 hard
- Every calculation triggers Notebook Capture
- Must include unit tracking in every answer
- G7-8: MC allowed for conceptual questions. G9-11: open-ended only for calculations.

### Tile Match
- 6-8 pairs
- Physics pair types:
  - Formula ↔ law name: "F = ma" ↔ "Nyuton 2-qonuni"
  - Quantity ↔ unit: "Kuch" ↔ "N (Nyuton)"
  - Diagram ↔ concept: [Circuit with resistor] ↔ "Om qonuni"
  - Cause ↔ effect: "Harorat oshadi" ↔ "Jism kengayadi"

### Memory Match
- 4×4 grid (8 pairs)
- Symbol ↔ quantity: "F" ↔ "Kuch", "m" ↔ "Massa", "a" ↔ "Tezlanish"
- Term ↔ definition pairs

### Sentence Fill
- 5-7 items
- Physics-specific gaps:
  - "F = m × ___" (javob: a)
  - "Kuchning birligi — ___ (N)" (javob: Nyuton)
  - "Om qonuni: I = U / ___" (javob: R)
  - "Ish = Kuch × ___" (javob: ko'chirish)

---

## Rules

- Every item tagged: `[Bloom: LX | PISA: LX]`
- Notebook Capture built into Adaptive Quiz — not a separate game
- No frozen/removed games
- Current chapter content only
- All answers must include proper physics units
- Language: Uzbek, "Siz" formal
- Visuals: If a game item needs a diagram (circuit, force vector, graph), generate inline SVG. Keep simple — under 200×150px.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "adaptive_quiz": [
    {
      "q": "string",
      "tags": "[Bloom: LX | PISA: LX]",
      "tier": "EASY|MEDIUM|HARD",
      "ans": ["string"],
      "capture": false
    }
  ],
  "why_chain": [
    {
      "q": "string",
      "inv": "string",
      "reprompts": ["string", "string"]
    }
  ],
  "memory_match": [
    ["string", "string"]
  ]
}
```
