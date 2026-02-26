# Phase 3: Knowledge Files

## Purpose
Determine what knowledge files to upload to the GPT, create any new ones needed, and avoid redundancy.

---

## Step 1: Inventory Available Materials

List everything available:
- Existing knowledge files (Voice of Artem, brand docs, etc.)
- Reference materials the user provided (theory docs, transcripts, examples)
- New files created during Phase 2 (synthesized patterns, frameworks)

---

## Step 2: Decide What to Upload

### Categories of Knowledge Files

**Voice/Tone Files**
- Voice of Artem (almost always included — it's how the GPT talks to users)
- Only skip if the GPT explicitly uses a different voice

**Theory/Philosophy Files**
- Underlying principles and frameworks that inform the GPT's approach
- These give the GPT deeper understanding beyond what's in the instructions
- Example: "Client Communication Theory" gives the negotiator GPT the philosophy behind Price Last

**Synthesized Pattern Files**
- Created during Phase 2 when reference materials had examples
- Contains named patterns with structure + thinking
- This is where the depth lives when instructions had to be condensed

### Decision Framework

For each potential file, ask:

1. **Does the GPT need this to produce good output?**
   - Yes → Include
   - No → Skip

2. **Is it redundant with another file?**
   - If two files cover the same material (like a theory doc and its condensed version), only include the more comprehensive one
   - Never upload redundant files — they confuse the GPT

3. **Is it too long or unfocused?**
   - If a file is very long but only parts are relevant, create a focused extract
   - Don't make the GPT dig through 50 pages to find what it needs

4. **Will the GPT copy-paste from it?**
   - If the file contains example outputs the GPT might regurgitate verbatim, don't upload it
   - Synthesize patterns instead (Phase 2)

---

## Step 3: Create New Knowledge Files (If Needed)

If Phase 2 identified content that should live in knowledge files:

### Synthesized Patterns File
When you created patterns from reference materials, save them as a standalone knowledge file:
- Named patterns with "When to use" triggers
- Structure (numbered steps)
- Thinking behind each pattern
- No copy-paste examples

### Focused Extracts
If an existing file is too broad, create a focused version:
- Pull only the sections relevant to this GPT
- Reorganize for the GPT's specific use cases
- Remove anything that would distract or confuse

---

## Step 4: Check for Redundancy

Before finalizing, verify:
- [ ] No two files cover the same material
- [ ] Every file serves a distinct purpose
- [ ] The GPT won't get conflicting guidance from different files
- [ ] Total number of files is manageable (aim for 2-4, max 6)

---

## Step 5: Document the Final List

Create a clear list of knowledge files with:
- File name
- What it provides to the GPT
- Whether it's an existing file or newly created

Example:
```
Knowledge Files to Upload:
1. Voice of Artem (existing) — How the GPT talks to users
2. Client Communication Theory (existing) — Underlying philosophy and frameworks
3. Synthesized Patterns & Frameworks (NEW) — Detailed patterns with thinking for each use case
```

---

## Output

- Any new knowledge files saved to `custom-gpts/[gpt-name]/`
- Final knowledge file list ready for the README
