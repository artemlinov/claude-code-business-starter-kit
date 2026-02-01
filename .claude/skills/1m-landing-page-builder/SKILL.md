---
name: 1m-landing-page-builder
description: Write high-converting checkout and sales page copy, then publish to Gamma. USE WHEN user says 'build a sales page', 'create checkout page', 'landing page', 'sales page copy', 'build a page for [offer]', 'offer doc', 'build an offer document', or any request for page copy that sells an offer. Handles short checkout pages, medium hybrid pages, full sales pages, and long-form offer docs.
---

# $1M Landing Page Builder

Write sales page copy that converts and publish it live to Gamma. Every page sounds like Artem — direct, warm, specific. No hype, no guru energy.

---

## Knowledge Dependencies

Before writing, load these files:

- `.claude/knowledge/artem/voice-of-artem.md` — Core voice
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Who we're speaking to
- `.claude/knowledge/full-time-editor/voice-of-customer.md` — Their exact language
- `.claude/knowledge/full-time-editor/full-time-editor-manifesto.md` — Brand philosophy
- Plus any **offer-specific context file** the user provides (e.g. `CONTEXT.md` for the offer)

**Inspiration references:**
- `.claude/skills/1m-landing-page-builder/inspiration/ollie-black-friday.md` — sales page structural patterns
- `.claude/skills/1m-landing-page-builder/inspiration/ollie-remotepro-offer-doc.md` — offer doc structural patterns (detailed section-by-section breakdown)

---

## Inputs

Gather before writing:

1. **Offer details:** What's being sold, what's included, price, timeline
2. **Page type:** Short checkout, medium hybrid, full sales page, or offer doc
3. **Payment link:** Stripe link or placeholder
4. **Target audience:** Who this page is for (load ICP if FTE)
5. **Social proof:** Testimonials or transformation stories (if available)
6. **Design notes:** Any specific visual direction for Gamma

If any input is missing, ask before writing.

---

## Process

### Step 1: Determine Page Type

| Type | When to use | Sections |
|------|-------------|----------|
| **Short checkout** | Warm traffic who already know the offer | Hero → What's Included → CTA |
| **Medium hybrid** | Some awareness, needs key benefits + checkout | Hero → What's Included → Who It's For/Not For → FAQ → CTA |
| **Full sales page** | Cold or lukewarm traffic, educates and sells from scratch | Hero → Problem → Qualification → Solution → What's Included → Timeline → Social Proof → Investment → FAQ → How to Join → Final CTA |
| **Offer doc** | Personal invitation format, longest form, narrative-driven with embedded proof throughout | Hero Invitation → What Is This? → Qualification → Unique Mechanism → Focus Areas → Detailed Outcomes → Program Summary → Timeline → The Effort → FAQ → Investment (Stress vs Stretch) → Guarantee → How to Join → Testimonials |

### Step 2: Apply Copy Rules

