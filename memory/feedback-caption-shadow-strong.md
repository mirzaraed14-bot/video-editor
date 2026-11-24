---
name: feedback-caption-shadow-strong
description: "Affan 2026-11-18 (Stygar Reel v3): the DOAC caption drop shadow (kit, 0.75) is too faded; captions hard to read on bright backgrounds; he wants it more potent"
metadata:
  type: feedback
---

Affan, 2026-11-18, on the Stygar v3 check, verbatim: "caption drop shadow should be more potent and less faded out right its hard to read and the drop shadow will help getting it read better".

**Why:** the DOAC kit's shadow (`doac_frames.shadow_alpha`: one blur of radius 9, peak alpha ~0.55 on thin serif strokes) is diffuse; his white shirt and hands wash out white and gold captions (measured on 74 captions: 7 below 3:1 contrast, worst 2.0). This supersedes "Add shadow, opacity 0.75" ([[feedback-scott-ig-minimal-format]]) for the DOAC strand: that pick was made from stills of the Tuesday Reel and not re-checked on a bright wardrobe.

**How to apply:** on every DOAC-look Reel use the two-layer shadow in `projects/_client-scott-clary/stygar-recorded-firing/work/v2/shadow_v4.py` (a tight halo hugging the strokes plus a wide soft shadow; contrast median 9.5, worst 3.5) instead of the kit's, and measure caption contrast on the rendered file (`contrast_video.py`) before delivery. Strength is one parameter set (`PARAMS`; the milder S2 is in `shadow_test.py`) if a future clip reads heavy. Related: [[feedback-keep-person-centred]], [[reference-doac-kit]].
