---
name: feedback-fix-only-what-he-named
description: Affan 2026-10-22 — a review note changes only what he named; never replace his grade/sharpen stack; test frames of every shot before a full render
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
