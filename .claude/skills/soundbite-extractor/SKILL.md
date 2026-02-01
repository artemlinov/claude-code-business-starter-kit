---
name: soundbite-extractor
description: Pull punchy, vlog-ready soundbites from call and meeting transcripts. USE WHEN user says 'pull soundbites', 'extract quotes from this call', 'vlog soundbites', 'punchy phrases from transcript', 'soundbites from this call', 'grab quotes from transcript', 'vlog segment from this call', 'give me a sequence of phrases'.
---

# Soundbite Extractor

Pull exact, punchy soundbites from transcripts and arrange them into a sequence that builds a story arc — ready to drop into a vlog as a montage segment.

## Knowledge Dependencies

Load these files before extracting:

**Voice & Context:**
- `.claude/knowledge/artem/voice-of-artem.md` — Understand Artem's natural speaking patterns and energy
- `.claude/knowledge/full-time-editor/full-time-editor-overview.md` — Brand context for relevance filtering

## Required Inputs

1. **The transcript** — A call transcript, meeting recording, coaching session, or any conversation transcript
2. **Context** (optional) — What the soundbites are for (e.g., "vlog segment about coaching my editors")
3. **Must-include phrases** (optional) — Specific phrases the user already wants in the sequence

If the user wants full content ideas extracted (not soundbites), redirect to `content-insight-extractor` instead. This skill is specifically for pulling punchy phrases for video montage segments.

## Workflow

### Step 1: Scan and Tag

Read the entire transcript. Mentally tag every phrase that hits as:

- **Emotional moments** — Vulnerability, excitement, frustration, breakthroughs
- **Conviction statements** — Strong opinions, hot takes, beliefs stated with force
- **Humor** — Funny moments, roasts, self-deprecating jokes, community banter
- **Hype / Energy** — Excitement, reactions, "bro that's sick" moments
- **Signature catchphrases** — Recurring phrases that define the speaker's personality
- **Conversational sparks** — Back-and-forth exchanges that feel alive

### Step 2: Extract Candidates

Pull 15-20 candidate phrases from the transcript.

For each candidate:
- Use the **exact quote** from the transcript — never paraphrase, never clean up grammar, never alter wording
- Label with the speaker's name
- Prefer shorter phrases over longer ones — if a long quote has a punchy core, extract just the punchy part
- Include phrases from multiple speakers, not just the main one

### Step 3: Build Story Arc

Arrange the best 7-12 candidates into a sequence that builds momentum:

1. **Open** — Set the scene or energy level. Something grounded or intriguing.
2. **Build** — Core beliefs, insights, or philosophy. The substance.
3. **Spark** — Community voices, reactions, conversational exchanges. Break up the monologue.
4. **Peak** — The most impactful or emotional phrase in the sequence.
5. **Close** — Warm, forward-looking, or signature sign-off.

Not every sequence needs all five beats. Some calls naturally have 3 beats, some have 6. Follow what the transcript gives you.

### Step 4: Present the Sequence

Format as a numbered list:

```
1. **Speaker Name:** "Exact quote from transcript."

2. **Speaker Name:** "Exact quote from transcript."

3. **Speaker Name:** "Exact quote from transcript."
```

No labels like "The Setup" or "The Philosophy" — just number, speaker, quote. Let the sequence speak for itself.

### Step 5: Iterate

The user will want to adjust. Common requests:
- Swap a phrase for something else — suggest alternatives from your candidate list
- Add a community member's voice — find the best quotes from other speakers
- Make it more/less punchy — adjust phrase length and intensity
- Change the opening or closing — offer alternatives
- Remove redundancy — if two phrases hit the same note, cut one

Always have alternative phrases ready from your Step 2 candidates. When the user removes a phrase, suggest what could replace it. When they say "is there more?", surface unused candidates that might work.

## Extraction Rules

1. **NEVER alter quotes.** The phrases must be verbatim from the transcript. Not cleaned up, not paraphrased, not grammar-fixed. The user cannot alter them in post — what's in the transcript is what they have to work with.
2. **Shorter wins.** "Bro, that's sick" hits harder in a montage than a 4-sentence explanation. Extract the punchy core.
3. **Multiple voices.** Including community members, clients, or other speakers makes it feel like a conversation, not a lecture. Always look for good back-and-forth moments.
4. **No filler.** Cut "um", "like", "you know" from the start/end of quotes if the transcript includes them — but never change actual words.
5. **Momentum matters.** Read the sequence out loud in your head. Does each phrase naturally lead to the next? Does energy build? If two adjacent phrases feel flat, reorder or swap.
6. **Context-free clarity.** Each phrase should land even without knowing the full conversation. If a quote only makes sense with 2 minutes of context, it's not a good soundbite.
7. **Emotional range.** Don't make every phrase a hot take. Mix conviction with humor, vulnerability with hype. The best sequences feel human.

## Quality Checklist

Before presenting, verify:

- [ ] Every quote is verbatim from the transcript
- [ ] Sequence builds momentum when read back-to-back
- [ ] Multiple speakers included where the transcript allows
- [ ] No two phrases are redundant or hit the same emotional note
- [ ] Each phrase lands without needing surrounding context
- [ ] The sequence works as a punchy montage segment when spoken aloud
- [ ] Opening is grounded or intriguing, not generic
- [ ] Closing feels like a natural end point
