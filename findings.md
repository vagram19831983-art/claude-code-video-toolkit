# Research & Discoveries

## Session: 2026-02-15

### Project Analysis

#### BMAD-METHOD
- **Location:** `/Users/romangasanov/Documents/Projects_coding/BMAD-METHOD/`
- **Size:** 2.1 MB
- **Installed modules:** bmm, bmb, tea, cis (4 из 5, bmgd недоступен)
- **Content:** 58 workflows, 20 agents, 6 tasks
- **Purpose:** AI-native development framework with specialized agent workflows

#### Planning-with-Files
- **Location:** `/Users/romangasanov/Documents/Projects_coding/planning-with-files/`
- **Size:** 1.6 MB
- **Skill installed:** `~/.claude/skills/planning-with-files/`
- **Purpose:** Persistent planning methodology (Manus AI-inspired)
- **Core pattern:** 3 files (task_plan.md, findings.md, progress.md)

#### Claude Code Video Toolkit
- **Location:** `/Users/romangasanov/Documents/Projects_coding/claude-code-video-toolkit/`
- **Size:** 35 MB
- **Original skills:** remotion, elevenlabs, ffmpeg, playwright-recording, qwen-edit, frontend-design
- **GitHub:** https://github.com/digitalsamba/claude-code-video-toolkit

**Capabilities:**
- Video creation from concept to render
- Remotion (React-based video framework)
- ElevenLabs voice generation
- Playwright browser recording
- Scene transitions library
- Brand system
- Templates: Sprint Review, Product Demo

**Identified Gap:** No dedicated scriptwriting skill - narration written "on the fly"

---

### Screenwriter Skill Creation

#### Problem Statement
Video toolkit writes scripts during scene planning without:
- Professional narrative structure
- Precise timing calculations
- Genre-specific formulas
- Emotional arc design
- Brand voice consistency

#### Solution Created
Built complete screenwriter skill from scratch:

**Files created:**
- `.claude/skills/screenwriter/SKILL.md` (23KB, 801 lines)
- `.claude/skills/screenwriter/examples.md` (14KB, 555 lines)
- `.claude/skills/screenwriter/README.md` (4KB, 168 lines)
- `.claude/commands/script.md` (17KB, 711 lines)
- `SCREENWRITER-INTEGRATION.md` (11KB, 387 lines)
- `WHAT-WAS-ADDED.md` (6KB, 273 lines)

**Total addition:** ~69KB, 2,895 lines

#### Key Features Implemented

**1. Narrative Structure Formulas**
| Video Type | Formula |
|------------|---------|
| Product Demo | Pain → Solution → Proof → Action |
| Sprint Review | Context → Shipped → Demo → Impact → Next |
| Tutorial | Goal → Steps → Result → Gotchas |
| Case Study | Challenge → Approach → Results → Takeaway |
| Announcement | Tease → Reveal → Impact → Access |

**2. Timing Precision**
- Standard pace: 150 words/minute (2.5 words/second)
- Automatic word count calculations
- Strategic pause insertion: `[pause 0.5s]`, `[pause 1.0s]`, etc.

**3. Professional Principles**
- Clarity over cleverness
- Benefits before features
- Active voice (not passive)
- Specific numbers (not vague claims)
- One idea per sentence
- Strategic pauses for impact

**4. Quality Checks**
- Readability analysis
- Sentence length variation
- Hook strength validation
- CTA optimization
- Brand voice alignment

**5. Examples Library**
- 8 complete script examples
- Before/after comparisons
- Tone variations by audience
- Anti-patterns to avoid

