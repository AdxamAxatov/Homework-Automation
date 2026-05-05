# Geometry — Homework Builder Instruction

You are building a homework session for Geometry (G7-9). Follow these steps in order.

## Step 1: Identify the lesson

You receive a chapter-section reference (e.g., "Grade 7 Geometry, §9 SAS Congruence Criterion" or "Grade 7 Geometry, §5 Types of Angles").

Find and read the corresponding textbook pages. Extract:
- Topic name
- All definitions and geometric terms on the page
- All theorems and their statements
- All proof steps shown
- All worked examples and construction procedures
- All exercises/problems listed
- All diagrams, labeled figures, and visual elements

## Step 2: Classify difficulty

Read `06-prompts/geometriya-g7-ru/classify.md` and apply it to the extracted content.

Two checks:
1. Is the topic inherently complex? (requires chaining prior concepts, involves formal proof, multi-step theorem) → **HARD**
2. Does the page teach a procedure or proof? (boxed theorem, worked proof, construction steps, "masala" section) → **HARD**
3. Only definitions, taxonomy, notation intro, no proof or procedure → **EASY**

Output: EASY or HARD + one sentence why.

## Step 3: Load the right prompt

- If EASY → read `06-prompts/geometriya-g7-ru/preview-easy.md`
- If HARD → read `06-prompts/geometriya-g7-ru/preview-hard.md`

## Step 4: Build

Follow the loaded prompt exactly. Use the extracted textbook content as your source material. Every panel must reference actual content from the textbook page — do not invent theorems, proof steps, or definitions that are not in the source.

Geometry-specific rule: Every panel that mentions a shape, angle, or theorem MUST include (1) a diagram described in brackets — e.g., `[Diagram: triangle ABC with tick marks on AB and AC showing equal sides]` — followed immediately by (2) actual SVG code for that diagram. Never describe a geometric concept in text alone, and never leave a diagram as a bracket description without SVG output. See the **SVG Output Rule** section below for templates and mark syntax.

---

## Visual Layer — Diagram Notation Standard (mandatory for all phases)

All diagram descriptions in brackets must follow this notation. This is the visual grammar of the entire session — consistent marks allow the rendering engine to produce accurate figures and allow students to read diagrams unambiguously.

### Mark types

| Element | Notation in brackets |
|---------|---------------------|
| Equal sides (1st pair) | `one tick on AB, one tick on DE` |
| Equal sides (2nd pair) | `two ticks on BC, two ticks on EF` |
| Equal sides (3rd pair) | `three ticks on AC, three ticks on DF` |
| Equal angles (1st pair) | `single arc at ∠B, single arc at ∠E` |
| Equal angles (2nd pair) | `double arc at ∠A, double arc at ∠D` |
| Right angle | `square corner symbol at ∠B` |
| Parallel lines (1st pair) | `single arrow on AB, single arrow on CD` |
| Parallel lines (2nd pair) | `double arrow on EF, double arrow on GH` |
| Construction line (added) | `dashed line from A to midpoint M` |
| Unknown / to find | `question mark on side AC` |

### Color coding (use in all phase descriptions)

| Color | Meaning |
|-------|---------|
| **Blue** | Given information — what is already known |
| **Orange** | What must be proved or found |
| **Green** | Construction line added during the proof |
| **Red** | Common error — shown and corrected |
| **Grey** | Background / context elements |

### Diagram states (for proofs and examples)

When a concept involves multiple steps, show the diagram in progressive states — not a single static image:

```
[State 0 — Given: triangle ABC, no marks yet]
[State 1 — Mark: one tick on AB, one tick on DE (given AB=DE)]
[State 2 — Mark: single arc at ∠B, single arc at ∠E (given ∠B=∠E)]
[State 3 — Mark: one tick on BC, one tick on EF (given BC=EF)]
[State 4 — Conclusion: triangles highlighted orange, label "△ABC = △DEF (SAS)"]
```

Use state diagrams in: Preview Panel 3 (worked examples), Final Challenge proof questions, Real-Life sub-questions that require proof.

### Diagram Anatomy block (mandatory in Panel 1 of every Preview)

Every session opens with a fully labeled reference diagram — the "map" the student returns to throughout the session. Format:

```
[Diagram Anatomy: full figure for this chapter — all vertices labeled (A, B, C...), 
all sides labeled (a, b, c or AB, BC, CA), all angles labeled (∠A, ∠B, ∠C), 
all marks shown (tick marks, arcs, right angle squares, parallel arrows),
blue = given elements, orange = what is typically asked]
```

