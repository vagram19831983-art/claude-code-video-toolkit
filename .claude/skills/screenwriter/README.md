# Screenwriter Skill

Professional video scriptwriting for Claude Code Video Toolkit.

## What It Does

Transforms raw content into compelling video scripts with:
- **Proper timing** - Word counts calculated for exact durations
- **Proven structures** - Genre-specific narrative formulas
- **Emotional arcs** - Engagement patterns that keep viewers watching
- **Brand alignment** - Consistent tone and terminology

## Quick Start

### Use the `/script` command:

```
/script              # Start scriptwriting session
/script new          # Create standalone script
/script [scene-id]   # Refine specific scene
```

The command will:
1. Discover your project context
2. Gather content and requirements
3. Propose narrative structure
4. Write scene-by-scene scripts
5. Save to `public/audio/scenes/*.txt`

## Core Principles

1. **Clarity over cleverness** - Simple beats wordplay
2. **150 words per minute** - Standard speaking pace
3. **Hook in 3 seconds** - Grab attention immediately
4. **Benefits before features** - Viewers care about outcomes
5. **Active voice** - "We encrypt" not "is encrypted by"
6. **Specific numbers** - "60 seconds" not "fast"

## Narrative Structures

Different video types use proven formulas:

| Type | Structure |
|------|-----------|
| **Product Demo** | Pain → Solution → Proof → Action |
| **Sprint Review** | Context → Shipped → Demo → Impact → Next |
| **Tutorial** | Goal → Steps → Result → Gotchas |
| **Case Study** | Challenge → Approach → Results → Takeaway |
| **Announcement** | Tease → Reveal → Impact → Access |

## Timing Calculator

```
30 seconds = ~75 words
60 seconds = ~150 words
90 seconds = ~225 words
120 seconds = ~300 words

Add pauses:
[pause 0.5s] = -1 word
[pause 1.0s] = -2-3 words
```

## File Structure

The skill creates per-scene scripts:

```
public/audio/scenes/
├── 01-hook.txt        "Still waiting 30 minutes for builds?"
├── 02-problem.txt     "Every deploy means context switching..."
├── 03-solution.txt    "Meet TurboDeploy - 60 seconds or less."
├── 04-demo.txt        "Watch this. From push to deployed..."
└── 05-cta.txt         "Start your free trial - link below."
```

**Benefits:**
- Regenerate individual scenes without re-recording all
- Easier iteration ("make scene 3 more energetic")
- Cost-effective ElevenLabs API usage

## Examples

See [examples.md](examples.md) for:
- Product demo scripts
- Sprint review scripts
- Tutorial scripts
- Before/after comparisons
- Tone variations by audience
- CTA formulas

## Integration

### Before Scriptwriting
- Create project with `/video`
- Set up brand with `/brand`

### After Scriptwriting
- Generate audio: `/generate-voiceover`
- Review sync: `/scene-review`
- Refine visuals: `/design`

## Best Practices

✅ Read scripts aloud before finalizing
✅ Account for visuals (reduce narration when showing complex UI)
✅ Front-load value (critical info in first 30 seconds)
✅ Use strategic pauses (let impressive moments breathe)
✅ Iterate ruthlessly (first drafts are always too long)

❌ Don't fabricate metrics
❌ Don't use passive voice
❌ Don't overload with jargon
❌ Don't rush impressive claims

## Quick Reference

### Scene Duration Guidelines
- Hook: 3-5 seconds
- Problem: 15-25 seconds
- Solution: 10-20 seconds
- Demo: 30-90 seconds
- Stats: 15-25 seconds
- CTA: 5-10 seconds

### Writing Checklist
- [ ] Hook grabs attention in 3 seconds
- [ ] Benefits before features
- [ ] Active voice throughout
- [ ] Specific numbers/examples
- [ ] One idea per sentence
- [ ] Clear CTA at end
- [ ] Timing matches target duration

## Troubleshooting

**Script too long?**
- Cut adjectives/adverbs
- Combine short sentences
- Identify visual-only moments

**Sounds robotic?**
- Add contractions (you'll, we're)
- Vary sentence length
- Include conversational phrases

**Weak hook?**
- Start with question
- Lead with biggest benefit
- Use unexpected stat

## Files

- **SKILL.md** - Complete skill documentation
- **examples.md** - Real-world script examples
- **README.md** - This file

## Feedback

Found a missing pattern or want to contribute?

Say "improve screenwriter skill" and Claude will help you update the skill and create a PR.

---

**Part of:** [Claude Code Video Toolkit](https://github.com/digitalsamba/claude-code-video-toolkit)
**Created:** 2026-02-15
**Version:** 1.0.0
