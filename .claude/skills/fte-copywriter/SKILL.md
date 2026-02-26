---
name: fte-copywriter
description: Write all FTE written content — newsletters, email sequences, Skool posts, sales/landing pages, offer docs. USE WHEN user says "write a newsletter", "email sequence", "nurture sequence", "pre-call emails", "post-call follow-up", "reminder email", "reactivation email", "launch email", "sales email", "Skool post", "build a sales page", "create checkout page", "landing page", "sales page copy", "build a page for [offer]", "offer doc", "repurpose this masterclass", "turn this masterclass into a newsletter", "newsletter from this session", "write a Skool post".
---

# FTE Copywriter

Write all Full-Time Editor written content. Every word sounds like Artem thinking out loud — direct, warm, specific. No hype, no guru energy.

The format adapts based on content type: newsletter, email, Skool post, or page.

---

## Knowledge Dependencies

**Always load:**

- `.claude/knowledge/artem/voice-of-artem.md` — Core voice and tone
- `.claude/knowledge/artem/voice-of-artem-written.md` — Written platform-specific patterns (email, newsletter, Skool)
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Who we're speaking to
- `.claude/knowledge/full-time-editor/voice-of-customer.md` — Their exact language
- `.claude/knowledge/full-time-editor/full-time-editor-manifesto.md` — Brand philosophy
- `.claude/knowledge/full-time-editor/fte-framework-definitions.md` — Frameworks with ™

**When writing sales copy or offer docs, also load:**

- `.claude/knowledge/full-time-editor/offer-positioning.md` — Offer stack, customer journey, headlines

---

## Step 1: Determine Content Type

Ask or infer what the user wants to write. This determines which rules to apply.

| Content Type | Key Rules | Output Location |
|-------------|-----------|-----------------|
| **Newsletter** | Newsletter rules (below) + never reveal source | `content/newsletters/[topic-slug]/` |
| **Email sequence** | Email rules (below) + sequence rules | Present in conversation |
| **Single email** | Email rules (below) | Present in conversation |
| **Skool post** | Skool rules (below) | Present in conversation |
| **Sales/landing page** | Page rules (below) | Present in conversation or Gamma |
| **Offer doc** | Page rules (below) + offer doc structure | Present in conversation or Gamma |

---

## Shared Copy Principles

These apply to ALL content regardless of type.

### Voice

- Direct, conversational, thinking out loud
- 1-3 sentence paragraphs, one thought per paragraph
- Contractions: gonna, wanna, it's
- Conversational interjections as transitions ("Solid, right??", "And here's the thing:")
- Cut aggressively — every draft is too long on the first pass
- NO hype words (amazing, incredible, life-changing)
- NO guru energy
- NO em dashes (—) — replace with period, comma, or colon
- NO bold in email or newsletter body (bold headers OK for pages only)

### Conversion Patterns

*The Thinking Out Loud Structure:*
1. State something direct
2. Add context or a question
3. Answer or reframe
4. Connect to the reader
5. Clear ask

*Reframes That Convert:*

"What has actually changed?"
```
What has actually changed in the past 6 months?

Not what you've tried. Not what you've learned. What has actually changed in your income, your clients, your situation?
```

"What happens if nothing changes?"
```
What happens if nothing changes?

If you're in the exact same position 6 months from now.

Same income. Same clients. Same frustrations.

→ What does that actually cost you?
```

"Difficult questions = real progress"
```
I'm not asking this to pressure you.

I'm asking because difficult questions are where the real progress is made.
```

"I'd rather you not join"
```
If it's not a fit, I'll tell you straight up. I'd rather you not join than join, spend your money, and not get the best results possible.
```

### Ethical Urgency Only

✓ "What's another 6 months of being stuck costing you?"
✓ "The sooner you start, the sooner you're at $5K/month"
✓ Real scarcity when true (e.g., "10 spots because I personally review every edit")

✗ "Only 3 spots left!" (unless actually true)
✗ Fake deadlines
✗ Pressure tactics
✗ ALL CAPS for emphasis

### Framework References

Always include ™ when referencing: Creative Director Shift™, Viewer-First Editing™, Quality-First Clients™, Freedom-First Workflow™, Price Last™, What, Not How™, Go Deep™, Twist & Stick™, The Three S's™, The 4-2-1™ Rule, The Blockout Graphic™, Story Blocks™, Powerful Phrases™, The Word-of-Work™ Method, High-Ticket Outreach™, The 5% Rule, Base File™.

---

## Newsletter Rules

For turning masterclass recordings, raw ideas, or topics into newsletter issues.

### Critical Newsletter Rules

