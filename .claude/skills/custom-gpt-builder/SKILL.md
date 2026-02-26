---
name: custom-gpt-builder
description: Build custom GPTs with comprehensive instructions and knowledge files. USE WHEN user says 'build a custom GPT', 'create a custom GPT', 'make a GPT for', 'new custom GPT', 'GPT for my students', 'build a bot for', 'create a chatbot for', 'custom GPT instructions'.
---

# Custom GPT Builder

Takes the user's idea for a custom GPT and guides them through building it — from clarifying the purpose to producing ready-to-paste instructions, knowledge files, name, description, and conversation starters.

---

## Workflow

This is a sequential 4-phase process. Always go through all phases in order.

| Phase | What Happens | Workflow |
|-------|-------------|----------|
| 1. Understand | Read reference materials, ask clarifying questions | `workflows/phase-1-understand.md` |
| 2. Instructions | Write GPT instructions (under 8,000 chars) | `workflows/phase-2-instructions.md` |
| 3. Knowledge | Determine and create knowledge files | `workflows/phase-3-knowledge.md` |
| 4. Packaging | Name, description, conversation starters | `workflows/phase-4-packaging.md` |

---

## When to Use

- User says "build a custom GPT"
- User says "create a custom GPT for [purpose]"
- User says "make a GPT for my students"
- User says "I need a chatbot that does [thing]"
- User says "custom GPT instructions"
- User wants to build any ChatGPT custom GPT

---

## Output

**Location:** `custom-gpts/[gpt-name]/`

Files produced:
- `GPT-Instructions.md` — Final instructions (under 8,000 characters)
- Knowledge files as needed (synthesized patterns, frameworks, etc.)
- `README.md` — Name, description, conversation starters, knowledge file list, setup notes

---

## Universal Rules for ALL Custom GPTs

These rules apply to every custom GPT we build, unless the user explicitly overrides them:

### 1. Voice
- The GPT speaks TO the user in the voice of Artem from Full-Time Editor (reference Voice of Artem knowledge file)
- The GPT crafts OUTPUTS (messages, content, etc.) in the USER's voice — not Artem's
- This distinction is critical: Artem's voice = how the GPT communicates. User's voice = what the GPT produces.

### 2. Scope Boundaries
- Every GPT must have a clearly defined area of expertise
- If the user asks something outside its scope, the GPT declines: "That's outside of what I can help with, dude. I'm here to help you with [specific purpose]."
- Never let the GPT wander into topics it wasn't built for

### 3. Context Collection
- Every GPT must collect context from the user BEFORE producing output
- Ask ONE question at a time — never send a list of questions
- The GPT should ask for as much context as it needs to produce good output

### 4. Output Quality
- Never sound AI-generated (no em dashes, no corporate speak, no overly polished language)
- Keep outputs human and conversational
- Never include copy-paste templates — always synthesize fresh output based on patterns and principles

### 5. Built for FTE Students
- Default audience is Artem's Full-Time Editor students (video editors)
- Unless explicitly specified for another audience

### 6. No Coaching
- The GPT helps the user DO the thing, not learn about the thing
- Don't critique, review, or coach — just produce the output they asked for

---

## Key Principles

### Synthesize, Don't Template
When reference materials contain examples (coaching call transcripts, sample messages, etc.), NEVER include them as copy-paste examples. The GPT will regurgitate them verbatim. Instead:
1. Extract the PATTERNS across multiple examples
2. Capture the THINKING PROCESS behind each pattern (the "why")
3. Write the pattern as structure + thinking, so the GPT generates fresh output every time

### 8,000 Character Limit
ChatGPT instructions have an 8,000 character limit. Strategy:
- Instructions contain: identity, scope, behavior rules, process flow, principles, don'ts, references to knowledge files
- Knowledge files contain: detailed patterns, frameworks, step-by-step processes, deep reference material
- Instructions tell the GPT WHAT to do; knowledge files give it the depth to do it WELL

### The Right Level of Detail
- Instructions should be specific enough that the GPT knows exactly how to behave
- But not so detailed that they become a manual the GPT ignores
- Put behavior rules in instructions, put reference depth in knowledge files
