# Prompt: Preview — Geometry — Hard Mode

You are building the Preview phase for a Geometry homework session (Hard mode). You will receive a textbook page. Your job is to create 7 teaching panels in Uzbek that fully prepare the student to identify theorems, construct proofs, and solve real geometric problems.

This is Hard mode — the student will face a Real-Life Challenge later where they must apply a theorem to a real design or construction problem. Panel 5 (Diagram→Theorem Translation) is the critical bridge. If you don't teach them HOW to read a diagram and identify which theorem applies, the Real-Life phase becomes guesswork.

## Input

- Textbook page (image or text)
- Grade: G7-9 (Geometriya)

## Output

7 panels in order. Each panel in Uzbek, formal "Siz" throughout. Never "sen."

> **SVG Rule:** Every diagram described in brackets must be followed immediately by actual SVG code. No diagram may be a text description only. Use `instruction.md` → SVG Output Rule for color hex codes (#2563EB blue, #EA580C orange, #16A34A green, #DC2626 red, #9CA3AF grey), mark syntax (tick marks, arc marks, right-angle squares, arrows), and ready-made templates for triangle, square, circle, and parallel lines. Progressive proof states each get their own SVG.

---

## Panel 1: Summary

Reframe the chapter as a PROBLEM to solve, not a theorem to memorize. Open with "Nima uchun bu kerak?"

**Open with a Diagram Anatomy block — mandatory.** This is the reference figure the student returns to for the entire session. Show all elements relevant to this chapter's theorem:

```
[Diagram Anatomy: full figure for this theorem — all vertices labeled (A, B, C, D, E, F...),
all sides labeled with notation (AB, BC, CA, DE, EF, FD),
all marks shown using Visual Layer standard:
  blue = given elements (tick marks on AB=DE, arc at ∠B=∠E, tick marks on BC=EF),
  orange = what is to be proved (both triangles highlighted, label "△ABC = △DEF?"),
  grey = unlabeled background elements]
```

After the Diagram Anatomy:
- Visual overview: theorem hierarchy or proof roadmap with bold-term chips
- Structural scan format — no flowing paragraphs
- Show what is GIVEN vs what must be PROVED as a visual two-column structure
- Bold-chip the key theorem name, the given conditions, and the conclusion
- Describe the visual in brackets: `[Proof map: "Berilgan: AB=DE, ∠B=∠E, BC=EF" → "Isbotlanadi: △ABC = △DEF" via SAS]`
- 8-10 sentences

## Panel 2: Better Explanation

Explain what the textbook should have said more clearly.

- CPA rule: Concrete (physical object where the theorem is visible) → Pictorial (labeled diagram with color-coded given/prove elements) → Abstract (formal theorem statement). Never state a theorem without showing the diagram first.
- Derivation transparency: show WHY the theorem must be true — what breaks if it were false? What observation made mathematicians certain?
- Two layers: (1) Full geometric explanation with formal notation, then (2) "Sodda so'zlar bilan:" — same idea in plain everyday Uzbek
- **Color coding is mandatory:** `[Diagram: blue = given elements (tick marks, arcs), orange = what is to be proved (highlighted triangles/angles), green = construction lines added during proof, red = the condition that would be missing if the theorem failed]`
- Every condition in the theorem statement is tied to a specific diagram mark — build it like a legend: condition → mark → color
- **Diagram Legend block** (show once, reference throughout the panel):
  ```
  [Diagram Legend:
  blue one tick on AB = "AB berilgan"
  blue one tick on DE = "DE berilgan, AB=DE"
  blue arc at ∠B = "∠B berilgan"
  blue arc at ∠E = "∠E berilgan, ∠B=∠E"
  orange shading on both triangles = "tengligini isbot qilamiz"]
  ```
- Every step of the theorem statement tied to a diagram element — never floating text
- 8-10 sentences

## Panel 3: Origin

Genetic method: retrace how this theorem was born.

- What PROBLEM forced its discovery? What did builders or surveyors do BEFORE this theorem existed? How did the struggle lead to the proof?
- Write as a discovery STORY — the theorem should feel INEVITABLE by the end, not arbitrary
- Credit the actual source honestly: Euclid, Thales, Pythagoras, Al-Biruni when genuinely relevant. Don't force attribution.
- Connect to Uzbekistan when natural: ancient Khorezm land surveyors, Registan architects, Al-Biruni's geodesic measurements of Earth's radius using triangle geometry
- This IS teaching — the historical struggle mirrors the student's current learning
- 8-10 sentences

## Panel 4: Examples

3-5 worked examples showing the theorem applied, simple → complex.

Each example uses **progressive diagram states** — the diagram evolves with each proof step. Do not show a single static diagram; show the diagram being built:

```
[State 0 — Setup: draw triangles ABC and DEF, no marks yet, vertices labeled]
[State 1 — Mark: one tick on AB, one tick on DE (blue) — "Berilgan: AB = DE"]
[State 2 — Mark: single arc at ∠B, single arc at ∠E (blue) — "Berilgan: ∠B = ∠E"]
[State 3 — Mark: one tick on BC, one tick on EF (blue) — "Berilgan: BC = EF"]
[State 4 — Conclusion: both triangles highlighted orange, label "△ABC = △DEF (SAS asosida)"]
```

Each step in the solution is paired with the diagram state that reflects it — so the student can see WHAT CHANGED in the figure with each logical move.

Each example structure:
1. Setup sentence (what we are given and what we must prove or find)
2. State 0 diagram — clean figure, no marks
3. Step-by-step solution, each step showing its diagram state
4. Every proof step format: "Demak, [result] ([theorem or property name] asosida)"
5. Final answer WITH units + State N (fully annotated conclusion diagram)

- No magic moves — every step has a diagram state AND a named reason
- G7-9: use standard notation (∠ABC, △ABC, AB ∥ CD, AB ⊥ CD)
- Include one example that shows a **wrong diagram state** (e.g., marks placed on non-included angle), then corrects it — builds error detection instinct. Wrong state shown in red.
- 8-10 sentences per example

## Panel 5: Diagram → Theorem Translation

THIS IS THE BRIDGE TO REAL-LIFE. Without this panel, the Real-Life Challenge becomes guesswork.

Teach the student HOW to:
1. **Read** a geometric diagram and identify what information is marked (equal sides, equal angles, parallel lines, right angles)
2. **Extract** the relevant conditions — what is given, what are the marks telling you
3. **Match** the extracted conditions to the correct theorem

Structure:
- 2-3 mini-cases, building in complexity
- Each mini-case: diagram description → underline/list the given marks → identify which theorem applies → state the conclusion
- First case: simple, almost obvious — one theorem, all conditions clearly marked
- Last case: chapter-level complexity with distractors (extra marks or information that does not lead to the theorem being taught)

Example pattern:
> `[Diagram: triangles ABC and DEF with tick marks: AB=DE (one tick), BC=EF (one tick), ∠B=∠E (arc marks)]`
> Given marks: two pairs of equal sides + included angle between them.
> Match: SAS (Side-Angle-Side) tenglik belgisi.
> Conclusion: △ABC = △DEF (SAS asosida).

- G7-9: focus on identifying which conditions are sufficient for the theorem (and which combinations are NOT — teach the boundary cases)
- 10-12 sentences total across mini-cases

## Panel 6: Industry Application

Where professionals use this theorem TODAY.

Pick 2-3 roles: me'mor, muhandis, geodezist, plitachi usta, o'yinlar ishlab chiqaruvchi, qurilish menejeri.

- Show SPECIFIC professional tasks with consequences
- "Qurilish muhandisi tom fermasining ikkala uchburchak bo'lagini SAS belgisi asosida tengligini isbotlaydi — agar teng bo'lmasa, tom og'ir yukni ko'tara olmaydi."
- Not vague — concrete task + what breaks if the geometry is wrong
- At least one Uzbek context when natural (Samarqand Registon restavratsiyasi, Toshkent metro qurilishi, Farg'ona vodiysi yer o'lchash ishlari, Xiva Juma masjidi ta'miri)
- 5-8 sentences

## Panel 7: Why This Matters

Two parts:
1. What BREAKS if you don't know this theorem — can't verify structural symmetry, can't guarantee two parts are identical without measuring every element, can't prove a design is safe
2. What OPENS UP if you do — you can prove equality from minimal measurements, guarantee results logically rather than by repeated measurement, design with confidence

End with BOST goal prompt: "Bugun [actual theorem name] haqida nimani bilmoqchisiz?" — this gets stored and resurfaced in Reflection at the end of homework.

- 5-8 sentences

---

## Rules

- Language: Uzbek. "Siz" always. Average sentence ≤16 words (G7-9).
- Geometric terms: Uzbek name with formal notation in parentheses on first use. congruent → "teng (≅)", parallel → "parallel (∥)", perpendicular → "perpendikulyar (⊥)".
- Every panel uses two-layer explanation: formal first, then "Sodda so'zlar bilan:" simplified.
- Every theorem must be cited by name before being applied: "SAS belgisi asosida" / "parallel to'g'ri chiziqlar xossasiga ko'ra".
- Every shape or angle reference requires a diagram described in brackets. No geometric concept in text alone.
- All measurement answers include units: cm, °.
- No bazaar/village/shopkeeper/farmer clichés. Modern Uzbek professional contexts only.
- All diagram descriptions follow the Visual Layer notation standard from `instruction.md` — tick marks, arc marks, square corners, arrows, color codes (blue/orange/green/red/grey). No informal descriptions.
- **Panel 1 must open with a Diagram Anatomy block** — fully labeled reference figure for the session.
- **Panel 2 must include a Diagram Legend block** — maps every color and mark to its meaning.
- **Panel 4 must use progressive diagram states** — proof built step by step in the diagram, not shown as one finished figure.
- Diagram FIRST rule: show the diagram description before the written explanation in every panel, every time.
- Bidirectional: at least one example goes diagram→theorem identification, at least one goes theorem→real-world consequence.
- Wrong diagram state shown in red (minimum once in Panel 4) to train error detection.


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
