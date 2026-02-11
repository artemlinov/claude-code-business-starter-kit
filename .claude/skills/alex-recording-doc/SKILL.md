---
name: alex-recording-doc
description: Create a recording doc for Alex Garcia's YouTube videos. Takes A/B test titles and a newsletter as input, outputs a scannable doc Alex uses while recording — scripted hook, rough body structure, and Kallaway-style engagement phrases between sections.
---

# Alex Garcia — YouTube Recording Doc

Turn Alex's newsletters into clean, scannable recording docs for YouTube.

## Knowledge Dependencies

Load these files before writing:

- `.claude/knowledge/alex-garcia/voice-of-alex.md` — Tone, patterns, what Alex sounds like
- `.claude/knowledge/alex-garcia/alex-garcia-brand-dna.md` — Brand identity, positioning, what to avoid

## Required Inputs

Before starting, confirm you have:

1. **A/B Test Titles** — The title options being tested (usually 2-3). The hook must deliver on ALL of them.
2. **Newsletter Content** — Alex's newsletter (PDF or pasted text). This is always the source material.

If either is missing, ask for it.

## Output

**Location:** `content/youtube/[topic-slug]/`
**File:** `recording-doc.md`

The output is a single markdown file Alex reads while recording. It must be:
- Scannable at a glance
- Clean — no meta-instructions, no AI language, no unnecessary explanation
- Formatted for fast reading under studio pressure

## Document Structure

Every recording doc has these sections in order:

### 1. HOOK (fully scripted)

The hook is the only part written word-for-word. Alex reads it or memorizes it.

**How to write the hook:**

- Read all A/B test titles. Identify the core promise and angle across them.
- The hook must be versatile — it should work no matter which title wins the A/B test.
- Write in Alex's voice: calm authority, no hype, speaks with certainty. Reference `voice-of-alex.md`.
- No exclamation points. No "let's go" energy. No emojis. No ALL CAPS.

**Hook structure (aim for 45-60 seconds spoken):**

1. **Pattern interrupt** (1-3 sentences) — Call out what most brands/creators get wrong. Bold claim or contrarian observation. Make the viewer stop scrolling.
2. **Authority anchor** (1-2 sentences) — Brief credibility. Alex's experience working with brands. Not bragging — just earning the right to teach.
3. **The mechanism** (2-3 sentences) — Name the concept. Define it in one line. State what it costs, what it requires, and why it works.
4. **The promise** (1-2 sentences) — Tell them exactly what they'll leave the video with. Be specific — name the formats, the number of things, the deliverable.
5. **Bridge** (1 sentence) — One punchy line that transitions into the body. Short. Confident. No fluff.

**Hook quality check:**
- Does it deliver on ALL the A/B test titles?
- Is it under 60 seconds when read aloud?
- Does it sound like Alex, not a YouTuber?
- Is there a clear promise of what the viewer gets?

### 2. VIEWER QUALIFIER (optional — skill decides)

A brief "who this is for" section right after the hook. Include it when:
- The topic could apply to multiple audience levels and you need to narrow it
- The video has a specific prerequisite (e.g. "you should already have X")
- Without it, the viewer might wonder "is this for me?" during the first few minutes

Skip it when:
- The hook already makes it obvious who the video is for
- The topic is universally applicable

Format: A transition line ("But first — who is this for?"), then 2-4 bullet points, then a transition into the first section. Keep it under 15 seconds spoken.

### 3. BODY (rough structure + engagement phrases)

This is NOT a script. Alex knows his content — he wrote the newsletter. The body is:

- **Bullet points** for what to cover in each section
- **Transitional phrases** between sections (written out word-for-word, blockquoted)
- **Mid-section engagement beats** to re-hook the viewer within longer sections

**How to build the body:**

1. Read the full newsletter. Identify the main sections and their content.
2. Decide the section order. Follow the newsletter's structure by default, but reorganize if a different order creates better video flow (e.g. building from simple to complex, or leading with the most compelling format).
3. For each section, write concise bullet points — not full sentences. Strip the newsletter's formal language down to conversational talking points. Less is more. Alex needs reminders, not a teleprompter.
4. Between every section, write a transitional phrase (blockquoted). These are the most important part of the body.

