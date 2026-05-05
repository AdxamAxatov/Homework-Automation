# Math + Algebra — Homework Builder Instruction

You are building a homework session for Math (G5-6) or Algebra (G7-9). Follow these steps in order.

## Step 1: Identify the lesson

You receive a chapter-section reference (e.g., "Grade 8 Algebra, §22 Kvadrat Tenglama" or "Grade 5 Matematika, §12 Kasrlar").

Find and read the corresponding textbook pages. Extract:
- Topic name
- All definitions, formulas, rules on the page
- All worked examples
- All exercises/problems listed
- Any diagrams, tables, or visual elements

## Step 2: Classify difficulty

Read `06-prompts/math-algebra/classify.md` and apply it to the extracted content.

Two checks:
1. Is the topic inherently complex? (requires chaining prior concepts, abstract, multi-step by nature) → **HARD**
2. Does the page teach a procedure? (boxed formula, worked example, step-by-step method, "masalalar" section) → **HARD**
3. Only definitions, taxonomy, notation intro, no procedure → **EASY**

Output: EASY or HARD + one sentence why.

## Step 3: Load the right prompt

- If EASY → read `06-prompts/math-algebra/preview-easy.md`
- If HARD → read `06-prompts/math-algebra/preview-hard.md`

## Step 4: Build

Follow the loaded prompt exactly. Use the extracted textbook content as your source material. Every panel must reference actual content from the textbook page — do not invent formulas, examples, or definitions that aren't in the source.

## Step 5: Verify

Before outputting, check:
- [ ] Every panel present in the right order
- [ ] Language is Uzbek, formal "Siz" throughout
- [ ] Two-layer explanation in each panel (formal + "Sodda so'zlar bilan")
- [ ] All examples have units
- [ ] No magic moves — every step explained
- [ ] Origin credits the actual inventor
- [ ] No bazaar/village/shopkeeper cliches
- [ ] Visuals described in brackets where needed
- [ ] HARD mode: Panel 5 (Word→Formula) teaches extraction, not just shows examples
