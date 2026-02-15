---
name: screenwriter
description: Professional video scriptwriting and narrative design. Use when creating voiceover scripts, planning video narratives, structuring story flow, or converting raw content into compelling video scripts. Triggers include writing narration for product demos, sprint reviews, tutorials, case studies, or any video requiring professional storytelling with proper timing, emotional arc, and audience engagement.
---

# Screenwriter

Professional scriptwriting for video content. Transforms raw material into compelling narratives with proper timing, emotional resonance, and clear calls-to-action.

## Core Principles

**Clarity over cleverness** - Simple, direct language beats wordplay. Viewers must understand instantly.

**Show, don't tell** - Write for what viewers will *see*, not abstract concepts. Narration complements visuals, doesn't replace them.

**Timing is everything** - Video narration has strict time constraints. Every word must earn its place.

**Hook within 3 seconds** - Viewers decide to stay or leave immediately. Open with immediate value or intrigue.

---

## Timing & Duration Formulas

### Speaking Rate Standards

| Pace | Words/Minute | Best For |
|------|--------------|----------|
| **Slow (Explanatory)** | 120-130 WPM | Complex technical concepts, tutorials |
| **Standard (Conversational)** | 140-160 WPM | Most product demos, reviews, features |
| **Fast (Energetic)** | 160-180 WPM | High-energy intros, montages, celebrations |

**Default assumption: 150 words per minute (2.5 words per second)**

### Quick Duration Calculations

```
30 seconds = ~75 words
60 seconds = ~150 words
90 seconds = ~225 words
120 seconds = ~300 words
```

### Adding Pauses for Impact

Strategic silence enhances key moments:

```
[pause 0.5s]   - Quick breath between thoughts
[pause 1.0s]   - Emphasize important point
[pause 1.5s]   - Transition between major sections
[pause 2.0s]   - Dramatic reveal, let visuals speak
```

**Account for pauses in word count:**
- 1-second pause = subtract 2-3 words from available count
- Visual-only segments need no narration (budget 0 words)

---

## Pre-Writing Research

Before drafting, gather context across these dimensions:

### 1. Purpose & Goals
- What action should viewers take after watching?
- What's the single most important message?
- Success metric (views? conversions? understanding?)

### 2. Audience Understanding
- Who watches this? (developers, managers, customers, investors)
- What's their existing knowledge level?
- What do they care about most?
- What objections or skepticism do they have?

### 3. Content Inventory
Collect raw materials:
- Release notes, changelogs, feature specs
- Demo recordings or screenshots
- Metrics, testimonials, data points
- Company messaging, brand voice docs

### 4. Visual Context
- What will viewers see during narration?
- Which moments need silence (let visuals speak)?
- Where do UI demos, stats, or b-roll appear?

**Check for existing documentation before asking questions.** Look for:
- `project.json` (video toolkit project metadata)
- `VOICEOVER-SCRIPT.md` (previous draft)
- Brand voice guides in `brands/` directory
- Template configs in `src/config/`

---

## Narrative Structure Formulas

Different video types follow proven story patterns:

### Product Demo (Marketing Focus)

```
Structure: Pain → Solution → Proof → Action

1. Hook (3-5 sec): Open with customer pain point
   "Deploying code still takes 45 minutes?"

2. Problem (10-15 sec): Amplify the frustration
   "Every deploy means context switching, waiting, wondering if it broke."

3. Solution Intro (5-10 sec): Introduce your product
   "Meet [Product] - deployment in under 60 seconds."

4. Feature Tour (40-60 sec): Show 3-5 key capabilities
   - Each feature = problem it solves (not just what it does)
   - Use specifics: "Deploy to 12 regions" not "Global deployment"

5. Social Proof (10-15 sec): Testimonial or metric
   "[Company] shipped 3x faster in their first week."

6. CTA (5-10 sec): Clear next step
   "Start your free trial - no credit card needed."
```

