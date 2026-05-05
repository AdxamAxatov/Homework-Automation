# Prompt: Game Breaks — History (O'zbekiston Tarixi + Jahon Tarixi)

You are building the Game Breaks (Phase 3) for a History homework session. This is where real practice happens. The student has just warmed up with Memory Sprint; now they apply what was learned in Preview through 3 sequenced games.

Phase 3 is the **heaviest graded component** — **50%** of the History Hard session score.

## Input

- Textbook lesson content (extracted in orchestrator Step 1)
- Preview output + Flash Cards output + Sprint output
- Grade: G5–G11
- Subject: `O'zbekiston Tarixi` or `Jahon Tarixi`

## Output

**3 games in sequence:** Game 1 → Game 2 (Von Restorff Anchor) → Game 3.

**~20 items total** across the 3 games (5–8 items per game).

**Difficulty distribution across all items:** ~40% Easy / ~40% Medium / ~20% Hard (tolerance ±5%).

Every item carries an inline tag: `[Bloom: LX | PISA: Reading/Creative Thinking LX | Skill: ... | Standard: UZ-TARIX-G-TOPIC-G##-##]`.

---

## Available Games — History v1 pool

Only 3 games are available for History v1. All from Default Pool.

| Game | Mechanic | Good for |
|---|---|---|
| **Tile Match** (mandatory Slot 1) | Drag pairs to match | cause↔effect, date↔event, figure↔achievement |
| **Memory Match** | 4×4 flip grid, find matching pairs | figure↔role, event↔date, place↔event |
| **Sentence Fill** | Cloze completion (select or drag missing piece) | historical term gaps, source-quote fills |

- **NO Adaptive Quiz** — History is non-calc family.
- **NO Notebook Capture** — non-calc.
- **Frozen / do NOT use:** Why Chain, Territory Conquest, Reaction Chain, Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Codebreaker.

## Dual-catalog rule

Framework spec requires `≥1 Interactive + ≥2 Default Pool` per Phase 3. For History v1, the dual-catalog rule is **WAIVED** because all Interactive games historically assigned to History (Why Chain, Territory Conquest, Reaction Chain) are frozen to v2+. History v1 uses **3 Default Pool games only**. Document the waiver inline in your output.

## Game sequence

- **Slot 1:** Tile Match — mandatory primary. Cause↔effect or figure↔achievement pairings that span the lesson's full arc.
- **Slot 2 (⭐ Von Restorff Anchor):** Memory Match — middle game. Include at least **one outstanding pair** (surprising fact, unexpected scale, striking juxtaposition). Tag it `⭐ Von Restorff`. This pair is the cognitive anchor students remember most.
- **Slot 3:** Sentence Fill — contextual retrieval of lesson terms or source quotes.

Modalities across the 3 games: Verbal/Logical (Tile) → Visual/Spatial (Memory) → Verbal/Logical (Sentence). ≥2 distinct modalities (soft rule).

---

## Construction per game

### Game 1 — Tile Match

- **6–8 pairs** (7 is a clean default).
- Left column: causes / dates / figures.
- Right column: effects / events / achievements.
- Preferred pair type for History: **cause↔effect** — matches the family goal of causal reasoning over date memorization.
- Pairs should **trace the lesson's full causal arc** from opening event to closing consequence.
- Difficulty mix within this game: ~3 Easy + ~3 Medium + 1 Hard.

### Game 2 — Memory Match (Von Restorff Anchor)

- **4×4 grid = 8 pairs.** Student flips two cards at a time to find matches.
- Pair pattern for History: **figure↔achievement**, **figure↔role**, or **event↔date**.
- **Von Restorff requirement:** exactly one pair carries an **outstanding fact** — unexpected scale, surprising consequence, vivid detail. Tag it `⭐ Von Restorff` in your output. This pair typically is the Hard-difficulty item in the game.
- Difficulty mix: ~4 Easy + ~3 Medium + 1 Hard.

### Game 3 — Sentence Fill

- **5–7 items** (6 is a clean default).
- Show a sentence from the lesson (or paraphrased) with ONE word or short phrase missing.
- Gap must test **historical understanding** — not random word removal.
- Two sub-types:
  - **Concept/term fill** — e.g., *"Bu maʼmuriy birliklar ___ deb nomlandi."* (answer: `tuman`)
  - **Source-quote fill** — pulled from a primary source the lesson cites. E.g., *"Namoz ___ uchunmi yoki Tarmashirin uchunmi?"* (answer: `Xudo`)
- **Include ≥1 source-quote fill** if the lesson contains a primary source (Panel 3 content).
- Difficulty mix: ~2 Easy + ~3 Medium + ~1 Hard.

---

## Rules

- **Exactly 3 games** in the order Tile Match → Memory Match → Sentence Fill.
- **Every item tagged** with Bloom / PISA / Skill / Standard. Game-level defaults are acceptable; per-item overrides when difficulty differs.
- **Von Restorff anchor on Slot 2** — always. Tag the outstanding pair explicitly.
- **Textbook fidelity** — every pair, every sentence-fill, every term from the source lesson.
- **Current chapter only** — no cross-chapter content.
- **No calculation / no Notebook Capture** — non-calc family.
- **No frozen games** — never reference Why Chain, Territory Conquest, Reaction Chain, or any removed mechanic.
- **Difficulty target:** 40/40/20 across all items in the 3 games (tolerance ±5%). Within any single game, do NOT load more than ~20% Hard items.
- **Von Restorff anchor item in Game 2** is typically the **Hard-difficulty** pair in that game — it's the outstanding fact, the cognitive peak. Do not tag it as Medium or Easy.
- **PISA tag MUST include L level.** Write `Reading L1`, `Reading L2`, `Creative Thinking L2`, etc. Never just `Reading` alone.
- **Language:** Uzbek, `Siz` when addressing student. Never `sen`.
- **Dual-catalog waiver** — document inline that History v1 uses 3 Default Pool games because Interactive games are frozen.
- **Weight:** Phase 3 = 50% of session score (heaviest graded component).


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
