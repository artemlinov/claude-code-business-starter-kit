---
name: youtube-transcript
description: Fetch and clean YouTube video transcripts. USE WHEN user says 'get transcript from youtube', 'pull transcript', 'youtube transcript', 'extract transcript from video', 'grab the transcript', 'transcribe this youtube video', 'clean this video transcript', 'get captions from youtube'.
---

# YouTube Transcript

Fetches auto-generated transcripts from YouTube videos and cleans them into readable text.

---

## When to Use

- User provides a YouTube video link and wants the transcript
- User says "get transcript from [youtube link]"
- User wants to read what was said in a video
- User needs a cleaned-up version of YouTube auto-captions
- User needs a transcript WITH timestamps (for YouTube descriptions, chapter creation, etc.)

---

## Output

**Type:** content
**Location:** `content/transcripts/`
**Files produced:**
- `[video-title].txt` - Cleaned, readable transcript

---

## Prerequisites

The `youtube-transcript-api` Python package must be installed. If not installed, run:

```bash
pip install youtube-transcript-api
```

---

## Process

### Step 1: Extract Video ID

From the YouTube URL, extract the video ID. Examples:
- `https://www.youtube.com/watch?v=ABC123` → `ABC123`
- `https://youtu.be/ABC123` → `ABC123`
- `https://www.youtube.com/watch?v=ABC123&t=120` → `ABC123`

### Step 2: Fetch the Transcript

Run the Python script to fetch the raw transcript:

**Without timestamps** (for reading/cleaning):
```bash
python3 .claude/skills/youtube-transcript/scripts/fetch_transcript.py "VIDEO_ID"
```

**With timestamps** (for YouTube descriptions/chapters):
```bash
python3 .claude/skills/youtube-transcript/scripts/fetch_transcript.py "VIDEO_ID" --timestamps
```

The `--timestamps` flag outputs in `[M:SS] text` format:
```
[0:00] Today we're talking about social shows
[0:05] and how you can build one from scratch
[0:33] Number one understanding your brand's content narrative
...
```

**When to use which:**
- **No timestamps**: Reading, summarizing, repurposing content
- **With timestamps**: Writing YouTube descriptions, creating chapters, video navigation

### Step 3: Clean the Transcript

Apply the transcript-cleaner skill rules to the raw transcript:

1. **Punctuation**: Add periods, commas, question marks where needed
2. **Capitalization**: Fix sentence starts, proper nouns (YouTube, names, etc.)
3. **Spelling**: Fix common auto-caption errors
4. **Paragraphs**: Break into logical paragraphs at topic shifts
5. **Remove artifacts**: Strip [music], gibberish, filler words

Reference the full cleaning rules from: `.claude/skills/transcript-cleaner/SKILL.md`

### Step 4: Save the Output

1. Create output directory if needed: `content/transcripts/`
2. Use the video title (kebab-case) as filename: `video-title-here.txt`
3. Save the cleaned transcript (no title header in the file content)

---

## Quality Checklist

**For cleaned transcripts (no timestamps):**

- [ ] Every sentence has proper punctuation
- [ ] Proper nouns are capitalized
- [ ] No timestamps or [music] tags remain
- [ ] Paragraphs break at logical points
- [ ] Text reads naturally when spoken aloud
- [ ] Saved as a single .txt file

**For timestamped transcripts:**

- [ ] Timestamps are preserved in [M:SS] format
- [ ] Text is readable (basic cleanup only)
- [ ] [music] tags can remain (they mark non-speech sections)

---

## Error Handling

**"No transcript available"**: Some videos don't have auto-captions. Let the user know and suggest they may need to use a different transcription service.

**"Video unavailable"**: The video may be private, deleted, or region-locked. Ask the user to verify the link works.

**Package not installed**: Run `pip install youtube-transcript-api` first.

---

## Example

**User:** Get the transcript from https://www.youtube.com/watch?v=dQw4w9WgXcQ

**Process:**
1. Extract video ID: `dQw4w9WgXcQ`
2. Run: `python3 .claude/skills/youtube-transcript/scripts/fetch_transcript.py "dQw4w9WgXcQ"`
3. Clean the raw output using transcript-cleaner rules
4. Save to: `content/transcripts/video-title.txt`
5. Return the cleaned transcript to user

---

**User:** I need a YouTube description for this video: https://youtu.be/8V-bA8w_hYw

**Process:**
1. Extract video ID: `8V-bA8w_hYw`
2. Run WITH timestamps: `python3 .claude/skills/youtube-transcript/scripts/fetch_transcript.py "8V-bA8w_hYw" --timestamps`
3. Use timestamps to identify chapter breaks and create accurate chapter markers
4. Pass to youtube-description-writer skill

---

## Alternative: YouTube MCP

If the YouTube MCP is configured (check `.mcp.json`), you can also use:
- `mcp__youtube__get_captions` — Get captions with timestamps
- `mcp__youtube__get_video_info` — Get video metadata

The MCP may provide additional features like chapter extraction. Check available tools with the MCP.
