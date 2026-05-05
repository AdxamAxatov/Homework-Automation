# Prompt: Final Challenge (Boss) — Kimyo (Hard only)

You are building the Final Challenge for a Kimyo Hard mode session. This is the boss fight — HP combat. The student proves mastery of everything taught in this session.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Grade: G7-11 (Kimyo)

## Output

4-6 boss questions with HP damage tags. Mix of difficulty tiers.

---

## HP and Damage

| Grade | HP |
|-------|:--:|
| G7-9 (Kimyo) | **100** |
| G10-11 (Kimyo) | **150** |

| Difficulty | Damage | Distribution |
|-----------|:------:|:----------:|
| Easy | -10 HP | 40% |
| Medium | -20 HP | 40% |
| Hard | -30 HP | 20% |

For 5 questions (G7-9): 2 Easy + 2 Medium + 1 Hard.
For 5 questions (G10-11): 2 Easy + 2 Medium + 1 Hard (harder stoichiometry, multi-step Periodic Table reasoning).

---

## Question Construction

Every question tagged: `[Damage: -XX HP]`

**Must include:**
- ≥1 three-scale reasoning question (student describes a substance or reaction at all three scales: macroscopic observable → microscopic particle model → symbolic formula or balanced equation)
- ≥1 equation balancing question (student writes and balances a chemical equation, showing atom count verification)
- ≥1 safety scenario question (student identifies the hazard, names the required PPE, and explains why)
- ≥1 real-context calculation or prediction question (stoichiometric problem, or Periodic Table prediction in a professional context)

**Every question involving a substance MUST include a three-scale description or observable diagram in brackets** using the Visual Layer notation standard.

**Three-scale questions show the macroscopic description (State A) only** — the student supplies the microscopic description and the symbolic formula from what they observe. Never show all three scales at once in the question.

**Equation balancing questions show the unbalanced equation (orange) and require:**
1. Student writes the balanced equation with correct coefficients
2. Student shows atom count verification: "element×N = element×N ✓" for every element

**MC restriction:**
- G7-11: **NO MC.** All open-ended with written reasoning steps.

**Difficulty scaling:**
- Easy (-10): single-step — name a substance from its observable properties, state a safety rule, or identify a reaction type
- Medium (-20): 2-3 steps — three-scale description of one substance, OR balance a simple equation and verify
- Hard (-30): multi-step with context — observe a substance, reason at all three scales, write and balance the equation, solve a stoichiometric calculation, and interpret the result in a professional context

---

## Example (§8 — Kislota va asoslar)

> **Q1** [Damage: -10 HP]
> `[Observable: rangsiz suyuqlik, o'tkir hidli, ko'k lakmusni qiziltiradi, temir bilan reaksiyaga kirishganda pufakchalar hosil bo'ladi]`
> Bu modda qaysi kimyoviy sinfga kiradi? Kuzatuvdan qanday xulosa chiqardingiz? Ehtimoliy bir formulani yozing.

> **Q2** [Damage: -10 HP]
> `[Diagram: student pouring liquid from unlabeled bottle without goggles; fume visible above bottle (red warning)]`
> Bu lab holatida qaysi xatolar bor? Har bir xatoni aniqlang va to'g'ri protsedura nima bo'lishi kerakligini tushuntiring.

> **Q3** [Damage: -20 HP]
> `[Observable: oq kristall kukun, hidsiz, suvda eriydi, qizil lakmusni ko'k qiladi]`
> Bu moddani uch darajada tasvirlang: makroskopik (berilgan), mikroskopik (Siz yozing), ramziy (Siz yozing). Moddani aniqlang va formulasini yozing.

> **Q4** [Damage: -20 HP]
> Quyidagi reaksiyani muvozanatlang va atom sonlarini tekshiring:
> `? Al + ? O₂ → ? Al₂O₃`
> Reaksiya turini aniqlang. Bu reaksiyaning makroskopik belgisini tasvirlang (nima ko'rinadi?).

> **Q5** [Damage: -30 HP]
> `[Safety: konsentrlangan NaOH — kuydirgich. Goggles + gloves majburiy. [Diagram: safety PPE labeled orange]]`
> Siz Navoiy kimyo kombinatining nazorat laboratoriyasida ishlaysiz. 80 g NaOH bilan qancha HCl reaksiyaga kirishadi?
> Reaksiya: NaOH + HCl → NaCl + H₂O
> 1. Reaksiyani muvozanatlang. 2. NaOH ning molar massasini hisoblang. 3. Necha mol NaOH bor? 4. Necha mol HCl kerak? 5. Bu natija sanoat jarayoni uchun nima anglatadi?

---

## Hint Ladder — Three-Scale Progressive Reveal

Hints in the Final Challenge are delivered as progressive scale reveals, not as text clues. Each hint adds one level to the three-scale description:

- **Hint 1 — -5 HP:** Reveal additional macroscopic detail — one more observable property added (e.g., "Bu modda metallarni ham eritadi"). No microscopic or symbolic information. Student reads the new observable and refines their identification.
- **Hint 2 — -5 HP:** Reveal the microscopic description — particle type and arrangement described (e.g., "H⁺ va Cl⁻ ionlari suvda"). Student must now write the symbolic formula.
- **Hint 3 — -5 HP:** Reveal the unbalanced equation framework — substance names or partial formula shown, coefficients still blank (orange "?"). Student must supply the correct coefficients and verify.

**Never give a text-only hint for a chemistry question.** The hint IS the next scale revealed. Moving from observation to microscopic model to symbolic formula is the core skill — the hints reinforce this direction.

Example hint sequence for a three-scale question:
> Hint 1: `[Observable update: rangsiz suyuqlik — litmus qizaradi, temir bilan H₂ gazi chiqadi, YONMAYDI]` — "Yana qanday kuzatuvlar bor? Fikringiz o'zgaradimi?"
> Hint 2: `[Micro: H⁺ va SO₄²⁻ ionlari suvda]` — "Mikroskopik darajada ionlar aniqlandi. Formulani yozing."
> Hint 3: `[Partial symbolic: H? SO? — coefficients blank (orange)]` — "Formula tuzilishi ko'rsatildi. Valentlikdan foydalanib to'ldiring."

## Failure Response

Wrong answer → "Hali emas!" (never "Noto'g'ri")
Show WHY the correct answer is correct with the three-scale description filled in and the balanced equation verified. Route back to the relevant Preview panel.

---

## Rules

- 4-6 questions, distribution 40/40/20 (easy/medium/hard)
- All questions from THIS chapter's content only
- Every question tagged with Damage
- G7-11: no MC — all open-ended, all require written reasoning
- Every substance question includes a macroscopic observable description in brackets
- Three-scale questions show macroscopic only — student supplies micro and symbolic
- Equation balancing questions require atom count verification explicitly
- Safety scenario question mandatory — PPE identification + hazard explanation
- Balanced equations in model answers must be verified — equal atom counts
- Hints are three-scale progressive reveals — never text-only clues
- Hints cost HP, not free
- HP: G7-9 = 100, G10-11 = 150
- Language: Uzbek, "Siz" formal


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
