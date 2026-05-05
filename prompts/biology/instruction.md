# Biology — Homework Builder Instruction

You are building a homework session for Biology (Biologiya, G5-11). Follow these steps in order.

## Step 1: Identify the lesson

You receive a chapter-section reference (e.g., "Grade 7 Biologiya, §12 Fotosintez").

Find and read the corresponding textbook pages. Extract:
- Topic name
- All biological terms and definitions on the page
- All named processes, stages, or mechanisms described
- All organisms, organs, or structures named with their functions
- All experiments, observations, or procedures listed
- Any diagrams, cycles, classification trees, or visual elements
- Any comparison tables (e.g., plant cell vs. animal cell)

## Step 2: Classify difficulty

Read `06-prompts/biology/classify.md` and apply it to the extracted content.

Two checks:
1. Is the topic inherently complex? (cell division, genetics, photosynthesis/respiration, nervous system, evolution, ecological cycles) → **HARD**
2. Does the page teach a process, mechanism, or experiment? (sequential steps, cycles, cause-effect chains, lab procedure) → **HARD**
3. Only naming, taxonomy, morphological description, historical introduction → **EASY**

Output: EASY or HARD + one sentence why.

## Step 3: Load the right prompt

- If EASY → read `06-prompts/biology/preview-easy.md`
- If HARD → read `06-prompts/biology/preview-hard.md`

## Step 4: Build

Follow the loaded prompt exactly. Use the extracted textbook content as your source material. Every panel must reference actual organisms, processes, or structures from the textbook page — do not invent biological facts, mechanisms, or classifications that aren't in the source.

**Teaching sequence — always observation-first:**
1. What do you SEE? (observable structure, organism, phenomenon)
2. What does it DO? (function, behavior, role)
3. HOW does it work? (mechanism, process, steps)
4. WHAT does it mean scientifically? (terminology, classification, formal definition)

Never lead with scientific terminology — always anchor it to what is observable first.

**SVG is critical for Biology.** Biological concepts are spatial and visual. Every panel that describes a structure, process, or cycle must include an SVG or a clearly specified visual. SVG priority:

```
SVG > Mermaid > ASCII
```

SVG use cases:
- Cell diagrams (organelles labeled, membrane layers, nucleus)
- Organism structures (leaf cross-section, flower anatomy, bone joints)
- Biological process/cycle diagrams (photosynthesis flow, mitosis stages, water cycle)
- Food chains and food webs (arrows showing energy flow)
- Classification trees (kingdom → phylum → class hierarchy)
- Organ system maps (digestive tract path, circulatory loop, nervous system branches)
- Comparison diagrams (plant cell vs. animal cell side-by-side)

SVG size constraints:
- Preview panels: max **300×200 px**
- Game panels (Tile Match, Memory Match): max **200×150 px**
- Use `viewBox` attribute so SVGs scale responsively

## Step 5: Verify

Before outputting, check:
- [ ] Every panel present in the right order
- [ ] Language is Uzbek, formal "Siz" throughout — never "sen"
- [ ] Two-layer explanation in each panel (formal biological term + "Sodda so'zlar bilan")
- [ ] Observation-first sequence respected (SEE → DO → HOW → WHAT)
- [ ] SVG or visual description present for every structural/process panel
- [ ] No Notebook Capture — Biology is exempt from calculation capture (TF-1)
- [ ] No invented biology — every fact traces to the textbook page
- [ ] No bazaar/village/shopkeeper clichés — modern professional context only (lab, agritech, medical, environmental science)
- [ ] v1 games only: Adaptive Quiz, Tile Match, Memory Match, Sentence Fill
- [ ] Adaptive Quiz: no capture blocks in Biology
- [ ] HARD mode: Real-Life uses narrative-process format (photosynthesis pattern) — flowing story first, then 2-3 questions from it
- [ ] HARD mode: Consolidation fires only when ≥2 distinct interlocking concepts are taught; skip for single-concept lessons
- [ ] Boss HP correct: G5-8 = 100 HP, G9-11 = 150 HP
- [ ] No MC in Final Boss for G6+ (G5 allows up to 30% MC)
- [ ] Every question carries inline tags: `[Bloom: LX | PISA: LX]`
- [ ] Boss questions also carry `[Damage: -XX HP]`
