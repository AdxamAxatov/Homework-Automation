# Prompt: Game Breaks — Geometry

You are building the Game Breaks (Phase 3) for a Geometry homework session. This is where real practice starts. The student applies what they learned in Preview through gamified repetition.

## Input

- Textbook page (image or text)
- Preview + Flash Cards + Sprint outputs (from previous steps)
- Grade: G7-9 (Geometriya)
- Mode: Easy → **2 games** | Hard → **3 games**

## Output

> **SVG Rule:** Every diagram in every game (tile images, Notebook Capture reference figure, Puzzle Lock fragments) must be actual SVG code — not a bracket description alone. Use `instruction.md` → SVG Output Rule for templates, color hex codes, and mark syntax.

---

## Dual-Catalog Rule (mandatory)

- Easy (2 games): ≥1 from Interactive Catalog + ≥1 from Default Pool
- Hard (3 games): ≥1 from Interactive Catalog + ≥2 from Default Pool

---

## Game Slots — Geometry

| Slot | Role | Primary | Backup |
|------|------|---------|--------|
| **Slot 1** | Spatial reasoning warmup | **Puzzle Lock** — reconstruct a labeled diagram, order proof steps, assemble a shape from parts | **Mystery Box** — identify shape or theorem from property clues |
| **Slot 2** | Theorem application | **Tile Match** — theorem name ↔ diagram, angle type ↔ degree range, congruence criterion ↔ marked figure | **Sentence Fill** — fill missing reason in a proof step or missing condition in a theorem |
| **Slot 3** | Proof and kinesthetic | **Notebook Capture** — student draws the figure, labels all elements, solves or proves, uploads photo | **Reaction Chain** — sequential proof steps, each correct answer unlocks the next node |

**Notebook Capture is the highest priority mechanic for Geometry.** It must appear in at least 1 of every 2 Hard sessions.

**Adaptive Quiz** may replace any Default Pool slot when the chapter is calculation-heavy (angle sums, measurement problems).

---

## Games to AVOID for Geometry

- Word Ladder — linguistic, no geometric value
- Why Chain — Socratic text dialogue without diagrams does not work for geometry
- Speed Match with numbers only — no geometric reasoning
- Connect Four, Tic Tac Toe — low value for proof-based content
- Worked Examples without diagrams — text-only worked examples do not work in geometry

---

## Construction per game

### Puzzle Lock (Sliding Tile) — Interactive Catalog
- 8-12 tiles to arrange in the correct configuration
- Correct answer slides chosen tile; wrong answer slides a random tile
- Tile types:
  - **Diagram assembly:** labeled parts of a triangle or parallel-line figure to reconstruct
  - **Proof step ordering:** jumbled steps of a 3-5 step argument to put in logical order — include one distractor tile at L3
  - **Cross-section:** 3D object → student identifies the 2D cross-section shape
**Every tile that references a figure must include a Visual Layer diagram description** (tick marks, arcs, square corners, color codes).
- Good: `"SAS isbootini 5 qadamdan yig'ing: [Tile 1: triangles ABC/DEF, no marks — State 0] → [Tile 2: one tick on AB=DE, blue — State 1] → [Tile 3: arc at ∠B=∠E, blue — State 2] → [Tile 4: one tick on BC=EF, blue — State 3] → [Tile 5: both triangles orange, △ABC=△DEF — Conclusion]"`
- Good (diagram assembly): `"Ushbu △ABC rasmini yig'ing: [Tile: vertex A top], [Tile: vertex B bottom-left], [Tile: vertex C bottom-right], [Tile: one tick on AB], [Tile: one tick on AC], [Tile: arc at ∠B = arc at ∠C], [Tile: label 'teng yonli uchburchak']"`
- Bad: All tiles are text definitions with no diagram fragments

