---
name: feedback-cover-phone-reading
description: "Affan 2026-10-23 (CA-007 review): never show him reading his script off the phone — every look-down moment goes under a FULL-FRAME graphic (or his face blurred behind one); also lips must be provably in sync after any V1 edit"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 26a2857f-411a-4f2c-917d-fb6059e77b46
  modified: 2026-10-23T02:39:43.044Z
---

Affan, reviewing AffanWiz CA-007 (Tella walkthrough 2026-10-23): "whenever I'm looking down … reading off the phone … it
should be a motion graphic overlay … cover the whole thing so that my face is not visible … or translucent so it's blurred
… this literally shows that I'm reading off a script … not good for my brand credibility". A small side card over the face
does NOT count as a cover. Same review: lips were out of sync (my `.end =` razor heal slipped V1) — "fixed one million
percent, otherwise I literally cannot upload this".

**Why:** his credibility as the expert on camera; reading reads as unprepared. Sync errors are unshippable.

**How to apply:** on every face-cam video measure head pitch over the cut (`projects/streamer-content-machines/review/tools/look_down.py`)
and put every clip ≥ 60 % "down" under a full-frame graphic (check 40–60 % clips by eye — gestures fool the proxy); expect
face share near a third on a script-heavy take. After ANY V1 write, run a picture-vs-voice audit
(`projects/streamer-content-machines/work/sync_audit.py`). Never extend a Premiere clip with `.end =` (lab-notes 2026-10-23).
AffanWiz specifics (SFX variety, a CTA card about once a minute) live in presets/youtube/affanwiz/PLAYBOOK.md.
Related: [[project-affanwiz-channel]], [[feedback-premium-sfx]], [[feedback-creators-hand-is-not-a-bug]].
