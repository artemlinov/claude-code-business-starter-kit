---
name: content-idea-analyzer
description: Analyze raw voice memo ideas and suggest what content pieces to create from them. Routes to appropriate content creation skills. Use when user says 'analyze this idea', 'what can we make from this', 'content idea', 'what content can I create', 'turn this into content', or pastes a voice memo about a content idea.
---

# Content Idea Analyzer

Analyze content ideas and determine what to create from them. This skill sits above all content creation skills and routes to the right one.

## Knowledge Dependencies

Load these files before analyzing:

**Voice & Stories:**
- `.claude/knowledge/artem/voice-of-artem.md` — Understand what resonates with Artem's voice
- `.claude/knowledge/artem/artem-story-bank.md` — Check existing stories, know where new ones fit

**Targeting:**
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Who this content serves
- `.claude/knowledge/full-time-editor/fte-framework-definitions.md` — Proprietary frameworks to connect ideas to

## Required Inputs

1. **The idea** — A voice memo transcript, written idea, or raw notes from the user

If the input is a call transcript or messy multi-topic source, redirect to `content-insight-extractor` skill first. This skill handles ONE clean idea at a time.

## Workflow

### Step 1: Read and Understand the Idea

Read the full idea. Identify:
- The core insight or lesson
- Who it's relevant to (check against ICP)
- Whether it connects to any existing FTE frameworks
- Whether it contains a personal story or example

### Step 2: Classify the Idea by Density

Every idea falls into one of two categories:

**A) Full Content Piece** — Has enough depth, nuance, or structure to be a standalone piece of content. Characteristics:
- Contains a teachable framework or process
- Has a clear belief shift or contrarian take
- Could sustain 5+ minutes of video or 500+ words
- Has packaging potential (someone would click on this)

**B) Micro-Idea / Story** — A personal example, analogy, proof point, or small insight. Too small for standalone content but valuable as enrichment. Characteristics:
- A personal anecdote or client story
- A single observation or analogy
- A proof point that makes a bigger idea stick
- Something that adds relatability or credibility when woven into other content

### Step 3: Present the Analysis

Output a structured analysis card:

```
## Idea Analysis

**Core Insight:** [1-2 sentence summary of the idea]

**Classification:** [Full Content Piece / Micro-Idea / Story]

**ICP Relevance:** [Why this matters to our audience — reference specific ICP pain points or desires]

**Framework Connection:** [Which FTE framework(s) this relates to, if any]
```

Then, based on classification:

#### For Full Content Pieces — Suggest Formats

List which formats this idea works for, with a brief note on WHY for each. Only suggest formats that genuinely fit — don't force it.

**Available formats:**
- **Tweet(s)** — Works if there's a punchy insight, hot take, or single powerful statement. Best for ideas that can land in 1-3 sentences.
- **Thread** — Works if there's a step-by-step breakdown, multi-point argument, or story arc. Best for ideas with 3-7 distinct points.
- **YouTube Video** — Works if there's enough depth for 10-15 minutes, a clear belief shift, and strong packaging potential (would someone click this title?). Requires a personal story element.
- **Newsletter** — Works if there's a framework to unpack, a lesson with layers, or a deep-dive that benefits from longer reading format.
- **Email** — Works if the idea relates to selling, nurturing, or overcoming objections about FTE offers.

Format the suggestions like this:

```
### Suggested Content

1. **[Format]** — [Why this idea fits this format + what angle to take]
2. **[Format]** — [Why + angle]
...
```

#### For Micro-Ideas / Stories — Suggest Storage

```
### Story Bank Addition

**Suggested Section:** [Which section of artem-story-bank.md this belongs in]
**Suggested Theme:** [What theme or lesson this story illustrates]
**Draft Entry:** [Write a concise story bank entry in the same format as existing entries]
```

Also suggest which types of future content this micro-idea could enrich:
```
### Future Use Cases
- Could illustrate [concept] in a YouTube video about [topic]
- Could be a proof point in a thread about [topic]
- Connects to [existing story bank entry] as a reinforcing example
```

### Step 4: Route to Content Creation

Ask the user what they want to create. Based on their choice:

- **Tweet(s)** — Summon `x-tweets-writer` skill (if it exists, otherwise write tweets directly using voice-of-artem-twitter.md)
- **Thread** — Summon `x-threads-writer` skill (if it exists, otherwise write thread directly using voice-of-artem-twitter.md)
- **YouTube Video** — Summon `youtube-script-writer` skill, passing the idea as the Big Idea + Raw Thoughts
- **Newsletter** — Summon newsletter writer (if it exists, otherwise write directly using voice-of-artem-newsletter.md)
- **Email** — Summon `1m-email-writer` skill
- **Story Bank** — Append the draft entry to `artem-story-bank.md` under the suggested section (confirm with user first)

When summoning a skill, pass along:
- The original idea text
- The core insight you identified
- The suggested angle for that format
- Any relevant framework connections

## Important Rules

1. **One idea at a time.** If the user gives you multiple ideas, analyze each separately.
2. **Don't force formats.** If an idea only works as a tweet, only suggest a tweet. Don't pad the list.
3. **Check the story bank.** Before suggesting a story bank addition, read artem-story-bank.md to avoid duplicates and find the right section.
4. **ICP lens always.** Every suggestion should pass the test: "Would our ICP care about this?"
5. **Be honest about density.** Most voice memo ideas are micro-ideas. That's fine. Don't inflate a small observation into a full video pitch.
