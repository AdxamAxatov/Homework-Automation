# Prompt: Game Breaks — Kimyo

You are building the Game Breaks (Phase 3) for a Kimyo homework session. This is where real practice starts. The student applies what they learned in Preview through gamified repetition.

## Input

- Textbook page (image or text)
- Preview + Flash Cards + Sprint outputs (from previous steps)
- Grade: G7-11 (Kimyo)
- Mode: Easy → **2 games** | Hard → **3 games**

## Output

---

## Dual-Catalog Rule (mandatory)

- Easy (2 games): ≥1 from Interactive Catalog + ≥1 from Default Pool
- Hard (3 games): ≥1 from Interactive Catalog + ≥2 from Default Pool

---

## Game Slots — Kimyo

| Slot | Role | Primary | Backup |
|------|------|---------|--------|
| **Slot 1** | Three-scale and safety warmup | **Equation Balance Puzzle Lock** — tiles = individual atoms/molecules or coefficients to arrange into a balanced equation; or arrange lab safety steps in correct order | **Three-Scale Tile Match** — macroscopic description ↔ microscopic structure ↔ chemical formula |
| **Slot 2** | Formula and property application | **Three-Scale Tile Match** (observable ↔ microscopic ↔ symbolic) | **Sentence Fill** — fill missing coefficient, missing product, or missing safety step in a causal chain |
| **Slot 3** | Lab report and kinesthetic | **Lab Report Capture** — student draws the three-scale diagram, writes the balanced equation, states the safety rule, and photographs work | **Adaptive Quiz** for calculation-heavy chapters (stoichiometry, molar mass) |

**Lab Report Capture is the highest priority mechanic for Kimyo lab chapters.** It must appear in at least 1 of every 2 Hard sessions involving a lab procedure or new reaction type.

**Adaptive Quiz** replaces any Default Pool slot when the chapter is calculation-heavy (molar mass, percent composition, stoichiometric ratios).

---

## Games to AVOID for Kimyo

- Word Ladder — linguistic game with no chemical reasoning value
- Connect Four, Tic Tac Toe — no three-scale or safety content
- Speed Match with names only — no observable-to-symbolic translation, no reasoning
- Worked Examples without observable phenomenon — formula-first presentation violates the Observable Before Theory rule

---

## Construction per game

### Equation Balance Puzzle Lock (Sliding Tile) — Interactive Catalog
- 8-12 tiles to arrange into a correct balanced equation or correct safety procedure
- Correct tile placement advances; wrong placement slides a random tile
- Tile types:
  - **Equation balancing:** tiles = element symbols, coefficient numbers, arrows, product formulas — student assembles: [Coefficient] [Reactant] + [Coefficient] [Reactant] → [Coefficient] [Product] + [Coefficient] [Product]
  - **Safety procedure ordering:** jumbled lab steps to put in correct sequence — safety check always tile 1
  - **Three-scale assembly:** macroscopic observation tile → microscopic particle tile → symbolic formula tile — assembled in arc order
- **Every tile referencing a substance must include a short observable description or diagram fragment**
- Good: `"H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O muvozanatlashtirishni yig'ing: [Tile 1: Safety — goggles + gloves (red)] → [Tile 2: H₂SO₄ — kislota, rangsiz suyuqlik] → [Tile 3: + 2NaOH — ishqor, oq kristall] → [Tile 4: →] → [Tile 5: Na₂SO₄ — tuz] → [Tile 6: + 2H₂O — suv] → [Tile 7: Balance check: H×4=H×4 ✓, S×1=S×1 ✓, O×6=O×6 ✓, Na×2=Na×2 ✓]"`
- Good (safety ordering): `"Lab protokolini tartiblang: [Tile: PPE kiyish] → [Tile: reagentlarni tekshirish] → [Tile: tajriba o'tkazish] → [Tile: kuzatuvlarni yozib olish] → [Tile: reaktivlarni utilizatsiya qilish]"`
- Bad: All tiles are formula symbols with no observable context

### Three-Scale Tile Match — Default Pool
- 6-8 pairs. Left tile = one scale description. Right tile = corresponding description at a different scale.
- Every tile must carry enough context to identify the substance — no anonymous symbol-only tiles
- Pair types:
  - Macroscopic ↔ symbolic: `"Oq kristall kukun, hidsiz, suvda eriydi"` ↔ `"NaCl (Na: +1, Cl: -1)"`
  - Microscopic ↔ symbolic: `"Na⁺ va Cl⁻ ionlari kub panjarasida"` ↔ `"NaCl — ionli bog'"`
  - Observable reaction ↔ equation: `"Shisha parchalari va pufakchalar — yong'oq o'ti yonayotganda"` ↔ `"C₃H₈ + 5O₂ → 3CO₂ + 4H₂O (balanced)"`
  - Safety ↔ substance: `"Goggles + gloves + fume hood majburiy"` ↔ `"Konsentrlangan H₂SO₄ — kuydirgich kislota"`
