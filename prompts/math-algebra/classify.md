# Prompt: Classify Lesson Difficulty — Math + Algebra

You are classifying a Math/Algebra textbook page as **EASY** or **HARD**. You only see this one page — no context about previous or next lessons.

## Input

- Textbook page (image or text)
- Grade: G5-6 (Matematika) or G7-9 (Algebra)

## Output

One word: `EASY` or `HARD`. Then one sentence explaining why.

## Classification — Two Steps

### Step 1: Is the topic inherently complex?

A topic is inherently complex if understanding it requires chaining multiple prior concepts together, or if the topic is abstract/multi-step by nature.

Examples of inherently complex topics (always HARD):
- Logarithms, trigonometry, limits, derivatives
- Quadratic equations, systems of equations
- Proofs, mathematical induction
- Compound operations (fraction of a fraction, nested functions)
- Any topic where a student must recall and combine 2+ prior methods to proceed

If YES → output **HARD**. Stop here.

### Step 2: Does the page teach a procedure?

Look at the page content for these signals:

**HARD signals** (any one = HARD):
- Boxed formula or rule in the page
- Worked example showing multi-step solution
- Step-by-step procedure demonstrated
- "Usul" / "qoida" / "formula" / "algoritm" / "yechish" in headings or bold text
- "Masalalar" / "Misollar" section with calculation exercises
- Graph, coordinate plane, or equation manipulation shown
- Page requires student to DO something with the concept (calculate, solve, convert, prove)

**EASY signals** (all must be true):
- Only definitions and new terms ("...deb ataladi" / "...deyiladi")
- Classification or taxonomy (types of numbers, types of shapes, naming)
- Notation introduction without any procedure attached
- Mostly text explanations, few or no calculation exercises
- No boxed formula
- Student only needs to UNDERSTAND and REMEMBER, not DO

**If mixed** — any HARD signal present → **HARD**.

## Examples

| Page content | Classification | Reason |
|-------------|:-:|--------|
| "Natural sonlar — bu 1, 2, 3, ... ketma-ketlik. Ular sanash uchun ishlatiladi." | EASY | Definition only, no procedure |
| "Kasrlarni qo'shish: maxrajlarni tenglashtirib..." + worked example | HARD | Procedure with multi-step example |
| "Kvadrat tenglama: ax² + bx + c = 0" + discriminant formula | HARD | Inherently complex + formula |
| "O'zgaruvchi — bu noma'lum sonni bildiruvchi harf" | EASY | Notation introduction, no procedure |
| "Logarifm xossalari" — even just listing properties | HARD | Inherently complex topic |
| "Uchburchak turlari: teng tomonli, teng yonli, turli tomonli" | EASY | Classification/taxonomy only |
| "Chiziqli tenglama yechish: 2x + 3 = 7" + step-by-step | HARD | Procedure demonstrated |
| Review page summarizing quadratic methods | HARD | Complex topic, even in review |


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
