---
description: Professional scriptwriting session - create or refine voiceover scripts for video projects
---

# Script

Dedicated scriptwriting workflow using the screenwriter skill. Write compelling narration with proper timing, structure, and emotional arc.

## Purpose

Professional voiceover script creation:
- Convert raw content into engaging narratives
- Structure story flow with proven formulas
- Calculate precise timing and word counts
- Refine existing scripts for clarity and impact

## Usage

```
/script              # Discover project and write/refine script
/script new          # Create standalone script (no project)
/script [scene-id]   # Refine specific scene script
```

---

## Step 1: Discover Project Context

First, determine if working within a video project:

1. **Check current directory**
   - Look for `project.json` (active video project)
   - Look for `VOICEOVER-SCRIPT.md` (existing script)
   - Check `public/audio/scenes/*.txt` (per-scene scripts)

2. **Scan for projects** (if not in one)
   - Glob `projects/*/project.json`
   - Find projects in "planning" or "assets" phase (script-ready)
   - Sort by most recently updated

3. **Present options**

**If in an active project:**
```
## Script Session

**Project:** {project_name}
**Template:** {template_type}
**Phase:** {current_phase}

What would you like to do?

1. Write complete script (all scenes)
2. Refine existing script
3. Write script for specific scene
4. Review script timing/structure
```

**If projects found nearby:**
```
Found video projects:

1. **my-release-video** (sprint-review)
   Phase: planning
   Scenes: 5 planned, no scripts yet

2. **product-launch** (product-demo)
   Phase: assets
   Script: Partial (3 of 6 scenes)

Which project? (or 'new' for standalone script)
```

**If no project:**
```
No video project found. Create a script for:

1. New video project (with /video first)
2. Standalone script (narration only, no project)
```

If user chooses standalone, proceed to Standalone Script Flow.

---

## Step 2: Gather Content & Context

Before writing, collect necessary information:

### A. Read Existing Materials

**Check for:**
1. `VOICEOVER-SCRIPT.md` - Previous draft
2. `project.json` - Scene structure, target durations
3. `brands/{brand}/messaging.md` - Brand voice guidelines
4. `brands/{brand}/voice-settings.json` - ElevenLabs voice config
5. Template config (if project-based):
   - `src/config/sprint-config.ts`
   - `src/config/demo-config.ts`

**Don't ask for information already present in these files.**

### B. Ask Clarifying Questions (if needed)

If critical context is missing, ask ONE question at a time:

**1. Purpose & Goal**
```
What should viewers do after watching this video?

Examples:
- Sign up for trial
- Understand new features
- Feel excited about sprint results
- Learn how to implement feature X
```

**2. Audience**
```
Who is the primary audience?

A. Developers/engineers
B. Product managers
C. Customers/end-users
D. Executives/investors
E. Mixed audience
```

**3. Tone Preference** (if not in brand guide)
```
What tone should the narration use?

| Tone | Example |
|------|---------|
| Professional | Formal, measured, third-person OK |
| Conversational | Casual, friendly, contractions welcome |
| Technical | Assume expertise, use proper terminology |
| Inspirational | Aspirational, storytelling, dramatic pauses |
| Energetic | Fast-paced, exciting, celebration-focused |
```

**4. Raw Content** (if not in config)
```
What content should the script cover?

You can provide:
- Release notes or changelog
- Feature descriptions
- URLs (docs, GitHub, blog posts)
- Bullet points or rough outline
- Existing text to adapt
```

If URL provided, fetch content and parse key points.

---

## Step 3: Plan Scene Structure

Using the **screenwriter skill**, analyze content and propose scene breakdown:

### A. Choose Narrative Structure

Based on video type, select proven formula:

| Video Type | Structure | Key Scenes |
|------------|-----------|------------|
| **Product Demo** | Pain → Solution → Proof → Action | Problem, Solution, Features, Testimonial, CTA |
| **Sprint Review** | Context → Shipped → Demo → Impact → Next | Recap, Features, Demo, Metrics, Forward Look |
| **Tutorial** | Goal → Steps → Result → Gotchas | Hook, Prerequisites, Walkthrough, Result, Tips |
| **Case Study** | Challenge → Approach → Results → Takeaway | Customer, Problem, Solution, Outcomes, Quote |
| **Announcement** | Tease → Reveal → Impact → Access | Curiosity, Announcement, Why It Matters, How to Get |