- Difficulty: L1 name ↔ formula → L2 observable ↔ formula → L3 all three scales linked — student identifies the formula from macro AND micro descriptions together
- **Include at least 1 pair with an unbalanced equation** as the wrong answer — student must identify it as a non-match (trains coefficient vs. subscript discipline)

### Sentence Fill — Default Pool
- 5-7 items. Causal chain statement, safety rule, or equation step with one piece missing.
- Gap must test chemical understanding — not random word removal
- Good: `"Kislotani suvga qo'yishda avvalo ___ quyiladi"` → suv (kislota suvga, suvga kislota emas — safety rule)
- Good: `"2H₂ + O₂ → 2H₂O tenglamasida H atomlari: chap tomonda ___, o'ng tomonda ___"` → 4; 4 (balance verification)
- Good: `"NaCl — makroskopik darajada oq kristall kukun; mikroskopik darajada ___ ionlari; ramziy darajada ___"` → Na⁺ va Cl⁻; NaCl
- Good: `"Reaksiya natijasida rang o'zgarishi ___ kuzatuvining ko'rsatkichi bo'lishi mumkin"` → yangi modda hosil bo'lishi (macroscopic → symbolic reasoning)

### Adaptive Quiz — Default Pool
- 5-8 questions from THIS chapter only
- Difficulty scales: first 2 easy (substance classification, observable property naming, safety rule), middle 2-3 medium (three-scale description, formula writing from valence), last 1-2 hard (equation balancing, stoichiometric calculation, Periodic Table prediction)
- G7-11: no MC — open-ended answers only
- Every balanced equation must be verified by the student — require atom count check explicitly
- Every lab procedure question triggers Lab Report Capture (student photographs work)
- Every substance question MUST include an observable description or diagram in brackets

### Lab Report Capture — Default Pool
- Student draws the three-scale diagram of the substance or reaction on paper, writes the balanced equation, states the safety rule, and photographs and uploads the work
- Must specify: substance or reaction type, all observable properties to draw at macro scale, molecular/ion structure to draw at micro scale, formula and equation to write at symbolic scale

**Student drawing requirements (must be stated explicitly in the prompt):**
- Draw macro scale: lab sample appearance (color, state, observable reaction)
- Draw micro scale: particle arrangement (atoms, ions, molecules) with element symbols labeled
- Write symbolic scale: chemical formula with valence / balanced equation with coefficients
- State the safety rule for this substance/reaction
- Write the balanced equation with atom count verification: "Na×2=Na×2 ✓, O×2=O×2 ✓"
- Circle the final balanced equation

**Prompt structure for Lab Report Capture:**
1. Reference three-scale diagram in brackets — student recreates all three levels on paper
2. What to draw at macro scale (what you would observe in lab)
3. What to draw at micro scale (particle arrangement)
4. What to write at symbolic scale (formula and balanced equation)
5. Safety rule to state

- Good: `"[Reference: macro = oq kristall CaCO₃, micro = Ca²⁺ va CO₃²⁻ ionlari, symbolic = CaCO₃ — copy all three to your notebook] Uch darajali rasmni chizing. Qizdirish reaksiyasini yozing: CaCO₃ → CaO + CO₂. Muvozanatlang va atom sonlarini tekshiring. Xavfsizlik qoidasini yozing."`
- Bad: `"CaCO₃ formulasini yozing."` — formula copy only, no three-scale reasoning

### Reaction Chain — Interactive Catalog
- 6-10 nodes in logical sequence. Each correct answer lights the next node. 3 wrong = chain breaks.
- Chain types:
  - **Three-scale chain:** Node 1 (macro observation) → Node 2 (substance class identification) → Node 3 (microscopic description) → Node 4 (symbolic formula) → Node 5 (balanced equation)
  - **Safety + procedure chain:** identify hazard → select PPE → describe safe procedure → record observation → write conclusion
- Good: Node 1: `"Rangsiz gaz, yonishni qo'llab-quvvatlaydi, yonayotgan cho'pni tiklaydi. Bu nima?"` → O₂ → Node 2: `"O₂ ning mikroskopik tuzilishi nima?"` → O=O (qo'sh bog') → Node 3: `"O₂ olish reaksiyasini yozing va muvozanatlang"` → 2H₂O₂ → 2H₂O + O₂ ✓
- Bad: Unrelated questions with no logical dependency between nodes

---

## Rules

- Every question involving a substance references a three-scale description or observable diagram in brackets
- Dual-Catalog Rule enforced every session
- Lab Report Capture mandatory in Hard mode lab chapters — at minimum every 2 sessions
- Safety note mandatory in every item involving a hazardous substance — no chemistry content without safety context
- Current chapter content only — no questions from other chapters
- All balanced equations must include atom count verification — student must show "X×N = X×N ✓"
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