This diagram is described once in Panel 1 and referenced by label in all later panels ("kabi 1-rasmda ko'rsatilgan").

---

## SVG Output Rule — mandatory for every diagram

Whenever a diagram is required, output **actual SVG code** immediately after the bracket description. Do not leave a diagram as text only — the SVG must be renderable by a browser.

### Output order (always this sequence)

1. Bracket description: `[Diagram: triangle ABC, right angle at B, blue sides AB and BC, orange hypotenuse AC]`
2. SVG code block immediately after — no other text between them.

### SVG style baseline

```svg
<svg viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg"
     style="font-family: sans-serif; font-size: 14px;">
  <!-- geometry here -->
</svg>
```

**Color palette — must match Visual Layer standard:**

| Role | Hex | SVG stroke/fill |
|------|-----|-----------------|
| Given (blue) | `#2563EB` | `stroke="#2563EB"` |
| To prove (orange) | `#EA580C` | `stroke="#EA580C"` |
| Construction (green) | `#16A34A` | `stroke="#16A34A" stroke-dasharray="6 3"` |
| Error (red) | `#DC2626` | `stroke="#DC2626"` |
| Background (grey) | `#9CA3AF` | `stroke="#9CA3AF"` |
| Shape fill | transparent | `fill="none"` |
| Labels | near-black | `fill="#111827"` |

**Stroke widths:** `stroke-width="2"` for shape edges; `stroke-width="1.5"` for marks (ticks, arcs).

### Mark types in SVG

**Tick mark — equal side (one tick on segment midpoint):**
```svg
<!-- midpoint of AB at (100,100), segment angle 45°: tick is perpendicular -->
<line x1="95" y1="105" x2="105" y2="95" stroke="#2563EB" stroke-width="2"/>
```

**Double tick mark — 2nd equal pair:**
```svg
<line x1="93" y1="107" x2="103" y2="97" stroke="#2563EB" stroke-width="2"/>
<line x1="97" y1="103" x2="107" y2="93" stroke="#2563EB" stroke-width="2"/>
```

**Arc mark — equal angle (small arc near vertex, opening toward triangle interior):**
```svg
<!-- Single arc at vertex B=(100,150) -->
<path d="M 118,142 A 20 20 0 0 0 88,138" fill="none" stroke="#2563EB" stroke-width="1.5"/>
```

**Double arc mark — 2nd equal angle:**
```svg
<path d="M 120,142 A 22 22 0 0 0 86,136" fill="none" stroke="#2563EB" stroke-width="1.5"/>
<path d="M 116,140 A 18 18 0 0 0 90,135" fill="none" stroke="#2563EB" stroke-width="1.5"/>
```

**Right angle square:**
```svg
<!-- At vertex B=(40,160), sides going right (+x) and up (-y) -->
<polyline points="55,160 55,145 40,145" fill="none" stroke="#2563EB" stroke-width="2"/>
```

**Parallel arrow (single arrow on segment, use marker-mid):**
```svg
<defs>
  <marker id="arr1" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
    <path d="M0,1 L7,4 L0,7 Z" fill="#2563EB"/>
  </marker>
</defs>
<line x1="40" y1="60" x2="200" y2="60" stroke="#2563EB" stroke-width="2"
      marker-mid="url(#arr1)"/>
<!-- Place a transparent midpoint circle to trigger marker-mid -->
<circle cx="120" cy="60" r="0" fill="none" stroke="#2563EB"
        marker-start="url(#arr1)"/>
```

**Construction / dashed line:**
```svg
<line x1="50" y1="50" x2="180" y2="150"
      stroke="#16A34A" stroke-width="1.5" stroke-dasharray="6 3"/>
```

**Unknown element — orange question mark label:**
```svg
<text x="128" y="102" fill="#EA580C" font-weight="bold" font-size="16">?</text>
```

### Common geometry SVG templates (adapt coordinates as needed)

**Triangle ABC (general, apex at top):**
```svg
<svg viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg"
     style="font-family: sans-serif; font-size: 14px;">
  <polygon points="120,25 25,175 215,175"
           fill="none" stroke="#9CA3AF" stroke-width="2"/>
  <text x="113" y="18"  fill="#111827">A</text>
  <text x="10"  y="188" fill="#111827">B</text>
  <text x="218" y="188" fill="#111827">C</text>
</svg>
```

