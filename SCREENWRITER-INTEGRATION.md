# Screenwriter Skill - Integration Guide

Professional scriptwriting capability added to Claude Code Video Toolkit.

## What Was Added

### 1. Screenwriter Skill
**Location:** `.claude/skills/screenwriter/`

**Files:**
- `SKILL.md` - Complete skill documentation (23KB)
- `examples.md` - Real-world script examples (14KB)
- `README.md` - Quick reference guide (4KB)

**Capabilities:**
- Professional narrative structure formulas
- Precise timing calculations (word count → duration)
- Genre-specific writing patterns (Product Demo, Sprint Review, Tutorial, etc.)
- Emotional arc design
- Brand voice alignment
- CTA (Call-to-Action) optimization

### 2. `/script` Command
**Location:** `.claude/commands/script.md`

**Features:**
- Project discovery and script creation workflow
- Per-scene script generation
- Timing analysis and validation
- A/B variations for hooks and CTAs
- Standalone script mode (no video project required)

## Installation Status

✅ **Fully Integrated** - Ready to use immediately

The skill and command are now part of your Claude Code Video Toolkit installation at:
```
/Users/romangasanov/Documents/Projects_coding/claude-code-video-toolkit/
```

## How to Use

### Quick Start

1. **Create a video project first** (if you haven't):
   ```
   /video
   ```

2. **Launch scriptwriting session**:
   ```
   /script
   ```

3. **Follow the interactive workflow**:
   - Claude discovers your project
   - Asks about audience and tone
   - Proposes scene structure
   - Writes scripts scene-by-scene
   - Saves to `public/audio/scenes/*.txt`

### Standalone Script (No Project)

```
/script new
```

Creates a script without a full video project setup.

## Key Features

### Narrative Structure Formulas

The skill includes proven patterns for different video types:

| Video Type | Formula | Use For |
|------------|---------|---------|
| **Product Demo** | Pain → Solution → Proof → Action | Marketing videos, launches |
| **Sprint Review** | Context → Shipped → Demo → Impact → Next | Team updates, release videos |
| **Tutorial** | Goal → Steps → Result → Gotchas | Educational content |
| **Case Study** | Challenge → Approach → Results → Takeaway | Customer stories |
| **Announcement** | Tease → Reveal → Impact → Access | Product launches |

### Timing Precision

Automatic word count calculation:
- **Standard pace:** 150 words/minute (2.5 words/second)
- **30 seconds** = ~75 words
- **60 seconds** = ~150 words
- **90 seconds** = ~225 words

Strategic pause insertion:
```
[pause 0.5s]  # Quick breath
[pause 1.0s]  # Emphasize point
[pause 1.5s]  # Scene transition
[pause 2.0s]  # Dramatic reveal
```

### Quality Principles

Scripts automatically follow best practices:
- ✅ Clarity over cleverness
- ✅ Benefits before features
- ✅ Active voice (not passive)
- ✅ Specific numbers (not vague claims)
- ✅ One idea per sentence
- ✅ Strategic pauses for impact

## Integration with Existing Workflow

### Before Using `/script`

1. **Create project** → `/video`
2. **Set brand** → `/brand` (optional but recommended)

### After `/script` Completes

1. **Generate voiceover** → `/generate-voiceover`
2. **Review timing** → `/scene-review`
3. **Refine visuals** → `/design`

## Example Workflow

```bash
# 1. Create video project
/video

# User selects: Product Demo template
# User provides: Feature list, metrics, target audience

# 2. Write professional script
/script

# Claude uses screenwriter skill to:
# - Propose structure (Pain → Solution → Proof → Action)
# - Calculate timing per scene
# - Write compelling narration
# - Save to public/audio/scenes/*.txt

# 3. Generate voiceover
/generate-voiceover

# 4. Review in Remotion Studio
/scene-review
```

## File Structure

After running `/script`, you'll have:

```
your-project/
├── public/
│   └── audio/
│       └── scenes/
│           ├── 01-hook.txt        # "Still waiting 30 minutes?"
│           ├── 02-problem.txt     # Pain amplification
│           ├── 03-solution.txt    # Product introduction
│           ├── 04-demo.txt        # Feature walkthrough
│           ├── 05-stats.txt       # Metrics and proof
│           └── 06-cta.txt         # Call-to-action
├── project.json                   # Updated with script status
└── VOICEOVER-SCRIPT.md           # Combined script (optional)
```

## Customization

### Brand Voice Integration

The skill automatically checks:
- `brands/{brand}/messaging.md` - Terminology and tone
- `brands/{brand}/voice-settings.json` - ElevenLabs voice config

Scripts will match your brand guidelines.

### Tone Variations

Available tones:
- **Professional** - Formal, measured, corporate
- **Conversational** - Casual, friendly, approachable
- **Technical** - Expert-level, proper terminology
- **Inspirational** - Aspirational, storytelling, dramatic
- **Energetic** - Fast-paced, exciting, celebration-focused

## Advanced Features

### A/B Hook Testing

Generate multiple hook variations:
```
Option A (Question): "Still waiting 30 minutes for builds?"
Option B (Bold Claim): "We just made deployment 10x faster."
Option C (Pain Point): "It's 5 PM. Your build broke. Again."
```

### Script Analysis

Automatic quality checks:
- Readability score
- Average sentence length
- Engagement hooks (questions, "you" usage)
- Emotional arc validation
- Timing accuracy

### Multi-Language Support

If your brand has multiple voice profiles, scripts can be generated for different languages.

## Examples

See `.claude/skills/screenwriter/examples.md` for:
- ✅ Complete product demo script (90 seconds)
- ✅ Sprint review script (120 seconds)
- ✅ Tutorial script (180 seconds)
- ✅ Before/after comparisons
- ✅ Tone variations by audience
- ✅ CTA formulas

## Comparison: Before vs After

### Before (Generic /video workflow)

**Process:**
1. Create project with `/video`
2. Claude writes basic narration during scene planning
3. User manually edits `VOICEOVER-SCRIPT.md`
4. No timing calculations
5. No narrative structure guidance

**Result:** Functional but often sounds like technical documentation

### After (With screenwriter skill)

**Process:**
1. Create project with `/video`
2. Run `/script` for professional scriptwriting
3. Claude applies narrative formulas
4. Automatic timing calculations
5. Strategic pause placement
6. Brand voice alignment

**Result:** Compelling narration with emotional arc and precise timing

## Troubleshooting

### Script Too Long?
```
/script
# Then say: "Scene 3 is 5 seconds too long, please shorten"
```

Claude will:
- Remove adjectives/adverbs
- Combine sentences
- Identify visual-only moments

### Sounds Robotic?
```
/script
# Then say: "Make scene 2 more conversational"
```

Claude will:
- Add contractions
- Vary sentence length
- Include natural phrases

### Weak Hook?
```
/script
# Then say: "Generate 3 hook variations"
```

Claude will provide A/B options.

## Performance Impact

**Skill Size:** 42KB (SKILL.md + examples.md + README.md)
**Command Size:** 17KB (script.md)
**Total Addition:** ~59KB

**Runtime:** No performance impact. Skills are loaded on-demand when `/script` is invoked.

## Version Compatibility

- **Claude Code:** Any version supporting skills
- **Video Toolkit:** v0.9.2+
- **Dependencies:** None (pure markdown instructions)

## Next Steps

### Immediate Use

Start using right away:
```
cd /Users/romangasanov/Documents/Projects_coding/claude-code-video-toolkit
claude-code  # or your preferred way to launch Claude Code
```

Then in Claude Code:
```
/video       # Create a project
/script      # Write professional script
```

### Contributing Back

This skill is custom-built but can be contributed to the official toolkit:

1. Test thoroughly with different video types
2. Gather feedback from real usage
3. Create PR to `github.com/digitalsamba/claude-code-video-toolkit`

## Feedback & Iteration

### Improve the Skill

Found a missing pattern or want to enhance it?

In Claude Code, say:
```
"Improve the screenwriter skill - add support for [use case]"
```

Claude will help you:
1. Update `SKILL.md`
2. Add examples to `examples.md`
3. Test the changes
4. Create a PR if desired

### Report Issues

If something doesn't work as expected:
- Check examples.md for similar use cases
- Verify brand voice files exist (if using)
- Ensure project.json is valid
- Try `/script new` for standalone testing

## Resources

**Skill Documentation:**
- `.claude/skills/screenwriter/SKILL.md` - Full documentation
- `.claude/skills/screenwriter/examples.md` - Real-world examples
- `.claude/skills/screenwriter/README.md` - Quick reference

**Command Documentation:**
- `.claude/commands/script.md` - Workflow guide

**Related Skills:**
- `remotion` - Video composition and rendering
- `elevenlabs` - Voiceover generation
- `frontend-design` - Visual refinement
- `ffmpeg` - Media processing

**Related Commands:**
- `/video` - Project creation
- `/generate-voiceover` - Audio generation
- `/scene-review` - Preview and timing check
- `/design` - Visual refinement

## Credits

**Created:** 2026-02-15
**Version:** 1.0.0
**Inspired by:**
- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) - Copywriting principles
- [obra/superpowers](https://github.com/obra/superpowers) - Content strategy patterns
- Professional screenwriting best practices

**Integrated into:** [Claude Code Video Toolkit](https://github.com/digitalsamba/claude-code-video-toolkit)

---

## Summary

You now have professional scriptwriting capabilities integrated into your video toolkit:

✅ **Screenwriter skill** - Expert knowledge for writing compelling video scripts
✅ **`/script` command** - Interactive workflow for script creation
✅ **Narrative formulas** - Proven structures for 5+ video types
✅ **Timing precision** - Automatic word count calculations
✅ **Brand alignment** - Consistent tone and terminology
✅ **Examples library** - Real-world reference scripts

**Start creating professional video scripts right now with `/script`**
