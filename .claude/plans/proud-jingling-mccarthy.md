# Plan: Breakthrough Checkout Page + Landing Page Builder Skill

## Part 1: Create The Breakthrough Sales Page in Gamma

### Page Structure (full sales page, ~11 sections/cards)

Inspired by Ollie's RemotePro page structure (progressive reveal, qualification early, investment framing, step-by-step join) but written in Artem's voice — direct, no emoji spam, no hype.

1. **Hero** — Headline + subhead + CTA
   - Headline: Editor → Creative Director transformation angle
   - Subhead: 30 days, 10 spots, $499
   - CTA button → placeholder Stripe link

2. **Problem** — The "Skilled But Stuck" reality
   - You have the skills. You're still at $1-2K/month.
   - The real gap: editor vs creative director mindset
   - Use the $300 vs $1,000 edit example

3. **Who It's For / Not For** — Qualification (placed early, like Ollie's page)
   - For: Editors at $1-2K/month who want creative director skills
   - Not for: Beginners, passive learners, editors who won't submit work

4. **Solution** — What The Breakthrough is
   - Month 1 of Full-Time Editor as a standalone 30-day intensive
   - Not a course — real mentorship with personalized feedback

5. **What's Included** — Full breakdown
   - Onboarding call + custom roadmap
   - 4 weekly edit reviews (personalized Loom feedback)
   - Full curriculum (all 3 pillars)
   - 12 group calls (3x/week) including weekly masterclass
   - Direct Slack access to Artem
   - Community access

6. **The 30-Day Arc** — Timeline/phases (borrowed pattern from Ollie)
   - Week 1: Diagnostic — onboarding, roadmap, first submission
   - Week 2: Focus — targeted feedback on one Core Four element
   - Week 3: Implementation — advanced feedback, positioning
   - Week 4: Decision point — progress review, continue or walk

7. **Social Proof** — Transformation stories
   - Pull from voice-of-customer.md: Marti, Botond, Taylor, Kimi
   - Focus on before/after income + lifestyle changes

8. **The Investment** — Price with ROI framing (borrowed from Ollie)
   - $499 for 30 days
   - Frame: one $1K client covers the investment 2x over
   - Handle price objection directly: "This isn't $3K. This is 30 days to find out what's actually holding you back."

9. **FAQ** — Objection handling
   - How is this different from the full $3K program?
   - What if it doesn't work for my niche?
   - How much time do I need to commit?
   - What happens after 30 days?
   - Is there a refund policy?

10. **How to Join** — Simple steps (borrowed from Ollie)
    - Step 1: Click the link below
    - Step 2: Complete checkout ($499)
    - Step 3: You'll get a Slack invite + onboarding call booking link
    - Step 4: We start

11. **Final CTA** — Close with urgency
    - 10 spots. $499. Doors close Feb 16.
    - CTA button → placeholder Stripe link

### Copy approach
- Use 1m-email-writer principles: direct, conversational, no hype
- Artem's voice but adapted for page format (can use bold/structure since it's not email)
- Lead with the editor → creative director transformation
- Ethical urgency only (real scarcity: 10 spots because Artem personally reviews every edit)

### Execution
- Load `gamma-page-creator` skill
- Load knowledge files for voice + brand
- Write all section copy with `\n---\n` breaks between sections
- Call Gamma API to generate the page
- Return live URL

### Files to reference
- `content/emails/breakthrough-launch/CONTEXT.md` — offer details
- `.claude/knowledge/full-time-editor/feb-2026-the-breakthrough.md` — detailed offer spec
- `.claude/knowledge/full-time-editor/voice-of-customer.md` — social proof + language
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — ICP for targeting
- `.claude/knowledge/artem/voice-of-artem.md` — voice
- `.claude/skills/gamma-page-creator/SKILL.md` — API instructions
- `.claude/skills/1m-email-writer/SKILL.md` — copywriting principles

---

## Part 1 Status: DONE

- Live page: https://gamma.app/docs/wrcak4qipqo7k5r
- Copy file: `content/emails/breakthrough-launch/checkout-page-copy.md`
- Theme used: `va7w64qimm0fof2` (Full-Time Editor custom theme)
- **Needs design tweaks in Gamma editor** (copy is good, design needs polish)
- **Needs:** Replace VSL placeholder with actual Loom/YouTube embed
- **Needs:** Replace `PLACEHOLDER-STRIPE-LINK` with real Stripe payment link

---

## Part 2: Create the `1m-landing-page-builder` Skill

### What it does
Writes high-converting checkout/sales page copy and publishes it to Gamma. Scoped to pages that sell (checkout pages, sales pages).

### Skill file: `.claude/skills/1m-landing-page-builder/SKILL.md`

