# Kimyo — Homework Builder Instruction

You are building a homework session for Kimyo (G7-11). Follow these steps in order.

## Step 1: Identify the lesson

You receive a chapter-section reference (e.g., "Grade 8 Kimyo, §7 Suvning xossalari" or "Grade 9 Kimyo, §3 Kislota-asos reaksiyalari").

Find and read the corresponding textbook pages. Extract:
- Topic name and the substance, reaction, or concept covered
- All observable properties described (color, state, smell, solubility, reactivity)
- All chemical formulas and equations on the page
- All safety rules and hazard warnings
- All lab procedures described (materials, steps, observations, conclusions)
- All Periodic Table references (group, period, valence, electronegativity)
- All three-scale descriptions: macroscopic → microscopic → symbolic
- All worked examples and calculations (molar mass, stoichiometry)
- All exercises and problems listed

## Step 2: Classify difficulty

Read `06-prompts/kimyo-g7-11/classify.md` and apply it to the extracted content.

Two checks:
1. Is the topic inherently complex? (requires three-scale reasoning, equation balancing, stoichiometry, Periodic Table prediction) → **HARD**
2. Does the page teach a chemical equation, lab procedure, or property prediction? (boxed equation, "masala" section, safety + procedure protocol) → **HARD**
3. Only observable properties, classification, element naming, safety rule recall → **EASY**

Output: EASY or HARD + one sentence why.

## Step 3: Load the right prompt

- If EASY → read `06-prompts/kimyo-g7-11/preview-easy.md`
- If HARD → read `06-prompts/kimyo-g7-11/preview-hard.md`

## Step 4: Build

Follow the loaded prompt exactly. Use the extracted textbook content as your source material. Every panel must reference actual content from the textbook page — do not invent reactions, properties, or safety rules not present in the source.

**Safety First rule — mandatory for all phases:** Every panel that introduces a substance or reaction MUST state the relevant safety rule before presenting any chemistry content. Safety precaution comes before formula, observation, or explanation — no exceptions.

**Observable Before Theory rule:** Every substance or reaction must be presented with its macroscopic observable properties FIRST (what you can see, smell, feel, observe in the lab), THEN the microscopic explanation (atomic/molecular structure), THEN the symbolic representation (formula with valence). Never introduce a formula before its observable phenomenon.

**Three-Scale rule:** Every substance or reaction must be described at all three scales:
1. Macroscopic: visible sample — color, state, smell, texture, reactivity
2. Microscopic: atom/molecule structure — what the particles look like, how they bond
3. Symbolic: chemical formula with valence notation, balanced equation

---

## Visual Layer — Substance and Apparatus Diagram Notation Standard (mandatory for all phases)

All diagram descriptions in brackets must follow this notation.

### Diagram element types

| Element | Notation in brackets |
|---------|---------------------|
| Macroscopic sample | `solid NaCl crystals — white, cubic, no smell` |
| Microscopic structure | `Na⁺ and Cl⁻ ions alternating in cubic lattice` |
| Symbolic formula | `NaCl (Na: valence +1, Cl: valence -1)` |
| Balanced equation | `2Na + Cl₂ → 2NaCl (balanced: Na×2 both sides, Cl×2 both sides)` |
| Lab apparatus | `evaporating dish, burner, safety goggles, tongs — all labeled` |
| Safety equipment | `goggles (orange = required), gloves (orange = required), fume hood (orange = required)` |
| Periodic Table position | `Period 3, Group 1 — Na highlighted (orange)` |
| Observable reaction | `gas bubbles forming, color change from clear to blue, precipitate settling` |
| Unknown/to find | `question mark on missing product or missing coefficient` |

### Color coding (use in all phase descriptions)

| Color | Meaning |
|-------|---------|
| **Blue** | Given information — observable properties, given formulas, stated quantities |
| **Orange** | What must be found, predicted, or written — unknown product, missing coefficient |
| **Green** | Mechanism — the microscopic reason for the macroscopic observation |
| **Red** | Safety hazard — shown and labeled with the safety precaution |
| **Grey** | Background lab context / non-essential apparatus |

### Three-Scale Anatomy block (mandatory in Panel 1 of every Preview)

Every session opens with a three-scale reference description — the "map" the student returns to throughout the session. Format:

```
[Three-Scale Anatomy:
Macroscopic: [visible appearance of the substance or reaction — color, state, texture, observable change]
Microscopic: [atom/molecule structure description — particle type, arrangement, bonding]
Symbolic: [chemical formula with valence notation / balanced equation with coefficients]
Safety: [relevant hazard label and required protection equipment — shown in orange/red]]
```

This block is described once in Panel 1 and referenced in all later panels.

### Safety Protocol block (mandatory when lesson includes a lab)

When the chapter involves lab work, include a structured safety + protocol block before any chemistry content:

```
[Safety Protocol:
Hazard: [substance hazard type — corrosive, flammable, toxic, irritant]
Required protection: [goggles / gloves / fume hood / fire extinguisher — labeled orange]
Procedure: Step 1 → Step 2 → Step 3 → Step 4
Observation: [what to record at each step]
Conclusion: [which substance or reaction the observations confirm]]
```

---

---

## Language Rule — mandatory

Generate all student-facing content **exclusively in the textbook's language**.

- If the textbook is in **Uzbek** → the entire session (all panels, questions, answers, hints, feedback) is in Uzbek.
- If the textbook is in **Russian** → the entire session is in Russian.
- **Never mix languages** within a single session. Do not add translations, parenthetical glosses, or notes in the other language unless the subject itself requires it (e.g., Ingliz tili, Rus tili, Ona tili).
- The textbook's language is determined from the source material provided. When in doubt, use the language of the chapter heading.

## Step 5: Verify

Before outputting, check:
- [ ] Every panel present in the right order
- [ ] Language is Uzbek, formal "Siz" throughout — never "sen"
- [ ] Two-layer explanation in each panel (formal + "Sodda so'zlar bilan:")
- [ ] Safety rule stated BEFORE any chemistry content in every panel introducing a substance or reaction
- [ ] Observable properties described BEFORE microscopic explanation or formula
- [ ] Three-scale descriptions present: macroscopic → microscopic → symbolic
- [ ] Panel 1 opens with a Three-Scale Anatomy block (with safety note)
- [ ] Lab lessons include a Safety Protocol block before any procedure content
- [ ] Islamic scientific heritage credited in Panel 4 (Jabir ibn Hayyan, Al-Razi, Ibn Sina alongside Lavoisier, Boyle)
- [ ] HARD mode: Panel 5 (Observable→Formula Translation) teaches HOW to move from macroscopic observation to symbolic formula — including boundary cases
- [ ] All balanced equations have equal atom counts on both sides — verify before outputting
- [ ] Periodic Table reasoning is directional: "Because [group/period position], we predict [property]"
- [ ] No bazaar/village clichés — modern professional contexts: kimyogar, farmatsevt, ekolog, oziq-ovqat texnologi
- [ ] HP: G7-9 = 100, G10-11 = 150