### Sprint Review (Team Update)

```
Structure: Context → Shipped → Demo → Impact → Next

1. Opening (5 sec): Sprint ID and theme
   "Sprint 47: Mobile Performance"

2. Recap (10-15 sec): What we set out to do
   "We committed to cutting app load time in half."

3. Shipped Features (20-30 sec): What got delivered
   - 3-5 bullet points
   - Focus on outcomes, not implementation details

4. Demo (60-90 sec): Show the most impressive feature
   - Narrate what's visible: "Watch the loading spinner - under 2 seconds."

5. Metrics (15-20 sec): Quantified impact
   "Load time dropped from 4.2s to 1.8s. That's 57% faster."

6. Next Sprint (10 sec): Forward look
   "Sprint 48 tackles offline mode. See you in two weeks."
```

### Tutorial (Educational)

```
Structure: Goal → Prerequisites → Steps → Result → Gotchas

1. Hook (5 sec): What they'll accomplish
   "Build a real-time chat app in 10 minutes."

2. Prerequisites (5-10 sec): What they need first
   "You'll need Node.js and a free account."

3. Step-by-Step (60-120 sec): Walkthrough
   - One step per scene (easier to edit)
   - Explain *why* not just *what*
   - Anticipate confusion: "This might look wrong, but..."

4. Result (10-15 sec): Show the working outcome
   "And there it is - messages flowing in real time."

5. Troubleshooting (10-20 sec): Common issues
   "If you see a connection error, check your API key."

6. Next Steps (5 sec): Where to go deeper
   "Add authentication in part 2."
```

### Case Study (Customer Story)

```
Structure: Challenge → Approach → Results → Takeaway

1. Customer Intro (5-10 sec): Who they are
   "[Company] processes 50 million transactions daily."

2. Challenge (15-20 sec): Their specific problem
   "Their legacy system couldn't scale past 10K requests/sec."

3. Solution Approach (30-40 sec): What they did
   - Why they chose your product
   - Implementation highlights (not boring details)

4. Results (20-30 sec): Measurable outcomes
   "100K requests/sec. 99.99% uptime. Zero downtime migrations."

5. Quote (10-15 sec): Customer voice
   "'We couldn't have scaled this fast without [Product].'"

6. Takeaway (5 sec): Universal lesson
   "Infrastructure shouldn't limit ambition."
```

### Announcement (Launch/Release)

```
Structure: Tease → Reveal → Why It Matters → Access

1. Tease (3-5 sec): Create curiosity
   "We've been building something new."

2. Reveal (5-10 sec): The announcement
   "Today, we're launching [Feature]."

3. Problem It Solves (15-20 sec): Why this matters
   "Until now, [pain point] meant [consequence]."

4. How It Works (30-45 sec): Core mechanism
   - Simple explanation, avoid jargon
   - Show, don't just describe

5. Who It's For (10-15 sec): Target audience
   "Perfect for teams shipping mobile apps."

6. Availability (5-10 sec): How to get it
   "Available today in your dashboard."
```

---

## Script Writing Principles

### 1. Write for the Ear, Not the Eye

**Bad:** "Utilize our innovative solution to optimize your workflow efficiency."
**Good:** "Get more done, faster."

- Read scripts aloud while writing
- Remove words you'd never say in conversation
- Break long sentences into short ones

### 2. Benefits Over Features

Viewers don't care *what* it does, they care *what it means for them*.

**Bad:** "Now with multi-threaded rendering."
**Good:** "Your exports finish in half the time."

Formula: `[Feature] → so you can → [Outcome they want]`

### 3. Specificity Beats Vagueness

Numbers, names, and concrete details feel credible.

**Bad:** "Much faster performance."
**Good:** "Load time dropped from 4 seconds to under 1."

**Bad:** "Many customers love it."
**Good:** "3,000 teams deployed this in the first month."

### 4. Active Voice

