# Math + Algebra — Prompt Flow

## Step 0: Classify

Run `classify.md` on the textbook page → **EASY** or **HARD**.

---

## Easy (5 phases)

```
classify → preview-easy → flashcards → memory-sprint (5) → game-breaks (2) → reflection
```

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-easy.md` | 5 panels: Summary, Explanation (CPA), Examples, Origin, Industry Application |
| 2 | `flashcards.md` | 5-8 cards: name + formula |
| 3 | `memory-sprint.md` | 5 items: MC/TF/YNNG, tap-only |
| 4 | `game-breaks.md` | 2 games: Adaptive Quiz (mandatory) + 1 other |
| 5 | `reflection.md` | Summary + question + spaced rep + closing |

**Skipped:** Real-Life, Consolidation, Final Challenge.

---

## Hard (8 phases)

```
classify → preview-hard → flashcards → memory-sprint (7) → game-breaks (3) → real-life → consolidation? → final-challenge → reflection
```

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-hard.md` | 7 panels: Summary, Explanation (CPA), Examples, Origin, Word→Formula Translation, Industry Application, Why This Matters |
| 2 | `flashcards.md` | 8-12 cards |
| 3 | `memory-sprint.md` | 7 items |
| 4 | `game-breaks.md` | 3 games: Adaptive Quiz (mandatory) + 2 others |
| 5 | `real-life.md` | 1 scenario, 4-6 sub-questions, first-person expert |
| 6 | `consolidation.md` | Mnemonic lock (SKIP if single concept) |
| 7 | `final-challenge.md` | Boss fight, 4-6 questions, HP: G5-6=80, G7-9=100 |
| 8 | `reflection.md` | Summary + question + spaced rep + closing |

---

## Assembly

All phase outputs are assembled into a single `.md` file — that is the final homework. Each phase becomes a section in order.

---

## Notes

- Covers: Matematika G5-6, Algebra G7-9
- Games: Adaptive Quiz, Tile Match, Memory Match, Sentence Fill (Notebook Capture built into Adaptive Quiz)
- Teaching: CPA mandatory G5-6, genetic method, no magic moves
- All content in Uzbek, "Siz" formal
