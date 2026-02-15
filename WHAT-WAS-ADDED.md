# Screenwriter Skill - What Was Added

## Overview

Professional scriptwriting capability has been fully integrated into Claude Code Video Toolkit. This addition transforms how video scripts are created - from basic narration to compelling stories with precise timing and emotional impact.

## Files Created

### 1. Screenwriter Skill
**Location:** `.claude/skills/screenwriter/`

```
screenwriter/
├── SKILL.md       (23KB) - Complete skill documentation
├── examples.md    (14KB) - Real-world script examples  
└── README.md      (4KB)  - Quick reference guide
```

### 2. Script Command
**Location:** `.claude/commands/script.md` (17KB)

Interactive workflow for creating professional scripts.

### 3. Integration Guide
**Location:** `SCREENWRITER-INTEGRATION.md` (11KB)

Complete documentation on how to use the new features.

## Total Addition

**Files:** 4 new files
**Size:** ~69KB of documentation and examples
**Impact:** Zero runtime overhead (skills load on-demand)

## What You Can Do Now

### Create Professional Scripts

```bash
/script
```

Launches an interactive session that:
1. Discovers your video project
2. Asks about audience and tone
3. Proposes narrative structure based on proven formulas
4. Writes scene-by-scene scripts with precise timing
5. Saves to `public/audio/scenes/*.txt`

### Use Proven Narrative Formulas

| Video Type | Formula |
|------------|---------|
| Product Demo | Pain → Solution → Proof → Action |
| Sprint Review | Context → Shipped → Demo → Impact → Next |
| Tutorial | Goal → Steps → Result → Gotchas |
| Case Study | Challenge → Approach → Results → Takeaway |
| Announcement | Tease → Reveal → Impact → Access |

### Get Precise Timing

Automatic calculations:
- 30 seconds = ~75 words
- 60 seconds = ~150 words
- 90 seconds = ~225 words
- 120 seconds = ~300 words

Based on 150 words/minute standard speaking pace.

### Apply Professional Principles

Every script follows:
- ✅ Clarity over cleverness
- ✅ Benefits before features
- ✅ Active voice throughout
- ✅ Specific numbers (not vague claims)
- ✅ Strategic pauses for impact
- ✅ Strong CTAs with friction reducers

## Example Output

**Input (raw content):**
```
Feature: Deploy in 60 seconds
Metric: 50,000 deploys/day
Benefit: Zero downtime
```

**Output (professional script):**

**Scene 01: Hook (5 seconds)**
```
Still waiting 30 minutes for deployments?
```

**Scene 02: Problem (15 seconds)**
```
Every deploy means context switching. Waiting. Wondering if something broke. [pause 0.5s]

Your team deserves better.
```

**Scene 03: Solution (12 seconds)**
```
Meet TurboDeploy - get your code live in under 60 seconds. [pause 0.5s]

Zero downtime. Zero stress.
```

## Workflow Integration

### Before
```
/video → manual script editing → /generate-voiceover
```

### After
```
/video → /script → /generate-voiceover
         ↓
   Professional narrative
   Precise timing
   Emotional arc
   Brand-aligned
```

## Key Features

### 1. Genre-Specific Patterns
Different video types get different structures automatically.

### 2. Timing Analysis
Word counts calculated per scene with duration validation.

### 3. A/B Variations
Generate multiple hook or CTA options for testing.

### 4. Brand Voice Integration
Automatically reads brand guidelines from `brands/` directory.

### 5. Emotional Arc Design
Scripts follow engagement patterns: Frustration → Hope → Satisfaction

### 6. Quality Checks
- Readability analysis
- Sentence length variation
- Active vs passive voice
- Specificity vs vagueness

## Where Everything Lives

```
claude-code-video-toolkit/
├── .claude/
│   ├── skills/
│   │   └── screenwriter/          ← NEW SKILL
│   │       ├── SKILL.md
│   │       ├── examples.md
│   │       └── README.md
│   └── commands/
│       └── script.md              ← NEW COMMAND
├── SCREENWRITER-INTEGRATION.md    ← INTEGRATION GUIDE
└── WHAT-WAS-ADDED.md             ← THIS FILE
```

## How to Start Using

1. **Navigate to toolkit:**
   ```bash
   cd /Users/romangasanov/Documents/Projects_coding/claude-code-video-toolkit
   ```

2. **Launch Claude Code** (in this directory)

3. **Create a video project:**
   ```
   /video
   ```

4. **Write professional script:**
   ```
   /script
   ```

## Examples Included

See `.claude/skills/screenwriter/examples.md` for:
- ✅ Product demo (90s)
- ✅ Sprint review (120s)
- ✅ Tutorial (180s)
- ✅ Before/after comparisons
- ✅ Tone variations by audience
- ✅ CTA formulas
- ✅ Hook variations
- ✅ Anti-patterns to avoid

## Documentation

**Quick Start:**
- `screenwriter/README.md` - 5-minute overview

**Complete Reference:**
- `screenwriter/SKILL.md` - Full documentation with all formulas

**Real Examples:**
- `screenwriter/examples.md` - Annotated scripts from different genres

**Integration:**
- `SCREENWRITER-INTEGRATION.md` - How it fits into toolkit workflow

**This File:**
- `WHAT-WAS-ADDED.md` - Summary of changes

## Next Steps

### Immediate Use
Start creating professional scripts right now with `/script`

### Learning
Read through `examples.md` to see patterns in action

### Customization
Edit `SKILL.md` to add your own narrative formulas

### Contributing
Test it and create PR to the official toolkit repo

## Comparison: With vs Without

### Without Screenwriter Skill
- ❌ Scripts sound like technical docs
- ❌ No timing calculations
- ❌ Unclear narrative structure
- ❌ Inconsistent tone
- ❌ Weak hooks and CTAs
- ❌ Manual editing required

### With Screenwriter Skill
- ✅ Compelling narratives with emotional arc
- ✅ Precise word counts per scene
- ✅ Proven formulas for each video type
- ✅ Brand-aligned tone
- ✅ Strong hooks that grab attention
- ✅ CTAs that drive action

## Installation Location

Everything was installed to:
```
/Users/romangasanov/Documents/Projects_coding/claude-code-video-toolkit/
```

Size: 35MB total (including original toolkit + screenwriter addition)

## Credits

**Created:** February 15, 2026
**Version:** 1.0.0

**Inspired by:**
- coreyhaines31/marketingskills (copywriting principles)
- obra/superpowers (content strategy)
- Professional screenwriting best practices

**Integrated into:** Claude Code Video Toolkit

---

## Ready to Use

The screenwriter skill is fully integrated and ready to create professional video scripts.

**Start now:** `/script`
