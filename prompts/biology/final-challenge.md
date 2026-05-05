# Prompt: Final Challenge (Boss) — Biology (Hard only)

You are building the Final Challenge for a Biology Hard mode session. HP boss fight. The student proves mastery of biological concepts.

## Input

- Textbook page + all previous phase outputs
- Grade: G5-11 (Biologiya)

## Output

4-6 boss questions with HP damage tags. Mix of difficulty tiers.

---

## HP and Damage

| Grade | HP |
|-------|:--:|
| G5-8 | **100** |
| G9-11 | **150** |

| Difficulty | Damage | Distribution |
|-----------|:------:|:----------:|
| Easy | -10 HP | 40% |
| Medium | -20 HP | 40% |
| Hard | -30 HP | 20% |

For 5 questions: 2 Easy + 2 Medium + 1 Hard.

---

## Question Construction

Every question tagged: `[Bloom: LX | PISA: LX | Damage: -XX HP]`

**Must include:**
- ≥1 **diagram analysis** — identify or label a biological structure or process from an SVG (organelle, organ cross-section, food web, cell cycle stage)
- ≥1 **mechanism explanation** — explain HOW or WHY a biological process works (e.g., "Fotosintez jarayonida kislorod qanday hosil bo'ladi?")
- ≥1 **real-context question** — professional scenario requiring biological knowledge to solve (lab finding, diagnostic observation, ecological data)
- ≥1 **prediction/consequence** — "Agar [condition] bo'lsa, nima sodir bo'ladi?" (e.g., "Agar xlorofill yo'q bo'lsa...")

**MC restriction:**
- G5: up to 30% MC allowed
- G6+: **NO MC.** All open-ended.

**Difficulty scaling:**
- Easy (-10): direct recall or single-step identification (name a structure, state a function)
- Medium (-20): 2-step reasoning (describe a process AND connect it to an outcome)
- Hard (-30): multi-step with context — observe data or diagram → explain mechanism → predict consequence OR recommend action

---

## Hint Ladder

- Hint 1: -5 HP. Show a diagram with one key component highlighted or labeled.
- Hint 2: -5 HP. Show the partial mechanism — "Bu jarayon [X] bilan boshlanadi..."
- Hint 3: -5 HP. Write out the first step of the correct answer — student completes the rest.

## Failure Response

"Hali emas!" — never "Noto'g'ri". Always show WHY the correct answer is correct, with a supporting diagram or step-by-step explanation.

---

## Example (5-question set, Grade 7-8)

> **1. [Easy | -10 HP]**
> Quyidagi hujayra diagrammasida mitoxondriyani toping va uning asosiy vazifasini ayting.
> [SVG: animal cell with organelles labeled A–F]
> `[Bloom: L1 | PISA: L1 | Damage: -10 HP]`
>
> **2. [Easy | -10 HP]**
> Fotosintez qaysi organellada sodir bo'ladi? Bu organellaning o'ziga xos tuzilishi nima uchun kerak?
> `[Bloom: L2 | PISA: L2 | Damage: -10 HP]`
>
> **3. [Medium | -20 HP]**
> Siz mikrobiolog sifatida namunani tekshiryapsiz. Mikroskopda hujayra devori va vakuola ko'rinmoqda. Bu hujayra o'simlikka yoki hayvonga tegishli? Xulosangizni asoslang.
> `[Bloom: L4 | PISA: L3 | Damage: -20 HP]`
>
> **4. [Medium | -20 HP]**
> Quyidagi oziq zanjirini ko'ring. Agar ikkinchi tartibli konsument yo'q bo'lib ketsa, qolgan organizmlar soniga qanday ta'sir qiladi?
> [SVG: food chain with 4 trophic levels]
> `[Bloom: L4 | PISA: L3 | Damage: -20 HP]`
>
> **5. [Hard | -30 HP]**
> Tadqiqotchilar o'rmon ekotizimasida azot miqdori keskin kamayganini aniqladilar. Bu holat: (a) tuproq mikroorganizmlariga, (b) o'simliklarga, (c) hayvonlarga qanday ta'sir qiladi? Har bir trofik daraja bo'yicha izohlab bering.
> `[Bloom: L5 | PISA: L4 | Damage: -30 HP]`

---

## SVG Diagrams

Generate inline SVGs for every diagram analysis question. Include SVGs for:
- Cell structures (plant cell, animal cell, organelles with labels)
- Biological process flows (photosynthesis, respiration, cell division stages)
- Organism anatomy (leaf cross-section, heart chambers, digestive tract segments)
- Ecological diagrams (food web, ecosystem layers, population graphs)

Place the SVG directly inside the question it belongs to. Keep under 300×200px. Use clean lines and readable labels.

---

## Rules

- 4-6 questions, 40/40/20 distribution
- THIS chapter content only — no concepts from outside the session
- Every question tagged Bloom + PISA + Damage
- G6+: no MC — open-ended only
- No numerical calculations — biology questions test observation, explanation, and prediction
- Hints cost HP (-5 HP each)
- Language: Uzbek, "Siz" formal
- "Hali emas!" on wrong answer — never "Noto'g'ri"
- SVGs required for all diagram-analysis questions


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
[
  {
    "q": "string",
    "tags": "[Bloom: LX | PISA: LX | Damage: -XX HP]",
    "ans": ["string", "string"],
    "hint": "string",
    "dmg": 10
  }
]
```
