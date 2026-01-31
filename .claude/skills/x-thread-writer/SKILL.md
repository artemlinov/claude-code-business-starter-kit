---
name: thread-writer
description: Generate X/Twitter threads for Full-Time Editor. USE WHEN user wants to create a thread, says "write a thread", "thread about", "turn this into a thread", or has long-form content (transcript, blog post, lesson) to transform into thread format.
---

# Thread Writer

Transform source content into story-driven X threads for Full-Time Editor's audience of skilled-but-stuck video editors.

---

## Knowledge Dependencies

Before generating threads, load:

- `.claude/knowledge/artem/voice-of-artem.md` — Core voice and tone
- `.claude/knowledge/artem/voice-of-artem-twitter.md` — Platform-specific patterns
- `.claude/knowledge/artem/artem-story-bank.md` — Personal stories to weave in
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Target audience
- `.claude/knowledge/full-time-editor/fte-framework-definitions.md` — Framework names with ™
- `.claude/knowledge/full-time-editor/full-time-editor-manifesto.md` — Brand beliefs

---

## Process

### Step 1: Extract Core Idea

Identify the transformation or lesson from source content. Ask:
- What's the before → after?
- What's the key insight?
- What proof/screenshots could support this?

### Step 2: Ask for Story Context

Prompt user: "Do you have a personal story related to [topic]? Check your story bank or share details."

Even educational threads benefit from story elements.

### Step 3: Generate 3 Hook Variations

Create 3 hook tweet options. Each must:
- Be under 280 characters
- Include specific transformation with numbers
- End with "Here's [the story / how]:" or similar
- Specify what image to use

**Wait for user approval before continuing.**

### Step 4: Write Full Thread

Once hook is approved, write the complete thread:
- Every tweet under 280 characters (hard limit)
- Image guidance for each tweet
- Transition phrases where needed
- CTA woven naturally when it fits content
- P.S. CTA at the end (always)

### Step 5: Format Output

For each tweet:

```
**Tweet [Number] — [Section Type]**

[Tweet text]

**Characters:** [X]
**Image:** [Specific description of what to show]
**Transition:** [Phrase leading to next tweet, if applicable]
```

---

## Output

**Location:** `content/social/twitter/threads/`
**Format:** Markdown file with complete thread

---

## Formatting Rules

### Character Limit
Every tweet under 280 characters. Count before presenting. No exceptions.

### Bullets
- Use `–` (medium dash) for bullet lists
- Use numbered lists (1. 2. 3.) for sequential steps or ranked tips
- Never use `*` or `-`

### Numbers
- Use $5K not $5,000
- Always specific: $2.5K, 18 months, 40 hours/week

### Structure
- Generous line breaks between thoughts
- Single-line statements hit harder
- Ladder format for lists: shortest → longest

---

## Thread Structure (Flexible)

### Hook Tweet (Always First)

```
[Timeframe] → [Timeframe]

[Specific transformation with numbers]:

– [Before metric]
– [After metric]
– [Result metric]

Here's [the story / how]:
```

**Image:** Always required. Transformation visual, Artem working, or key proof.

### Context / Setup

```
[The problem or situation]

[Emotional state if story-driven]

[Specific details that make it real]
```

**Image:** Screenshot, proof, or relevant visual.

### Turning Point

```
[What changed / the realization]

[Action taken]

[Hint at what's coming]
```

**Image:** Proof of action taken.

### The Climb / Teaching Section

For story threads:
```
[Step-by-step progression]
[Specific numbers at each stage]
[Mini-bars at end of tweets]
```

For educational threads with tips:
```
1. [Headline of Tip]

[Explanation + why it works]

[Personal proof/example if available]
```

**Images:** As many as possible — screenshots, DMs, income proof, app interfaces.

### Breakthrough / Result

```
[The outcome / transformation]

[Specific numbers]

[What it means / felt like]
```

**Image:** Proof of result.

### P.S. CTA (Always Last)

```
P.S. [Pitch related to thread content]

[What they'll get]

[Link]
```

---

## Hook Formulas

### The Transformation Hook

```
[Date/Time] → [Date/Time]

[X months] that changed my life:

– [Before metric]
– [After metric]
– [Key result]

Here's the entire story:
```

### The Result Hook

