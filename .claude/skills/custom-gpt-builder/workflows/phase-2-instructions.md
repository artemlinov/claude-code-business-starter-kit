# Phase 2: Write Instructions

## Purpose
Write the GPT's instructions — the core behavior document that goes into ChatGPT's "Instructions" field. Must be under 8,000 characters.

---

## Strategy: Instructions vs Knowledge Files

**Instructions (8,000 char limit)** contain:
- Identity (who the GPT is, voice, audience)
- Scope (what it does / doesn't do)
- How it works (process rules, behavior)
- Use cases (condensed — what to do, context to collect, steps)
- Principles (rules for all outputs)
- Don'ts (explicit list of things to avoid)
- References to knowledge files ("see [Knowledge File Name] for detailed patterns")

**Knowledge files** contain:
- Detailed patterns with structure + thinking
- Step-by-step frameworks with explanations
- Deep reference material (voice guides, theory docs, etc.)
- Anything that adds depth but isn't a behavior rule

**Rule of thumb:** If removing it would change HOW the GPT behaves, it's an instruction. If removing it would reduce the DEPTH of its output, it's a knowledge file.

---

## Step 1: Write Full Draft (No Character Limit)

First, write comprehensive instructions without worrying about length. Cover everything:

### Sections to Include

**Identity**
- What the GPT is and does (1-2 sentences)
- Voice: "You speak TO the user in the voice of Artem from Full-Time Editor (see Voice of Artem knowledge file)"
- Output voice: "The [outputs] you CRAFT are in the USER's voice — not Artem's. They should sound like the user naturally wrote them."

**Scope**
- "You DO:" — list of specific things it handles
- "You DO NOT:" — list of things it explicitly declines
- Out-of-scope response: "That's outside of what I can help with, dude. I'm here to help you with [specific purpose]."

**How You Work**
- Context collection rules (one question at a time)
- Step-by-step process (if applicable)
- Output format (output + strategy explanation, or just output)
- Price/specificity rules (placeholders vs. specific suggestions)
- Knowledge file references

**Use Cases (one section per use case)**
For each use case:
- Context to collect (list the questions, specify one at a time)
- Process steps (numbered, clear)
- Any patterns to reference from knowledge files

**Principles**
- Universal rules that apply to ALL outputs
- Quality standards
- What makes output good vs. bad

**Don'ts**
- Explicit list of things the GPT must never do
- Common failure modes to prevent

---

## Step 2: Synthesize Patterns from Reference Materials

If the user provided reference materials with examples (coaching calls, sample outputs, etc.):

### The Synthesis Process

1. **Read all examples** — Don't just skim. Understand each one deeply.

2. **Extract patterns** — What approaches repeat across examples? Group them.
   - Example: "In 3 out of 6 coaching calls, the raise was framed around a life change"
   - Example: "Every successful message led with what the client gets, not what the editor wants"

3. **Name the patterns** — Give each pattern a clear name.
   - Example: "The Life Change Frame," "The Options Technique," "The Accountability + Raise"

4. **Capture the structure** — For each pattern, document:
   - When to use it (the trigger/situation)
   - The structure (numbered steps)
   - The thinking behind it (WHY this works — use the user's actual explanations from coaching calls, not generic advice)

5. **Write it as guidance, not templates** — The GPT should understand the PATTERN well enough to generate fresh output every time. Never include actual message text that could be copied.

### What "Thinking Behind It" Looks Like

BAD (generic):
"This approach works because it builds trust."

GOOD (specific, from actual coaching reasoning):
"When an editor frames a raise around a genuine life change, it humanizes the ask. The client isn't hearing 'I want more money' — they're hearing 'my life is changing and here's how I'm adapting.' The key is pairing honesty about your situation with genuine excitement about THEIR goals. This turns an awkward conversation into a moment of connection."

The thinking should sound like it came from someone who has actually coached people through this — because it did.

---

## Step 3: Check Character Count

Run: `wc -c [file]` to count characters.

**If under 8,000:** You're done. This is your final instructions file.

**If over 8,000:** Split into instructions + knowledge files:

1. Keep in instructions: Identity, Scope, How You Work, Don'ts, Use Cases (condensed to just context questions + step names + references to knowledge files)
2. Move to knowledge file(s): Detailed patterns with structure + thinking, step-by-step frameworks with explanations, principles with examples

3. Add references in instructions: "See [Knowledge File Name] for detailed patterns on [topic]"

4. Re-check character count. Repeat until under 8,000.

---

## Step 4: Verify Instructions Quality

Before moving to Phase 3, verify:

- [ ] Under 8,000 characters
- [ ] Identity section includes both voice directions (GPT's voice + output voice)
- [ ] Scope clearly defines what it does AND doesn't do
- [ ] Out-of-scope response is defined
- [ ] Process rules are clear (context collection, step-by-step, etc.)
- [ ] Every use case has: context to collect + process steps
- [ ] Principles cover all outputs
- [ ] Don'ts list is explicit
- [ ] Knowledge file references are included (if using knowledge files)
- [ ] No copy-paste examples that the GPT would regurgitate
- [ ] No em dashes, no corporate speak in the instructions themselves
- [ ] [YOUR PRICE] or similar placeholders used where appropriate

---

## Output

Save to: `custom-gpts/[gpt-name]/GPT-Instructions.md`

If you had to split, also save knowledge files (see Phase 3).
