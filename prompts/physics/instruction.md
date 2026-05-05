# Physics — Homework Builder Instruction

You are building a homework session for Physics (Fizika, G7-11). Follow these steps in order.

## Step 1: Identify the lesson

You receive a chapter-section reference (e.g., "Grade 7 Fizika, §15 Nyuton qonunlari").

Find and read the corresponding textbook pages. Extract:
- Topic name
- All definitions, laws, formulas on the page
- All worked examples and experiments
- All exercises/problems listed
- Any diagrams, graphs, or visual elements

## Step 2: Classify difficulty

Read `06-prompts/physics/classify.md` and apply it to the extracted content.

Two checks:
1. Is the topic inherently complex? (requires chaining prior formulas, abstract, multi-step) → **HARD**
2. Does the page teach a formula or procedure? (boxed law, worked example, lab procedure) → **HARD**
3. Only definitions, taxonomy, qualitative description → **EASY**

Output: EASY or HARD + one sentence why.

## Step 3: Load the right prompt

- If EASY → read `06-prompts/physics/preview-easy.md`
- If HARD → read `06-prompts/physics/preview-hard.md`

## Step 4: Build

Follow the loaded prompt exactly. Use the extracted textbook content as your source material. Every panel must reference actual content from the textbook page — do not invent laws, formulas, or experiments that aren't in the source.

## Step 5: Verify

Before outputting, check:
- [ ] Every panel present in the right order
- [ ] Language is Uzbek, formal "Siz" throughout
- [ ] Two-layer explanation in each panel (formal + "Sodda so'zlar bilan")
- [ ] All examples have units
- [ ] No magic moves — every derivation step explained
- [ ] Origin credits the actual discoverer honestly
- [ ] No bazaar/village/shopkeeper cliches
- [ ] Visuals described in brackets where needed
- [ ] HARD mode: Panel 5 (Phenomenon→Formula) teaches how to extract physics data from real situations
