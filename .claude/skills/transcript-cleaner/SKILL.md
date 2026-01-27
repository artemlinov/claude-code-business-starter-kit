---
name: transcript-cleaner
description: Clean and format raw transcripts into readable .txt files. Use when the user provides a transcript (raw, auto-generated, or copied from YouTube, podcasts, interviews, or any other source) and wants it cleaned up, formatted with proper paragraphs, corrected for grammar and spelling, with timestamps removed.
---

# Transcript Cleaner

Transform raw transcripts into polished, professionally formatted .txt files that read like written prose.

## Core Principles

1. **Preserve the speaker's voice**: The cleaned transcript should sound exactly like the speaker, just with proper punctuation and formatting. Never change their word choices or rephrase their ideas.

2. **Read it aloud mentally**: When adding punctuation, imagine reading the sentence aloud. Punctuation marks indicate pauses and intonation changes.

3. **Professional quality**: The output should be indistinguishable from a professionally transcribed document.

4. **Single file output**: ALWAYS output each transcript as ONE complete file. NEVER split transcripts into multiple parts, regardless of length. If a transcript is long, use bash commands to write the file in chunks and concatenate them, or write directly to the output directory.

## Rules

### Punctuation (CRITICAL)

1. **Periods**: End every complete thought with a period. Transcripts often run sentences together without periods. Look for places where the speaker finishes one idea and starts another.

2. **Commas**: Add commas for:
   - Items in a series: "titles, thumbnails, and hooks"
   - After introductory phrases: "So, here's what I learned"
   - Before coordinating conjunctions joining independent clauses: "I tried everything, but nothing worked"
   - Around non-essential information: "My business partner, Hassan, takes the calls"
   - After transitional words: "However, this approach failed"

3. **Question marks**: Add question marks to all questions, including rhetorical ones: "But here's the thing, right?" becomes "But here's the thing. Right?"

4. **Colons**: Use colons to introduce lists or explanations: "There are three things you need: clarity, consistency, and patience."

5. **Semicolons**: Use sparingly to connect closely related independent clauses: "The views were high; the business was bleeding."

6. **Apostrophes**: Ensure all contractions and possessives have apostrophes: "don't", "they're", "the viewer's attention", "clients' needs"

7. **Quotation marks**: Use for:
   - Direct speech or quotes: He said, "This is the way."
   - Titles of videos or specific phrases being referenced: the "how I" format
   - Scare quotes for ironic or emphasized terms: these "gurus" online

8. **Never use em dashes (—)**: Replace with commas, colons, or periods depending on context.

### Capitalization

1. **Sentence beginnings**: Always capitalize the first word after a period, question mark, or exclamation point.

2. **Proper nouns**: Capitalize names of people, companies, platforms, products:
   - People: Daniel Dalen, Alex Hormozi, Ali Abdaal
   - Companies: YouTube, Instagram, TikTok, Calendly, ChatGPT
   - Products/Features: YouTube Studio, Instagram Reels

3. **Titles**: Capitalize significant words in video titles, book titles, etc.

4. **Acronyms**: Keep in all caps: ICP, CTA, VSSL, B2B, ROI, KPI, SOP

### Spelling Corrections

1. **Common auto-caption errors**:
   - "Daniel Dalon" → "Daniel Dalen"
   - "Eman" or "Emanatsi" → "Iman Gadzhi" (context dependent)
   - "Hormosi" or "Hermosy" → "Hormozi"
   - "chatbt" → "ChatGPT"
   - "Tik Tok" → "TikTok"
   - "calendarly" → "Calendly"
   - "salesunnel" → "sales funnel"
   - "topofunnel" → "top of funnel"
   - "middlefunnel" → "middle funnel"
   - "bottomfunnel" → "bottom of funnel"

2. **Business terms**: Ensure correct spelling of:
   - high ticket (two words)
   - paid in full (three words)
   - one-on-one (hyphenated)
   - long-term, short-term (hyphenated when used as adjectives)

3. **Numbers**: 
   - Spell out numbers one through ten
   - Use numerals for 11 and above
   - Use numerals for money: $37,000, 500K, 10K
   - Use numerals with K/M abbreviations: 40K a month, 4 million views

### Paragraph Structure

1. **Topic-based breaks**: Start a new paragraph when:
   - The speaker shifts to a new topic or point
   - A new example or story begins
   - The speaker transitions with phrases like "Now," "So," "All right," "Okay"
   - There's a clear rhetorical shift (question to answer, problem to solution)

2. **Length**: Aim for paragraphs of 3-6 sentences. Break up longer blocks for readability.

3. **Speaker changes**: In interviews or multi-speaker content, start a new paragraph for each speaker. Consider using speaker labels if helpful.

4. **Lists**: When the speaker gives numbered steps or items, consider formatting as a visual list if there are 3+ items, or keep inline for 2 items.

### Content Handling

