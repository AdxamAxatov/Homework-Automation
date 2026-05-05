# Prompt: Classify Lesson Difficulty — Geometry

You are classifying a Geometry textbook page as **EASY** or **HARD**. You only see this one page — no context about previous or next lessons.

## Input

- Textbook page (image or text)
- Grade: G7-9 (Geometriya)

## Output

One word: `EASY` or `HARD`. Then one sentence explaining why.

## Classification — Two Steps

### Step 1: Is the topic inherently complex?

A topic is inherently complex if understanding it requires chaining multiple prior geometric concepts, or if the topic demands formal logical reasoning to proceed.

Examples of inherently complex topics (always HARD):
- Congruence criteria (SAS, SSS, ASA) — require understanding of triangle elements and logical proof structure
- Parallel lines and transversal angle relationships — require chaining angle definitions with parallelism
- Triangle angle sum theorem — requires proof via parallel line construction
- Any topic where the student must construct a multi-step logical argument
- Any topic where a theorem must be proved before it can be used
- Constructions (compass and ruler) — require chaining multiple prior procedures
- Side-angle relationships and triangle inequality — require combining multiple theorems

If YES → output **HARD**. Stop here.

### Step 2: Does the page teach a procedure or proof?

Look at the page content for these signals:

**HARD signals** (any one = HARD):
- Boxed theorem or rule on the page
- Worked proof showing step-by-step logical argument
- "Teorema", "isbotlash", "dalil", "isbot" in headings or bold text
- Congruence marks (tick marks, arc marks) used to label equal elements
- Construction steps shown (compass arcs, perpendicular construction)
- "Masala", "misollar" section with calculation or proof exercises
- Angle relationships derived from a diagram (not just named)
- Page requires student to DO something with the concept (prove, calculate, construct, identify which theorem applies)

**EASY signals** (all must be true):
- Only definitions and new terms ("...deb ataladi" / "...deyiladi")
- Classification or taxonomy (types of triangles, types of angles, naming shapes)
- Notation introduction without any theorem or proof attached
- Mostly text and labeled diagrams with names — no derivation
- No boxed theorem
- Student only needs to UNDERSTAND and REMEMBER, not PROVE or CONSTRUCT

**If mixed** — any HARD signal present → **HARD**.

## Examples

| Page content | Classification | Reason |
|-------------|:-:|--------|
| "Uchburchak — uchta nuqtadan iborat geometrik figura." + types listed | EASY | Definition and taxonomy only, no proof |
| "Uchburchaklarning tenglik belgisi (SAS)" + proof steps | HARD | Theorem with formal proof |
| "To'g'ri burchak — 90° ga teng burchak" | EASY | Notation introduction, no procedure |
| "Parallel to'g'ri chiziqlar va kesuvchi" + angle relationships derived | HARD | Requires chaining angle definitions |
| "Burchak turlari: o'tkir, to'g'ri, o'tmas, to'liq" | EASY | Classification only |
| "Uchburchak ichki burchaklari yig'indisi = 180°" + proof via parallel line | HARD | Theorem proof, inherently complex |
| "Perpendikulyar to'g'ri chiziqlar — o'zaro 90° hosil qiladi" | EASY | Definition, no derivation |
| "Teng yonli uchburchak asosi burchaklari tengligi" + proof | HARD | Theorem proof, multi-step |
| "Tsirkul va chizg'ich yordamida burchakni ikkiga bo'lish" + steps | HARD | Construction procedure |
| "Uchburchak tomonlari: a, b, c; burchaklari: A, B, C" | EASY | Notation introduction only |


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
