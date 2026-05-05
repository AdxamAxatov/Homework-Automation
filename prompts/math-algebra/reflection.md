# Prompt: Reflection — Math + Algebra

You are building the Reflection phase (final phase) for a Math/Algebra homework session. This is a quiet closing — no scoring, no pressure. Summarize what was learned, ask one thinking question, set up next review.

## Input

- All previous phase outputs
- Grade: G5-6 (Matematika) or G7-9 (Algebra)
- Mode: Easy or Hard

## Output

4 parts, ~2 minutes total.

---

## 1. Summary (3 sentences)

What the student learned today. Include:
- The concept name
- The key formula or method
- One real-world connection

Write as: "Bugun Siz [concept] ni o'rgandingiz..."

Example:
> Bugun Siz sonlarni o'nlik va yuzliklarga ko'paytirishni o'rgandingiz. Asosiy usul: katta sonni qulay bo'laklarga ajratib, bosqichma-bosqich ko'paytirish. Bu usul muhandislar va logistlar har kuni ishlatadigan tez hisob usuli.

## 2. One Thinking Question

Pick ONE from these (rotate across sessions):
- "Bu bobda eng qiyin qismi nima edi?"
- "Do'stingizga qanday tushuntirgan bo'lar edingiz?"
- "Kundalik hayotda qayerda ishlatishingiz mumkin?"

Student answers freely. Not scored.

## 3. Spaced Repetition Schedule

> "Keyingi takrorlash: ertaga (1 kun), 3 kundan keyin, 7 kundan keyin."

List 2-3 specific concepts from this session that the student should review — based on what appeared in the homework.

## 4. Closing Line

- Score ≥60%: "Sizning aniqligingiz va qat'iyatingiz — Uchinchi Renessansning poydevori."
- Score <60%: "Har bir mashq miyangizni kuchaytirad. Ertaga davom etamiz!"

Never punitive. Never "you failed."

---

## Rules

- ~2 minutes, 4 parts
- Not scored
- Language: Uzbek, "Siz" formal
- Summary must reference actual content from this session, not generic


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
