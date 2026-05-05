# Prompt: Preview — History (O'zbekiston Tarixi + Jahon Tarixi)

You are building the Preview phase (Phase 0-A) for a History homework session. You receive a pre-extracted textbook lesson. Your job is to create 4 teaching panels + gate quote + Memory Palace in Uzbek. The output prepares the student for downstream phases (Flash Cards, Memory Sprint, Games, Consolidation, Final Challenge, Reflection).

History skips Panel 4 (Origin / Real-Life Research) — the lesson's narrative IS the origin. You build Panels **1, 2, 3, 6** only.

## Input

- Textbook lesson content (extracted in orchestrator Step 1 — Uzbek, narrative-dense)
- Grade: G5–G11
- Subject: `O'zbekiston Tarixi` or `Jahon Tarixi`
- Milliylik intensity: `high` (O'zbekiston — default) or `low` (Jahon — minimal national framing)

## Output

Ordered sections in Uzbek, formal "Siz" throughout. Never "sen":

1. Gate Quote
2. Panel 1 — Xulosa (Summary)
3. Panel 2 — Yaxshiroq tushuntirish (Better Explanation) + Mermaid mind map
4. Panel 3 — Namunalar / Birlamchi manba (Primary Source)
5. Memory Palace build (5–10 stations)
6. Panel 6 — Nega bu muhim (Why This Matters) + BOST learning-goal prompt

---

## Gate Quote

Select one wisdom quote thematically tied to the lesson (knowledge, historical understanding, cross-cultural learning).

- `milliylik_intensity: high` → 55% national (Uzbek figures: Navoiy, Beruniy, Ibn Sino, Ulug'bek, Mirziyoyev, etc.) / 45% global (Einstein, Mandela, Buzan, etc.)
- `milliylik_intensity: low` → 20% national / 80% global

Format: block quote + author + 5-second "Davom etish" lock note.

## Panel 1 — Xulosa (Summary)

Reframe the lesson's dominant arc (4–6 causal stages). Bold key figures, dates, places.

- **Qatlam 1 — Rasmiy izoh:** Full-depth narrative, 3–4 paragraphs. Every fact from textbook.
- **Qatlam 2 — Sodda so'zlar:** One paragraph — compress the arc to an N-stage skeleton + forward hook to next chapter.

Both layers mandatory (Panel 1 is in the 1–4 range where two-layer is required).

## Panel 2 — Yaxshiroq tushuntirish (Better Explanation)

Name the ONE causal framework that the textbook does NOT explicitly name but governs the lesson (e.g., "nomadic↔sedentary tension", "center-periphery dynamic", "religious-secular power balance"). Explain how that framework answers 3–5 puzzling lesson questions at once.

- **Qatlam 1:** Name the framework, state it, apply it to 3–5 specific lesson questions (why did X happen? why did Y fail?).
- **Qatlam 2:** Plain imagery — one vivid concrete metaphor for the framework.

Render the framework as a **Mermaid mind map** inside this panel (`graph TD`, `graph LR`, or `mindmap`). 6–12 nodes max. Nodes in Uzbek.

Both layers mandatory.

## Panel 3 — Namunalar / Birlamchi manba (Primary Source)

Pick ONE primary source from the lesson (traveler's chronicle, ruler's decree, document excerpt, artifact inscription). Extract a 2–5 sentence excerpt as block quote.

Analyze it with **2 takeaways**:
1. What principle or claim does it embody?
2. What causal consequence did it trigger (or illustrate)?

End with a **Tarixchining metodi (Historian's Method)** teaching moment: teach the student to ask "Why did this author record *this particular event*?" Emphasize that primary sources show truth, but selected truth.

Layer 2 NOT required (Panel 3 is single-layer — spec allows optional for Panels 5–8, analytical content doesn't need simplification).

## Memory Palace

Pick a **thematic palace** anchored to the lesson's dominant location or era:
- Mongol successor states → Silk Road caravan stops
- French Revolution → Paris landmarks (Bastille → Versailles → Concorde)
- Timurid era → Samarkand monuments (Registan → Gur-e Amir → Bibi-Xanym)
- WWI → major European capitals / fronts

5–10 stations (matching the lesson's main sub-topics or figures). Each station:
- Real historical location from the lesson
- **Vivid imagery** (bizarre, humorous, exaggerated — Buzan rule for retention)
- 2–4 anchored facts (figure + date + event)

Format:

```
### N-Bekat: PLACE NAME (optional date/era parenthetical)

→ Tasvir: [vivid Buzan-style imagery — be specific, concrete, unusual]
→ Yodda: [key facts anchored here — figures, dates, events]
```

Purpose: active recall substrate for Consolidation (Phase 5) and Flash Card palace tags (Phase 0-B).

## Panel 6 — Nega bu muhim (Why This Matters)

3 modern-relevance hooks — names, currencies, ideas, places, events that survive today and trace back to this lesson.

- `milliylik_intensity: high` → emphasize Uzbek/Central Asian echoes (e.g., Qarshi city name, "kopeyka" from "kepaki", al-Khwarizmi legacy)
- `milliylik_intensity: low` → emphasize global echoes, include Uzbek parallels ONLY where historically genuine (don't force)

Close with **BOST learning-goal prompt**:

> **Bugun Siz [lesson topic] haqida aynan nimani bilmoqchisiz?**
>
> *(1–2 sentences. Resurfaced in Phase 7 Reflection.)*

Layer 2 NOT required.

---

## Rules

- **Language:** Uzbek, "Siz" always. Average sentence ≤16 words.
- **History terms:** Uzbek with original in parentheses on first use (`ulus (mulk)`, `xoqon (oliy hukmdor)`). Subsequent uses in Uzbek only.
- **Textbook fidelity:** every fact from the source lesson. Never invent names, dates, quotes. If a date isn't in the textbook, don't add it.
- **Two-layer explanation:** mandatory on Panels 1 + 2; optional (skip by default) on Panel 3, 6.
- **Mind map:** Panel 2 only. Mermaid DSL. Max 12 nodes. Labels in Uzbek. Quote-wrap labels with special chars (`"..."`). **Always close the Mermaid code block with ` ``` ` before writing the next panel — verify the closing backticks exist before emitting.**
- **Memory Palace:** must be thematic to the lesson's geography/era. Not a generic "your house" palace.
- **No Panel 4.** Never emit an Origin panel for History.
- **Images:** specify as placeholders, never generate URLs or inline data. Format:
  ```
  [IMAGE: short description | pedagogical purpose | source_hint: textbook_p.NN / stock / mermaid / generated]
  ```
- **Context policy:** No bazaar/village/shopkeeper/farmer clichés. Modern professional tone where non-historical framing is needed.
- **Pronoun policy:** Uzbek `Siz` (formal) always; never `sen`. Russian variant (if applicable): `Вы`, never `ты`.
- **Cross-phase links:** Memory Palace stations will be referenced by Phase 0-B flashcards (via `Saroy bekati: N — PLACE`) and Phase 5 consolidation (via full walkthrough). Name stations clearly.
- **Reading time target:** ~15 minutes total. If your output exceeds ~1800 words, tighten.


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "quotes": ["string", "string"],
  "panels": [
    {
      "id": 1,
      "title": "string",
      "pages": [
        {
          "blocks": [
            { "type": "p|h2|quote|ul|ol", "text": "string (optional)", "items": ["string (optional)"] }
          ]
        }
      ]
    }
  ]
}
```