### B. Propose Scene Breakdown

Present a structured outline:

```
## Proposed Script Structure

**Total Duration Target:** ~120 seconds (based on {fps * durationInFrames})

| # | Scene | Type | Duration | Word Count | Key Message |
|---|-------|------|----------|------------|-------------|
| 1 | Hook | hook | 5s | ~12 words | "Deployment taking 30 minutes? Not anymore." |
| 2 | Problem | problem | 15s | ~35 words | Explain frustration of slow deploys |
| 3 | Solution | solution | 10s | ~25 words | Introduce product name and core benefit |
| 4 | Demo | demo | 40s | ~80 words | Narrate key actions, let visuals lead |
| 5 | Stats | stats | 20s | ~50 words | Quantified improvements, metrics |
| 6 | CTA | cta | 10s | ~25 words | "Start your free trial - link below" |

**Formula Used:** Product Demo (Pain → Solution → Proof → Action)

Adjustments needed?
```

### C. Iterate Structure

Allow user to:
- Add/remove scenes
- Adjust durations
- Reorder sequence
- Change scene types

Update breakdown based on feedback.

---

## Step 4: Write Per-Scene Scripts

For each scene, create narration text:

### A. Calculate Word Budget

Using **150 words per minute** (2.5 words/second):

```
Scene duration: 15 seconds
Word budget: 15 × 2.5 = ~38 words
Account for pauses: -3 words per second of silence
Final budget: ~35 words
```

### B. Apply Scene-Specific Principles

**Hook (3-5 seconds):**
- Problem question or bold claim
- Front-load value immediately
- Examples: "Still waiting 30 minutes?" / "We just made it 10x faster."

**Problem (15-25 seconds):**
- Empathetic, relatable pain
- Amplify frustration without being negative
- Transition to hope

**Solution (10-20 seconds):**
- Introduce product/feature name
- Lead with benefit, not description
- Confident tone

**Demo (30-90 seconds):**
- Narrate key actions visible on screen
- 30-50% coverage (let visuals breathe)
- Use present tense: "Watch this - the build starts..."

**Stats (15-25 seconds):**
- Specific numbers, not vague claims
- Comparison context: "Down from 4.2s to 1.8s"
- One stat per sentence

**CTA (5-10 seconds):**
- Action verb + benefit + friction reducer
- Examples: "Start your free trial - no credit card needed"

### C. Write Draft Text

For each scene, produce:

```
[Scene 02: Problem - Target 15 seconds]

Every deploy means context switching. Waiting. Wondering if something broke. [pause 0.5s]

Your team deserves better.

[Word count: 18 words + 0.5s pause = ~10 seconds actual]
[Note: Under budget - good, allows for natural pacing]
```

### D. Review Scene-by-Scene

After each scene draft:
1. Read aloud (check natural flow)
2. Verify word count vs. duration
3. Check alignment with visual (if specified)
4. Ensure tone consistency

Present each scene for approval before proceeding to next.

---

## Step 5: Create Script Files

### Option A: Per-Scene Files (Recommended)

Create individual text files in `public/audio/scenes/`:

```bash
public/audio/scenes/
├── 01-hook.txt
├── 02-problem.txt
├── 03-solution.txt
├── 04-demo.txt
├── 05-stats.txt
└── 06-cta.txt
```

**Benefits:**
- Regenerate individual scenes without re-recording all
- Easier iteration ("make scene 3 more energetic")
- More cost-effective with ElevenLabs API

**File format:**
```
Still waiting 30 minutes for builds?

Those days are over.
```
(Clean text, no metadata in file)

### Option B: Combined Script (Legacy)

Create single `VOICEOVER-SCRIPT.md`:

```markdown
# Voiceover Script: Product Demo

## Scene 01: Hook (5 seconds)

Still waiting 30 minutes for builds?

Those days are over.

---

## Scene 02: Problem (15 seconds)

Every deploy means context switching. Waiting. Wondering if something broke. [pause 0.5s]

Your team deserves better.

---

## Scene 03: Solution (10 seconds)

...
```

**Use this if:**
- User prefers single file
- Script will be used by human narrator (not TTS)
- Legacy project already uses this format

---

## Step 6: Update Project Metadata

If working within a video project:

### A. Update project.json

