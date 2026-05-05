# Prompt: Game Breaks — Biology (Biologiya G5-11)

You are building the Game Breaks (Phase 3) for a Biology homework session. Real practice starts here — the student applies what they learned through gamified repetition.

## Input

- Textbook page + all previous phase outputs
- Grade: G5-11 (Biologiya)
- Mode: Easy → **2 games** | Hard → **3 games**

## Output

2 or 3 games. Each game has 5-8 items. Every item tagged with `[Bloom: LX | PISA: LX]`.

---

## Available Games (v1 — pick from these only)

| Game | How it works | Biology use |
|------|-------------|------------|
| **Adaptive Quiz** | Question → answer → difficulty adjusts. | Organism identification, process recall, structure-function questions. **Mandatory for Biology.** No Notebook Capture (no calculations in Biology). |
| **Tile Match** | Drag pairs to match. 6-8 pairs. | Structure ↔ function, organism ↔ classification, process ↔ result |
| **Memory Match** | 4×4 flip grid, find matching pairs. | Term ↔ diagram description, organism ↔ phylum, structure ↔ function |
| **Sentence Fill** | Statement with gap, student selects missing piece. | Process descriptions with one missing step or organism |

## Game Selection

**Mandatory:** Adaptive Quiz in one slot. No Notebook Capture (Biology has no calculations).

**Easy (2 games):** Adaptive Quiz + pick 1.

**Hard (3 games):** Adaptive Quiz + pick 2. Vary the type.

Pick based on chapter type:
- **Taxonomy/classification chapter** → Memory Match (organism ↔ kingdom/phylum pairs)
- **Process chapter** (photosynthesis, digestion, mitosis, respiration) → Sentence Fill (missing step or product in the process)
- **Structure chapter** (cell organelles, organ systems, tissue types) → Tile Match (structure ↔ function)
- **Mixed chapter** → Tile Match + Memory Match (cover both terminology and classification)

---

## Construction per game

### Adaptive Quiz
- 5-8 questions from THIS chapter
- Difficulty scales: first 2 easy (name recognition), next 2-3 medium (structure-function), last 1-2 hard (process reasoning or classification edge case)
- NO Notebook Capture — Biology does not require calculation steps
- G5-7: MC allowed for all question types
- G8-11: open-ended identification for hard-tier questions (student types organism/process name)
- Bloom levels must span L1 (recall) → L3 (application) across the set

### Tile Match
- 6-8 pairs
- Biology pair types:
  - Structure ↔ function: "Mitoxondriya" ↔ "ATP ishlab chiqaradi"
  - Organism ↔ classification: "Amyoba" ↔ "Sarcodina tipi"
  - Process ↔ result: "Fotosintez" ↔ "O₂ va glukoza hosil bo'ladi"
  - Cause ↔ effect: "Xlorofill quyosh nurini yutadi" ↔ "Fotosintez boshlanadi"
- If a structure needs a diagram to be recognizable, include a small inline SVG (under 200×150px)

### Memory Match
- 4×4 grid (8 pairs)
- Biology pair types:
  - Term ↔ diagram description: "Yadro" ↔ [Dumaloq, membranali, DNAni saqlaydi]
  - Organism ↔ phylum: "Gidra" ↔ "Tssellenteratlar tipi"
  - Structure ↔ function: "Vakuola" ↔ "Suv va moddalarni saqlaydi"
- If a tile represents a structure that students recognize visually, include a minimal SVG on that tile

### Sentence Fill
- 5-7 items
- Biology-specific gaps:
  - "Fotosintez jarayonida o'simlik ___ ni yutadi" (javob: CO₂)
  - "Mitoz natijasida ___ ta qiz hujayra hosil bo'ladi" (javob: 2)
  - "Xloroplastdagi yashil pigment ___ deb ataladi" (javob: xlorofill)
  - "Odam teri epiteliysi ___ to'qima turiga kiradi" (javob: epiteliy)
  - "Zamburug'lar ___ yo'l bilan oziqlanadi" (javob: heterotrofik)
- Each gap must have exactly one correct answer selectable from 3-4 options (tap to select)

---

## Rules

- Every item tagged: `[Bloom: LX | PISA: LX]`
- No Notebook Capture in Biology (no calculations)
- No frozen/removed games: no Why Chain, Territory Conquest, Connect Four, Word Ladder, Puzzle Lock, Reaction Chain, Blackjack, Bridge Builder, Minefield Navigator, Escape Room, Codebreaker
- Current chapter content only
- Language: Uzbek, "Siz" formal
- Visuals: If a game item references a structure or organism that students identify visually (cell organelle, leaf cross-section, organism diagram), generate an inline SVG. Keep simple — under 200×150px.


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