**What stays the same from email writing:**
- Voice: direct, conversational, no hype, thinking out loud
- 1-3 sentence paragraphs, one thought per paragraph
- Urgency: ethical only, cost-of-inaction, real scarcity
- No hype words (amazing, incredible, life-changing)
- No guru energy
- Contractions (gonna, wanna, it's)
- Cut aggressively — every draft is too long
- Conversational interjections as transitions

**What changes for pages:**
- **Bold headers OK** — use for section titles and sub-items
- **Structured lists OK** — for "what's included" sections
- **CTA repeated 2-3 times** — hero, after investment section, final section
- **Visual hierarchy** — use H1/H2/H3 to create scannable structure
- **Longer format OK** — pages can be comprehensive
- **"How to Join" section** — numbered steps to make action feel simple
- **Investment framing section** — ROI math + price objection handling on-page

### Step 3: Apply Conversion Patterns

**Progressive reveal structure:**
Problem → Qualification → Solution → Details → Proof → Price → Action

**Key patterns to use:**

- **Qualification section early** — filter before selling. "This is for X. This is NOT for Y."
- **Named frameworks with ™** — builds perceived value
- **"The Investment" framing** — not just "Price"
- **Stress vs Stretch concept** — handle price objection by reframing what "expensive" means
- **Step-by-step "How to Join"** — makes action feel simple (3-4 numbered steps)
- **Testimonials after price** — reinforce after the investment section

**Adapted from email writer:**
- "Thinking Out Loud" structure (state → context → reframe → connect → ask)
- "What has actually changed?" reframe
- "What happens if nothing changes?" cost-of-inaction
- The "What If" close for final CTA sections

### Step 4: Apply Urgency (Ethically)

Use cost-of-inaction urgency, NOT artificial scarcity:

✓ "What's another 6 months of being stuck costing you?"
✓ Real scarcity when true (e.g., "10 spots because I personally review every edit")
✓ Real deadlines when true (e.g., "Doors close Feb 16")

✗ Fake scarcity or fake deadlines
✗ Pressure tactics
✗ Hype language

### Step 5: Write Copy Section by Section

Write each section with `\n---\n` breaks between them. Each break becomes a separate card in Gamma.

**Full sales page template:**

```
[H1 Headline]
[Subheadline — who it's for + key transformation + price/timeline]

[CTA Button → payment link]
---
[H2 The Problem]
[2-3 paragraphs identifying the core pain point]
[Use specific examples and numbers]
---
[H2 Who This Is For]
[Who it's for — 3-4 bullet points]

[H2 Who This Is NOT For]
[Who it's not for — 3-4 bullet points]
---
[H2 What [Program Name] Is]
[2-3 paragraphs explaining the solution]
[Position against alternatives]
---
[H2 What's Included]
[Full breakdown with bold item names]
[Each item: name + 1-line description]
---
[H2 The 30-Day Arc / Timeline]
[Week-by-week or phase-by-phase breakdown]
---
[H2 Results / Social Proof]
[Testimonials with before/after]
[Real names, real numbers]
---
[H2 The Investment]
[$X for Y]
[ROI math: "One [outcome] covers the investment X times over"]
[Handle price objection directly]

[CTA Button → payment link]
---
[H2 Common Questions]
[Q&A format, 4-6 questions]
[Handle real objections, not softballs]
---
[H2 How to Join]
Step 1: [action]
Step 2: [action]
Step 3: [action]
Step 4: [action]
---
[Final headline — urgency + CTA]
[1-2 lines reinforcing scarcity/deadline]

[CTA Button → payment link]
```

**Offer doc template:**

The offer doc is the longest format — it reads like a personal invitation, not a landing page. Every section ends with a transition hook teasing the next section. Social proof is scattered throughout (not just one section). See `inspiration/ollie-remotepro-offer-doc.md` for the full structural reference.

```
[H1 Your invitation to join [Program Name].....]
[Urgency note if real: "X spots only" or "Doors close [date]"]
[Author byline]

[CTA Button → payment link]
---
[H2 What is [Program Name]?]
[One-line positioning: "[Program] is the [category] at [brand]."]
[2-3 paragraphs on why now — what's changed in the market]
[Short conversational lines building tension]
[Bold reframe statement with specific numbers]
[Social proof screenshots scattered here]

[Transition: "First, let's make sure reading this is worth your time... Here's who this is for.... ↓"]
---
[H2 Who this is and isn't for...]

**Who this isn't for:**
[3-4 bullet points filtering out wrong fits]

**Who this is for:**
[Bold keyword: description format, 5-7 items]
[e.g. "**Freedom:** you value freedom over everything else"]

[Transition: "If you're still reading, you align with [Program]... keep reading..."]
[Transition hook: "Introducing [your secret weapon / unique mechanism].... ↓"]
---
[H2 Introducing [Named Framework/Methodology]]
[Problem it solves: why traditional approaches fail]
[How your mechanism is different]
[Sub-components explained]
[Screenshots/visuals of the system if available]

[Transition hook: "Here's what we're gonna focus on when we work together.... ↓"]
---
[H2 What are we focusing on?]
[3 core bottlenecks/problems identified]
[3 pillars/focus areas that address them]
[Each pillar: **Bold Name** — one-line description]
[Social proof screenshot between sections]

[Transition hook: "What are the outcomes of working together? ↓"]
---
[H2 The Outcomes]
[Overview paragraph: "We'll [add/build/implement] these X core systems..."]
[Summary list of outcomes with named frameworks]

[H3 1. [PILLAR NAME] — [Framework Name]]
[2-3 paragraphs explaining what it is and why it matters]
[Outcome line: "Outcome: [specific result]"]

[H3 2. [PILLAR NAME] — [Framework Name]]
[2-3 paragraphs]
[Authority quotes if relevant]
[Outcome line]

[H3 3. [PILLAR NAME] — [Framework Name]]
[2-3 paragraphs]
[Outcome line]

[Result screenshots — income numbers, wins from members]
[Transition hook: "Time to be one of our next success stories? ↓"]
---
[H2 [Program Name] — What to Expect]
[Recap: "Setting up these systems is the foundation..."]
[Bold promise: "No more [pain point]. Just [simple outcome]."]
[Case study framing: "I want to create new case studies, so I'll work closely with you..."]
[Personal commitment statement]
[Social proof: Slack wins, community screenshots]

[Transition hook: "Here's the timeline to expect.... ↓"]
---
[H2 The Timeline]
["This is a [duration] program"]

**Phase 1: (weeks X-Y)**
[What happens first — onboarding, kickoff, initial builds]
[Bullet list of deliverables]

**Phase 2: (weeks X-Y)**
[Core implementation phase]
[What they get access to — community, calls, resources]

**Phase 3: (weeks X-Y)**
[Scale/refine phase]
[KPI tracking, optimization]

[Community screenshot]
[Transition hook: "Here's how easy it will be..... ↓"]
---
[H2 The Effort]
[Honest reframe of "hard work"]
[Metaphor for effort (e.g. airplane takeoff)]
[Specific time commitment: "X hours/week"]
[Bold promise tied to commitment]
[Filter: "If that sounds like too much, this isn't for you. Fair enough?"]
[Value question: "What is it worth to learn the skills to make $X per year?"]
---
[H2 FAQ]
[Embedded video if available, OR written Q&A format]
[4-6 real objections, not softballs]
---
[H2 The Investment]
[Framing: "introductory offer" or "founding member" if true]
[Cap: "X spots total" if real]

**Payment options:**
1. [Option A: X monthly payments of $Y ($Z total)]
2. [Option B: X monthly payments of $Y ($Z total)]
3. [Option C: Pay in full, save X% ($Y)]

[ROI framing: "Your first X clients covers the entire investment"]
[Speed: "Most members make it back within X days"]
[10x framing: "The intended outcome is you more than Xx your investment"]

**"I can't afford it..."**
[Stress vs Stretch Investment concept:]
- **Stress Investment** — if it keeps you up at night, don't do it
- **Stretch Investment** — something that stretches you and forces you to level up

[Personal story about stretch investments]
[Long-term framing: "I want to work with you for years"]

[CTA Button → payment link]
---
[H2 Our Guarantee]
[Reframe: "a guarantee that's uncommon in this space"]
[The guarantee: "if you don't do the work, you won't get the outcome"]
[Reframe who needs guarantees: "People that need a guarantee are looking for someone else to save them."]
[Close: "You don't strike me as that kind of person, right?"]
---
[H2 How to Join]
Step 1: [Commitment statement — "Draw a line in the sand"]
Step 2: [Checkout via payment link] [CTA Button]
Step 3: [Enrollment — what happens after payment]
Step 4: [Kickoff — schedule first call]
Step 5: [We build together]

[Close: "Sound good? Let's do this."]
---
[H2 Client Testimonials]
[Embedded video testimonials if available]
[OR written testimonials with real names, real numbers, before/after]
[4-6 testimonials]
```

### Step 6: Show Copy to User for Approval

Present the full copy to the user before publishing. Ask for approval or revisions.

### Step 7: Publish to Gamma

**CRITICAL: Use Python `requests` library — NOT curl or urllib.**

curl fails in sandboxed environments. urllib gets blocked by Cloudflare (error 1010). Only `requests` works reliably.

```python
import requests, time, os

API_KEY = os.environ.get("GAMMA_API_KEY")
HEADERS = {"Content-Type": "application/json", "X-API-KEY": API_KEY}

payload = {
    "inputText": "<FULL_PAGE_COPY_WITH_BREAKS>",
    "textMode": "preserve",
    "format": "webpage",
    "cardSplit": "inputTextBreaks",
    "additionalInstructions": "<DESIGN_DIRECTION>",
    "imageOptions": {"source": "noImages"},
    "sharingOptions": {"externalAccess": "view"},
    "themeId": "va7w64qimm0fof2"  # FTE custom theme (omit for other brands)
}

# Start generation
r = requests.post("https://public-api.gamma.app/v1.0/generations", json=payload, headers=HEADERS)
if r.status_code not in (200, 201):
    print(f"Error: {r.status_code} - {r.text}")
else:
    gen_id = r.json()["generationId"]
    print(f"Generation started: {gen_id}")

    # Poll for completion (~70 seconds for full page)
    for i in range(20):
        time.sleep(10)
        poll = requests.get(f"https://public-api.gamma.app/v1.0/generations/{gen_id}", headers=HEADERS)
        data = poll.json()
        print(f"Poll {i+1}: {data['status']}")
        if data["status"] == "completed":
            print(f"Live URL: {data['gammaUrl']}")
            break
        elif data["status"] == "failed":
            print(f"Failed: {data}")
            break
```

**Key API details:**
- Returns **201** (not 200) on success — check for both
- Poll every **10 seconds**, expect ~60-70 seconds total for a full page
- `textMode: "preserve"` keeps our exact copy
- `cardSplit: "inputTextBreaks"` splits on our `---` breaks
- `themeId: "va7w64qimm0fof2"` is the FTE custom theme

---

## Output

After successful creation, provide:

1. **Copy file** saved to `content/[project]/[page-name]-copy.md`
2. **Live Gamma URL**
3. **Summary** of what's on the page
4. **Reminders:**
   - Edit design directly in Gamma's editor
   - Replace any placeholder links with real payment links
   - Add video embeds if needed

---

## Quality Checklist

Before publishing, verify:

- [ ] Sounds like Artem wrote it (not a marketer)
- [ ] Clear CTA repeated 2-3 times throughout the page
- [ ] Uses bold headers and structured lists (page format, not email)
- [ ] 1-3 sentences per paragraph
- [ ] Qualification section appears early (before selling)
- [ ] Price is framed as "The Investment" with ROI math
- [ ] "How to Join" uses simple numbered steps
- [ ] Uses contractions: gonna, wanna, it's
- [ ] Conversational interjections as transitions
- [ ] Draft has been cut — no filler, no fluff
- [ ] No hype words: amazing, incredible, life-changing
- [ ] No guru energy
- [ ] No fake scarcity or fake deadlines
- [ ] All payment links are included (or clearly marked as placeholders)
- [ ] Section breaks (`---`) are correctly placed for Gamma card splits

---

## Anti-Patterns

**DON'T write pages like this:**

```
🚀 TRANSFORM YOUR LIFE IN 30 DAYS! 🚀

Are you READY to unlock your FULL POTENTIAL??

Join our EXCLUSIVE program and get:
• UNLIMITED access to our PREMIUM content
• LIVE coaching from industry EXPERTS
• A SUPPORTIVE community of like-minded individuals

⚡ LIMITED SPOTS AVAILABLE — ACT NOW! ⚡

Regular price: $999  TODAY ONLY: $499!!
```

Everything wrong:
- Emoji spam
- ALL CAPS for emphasis
- Hype words (transform, unlock, full potential, exclusive, premium)
- Generic language (like-minded individuals, industry experts)
- Fake urgency (TODAY ONLY)
- Crossed-out price trick
- No specifics, no real voice
