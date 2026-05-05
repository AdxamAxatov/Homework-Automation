# Prompt: Reflection — Kimyo

You are building the Reflection phase (final phase) for a Kimyo homework session. This is a quiet closing — no scoring, no pressure. Summarize what was learned, ask one thinking question, set up next review.

## Input

- All previous phase outputs
- Grade: G7-11 (Kimyo)
- Mode: Easy or Hard

## Output

4 parts, ~2 minutes total.

---

## 1. Summary (3 sentences)

What the student learned today. Include:
- The specific substance or reaction type from this session (not generic — use the actual name)
- The key three-scale connection: what you observe (macro) → what is happening at the particle level (micro) → how it is represented symbolically
- One real-world professional connection where this substance or reaction is used

Write as: "Bugun Siz [actual substance/reaction name] ni o'rgandingiz..."

Example:
> Bugun Siz kislota-asos neytrallash reaksiyasini o'rgandingiz. Asosiy uch darajali aloqa: makroskopik darajada indikator rangini o'zgartiradi va issiqlik chiqadi — mikroskopik darajada H⁺ va OH⁻ ionlari birlashib H₂O hosil qiladi — ramziy darajada: HCl + NaOH → NaCl + H₂O (muvozanlashtirilgan). Bu reaksiyadan farmatsevtlar dori ishlab chiqarishda, ekologlar suv muhitini neytrallashtirish ishlarda har kuni foydalanadi.

## 2. One Thinking Question

Pick ONE from these (rotate across sessions):
- "Bu bobda eng qiyin qismi nima edi — kuzatuv, mikroskopik tavsif, yoki muvozanlash?"
- "Do'stingizga bu reaksiyani uch darajada — ko'rish, tasavvur qilish, yozish orqali qanday tushuntirgan bo'lar edingiz?"
- "Agar bu modda mavjud bo'lmaganda, qaysi sanoat jarayoni yoki tibbiy amaliyot qiyin bo'lar edi?"
- "Bugun o'rgangan moddaning xavfsizlik qoidasini qanday esda saqlab qolishingiz mumkin?"

Student answers freely. Not scored.

## 3. Spaced Repetition Schedule

> "Keyingi takrorlash: ertaga (1 kun), 3 kundan keyin, 7 kundan keyin."

List 2-3 specific substances, reaction types, or three-scale reasoning skills from this session that the student should review. Be specific — not "chemistry formulas" but the actual substance name and skill type.

Example:
> Takrorlash:
> - Neytrallash reaksiyasi: HCl + NaOH → NaCl + H₂O — ertaga (atom sonlarini tekshirishni eslab qoling: H×2=H×2, O×1=O×1, ✓)
> - H⁺ va OH⁻ ionlari — mikroskopik darajada aniqlash — 3 kundan keyin
> - Kislota-asos kuzatuvlari → formula: lakmus testi, reaksiya belgisi, microscopic tavsif — 7 kundan keyin

## 4. Closing Line

- Score ≥60%: "Sizning uch darajali kimyoviy fikrlashingiz va xavfsizlikka e'tiboringiz — Uchinchi Renessansning poydevori."
- Score <60%: "Har bir kuzatuv va muvozanlash qadami miyangizni kuchaytirad. Ertaga davom etamiz!"

Never punitive. Never "you failed."

---

## Rules

- ~2 minutes, 4 parts
- Not scored
- Language: Uzbek, "Siz" formal
- Summary must reference the actual substance or reaction name from this session, and include all three scales — not generic
- Spaced repetition items must be specific substance names, reaction types, or scale-translation skills — not vague topics
- Closing line references the student's three-scale reasoning effort and the Third Renaissance — connects individual learning to national aspiration


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "summary": "string",
  "question": "string",
  "spaced_rep": "string",
  "closing": "string"
}
```
