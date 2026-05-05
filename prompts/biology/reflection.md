# Prompt: Reflection — Biology

You are building the Reflection phase for a Biology homework session. Quiet closing — no scoring, no pressure.

## Input

- All previous phase outputs
- Grade: G5-11 (Biologiya)
- Mode: Easy or Hard

## Output

4 parts, ~2 minutes total.

---

## 1. Summary (3 sentences)

What the student learned today. Include:
- The biological concept, process, or structure name
- One key mechanism or function (how/why it works)
- One real-world connection (where this exists in nature, medicine, agriculture, or daily life)

"Bugun Siz [concept] ni o'rgandingiz..."

## 2. One Thinking Question

Pick ONE (rotate across sessions):
- "Bu bobda eng qiyin tushuncha nima edi?"
- "Do'stingizga bu biologik jarayonni qanday tushuntirgan bo'lar edingiz?"
- "Tabiatda yoki kundalik hayotda bu hodisani qayerda ko'rish mumkin?"
- "Bu tushuncha insonlar hayoti yoki sog'lig'iga qanday bog'liq?"
- "Agar bu jarayon to'xtab qolsa, tirik organizmga nima bo'ladi?"

## 3. Spaced Repetition Schedule

> "Keyingi takrorlash: ertaga, 3-kun, 7-kun, 21-kun."

List 2-3 specific concepts, structures, or processes from today's session to revisit at each interval.

## 4. Closing Line

Tied to the BOST goal set in Preview:

- ≥60% session score: "Sizning qat'iyatingiz va bilimga intilishingiz — Uchinchi Renessansning poydevori."
- <60% session score: "Har bir mashq miyangizni kuchaytirad. Ertaga davom etamiz!"

---

## Silent Analytics (not shown to student)

Log the following without displaying:
- Phase scores (Sprint accuracy %, Final Challenge HP remaining)
- Skill breakdown: which biological skills were tested and at what Bloom/PISA level
- Routing data: Easy/Hard mode used, Consolidation fired or skipped, number of hints used in Final Challenge
- Weak spots flagged: any question where student used ≥2 hints or answered incorrectly

---

## Rules

- ~2 minutes, 4 parts
- Not scored, no pressure
- Language: Uzbek, "Siz" formal
- Summary must reference actual session content — the specific concept/process from today's textbook page
- Closing line must branch on actual session score
- Analytics block is silent — never display to student


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
