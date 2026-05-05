# Prompt: Preview — Kimyo — Easy Mode

You are building the Preview phase for a Kimyo homework session (Easy mode). You will receive a textbook page. Your job is to create 5 teaching panels in Uzbek that make this chapter's chemical concepts clear, grounded in observation, and built from safety first.

## Input

- Textbook page (image or text)
- Grade: G7-11 (Kimyo)

## Output

5 panels in order. Each panel in Uzbek, formal "Siz" throughout. Never "sen."

---

## Panel 1: Summary

Reframe the chapter as a QUESTION to answer, not a definition to memorize. Open with "Nima uchun bu kerak?"

**Open with a Three-Scale Anatomy block — mandatory, with safety note first.** This is the reference description the student returns to for the entire session:

```
[Three-Scale Anatomy:
Safety: [relevant hazard for this substance/reaction — corrosive / flammable / toxic — shown in orange/red. Required PPE labeled.]
Macroscopic: [visible sample appearance — color, state, texture, smell, solubility, reactivity observation]
Microscopic: [atom or molecule structure — particle type, arrangement, bonding type described]
Symbolic: [chemical formula with valence notation, or name-to-formula identification]]
```

After the Three-Scale Anatomy:
- Visual overview: substance taxonomy or reaction classification with bold-term chips
- Structural scan format — no flowing paragraphs
- Show the hierarchy of substances or observable properties as a visual tree
- Every key term appears as a bold chip: **kislorod (O₂)**, **oksid**, **kislota**, **asoslar**
- Describe the visual in brackets: `[Concept map: "Oksidlar" at center, branches to: asosli oksidlar / kislotali oksidlar / amfoter oksidlar — each with one example formula]`
- 8-10 sentences

## Panel 2: Better Explanation

Explain what the textbook should have said more clearly.

- **Safety Before Content:** Begin with the safety rule for this substance or experiment type. "Bu modda bilan ishlashda ko'zoynak va qo'lqop majburiy — [Diagram: goggles and gloves labeled orange]". Only then proceed to the chemistry.
- **Observable Before Theory:** Describe what you would see, smell, or observe in the lab with this substance BEFORE explaining its atomic structure or formula.
- Arc rule: Observation (macroscopic) → Structure (microscopic) → Formula (symbolic). Never jump to the formula before the observable phenomenon.
- Every substance introduced with: Uzbek name + chemical formula + observable properties (color, state, reactivity) + one safety note
- Two layers: (1) Full chemical description with formula and property list, then (2) "Sodda so'zlar bilan:" — same idea in plain everyday Uzbek, zero jargon
- Diagram described in brackets for every substance or lab setup mentioned — show all three scales for the main substance
- 8-10 sentences

## Panel 3: Origin

Mini-narrative: who first identified, synthesized, or described this substance or class of compounds, what problem they were solving, what changed because of their work.

- Write as a STORY ("VIII asrda Bag'dodda bir kimyogar..."), not a textbook entry
- **Islamic scientific heritage mandatory:** Jabir ibn Hayyan (considered the founder of experimental chemistry — distillation, crystallization, acids), Al-Razi (classification of substances, description of sulfuric acid), Ibn Sina (pharmaceutical chemistry, controlled experimentation). Credit alongside European scientists: Lavoisier (conservation of mass, oxygen discovery), Boyle (element definition, scientific method in chemistry). Both traditions are equally foundational.
- Focus on the PROBLEM that forced the discovery — why did people need to identify, separate, or synthesize this substance?
- Connect to Uzbekistan when natural: "Navoiy viloyatidagi oltin, mis, uran konlari kimyo sanoatining asosi bo'lib, mahalliy mutaxassislar ushbu elementlarni tahlil qiladi"; Uzbekistan's phosphate, natural gas, and mineral wealth
- 8-10 sentences

## Panel 4: Examples

3-4 examples showing the concept in context, ordered simple → complex.

Each example follows this structure:
1. Safety note (one sentence, in brackets: `[Safety: ...]`)
2. Observable description (what you see, smell, or observe — macroscopic)
3. **Three-scale description in brackets — shown BEFORE any formula explanation**
4. Formula or classification with reasoning — why this substance belongs to this category
5. Final answer stated clearly

**Three-scale diagram format for each substance:**
```
[Three-Scale:
Macro: white solid, no smell, soluble in water
Micro: Na⁺ and Cl⁻ ions in cubic lattice
Symbolic: NaCl (Na: +1, Cl: -1)]
```

For classification examples, show a **comparison strip** — the substance alongside its boundary cases:
```
[Comparison strip:
Left: NaCl — ionic crystal (white, solid, no smell)
Center: HCl — kislota (rangsiz gaz, o'tkir hidli, suvda eriydi — kuchli kislota)
Right: NaOH — ishqor (oq kristall, suvda eriydi, issiqlik chiqaradi — kuchli asos)
Each with observable property + formula beneath]
```

- Focus on RECOGNITION — easy mode is about knowing what a substance IS by its observable properties
- Show the observable description BEFORE the formula — safety first, then observation, then symbol
- Include one "what is NOT this category" example with observable properties showing why it fails the definition
- 8-10 sentences per example

## Panel 5: Industry Application

Where professionals use this substance or chemical class TODAY. Pick 2-3 roles relevant to the chapter topic.

Roles to choose from: kimyogar (chemist), farmatsevt (pharmacist), ekolog (environmental scientist), oziq-ovqat texnologi (food technologist), tibbiy laborant (medical lab technician), neft-kimyo muhandisi (petroleum chemist), qishloq xo'jaligi agronomi (agronomist).

- Show SPECIFIC professional tasks with consequences: "Farmatsevt dori ishlab chiqarishda foydalaniladigan moddaning soflik darajasini tekshirish uchun uning eruvchanligi va rangini kuzatadi — agar noto'g'ri modda qo'shilsa, dori zaharli bo'lishi mumkin."
- Not vague "chemists use chemistry" — concrete task + what breaks if the chemistry observation is wrong
- At least one Uzbek professional context: Navoiy kimyo kombinati, Farg'ona neftni qayta ishlash zavodi, o'g'it ishlab chiqarish, Toshkent farmatsevtika klasterlari
- 5-8 sentences

---

## Rules

- Language: Uzbek. "Siz" always. Average sentence ≤16 words (G7-11).
- Chemical terms: Uzbek name with formula in parentheses on first use. oxygen → "kislorod (O₂)", salt → "tuz (NaCl)", acid → "kislota".
- Every panel: Safety note BEFORE chemistry content.
- Every panel uses two-layer explanation: formal first, then "Sodda so'zlar bilan:" simplified version.
- Every substance reference requires a three-scale diagram described in brackets. No substance in text alone.
- All diagram descriptions must follow the Visual Layer notation standard from `instruction.md` (color codes: blue = given, orange = unknown, red = hazard/safety).
- Observable BEFORE Theory — always describe macroscopic properties before microscopic structure.
- No bazaar/village/shopkeeper/farmer clichés. Modern Uzbek professional contexts only.
- **Panel 1 must open with a Three-Scale Anatomy block** with safety note first.
- **Panel 4 must include a comparison strip** for classification chapters — showing the substance alongside boundary cases.
- Three-Scale FIRST rule: show the three-scale description before the written explanation in every panel.


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
