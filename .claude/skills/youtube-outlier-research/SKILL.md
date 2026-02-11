---
name: youtube-outlier-research
description: Find YouTube outlier videos that massively outperform their channel's average. USE WHEN user says 'find outlier videos', 'youtube outlier research', 'viral videos in niche', 'outlier videos about', 'research youtube niche', 'find top performing videos', 'what videos are going viral', 'youtube competitor research'.
---

# YouTube Outlier Research

Finds videos that massively outperformed their channel's typical views — the same "outlier detection" feature from vidIQ, powered by the free YouTube Data API.

**How it works:** Searches for channels in a niche, pulls their recent videos, calculates each channel's median views, and scores every video as `views / median`. A 48x outlier means a video got 48 times more views than that channel normally gets.

---

## When to Use

- User wants to find outlier/viral videos in a niche
- User says "find outlier videos about [topic]"
- User wants to research what's working on YouTube in a specific topic
- User says "youtube research" or "competitor research"
- User wants video ideas based on what's performing well

---

## Output

**Type:** research
**Location:** `research/youtube-outliers/[topic]/`
**Files produced:**
- `report.md` - Formatted outlier report with analysis

---

## Prerequisites

### YouTube Data API Key (one-time setup)

The script needs a free YouTube Data API v3 key. If not set up yet, walk the user through these steps:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Select a Project** → **New Project** → name it "YouTube Research" → Create
3. In the search bar, search "YouTube Data API v3" → click it → click **Enable**
4. Go to **APIs & Services** → **Credentials** → **Create Credentials** → **API Key**
5. Copy the key
6. Create a `.env` file in the project root with: `YOUTUBE_API_KEY=your_key_here`

This is completely free. The daily quota (10,000 units) supports ~30 research sessions per day.

### Python Dependencies

```bash
pip install google-api-python-client python-dotenv
```

---

## Process

### Step 1: Understand the Request

Parse what the user wants:
- **Topic/niche** (required): e.g., "video editing", "productivity", "AI tools"
- **How many channels** (optional, default 10): more channels = broader research but uses more quota
- **Time period** (optional, default 12 months): how far back to look
- **Minimum channel size** (optional, default 1,000 subs): filters out tiny channels

### Step 2: Run the Script

```bash
python3 .claude/skills/youtube-outlier-research/scripts/outlier_research.py \
  --query "TOPIC" \
  --max-channels 10 \
  --months 12 \
  --min-subscribers 1000 \
  --min-outlier-score 3.0
```

**Parameters:**

| Flag | Default | What it does |
|------|---------|--------------|
| `--query` | required | The niche/topic to search |
| `--max-channels` | 10 | Number of channels to analyze |
| `--months` | 12 | Only include videos from last N months |
| `--min-subscribers` | 1000 | Skip channels below this sub count |
| `--min-outlier-score` | 3.0 | Minimum views/median ratio to include |
| `--max-videos-per-channel` | 100 | Max videos to pull per channel |

**Adjusting for different needs:**
- Quick scan: `--max-channels 5 --months 6`
- Deep dive: `--max-channels 20 --months 12`
- Only big channels: `--min-subscribers 10000`
- Only massive outliers: `--min-outlier-score 10`

### Step 3: Build the Report

The script outputs JSON. Use it to create a markdown report at `research/youtube-outliers/[topic]/report.md` with this format:

```markdown
# Outlier Research: [Topic]

**Date:** YYYY-MM-DD | **Channels analyzed:** N | **Videos scanned:** N

---

## Top Outlier Videos

### 1. "Video Title" — Xx outlier
- **Channel:** Channel Name (XK subs)
- **Views:** X vs channel median of X
- **Engagement:** X likes, X comments
- **Published:** Date (X days ago)
- **Link:** URL
- **Why it likely worked:** [Your analysis of the title, topic, or angle]

### 2. ...

---

## Patterns & Takeaways

Analyze the top outliers and identify:
1. **Title patterns** — What do the top titles have in common?
2. **Topic clusters** — Are certain sub-topics dominating?
3. **Format signals** — Tutorials, listicles, stories, comparisons?
4. **Timing** — Any seasonal or trend-based patterns?

## Content Ideas for Artem

Based on the outliers above, suggest 3-5 video ideas that could work for the Full-Time Editor channel, adapted to Artem's audience (editors building a business).

---

## Channels Analyzed

| Channel | Subscribers | Videos Scanned |
|---------|-------------|----------------|
| Channel Name | XK | N |
| ... | ... | ... |

*Quota used: ~X units (of 10,000 daily)*
```

### Step 4: Present Key Findings

After saving the report, summarize the top 3-5 outliers for the user with:
- The video title and outlier score
- Why it likely performed well
- How it could be adapted for their channel

---

## Outlier Score Guide

| Score | Meaning |
|-------|---------|
| 3-5x | **Notable** — performed well above average |
| 5-10x | **Strong outlier** — clearly hit a nerve |
| 10-30x | **Viral for the channel** — massive outperformance |
| 30x+ | **Extreme outlier** — likely hit the algorithm jackpot |

---

## Error Handling

**"YOUTUBE_API_KEY not found"**: Walk the user through the API key setup in Prerequisites above.

**"Missing dependency"**: Run `pip install google-api-python-client python-dotenv`

**"No channels found"**: Try a broader or different search term.

**"No qualifying channels"**: Lower `--min-subscribers` or broaden the search.

**Quota exceeded**: The daily limit (10,000 units) resets at midnight Pacific time. Each research session uses ~250-350 units.

---

## Quality Checklist

- [ ] Report includes outlier score AND channel median for context
- [ ] Videos are recent (within the specified time period)
- [ ] Patterns & Takeaways section has actionable insights, not just data
- [ ] Content Ideas section is tailored to Artem's audience (editors building a business)
- [ ] Report is saved to `research/youtube-outliers/[topic]/report.md`
