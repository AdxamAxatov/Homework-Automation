# Prompt: Memory Sprint — Kimyo

You are building the Memory Sprint (Phase 1) for a Kimyo homework session. This is a quick warm-up — tap-only, under 2 minutes. The student just finished Preview and Flash Cards. Now you activate what they learned with fast recognition questions.

This is NOT real practice. No equation balancing, no stoichiometric calculations, no lab design. Just: do you recognize the substance, the safety rule, the formula, and the scale?

## Input

- Textbook page (image or text)
- Preview output + Flash Cards output (from previous steps)
- Grade: G7-11 (Kimyo)
- Mode: Easy → **5 items** | Hard → **7 items**

## Output

5 or 7 items. Each item is one of 4 formats. Must use at least 3 different formats.

---

## 4 Formats (ONLY these — nothing else)

### Multiple Choice (MC)
- Question + 4 options. 1 correct, 3 wrong.
- Each wrong option must come from a real student mistake — not random:
  - Confusing substance class (acid vs. salt, oxide vs. hydroxide)
  - Wrong observable property (describing a solid as a gas)
  - Mixing up formula and name (NaOH is base, not acid)
  - Confusing a subscript with a coefficient in a formula
- When a substance or lab setup is involved, reference a diagram: `[Diagram: ...]`

Example:
> `[Diagram: clear liquid turns red litmus paper blue; releases heat when diluted with water]`
> Bu modda qaysi sinfga kiradi?
> A) Ishqor (asos) ✓  B) Kislota  C) Oksid  D) Tuz

### True / False (T/F)
- A statement. Student taps To'g'ri or Noto'g'ri.
- Must test a CHEMICAL LAW, safety rule, or common MISCONCEPTION about formulas or scales — not trivial naming.
- BAD: "NaCl — natriy xlorid — To'g'ri yoki Noto'g'ri?" (trivial name recall)
- GOOD: "Kimyoviy tenglamani muvozanatlashda formuladagi indeksni o'zgartirish mumkin — To'g'ri yoki Noto'g'ri?" (tests balancing rule)
- GOOD: "Kislota bilan ishlashda avvalo kislotani suvga quyish kerak, suvni kislotaga emas — To'g'ri yoki Noto'g'ri?" (tests safety rule)

### Yes / No / Not Given (YNNG)
- Statement about THIS chapter's content. Student taps Ha / Yo'q / Aytilmagan.
- "Aytilmagan" means the chapter doesn't address this claim.
- Include at least 1 item with "Aytilmagan" as correct answer.

Example:
> "Bobda aytilganiga ko'ra, barcha metallar suvda eriydi — Ha / Yo'q / Aytilmagan"

### Safety Check (SC) — Kimyo only
- Show a lab scenario or substance description. Student identifies the correct safety action or the hazard class.
- Used for: recognizing when PPE is required, identifying the correct disposal procedure, spotting an unsafe lab practice, naming the hazard type.
- No typing — student taps one of: "Xavfli — to'xtatib xavfsizlik qoidasini ko'ring" / "Xavfsiz" / "Boshqacha himoya kerak"

Example:
> `[Diagram: student pouring concentrated sulfuric acid (H₂SO₄) without goggles (red warning label on bottle)]`
> Bu lab amalida nima noto'g'ri?
> A) Ko'zoynak kiyilmagan — kuydirgich kislota bilan ishlashda goggles majburiy ✓
> B) Hamma narsa to'g'ri
> C) Faqat qo'lqop kerak
> D) Kislotani suvga emas, suvni kislotaga qo'shish kerak — ham bu xato lekin boshqa xato ✓ (ikkinchi to'g'ri javob)

Example:
> `[Diagram: lab bench with open flame burner next to a bottle labeled "spirt (etanol)"]`
> Bu laboratoriya holatida qaysi xavf mavjud?
> A) Yonuvchan suyuqlik — ochiq olov yaqinida saqlash man etiladi ✓  B) Xavf yo'q  C) Faqat hid bor  D) Etanol zaharli emas

**Safety Check is mandatory: ≥1 SC item per sprint.** Safety awareness must be activated before every chemistry session.

**Scale identification is mandatory: ≥1 item per sprint** that explicitly asks whether a given description is macroscopic, microscopic, or symbolic.

Example scale identification:
> "Na⁺ va Cl⁻ ionlari kub panjarasida joylashgan — bu tavsif qaysi darajada?"
> A) Makroskopik  B) Mikroskopik ✓  C) Ramziy (simvolik)  D) Matematik

---

## Kimyo-specific additions (mandatory)

- Include 1-2 **lab sample identification questions** — reference an observable description or diagram and ask to identify the substance class or the safety hazard
- Every question involving a substance or lab setup MUST reference a diagram using the Visual Layer notation standard
- Wrong answer feedback: show the correct three-scale description with the safety note highlighted — one sentence explaining why

---

## Item distribution

**5 items (Easy):** 2 MC + 1 T/F + 1 YNNG + 1 SC

**7 items (Hard):** 2 MC + 1 T/F + 1 YNNG + 2 SC + 1 MC or T/F

Put the most important safety rule or substance classification as item 1. Safety awareness must be the first thing activated.

---

## Rules

- **Tap only.** No typing, no drag-and-drop, no fill-in-blank, no open-ended.
- **2 minutes max.** Keep items fast — read and tap.
- **Current chapter only.** No items from other chapters.
- **No hints.** No help available in this phase.
- **No equation balancing or stoichiometric calculations.** If answering requires multi-step reasoning, it doesn't belong here.
- **Every substance or lab question references a diagram** described in brackets.
- **Wrong answer feedback:** Show WHY the correct answer is correct in one line with substance description or safety diagram reference.
- Language: Uzbek, "Siz" formal.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
[
  {
    "type": "KO|TF|YNNG",
    "prompt": "string",
    "subtitle": "",
    "tags": "[Bloom: LX | PISA: LX]",
    "explain": "string",
    "options": ["string", "string"],
    "correct": 0
  }
]
```
