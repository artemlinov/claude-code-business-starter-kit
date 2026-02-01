---
name: gamma-page-creator
description: Create pages and checkout pages directly in Gamma via their API. USE WHEN user says 'create a gamma page', 'build checkout page', 'gamma checkout', 'create page in gamma', 'gamma landing page', or any request to create a live page in Gamma.
---

# Gamma Page Creator

Create live Gamma webpages via the Gamma Generate API. Instead of outputting copy for the user to manually paste, this skill builds the page directly in Gamma and returns the live URL.

---

## Prerequisites

- Gamma paid plan (Pro, Ultra, Team, or Business)
- API key stored as environment variable: `GAMMA_API_KEY`
  - Get your key from: Gamma account settings
  - Set it: `export GAMMA_API_KEY=sk-gamma-xxxxxxxxxx`

---

## How It Works

### Step 1: Gather Context

Load relevant knowledge files and offer context for the page being created. For checkout/sales pages, this typically includes:

- The offer details (price, what's included, who it's for)
- Brand voice files from `.claude/knowledge/`
- Any specific copy the user wants on the page

### Step 2: Write the Page Copy

Structure the page content using `\n---\n` as section breaks between cards. Each section between breaks becomes a separate card/section on the Gamma page.

Example structure for a checkout page:

```
[Hero headline + subheadline]
---
[What's included - full breakdown]
---
[Who this is for / Who this is NOT for]
---
[Social proof or testimonials if available]
---
[Price + CTA with payment link]
```

### Step 3: Call the Gamma API

Use this exact curl command structure:

```bash
# Step 1: Start generation
RESPONSE=$(curl -s --request POST \
  --url https://public-api.gamma.app/v1.0/generations \
  --header 'Content-Type: application/json' \
  --header "X-API-KEY: $GAMMA_API_KEY" \
  --data '{
    "inputText": "<PAGE_COPY_WITH_SECTION_BREAKS>",
    "textMode": "preserve",
    "format": "webpage",
    "cardSplit": "inputTextBreaks",
    "additionalInstructions": "<DESIGN_INSTRUCTIONS>",
    "imageOptions": {
      "source": "noImages"
    },
    "sharingOptions": {
      "externalAccess": "view"
    }
  }')

GENERATION_ID=$(echo $RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['generationId'])")
echo "Generation started: $GENERATION_ID"
```

```bash
# Step 2: Poll for completion (wait a few seconds between checks)
sleep 10
STATUS_RESPONSE=$(curl -s --request GET \
  --url "https://public-api.gamma.app/v1.0/generations/$GENERATION_ID" \
  --header "X-API-KEY: $GAMMA_API_KEY")
echo $STATUS_RESPONSE | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Status: {d[\"status\"]}'); print(f'URL: {d.get(\"gammaUrl\", \"still generating...\")}')"
```

If status is still `pending`, wait another 10 seconds and poll again. Repeat until `completed` or `failed`.

### Step 4: Return the URL

Once the generation completes, share the `gammaUrl` with the user. This is the live Gamma webpage they can view, edit, and share.

---

## API Parameters Reference

| Parameter | Value | Why |
|-----------|-------|-----|
| `format` | `"webpage"` | Creates a webpage (not presentation/doc) |
| `textMode` | `"preserve"` | Keeps our exact copy, doesn't rewrite |
| `cardSplit` | `"inputTextBreaks"` | We control sections with `\n---\n` |
| `imageOptions.source` | `"noImages"` | Clean checkout page (or use `"aiGenerated"` if user wants visuals) |
| `sharingOptions.externalAccess` | `"view"` | Anyone with link can view |
| `additionalInstructions` | varies | Design direction (e.g., "Clean, modern sales page. Bold headline. Clear CTA buttons.") |
| `themeId` | optional | Specific Gamma theme. Omit for default. |
| `numCards` | optional | Number of sections. Omit when using `inputTextBreaks`. |

---

## Optional: Add Theme

To list available themes and pick one:

```bash
curl -s --request GET \
  --url https://public-api.gamma.app/v1.0/themes \
  --header "X-API-KEY: $GAMMA_API_KEY" | python3 -c "import sys,json; [print(f'{t[\"id\"]}: {t[\"name\"]}') for t in json.load(sys.stdin)['themes']]"
```

Then pass the `themeId` in the generation request.

---

## Error Handling

- **401**: Invalid API key. Check `GAMMA_API_KEY` is set correctly.
- **400**: Input validation error. Check the response message for details.
- **422**: Generation failed. Usually a content issue. Check the error message.
- **429**: Rate limited. Wait and retry.

---

## Output

After successful creation, confirm to the user with:
- The live Gamma URL
- A summary of what's on the page
- Reminder they can edit the page directly in Gamma's editor
