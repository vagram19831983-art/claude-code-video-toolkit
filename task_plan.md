# Task Plan: Video Toolkit Improvements

**Created:** 2026-02-15
**Status:** Ready for next session
**Goal:** Enhance Claude Code Video Toolkit with professional scriptwriting and advanced voiceover capabilities

---

## Context

This plan tracks improvements to the Claude Code Video Toolkit. Current session completed screenwriter skill integration. Future work focuses on testing, VoicePro integration, and community contribution.

---

## Phases

### Phase 1: Screenwriter Skill Creation ✅ COMPLETE
**Status:** `complete`
**Completed:** 2026-02-15

**Objectives:**
- [x] Research existing scriptwriting skills on skills.sh
- [x] Analyze video toolkit structure
- [x] Design screenwriter skill architecture
- [x] Write SKILL.md with narrative formulas
- [x] Create examples.md with real-world scripts
- [x] Build /script command workflow
- [x] Write integration documentation
- [x] Commit to git

**Deliverables:**
- `.claude/skills/screenwriter/SKILL.md` (23KB, 801 lines)
- `.claude/skills/screenwriter/examples.md` (14KB, 555 lines)
- `.claude/skills/screenwriter/README.md` (4KB, 168 lines)
- `.claude/commands/script.md` (17KB, 711 lines)
- `SCREENWRITER-INTEGRATION.md` (11KB)
- `WHAT-WAS-ADDED.md` (6KB)

**Git commit:** `17b0ba9` (not pushed)

**Key learnings:**
- No existing video scriptwriting skills on marketplace
- Needed custom solution combining copywriting + content strategy principles
- 5 genre formulas implemented (Product Demo, Sprint Review, Tutorial, Case Study, Announcement)
- Timing calculation: 150 words/min standard pace

---

### Phase 2: Screenwriter Testing 🔄 READY
**Status:** `pending`
**Dependencies:** Phase 1 complete

**Objectives:**
- [ ] Create test video project with `/video`
- [ ] Run `/script` command end-to-end
- [ ] Generate scripts for all 5 genres
- [ ] Test timing accuracy (words → seconds)
- [ ] Verify brand voice integration
- [ ] Test A/B hook variations
- [ ] Generate actual voiceover with `/generate-voiceover`
- [ ] Measure real duration vs. predicted
- [ ] Review in Remotion Studio
- [ ] Document any bugs or improvements

**Acceptance Criteria:**
- Scripts generate for all supported templates
- Timing accuracy within ±5 seconds for 60s target
- Brand voice guidelines applied correctly
- No workflow blockers

**Estimated time:** 2-3 hours

**Risks:**
- ElevenLabs API quota limits
- Timing calculations may need tuning
- Brand integration edge cases

---

### Phase 3: VoicePro Integration Analysis 🔄 READY
**Status:** `pending`
**Dependencies:** None (can run in parallel with Phase 2)

**Objectives:**
- [ ] Analyze VoicePro_fixed.py architecture
- [ ] Map VoicePro features to toolkit needs
- [ ] Design integration approach (replace vs. extend)
- [ ] Plan config structure for proxies/keys
- [ ] Design key pool management in toolkit context
- [ ] Sketch API for toolkit compatibility
- [ ] Document migration path
- [ ] Estimate implementation effort

**Key Questions:**
1. Replace `tools/voiceover.py` or create `tools/voiceover_pro.py`?
2. Where to store proxy credentials? (`.env`, `brands/`, config file?)
3. How to manage `base.txt` key pool in project?
4. Should parallelism be opt-in or default?
5. How to preserve per-scene workflow?
6. Integration with existing brand voice settings?

**Deliverables:**
- Design document: `VOICEPRO-INTEGRATION-PLAN.md`
- API compatibility analysis
- Risk assessment
- Implementation roadmap

**Estimated time:** 3-4 hours

---

### Phase 4: VoicePro Implementation ⏸️ BLOCKED
**Status:** `pending`
**Dependencies:** Phase 3 complete, user approval

**Objectives:**
- [ ] Create `tools/voiceover_pro.py` (or refactor existing)
- [ ] Implement proxy rotation logic
- [ ] Add key pool management
- [ ] Integrate retry mechanisms
- [ ] Add parallel processing
- [ ] Preserve session state
- [ ] Update config templates
- [ ] Write migration guide
- [ ] Add tests
- [ ] Update documentation

**Acceptance Criteria:**
- Passes all existing toolkit tests
- Proxy rotation works with Evomi
- Key pool exhaustion handled gracefully
- Parallel processing scales linearly
- No breaking changes to `/generate-voiceover`

**Estimated time:** 1-2 days

**Risks:**
- Breaking existing workflows
- Proxy credential security
- Complex retry state management
- Thread safety issues

---

### Phase 5: Documentation & Examples 🔄 READY
**Status:** `pending`
**Dependencies:** Phase 2 or 4 complete

**Objectives:**
- [ ] Create video walkthrough of `/script`
- [ ] Write troubleshooting guide
- [ ] Add more script examples (6-10 total)
- [ ] Document common pitfalls
- [ ] Create FAQ section
- [ ] Write contribution guidelines
- [ ] Add architecture diagrams
- [ ] Update main README

