---
name: feedback-bolt-motivation-look
description: "Affan 2026-11-05 — Bolt Motivation (YouTube, 2.2M) is his reference for Topaz upscale + colour on our Shorts; frame study and numbers in research/bolt-motivation-look.md"
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