### Mystery Box — Default Pool
- 3-5 closed boxes, each containing a geometry problem from a different topic of the current chapter
- Student first names the theorem or shape type (identifies the box's content), then solves
- Use only for practice/review sessions (§4, §7, §13, §17, §22, §24, §26) or when chapter covers multiple theorems

### Tile Match — Default Pool
- 6-8 pairs. Left tile = theorem name, angle type, or congruence criterion. Right tile = labeled diagram.
- Every right tile must be a diagram description using Visual Layer notation — no text-only pairs
- Pair types:
  - Theorem name ↔ diagram: `"SAS belgisi"` ↔ `[Diagram: triangles ABC and DEF, one tick on AB=DE (blue), one tick on BC=EF (blue), single arc at ∠B=∠E (blue)]`
  - Angle type ↔ diagram: `"O'tmas burchak"` ↔ `[Diagram: rays BA and BC, wide arc inside showing angle > 90°, label "90° < α < 180°"]`
  - Notation ↔ diagram: `"AB ∥ CD"` ↔ `[Diagram: two horizontal lines with single arrows, gap between them, symbol ∥ labeled]`
  - Mark ↔ meaning: `[Diagram: single tick mark on segment]` ↔ `"Bu tomon boshqa bir tomon bilan teng"`
- Difficulty: L1 name ↔ symbol → L2 theorem ↔ fully marked diagram → L3 criterion ↔ real-scenario diagram with partial marks (student identifies which criterion fits)
- **Include at least 1 pair where the diagram has a deliberate wrong mark** — student must identify it as a non-match (builds error-detection instinct)

### Sentence Fill — Default Pool
- 5-7 items. Proof step or theorem statement with one piece missing.
- Gap must test geometric understanding — not random word removal
- Good: `"∠ABC va ∠BCD — ___ burchaklar (AB ∥ CD bo'lganda)"` → almashma ichki
- Good: `"△ABC = △DEF, chunki AB=DE, ∠B=∠E, BC=EF → ___ belgisi asosida"` → SAS
- Good: `"Uchburchak ichki burchaklari yig'indisi ___ ga teng"` → 180°

### Adaptive Quiz — Default Pool
- 5-8 questions from THIS chapter only
- Difficulty scales: first 2 easy, middle 2-3 medium, last 1-2 hard
- G7-9: no MC — open-ended answers only
- Every proof or construction step triggers Notebook Capture (student photographs work)
- Every question involving a shape MUST include a diagram described in brackets

### Notebook Capture — Default Pool
- Student draws a labeled geometric figure on paper, solves or proves, photographs and uploads
- Must specify: figure type, all given measurements (cm or °), what to find or prove
- The prompt includes a **reference diagram in brackets** — student must replicate this diagram on paper, then add their own marks as they solve

**Student drawing requirements (must be stated explicitly in the prompt):**
- Label ALL vertices (A, B, C), all sides (AB, BC, CA), all angles (∠A, ∠B, ∠C)
- Mark equal sides with tick marks, equal angles with arc marks, right angles with a square corner symbol
- Color code if possible: blue for given, orange for found/proved
- Write the theorem name next to the step where it is used
- Write the final answer with units and circle it

**Prompt structure for Notebook Capture:**
1. Reference diagram in brackets (using Visual Layer notation) — student recreates this on paper
2. What to add: marks that are given (blue)
3. What to find or prove (orange)
4. Theorem to name and cite at each step

- Good: `"[Reference diagram: triangle ABC, right angle square at ∠B, BC = 4 sm, AB = 3 sm — copy this to your notebook] ∠B ni □ bilan belgilang. O'tkir burchaklarini arc bilan belgilang. ∠A + ∠C yig'indisini toping. Ishlatingan teoremani yozing."`
- Bad: `"Uchburchak ta'rifini yozing."` — definition copy, not construction or proof

### Reaction Chain — Interactive Catalog
- 6-10 nodes in logical sequence. Each correct answer lights the next node. 3 wrong = chain breaks.
- Chain types:
  - **Proof chain:** each node = one step of a formal proof (identify given → cite theorem → first deduction → second deduction → conclusion)
  - **Angle calculation chain:** find angle 1 → use it to find angle 2 → use that to find angle 3
- Good: Node 1: `"△ABC da ∠A = 50°, ∠B = 70°. Barcha burchaklar yig'indisi?"` → 180° → Node 2: `"∠C ni toping"` → 60° → Node 3: `"Bu uchburchak qaysi turga kiradi?"` → o'tkir burchakli
- Bad: Unrelated questions with no logical dependency between nodes

---

## Rules

- Every question involving a shape references a diagram in brackets
- Dual-Catalog Rule enforced every session
- Notebook Capture mandatory in Hard mode — at minimum every 2 sessions
- Current chapter content only — no questions from other chapters
- Language: Uzbek, "Siz" formal


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
