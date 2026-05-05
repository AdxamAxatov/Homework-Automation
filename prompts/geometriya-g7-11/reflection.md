# Prompt: Reflection — Geometry

You are building the Reflection phase (final phase) for a Geometry homework session. This is a quiet closing — no scoring, no pressure. Summarize what was learned, ask one thinking question, set up next review.

## Input

- All previous phase outputs
- Grade: G7-9 (Geometriya)
- Mode: Easy or Hard

## Output

4 parts, ~2 minutes total.

---

## 1. Summary (3 sentences)

What the student learned today. Include:
- The theorem or concept name
- The key condition (what is given) and conclusion (what follows)
- One real-world connection where this theorem is used

Write as: "Bugun Siz [theorem/concept] ni o'rgandingiz..."

Example:
> Bugun Siz SAS tenglik belgisini o'rgandingiz. Asosiy qoida: agar ikkita tomon va ular orasidagi burchak teng bo'lsa, uchburchaklar tengdir. Bu belgini me'morlar va muhandislar simmetrik konstruksiyalarni tekshirishda har kuni ishlatadi.

## 2. One Thinking Question

Pick ONE from these (rotate across sessions):
- "Bu bobda eng qiyin qismi nima edi?"
- "Do'stingizga bu teoremani qanday tushuntirgan bo'lar edingiz?"
- "Kundalik hayotda bu teorema qayerda qo'llanilishini ko'rasiz?"
- "Isbotning qaysi qadami sizga eng qiyin tuyuldi va nima uchun?"

Student answers freely. Not scored.

## 3. Spaced Repetition Schedule

> "Keyingi takrorlash: ertaga (1 kun), 3 kundan keyin, 7 kundan keyin."

List 2-3 specific theorems, diagram types, or proof structures from this session that the student should review.

Example:
> Takrorlash:
> - SAS tenglik belgisi — ertaga
> - Tenglik belgilarini diagrammadan aniqlash — 3 kundan keyin
> - Isbotda har bir qadamga sabab ko'rsatish — 7 kundan keyin

## 4. Closing Line

- Score ≥60%: "Sizning mantiqiy fikrlashingiz va aniqligingiz — Uchinchi Renessansning poydevori."
- Score <60%: "Har bir isbot qadami miyangizni kuchaytirad. Ertaga davom etamiz!"

Never punitive. Never "you failed."

---

## Rules

- ~2 minutes, 4 parts
- Not scored
- Language: Uzbek, "Siz" formal
- Summary must reference actual theorem name and conditions from this session — not generic
- Spaced repetition items must be specific theorem names or skill types, not vague topics


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
