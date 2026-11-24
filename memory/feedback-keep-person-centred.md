---
name: feedback-keep-person-centred
description: "Affan 2026-11-18 (Stygar Reel v1): keep the person in the MIDDLE of the window; a static crop shifted to hold a lean sat him left; he also wants light continuous zooms and explanatory motion graphics on real-video guest clips"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ede00dd1-2d3f-4a5e-8d58-6009bd299cd7
  modified: 2026-11-18T02:15:48.331Z
---

Affan, 2026-11-18, on the 30 fps DOAC check of "She Recorded Her Own Firing" (Ryan Stygar, job `projects/_client-scott-clary/stygar-recorded-firing`), verbatim: "needs motion graphics and why he is postioned to left too much bruv you've edited so many reels you forget basic things like keeping the person in the middle incorprate also light zooms subte throughout and motion graphics to better explain the environment and info".

**Why:** v1 kept the kit's STATIC per-shot crop and I shifted the whole crop chain 175 px so his lean ("the upward angle", face box up to 92 px out of the window) stayed inside; the cost (head a third from the left for ~37 s) was reported as "his call" instead of being solved. He reads that as forgetting basics. v1 also had no zoom and no graphics (I had read "no overlays" from the cancelled 48 Visits Left Reel, which was about stock pictures over an audio-only podcast, not about motion graphics).

**How to apply:**
- A talking head in a window sits in the MIDDLE (face-box centre at the window centre, eyes about 29 % down) in every frame. If a static crop can't hold the lean, the answer is a tracked crop, never an off-centre static one. The DOAC kit (`_doac-kit`) only has static per-shot crops; the job-local fork `projects/_client-scott-clary/stygar-recorded-firing/work/v2/` (make_path.py + build_v2.py + gfx_v2.py) is the tracked build; Affan approved its v4 ("approved", 2026-11-18, after the shadow note) and the 60 fps final of it was built and delivered the same day (`build60_v2.py`, Chronos over the clean tracked plate, `qa60_extra.py` checks). His review of that 60 fps file is still pending, so treat the fork as a working base, not yet a standard. See [[reference-doac-kit]] for the 60 fps recipe.
- Track the face-BOX centre (eyes shift with yaw), never his size; smooth within each span only; clamp to the frame before smoothing; verify centring by running the detector on the RENDERED window (the source-scale detector read 10-25 px off).
- Light, subtle, CONTINUOUS zoom through the whole film, no reset at a cut (same camera). The curve I used is mine (1.00-1.08), not a measured reel; ask if he wants it stronger ([[feedback-steady-drift-zoom]], [[feedback-no-same-camera-punch-ins]]).
- On a guest clip with real video, motion graphics that EXPLAIN the environment and info are wanted (a diagram of the scene, who is speaking a quoted line, a scoreboard, an X-list, a check-list). Labels go in the bottom band ([[feedback-labels-at-bottom]]), never over the face, wording his own or neutral. "No overlays" in [[feedback-no-audio-only-podcasts]] means no stock pictures covering a missing picture, not no graphics.
- Related: [[feedback-head-steady-across-cuts]], [[reference-doac-kit]], [[feedback-scott-ig-minimal-format]].
