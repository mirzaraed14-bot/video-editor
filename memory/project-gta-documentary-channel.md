---
name: project-gta-documentary-channel
description: "Affan Afterhours — the user's GTA channel: TWO formats (the GTA 6 explainer is the engine and the default; the documentary is paused); episode 2 'How Rockstar Hired Travis Scott' SHIPPED 2026-09-20, post-mortem written; the creator's face-zoom grammar, overlay frame and PNG-puppet direction"
metadata: 
  node_type: memory
  type: project
  originSessionId: e1b9cd8c-a044-4294-9e79-318eb202a8a0
  modified: 2026-09-19T06:35:36.226Z
---

**Affan Afterhours** (https://www.youtube.com/@AffanAfterhours, ~2k subs, 51 videos). The user stays on camera.

**Two formats, decided 2026-09-19.** The **GTA 6 explainer** is the channel's engine — top videos 167k / 34k /
16k / 13k / 10k — and the **default** for what comes next: a bright colour-LED room, animated hands, ≥ 17 visible
changes/min, **opens on the face**, illustrated **stills in Rockstar's own VI key-art style** (flat vector, hard
shading, saturated pastels; Higgsfield, 2 cr, never video) placed at **85–90 over a dark colour matte + BCC Film
Grain** (dark red / dark blue / dark gold, never light), gameplay **zoomed out over the same matte**, posters with
ONE hot-pink keyword, motion graphics doing the heavy lifting with **people as animated PNG cutouts of the real
person** (a manager's cutout travels to the artist's, the artist's to the label's), ≤ 30 credits. The
**documentary format is PAUSED**: Hot Coffee (shipped 2026-09-18, `projects/gta-san-andreas-hot-coffee/`,
~900 credits ≈ $50) sits at 237 views; *"we can just pay an editor $20… that was an experiment video."*

**THE FACE SHOT IS NEVER STILL — the creator's own grammar, in order (confirmed in the Hot Coffee export):** (1)
nest a face run's jump-cuts into one sequence; (2) inside the nest, a **"cut zoom"** on the emphasis word — an
instant scale snap, no ramp, **+25 in the explainer** (+5/+10 in the doc); (3) a **keyframed gradual zoom
100 → 110** on the nest clip itself. Stills get a ~5 % creep too. A replay that flattens the face destroys all
three; hand face runs back nested with the ramp on the nest. **The pipeline does it now** (2026-09-19, on the creator's ask): picks as data in the job's `transcript/face-zooms.json`, applied by `lanes/premiere/face-nests.py --apply/--verify`.

**Episode 2 — "How Rockstar Actually Hired Travis Scott For GTA 6"** (~8 min, the casting-call thesis). Job
`projects/gta6-travis-scott-hired/`. **SHIPPED 2026-09-20** (they exported and uploaded; 7:39). The learning pass is written:
`projects/gta6-travis-scott-hired/POSTMORTEM.md` — they KEPT 37/37 graphics, 163/164 SFX at identical levels, all 38 face
nests + 37 cut zooms and the cut itself; they ADDED three receipts (the real Club Shay Shay interview inserted 8.1 s where the
narration cites it, a credits card from Metro Boomin's *Superhero*, a Travis photo in the slot I could not source), REPLACED
the voice with an Adobe Enhance Speech v2 bounce (−22 LUFS, 128 kbps) and laid 4 Epidemic tracks on A7 with silences before
section turns. Rules that changed: the face gradual zoom is a RATE (~1.6 %/s), a cited on-camera source is PLAYED not drawn,
an unsourceable slot gets an alternative artifact offered, insert points snap to word boundaries.

**Why:** the creator wants each video cheaper and faster, in the style that already works for them, with better
explanation than a static poster gives.
**How to apply:** start with `PLAYBOOK.md` § 0a (two formats) and the job's `BRIEF.md` "▶ STATUS" block. The
overlay frame (matte + grain under an inset picture) is CHANNEL-WIDE — only the scale differs per format; the doc's
palette and mannequin rule do not carry to an explainer. Any web-sourced picture is enhanced in Higgsfield if soft
([[feedback-sourced-stills-must-be-hq]]). Get approval before any Higgsfield credit
([[reference-higgsfield-connector]]); never touch A2 ([[feedback-creators-hand-is-not-a-bug]]). Related:
[[user-abundance-wisdom-editor]], [[feedback-long-term-self-improving]], [[reference-epidemic-sound-connector]].