1. **Filler words**: 
   - Remove excessive "um," "uh," "like," "you know" when they add no meaning
   - Keep occasional filler if it's part of the speaker's authentic voice or adds emphasis
   - Keep "like" when used for comparisons or examples

2. **False starts and repetitions**: 
   - Remove stutters and immediate self-corrections
   - "I I think" → "I think"
   - "So so so important" → "so, so, so important" OR "so incredibly important"

3. **Incomplete sentences**: 
   - If the speaker trails off, complete the thought if obvious, or end with an ellipsis if deliberately trailing off
   - Fragment sentences are okay if they're intentional for emphasis: "Simplicity. That's the answer."

4. **Music/sound notations**: Remove any "[music]" or similar notations from auto-captions.

5. **Gibberish at end**: Remove any garbled text or song lyrics that appear at the end of transcripts (common artifact of auto-captions continuing past the content).

6. **Timestamps**: Remove all timestamps in any format (0:03, 9:12, 1:23:45, etc.)

7. **Line breaks within sentences**: Raw transcripts often have line breaks mid-sentence. Combine these into proper flowing sentences.

### Output File Naming

1. **Title goes in filename, not content**: If a title is provided or can be derived from the transcript, use it in the output filename. Do NOT include the title as the first line of the transcript content.

2. **Filename format**: Use kebab-case for the filename based on the title or topic:
   - "How I Made $100K From One Client" → `how-i-made-100k-from-one-client.txt`
   - "Interview with Alex Hormozi" → `interview-with-alex-hormozi.txt`
   - If no title is provided, use a descriptive name based on content: `transcript.txt` or `cleaned-transcript.txt`

3. **Content starts immediately**: The cleaned transcript file should begin directly with the first paragraph of spoken content, with no title header.

## Quality Checklist

Before outputting, verify:

- [ ] Every sentence ends with appropriate punctuation (. ? !)
- [ ] All contractions have apostrophes (don't, they're, it's, etc.)
- [ ] Commas are used after introductory phrases ("So," "Now," "However,")
- [ ] Proper nouns are capitalized (YouTube, Instagram, names)
- [ ] No em dashes (—) remain in the text
- [ ] Numbers and money formatted consistently
- [ ] Paragraphs break at logical topic shifts
- [ ] No [music] or timestamp artifacts remain
- [ ] Misspelled names and terms are corrected
- [ ] Text flows naturally when read aloud
- [ ] Output is a SINGLE file (not split into parts)
- [ ] Title is in the filename, NOT in the file content

## Workflow

1. **Receive** the raw transcript from the user.
2. **Read through** the entire transcript to understand context, identify speakers, and note recurring terms/names.
3. **Clean systematically**:
   - First pass: Remove timestamps, [music] tags, and obvious artifacts
   - Second pass: Fix spelling and capitalization
   - Third pass: Add missing punctuation sentence by sentence
   - Fourth pass: Organize into logical paragraphs
4. **Review** against the quality checklist.
5. **Output as a SINGLE file**: 
   - Use the title (if available) in the filename, not as a header in the content
   - For long transcripts, use bash to write the file: `cat << 'EOF' > /mnt/user-data/outputs/filename.txt` or write chunks and concatenate
   - NEVER split into Part 1, Part 2, etc.
   - Save to /mnt/user-data/outputs/ and present to the user

## Handling Long Transcripts

When a transcript is too long to create in one tool call:

**Method 1: Using bash with heredoc**
```bash
cat << 'EOF' > /mnt/user-data/outputs/how-i-built-my-business.txt
[Full transcript content here - no title header]
EOF
```

**Method 2: Write in chunks and concatenate**
```bash
# Write first chunk
cat << 'EOF' > /home/claude/part1.txt
[First portion]
EOF

# Append remaining chunks
cat << 'EOF' >> /home/claude/part1.txt
[Next portion]
EOF

# Move to outputs when complete
mv /home/claude/part1.txt /mnt/user-data/outputs/final-transcript.txt
```

**Method 3: Use echo with append**
```bash
echo "First section content..." > /mnt/user-data/outputs/transcript.txt
echo "Next section..." >> /mnt/user-data/outputs/transcript.txt
```

The key is: ONE transcript = ONE file. Always.

## Examples

### Before (Raw):
```
so the first thing you want to do is
you want to understand your ICP right
like who are you actually talking to
um and this is super important because
if you dont know who youre talking to
youre basically just throwing content
into the void you know what I mean
```

### After (Cleaned):
```
So, the first thing you want to do is understand your ICP. Who are you actually talking to? This is super important because if you don't know who you're talking to, you're basically just throwing content into the void.
```

### Before (Raw):
```
I built a consulting business that pays
me over $500000 a year in profit and I
did it all with a small team happy
clients and the freedom to spend my
days how I want [music] and the best part is
```

### After (Cleaned):
```
I built a consulting business that pays me over $500,000 a year in profit. And I did it all with a small team, happy clients, and the freedom to spend my days how I want. And the best part is...
```
