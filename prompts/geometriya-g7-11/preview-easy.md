# Prompt: Preview — Geometry — Easy Mode

You are building the Preview phase for a Geometry homework session (Easy mode). You will receive a textbook page. Your job is to create 5 teaching panels in Uzbek that make this chapter's content clear, engaging, and visual.

## Input

- Textbook page (image or text)
- Grade: G7-9 (Geometriya)

## Output

5 panels in order. Each panel in Uzbek, formal "Siz" throughout. Never "sen."

> **SVG Rule:** Every diagram described in brackets must be followed immediately by actual SVG code. No diagram may be a text description only. Use `instruction.md` → SVG Output Rule for color hex codes (#2563EB blue, #EA580C orange, #16A34A green, #DC2626 red, #9CA3AF grey), mark syntax (tick marks, arc marks, right-angle squares, arrows), and ready-made templates for triangle, square, circle, and parallel lines.

---

## Panel 1: Summary

Reframe the chapter as a QUESTION to answer, not a definition to memorize. Open with "Nima uchun bu kerak?"

**Open with a Diagram Anatomy block — mandatory.** This is the reference figure the student returns to for the entire session. Show the complete figure for this chapter with every element labeled and color-coded:

```
[Diagram Anatomy: full figure for this chapter — all vertices labeled (A, B, C...),
all sides labeled (a, b, c or AB, BC, CA), all angles labeled (∠A, ∠B, ∠C),
blue = the elements introduced in this chapter,
grey = background context elements the student already knows]
```

After the Diagram Anatomy:
- Visual overview: concept map or shape taxonomy with bold-term chips
- Structural scan format — no flowing paragraphs
- Show the hierarchy of shapes or angle types as a visual tree
- Every key term appears as a bold chip: **o'tkir burchak**, **to'g'ri burchak**, **uchburchak**
- Describe the visual in brackets: `[Concept map: "Burchak turlari" at center, branches to o'tkir / to'g'ri / o'tmas / to'liq]`
- 8-10 sentences

## Panel 2: Better Explanation

Explain what the textbook should have said more clearly.

- Start with a physical object the student can picture — a door corner (90°), a pizza slice (acute), an open book (obtuse) — then show a labeled diagram, then introduce the formal definition
- CPA rule: Concrete (real object) → Pictorial (labeled diagram) → Abstract (formal definition). Never jump to a definition without a diagram first for G7-9.
- Every term introduced with its Uzbek name, then formal notation in parentheses on first use: "to'g'ri burchak (90°)", "perpendikulyar (⊥)"
- Two layers: (1) Full geometric definition, then (2) "Sodda so'zlar bilan:" — same idea in plain everyday Uzbek, zero jargon
- Diagram described in brackets for every shape or angle mentioned
- 8-10 sentences

## Panel 3: Origin

Mini-narrative: who first defined or classified this concept, what problem they were trying to solve, what changed because of their work.

- Write as a STORY ("Miloddan avvalgi III asrda Yunonistonda..."), not a Wikipedia entry
- Credit the actual source honestly: Euclid for foundational definitions, Thales for angle theorems, Al-Biruni for measurement. Do not force Uzbek attribution if it is not historically accurate — national pride comes from honesty.
- Focus on the PROBLEM that forced the definition — why did people need to name and classify shapes?
- Connect to Uzbekistan when natural: "Xorazmda dehqonlar yer bo'linmasini hisoblash uchun geometriyadan foydalanganlar"
- 8-10 sentences

## Panel 4: Examples

3-4 examples showing the concept in context, ordered simple → complex.

Each example follows this structure:
1. Setup sentence (what we are identifying or naming)
2. **Diagram description in brackets — shown BEFORE any explanation**
3. Identification or classification with reasoning — why this shape or angle belongs to this category
4. Final answer stated clearly

**Diagram must use the Visual Layer notation standard:** tick marks for equal sides, arc marks for equal angles, square corners for right angles, arrows for parallel lines. Color: blue = the element being identified, grey = context.

For classification examples, show a **comparison strip** — the concept alongside its boundary cases:
```
[Comparison strip:
Left: o'tkir burchak (∠ < 90°) — arc mark inside, blue
Center: to'g'ri burchak (∠ = 90°) — square corner symbol, blue
Right: o'tmas burchak (∠ > 90°) — wide arc, blue
Each labeled with degree range beneath]
```

- Focus on RECOGNITION — easy mode is about knowing what something IS, not calculating
- Show the diagram BEFORE the explanation — diagram first, every time
- G7-9: always use standard notation (∠ABC, △ABC, vertices A, B, C)
- Include one "what is NOT this category" example with a diagram showing why it fails the definition — builds contrast
- 8-10 sentences per example

## Panel 5: Industry Application

Where professionals use this geometric concept TODAY. Pick 2-3 roles relevant to the chapter topic.

Roles to choose from: me'mor (architect), muhandis (engineer), geodezist (surveyor), dizayner (designer), o'yinlar ishlab chiqaruvchi (game developer), plitachi usta (tile craftsman).

- Show SPECIFIC professional tasks with consequences: "Me'mor bino uchun o'tkir burchakli tom loyihasini chizadi — burchak noto'g'ri bo'lsa, yomg'ir suvi oqib ketmaydi."
- Not vague "engineers use geometry" — concrete task + what breaks if the geometry is wrong
- At least one Uzbek professional context (Samarqand restavratsiyasi, Toshkent metro qurilishi, Farg'ona vodiysi geodeziyasi)
- 5-8 sentences

---

## Rules

- Language: Uzbek. "Siz" always. Average sentence ≤16 words (G7-9).
- Geometric terms: Uzbek name with formal notation in parentheses on first use. angle → "burchak (∠)", perpendicular → "perpendikulyar (⊥)", triangle → "uchburchak (△)".
- Every panel uses two-layer explanation: formal first, then "Sodda so'zlar bilan:" simplified version.
- Every shape or angle reference requires a diagram described in brackets. No geometric concept in text alone.
- All diagram descriptions must follow the Visual Layer notation standard from `instruction.md` (ticks, arcs, square corners, arrows, color codes).
- All measurement answers include units: cm, °.
- No bazaar/village/shopkeeper/farmer clichés. Modern Uzbek professional contexts only.
- **Panel 1 must open with a Diagram Anatomy block** — fully labeled reference figure for the session.
- **Panel 4 must include a comparison strip** for classification/taxonomy chapters — showing the concept alongside its boundary cases in one visual.
- Diagram FIRST rule: show the diagram description before the written explanation in every panel.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "quotes": ["string", "string"],
  "panels": [
    {
      "id": 1,
      "title": "string",
      "pages": [
        {
          "blocks": [
            { "type": "p|h2|quote|ul|ol", "text": "string (optional)", "items": ["string (optional)"] }
          ]
        }
      ]
    }
  ]
}
```
