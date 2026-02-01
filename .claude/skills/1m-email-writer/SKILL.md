---
name: 1m-email-writer
description: Write high-converting sales emails for Full-Time Editor. USE WHEN user says 'write an email', 'email sequence', 'nurture sequence', 'pre-call emails', 'post-call follow-up', 'reminder email', 'reactivation email', 'launch email', 'sales email', or any request for email copy that isn't a newsletter. This skill handles all sales-related email communications including pre-call nurture sequences, post-call follow-ups, reactivation sequences, and launch emails.
---

# $1M Email Writer

Write sales emails that convert leads into Full-Time Editor customers. Every email sounds like Artem thinking out loud — direct, warm, specific.

---

## Knowledge Dependencies

Before writing, load these files:

- `.claude/knowledge/artem/voice-of-artem.md` — Core voice (shared across all formats)
- `.claude/knowledge/artem/voice-of-artem-email.md` — Email-specific patterns
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Who we're speaking to
- `.claude/knowledge/full-time-editor/voice-of-customer.md` — Their exact language
- `.claude/knowledge/full-time-editor/full-time-editor-manifesto.md` — Brand philosophy

---

## Inputs

Gather before writing:

1. **Email type:** Pre-call nurture, post-call follow-up, reactivation, launch, reminder
2. **Position in sequence:** First email, follow-up, or standalone
3. **Reader's state:** What do they know? What just happened? What's next?
4. **Primary action:** What's the ONE thing they should do after reading?
5. **Available personalization tokens:** `{{contact.first_name}}`, `{{appointment.start_time}}`, etc.

If any input is missing, ask before writing.

---

## Process

### Step 1: Determine Email Type

| Type | Tone | Key Pattern |
|------|------|-------------|
| Pre-call nurture | Warm, anticipatory | Build trust before the call |
| Post-call follow-up | Direct, momentum | Maintain energy from call |
| Reactivation | Curious, no pressure | Re-engage without guilt |
| Launch | Urgent (real), excited | Time-bound opportunity |
| Reminder | Brief, helpful | Simple nudge |

### Step 2: Apply Structural Rules

**Greetings:**
- First email in sequence: `Hey {{name}},`
- Follow-up emails: `{{name}},` (no "Hey")

**Paragraphs:**
- 1-3 sentences max per paragraph
- One thought per paragraph
- Generous whitespace

**Lists:**
- 3-5 items max
- One item per line
- NO bullet points or dashes — just line breaks

**Emphasis:**
- Use `→` before the primary CTA (ONE per email max)
- NO bold in email body
- Use spacing for emphasis instead

**Sign-offs:**
- In sequences: "Talk [day of week]." where [day] = the weekday the next email sends (e.g. "Talk Tuesday.")
- Standalone emails: "Looking forward to it." / "Talk soon." / "See you tomorrow."
- Always just "Artem" (no dash)

### Step 2b: Apply Rhythm & Pacing Rules

These are critical. They're the difference between "good copy" and "sounds like Artem."

1. **One sentence per line.** Break compound sentences apart. Each thought gets its own line.
2. **Use ellipsis (...)** for trailing thoughts. 1-2 per email max. Creates a conversational pause.
3. **Use conversational interjections as transitions:** "The second type though?" / "Solid, right??" / "And here's the craziest part:" — these replace formal transitions.
4. **Colons before lists/explanations.** "Here's what I mean:" not "Here's what I mean."
5. **Never echo subject/preview in the opening.** Jump straight into content.
6. **Cut aggressively.** Remove setup sentences, transition phrases, repeated conclusions, anything the reader can infer. Every draft is too long on the first pass.
7. **Double question marks** ("??") for rhetorical emphasis.

### Step 3: Apply Conversion Patterns

**The Thinking Out Loud Structure:**
1. State something direct
2. Add context or a question
3. Answer or reframe
4. Connect to the reader
5. Clear ask

**Reframes That Convert:**

*"What has actually changed?"*
```
What has actually changed in the past 6 months?

Not what you've tried. Not what you've learned. What has actually changed in your income, your clients, your situation?
```

*"What happens if nothing changes?"*
```
What happens if nothing changes?

If you're in the exact same position 6 months from now.

Same income. Same clients. Same frustrations.

→ What does that actually cost you?
```

