# affanwiz — the channel preset (v0, 2026-09-23)

**The default for every AffanWiz video**: the creator's ENGLISH personal brand, long-form YouTube, 16:9, the
creator on camera. The channel exists to grow and promote their **Skool community** (the footage lives in
`E:\Skool Recordings\`). A job for this channel reads this folder before step 0:
`README.md` (the look, this file) · `PLAYBOOK.md` (the repeatable procedure) · `LESSONS.md` (what earlier jobs taught).

**Not the same channel as `presets/instagram/affanwizu/`** (Urdu reels, Roman Urdu captions only). Nothing in that
folder applies here, and nothing here applies there.

**Nothing from another channel carries over by default either.** Affan Afterhours' face grammar, overlay frame and
palette are that channel's; this one earns its own numbers from the creator's direction and their hand passes.

## 1. The look — PENDING the creator's direction

The creator gives the editing direction after the first rough cut (2026-09-23). Record it here as locked rules,
each with its date and the job it came from. Until then the house defaults hold:
`presets/youtube/default/` (long-form cards + creative moves, grade Autumn-Rec709 70/115).

| Area | Rule | Source |
|---|---|---|
| Face / zooms | **the creator's own**: they cut, nest and zoom the face themselves (cut zooms + nested gradual zooms). Nests are never touched. | creator, 2026-09-23 |
| Overlays (screenshots, captures, clips) | **§ 1a THE OVERLAY FRAME, locked** | creator + reference frame, 2026-09-23 |
| Grade | _pending_ (house default until told) | |
| SFX / music | _pending_ | |
| Captions | none (long-form, YouTube CC) unless told | CLAUDE.md format table |

## 1a. 🔒 THE OVERLAY FRAME (the creator's direction, 2026-09-23, job monetized-before-gta6)

The creator drops every overlay (a screenshot, a YouTube/Instagram capture, a gameplay clip) straight onto V1 in
place of the face, un-resized. The finish turns each one into this frame, measured off their reference image
(`projects/monetized-before-gta6/overlays/reference-overlay-frame.webp`):

| Element | Rule |
|---|---|
| **Size** | **No overlay ever fills the screen.** Fit inside **1700 × 972** (≈ 88.5 % × 90 %) with "intentional leakage" so the matte shows around it. Video overlays: Motion Scale **88.5**. |
| **Tiny overlays** (a view-count badge, a one-line crop) | scaled up to **50 % of the screen width (960 px)**, never full size. |
| **Resolution** | anything blown up past 1.1× is **enhanced in Higgsfield first**, never shipped soft. Screenshots → `upscale_image` (4k, 2 credits). **Crops under ~200 px** → `gpt_image_2_5` edit (high, 2k, ~0.25–1 credit) with the exact text spelled out: the upscaler INVENTS text on tiny icons. Every result is checked against the original before use. |
| **Matte** | an **animated colour matte under every overlay** (V1, the overlay on V2): near-black corners, a plum/magenta glow top-left (#251221), dark teal right (#0a1820), slate-blue floor (#1e212f), glows drifting on 23/31/41/53 s periods, vignette, fixed dither. One file the length of the sequence, laid with in-point = sequence time, so back-to-back overlays share one seamless background. Rendered at the sequence frame rate (59.94), or its edges miss the cut. |
| **Drop shadow** | **on every overlay, baked**: black, 100 %, spread 10 px, offset 16/20 px, blur 24 px. Premiere's Drop Shadow effect is too faint on this dark matte (tested). |

Tools (job-local, reusable as the pattern): `overlays/make-matte.py`, `build-overlays.py`, `place-overlays.py`.

## 2. The shoot — measured on job 1 (`projects/monetized-before-gta6/`, 2026-09-23)

- **Camera:** 1920×1080, **59.94 fps** (60000/1001), H.264 ~50 Mb/s, PCM stereo 48 k scratch audio (live, usable as
  a sync reference). One continuous take (~21 min).
- **Voice:** the creator cleans the voice themselves in **Adobe Enhance Speech v2** before handing over
  (job 1: `…-esv2-2p-bg-10p-music-10p.mp3`, 128 kbps MP3, 48 k stereo) and lays it on A1 in Premiere, aligned to
  the camera. That enhanced track is the program audio; intake muxes it onto the camera picture
  (`PLAYBOOK.md` § Intake).

## 3. Assets

Channel-specific assets (logos, lower-thirds, Skool branding, music picks) go in `assets/` subfolders named
`affanwiz-*` and are listed here as they arrive. None yet.