```json
{
  "phase": "audio",  // Advance from "planning" to "audio"
  "scenes": [
    {
      "id": "hook",
      "narration": {
        "text": "Still waiting 30 minutes for builds? Those days are over.",
        "wordCount": 10,
        "estimatedDuration": 5,
        "file": "public/audio/scenes/01-hook.txt",
        "status": "script-ready"
      }
    }
  ],
  "sessions": [
    {
      "date": "2026-02-15",
      "summary": "Created complete voiceover script using screenwriter skill"
    }
  ],
  "updated": "2026-02-15T10:30:00Z"
}
```

### B. Regenerate CLAUDE.md

Update project context file with:
- Script completion status
- Word counts and durations per scene
- Next action: "Generate voiceover with /generate-voiceover"

---

## Step 7: Review & Iterate

Present completed script with analysis:

```
## Script Complete

Created {N} scene scripts totaling {X} words (~{Y} seconds)

### Timing Analysis

| Scene | Target | Actual | Status |
|-------|--------|--------|--------|
| Hook | 5s | 4s | ✅ Under (good pacing) |
| Problem | 15s | 16s | ⚠️ Slightly over |
| Solution | 10s | 9s | ✅ On target |
| Demo | 40s | 38s | ✅ On target |
| Stats | 20s | 22s | ⚠️ Slightly over |
| CTA | 10s | 8s | ✅ Under (good) |

**Total:** Target 100s, Actual 97s ✅

### Brand Alignment

- Tone: ✅ Conversational (matches brand guidelines)
- Terminology: ✅ Consistent with product docs
- Voice: ✅ Active voice throughout

### Recommendations

1. **Scene 02 (Problem):** Consider removing "without a doubt" (-3 words) to hit target
2. **Scene 05 (Stats):** Currently 22s - could trim adjectives to reach 20s exactly

Would you like to:
- Refine specific scenes
- Generate voiceover audio (/generate-voiceover)
- Preview in Remotion Studio (/scene-review)
- Make edits
```

### Allow Refinements

User can request:
- "Make scene 3 more energetic"
- "Shorten scene 5 by 5 seconds"
- "Add a pause after the first sentence in scene 2"
- "Make the hook more compelling"
- "Simplify the technical language in scene 4"

Iterate using screenwriter skill principles.

---

## Standalone Script Flow

If user chose to create script without a video project:

### 1. Gather Requirements

```
Let's create a standalone script.

What's the purpose of this narration?

Examples:
- Product demo for website
- Voiceover for external video
- Podcast intro/outro
- Presentation narration
```

### 2. Collect Details

