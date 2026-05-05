# Prompt: Consolidation — Physics (Hard only, conditional)

You are building the Consolidation phase for a Physics Hard mode session. Fires ONLY when the lesson teaches 2+ distinct interlocking concepts. Single-concept lessons skip this.

Purpose: lock concepts into long-term memory before the Final Challenge.

## Input

- Textbook page + all previous outputs
- Grade: G7-11 (Fizika)

## Decision: Build or Skip?

- 2+ concepts that connect → **BUILD**
- 1 concept → **SKIP** (output: "Consolidation skipped — single concept lesson")

Examples:
- "Kuch va tezlanish" → 2 connected concepts → BUILD
- "Om qonuni + Kirchhoff qonuni" → 2 laws → BUILD
- "Inersiya tushunchasi" → 1 concept → SKIP

## Output (if building)

One mnemonic exercise, ~3 minutes.

| Content structure | Technique | Physics example |
|-------------------|-----------|----------------|
| **Hierarchical** (types of energy, types of forces) | **Radiant Summary** | Center: "Energiya" → branches: Kinetik / Potensial / Issiqlik / Elektr |
| **Formulas** (2-5 laws to remember) | **Peg System** | Each formula paired with vivid image |
| **Sequential** (experiment steps, process chain) | **Link System** | Steps chained into a story |
| **Spatial** (field lines, circuit layout) | **Memory Palace** | Concepts at locations in a familiar space |

Pick ONE technique. ~3 minutes max.

## Rules

- Only fires when 2+ concepts
- One technique only
- ~3 minutes
- Language: Uzbek, "Siz" formal
- No scoring


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
