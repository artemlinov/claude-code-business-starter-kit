# Phase 1: Understand the GPT

## Purpose
Deeply understand what the GPT should do before writing a single line of instructions. This is where you gather everything needed to make the instructions comprehensive and the output quality high.

---

## Step 1: Read Reference Materials

Before asking any questions, read EVERYTHING the user points you to:
- Documents, transcripts, examples, frameworks
- Student/client examples (these are gold — they show what good output looks like)
- Any existing knowledge files or brand docs
- Voice files, style guides

Use the Explore agent or read files directly. Be thorough — don't skim. The quality of the GPT depends on how well you understand the source material.

**Important:** When reading example outputs (messages, content, etc.), don't just note WHAT was produced. Note:
- What PATTERN does this follow?
- What THINKING led to this specific approach?
- Why is THIS framing better than alternatives?
- What would a BAD version of this look like?

---

## Step 2: Ask Clarifying Questions

After reading all materials, ask the user clarifying questions. Ask in a batch of 5-7 questions (this is a planning conversation with the user, not the GPT collecting context from its users).

### Questions to Cover

**Scope & Boundaries:**
- What specific use cases should this GPT handle? (rank by popularity)
- What should it explicitly NOT do?
- Should we keep the scope narrow (better output) or broad (more versatile)?

**Behavior:**
- Should the GPT suggest specific numbers/amounts, or use placeholders?
- Should it coach/critique the user, or just produce output?
- Should it explain its strategy/reasoning alongside the output?
- How much context should it demand before producing output?

**Process:**
- Is this a single-step output or a multi-step walkthrough?
- If multi-step: should the GPT walk through one step at a time, waiting for input between steps?
- Should it ask for links/URLs (can the GPT browse)?

**Voice & Tone:**
- Who is the GPT talking to? (FTE students by default)
- Is the output in the user's voice or a specific voice?
- What should the output NOT sound like?

**Edge Cases:**
- What happens when the user asks something borderline?
- What if the user asks the GPT to do something dishonest?
- What are common mistakes users might make that the GPT should handle?

### Handling User Answers

After the user answers:
1. Confirm your understanding of the key decisions
2. If anything is still unclear, ask follow-up questions
3. Share your own recommendations where relevant (e.g., "I'd recommend keeping this narrow because...")
4. Don't start writing instructions until scope and behavior are locked in

---

## Step 3: Map the Use Cases

Before moving to Phase 2, have a clear map:

```
GPT: [Name/Purpose]
├── Use Case 1: [Most popular]
│   ├── Context needed: [what to collect]
│   ├── Process: [single step or multi-step]
│   └── Output: [what it produces]
├── Use Case 2: [Second most popular]
│   ├── Context needed: [what to collect]
│   ├── Process: [single step or multi-step]
│   └── Output: [what it produces]
└── Use Case 3: [etc.]
```

---

## When to Move to Phase 2

Move on when you have:
- [ ] Read all reference materials thoroughly
- [ ] Asked clarifying questions and gotten answers
- [ ] Clear scope boundaries (what it does / doesn't do)
- [ ] Clear behavior rules (coaching vs. producing, placeholders vs. specifics, etc.)
- [ ] Use cases ranked by popularity
- [ ] Understanding of voice distinction (GPT's voice vs. output voice)
- [ ] Understanding of the thinking/patterns behind any examples (not just the examples themselves)