1. **Never reveal the source.** The newsletter reads as Artem's personal insights — not a masterclass recap. Never write "in my recent masterclass," "I was teaching last week," "my students asked about this." The reader should feel like Artem sat down and wrote this directly to them.

2. **Images as placeholders.** Where a slide or screenshot belongs, write `*[image: brief description]*`. Mark the spot — don't describe the visual in text.

3. **Subject and preview are separate.** Never embed the subject line into the email body. Present them as distinct labeled elements.

### Newsletter Process

**Step 1: Review source materials.** Extract: the single core insight (the "big idea"), 5-8 practical actionable techniques, personal stories or Artem moments, connections to FTE frameworks.

**Step 2: Generate 3 angles.** Each includes: subject line, preview line (85-140 chars), hook (first 3-5 sentences), core framing (one sentence), and structure (2-3 sentences). Present all 3. Let user select or mix.

Good angle directions:
- "The weird thing I've noticed" — observation revealing a deeper truth
- "The secret to [X]" — contrarian reveal of what actually creates the result
- "It's not your [X], it's your [Y]" — reframing a false belief

**Step 3: Wait for angle selection.** Do not draft until confirmed.

**Step 4: Draft the newsletter.** Follow the structure below.

**Step 5: Output.** Present: subject line, preview line, email body. List slides/images at each placeholder. Save to `content/newsletters/[topic-slug]/[topic-slug].md`.

### Newsletter Structure

**1. Hook (2-5 lines)** — Contrarian observation, "weird thing I've noticed," or bold claim. No fluff. No warm-up.

**2. Personal Story (3-6 lines)** — Brief. Grounds the lesson in Artem's real experience. Specific, not vague. Short — it sets up the principle, not the main event. Skip if no clean story in source.

**3. The Principle (2-4 lines)** — Core insight in simplest form. Quotable. Name the FTE framework if natural fit.

**4. Framework Steps (main body)** — Walk through the framework as named steps, written conversationally.

Format for each step:
```
Step [N]: [Name]

[2-4 short paragraphs. One thought per paragraph.]

[Use – lists for sub-items:]

– First item
– Second item
– Third item

*[image: description]* — only if a slide genuinely adds value. Optional.
```

Rules:
- "Step N: Name" is a plain text heading, NOT bold numbered bullets
- Write each step as prose, not a definition or instruction manual
- Be specific: real numbers, real examples, real scenarios
- Sub-items within steps use `–` lists, not numbers
- Keep it conversational

**5. Close + CTA (Bar + Teaser + Link)**

The Bar: one memorable, quotable line that crystallizes the whole lesson. Stands alone.

The Teaser: immediately after the Bar, introduce a NEW curiosity hook. Don't restate the lesson. Open a new door.

The CTA: let the teaser carry them into why they should click. Name the specific pillar or framework from the free course.

```
[The CTA]
I cover exactly how to do this in the [Pillar Name] pillar of the Creative Director Shift™.

You can watch the whole thing for free right now inside my Skool community.

See you there,

– Artem
```

Rules:
- Never "Grab it inside the free community here:" — too transactional
- Use "See you there," or "See you inside,"
- Link always goes to https://www.skool.com/full-time-editors

**6. P.S.**

Default — Engagement P.S.:
```
P.S. [Topic question]? Hit reply and let me know. I read every single one.
```

Optional — Sales P.S. (only when naturally connected):
```
P.S. If you're already above $1K/month and want to take this further, reply with "coconut" and I'll send you the details on working together.
```

### Newsletter Quality Checklist

- [ ] Source never mentioned (no "masterclass," "session," "my students")
- [ ] No em dashes anywhere
- [ ] All paragraphs 1-3 sentences
- [ ] Subject and preview labeled and separate from body
- [ ] Framework steps use "Step N: Name" heading — NOT bold numbered bullets
- [ ] Sub-items use `–` lists, not numbers
- [ ] Specific details (real numbers, examples, scenarios)
- [ ] Close has a memorable "Bar" line
- [ ] Close includes a curiosity teaser before CTA
- [ ] CTA uses "See you there," or "See you inside,"
- [ ] CTA links to https://www.skool.com/full-time-editors
- [ ] Sounds like Artem talking to one reader

---

## Email Rules

For email sequences, pre-call emails, reminders, follow-ups, reactivation emails, nurture sequences, launch emails, and sales emails.

### Structural Rules

**Greetings:**
- First email in sequence: `Hey {{name}},`
- Follow-up emails: `{{name}},` (no "Hey")

**Paragraphs:** 1-3 sentences max. One thought per paragraph. Generous whitespace.

