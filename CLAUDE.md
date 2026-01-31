# Claude Code for Business - Starter Kit

Your AI Employee infrastructure. Build AI systems that do real work in your business.

---

## IMPORTANT: Working Directory

**You MUST open THIS folder directly in VS Code.**

If you cloned this repo into a subfolder, make sure VS Code opens the folder containing this `CLAUDE.md` file at the root - NOT a parent folder.

**Correct:** VS Code opens `claude-code-business-starter-kit/`
**Wrong:** VS Code opens a parent folder that contains `claude-code-business-starter-kit/`

If skills, MCPs, or agents aren't working, this is usually why.

---

## Routing

### Skills (Actions)

| When you want to... | Load skill |
|---------------------|------------|
| Extract ideas from a call/transcript | `content-insight-extractor` |
| Analyze a content idea / voice memo | `content-idea-analyzer` |
| Write a YouTube script | `youtube-script-writer` |
| Write a YouTube description | `youtube-description-writer` |
| Write X posts | `x-tweet-writer` |
| Write X threads | `x-thread-writer` |
| Write sales/nurture emails | `1m-email-writer` |
| Get a YouTube video transcript | `youtube-transcript` |
| Clean/format a raw transcript | `transcript-cleaner` |
| Create a new skill | `create-skill` |
| Create a new command | `create-command` |
| Create a new agent | `create-agent` |
| Create a new hook | `create-hook` |
| Add or build an MCP | `create-mcp` |
| Search online for MCP servers | `mcp-finder` agent (spawned by create-mcp) |

### Knowledge (Reference)

**Default: Artem / Full-Time Editor**

Unless specified otherwise, ALL content is for Artem. Always load:
- `.claude/knowledge/artem/` — Voice, stories, journey
- `.claude/knowledge/full-time-editor/` — Brand, ICP, frameworks

**Only when explicitly specified for another persona:**

| If user says... | Load instead |
|-----------------|--------------|
| "for Alex" / "Marketing Examined" | `.claude/knowledge/alex-garcia/` |
| "for [other client]" | Create new knowledge folder or ask |

#### Knowledge Files

**artem/** (default voice)
- `voice-of-artem.md` — Core tone, style, personality (platform-agnostic)
- `voice-of-artem-email.md` — Email-specific voice patterns
- `voice-of-artem-youtube.md` — YouTube-specific voice patterns
- `voice-of-artem-twitter.md` — X/Twitter-specific voice patterns
- `voice-of-artem-newsletter.md` — Newsletter-specific voice patterns
- `artem-story-bank.md` — Personal stories by theme
- `artem-journey.md` — Background and journey

**full-time-editor/** (default brand)
- `full-time-editor-overview.md` — What FTE is
- `full-time-editor-manifesto.md` — Core beliefs and mission
- `ideal-customer-profile.md` — Who the customer is
- `voice-of-customer.md` — Customer language and pain points
- `fte-framework-definitions.md` — Key frameworks and terminology
- `fte-30-day-sprint.md` — Sprint program details
- `micro-offer-launch-plan.md` — Launch strategy

**alex-garcia/** (only when specified)
- `voice-of-alex.md` — Tone, style, personality
- `alex-garcia-brand-dna.md` — Brand identity
- `alex-garcia-visual-style-guide.md` — Visual guidelines
- `alex-garcia-sound-design-guide.md` — Audio guidelines

### Content Creation Rules

1. **Default to Artem** — No persona specified = Artem + FTE knowledge
2. **Load knowledge first** — Before creating content, load relevant knowledge files
3. **Match skill to task** — Use the appropriate content skill
4. **Switch only when told** — Only use other personas when explicitly requested

---

## Output Organization

**Principle:** Never dump files in root. Outputs go in logical folders.

| Output Type | Location | Example |
|-------------|----------|---------|
| Content | `content/[type]/[project]/` | `content/youtube/competitor-analysis/` |
| Research | `research/[topic]/` | `research/ai-tools/` |
| Data | `data/[source]/` | `data/youtube-api/` |
| Exports | `exports/[format]/` | `exports/csv/` |

**When creating skills that produce output:**
1. Determine what TYPE of output (content, research, data, export)
2. Create the appropriate folder structure
3. Use descriptive project/topic names
4. Keep related files together

---

## Folder Structure

```
project/
├── CLAUDE.md              # Project memory + rules (this file)
├── .mcp.json              # MCP server connections
│
├── .claude/
│   ├── settings.json      # Permissions and hooks
│   ├── skills/            # Actions (how to do things)
│   ├── knowledge/         # Reference (what to know)
│   │   ├── artem/         # Artem's voice and stories (default)
│   │   ├── full-time-editor/  # FTE brand context (default)
│   │   └── alex-garcia/   # Alex's brand (when specified)
│   ├── commands/          # Your slash commands
│   └── agents/            # Your subagents
│
├── content/               # Content outputs (videos, posts, etc.)
├── research/              # Research outputs
├── data/                  # Data exports and raw data
└── exports/               # Formatted exports
```

**Skills vs Knowledge:**
- **Skills** = Actions, processes, how to do things (`.claude/skills/`)
- **Knowledge** = Reference material, context, what to know (`.claude/knowledge/`)

**Rules live in CLAUDE.md** - this file. Add project-wide guidelines here.

---

## MCP Servers

This project is configured to use:
- **YouTube MCP** - For video research and analytics
- **Notion MCP** - For saving insights and data

See `.mcp.json` for configuration.

---

## Getting Started

1. Open this folder in your terminal
2. Run `claude` to start Claude Code
3. Say "create a skill for [something]" to build your first skill

---

## Communication Rules

- **Always confirm when done.** After completing a task (editing files, creating content, running commands), explicitly tell the user you're finished and summarize what was done. Never leave the user wondering if you're still working.
