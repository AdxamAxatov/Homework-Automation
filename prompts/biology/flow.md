# Biology — Prompt Flow

## Step 0: Classify

Run `classify.md` on the textbook page → **EASY** or **HARD**.

---

## Easy (5 phases)

```
classify → preview-easy → flashcards → memory-sprint (5) → game-breaks (2) → reflection
```

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-easy.md` | 4 panels: Observation Hook, What It Does, Origin/Discovery, Real-World Connection |
| 2 | `flashcards.md` | 5-8 cards: term + definition or organism + trait |
| 3 | `memory-sprint.md` | 5 items: MC/TF/YNNG, tap-only, ≥2 formats |
| 4 | `game-breaks.md` | 2 games: Adaptive Quiz (mandatory) + 1 other (Tile Match or Memory Match) |
| 5 | `reflection.md` | Summary + open question + spaced rep + closing |

**Skipped:** Real-Life, Consolidation, Final Challenge.

---

## Hard (8 phases)

```
classify → preview-hard → flashcards → memory-sprint (7) → game-breaks (3) → real-life → consolidation? → final-challenge → reflection
```

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-hard.md` | 6 panels: Observation Hook, What It Does, Mechanism/Process Steps, Origin/Discovery, Real-World Connection, Why This Matters |
| 2 | `flashcards.md` | 8-12 cards: terms, process stages, organism↔function pairs |
| 3 | `memory-sprint.md` | 7 items: MC/TF/YNNG, tap-only, ≥2 formats |
| 4 | `game-breaks.md` | 3 games: Adaptive Quiz (mandatory) + Tile Match + Memory Match or Sentence Fill |
| 5 | `real-life.md` | Narrative-process scenario: flowing story of the biological process (matches textbook) → 2-3 questions |
| 6 | `consolidation.md` | Mnemonic or concept map (SKIP if single concept — TF-6) |
| 7 | `final-challenge.md` | Boss fight, 4-6 questions, HP: G5-8=100, G9-11=150 |
| 8 | `reflection.md` | Summary + open question + spaced rep + closing |

---

## Assembly

All phase outputs are assembled into a single `.md` file — that is the final homework. Each phase becomes a section in order. Biology homework may include inline SVG blocks within section headers for structural/process content.

---

## Notes

- Covers: Biologiya G5-11
- Games (v1 only): Adaptive Quiz, Tile Match, Memory Match, Sentence Fill. No Notebook Capture — Biology exempt from calculation capture (TF-1).
- Teaching sequence: observation-first (SEE → DO → HOW → WHAT) — never lead with terminology
- Real-Life: narrative-process format (photosynthesis pattern) — one flowing process story, then 2-3 questions from it. Not a word-problem or scenario-problem format.
- Consolidation: fires only when ≥2 distinct interlocking concepts taught (e.g., mitosis + meiosis compared, or photosynthesis + respiration as linked cycles). Skip for single-concept lessons.
- SVG critical: cell diagrams, organism anatomy, process/cycle flows, food chains, classification trees, organ system maps. Priority: SVG > Mermaid > ASCII. Preview panels max 300×200 px; game panels max 200×150 px.
- Boss HP: G5-8 = 100 HP | G9-11 = 150 HP
- No MC in Final Boss for G6+. G5 allows up to 30% MC.
- All content in Uzbek, "Siz" formal — never "sen"
- Modern professional contexts only: medical lab, agritech IoT, pharmaceutical research, environmental monitoring, clinical diagnostics — never bazaar/village/shopkeeper
- Removed/frozen games — never select: Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Codebreaker, Territory Conquest, Why Chain, Connect Four, Word Ladder, Puzzle Lock, Reaction Chain
