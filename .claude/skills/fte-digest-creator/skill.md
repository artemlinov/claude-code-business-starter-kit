---
name: fte-digest-creator
description: Create the weekly FTE Digest presentation and Slack message. USE WHEN user says 'create this week's digest', 'FTE digest', 'weekly digest', 'digest for this week', or provides weekly update info for the Full-Time Editor community.
---

# FTE Digest Creator

Create the weekly Full-Time Editor Digest as a Gamma presentation + Slack message. The digest is a set of Loom talking-point slides, NOT standalone content.

---

## Prerequisites

- Gamma API key stored as `GAMMA_API_KEY`
- User provides this week's updates (masterclass topic, announcements, community notes, etc.)

---

## Reference Material

Before creating, load:
- `.claude/knowledge/artem/voice-of-artem.md` for tone
- `.claude/knowledge/full-time-editor/fte-framework-definitions.md` if referencing a framework
- Past digests in `.claude/knowledge/misc/fte-digests/` for style reference

---

## Style Rules (from past digests)

### These are Loom talking points, NOT standalone content.

Artem records a Loom walking through the slides. The slides on their own don't need to make complete sense. They're visual cues for his Loom recording.

### Slide structure:
- **Slide 1 (ALWAYS):** Cover slide. "FTE Digest" + date. Nothing else.
- **Middle slides:** One topic per slide. Bold headline does the heavy lifting. Body is short bullet points (talking points).
- **Last slide (ALWAYS):** Weekly wins reminder. Single bold line like "Looking forward to your Weekly Wins" or "Submit your #weekly-wins as always"

### Copy style:
- Ultra casual. Shorthand is fine: "Pls pls", "Lmk", "Gonna", "goated", "crushing it"
- Bold headlines are punchy and short (2-6 words max)
- Body bullets are brief talking points, not full sentences
- 3 bullets max per slide
- One idea per slide. Never cram two topics on one slide.
- Emojis are used sparingly but naturally (trophy, pin, heart)
- Use Artem's voice: direct, warm, casual, no guru energy

### Common slide types (use as needed):
- **Masterclass slide:** "This Week's Masterclass:" as subheading, then big bold technique/topic name, pin emoji + "Wednesday 11AM GMT", 2-3 bullet talking points
- **Community update slide:** Bold headline + short bullets celebrating wins or welcoming new members
- **Programme update slide:** Bold headline about what's changing + short bullets explaining why
- **Ask/CTA slide:** Bold headline with the ask + embedded link or short casual line

### What NOT to do:
- No long paragraphs
- No formal language
- No "Dear members" or corporate tone
- No more than 3-4 bullets per slide
- Don't try to make slides self-explanatory. They're Loom backdrops.

---

## Step 1: Gather Info from User

Ask the user what's happening this week. Common items:
- Wednesday masterclass topic
- Community updates / shoutouts
- Programme changes
- Any asks (surveys, feedback, etc.)
- Any links to include

---

## Step 2: Draft the Slide Copy

Write the copy using `\n---\n` as section breaks between slides. Each section = one slide.

Structure each slide as:
```
# Bold Headline

Optional subheading or emoji line

- Bullet talking point
- Bullet talking point
```

Always start with the cover slide and end with weekly wins.

---

## Step 3: Draft the Slack Message

Create the accompanying Slack message using this exact format:

```
@channel FTE Digest [DATE] :headphones:
→  [LOOM LINK or placeholder]

:one: [First topic - one line]
:two: [Second topic - one line]
:three: [Third topic - one line]
```

Leave the Loom link as a placeholder if user hasn't recorded yet. Number emojis match the number of topics (use :one:, :two:, :three:, :four: etc.)

---

## Step 4: Create the Gamma Presentation

Use this exact curl structure:

```bash
RESPONSE=$(curl -s --request POST \
  --url https://public-api.gamma.app/v1.0/generations \
  --header 'Content-Type: application/json' \
  --header "X-API-KEY: $GAMMA_API_KEY" \
  --data '{
    "inputText": "<SLIDE_COPY_WITH_SECTION_BREAKS>",
    "textMode": "preserve",
    "format": "presentation",
    "cardSplit": "inputTextBreaks",
    "additionalInstructions": "Light grey background. Bold black headlines. Green accent for the date on the cover slide. Minimal, clean design. Line-art style illustrations. These are Loom talking-point slides, keep text large and scannable.",
    "imageOptions": {
      "source": "aiGenerated"
    },
    "sharingOptions": {
      "externalAccess": "view"
    }
  }')

GENERATION_ID=$(echo $RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['generationId'])")
echo "Generation started: $GENERATION_ID"
```

Then poll for completion:

```bash
sleep 15
STATUS_RESPONSE=$(curl -s --request GET \
  --url "https://public-api.gamma.app/v1.0/generations/$GENERATION_ID" \
  --header "X-API-KEY: $GAMMA_API_KEY")
echo $STATUS_RESPONSE | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Status: {d[\"status\"]}'); print(f'URL: {d.get(\"gammaUrl\", \"still generating...\")}')"
```

If still pending, wait 15 seconds and poll again. Repeat until completed or failed.

---

## Step 5: Output

Save the Slack message to `content/digests/fte-digest-[DATE].md` with both the Slack message and Gamma URL.

Present to the user:
1. The live Gamma presentation URL
2. The Slack message (ready to copy-paste)
3. Reminder they can edit slides directly in Gamma before recording their Loom

---

## Example Output (Feb 2, 2026)

### Gamma slide copy:

```
# FTE Digest
## Feb 2, 2026

---

# FTE Revamp is coming
# I need YOUR help!!!

Pls pls complete the typeform survey I linked in the Slack message. It makes a huge difference

---

# This Week's Masterclass:
# The Blockout Graphic™

📍 Wednesday 11AM GMT

---

# Looking forward to your Weekly Wins
```

### Slack message:

```
@channel FTE Digest 2nd February :headphones:
→  https://www.loom.com/share/xxxxx

:one: Feedback Survey – I need your help shaping the future of FTE. Huge revamp coming. Fill this out: https://full-time-editor.typeform.com/to/yfPJpctX
:two: This Wednesday's Masterclass: The Blockout Graphic™
:three: Submit your #weekly-wins as always
```