Passive voice sounds corporate and distant.

**Bad:** "Your data is encrypted by our system."
**Good:** "We encrypt your data end-to-end."

### 5. One Idea Per Sentence

Each sentence should advance the narrative once.

**Bad:** "Our platform, which was built from the ground up with security in mind, offers enterprise-grade encryption while maintaining fast performance."

**Good:** "Security built in from day one. Enterprise-grade encryption that doesn't slow you down."

### 6. Confident Tone

Remove qualifiers that undermine credibility.

**Weak:** "We think this might help you be more productive."
**Strong:** "This makes you more productive."

Avoid: very, quite, rather, pretty, somewhat, fairly, almost, nearly

### 7. Never Fabricate

- Don't invent metrics you don't have
- Don't quote customers who didn't say it
- Don't claim features that aren't ready

If data is missing, use a different angle. Integrity matters.

---

## Scene-by-Scene Structure

### Scene Types & Their Purpose

| Scene Type | Duration | Purpose | Narration Style |
|------------|----------|---------|-----------------|
| **Title** | 3-5 sec | Establish topic | Title only, no narration |
| **Hook** | 5-10 sec | Grab attention | Question or bold statement |
| **Overview** | 15-30 sec | Set context | Conversational, orienting |
| **Problem** | 15-25 sec | Establish pain | Empathetic, relatable |
| **Solution** | 10-20 sec | Introduce product | Clear, confident |
| **Feature** | 20-40 sec | Explain capability | Specific, outcome-focused |
| **Demo** | 30-90 sec | Show in action | Descriptive, minimal (let visuals lead) |
| **Stats** | 15-25 sec | Prove impact | Factual, impressive |
| **Testimonial** | 10-20 sec | Customer voice | Quote verbatim, authentic |
| **CTA** | 5-10 sec | Drive action | Direct, benefit-forward |
| **Credits** | 3-5 sec | Attribution | Silent or minimal |

### Writing Per-Scene Scripts

Create individual `.txt` files in `public/audio/scenes/`:

```
public/audio/scenes/
├── 01-hook.txt          "Still waiting 30 minutes for builds?"
├── 02-problem.txt       "Every minute waiting is a minute not shipping..."
├── 03-solution.txt      "Meet Turbo - builds in under 60 seconds..."
├── 04-demo.txt          "Watch this - from git push to deployed..."
├── 05-cta.txt           "Start building faster today. Link below."
```

**Benefits of per-scene files:**
- Regenerate one scene without re-recording entire video
- Easier iteration ("Make scene 3 more energetic")
- Individual ElevenLabs API calls (cheaper, faster)

### Narration Density by Scene Type

| Scene Type | Narration Coverage | Rationale |
|------------|-------------------|-----------|
| **Title/Credits** | 0-10% | Visuals + music only |
| **Demo/Screencap** | 30-50% | Let viewers watch, narrate key actions |
| **Stats/Slides** | 70-90% | Visuals are simple, narration carries content |
| **Talking Head** | 90-100% | Person is speaking, narration = their words |

**Rule of thumb:** If the visual is complex (code, UI), reduce narration. If the visual is simple (text slide), narration can be dense.

---

## Voice & Tone Guidelines

Match tone to audience and content type:

### Corporate/Professional
- Formal but not stiff
- Third-person acceptable ("The team delivered...")
- Measured pace, avoid slang
- **Example:** "This quarter's release introduces three enterprise capabilities designed for regulated industries."

