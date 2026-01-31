---
name: content-insight-extractor
description: Extract content ideas and insights from call transcripts, mastermind recordings, and other messy multi-topic sources. Use when user says 'extract ideas from this', 'pull content from this call', 'what content can we get from this transcript', 'extract insights', or pastes a long call/meeting transcript.
---

# Content Insight Extractor

Extract discrete content ideas from noisy sources like call transcripts, mastermind recordings, coaching calls, and interviews. This skill sits at the top of the content pipeline — it feeds clean idea cards into `content-idea-analyzer`.

## Knowledge Dependencies

Load these files before extracting:

**Targeting:**
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Filter for ICP relevance
- `.claude/knowledge/full-time-editor/voice-of-customer.md` — Recognize language that signals valuable content
- `.claude/knowledge/full-time-editor/fte-framework-definitions.md` — Spot framework connections

## Required Inputs

1. **The source material** — A call transcript, mastermind recording transcript, interview notes, or any multi-topic text
2. **Source context** (optional but helpful) — What kind of call this was, who was on it, what the purpose was

If the user gives you a clean single-topic voice memo or idea, redirect them to `content-idea-analyzer` instead. This skill is for messy, multi-topic sources.

## Workflow

### Step 1: Read and Filter

Read the entire source. Mentally separate:
- **Signal** — Insights, stories, frameworks, lessons, hot takes, personal examples, client wins, aha moments
- **Noise** — Small talk, logistics, scheduling, off-topic tangents, filler, pleasantries

### Step 2: Extract Idea Cards

For each distinct content idea found, create an idea card:

```
### Idea [number]: [Short title]

**Core Insight:** [1-2 sentences — the actual idea, cleaned up]

**Who Said It / Context:** [Speaker name if identifiable, what prompted this insight]

**ICP Relevance:** [Why our audience would care — reference specific pain points or desires]

**Density Classification:**
- [ ] Full Content Piece — enough depth for standalone content
- [ ] Micro-Idea / Story — a proof point, anecdote, or small insight to enrich other content

**Framework Connection:** [Which FTE framework this relates to, if any. "None" is fine.]

**Raw Quote:** [The best direct quote from the source that captures this idea, if available]
```

### Step 3: Present All Extracted Ideas

Present the complete list of idea cards, ordered by ICP relevance (most relevant first).

At the top, include a summary:

```
## Extraction Summary

**Source:** [Type of call/meeting + date if known]
**Ideas Found:** [X total — Y full content pieces, Z micro-ideas/stories]
**Top Insight:** [The single most valuable idea from this source]
```

### Step 4: Route to Analyzer

Ask the user which ideas they want to develop. For each selected idea:

1. Pass the idea card to `content-idea-analyzer` skill
2. The Analyzer will then suggest formats and route to content creation skills

The user can also:
- **Select all** — Analyze every extracted idea
- **Pick specific numbers** — "Analyze ideas 1, 3, and 5"
- **Story bank only** — Send all micro-ideas directly to story bank without full analysis

## Extraction Rules

1. **Be aggressive about extracting.** If something could be content, pull it out. The user can discard later. Missing an idea is worse than suggesting one that doesn't work.
2. **Separate compound ideas.** If one conversation segment contains two distinct insights, make two idea cards.
3. **Preserve the raw language.** Include direct quotes when possible — the original phrasing often has more energy than a clean summary.
4. **Check for Artem's stories.** If Artem tells a personal story or example during the call, always flag it as a micro-idea for the story bank, even if it's also part of a bigger point.
5. **ICP filter is soft, not hard.** Some ideas might serve the broader content creator audience, not just video editors. Still extract them — note the wider relevance.
6. **Don't editorialize.** Present what was said. Don't add your opinion on whether the idea is "good" — let the Analyzer handle that.
