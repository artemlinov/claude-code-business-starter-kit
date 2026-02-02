---
name: sop-creator
description: Create SOPs from Loom recordings for VAs and team members. USE WHEN user says 'create an SOP', 'SOP from this Loom', 'turn this Loom into an SOP', 'VA task from Loom', 'document this process', or shares a Loom link and wants a task document created from it.
---

# SOP Creator

Turn Loom recordings into clean, simple SOP documents for VAs and team members.

## Process

### Step 1: Get the transcript

- If the user provides a Loom link, use the `getLoomTranscript` MCP tool to pull the transcript automatically
- If the user pastes a transcript directly, use that instead
- Ask for the Loom link if neither is provided

### Step 2: Extract the key information

Go through the transcript and pull out:

- **Task title** — what is the task about (short, clear)
- **Who it's assigned to** — name of the person
- **Deadline** — if mentioned, include urgency level
- **Objective** — one line on what needs to be done
- **Access/tools provided** — any platforms, accounts, or tools given to the person, with sub-bullets for confirmation requests (e.g., "let me know if you can log in")
- **Core instructions** — the actual steps or process, broken into simple bullets
- **Important rules/exceptions** — edge cases, things NOT to do, special situations mentioned
- **How to handle questions** — if the person explains how they want questions asked (e.g., batch them)
- **Action items for the assignee** — what they need to confirm or deliver

### Step 3: Write the SOP

Format rules:
- Keep it short and scannable — bullets over paragraphs
- No tables, no cheat sheets, no checklists with checkboxes
- No overly formal tone — write it like the person spoke it
- Use simple markdown: `#` for title, `**bold**` for labels, `-` for bullets, backticks for tags/codes
- The Loom link goes at the top right under the title
- Deadline and urgency right under the Loom link
- Group related info under short bold labels (e.g., "Ignore:", "Important:")
- Only include what was actually said — don't add extra steps or over-explain
- End with a natural closing like "Let me know if you have any questions"

### Step 4: Save and confirm

- Save to `content/sops/[descriptive-name].md`
- Tell the user the SOP is ready and where it's saved
- Ask if anything needs tweaking

## Output

- Location: `content/sops/`
- Format: Markdown (.md)
- Naming: lowercase, hyphenated, descriptive (e.g., `add-tags-gohighlevel.md`)

## Reference Example

This is the style and level of detail to aim for:

```markdown
# Add Tags in GoHighLevel

**Loom:** https://www.loom.com/share/example
**Deadline:** Wednesday (urgent)

---

I gave you access to:
1. GoHighLevel
   - Let me know if you can log in
2. My two calendars
   - Old calendar — ends around September 25th
   - New calendar — starts in September

Two tags to add:
- `salescall-attended`
  - Editor Success Session
  - Roadmap Call
  - "[Name] x Artem" with no event type
- `discoverycall-attended`
  - Editor Clarity Session
  - Clarity Call

How to tag: find the person on the calendar, search them by email in GoHighLevel, scroll to tags, add the right one.

Ignore:
- Anything with "Starter Story"
- Anything with "Coaching"
- Group calls

Important:
- Never remove existing tags — only add
- If someone had a Clarity Session AND a plain "[Name] x Artem" call, add both tags
- Some tags are already there from before — many are still missing, go through everything
- No-shows still get tagged (e.g. Sedgar = discovery call no-show)

When you're unsure about someone, skip them and keep going. Batch all your questions into one message instead of asking one by one.

Let me know if you have any questions and if you can deliver by Wednesday.
```

## Critical Rules

- Never add information that wasn't in the transcript
- Keep it simple — if it feels like a corporate document, it's too formal
- Every SOP should be readable in under 2 minutes
- Match the speaker's tone and intent, not just their words