### Conversational/Friendly
- First-person or direct address ("We built..." / "You'll see...")
- Contractions welcome (you'll, we're, it's)
- Slightly faster pace, casual language
- **Example:** "We've been working on this for months, and we think you're going to love it."

### Technical/Developer
- Assume knowledge, skip basic explanations
- Use correct terminology (don't dumb down)
- Focus on "how" and "why"
- **Example:** "The new runtime uses incremental compilation with aggressive tree-shaking, cutting bundle size by 40%."

### Inspirational/Visionary
- Aspirational language
- Metaphors and storytelling
- Slower pace, dramatic pauses
- **Example:** "Imagine a world where deployment fear is a distant memory. [pause] That world starts today."

### Energetic/Hype
- Exclamations, punchy sentences
- Fast pace, momentum-building
- Celebrate achievements
- **Example:** "Look at that! Twelve features. Two weeks. Zero bugs. This team is unstoppable."

**Consistency matters.** Choose one tone and stick with it across all scenes. Jarring shifts break immersion.

---

## Hooks & Openings

The first 3-5 seconds determine if viewers keep watching.

### Hook Formulas

**1. Problem Question**
```
"Still manually testing every deployment?"
"Tired of waiting hours for CI to finish?"
```

**2. Bold Claim**
```
"We just made deployment 10x faster."
"This changes everything about mobile analytics."
```

**3. Curiosity Gap**
```
"We've been hiding a secret feature for months."
"What if I told you onboarding could take 30 seconds?"
```

**4. Relatable Pain**
```
"It's 5 PM. Your build is broken. Again."
"You've written the same boilerplate 100 times."
```

**5. Impressive Stat**
```
"47,000 developers switched in the last 30 days."
"99.99% uptime. Across 12 million requests per second."
```

**Bad hooks to avoid:**
- "Hi, I'm [name] from [company]..." (nobody cares yet)
- "In this video I'm going to show you..." (boring)
- Long-winded context before getting to the point

---

## Calls-to-Action (CTAs)

### CTA Formula

`[Action Verb] + [Specific Benefit] + [Friction Reducer]`

**Examples:**

| Weak CTA | Strong CTA |
|----------|------------|
| "Learn more" | "See the full demo - watch now" |
| "Get started" | "Start your free trial - no credit card required" |
| "Click here" | "Download the migration guide - it's free" |
| "Contact us" | "Talk to an engineer - book a 15-minute call" |

### Reducing Friction

Add qualifiers that remove hesitation:

- "No credit card needed"
- "Free for 30 days"
- "Cancel anytime"
- "5-minute setup"
- "No installation required"

### Urgency (Use Sparingly)

Only if genuinely time-limited:

- "Offer ends Friday"
- "Limited beta slots remaining"
- "Early access closes at midnight"

**Never fake urgency.** It damages trust.

---

## Iteration & Review

### Self-Editing Checklist

After drafting, review for:

**1. Timing**
- [ ] Word count matches target duration (±10%)
- [ ] Pauses are marked where needed
- [ ] No run-on sentences that rush the reader

**2. Clarity**
- [ ] Every sentence has one clear idea
- [ ] No jargon without explanation (unless technical audience)
- [ ] Active voice used throughout

**3. Engagement**
- [ ] Hook grabs attention in first 3 seconds
- [ ] Benefits mentioned before features
- [ ] Specific examples replace vague claims

**4. Flow**
- [ ] Logical progression between sentences
- [ ] Transitions between scenes feel natural
- [ ] No abrupt topic changes

**5. Brand Alignment**
- [ ] Tone matches brand voice (check `brands/` directory)
- [ ] Terminology consistent with product docs
- [ ] No off-brand language

### Common Issues & Fixes

| Problem | Fix |
|---------|-----|
| Script feels too long | Cut adjectives, combine sentences, remove redundancy |
| Sounds robotic | Add contractions, conversational phrases, vary sentence length |
| Too much information | Focus on 1-3 key points, save details for docs |
| Boring opening | Start with question, stat, or bold statement |
| Weak ending | Add clear CTA with benefit, not generic "thanks for watching" |

### A/B Variations

For critical moments (hook, CTA), draft 2-3 alternatives:

**Hook options:**
1. "Deployment doesn't have to be scary."
2. "What if deploys took 60 seconds, not 60 minutes?"
3. "We just eliminated deployment downtime. Completely."

Ask: Which creates more curiosity? Which resonates with the target audience?

---

## Integration with Video Toolkit

### File Locations

**Per-scene scripts (recommended):**
```
public/audio/scenes/
├── 01-title.txt
├── 02-hook.txt
├── 03-feature-demo.txt
└── 04-cta.txt
```

**Combined script (legacy):**
```
VOICEOVER-SCRIPT.md
```

### Script Metadata

Include timing annotations in scripts:

```
[Scene 02: Hook - Target 8 seconds]

Still waiting 30 minutes for your builds to finish? [pause 1.0s]

Those days are over.

[Duration: ~6 seconds + 1s pause = 7s total]
```

### Voiceover Generation

After script approval, generate audio:

```bash
# Per-scene generation (recommended)
python tools/voiceover.py --scene-dir public/audio/scenes --json

# Single file generation
python tools/voiceover.py --script VOICEOVER-SCRIPT.md --output public/voiceover.mp3
```

### Brand Voice Integration

Check `brands/[brand-name]/` for:
- `voice-settings.json` - ElevenLabs voice ID, stability, similarity
- `messaging.md` - Brand voice guidelines, terminology
- `tone.md` - Preferred tone (professional, casual, technical)

Use these to inform script style and voice generation.

---

## Best Practices

### 1. Write Visually

Narration should complement what's on screen, not duplicate it.

**Bad:**
```
Visual: Dashboard showing "1.2s load time"
Narration: "The dashboard shows a load time of one point two seconds."
```

**Good:**
```
Visual: Dashboard showing "1.2s load time"
Narration: "Under 1.5 seconds - fast enough that users don't even notice."
```

### 2. Respect Silence

Some moments don't need narration. Let impressive visuals speak:

- Impressive animations
- Before/after comparisons (pause, let them see)
- Emotional moments (music + visuals)

### 3. Front-Load Value

Put the most important information early. Viewers drop off over time.

**Retention curve:**
- First 10 seconds: 100% watching
- At 30 seconds: ~70% remain
- At 60 seconds: ~45% remain
- At 120 seconds: ~25% remain

Say your most critical point in the first 30 seconds.

### 4. Vary Sentence Length

Mix short punchy sentences with longer explanatory ones. Creates rhythm.

**Monotonous:**
"This is fast. This is secure. This is scalable. This is the future."

**Better:**
"Fast. Secure. Scalable. This is the deployment platform we've been waiting for."

### 5. Test with Target Audience

Before finalizing, get feedback from someone who matches your audience:

- Do they understand the message?
- What's the one thing they remember?
- Where did they get confused or lose interest?

### 6. Iterate Ruthlessly

First drafts are always too long and too vague. Cut 20%, add specifics, sharpen the hook.

**Editing checklist:**
- Remove every unnecessary word
- Replace weak verbs with strong ones ("utilize" → "use")
- Cut marketing fluff ("innovative," "cutting-edge")
- Add concrete numbers where possible

---

## Advanced Techniques

### Emotional Arc

Even technical videos benefit from emotional structure:

```
Start: Frustration/Pain (relatable struggle)
  ↓
Middle: Hope/Possibility (solution appears)
  ↓
End: Satisfaction/Confidence (problem solved)
```

**Example for a deployment tool:**
- Open: "Deployment stress. We've all been there." [frustration]
- Middle: "What if it didn't have to be this way?" [hope]
- End: "Deploy with confidence. Every time." [satisfaction]

### Pattern Interruption

Break viewer expectations to maintain attention:

- Unexpected question: "But wait - why does this even matter?"
- Contrarian take: "Most companies get this wrong."
- Self-awareness: "I know what you're thinking..."

### The Rule of Three

Humans remember things in threes:

- "Fast, reliable, secure"
- "Build it. Ship it. Forget it."
- "Three features. Two minutes. One platform."

### Callback & Payoff

Reference the opening later for satisfaction:

**Opening:** "Remember when deployments meant Friday nights in the office?"
**Closing:** "No more Friday nights. No more stress. Just ship."

---

## Genre-Specific Notes

### Product Demos
- Show, don't tell (screen recordings > explanations)
- Keep features list to 3-5 max (more = forgettable)
- Always end with clear next step

### Sprint Reviews
- Team-facing, so inside jokes/references OK
- Celebrate wins explicitly (morale matters)
- Be honest about what didn't ship

### Tutorials
- One step per scene (easier editing)
- Anticipate confusion points
- Show mistakes and fixes (relatability)

### Case Studies
- Let customer voice dominate (quote liberally)
- Use real numbers (even if small, specifics beat vague "growth")
- Focus on process, not just results

### Announcements
- Tease before reveal (build anticipation)
- Explain "why now" (timing context)
- Make it easy to share (memorable soundbite)

---

## Common Mistakes to Avoid

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Writing too much | Narration rushes, feels frantic | Cut 20%, slow down |
| Generic openings | Viewers click away | Hook with problem/question/stat |
| Feature lists | Boring, forgettable | Convert to benefits, show outcomes |
| Passive voice | Sounds corporate, distant | Use active voice |
| No CTA | Viewers don't know next step | Always end with clear action |
| Jargon overload | Excludes non-experts | Explain or simplify |
| Identical tone across scenes | Monotonous | Vary energy (excited intro, calm explanation, bold CTA) |

---

## Workflow Integration

### Step 1: Pre-Production (use `/script` command)
1. Gather raw content (release notes, features, data)
2. Define audience and goal
3. Choose narrative structure (demo/review/tutorial/case study)
4. Draft scene breakdown with target durations

### Step 2: Scriptwriting
1. Write per-scene scripts in `public/audio/scenes/*.txt`
2. Add timing annotations `[Target: 15 seconds]`
3. Mark pauses `[pause 1.0s]`
4. Include visual cues `[Visual: Dashboard animation]`

### Step 3: Review
1. Read aloud, check timing
2. Verify brand voice alignment (check `brands/` directory)
3. Self-edit using checklist above
4. Get feedback from target audience member

### Step 4: Finalization
1. Update `project.json` with script status
2. Generate voiceover with `/generate-voiceover`
3. Review audio sync in Remotion Studio
4. Iterate if pacing feels off

---

## Quick Reference Card

### Timing
- 150 words = ~60 seconds
- 1-second pause = subtract 2-3 words
- Hook: 3-5 seconds
- CTA: 5-10 seconds

### Formulas
- **Hook:** Problem question or bold claim
- **Feature:** [What it does] so you can [benefit]
- **CTA:** [Action] + [Benefit] + [Friction reducer]

### Checklist
- [ ] Hook grabs attention in 3 seconds
- [ ] Benefits before features
- [ ] Active voice throughout
- [ ] Specific numbers/examples
- [ ] One idea per sentence
- [ ] Clear CTA at end
- [ ] Timing matches target duration

---

## When to Use This Skill

Invoke the screenwriter skill when:

- Starting a new video project (plan narrative structure)
- Converting release notes → voiceover script
- Refining existing script for clarity/timing
- Writing narration for demos, reviews, tutorials
- Improving weak hooks or CTAs
- Ensuring brand voice consistency
- Calculating script duration from word count

**Don't use for:**
- Visual design (use frontend-design skill)
- Video editing/rendering (use remotion skill)
- Audio generation (use elevenlabs skill)

---

## Feedback & Contributions

This skill can always improve. If you encounter:

- **Missing narrative pattern** - Share the video type/use case
- **Timing formula issues** - Let me know your speaking rate
- **Genre-specific needs** - Describe the content type

Say "improve screenwriter skill" and I'll help you update this file and contribute to the toolkit.