**Bullet point rules:**
- Short — one line per point
- Conversational — how Alex would say it, not how the newsletter reads
- Include examples with brand names (e.g. "Example: Heart and Soil")
- No "Alex covers:" or "Alex talks about:" prefixes — just the bullets

### 4. MID-ROLL CTA

Place one CTA after the first body section. Always the same structure:

> "If you want to get the full [Topic] Playbook as a follow-along guide, click the first link in the description."

Replace [Topic] with whatever the video's subject is. This is the newsletter repackaged as a one-pager download.

Visually separate it with a horizontal rule so Alex can see it clearly while recording.

### 5. CLOSE (scripted)

The close follows a consistent structure:

1. **Recap** — Quick summary of what was covered. Short list, not a paragraph.
2. **Action step** — One specific thing the viewer should do right now.
3. **The line** — "Execute optimistically, strategize pessimistically. Start where you are. Not where you wish you were."
4. **CTA** — "If you want to get the full [Topic] Playbook as a follow-along guide, click the first link in the description."
5. **Sign-off** — "Until the next episode, Alex."

## Transitional Phrases — The Engagement Layer

These are the core value of this doc. Without them, the video is just information stacked on information. With them, it breathes.

**Types of transitions to use between and within sections:**

| Type | When to use | Example |
|------|------------|---------|
| "But" pivot | After setting up what most people think/do — flip it | "But here's where the execution starts to separate." |
| "Therefore" resolution | After explaining a problem — deliver the payoff | "And therefore, the only thing that matters is how good the idea is executed." |
| Short reset | After a dense section — snap attention back | "That's it." / "Zero budget." / "That's the whole formula." |
| Rhetorical bridge | Before showing examples or a new section | "So what does that actually look like?" |
| Payoff preview | Before a section to keep them watching through the current one | "This next format is the one most brands overlook." |
| Contrast flip | Before teaching something — break the old belief first | "It's not about expensive gear. It's about being intentional." |
| Callback | Anytime — tie back to the hook for cohesion | "Remember — phone and a brain. That's all you need." |

**Rules for transitions:**
- Every section must have a transition IN and a transition OUT
- Longer sections get 1-2 mid-section beats to re-engage
- Transitions are always blockquoted (>) so they stand out visually
- Write them conversationally — these are spoken phrases, not written ones
- Vary the types. Don't use the same trick twice in a row.

## Formatting Rules

The doc must be instantly scannable. Alex is reading this under studio lights, between takes.

- **Section headers** — `##` for main sections, bold for sub-sections within
- **Transitions** — Always blockquoted (`>`)
- **Bullet points** — Short, one line each
- **Horizontal rules** (`---`) — Between major sections and around the mid-roll CTA
- **No meta-language** — No "Alex should talk about", no "this section covers", no "note for Alex"
- **No italic instructional text** — Everything in the doc is either script or bullet points
- **No emoji** — Ever
- **No exclamation points** — Ever

## Voice Reference

Pull from `voice-of-alex.md`. Key patterns for the scripted sections (hook + close):

- "Here's the reality..."
- "Let me break it down..."
- "So, in this video you're going to learn..."
- Ellipsis for dramatic pause: "But here's the problem..."
- Short paragraphs. Breathing room.
- Certainty, not speculation. Frameworks, not hype.
- Opens with proof or bold claim, never fluff.

## Quality Checklist

Before delivering:

- [ ] Hook delivers on ALL A/B test titles?
- [ ] Hook is under 60 seconds spoken?
- [ ] Hook sounds like Alex (no hype, no exclamation points)?
- [ ] Body follows newsletter content but is reorganized for video flow if needed?
- [ ] Every section has a transition in AND out?
- [ ] Longer sections have mid-section engagement beats?
- [ ] Transition types are varied (not the same trick twice in a row)?
- [ ] Mid-roll CTA placed after first body section?
- [ ] End CTA matches the video topic?
- [ ] Bullet points are short and conversational?
- [ ] No meta-language, no AI artifacts, no instructional notes?
- [ ] Doc is scannable at a glance?

## Example

See `content/youtube/level-1-content-strategy/recording-doc.md` for a reference output.