#### Inspiration Sources
- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) - Copywriting principles
- [obra/superpowers](https://github.com/obra/superpowers) - Content strategy
- Professional screenwriting best practices

#### Git Status
- **Commit:** `17b0ba9`
- **Branch:** main (1 commit ahead of origin)
- **Status:** Not yet pushed to GitHub
- **Message:** "Add professional screenwriter skill and /script command"

---

### VoicePro_fixed.py Discovery

**Location:** `/Users/romangasanov/Documents/Projects_coding/Batch-image-creator/VoicePro_fixed.py`

**Purpose:** Standalone script for mass voiceover generation via ElevenLabs

**Key capabilities:**
- 📊 Excel input (bulk text processing)
- 🔄 Parallel processing (multithreading)
- 🌍 Evomi residential proxies (sticky sessions for IP masking)
- 🔑 Automatic API key rotation on quota exhaustion
- 📦 Text chunking (≤1500 chars/chunk)
- 🔧 ffmpeg integration (audio stitching, silence padding)
- 🔁 Advanced retry logic (up to 10 attempts per task, 5 network retries)
- 💾 Output: Numbered MP3 files

**Technologies used:**
- ElevenLabs Internal API (refresh token → access token flow)
- Firebase auth endpoints
- Evomi proxy with session management
- ffmpeg for audio processing
- Python threading + concurrent.futures

**Differences from Video Toolkit's voiceover.py:**

| Feature | VoicePro | Toolkit voiceover.py |
|---------|----------|---------------------|
| Proxy support | ✅ Evomi Sticky | ❌ None |
| Key rotation | ✅ Automatic | ❌ Single key |
| Retry logic | ✅ 10 task + 5 network | ❌ Basic |
| Chunking | ✅ 1500 chars | ❌ Full text |
| Parallelism | ✅ Multithreading | ❌ Sequential |
| Input format | Excel | Text files |
| Session persistence | ✅ Resume on failure | ❌ None |

**Potential Integration Value:**
1. Bypass ElevenLabs rate limits via proxy rotation
2. Handle quota exhaustion gracefully with key pools
3. Faster generation via parallel processing
4. Better reliability with retry mechanisms
5. Cost optimization through multiple free-tier accounts

**Integration complexity:** Medium
- Need to adapt Excel input → text files from `public/audio/scenes/*.txt`
- Integrate proxy config into toolkit settings
- Merge with existing brand voice system
- Preserve toolkit's per-scene workflow

---

### Skills.sh Marketplace Analysis

**Search query:** "Screenwriting, scriptwriting, video production skills"

**Results:** No dedicated video scriptwriting skills found

**Available writing skills:**
- `copywriting` (vercel-labs) - Landing page copy, CTA optimization
- `content-strategy` (coreyhaines31) - Blog/SEO content planning
- `brainstorming` (obra) - Code project design
- `writing-plans` (obra) - TDD implementation plans

**Closest match:** `copywriting` by coreyhaines31/marketingskills
- 7.8K installs
- Conversion-focused copy
- CTA formulas
- Clarity principles
- NOT designed for video narration

**Conclusion:** Custom screenwriter skill was necessary - no existing solution

---

### Key Insights

#### 1. Video Toolkit Architecture
- Modular skill system (`.claude/skills/`)
- Command system (`.claude/commands/`)
- Brand management (`brands/` directory)
- Project lifecycle tracking (`project.json`)
- Per-scene audio workflow (`public/audio/scenes/*.txt`)

#### 2. Scriptwriting Gap
Original workflow:
```
/video → scene planning → basic narration → /generate-voiceover
```

Claude writes narration during planning without:
- Narrative expertise
- Timing calculations
- Emotional design
- Quality validation

New workflow:
```
/video → /script → professional narration → /generate-voiceover
                ↓
          screenwriter skill
          - Genre formulas
          - Timing precision
          - Brand alignment
          - Quality checks
```

#### 3. ElevenLabs Integration Levels

**Current (toolkit):**
- Simple API calls
- Single key
- No retry logic
- Sequential processing

**Advanced (VoicePro):**
- Proxy rotation
- Key pool management
- Network retry + task retry
- Parallel processing
- Session persistence

**Opportunity:** Merge both approaches for production-grade voiceover

---

### Files & Directories Structure

```
claude-code-video-toolkit/
├── .claude/
│   ├── skills/
│   │   ├── remotion/
│   │   ├── elevenlabs/
│   │   ├── ffmpeg/
│   │   ├── playwright-recording/
│   │   ├── frontend-design/
│   │   ├── qwen-edit/
│   │   └── screenwriter/           ← NEW
│   │       ├── SKILL.md
│   │       ├── examples.md
│   │       └── README.md
│   └── commands/
│       ├── video.md
│       ├── brand.md
│       ├── design.md
│       ├── generate-voiceover.md
│       ├── record-demo.md
│       └── script.md               ← NEW
├── brands/
│   ├── default/
│   └── digital-samba/
├── lib/
│   ├── components/
│   ├── transitions/
│   └── project/
├── templates/
│   ├── sprint-review/
│   └── product-demo/
├── tools/
│   └── voiceover.py               ← Could be enhanced with VoicePro logic
├── SCREENWRITER-INTEGRATION.md    ← NEW
└── WHAT-WAS-ADDED.md              ← NEW
```

---

### Open Questions

1. **VoicePro Integration:**
   - Should we replace `tools/voiceover.py` or create `tools/voiceover_pro.py`?
   - How to manage proxy credentials in toolkit config?
   - How to handle key pool (`base.txt`) in project structure?
   - Should parallelism be opt-in or default?

2. **Screenwriter Testing:**
   - Need real project to test `/script` command
   - Verify timing calculations with actual ElevenLabs output
   - Test brand voice integration
   - Validate A/B hook variations

3. **GitHub PR:**
   - Should screenwriter skill be contributed back to official toolkit?
   - Need to test on multiple video types first?
   - Documentation quality sufficient?

---

### Technical Specs

#### System Environment
- **OS:** macOS (Darwin 24.3.0)
- **Working dir:** `/Users/romangasanov/Documents/Projects_coding/Batch-image-creator`
- **Projects dir:** `/Users/romangasanov/Documents/Projects_coding/`

#### Installed Tools
- Node.js v20+ (for BMAD-METHOD)
- Python 3.9+ (for video toolkit tools)
- ffmpeg (for audio processing)
- git (for version control)
- Claude Code (AI IDE)

#### API Keys Required
- ElevenLabs API key (for voiceover)
- RunPod API key (optional, for GPU tools)
- Firebase API key (for VoicePro auth)
- Evomi proxy credentials (for VoicePro)

---

### References

**Documentation:**
- [Claude Code Video Toolkit README](https://github.com/digitalsamba/claude-code-video-toolkit)
- [Remotion Docs](https://remotion.dev)
- [ElevenLabs API Docs](https://elevenlabs.io/docs)
- [BMAD Method Docs](http://docs.bmad-method.org/)

**Skills:**
- skills.sh marketplace: https://skills.sh/
- coreyhaines31/marketingskills: https://github.com/coreyhaines31/marketingskills
- obra/superpowers: https://github.com/obra/superpowers

**Proxies:**
- Evomi residential proxies: core-residential.evomi.com:1000
- Session format: `username:password_country-US_session-xxx_lifetime-30`

---

### Next Session Priorities

1. **Test screenwriter skill**
   - Create demo video project
   - Run `/script` command
   - Generate actual voiceover
   - Measure timing accuracy

2. **VoicePro integration (if desired)**
   - Design config structure
   - Adapt Excel → text files
   - Preserve per-scene workflow
   - Add proxy config

3. **Documentation improvements**
   - Add troubleshooting section
   - Create video tutorials
   - Write contribution guide

4. **Community contribution**
   - Push to GitHub
   - Create PR to official toolkit
   - Gather user feedback
