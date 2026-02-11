# Remove Sparkle Syndrome™ + Fix Outdated Messaging

## Context

Sparkle Syndrome™ is being retired. It's redundant — the concept is fully absorbed into "Button Pusher" (the before-identity in the Creative Director Shift™). Additionally, phrases like "creative direction over flash/effects/execution" are outdated — the correct framing is now **"what to show, not how to show it"**.

**Decisions from Artem:**
- Sparkle Syndrome™ → absorbed into Button Pusher, remove everywhere
- "creative direction over flash/effects" → replace with "what to show, not how" language
- "serve the story" vs "serve the viewer" → use both contextually: "serve the viewer" for high-level messaging, "serve the story" for specific editing decisions
- Generic word "storytelling" → keep as-is, it's fine as a generic English word
- Core Four™ stays as-is for now (Artem may rework later)

---

## Changes

### A. Remove Sparkle Syndrome™ (6 files, ~15 edits)

**1. `fte-framework-definitions.md`**
- Line 21: `Button Pusher mindset, Sparkle Syndrome™ (adding effects for their sake)` → `Button Pusher mindset`
- Lines 334-338: Delete entire Sparkle Syndrome™ section from Enemy Language (redundant with Button Pusher definition in Section 1)

**2. `full-time-editor-manifesto.md`**
- Lines 187-199: Replace Enemy #1 Sparkle Syndrome™ section → Rewrite as "Button Pusher Mindset" enemy (adding effects to compensate, executing without thinking for the viewer)
- Line 334: `That's \`Sparkle Syndrome™\` — the hallmark of a button pusher.` → `That's the hallmark of a button pusher — compensating for weak fundamentals with flashy effects.`
- Line 593: `Chasing effects to compensate (\`Sparkle Syndrome™\`)` → `Chasing effects to compensate (button-pusher behavior)`
- Line 823: Remove Sparkle Syndrome™ row from Enemies quick reference table

**3. `full-time-editor-overview.md`**
- Line 67: Remove `(\`Sparkle Syndrome™\`)` parenthetical → `(button-pusher behavior)`

**4. `voice-of-customer.md`**
- Line 250: `compensating with effects (Sparkle Syndrome™)` → `compensating with effects (button-pusher behavior)`

**5. `voice-of-artem.md`**
- Lines 113-121: Replace Enemy #1 Sparkle Syndrome™ section → Rewrite as "Button Pusher Behavior" (editors adding effects to compensate instead of thinking for the viewer)
- Line 225: Remove `Sparkle Syndrome™` from enemy language list
- Line 643: Remove Sparkle Syndrome™ row from Enemy Quick Reference table

**6. `voice-of-artem-youtube.md`**
- Line 414: Remove `anti-Sparkle Syndrome™` from philosophy list
- Line 440: Remove `Anti-Sparkle Syndrome™` from movement topics list

### B. Fix "creative direction over flash/effects/execution" (3 edits)

**1. `voice-of-artem.md`**
- Line 86: `creative direction > flash` → `what to show > how to show it`

**2. `full-time-editor-manifesto.md`**
- Line 124: Section heading `Creative Direction Over Execution` → `What to Show, Not How to Show It`

**3. `artem-journey.md`**
- Line 315: `Creative direction over effects` → `What to show, not how to show it`

### C. Fix "serve the story" → "serve the viewer" in high-level definitions (1 edit)

**1. `fte-framework-definitions.md`**
- Line 33: `serving the story` → `serving the viewer`

### D. Fix stale x-tweet-writer example (1 edit)

**1. `x-tweet-writer/SKILL.md`**
- Line 274: `Eight months of Storytelling later:` → `Eight months after making the Creative Director Shift:`

---

## Verification

After all changes:
1. Grep for "Sparkle Syndrome" across `.claude/knowledge/` and `.claude/skills/` — should return zero results
2. Grep for "creative direction over" — should return zero results
3. Confirm "Button Pusher" references are consistent across all files
