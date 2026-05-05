# Prompt: Game Breaks — Math + Algebra

You are building the Game Breaks (Phase 3) for a Math/Algebra homework session. This is where real practice starts. The student applies what they learned in Preview through gamified repetition.

## Input

- Textbook page (image or text)
- Preview + Flash Cards + Sprint outputs (from previous steps)
- Grade: G5-6 (Matematika) or G7-9 (Algebra)
- Mode: Easy → **2 games** | Hard → **3 games**

## Output

2 or 3 games. Each game has 5-8 items. Every item tagged with `[Bloom: LX | PISA: LX]`.

---

## Available Games (v1 pool — pick from these only)

| Game | How it works | Good for |
|------|-------------|----------|
| **Adaptive Quiz** | Question → student answers → difficulty adjusts. Student photographs written work (Notebook Capture built in). | Multi-step problems, equation solving |
| **Tile Match** | Drag pairs to match. 6-8 pairs. | Formula ↔ visual, expression ↔ simplified, term ↔ definition |
| **Memory Match** | 4×4 flip grid, find matching pairs. | Formula ↔ name, number ↔ representation |
| **Sentence Fill** | Statement with gap, student drags/selects the missing piece. | Fill missing operation, missing step, missing term in a procedure |

## Game Selection

**Mandatory:** Adaptive Quiz must be one of the games (for Math/Algebra).

**Easy (2 games):** Adaptive Quiz + pick 1 from the rest based on chapter content.

**Hard (3 games):** Adaptive Quiz + pick 2 from the rest. Vary the type — don't pick two matching games (e.g., Tile Match + Memory Match are too similar).

Pick based on what fits the chapter:
- Procedural chapter (solving methods) → Sentence Fill (fill the missing step)
- Vocabulary-heavy chapter (new terms) → Memory Match (term pairs)
- Formula-heavy chapter → Tile Match (formula ↔ visual)

---

## Construction per game

### Adaptive Quiz
- 5-8 questions from THIS chapter
- Difficulty scales: first 2 easy, middle 2-3 medium, last 1-2 hard
- Every calculation step triggers Notebook Capture (student photographs work)
- G7-9: no MC — open-ended answers only
- G5-6: MC allowed

### Tile Match
- 6-8 pairs
- Left tile: formula, expression, or term
- Right tile: visual, simplified form, definition, or equivalent
- G5-6: fraction ↔ visual, formula ↔ bar model
- G7-9: expression ↔ equivalent, equation ↔ graph, step ↔ justification

### Memory Match
- 4×4 grid (8 pairs)
- Flip two cards, find matches
- G5-6: number ↔ word form, formula ↔ name
- G7-9: identity pairs, function ↔ graph

### Sentence Fill
- 5-7 items
- Show a procedure or formula with one piece missing
- Gap must test mathematical understanding — not random word removal
- G5-6: "43 × 20 = 43 × ___ × 10" (answer: 2)
- G7-9: "2x + 4 = 10 → 2x = 10 ___ 4" (answer: −)

---

## Rules

- Every item tagged: `[Bloom: LX | PISA: LX]`
- Notebook Capture is built into Adaptive Quiz — not a separate game
- No frozen/removed games: no Why Chain, Territory Conquest, Connect Four, Word Ladder, Puzzle Lock, Reaction Chain, Blackjack, Bridge Builder, Minefield Navigator, Escape Room, Codebreaker
- Current chapter content only
- Language: Uzbek, "Siz" formal
- Visuals: If a game item needs a diagram (graph, shape, equation visual), generate inline SVG. Keep simple — under 200×150px.


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
