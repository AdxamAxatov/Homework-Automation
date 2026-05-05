# Prompt: Consolidation — Biology (Hard only, conditional)

You are building the Consolidation phase for a Biology Hard mode session. Fires ONLY when the lesson teaches 2+ distinct interlocking biological concepts. Single-concept lessons skip this phase entirely.

Purpose: lock interlocking concepts into long-term memory before the Final Challenge using Buzan mnemonic techniques.

## Input

- Textbook page + all previous phase outputs
- Grade: G5-11 (Biologiya)

## Decision: Build or Skip?

- 2+ concepts that connect and interlock → **BUILD**
- 1 concept → **SKIP** (output: "Consolidation skipped — single concept lesson")

Examples:
- "Fotosintez + Nafas olish" → 2 interlocking processes → BUILD
- "Genetika + Evolyutsiya" → 2 connected fields → BUILD
- "Hujayra bo'linishi (mitoz) + Meyoz" → 2 interlocking mechanisms → BUILD
- "Oziq zanjiri + Ekosistema muvozanati" → 2 connected concepts → BUILD
- "Hujayra membranasi tuzilishi" → 1 concept → SKIP

## Output (if building)

One mnemonic exercise, ~3 minutes.

| Content structure | Technique | Biology example |
|-------------------|-----------|----------------|
| **Hierarchical** (classification trees, organism taxonomy, organ systems) | **Radiant Summary** | Center: "Qon aylanish tizimi" → branches: Yurak / Arteriyalar / Venalar / Kapillyarlar |
| **Sequential** (process steps, metabolic pathways, reaction chains) | **Link System** | Fotosintez bosqichlari → har bir qadam oldingi qadamga bog'liq hikoya sifatida |
| **Spatial** (organ locations, ecosystem layers, cell compartments) | **Memory Palace** | Tananing bo'limlari = tanish xonadagi joylar; ekosistema qatlamlari = uy qavatlar |
| **Discrete items** (organism names, biological terms, classification groups) | **Peg System** | Har bir atama jonli, g'alati tasvir bilan juftlashtirilgan |

Pick ONE technique based on the lesson's content structure. ~3 minutes max.

### Technique selection logic

- Is the content a tree or branching classification? → **Radiant Summary**
- Is the content a chain of steps or a cycle (e.g., Krebs, photosynthesis light reactions)? → **Link System**
- Does it involve WHERE things are located (organs, layers, zones)? → **Memory Palace**
- Is it a list of names or terms to memorize (species, phyla, vocabulary)? → **Peg System**

## Rules

- Only fires when 2+ interlocking concepts
- One technique only — never mix two techniques in one exercise
- ~3 minutes
- Language: Uzbek, "Siz" formal
- No scoring
- Log the decision: state which technique was chosen and why (1 sentence reasoning)


---

## OUTPUT REQUIREMENT
Return valid JSON matching this exact schema:
```json
{
  "mnemonic": "string",
  "lock_code": "string",
  "explanation": "string"
}
```