**Right triangle ABC (right angle at B):**
```svg
<svg viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg"
     style="font-family: sans-serif; font-size: 14px;">
  <polygon points="40,30 40,170 200,170"
           fill="none" stroke="#9CA3AF" stroke-width="2"/>
  <!-- right angle square at B=(40,170) -->
  <polyline points="55,170 55,155 40,155"
            fill="none" stroke="#2563EB" stroke-width="2"/>
  <!-- hypotenuse AC orange -->
  <line x1="40" y1="30" x2="200" y2="170"
        stroke="#EA580C" stroke-width="2"/>
  <text x="28"  y="24"  fill="#111827">A</text>
  <text x="22"  y="188" fill="#111827">B</text>
  <text x="205" y="188" fill="#111827">C</text>
</svg>
```

**Square ABCD:**
```svg
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"
     style="font-family: sans-serif; font-size: 14px;">
  <rect x="35" y="35" width="130" height="130"
        fill="none" stroke="#9CA3AF" stroke-width="2"/>
  <text x="22"  y="30"  fill="#111827">A</text>
  <text x="170" y="30"  fill="#111827">B</text>
  <text x="170" y="180" fill="#111827">C</text>
  <text x="22"  y="180" fill="#111827">D</text>
</svg>
```

**Circle with center O and radius r:**
```svg
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"
     style="font-family: sans-serif; font-size: 14px;">
  <circle cx="100" cy="100" r="70"
          fill="none" stroke="#9CA3AF" stroke-width="2"/>
  <!-- center dot -->
  <circle cx="100" cy="100" r="3" fill="#111827"/>
  <text x="106" y="104" fill="#111827">O</text>
  <!-- radius line in blue -->
  <line x1="100" y1="100" x2="170" y2="100"
        stroke="#2563EB" stroke-width="2"/>
  <text x="128" y="93"  fill="#2563EB">r</text>
</svg>
```

**Two parallel lines with transversal:**
```svg
<svg viewBox="0 0 240 180" xmlns="http://www.w3.org/2000/svg"
     style="font-family: sans-serif; font-size: 14px;">
  <defs>
    <marker id="a" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,1 L7,4 L0,7 Z" fill="#9CA3AF"/>
    </marker>
  </defs>
  <!-- parallel lines -->
  <line x1="20" y1="60"  x2="220" y2="60"  stroke="#9CA3AF" stroke-width="2"/>
  <line x1="20" y1="120" x2="220" y2="120" stroke="#9CA3AF" stroke-width="2"/>
  <!-- transversal -->
  <line x1="60" y1="20"  x2="160" y2="160" stroke="#2563EB" stroke-width="2"/>
  <!-- arrow marks for parallel -->
  <line x1="90"  y1="60"  x2="110" y2="60"  stroke="#9CA3AF" stroke-width="2" marker-end="url(#a)"/>
  <line x1="90"  y1="120" x2="110" y2="120" stroke="#9CA3AF" stroke-width="2" marker-end="url(#a)"/>
</svg>
```

### Progressive state SVGs

For proof steps, output one SVG per state, labeled `State 0`, `State 1`, etc. Each state adds marks to the previous — do not redraw from scratch, just add the new element SVG lines:

```
State 0 — Given figure, no marks:
[SVG: clean triangle ABC]

State 1 — Given AB = DE:
[SVG: same triangle + one tick on AB in blue]

State 2 — Given ∠B = ∠E:
[SVG: State 1 + single arc at ∠B in blue]
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
- [ ] Every theorem cited by name before being used
- [ ] Every shape or angle reference has a diagram description in brackets
- [ ] Every diagram description is followed immediately by SVG code — no diagram is text-only
- [ ] All SVG diagrams use the correct color hex codes (#2563EB blue, #EA580C orange, #16A34A green, #DC2626 red, #9CA3AF grey)
- [ ] All diagram descriptions follow the Visual Layer notation standard (ticks, arcs, color codes)
- [ ] Panel 1 opens with a Diagram Anatomy block (fully labeled reference figure)
- [ ] Proof examples use progressive diagram states (State 0 → State N), not a single static image
- [ ] All measurement answers include units (cm, °)
- [ ] No magic moves — every proof step has a named reason
- [ ] Origin credits the actual inventor (Euclid, Al-Biruni, Thales — honest attribution only)
- [ ] No bazaar/village/shopkeeper clichés — modern Uzbek professional contexts only
- [ ] HARD mode: Panel 5 (Diagram→Theorem Translation) teaches HOW to read a diagram and identify which theorem applies — not just shows examples
- [ ] HARD mode: at least one example includes a deliberately wrong diagram state to build error-detection instinct
