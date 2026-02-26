# Phase 4: Packaging

## Purpose
Finalize the GPT with a name, description, conversation starters, and a README that has everything needed to set it up in ChatGPT.

---

## Step 1: Name

Generate 5 name options for the user to pick from.

**Good name qualities:**
- Short (2-3 words max)
- Clear what it does
- Memorable
- Can start with "FTE" if it's an FTE-specific tool (e.g., "FTE Negotiator")

**Naming patterns:**
- [Function]: "Client Message Crafter," "The Negotiator"
- [Brand + Function]: "FTE Negotiator," "FTE Script Coach"
- [Outcome]: "Close & Communicate," "Texts to Thousands"
- [Identity]: "The Editor's Advisor," "The Closer"

Present all 5 options and let the user pick.

---

## Step 2: Description

Write a short description (1-2 sentences) that:
- Says what the GPT does
- Says who it's for
- Doesn't oversell or use buzzwords

**Example:**
"Helps video editors craft client messages — closing new clients, raising prices, and handling tricky situations."

---

## Step 3: Conversation Starters

Create 4 conversation starters that cover the main use cases.

**Rules:**
- Each starter should map to a different use case or entry point
- Keep them short and natural — how someone would actually start a conversation
- First 2 should cover the most popular use cases
- For the other 2 slots, present 3-4 options each and let the user pick

**Good starter qualities:**
- Action-oriented ("A client just DMed me" not "I have a question about clients")
- Specific enough to route the GPT immediately
- Sound like how a real person would talk
- Not too long (under 15 words ideally)

---

## Step 4: Create README

Save a README.md to `custom-gpts/[gpt-name]/` with everything needed to set up the GPT:

```markdown
# [GPT Name]

## Description
[1-2 sentence description]

## Instructions
Copy the contents of `GPT-Instructions.md` into the ChatGPT "Instructions" field.

## Knowledge Files to Upload
1. `[filename]` — [what it provides]
2. `[filename]` — [what it provides]
3. `[filename]` — [what it provides]

For files from `.claude/knowledge/`, copy them from:
- `.claude/knowledge/artem/voice-of-artem.md`
- [etc.]

For files created in this folder, upload directly:
- `[filename].md`

## Conversation Starters
1. [Starter 1]
2. [Starter 2]
3. [Starter 3]
4. [Starter 4]

## Capabilities
- [ ] Web Browsing — [On/Off and why]
- [ ] DALL-E Image Generation — [On/Off and why]
- [ ] Code Interpreter — [On/Off and why]

## Setup Notes
[Any additional notes about setting up this GPT — e.g., "Make sure to upload Voice of Artem as a separate file, not combined with other docs"]
```

---

## Step 5: Present Everything to User

Summarize what was built:
1. Name (confirmed)
2. Description
3. Conversation starters (confirmed)
4. Knowledge files list
5. Where all the files are saved
6. Any setup notes

Confirm the user has everything they need to create the GPT in ChatGPT.

---

## Output

- `custom-gpts/[gpt-name]/README.md` — Complete setup guide
