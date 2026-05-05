# Kimyo — Prompt Flow

## Step 0: Classify

Run `classify.md` on the textbook page → **EASY** or **HARD**.

---

## Easy (5 phases)

`classify → preview-easy → flashcards → memory-sprint → game-breaks → reflection`

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-easy.md` | 5 panels: Summary (Three-Scale Anatomy block with safety first), Better Explanation (Safety Before Content + Observable Before Theory arc), Examples (comparison strip — substance boundary cases), Origin (Islamic heritage — Jabir ibn Hayyan, Al-Razi + European), Industry Application |
| 2 | `flashcards.md` | 6–10 cards: substance names with observable properties + formulas, safety hazard symbols, classification terms (kislota, asos, oksid, tuz) |
| 3 | `memory-sprint.md` | 10–15 items: substance classification from observable description, formula recognition, safety rule recall |
| 4 | `game-breaks.md` | 2 games: Equation Balance Puzzle Lock (Interactive Catalog) + one of Three-Scale Tile Match / Sentence Fill / Adaptive Quiz / Reaction Chain (Default Pool) |
| 5 | `reflection.md` | Summary + question + spaced rep + closing |

**Skipped:** Observable→Formula Translation, Industry Application panel 6, Why This Matters, Real-Life, Consolidation, Final Challenge.

---

## Hard (8 phases)

`classify → preview-hard → flashcards → memory-sprint → game-breaks → real-life → consolidation? → final-challenge → reflection`

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-hard.md` | 7 panels: Summary (Three-Scale Anatomy block — safety first + three-scale arc map), Better Explanation (Safety Before Content + Observable→Micro→Symbolic arc + Three-Scale Legend), Examples (progressive scale states — safety first), Origin (genetic method — Islamic heritage + European), Observable→Formula Translation, Industry Application, Why This Matters |
| 2 | `flashcards.md` | 8–12 cards: substance formulas with all three scales, safety hazard classes, reaction types, Periodic Table position references |
| 3 | `memory-sprint.md` | 15–20 items: three-scale matching, equation balancing verification, safety rule ordering, classification from observable properties |
| 4 | `game-breaks.md` | 3 games: Equation Balance Puzzle Lock (Interactive Catalog) + 2 from Default Pool (Three-Scale Tile Match / Sentence Fill / Lab Report Capture / Reaction Chain / Adaptive Quiz) |
| 5 | `real-life.md` | Lab observation scenario requiring three-scale reasoning, formula writing from observable properties, and equation balancing with safety note |
| 6 | `consolidation.md` | Mnemonic for reaction type sequence or three-scale arc (SKIP if chapter covers single substance classification only) |
| 7 | `final-challenge.md` | Boss fight, 5–8 questions, no MC for G7+, HP: G7–9=100, G10–11=150 |
| 8 | `reflection.md` | Summary + BOST goal recall + spaced rep + closing |

---

## Assembly

All phase outputs assembled into a single `.md` file — that is the final homework. Each phase becomes a section in order.

---

## Notes

- **Covers:** Kimyo G7–11
- **Games:** Equation Balance Puzzle Lock, Three-Scale Tile Match, Sentence Fill, Lab Report Capture, Reaction Chain, Adaptive Quiz
- **Teaching:** Safety Before Content — safety note mandatory before any chemistry content in every panel involving a substance or reaction.
- **Teaching:** Observable Before Theory — macroscopic properties described before microscopic structure, before symbolic formula. Arc: Macro → Micro → Symbolic.
- **Teaching:** Every substance described at all three scales (macroscopic, microscopic, symbolic) — never in text alone.
- **Teaching:** Lab Report Capture mandatory in Hard mode lab chapters (at minimum every 2 sessions) — student draws three-scale diagram, writes balanced equation, states safety rule.
- **Teaching:** All balanced equations verified with atom count check before output.
- **Teaching:** Islamic scientific heritage credited in Panel 4 (Jabir ibn Hayyan, Al-Razi, Ibn Sina alongside Lavoisier, Boyle).
- **Visual layer:** Three-Scale Anatomy Notation — macro (observable), micro (particle), symbolic (formula/equation). Color: blue=given/observable, orange=unknown/to find, green=microscopic mechanism, red=safety hazard, grey=background.
- **Language:** Uzbek (or Russian if textbook is Russian). Formal "Siz" throughout — never "sen."
- **HP:** G7–9 = 100 HP, G10–11 = 150 HP
