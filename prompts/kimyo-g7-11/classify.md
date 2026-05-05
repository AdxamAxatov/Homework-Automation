# Prompt: Classify Lesson Difficulty — Kimyo

You are classifying a Kimyo (Chemistry) textbook page as **EASY** or **HARD**. You only see this one page — no context about previous or next lessons.

## Input

- Textbook page (image or text)
- Grade: G7-11 (Kimyo)

## Output

One word: `EASY` or `HARD`. Then one sentence explaining why.

## Classification — Two Steps

### Step 1: Is the topic inherently complex?

A topic is inherently complex if understanding it requires simultaneous three-scale reasoning (macroscopic + microscopic + symbolic), chemical equation balancing, stoichiometric calculation, or predicting properties from Periodic Table position.

Examples of inherently complex topics (always HARD):
- Chemical equation balancing — requires atoms conserved + charges balanced + symbolic manipulation simultaneously
- Stoichiometric calculations — requires molar mass, formula mass, mole-to-gram conversions
- Three-scale translation tasks — given macroscopic observation, write the microscopic model AND the symbolic formula
- Predicting reactivity or properties from Periodic Table group/period position — requires applying the table as a reasoning tool
- Lab procedure design for a specific chemical reaction — requires hazard identification + procedure + expected observation
- Oxidation state calculation or redox reaction balancing — multi-step symbolic and conceptual reasoning
- Any topic requiring: "Write the balanced equation for..." or "Predict the product of..."

If YES → output **HARD**. Stop here.

### Step 2: Does the page require equation writing, property prediction, or safety reasoning?

Look at the page content for these signals:

**HARD signals** (any one = HARD):
- Boxed chemical equation or formula derivation on the page
- Worked calculation (molar mass, percent composition, stoichiometry)
- "Misol" or "Masala" section with numerical or equation-writing exercises
- Lab procedure described requiring safety precautions + steps + observations
- Property prediction from Periodic Table position (group, period, electronegativity)
- Valence or oxidation state determination
- Three-scale reasoning required (macroscopic observable → microscopic model → symbolic formula)
- "Reaksiya tenglamasi tuzing" or "Formulasini yozing" in exercises

**EASY signals** (all must be true):
- Observable property description only (color, state, smell, solubility) — no formula writing
- Safety rule recall — "Name the safety rule for this equipment" — not designing a procedure
- Element identification by name, symbol, or position in Periodic Table — no prediction
- Classification of substances (metal/nonmetal, acid/base, organic/inorganic) — no formula derivation
- Naming compounds from a given formula — not deriving the formula
- Student only needs to OBSERVE and REMEMBER, not BALANCE or PREDICT

**If mixed** — any HARD signal present → **HARD**.

## Examples

| Page content | Classification | Reason |
|-------------|:-:|--------|
| "Kislorod — rangsiz, hidsiz, mazasiz gaz. Formulasi O₂." | EASY | Observable property description, formula given (not derived) |
| "Suvning elektrolizi: 2H₂O → 2H₂ + O₂. Reaksiya tenglamasini muvozanatlang." | HARD | Equation balancing required |
| "Metallar — elektr tokini o'tkazadi, yaltiroq, egiluvchi." | EASY | Observable property classification only |
| "Natriyning valentligi +1. NaCl formulasini valentlik bo'yicha yozing." | HARD | Valence determination + formula derivation required |
| "Davliy jadvalning 1-guruhidagi elementlar — ishqoriy metallar." | EASY | Classification by Periodic Table position, no prediction |
| "2-guruh metallariga nisbatan 1-guruh metallari nima uchun ko'proq faol?" | HARD | Periodic Table prediction + causal mechanism required |
| "Laboratoriya xavfsizligi: kislota bilan ishlashda ko'zoynak kiyiladi." | EASY | Safety rule recall only |
| "Konsentrlangan sulfat kislota bilan ishlash protokolini tuzing." | HARD | Lab procedure design + safety reasoning required |
| "H₂O — suv, H₂SO₄ — sulfat kislota, NaCl — osh tuzi." | EASY | Formula-to-name identification only |
| "NaOH va HCl o'rtasidagi neytrallash reaksiyasini yozing va muvozanatlang." | HARD | Equation writing and balancing required |


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "mode": "easy|hard",
  "level": "string",
  "reason": "string"
}
```