**Lists:** 3-5 items max. One item per line. NO bullet points or dashes — just line breaks.

**Emphasis:** Use `→` before the primary CTA (ONE per email max). NO bold in email body.

**Sign-offs:**
- In sequences: "Talk [day of week]." (day = when next email sends)
- Standalone: "Looking forward to it." / "Talk soon." / "See you tomorrow."
- Always just "Artem" (no dash)

### Email Rhythm & Pacing

1. One sentence per line. Break compound sentences.
2. Ellipsis (...) for trailing thoughts. 1-2 per email max.
3. Conversational interjections as transitions: "The second type though?" / "Solid, right??"
4. Colons before lists/explanations: "Here's what I mean:" not "Here's what I mean."
5. Never echo subject/preview in the opening. Jump straight into content.
6. Cut aggressively. Remove filler.
7. Double question marks ("??") for rhetorical emphasis.

### Subject Lines

4-8 words, lowercase (unless proper noun), no periods, personal not promotional.

| Format | Example |
|--------|---------|
| Direct question | "quick question before our call" |
| Specific number | "the $2K/video question" |
| Curiosity gap | "one thing I forgot to mention" |
| Time-based | "12 hours from now" |
| Pattern interrupt | "this might sound weird" |
| Continuation | "re: your call tomorrow" |

### Preview Text

