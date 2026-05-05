# Prompt: Final Challenge (Boss) — Physics (Hard only)

You are building the Final Challenge for a Physics Hard mode session. HP boss fight. The student proves mastery.

## Input

- Textbook page + all previous phase outputs
- Grade: G7-11 (Fizika)

## Output

4-6 boss questions with HP damage tags. Mix of difficulty tiers.

---

## HP and Damage

| Grade | HP |
|-------|:--:|
| G7-8 | **100** |
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
- ≥1 formula application (given values, find unknown)
- ≥1 diagram reading (force diagram, circuit, graph → answer question)
- G9-11: ≥1 interpretation ("Bu natija fizik jihatdan nimani bildiradi?")

**MC restriction:**
- G7: up to 30% MC
- G8+: **NO MC.** Open-ended with shown work.

**Difficulty scaling:**
- Easy (-10): direct formula substitution, one step
- Medium (-20): 2-3 steps, unit conversion may be needed
- Hard (-30): multi-step with context, setup + solve + interpret

---

## Hint Ladder

- Hint 1: -5 HP. Remind which formula/law applies.
- Hint 2: -5 HP. Show what quantities are given.
- Hint 3: -5 HP. Show setup, student completes calculation.

## Failure Response

"Hali emas!" — never "Noto'g'ri". Show WHY the correct answer is correct.

---

## Rules

- 4-6 questions, 40/40/20 distribution
- THIS chapter content only
- Every question tagged Bloom + PISA + Damage
- G8+: no MC
- All answers require units
- Hints cost HP
- Language: Uzbek, "Siz" formal
- Visuals: Generate inline SVG for diagram-reading questions (force diagrams, circuits, graphs, data tables). Place SVG inside the question.


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
