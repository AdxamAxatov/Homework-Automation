# Prompt: Consolidation — Kimyo (Hard only, conditional)

You are building the Consolidation phase (Phase 5) for a Kimyo Hard mode session. This phase fires ONLY when the lesson teaches 2 or more distinct interlocking chemical concepts, reaction types, or substance classes. If the lesson covers a single concept, skip this phase entirely.

Purpose: lock the substances, reactions, and three-scale reasoning into long-term memory using a mnemonic technique before the Final Challenge.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Grade: G7-11 (Kimyo)

## Decision: Build or Skip?

- Lesson has 2+ distinct substances, reaction types, or three-scale concepts that connect → **BUILD**
- Lesson covers 1 substance or 1 observable property → **SKIP** (output: "Consolidation skipped — single concept lesson")

Examples:
- "Kislotalar, asoslar va tuzlar" → 3 substance classes → BUILD
- "Neytrallash reaksiyasi + ion almashinuvi" → 2 reaction concepts → BUILD
- "Kislorod va vodorodning xossalari" → 2 substances → BUILD
- "Natriy xloridning xossalari" → 1 substance → SKIP

## Output (if building)

One mnemonic exercise, ~3 minutes.

---

## Pick a technique based on content structure

| Content structure | Technique | How to build |
|-------------------|-----------|-------------|
| **Hierarchical** (substance class families, reaction type taxonomy) | **Radiant Summary** | Center = main concept (e.g., "Kimyoviy reaksiya turlari"). 3-5 branches = sub-types (qo'shilish, parchalanish, almashinish, neytrallash). Each branch: reaction name + balanced example equation + observable sign. Student fills in missing branches. |
| **Discrete substances** (2-4 compounds to remember) | **Peg System** | Each substance paired with its most distinctive observable property as a vivid image — white crystals for salt, fizzing for acid-metal reaction, color change for indicator. Student recalls substance from property and property from substance — in both directions. |
| **Sequential** (steps of an equation balancing procedure or lab protocol) | **Link System** | Steps of the three-scale reasoning arc chained into a story: "I observe the macro → I picture the micro → I write the symbolic → I verify the balance." Each step links to the next through a physical action or observable change. |
| **Spatial / Multi-substance** (several substances studied in same experiment) | **Memory Palace** | Substances placed at locations in a familiar Uzbek lab or building. Student "walks through" the lab bench and at each station recalls: macro properties, micro structure, symbolic formula, safety precaution. |

Pick ONE technique. Keep it to 3 minutes — this is a quick lock, not a deep exercise.

---

## After the mnemonic (mandatory)

Show 3-4 observable descriptions — student identifies the substance or reaction at all three scales. 45 seconds.

> "Moddalar galereyasi — har bir kuzatuvga asoslanib, moddani uch darajada aniqlang."
> `[Observable description 1: ...]` → substance name + formula + micro description
> `[Observable description 2: ...]` → substance name + formula + micro description
> `[Observable description 3: ...]` → reaction name + balanced equation

Every observable description shown as a macroscopic lab description in brackets — what you see, smell, or measure. Student must supply all three scales: macro (already given) → micro → symbolic.

Minimum requirement for each answer: substance or reaction name + formula or balanced equation + one-line microscopic description.

---

## Rules

- Only fires when 2+ distinct substances, reaction types, or three-scale concepts in the lesson
- One technique only
- ~3 minutes max
- Every substance referenced as a three-scale description — macro + micro + symbolic
- Safety note for hazardous substances in the mnemonic — even in a memory exercise, safety is not dropped
- Language: Uzbek, "Siz" formal
- No scoring — this is a calm moment before the Final Challenge
- "Moddalar galereyasi" section is mandatory — student identifies substance at all three scales from observable description alone


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
