# Claude Code Infrastructure Context

Use this context when creating skills. All skills will be used inside Claude Code (Anthropic's CLI tool).

---

## Skills vs Knowledge

There are two types of files in my Claude Code setup:

- **Skills** = Actions, processes, HOW to do things → Live in `.claude/skills/`
- **Knowledge** = Reference material, context, WHAT to know → Live in `.claude/knowledge/`

**Skills should never contain knowledge.** A scriptwriting skill should NOT include my voice guidelines, personal stories, or brand context. Instead, it should reference the knowledge files where that information lives.

---

## Folder Structure

```
.claude/
├── skills/                    # Actions (how to do things)
│   └── [skill-name]/
│       ├── SKILL.md           # Main skill file
│       └── [optional extras]  # Templates, examples, inspiration, scripts
│
└── knowledge/                 # Reference (what to know)
    ├── artem/                 # Artem's voice and stories (default)
    │   ├── voice-of-artem.md            # Core voice (shared across all formats)
    │   ├── voice-of-artem-email.md      # Email-specific voice patterns
    │   ├── voice-of-artem-youtube.md    # YouTube-specific voice patterns
    │   ├── voice-of-artem-twitter.md    # X/Twitter-specific voice patterns
    │   ├── voice-of-artem-newsletter.md # Newsletter-specific voice patterns
    │   ├── artem-story-bank.md
    │   └── artem-journey.md
    ├── full-time-editor/      # FTE brand and business (default)
    │   ├── full-time-editor-overview.md
    │   ├── full-time-editor-manifesto.md
    │   ├── ideal-customer-profile.md
    │   ├── voice-of-customer.md
    │   ├── fte-framework-definitions.md
    │   ├── fte-30-day-sprint.md
    │   └── micro-offer-launch-plan.md
    └── alex-garcia/           # Alex's brand (only when specified)
        ├── voice-of-alex.md
        ├── alex-garcia-brand-dna.md
        ├── alex-garcia-visual-style-guide.md
        └── alex-garcia-sound-design-guide.md
```

---

## Default Persona

**All content defaults to Artem / Full-Time Editor** unless explicitly specified otherwise.

This means every content skill should reference:
- `.claude/knowledge/artem/` — Voice, stories, journey
- `.claude/knowledge/full-time-editor/` — Brand, ICP, frameworks

Only switch to another persona (Alex, etc.) when the user explicitly says so.

---

## Gold Standard: SKILL.md Format

Every skill file should follow this structure:

```markdown
---
name: [skill-name]
description: [When to use this skill. Include trigger phrases like 'USE WHEN user says...']
---

# [Skill Name]

[One-line description of what this skill does.]

---

## Knowledge Dependencies

Before executing, load the following knowledge files:

- `.claude/knowledge/artem/voice-of-artem.md` — Tone and style
- `.claude/knowledge/artem/artem-story-bank.md` — Personal stories (when relevant)
- `.claude/knowledge/full-time-editor/ideal-customer-profile.md` — Who we're speaking to
- [Add or remove knowledge files based on what this specific skill needs]

---

## When to Use

- [Trigger condition 1]
- [Trigger condition 2]

---

## Inputs

[What the skill expects as input from the user]

---

## Process

[Step-by-step instructions for how the skill works]

---

## Output

**Type:** [content / research / data / export]
**Location:** `[output folder path]`
**Files produced:** [what gets created]
```

### Key Rules for SKILL.md Files:

1. **Reference knowledge, don't duplicate it** — Never paste voice guidelines, stories, or brand info into the skill. Always point to the knowledge file path.
2. **One skill = one action** — Keep skills focused. If you're tempted to add idea generation AND scriptwriting AND packaging, split them into separate skills.
3. **Include trigger phrases in the description** — The `description` field in the frontmatter helps Claude Code route to the right skill. Include phrases like `USE WHEN user says 'write a script', 'create a video script'`.
4. **Outputs go in organized folders** — Never dump files in the project root. Use `content/[type]/`, `research/[topic]/`, `data/[source]/`, or `exports/[format]/`.

---

## Routing in CLAUDE.md

After creating a skill, it gets added to the routing table in CLAUDE.md:

```markdown
| When you want to... | Load skill |
|---------------------|------------|
| [action description] | `[skill-name]` |
```

If a skill is for content creation, it automatically inherits the default persona (Artem + FTE) through the knowledge dependency system.

---

## What NOT to Put in a Skill

- Voice/tone guidelines → That's knowledge (`voice-of-artem.md`)
- Personal stories → That's knowledge (`artem-story-bank.md`)
- Brand context → That's knowledge (`full-time-editor-overview.md`)
- ICP details → That's knowledge (`ideal-customer-profile.md`)
- Multiple unrelated actions → Split into separate skills