```
I finally hit [specific result] in [timeframe].

But I wanted more...

So I [action taken] until I [bigger result].

Here are [X] that actually worked:
```

### The Contrast Hook

```
[X]% of video editors don't [do thing].

But it [benefit].

Here's how:
```

### The Proof Hook

```
This is [specific artifact — email, DM, screenshot].

[X] crazy things here:

1. [Surprising fact]
2. [Result it led to]
3. [Context that makes it impressive]

Here's how you can too:
```

---

## Transition Phrases

Use between tweets to maintain flow:

- "Here's how:"
- "Here's the story:"
- "And it worked!"
- "But I wanted more..."
- "Until one day something happened..."
- "Let me explain:"
- "Now, let's break down how:"
- "The breakthrough happened when..."
- "This is where it gets interesting:"
- "But here's the thing:"

---

## CTA Guidelines

### P.S. CTA (Required — Always at End)

```
P.S. Inside [program/resource], I [what you do for them].

[Specific benefit]

[Link]
```

### Woven CTAs (Optional — Only When Natural)

- Only include when directly related to content just discussed
- Better to have fewer, well-placed CTAs than forced ones
- Should feel like a natural extension, not an interruption
- Link to specific resource that matches the topic

**Example of natural CTA placement:**

After discussing X Brand strategy:
```
And I actually recorded an in-depth training on how you can set up your own High-Ticket X Brand, too.

Sign up here to get it for free: [link]
```

---

## Proof Elements

Threads need proof. Types to suggest:

- **DM screenshots** — Client conversations, wins, testimonials
- **Income proof** — Payment screenshots, revenue graphs, rate increases
- **Email screenshots** — Outreach that worked, client responses
- **App/tool screenshots** — Settings, workflows, systems
- **Before/after comparisons** — Edits, rates, results
- **Timeline visuals** — Progress charts, milestone markers

---

## Image Guidance Format

For each tweet, specify:

```
**Image:** [Type]: [Specific description]
```

Examples:
- **Image:** Screenshot: DM conversation showing client agreeing to $2K/video rate
- **Image:** Graph: Income progression from $600 to $8K over 9 months
- **Image:** App screenshot: OneSec app blocking Instagram with breathing exercise
- **Image:** Proof: Email showing first $300/video client response
- **Image:** Visual: Artem working at desk during deep work block

---

## Headline Format (For Tips/Lists)

When thread includes numbered tips:

```
1. Never Check Your Phone First Thing

[Explanation]

[Why it works]

[Personal example if available]
```

Use this format when:
- Thread is listicle-style (5 hacks, 7 tips, etc.)
- Each tip is distinct enough to warrant its own section
- It helps scannability

Skip if thread flows better as continuous narrative.

---

## Quality Checklist

Before presenting thread, verify:

- [ ] Every tweet under 280 characters
- [ ] Hook includes specific numbers and transformation
- [ ] Image guidance for every tweet
- [ ] Transitions flow naturally between tweets
- [ ] CTAs only where they fit naturally
- [ ] P.S. CTA at the end
- [ ] Proof elements suggested throughout
- [ ] Sounds like Artem, not AI

---

## Example Hook Variations

For a thread about productivity systems:

**Hook Option 1 — Transformation**
```
I finally hit $2.5K/month video editing in August 2023.

But I wanted so much more...

So I locked myself in my room and experimented with every productivity hack until I cracked $10K/month.

Here are 5 that actually worked:
```
**Characters:** 273
**Image:** Graph showing income progression from $2.5K to $10K

---

**Hook Option 2 — Contrast**
```
Most video editors grind 12 hours and make $2K/month.

I work 4 hours and make $10K.

The difference isn't talent.

It's these 5 systems:
```
**Characters:** 147
**Image:** Split screen: chaotic desk vs. clean minimal setup

---

**Hook Option 3 — Specific Result**
```
One change added $8K/month to my editing income:

Not checking my phone before 11am.

Sounds too simple to work.

Here's why it changed everything:
```
**Characters:** 168
**Image:** Screenshot of phone screen time showing minimal morning usage

---

## Thread Length

No strict requirement. Write whatever explains the concept fully.

Soft guidance: Most effective threads are 8-20 tweets. Shorter for focused concepts, longer for journey stories.
