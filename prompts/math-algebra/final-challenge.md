# Prompt: Final Challenge (Boss) — Math + Algebra (Hard only)

You are building the Final Challenge for a Math/Algebra Hard mode session. This is the boss fight — HP combat. The student proves mastery of everything taught in this session.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Grade: G5-6 (Matematika) or G7-9 (Algebra)

## Output

4-6 boss questions with HP damage tags. Mix of difficulty tiers.

---

## HP and Damage

| Grade | HP | 
|-------|:--:|
| G5-6 (Matematika) | **80** |
| G7-9 (Algebra) | **100** |

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
- ≥1 word problem (real situation → set up formula → solve)
- ≥1 visual question (read a diagram, bar model, graph, or table and answer)
- G7-9: ≥1 interpretation question ("Javobingiz nimani bildiradi?" or "Bu natija mantiqiymi?")

**MC restriction:**
- G5-6: up to 30% MC allowed (max 1-2 questions)
- G6+: **NO MC.** All open-ended with written steps.

**Difficulty scaling:**
- Easy (-10): single-step, direct application of the formula
- Medium (-20): 2-3 steps, requires choosing the right approach
- Hard (-30): multi-step with context, requires setup + solve + interpret

---

## Example (§23 — multiplying by tens/hundreds)

> **Q1** [Bloom: L2 | PISA: L2 | Damage: -10 HP]
> 56 × 30 = ? Yechimni bosqichma-bosqich ko'rsating.
>
> **Q2** [Bloom: L3 | PISA: L2 | Damage: -10 HP]
> 245 × 400 ni hisoblang va chamalab tekshiring.
>
> **Q3** [Bloom: L3 | PISA: L3 | Damage: -20 HP]
> Zavod har kuni 38 ta detal ishlab chiqaradi. Har bir detal 200 gramm. 5 kunda jami qancha kilogramm detal ishlab chiqariladi?
>
> **Q4** [Bloom: L4 | PISA: L3 | Damage: -20 HP]
> [Jadval: 3 turdagi mahsulot, har birining soni va narxi berilgan] Jami xarajatni hisoblang. Qaysi mahsulot eng qimmatga tushdi?
>
> **Q5** [Bloom: L5 | PISA: L4 | Damage: -30 HP]
> Siz do'kon menejerisiz. 600 so'mlik mahsulotdan 125 ta va 400 so'mlik mahsulotdan 230 ta buyurtma qildingiz. Byudjet 170 000 so'm. Yetadimi? Agar yetmasa, qaysi buyurtmani qisqartirasiz va nima uchun?

---

## Hint Ladder

If student is stuck:
- Hint 1: -5 HP. Remind which formula to use.
- Hint 2: -5 HP. Show the first step.
- Hint 3: -5 HP. Show setup, student completes the calculation.

## Failure Response

Wrong answer → "Hali emas!" (never "Noto'g'ri")
Show WHY the correct answer is correct. Route back to relevant concept.

---

## Rules

- 4-6 questions, distribution 40/40/20 (easy/medium/hard)
- All questions from THIS chapter's content only
- Every question tagged with Bloom + PISA + Damage
- G6+: no MC
- All answers require units
- Hints cost HP, not free
- Language: Uzbek, "Siz" formal
- Visuals: Generate inline SVG for diagram-reading questions (force diagrams, graphs, tables). Place SVG inside the question.


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