**Deliverables:**
- Video tutorial (3-5 minutes)
- `TROUBLESHOOTING.md`
- Extended examples in `examples.md`
- `CONTRIBUTING.md`
- Architecture diagrams (Mermaid or similar)

**Estimated time:** 4-6 hours

---

### Phase 6: Community Contribution 📤 READY
**Status:** `pending`
**Dependencies:** Phase 2 complete, user approval

**Objectives:**
- [ ] Push screenwriter commit to GitHub
- [ ] Create feature branch for PR
- [ ] Write comprehensive PR description
- [ ] Add screenshots/examples
- [ ] Request maintainer review
- [ ] Address feedback
- [ ] Merge to main (if accepted)
- [ ] Announce on relevant communities

**Deliverables:**
- GitHub PR to digitalsamba/claude-code-video-toolkit
- PR description with examples
- Community announcement

**Estimated time:** 2-3 hours

**Risks:**
- PR rejection (low risk - fills clear gap)
- Requested changes
- Maintainer response time

---

## Current Status Summary

| Phase | Status | Progress |
|-------|--------|----------|
| 1. Screenwriter Creation | ✅ Complete | 100% |
| 2. Testing | 🔄 Ready | 0% |
| 3. VoicePro Analysis | 🔄 Ready | 0% |
| 4. VoicePro Implementation | ⏸️ Blocked | 0% |
| 5. Documentation | 🔄 Ready | 0% |
| 6. Community PR | 📤 Ready | 0% |

**Overall Progress:** 1 of 6 phases complete (16.7%)

---

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-15 | Create custom screenwriter skill | No existing solutions on skills.sh marketplace |
| 2026-02-15 | Use per-scene script files | Easier iteration, cheaper ElevenLabs API usage |
| 2026-02-15 | Include 5 genre formulas | Covers main use cases (demo, review, tutorial, case study, announcement) |
| 2026-02-15 | 150 words/min standard pace | Industry standard for conversational narration |
| 2026-02-15 | Create `/script` command | Dedicated workflow separate from `/video` |
| 2026-02-15 | Document in SKILL.md format | Consistent with toolkit conventions |
| 2026-02-15 | Not push to GitHub yet | Need testing first |

---

## Errors Encountered

| Error | Attempt | Resolution | Phase |
|-------|---------|------------|-------|
| Game Dev module (bmgd) unavailable | 1 | Installed without it (bmm, bmb, tea, cis only) | Setup |
| None during screenwriter creation | - | Clean implementation | Phase 1 |

---

## Files Modified/Created

### Session 2026-02-15

**Created:**
- `.claude/skills/screenwriter/SKILL.md`
- `.claude/skills/screenwriter/examples.md`
- `.claude/skills/screenwriter/README.md`
- `.claude/commands/script.md`
- `SCREENWRITER-INTEGRATION.md`
- `WHAT-WAS-ADDED.md`
- `findings.md` (this session context)
- `task_plan.md` (this file)
- `progress.md` (session log)

**Modified:**
- None (clean addition, no breaking changes)

**Git status:**
- 1 commit ahead of origin/main
- Commit hash: `17b0ba9`
- Not yet pushed

---

## Next Actions (Priority Order)

### Immediate (Next Session)
1. **Test screenwriter skill** (Phase 2)
   - Create demo project
   - Run `/script` end-to-end
   - Verify timing accuracy

2. **Push to GitHub** (if tests pass)
   - `git push origin main`
   - Makes work backed up

### Short-term (This Week)
3. **VoicePro analysis** (Phase 3)
   - Design integration approach
   - Document decisions

4. **Documentation improvements** (Phase 5)
   - Add troubleshooting guide
   - Create more examples

### Medium-term (This Month)
5. **Community PR** (Phase 6)
   - After thorough testing
   - With examples and docs

6. **VoicePro implementation** (Phase 4)
   - If user approves integration plan
   - After Phase 3 analysis complete

---

## Success Metrics

**Phase 2 Success:**
- [ ] 5 scripts generated successfully
- [ ] Timing accuracy ≥90% (±6s for 60s target)
- [ ] No workflow blockers
- [ ] Real voiceover generated and synced

**Phase 6 Success:**
- [ ] PR merged to official toolkit
- [ ] ≥3 users adopt skill
- [ ] Positive community feedback

**Overall Success:**
- [ ] Screenwriter skill in production use
- [ ] ≥10 video projects use `/script`
- [ ] Contributed back to open source
- [ ] (Optional) VoicePro integration complete

---

## Resources

**Documentation:**
- Toolkit: https://github.com/digitalsamba/claude-code-video-toolkit
- Remotion: https://remotion.dev
- ElevenLabs: https://elevenlabs.io/docs

**Planning files:**
- `findings.md` - Research and discoveries
- `progress.md` - Session logs
- This file (`task_plan.md`) - Roadmap and status

**Skills referenced:**
- planning-with-files: `~/.claude/skills/planning-with-files/`
- screenwriter: `.claude/skills/screenwriter/`

---

## Notes

- **No time pressure:** This is enhancement work, not critical bugs
- **User approval needed:** Before VoicePro integration (Phase 4)
- **Testing first:** Don't push to community without validation
- **Backup context:** This file ensures session recovery

**Last updated:** 2026-02-15 10:45 MSK
