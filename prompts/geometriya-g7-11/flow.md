# Geometriya — Prompt Flow

## Step 0: Classify

Run `classify.md` on the textbook page → **EASY** or **HARD**.

---

## Easy (5 phases)

`classify → preview-easy → flashcards → memory-sprint → game-breaks → reflection`

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-easy.md` | 5 panels: Summary (Diagram Anatomy block), Better Explanation (CPA arc + labeled diagram), Examples (comparison strip), Origin (Euclid / Thales / Al-Biruni), Industry Application |
| 2 | `flashcards.md` | 6–10 cards: geometric terms with diagram descriptions, notation symbols (∠, △, ⊥, ∥), mark meanings (tick, arc, square corner) |
| 3 | `memory-sprint.md` | 10–15 items: shape/angle recognition, theorem name recall, notation reading |
| 4 | `game-breaks.md` | 2 games: Puzzle Lock (Interactive Catalog) + one of Mystery Box / Tile Match / Sentence Fill / Adaptive Quiz (Default Pool) |
| 5 | `reflection.md` | Summary + question + spaced rep + closing |

**Skipped:** Diagram→Theorem Translation, Industry Application panel 6, Why This Matters, Real-Life, Consolidation, Final Challenge.

---

## Hard (8 phases)

`classify → preview-hard → flashcards → memory-sprint → game-breaks → real-life → consolidation? → final-challenge → reflection`

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-hard.md` | 7 panels: Summary (Diagram Anatomy block + proof roadmap), Better Explanation (CPA + Diagram Legend + color-coded given/prove), Examples (progressive diagram states), Origin (genetic method), Diagram→Theorem Translation, Industry Application, Why This Matters |
| 2 | `flashcards.md` | 8–12 cards: theorem names, congruence criteria, mark meanings, notation symbols with SVG diagram references |
| 3 | `memory-sprint.md` | 15–20 items: theorem identification from diagram marks, proof step ordering, notation matching |
| 4 | `game-breaks.md` | 3 games: Puzzle Lock (Interactive Catalog) + 2 from Default Pool (Mystery Box / Tile Match / Sentence Fill / Notebook Capture / Reaction Chain / Adaptive Quiz) |
| 5 | `real-life.md` | Design or construction problem requiring theorem application; student draws labeled figure and proves |
| 6 | `consolidation.md` | Mnemonic for proof structure or theorem conditions (SKIP if chapter covers single definition only) |
| 7 | `final-challenge.md` | Boss fight, 5–8 questions, no MC for G7+, HP: G7–9=100 |
| 8 | `reflection.md` | Summary + BOST goal recall + spaced rep + closing |

---

## Assembly

All phase outputs assembled into a single `.md` file — that is the final homework. Each phase becomes a section in order.

---

## Notes

- **Covers:** Geometriya G7–9
- **Games:** Puzzle Lock, Mystery Box, Tile Match, Sentence Fill, Notebook Capture, Reaction Chain, Adaptive Quiz
- **Teaching:** Every diagram description in brackets must be followed immediately by actual SVG code — no text-only diagrams.
- **Teaching:** Diagram Anatomy block mandatory in Panel 1 — fully labeled reference figure for the session.
- **Teaching:** Progressive diagram states (State 0 → State N) for all proof examples — diagram built step by step, never static.
- **Teaching:** Every proof step cites theorem name before being applied: "SAS belgisi asosida."
- **Teaching:** Notebook Capture mandatory in Hard mode (at minimum every 2 sessions) — student draws figure, labels all elements, photographs.
- **Visual layer:** SVG Diagram Notation — tick marks, arc marks, right-angle squares, parallel arrows. Color: #2563EB blue=given, #EA580C orange=to prove, #16A34A green=construction, #DC2626 red=error, #9CA3AF grey=context.
- **Language:** Uzbek (or Russian if textbook is Russian). Formal "Siz" throughout — never "sen."
- **HP:** G7–9 = 100 HP
