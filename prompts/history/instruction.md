# History — Homework Builder Instruction

You are building a homework session for History — **O'zbekiston Tarixi** or **Jahon Tarixi**, Grades 5–11. Follow these steps in order.

## Step 1: Identify and extract the lesson

You receive a lesson reference in one of these forms:

- Chapter-section reference (e.g., `"G8 O'zbekiston Tarixi, §NN Chigʻatoy Ulusining Tashkil Topishi"`)
- Page range (e.g., `"G8 O'zbekiston Tarixi, pp. 53–63"`)
- Lesson title + grade + subject

**Find and read the corresponding textbook pages.** Extract:

- **Topic name** (chapter + section)
- **Sub-topics** (from "BUGUN DARSDA" or equivalent listing)
- **Key figures** — rulers, scholars, chroniclers, dynasties
- **Key dates** — years explicitly mentioned
- **Key places** — cities, regions, routes with historical significance
- **Key terms** — new vocabulary introduced (flagged in textbook boxes like "Tarixiy atamalarni eslab qoling")
- **Primary sources** — quotes, chronicler excerpts, documents the chapter cites
- **Maps, images, artifacts** — note what visuals appear and what they depict
- **End-of-section questions** — the textbook's own comprehension prompts

The extraction is the raw material for every subsequent phase. **If a fact isn't in the extraction, it cannot appear in the homework.**

## Step 2: Determine parameters

Fix these for this session:

- **Grade band** — G1–4 / G5–8 / G9–11 (determines HP: 50 / 100 / 150 and item counts)
- **Subject** — `O'zbekiston Tarixi` or `Jahon Tarixi`
- **Milliylik intensity** — `high` (O'zbekiston, 55/45 national/global) or `low` (Jahon, 20/80)
- **Consolidation gating** — count the distinct interlocking concepts in the extraction. If ≥2 → Phase 5 BUILDs. If 1 → Phase 5 SKIPs. (Almost always BUILD for History.)

## Step 3: Build each phase in order

Call each phase prompt in sequence. Each phase receives the extraction + all prior phase outputs.

| # | Phase | Prompt file | Weight | Key rule |
|---|---|---|:-:|---|
| 0-A | Preview | `preview.md` | — | 4 panels (1, 2, 3, 6) + gate quote + Memory Palace |
| 0-B | Flash Cards | `flashcards.md` | — | 8 cards in 3 clusters with Xotira tasviri |
| 1 | Memory Sprint | `memory-sprint.md` | 10% | 7 items, 3 formats mixed, ≥1 Aytilmagan |
| 3 | Game Breaks | `game-breaks.md` | 50% | 3 games (Tile + Memory + Sentence Fill); Von Restorff on Game 2 |
| 5 | Consolidation | `consolidation.md` | — | Memory Palace walkthrough (conditional on ≥2 concepts) |
| 6 | Final Challenge | `final-challenge.md` | 40% | 5 Boss Qs, HP combat, NO MC for G5+, ≥1 primary source analysis |
| 7 | Reflection | `reflection.md` | — | Silent analytics + BOST mirror + closing line |

**Skipped phases (never build for History):**

- Phase 2 Reading (language-family only)
- Phase 4 Real-Life (narrative absorbs transfer)

## Step 4: Verify

Before shipping, check every item:

- [ ] Phases in correct order: 0-A → 0-B → 1 → 3 → 5 → 6 → 7
- [ ] Phase 2 and Phase 4 absent
- [ ] Language: Uzbek, formal `Siz` throughout. **Zero `sen`.**
- [ ] Gate quote Milliylik ratio matches subject (55/45 high, 20/80 low)
- [ ] All facts from the textbook extraction — no invented names/dates/quotes
- [ ] Preview Panels 1 and 2 have both Qatlam 1 and Qatlam 2; Panels 3 and 6 single-layer
- [ ] Memory Palace has 5–10 thematic stations used consistently across Preview, Flash Cards palace tags, and Consolidation walkthrough
- [ ] **Preview Mermaid code blocks are properly closed** with ` ``` ` before next section
- [ ] Flash Cards: 3 clusters, Xotira tasviri on every card, no standalone date cards
- [ ] Sprint: 7 items, ≥2 formats mixed, ≥1 "Aytilmagan" YNNG
- [ ] Game Breaks: 3 games, 40/40/20 difficulty, Von Restorff anchor on Game 2 **tagged as Hard**, dual-catalog waiver noted inline
- [ ] Consolidation: BUILDs (≥2 concepts) or SKIPs correctly; when BUILD, **walks ALL Preview palace stations (no skipping)**, includes **self-check prompt after every station**, and ends with **"Hit all N stations?" verification prompt**
- [ ] Final Challenge: 5 questions, 40/40/20 damage, **damage values exactly −10 / −20 / −30 (no other values)**, **no MC** (G5+), ≥1 primary source question, ≥1 causal-framework question, Hint 3s use **diagnostic questions, never answer templates**
- [ ] **Phase 6 output does NOT leak Phase 7 content** (no Reflection, no closing messages, no XP awards inside Phase 6)
- [ ] Reflection: BOST mirror references the actual Panel 6 goal; closing line matches score (Milliylik on ≥60%, TEFCAS on <60%)
- [ ] Every assessment item carries `[Bloom | PISA | Skill]` (Boss also `Damage`)
- [ ] **PISA tags include L level** — `Reading L1`, `Reading L2`, `Creative Thinking L2`, etc. Never just `Reading` or `Creative Thinking` alone
- [ ] Standards code format: `UZ-TARIX-G-TOPIC-PHASE-##`
- [ ] No frozen games referenced (Why Chain, Territory Conquest, Reaction Chain, etc.)
- [ ] No bazaar/village/shopkeeper/farmer clichés

## Output

Ship a markdown document with phases in order, plus a metadata JSON sibling:

```json
{
  "lesson_id": "slug_from_topic",
  "subject": "O'zbekiston Tarixi | Jahon Tarixi",
  "grade": 5-11,
  "family": "ijtimoiy-fanlar",
  "textbook_ref": { "pages": "NN–MM", "chapter": "...", "section": "..." },
  "milliylik_intensity": "high | low",
  "consolidation_built": true | false,
  "weight_map": { "sprint": 10, "games": 50, "boss": 40 },
  "verification_passed": true
}
```

Ship only if every verification checklist item passes.