40-90 characters. Complements subject (doesn't repeat). Fragment, not a sentence.

### Email Output Format

```
**Subject:** [subject line]
**Preview:** [preview text]

---

[Email body]
```

### Sequence Rules

- Don't repeat offer details from earlier emails. Each email adds new info or angle.
- When a checkout/landing page exists, use that as CTA. Don't use "reply and I'll send the link."
- First mention of program price: full program name. After that, shorthand.
- Use concrete numbers, not ranges ($1,500/video not $1,000+/video)
- Trust the sequence — don't repeat what's covered

### Email Quality Checklist

- [ ] Sounds like Artem (not a marketer)
- [ ] ONE clear ask per email
- [ ] No bullet points or bold text
- [ ] 1-3 sentences per paragraph
- [ ] One sentence per line
- [ ] Arrow (→) used only once, before primary CTA
- [ ] Subject line 4-8 words, lowercase
- [ ] Preview complements (not repeats) subject
- [ ] Opening does NOT echo subject/preview
- [ ] Uses contractions
- [ ] No hype words, no guru energy

---

## Skool Post Rules

For community announcements, teasers, launches, and engagement posts inside Skool.

### Structural Rules

**Titles:** Short, punchy. Lowercase unless proper noun. Can use ellipsis for curiosity.

**Paragraphs:** 1-2 sentences max (shorter than email). One thought per line.

**Lists:** Emoji numbers (1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣) for structured lists. One item per line. Short items.

**Emphasis:** Arrow (→) before key info or CTA — ONE per post max. NO bold. NO bullet points with dashes.

**Engagement:** Every post ends with an invitation to engage: "Drop a comment." / "Reply if you have questions." / "I wanna know who's paying attention."

### Skool-Specific Patterns

- More vulnerability than email — share nervousness, uncertainty, behind-the-scenes feelings
- "People in this room" / "people in this community" — creates belonging
- Can reference existing members directly
- NO walls of text — posts get skipped in feeds
- NO multiple links — one link per post max

### Post Types

**Announcement/Tease:**
```
Title: Something new is dropping [date]...

I've been building something I've never done before.

And I'm kinda nervous about it.

It's for a very specific type of editor:

1️⃣ Someone who's in this community
2️⃣ Someone who knows they're capable of more, but feels stuck in the same spot.

[continue with tease, end with engagement prompt]
```

**Launch/Offer:**
```
Title: [Offer name] is live.

[Reference previous tease]

[One-line description]

[Key details: price, spots, deadline]

Here's what you get:

1️⃣ [Item]
2️⃣ [Item]
3️⃣ [Item]

[Link]

Reply if you have questions.
```

### Skool Quality Checklist

- [ ] Title is short and punchy
- [ ] Paragraphs are 1-2 sentences max
- [ ] Lists use emoji numbers, not dashes
- [ ] ONE link max per post
- [ ] Ends with engagement prompt
- [ ] No walls of text
- [ ] More vulnerability/behind-the-scenes than email

---

## Page Rules

For sales pages, checkout pages, landing pages, and offer docs.

### What Changes for Pages

- **Bold headers OK** — use for section titles and sub-items
- **Structured lists OK** — for "what's included" sections
- **CTA repeated 2-3 times** — hero, after investment section, final section
- **Visual hierarchy** — use H1/H2/H3 for scannable structure
- **Longer format OK** — pages can be comprehensive
- **"How to Join" section** — numbered steps to make action simple
- **Investment framing** — ROI math + price objection handling on-page

### Conversion Flow

Progressive reveal: Problem → Qualification → Solution → Details → Proof → Price → Action

Key patterns:
- **Qualification section early** — filter before selling: "This is for X. This is NOT for Y."
- **Named frameworks with ™** — builds perceived value
- **"The Investment" framing** — not just "Price"
- **Step-by-step "How to Join"** — makes action feel simple (3-4 numbered steps)
- **Testimonials after price** — reinforce after investment section

### Page Type Reference

| Type | Sections |
|------|----------|
| **Short checkout** | Hero → What's Included → CTA |
| **Medium hybrid** | Hero → What's Included → Who It's For/Not For → FAQ → CTA |
| **Full sales page** | Hero → Problem → Qualification → Solution → What's Included → Timeline → Social Proof → Investment → FAQ → How to Join → Final CTA |
| **Offer doc** | Hero Invitation → What Is This? → Qualification → Unique Mechanism → Focus Areas → Detailed Outcomes → Program Summary → Timeline → The Effort → FAQ → Investment → Guarantee → How to Join → Testimonials |

### Two Sales Pages in the FTE Ecosystem

1. **Core Offer Doc** — For the Full-Time Editor program ($3,000/6mo). Used after qualification.
2. **Micro Offer Doc** — For the Insight Program ($249/2wk, "sneak peek into FTE"). Used for qualified leads not ready for full commitment.

### Page Quality Checklist

- [ ] Sounds like Artem (not a marketer)
- [ ] Clear CTA repeated 2-3 times
- [ ] Bold headers and structured lists (page format, not email)
- [ ] 1-3 sentences per paragraph
- [ ] Qualification section appears early
- [ ] Price framed as "The Investment" with ROI math
- [ ] "How to Join" uses simple numbered steps
- [ ] Uses contractions
- [ ] No hype words, no guru energy
- [ ] No fake scarcity or deadlines

---

## Anti-Patterns

**DON'T write like this:**

```
🔥 LAST CHANCE to Join Full-Time Editor! 🔥

Hey there!

I hope this email finds you well! I wanted to reach out because I have an AMAZING opportunity...

**Here's what you'll get:**
- Weekly coaching calls
- Private community access
- Exclusive templates

This is a LIMITED TIME offer and spots are filling up FAST!

Click here to secure your spot before it's too late!

Best regards,
Artem
```

Everything wrong: emoji spam, "hope this finds you well," hype words, bullet points in email, bold in email, fake urgency, generic greeting, formal sign-off, ALL CAPS, no specifics, no real voice.

---

## Examples

### Pre-Call Confirmation Email

**Subject:** just booked — quick video inside
**Preview:** 3 minutes, worth watching before we talk

---

Hey {{contact.first_name}},

You just booked a clarity call with me.

Here's the deal:

It's a quick 15-minute chat where I'm gonna ask you where you are right now, where you're trying to go, and what's holding you back.

I'm not gonna pitch you on anything. We're literally just figuring out if you're a good fit for Full-Time Editor.

Before we talk, I made a short video explaining what to expect and what kind of editor I work with.

→ Watch it here.

It's like 3 minutes. Worth it.

Your call:

{{appointment.start_time}}
{{appointment.meeting_location}}

Looking forward to it.

Artem

---

### Pre-Call Reminder Email (12 Hours Before)

**Subject:** 12 hours from now
**Preview:** one question to sit with before we talk

---

{{contact.first_name}},

Our call is in about 12 hours.

I want you to sit with one question:

What happens if nothing changes?

If you're in the exact same position 6 months from now.

Same income. Same clients. Same frustrations.

→ What does that actually cost you?

I'm not asking this to pressure you.

I'm asking because difficult questions are where the real progress is made.

Come ready to have a real conversation. Not a surface-level one.

That's all I ask.

Your call:

{{appointment.start_time}}
{{appointment.meeting_location}}

Talk soon.

Artem

---

### Reactivation Email

**Subject:** no pressure, just curious
**Preview:** noticed you went quiet

---

{{contact.first_name}},

I noticed you went quiet after we talked.

No pressure. Just curious what happened.

Did something change? Did you decide to go a different direction? Did life just get busy?

I'm not trying to sell you on anything. I'm genuinely asking because I want to know if there's something I missed or could have done better.

If Full-Time Editor isn't for you, that's totally fine. I'd rather know than wonder.

→ Hit reply and let me know where you're at.

Either way, I hope things are going well.

Artem