Ask one at a time:
1. Target duration (seconds or minutes)
2. Audience (who's listening?)
3. Tone preference
4. Content to cover (bullet points, URL, or raw text)

### 3. Write Script

Follow same principles but without project structure:
- Apply appropriate narrative formula
- Calculate word count from duration
- Structure with clear beginning/middle/end
- Include pauses and timing notes

### 4. Save Standalone File

```
Save as: standalone-script-YYYY-MM-DD.md
Location: Current directory or user-specified path
```

Include metadata header:

```markdown
---
created: 2026-02-15
purpose: Product demo voiceover
duration: 90 seconds
audience: Developers
tone: Conversational
word_count: 225
---

# Standalone Script

[Hook - 5s]
Still waiting 30 minutes for builds?

...
```

---

## Advanced Features

### A/B Script Variations

For critical moments (hook, CTA), offer alternatives:

```
## Hook Variations

Which opening resonates most with your audience?

**Option A (Question):**
"Still waiting 30 minutes for builds to finish?"

**Option B (Bold Claim):**
"We just made deployment 10x faster."

**Option C (Relatable Pain):**
"It's 5 PM. Your build broke. Again."

Choose option or request another variation.
```

### Script Analysis

Provide detailed breakdown:

```
## Script Analysis

**Readability:**
- Average sentence length: 8 words (✅ conversational)
- Longest sentence: 14 words (✅ digestible)
- Reading level: 7th grade (✅ accessible)

**Engagement Hooks:**
- Opens with question (✅ attention-grabbing)
- Uses "you" 8 times (✅ direct address)
- Includes 3 specific numbers (✅ credibility)

**Emotional Arc:**
- Start: Frustration (relatable problem)
- Middle: Hope (solution appears)
- End: Confidence (clear path forward)
✅ Complete arc

**Potential Issues:**
- Scene 4: Word "utilize" (replace with "use")
- Scene 6: Generic CTA (add specific benefit)
```

### Multi-Language Support

If brand has multiple voice profiles:

```
## Voice Profiles Available

Which language/voice for this script?

1. **English (US)** - Mark (conversational male)
2. **English (UK)** - Charlotte (professional female)
3. **Spanish** - Diego (energetic male)

(Voice settings from brands/{brand}/voice-settings.json)
```

---

## Integration Points

### Before Scriptwriting
- **Dependencies:** `/video` (create project structure)
- **Brand setup:** `/brand` (ensure voice guidelines exist)
- **Template choice:** Determines narrative structure

### After Scriptwriting
- **Generate audio:** `/generate-voiceover` (TTS from script)
- **Visual sync:** `/scene-review` (check timing in Remotion)
- **Refinement:** `/design` (ensure visuals match narration)

### Parallel Workflows
- **Recording demos:** Can happen while script is being written
- **Music selection:** Independent of narration

---

## Best Practices

### 1. Always Read Aloud
Before finalizing, read scripts aloud at natural pace. Text that looks good may sound awkward.

### 2. Account for Visuals
If scene shows complex UI/code, reduce narration density. Let viewers watch.

### 3. Front-Load Value
Put critical information in first 30 seconds. Retention drops over time.

### 4. Test with Target Audience
Before recording, get feedback from someone matching your audience profile.

### 5. Iterate Ruthlessly
First drafts are always too long. Cut 20%, add specifics, sharpen hooks.

### 6. Preserve Brand Voice
Check `brands/{brand}/messaging.md` for terminology, tone, and voice guidelines.

---

## Troubleshooting

### Script Too Long
**Symptoms:** Word count exceeds target by >15%

**Fixes:**
1. Remove adjectives and adverbs
2. Combine short sentences
3. Cut redundant phrases
4. Identify scenes that can be visual-only

### Script Feels Robotic
**Symptoms:** Sounds unnatural when read aloud

**Fixes:**
1. Add contractions (you'll, we're, it's)
2. Vary sentence length
3. Include conversational phrases ("Here's the thing...")
4. Add strategic pauses

### Weak Hook
**Symptoms:** Opening doesn't grab attention

**Fixes:**
1. Start with question instead of statement
2. Lead with biggest benefit
3. Use unexpected stat or claim
4. Create curiosity gap

### Boring Ending
**Symptoms:** No clear next step

**Fixes:**
1. Add explicit CTA with benefit
2. Create urgency (if genuine)
3. Remove generic "thanks for watching"
4. End with forward-looking statement

---

## When to Use This Command

Use `/script` when:

✅ Planning narration for new video project
✅ Converting raw content (release notes, specs) into script
✅ Refining existing script for timing/clarity
✅ Creating standalone voiceover (no video project)
✅ Writing narration for specific scene
✅ Ensuring brand voice consistency
✅ A/B testing different narrative approaches

**Don't use for:**
❌ Visual design (use `/design`)
❌ Video editing (use Remotion directly)
❌ Audio generation (use `/generate-voiceover`)
❌ Demo recording (use `/record-demo`)

---

## Quick Reference

### Timing Formulas
- **Standard pace:** 150 words/minute (2.5 words/second)
- **30 seconds:** ~75 words
- **60 seconds:** ~150 words
- **1-second pause:** subtract 2-3 words

### Scene Duration Guidelines
- Hook: 3-5 seconds
- Problem: 15-25 seconds
- Solution: 10-20 seconds
- Demo: 30-90 seconds
- Stats: 15-25 seconds
- CTA: 5-10 seconds

### Narrative Structures
- **Product Demo:** Pain → Solution → Proof → Action
- **Sprint Review:** Context → Shipped → Demo → Impact → Next
- **Tutorial:** Goal → Steps → Result → Gotchas
- **Case Study:** Challenge → Approach → Results → Takeaway

### Writing Principles
1. Clarity over cleverness
2. Benefits before features
3. Active voice
4. Specific numbers/examples
5. One idea per sentence
6. Front-load value

---

## Feedback & Improvements

If this command workflow could be better:

- **Missing a step?** Describe what's unclear
- **Wrong assumptions?** Let me know your use case
- **Want to contribute?** I can help you update this file

Say "improve /script command" and I'll guide you through editing this file and contributing to the toolkit.
