---
name: feedback-fix-only-what-he-named
description: Affan 2026-10-22 — a review note changes only what he named; never replace his grade/sharpen stack; a reference channel he names covers ONLY the dimension he names (11-24); test frames of every shot before a full render
metadata:
  type: feedback
---

A review note is fixed by changing ONLY what he named. On the MJ siblings short he said skin was "too black"; I swapped
out his whole AE grade stack (look + sharpen bands + Sharpen 40) for a fitted curve without sharpening, and v5 came back
"so soft... I told you to just reduce the blackness". His grading reference is his own finals on disk
(`E:/Shorts/Abudance Wisdom Shorts Exports/Final Renders`, the same videos as his channel), and he offers his AE projects
for exact values.

**Why:** every revision costs him usage and time; an over-reach means another full round. The real cause (a colour-drift
bug upstream) was fixable without touching his look.

**How to apply:** find the root cause and fix that; keep his grade, sharpening and look untouched unless he asks; compare
against his own finals; send test frames of EVERY shot before any full render (his ask, 2026-10-22). Related:
[[feedback-creators-hand-is-not-a-bug]], [[feedback-every-video-better-than-last]].

**Revise, don't remake (Affan 2026-10-27, batch-5 Onyx reactions):** "don't completely remake the Onyx reaction video, just do the
revisions, because otherwise a lot of tokens are going to get wasted." I had briefed a from-source rebuild as v2 sequences. A note
gets a surgical pass instead: duplicate the prepared sequence → ripple-insert or ripple-delete the named spans → re-render only what
those spans touch → swap a layer in place. No new catalog pass, re-plan or review rounds over unchanged parts.

**Lean revisions on code builds (Affan 2026-10-28, Janet short):** "don't make any major changes, don't do complete renders, be as
lean as possible." A review note on a code-built short is applied as DATA over the reviewed picture: timeline values + one finish
render (e.g. a finish-side `lift` translate for letterboxed shots), never a Stage A / Topaz / caption / audio re-run unless the note
touches them. Prove unchanged shots match the reviewed export outside the changed region before shipping.

**A reference channel covers only the dimension he names (Affan 2026-11-24, AW "Streamers Rated GTA 6", fix1 REJECTED:
"forgot my whole style… worst video… a little kids cartoon trophy").** His Tella note pointed at Music Media Co for the TRANSITIONS.
The BRIEF read it as "everything except captions follows MMC", so the build invented a non-AW look: generic captions, a scoreboard,
name labels, white flashes, a washed grade. It also replaced the Higgsfield 3D render he asked for (the real Game Awards statue)
with a code-drawn cup. The hub passed fix1 on specs and AW defect rules without a style check.

**How to apply:** a named reference changes ONLY the dimension he names (transitions, captions, pacing...). The channel's house kit is
the default for everything else (AW Shorts: `projects/mj-son-step-outside/`, [[feedback-bolt-motivation-look]]). A prop he showed
or named is built as THAT object, never a drawn stand-in. Before any spec QA, run a side-by-side style-conformance check against an
approved Short of the same channel (captions, labels, grade, transitions, props). The hub runs it again before calling a render
shippable.

**The hub style gate covers the WHOLE Short, every version (2026-11-24, Travis A2 v6).** The hub passed v6 because only beat 10 had changed and it "fit the rest of the Short". Affan rejected it as "worst video, not upload material": the whole Short had been built without the AW engine. So every version gets compared with the house kit, never with its own previous version. A build without the AW engine (Topaz, head lock, AE grade, glow bars, CapCut caption pass) fails on sight; "lean" means fewer rounds, never a cheaper engine.