### Knowledge dependencies (same as 1m-email-writer)
- `.claude/knowledge/artem/voice-of-artem.md`
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md`
- `.claude/knowledge/full-time-editor/voice-of-customer.md`
- `.claude/knowledge/full-time-editor/full-time-editor-manifesto.md`
- Plus any offer-specific context file the user provides

### Inspiration reference
- `.claude/skills/1m-landing-page-builder/inspiration/ollie-black-friday.md` — Ollie's RemotePro sales page (good structural patterns)

### Page templates (3 types)

**1. Short checkout page** — For warm traffic who already know the offer
- Hero (headline + price + CTA)
- What's included (brief)
- CTA

**2. Medium hybrid** — Key benefits + checkout
- Hero + CTA
- What's included
- Who it's for / not for
- FAQ (3-4 questions)
- CTA

**3. Full sales page** — Educates and sells from scratch (what we built for The Breakthrough)
- Hero + CTA
- Problem
- Who it's for / not for (qualification early)
- Solution (what this is)
- What's included
- Timeline/arc
- Social proof
- The Investment (price with ROI framing)
- FAQ
- How to join (simple steps)
- Final CTA

### Copy rules (adapted from 1m-email-writer for page format)

**What stays the same:**
- Voice: direct, conversational, no hype, thinking out loud
- 1-3 sentence paragraphs, one thought per paragraph
- Urgency: ethical only, cost-of-inaction, real scarcity
- No hype words (amazing, incredible, life-changing)
- No guru energy
- Contractions (gonna, wanna, it's)
- Cut aggressively (every draft is too long)
- Conversational interjections as transitions

**What changes for pages:**
- **Bold headers OK** — use for section titles and sub-items (email forbids bold)
- **Structured lists OK** — for "what's included" sections (email forbids bullets)
- **CTA repeated 2-3 times** — hero, after investment section, final section (email has 1 CTA)
- **Visual hierarchy matters** — use H1/H2/H3 to create scannable structure
- **Longer format OK** — pages can be comprehensive; emails must be concise
- **"How to Join" section** — numbered steps to make action feel simple
- **Investment framing section** — ROI math + price objection handling on-page

### Conversion patterns for pages

**Progressive reveal structure:**
Problem → Qualification → Solution → Details → Proof → Price → Action

**Key patterns from Ollie's page worth using:**
- Qualification section early (filter before selling)
- Named frameworks with ™ (builds perceived value)
- "The Investment" framing (not just "Price")
- Stress vs Stretch investment concept (handle price objection)
- Step-by-step "How to Join" (makes action feel simple)
- Testimonials at the end (reinforce after price)

**Key patterns from 1m-email-writer to adapt:**
- "Thinking Out Loud" structure (state → context → reframe → connect → ask)
- "What has actually changed?" reframe
- "What happens if nothing changes?" cost-of-inaction
- The "What If" close for final CTA sections

### Gamma publishing integration

**CRITICAL: Technical lessons learned**

1. **Use Python `requests` library, NOT `curl` or `urllib`**
   - `curl` fails in sandboxed environments due to shell escaping issues
   - `urllib` gets blocked by Cloudflare (error 1010)
   - `requests` works reliably: `pip3 install requests` or use `source ~/myenv/bin/activate`

2. **API returns 201 (not 200) on successful generation start**
   - Check for `r.status_code in (200, 201)`, not just 200

3. **Poll timing: 10 seconds between polls, expect ~60-70 seconds total**
   - Generation took 7 polls × 10 seconds = ~70 seconds for a full sales page

4. **Key API parameters:**
   ```json
   {
     "textMode": "preserve",
     "format": "webpage",
     "cardSplit": "inputTextBreaks",
     "imageOptions": {"source": "noImages"},
     "sharingOptions": {"externalAccess": "view"}
   }
   ```

5. **Section breaks:** Use `\n---\n` in inputText to control card splits

6. **Custom themes:** List with GET `/v1.0/themes`, pass `themeId` in generation request
   - Artem's FTE theme: `va7w64qimm0fof2`

7. **API key:** Stored in `~/.zshrc` as `GAMMA_API_KEY` but in Python scripts, hardcode or read from env since `source ~/.zshrc` doesn't always work in subprocesses

8. **Working Python publish script pattern:**
   ```python
   import requests, time
   API_KEY = "sk-gamma-..."  # or os.environ["GAMMA_API_KEY"]
   HEADERS = {"Content-Type": "application/json", "X-API-KEY": API_KEY}

   r = requests.post("https://public-api.gamma.app/v1.0/generations", json=payload, headers=HEADERS)
   gen_id = r.json()["generationId"]

   for i in range(20):
       time.sleep(10)
       poll = requests.get(f"https://public-api.gamma.app/v1.0/generations/{gen_id}", headers=HEADERS)
       data = poll.json()
       if data["status"] == "completed":
           print(data["gammaUrl"])
           break
   ```

### Process (what the skill should do step by step)

1. **Gather inputs:** Offer details, page type (short/medium/full), payment link, voice files
2. **Determine template:** Based on page type selection
3. **Load knowledge:** Voice files + ICP + voice of customer + offer context
4. **Write copy section by section** with `---` breaks between sections
5. **Show copy to user for approval** before publishing
6. **Publish to Gamma** using the Python requests pattern above
7. **Return live URL** + summary of what's on the page

---

## Verification
- Skill file exists at `.claude/skills/1m-landing-page-builder/SKILL.md`
- Skill follows same format as existing skills (frontmatter, sections, examples)
- Gamma publishing code uses `requests` library (not curl/urllib)
- Handles 201 status code correctly
- Includes all 3 page templates
- References correct knowledge dependencies
- Inspiration file preserved at `.claude/skills/1m-landing-page-builder/inspiration/ollie-black-friday.md`
