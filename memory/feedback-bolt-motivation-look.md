---
name: feedback-bolt-motivation-look
description: "Affan 2026-11-05/09 — Bolt Motivation (YouTube, 2.2M) is his reference for Topaz + colour AND (11-09) for how to place a real-life, non-podcast shot; numbers in research/bolt-motivation-look.md"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d942343f-3a2e-4750-9957-c10be704ca52
  modified: 2026-11-05T13:07:44.807Z
---

Affan 2026-11-05: "this channel I really like his Topaz ... it looks very realistic ... try to replicate that on our shorts and also try to copy the color grading of him."

**Why:** his faces read real (skin texture, sharp eyes, deep blacks, no orange), while our AW AE grade pushes skin orange (hue 29.7, sat .61 vs Bolt's 16-24, .44).

**How to apply:** `research/bolt-motivation-look.md` holds the study. First used on La Toya v2 (delivered 2026-11-05): Iris x2 (his preset numbers) + `blend=0.2` per segment, plus `build/bolt_look.py` + `bolt_torch.py` as grade_mode 'bolt', in projects/latoya-betrayed. It also needs: grade before the letterbox, twin_opacity .33 + blur 30, no grain, export CRF 5 (LESSONS 2026-11-05 items 9-11). Not yet ruled on: his verdict on La Toya v2 decides whether it replaces the AW AE grade ([[feedback-aw-grade-faceless-only]]) on other Shorts. Check `presets/youtube-shorts/abundance-wisdom/LESSONS.md` for it. Don't force Bolt's skin level on dark skin: only the orange comes out.

To study any YouTube channel frame by frame without downloading: open /shorts/<id> in his Chrome (the player is already muted there), pause, draw the video on a canvas 1:1 and zoom. Reading `canvas.getImageData` gives colour numbers. YouTube's yt-dlp block ([[feedback-youtube-sourcing]]) doesn't touch normal viewing; a tab can freeze after many seeks, so open a fresh one.

**2026-11-09 shot placement (his words: Bolt is the one to learn from for placing a real-life, not-crisp-podcast shot).** Measured on 6 Shorts: one fixed 4:5 picture box (y284-1634) on a blurred twin for wide footage, full-bleed for tight/vertical; subject small and in context (face 7-24 % of frame), faces only tight when they carry the line (centre y .29-.47, above the mid-frame caption), and every shot shows the NOUN or VERB of its caption line, time-locked. Rules in `research/bolt-motivation-look.md` § SHOT PLACEMENT. Same day his Bieber Tella 2 said the overlays "just feel like random overlays": content and timing must match the line (see [[project-abundance-shorts-automation]]).

**2026-11-12 ~19:45: the AW build TEMPLATE is "MJ son step outside" exactly as shipped (he called it "really close to
Bolt Motivation").** Affan: "copy Bolt Motivation's style aesthetic, it's very very close to my style, but I really like the
editing style of the Prince Jackson / Jaafar Jackson short you made ... I just really want to continue that aesthetic. I like
the Topaz, the head tracks, everything about it".
- **Why:** he named that Short. Its zoom, transitions, caption position and grade are his own earlier rulings.
- **How to apply:**
  - Every AW Short build takes `projects/mj-son-step-outside/` (BUILD.md + `build/`) values as they are.
  - **Its grade is his AE look (`grade_mode 'ae'`), NOT the Bolt grade**, which stays an open trial (La Toya).
  - Bolt's measured differences are his call, never default: hard cuts only, a slow linear push of ~2.5 %/s, 3-word
    captions every ~1 s, the Bolt grade, stacked comparison splits, reaction cutaways.
  - The measured study and the parameters with file:line references are in
    `research/bolt-style-2026-11-12/findings.md`; the newest Shorts are in `chrome-newest.md` there.
- **Adopted on 12 Nov (his pick "Add splits + cutaways"):**
  - stacked two-panel splits on comparison beats, with the seam at the base caption y and a white line on it;
  - reaction cutaways of 1-2 s, at most about one per 6-8 s, first-party, matching the line.
  Rules are in AW README § 13. They are sequencing moves and never change a cut he has locked.
- A near-done job is NOT rebuilt for this. It applies from the job's next step.
- Running AW sessions told on 12 Nov: snape-prank-build and the HP fork, plus a correction about the grade.
