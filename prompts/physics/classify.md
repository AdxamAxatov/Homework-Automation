# Prompt: Classify Lesson Difficulty — Physics

You are classifying a Physics textbook page as **EASY** or **HARD**. You only see this one page — no context about previous or next lessons.

## Input

- Textbook page (image or text)
- Grade: G7-11 (Fizika)

## Output

One word: `EASY` or `HARD`. Then one sentence explaining why.

## Classification — Two Steps

### Step 1: Is the topic inherently complex?

A topic is inherently complex if understanding it requires chaining multiple prior concepts, involves mathematical modeling of phenomena, or is abstract/multi-step by nature.

Examples of inherently complex topics (always HARD):
- Electromagnetic induction, wave interference, thermodynamics laws
- Circuit analysis (Ohm's law with multiple resistors)
- Projectile motion, rotational dynamics
- Nuclear physics, quantum phenomena
- Any topic requiring 2+ prior formulas to solve

If YES → output **HARD**. Stop here.

### Step 2: Does the page teach a procedure or formula application?

**HARD signals** (any one = HARD):
- Boxed formula or law (F=ma, V=IR, E=mc²)
- Worked example with multi-step calculation
- Laboratory procedure or experiment described
- "Qonun" / "formula" / "usul" / "tajriba" in headings
- Graph interpretation requiring calculation
- Unit conversion procedures

**EASY signals** (all must be true):
- Only definitions and descriptions of phenomena
- Classification of physical concepts (types of energy, types of waves)
- Historical introduction to a field
- Qualitative descriptions without formulas
- No calculation exercises on the page

**If mixed** — any HARD signal present → **HARD**.

## Examples

| Page content | Classification | Reason |
|-------------|:-:|--------|
| "Kuch — bu jismning tezlanishini o'zgartiruvchi ta'sir" + definition only | EASY | Definition, no procedure |
| "Nyuton ikkinchi qonuni: F = ma" + worked problems | HARD | Formula + multi-step examples |
| "Elektr tokining turlari: o'zgarmas va o'zgaruvchan" | EASY | Classification only |
| "Om qonuni: I = U/R" + circuit diagram + calculation | HARD | Formula + procedure |
| "Termodinamikaning birinchi qonuni" — even just stating it | HARD | Inherently complex topic |
| "Energiya turlari: kinetik, potensial, issiqlik" | EASY | Taxonomy only |


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
