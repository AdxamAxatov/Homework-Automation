# Prompt: Classify Lesson Difficulty — Biology

You are classifying a Biology textbook page as **EASY** or **HARD**. You only see this one page — no context about previous or next lessons.

## Input

- Textbook page (image or text)
- Grade: G5-11 (Biologiya)

## Output

One word: `EASY` or `HARD`. Then one sentence explaining why.

## Classification — Two Steps

### Step 1: Is the topic inherently complex?

A topic is inherently complex if understanding it requires chaining multiple biological concepts, involves multi-step mechanisms or cycles, or is abstract/systemic by nature.

Examples of inherently complex topics (always HARD):
- Cell division: mitosis, meiosis (stage sequences, chromosomal changes)
- Genetics and inheritance (Mendelian ratios, dominant/recessive, Punnett squares)
- Photosynthesis and cellular respiration (light reactions, Calvin cycle, ATP synthesis, electron transport)
- Nervous system function (action potential, synapse transmission, reflex arcs)
- Evolution and natural selection (variation, selection pressure, speciation, Hardy-Weinberg)
- Ecological cycles: carbon cycle, nitrogen cycle, water cycle (multi-actor flows)
- Hormonal regulation and feedback loops (endocrine system, negative feedback)
- Immune response (antigen-antibody cascade, T-cell/B-cell activation)
- DNA replication, transcription, translation (molecular mechanism, codon-anticodon)
- Any topic requiring ≥2 prior biological concepts to understand

If YES → output **HARD**. Stop here.

### Step 2: Does the page teach a process, mechanism, or experiment?

**HARD signals** (any one = HARD):
- A named biological process with numbered or sequential steps (e.g., stages of mitosis, steps of digestion)
- A cycle diagram showing inputs, outputs, and transformations
- A laboratory experiment or scientific method described (hypothesis, procedure, observation)
- "Jarayon" / "mexanizm" / "bosqich" / "tajriba" / "sikl" / "reaksiya" in headings
- Cause-and-effect chains (e.g., hormone triggers → organ response → feedback)
- Comparison of two processes that must be understood together (e.g., aerobic vs. anaerobic)
- Diagram requiring interpretation of functional relationships (food web, organ system, life cycle)

**EASY signals** (all must be true):
- Only naming and describing organisms, organs, or structures
- Taxonomy and classification (kingdom/phylum/class/order — just the labels)
- Morphological descriptions (what it looks like, where it lives)
- Historical introduction to a field or scientist
- Observation-based content with no mechanism required
- No sequential process, no cycle, no experimental procedure on the page

**If mixed** — any HARD signal present → **HARD**.

## Examples

| Page content | Classification | Reason |
|-------------|:-:|--------|
| "Zamburug'lar — eukariot organizmlar. Hujayra devori xitindan tashkil topgan" | EASY | Morphological description only |
| "Mitoz bo'linishning bosqichlari: profaza, metafaza, anafaza, telofaza" | HARD | Multi-step sequential process |
| "O'simliklarning asosiy organlari: ildiz, poya, barg, gul, meva" | EASY | Naming/taxonomy only |
| "Fotosintez: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂" + light/dark reactions | HARD | Multi-step biochemical mechanism |
| "Mendel qonunlari — dominant va retsessiv belgilar" + Punnett squares | HARD | Inherently complex (genetics/inheritance) |
| "Qushlarning sinflarga bo'linishi va tashqi tuzilishi" | EASY | Classification + morphology only |
| "Ovqat hazm qilish: og'iz bo'shlig'idan to ingichka ichakgacha" + enzymes | HARD | Sequential process with mechanism |
| "Ekosistemadagi oziq zanjiri: o'simlik → o'tchi → yirtqich" | EASY | Simple taxonomy of relationships, no cycle |
| "Azot aylanishi — bakteriyalar, o'simliklar, hayvonlar, atmosfera" | HARD | Inherently complex (ecological cycle) |
| "Hujayra nazariyasi tarixi — Guk, Shleyden, Shvann" | EASY | Historical introduction, no mechanism |


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "mode": "easy|hard",
  "level": "string",
  "reason": "string"
}
```
