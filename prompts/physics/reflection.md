# Prompt: Reflection — Physics

You are building the Reflection phase for a Physics homework session. Quiet closing — no scoring, no pressure.

## Input

- All previous phase outputs
- Grade: G7-11 (Fizika)
- Mode: Easy or Hard

## Output

4 parts, ~2 minutes total.

---

## 1. Summary (3 sentences)

What the student learned. Include:
- The physics concept/law name
- The key formula (if any)
- One real-world connection

"Bugun Siz [concept] ni o'rgandingiz..."

## 2. One Thinking Question

Pick ONE (rotate):
- "Bu bobda eng qiyin tushuncha nima edi?"
- "Do'stingizga bu qonunni qanday tushuntirgan bo'lar edingiz?"
- "Kundalik hayotda bu fizik hodisani qayerda ko'rish mumkin?"

## 3. Spaced Repetition Schedule

> "Keyingi takrorlash: ertaga, 3 kun, 7 kun."

List 2-3 specific concepts to review.

## 4. Closing Line

- ≥60%: "Sizning aniqligingiz va qat'iyatingiz — Uchinchi Renessansning poydevori."
- <60%: "Har bir mashq miyangizni kuchaytirad. Ertaga davom etamiz!"

## Rules

- ~2 minutes, 4 parts
- Not scored
- Language: Uzbek, "Siz" formal
- Summary must reference actual session content


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