*"Difficult questions = real progress"*
```
I'm not asking this to pressure you.

I'm asking because difficult questions are where the real progress is made.
```

### Step 4: Apply Urgency (Ethically)

Use cost-of-inaction urgency, NOT artificial scarcity:

✓ "What's another 6 months of being stuck costing you?"
✓ "The sooner you start, the sooner you're at $5K/month"
✓ "If you're gonna do this eventually, might as well start now"

✗ "Only 3 spots left!" (unless actually true)
✗ "This offer expires tonight!" (fake deadlines)
✗ Pressure tactics

**Rolling cohort urgency (if applicable):**
```
If you sign up today, I can get you in with our next group that kicks off on Monday.

Otherwise you'll have to wait until the next one.
```

### Step 5: Write the Hook (Subject Line)

**Hook Formats for Subject Lines:**

| Format | Example |
|--------|---------|
| Direct question | "Quick question before our call" |
| Specific number | "The $2K/video question" |
| Curiosity gap | "One thing I forgot to mention" |
| Time-based | "12 hours from now" |
| Pattern interrupt | "This might sound weird" |

Subject lines should be:
- 4-8 words
- Lowercase (unless proper noun)
- No periods
- Personal, not promotional

### Step 6: Write the Preview Text

Preview text (the snippet shown after the subject line in inbox):
- 40-90 characters
- Complements subject line (doesn't repeat it)
- Creates curiosity or continues the thought
- Written as a fragment, not a complete sentence

---

## Output

Every email output includes:

```
**Subject:** [subject line]
**Preview:** [preview text]

---

[Email body]
```

---

## Quality Checklist

Before delivering, verify:

- [ ] Sounds like Artem wrote it (not a marketer)
- [ ] ONE clear ask per email
- [ ] No bullet points or bold text
- [ ] 1-3 sentences per paragraph
- [ ] One sentence per line — no compound sentences sharing a line
- [ ] Greeting matches position in sequence
- [ ] Arrow (→) used only once, before primary CTA
- [ ] Sign-off matches tone
- [ ] Subject line is 4-8 words, lowercase
- [ ] Preview text complements (not repeats) subject
- [ ] Opening lines do NOT echo the subject line or preview text
- [ ] Uses contractions: gonna, wanna, it's
- [ ] Uses colons (not periods) before lists and explanations
- [ ] Includes conversational interjections as transitions ("Solid, right??", "And here's the thing:")
- [ ] Draft has been cut — no unnecessary setup, transitions, or repeated conclusions
- [ ] No hype words: amazing, incredible, life-changing
- [ ] No guru energy

---

## Examples

### Pre-Call Confirmation (First Email)

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

### Pre-Call Reminder (12 Hours Before)

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

---

## Anti-Patterns

**DON'T write like this:**

```
Subject: 🔥 LAST CHANCE to Join Full-Time Editor! 🔥

Hey there!

I hope this email finds you well! I wanted to reach out because I have an AMAZING opportunity for you...

**Here's what you'll get:**
- Weekly coaching calls
- Private community access
- Exclusive templates

This is a LIMITED TIME offer and spots are filling up FAST!

Click here to secure your spot before it's too late!

Best regards,
Artem
```

Everything wrong:
- Emoji spam
- "Hope this email finds you well"
- Hype words (AMAZING, LIMITED TIME, FAST)
- Bullet points
- Bold text
- Fake urgency
- Generic greeting
- Formal sign-off

---

## Sequence Writing Rules

When writing multi-email sequences (3+ emails), follow these additional rules:

### Trust the Sequence
Don't repeat offer details that were covered in earlier emails. If Email 2 listed everything included, Email 4 shouldn't list it again. Each email should add NEW information or a new angle — not rehash what came before.

### Funnel to Landing Pages
When a checkout or landing page exists, make that the primary CTA. Don't use "reply and I'll send the link" when the link already exists. "Reply if you have questions" works as a secondary line, but the arrow (→) should point to the page.

### Name Programs Fully
First mention of a program's price in any email should use the full program name. "Full-Time Editor is $3K" not "The full program is $3K." After the first mention, shorthand is fine.
