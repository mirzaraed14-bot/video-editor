# jealous-uncle-fire-head — ABW10 · Sequence 35 (head on fire, whole reel)

▶ **STATUS 2026-10-31 ~20:30: FIRE VERSION SWAPPED ONTO V1 + CAPTIONS DELIVERED, at his review.**
- **Swap** ("swap my video in premiere with the fire version"): `outputs/jealous-uncle-fire.mov` (the BAKE: Premiere-exact
  frames + the three layers by Premiere's measured math, `work/bake.py`; ProRes 4444, video only, 1323 frames) now fills V1
  cut-for-cut: 9 clips at his exact cut points, inPoint = start (`work/pr/swap.py`; setIn/OutPoint floor → +0.5 ms). V2–V4
  emptied (the layers would double the fire). A1 audio unchanged (read back). Proof: 22 Premiere frames incl. both sides of
  all 8 cuts vs the verified layered frames: 0.39/255 worst mean (`work/pr/swapcheck.py`). Backup of his V1 before the swap:
  `work/pr/seq35-before-swap.xml` (FCP XML) + `.json`. NOT saved, NOT exported.
- **Captions:** `jealous-uncle-fire-head.srt`, 19 cues, yellow deep-talks, baseline **y1277** (chin 1162 + 115), first cue
  00:00, `caption_qa.py` PASS (1 warn: 14.76 "aisa" = Urdu "career ho to aisa", all 3 decoders agree). He drags the .srt onto
  Sequence 35 at 00:00 and applies the "affanwizu yellow" Track Style. Every line quoted (all the uncle's dialogue).
  Flag for him: 7.84 "haan yar sahi hai yar" (WhisperX dropped it; ur + hi + en hear it), 16.55 "warna" (Whisper: wonda/banda).
- Earlier the same day: the three layers were placed + verified on V2–V4 (below); the swap replaced them. Since the fire is
  now baked into V1, "B" (or any fire change) = re-bake (`work/bake.py`, flame/core rows < 420 zeroed for B) + re-run
  `swap.py`; the Crop Top trick below applied only to the layer version.

(previous status) He answered the A/B stills
"Looks good to me" → version A (flames rise into the top bar). V2 light / V3 flame / V4 core placed 0 → 22.05 s, blend modes
read back 2 / 22 / 18, V1's 9 clips unchanged. NOT saved (his project), NOT exported (he exports).
Proof (`work/pr/verify.py`, 86 Premiere program frames = both sides of every cut, the fastest moves, 7 per clip): inside the
fire, Premiere = predicted composite at 0.28/255 mean (worst frame 0.32); outside the layers' reach, identical to the
overlay-free grabs except ~600–800 px/frame at ±1/255, 97 % of them within 16 px of the flame edge (ProRes spreads the soft
fringe a hair) and ~20 px/frame farther (1/255 encoder rounding). Sheet: `work/pr/verify/premiere-frames-sheet.png`.
B on request = Motion > Crop Top 21.875 % (420/1920) on the V3 + V4 clips (NOT a track toggle). A re-cut of V1 needs a
re-render: delta fit (`work/sync/`) → track.py → render.py --prep → --render → replace the three clips.
Resume: if `outputs/fire-*.mov` exist but V2–V4 are empty → `python work/pr/place.py`; then `uv run work/pr/verify.py`.

## Layers (all 0 → 22.05 s, 60 fps, ProRes 4444; V1 untouched, no save, no export: he exports)
| track | file | blend (MEASURED value) | content |
|---|---|---|---|
| V2 | `outputs/fire-1-light.mov` | Color Dodge (**2**) | the fire's warm light: v = Lw/(1+Lw), so base/(1−v) = base·(1+Lw) (no copy of his pixels) |
| V3 | `outputs/fire-2-flame.mov` | Screen (**22**) | flame emission + bloom, opaque, black = identity |
| V4 | `outputs/fire-3-core.mov` | Normal (**18**), alpha straight | the solid hot core |
Premiere's blend-mode enum is NOT menu order (V1 Normal reads 18): measured by stepping 0–35 against predictions
(`work/pr/blendmodes.py`, errors 0.18 / 0.30 per 255). Sequence 35 composites alpha in LINEAR light (gamma ≈ 2.4 fits;
Screen/Dodge still act on encoded values): the core's semi-transparent edges read a touch brighter than still.py's gamma mix.
His sequence setting is left alone; `render.composite()` models it for the proof.

## Frame sync (fixed before the render)
The CRF-30 rebuild (`sequence_reference.py`) ran ~1.5 frames AHEAD of what Premiere shows on these 0.9x clips → the fire would
have led his head by up to ~50 px on fast moves. 86 program grabs → displayed source frame = floor(m + δ_clip), δ per clip
(`work/sync/`: check → offset → delta.json → verify_frames 86/86 exact). `work/frames.py` decodes those exact frames from the
original C1371; track (`work/track.py`, rebuild track kept as `track.rebuild.json`) and contours are measured on them.
Lab note written (lanes/premiere/lab-notes.md, speed-changed clips).

## His constraints (2026-10-31, in his words)
- "don't regenerate / reanimate my video… fire on my head that's it" → his footage is never sent to Higgsfield.
- "the fire should move with my head… with the momentum, within the physics" → spring-damper lean/stretch, reset per cut.
- "show me frames first so that you don't waste credits" (arrived AFTER the 2 plates were submitted: 30 credits spent).
- "flames which look super real and part of the footage, none of that drag-and-drop green screen type" → interactive warm
  light on hair/forehead/wall flickering with the fire, bloom, camera softness/grain match, dense burning band on the real
  hair contour. No embers/smoke (goofy risk).

## Spent
Kling 3.0 pro, 10 s, silent, 9:16, ×2 = **30 credits** (balance 1104.75 → 1074.75). Plates: `assets/fire-a.mp4` (used,
fuller), `assets/fire-b.mp4` (alternate tongues). Both are tall thin columns, so the crown is 13 tongues on the hair contour.

## The ask (Affan, 2026-10-31)
"make my head look like it's on fire… jealous uncle… use Higgsfield… every single piece of environment should be the same,
nothing should change except the fire which is on my head… throughout the whole video."

## Sequence 35 (read 2026-10-31, `transcript/sequence.json`, rebuilt cut `raw/jealous-uncle-fire-head-cut.mp4`)
- 1080×1920, 60 fps, 22.050 s. V1/A1: 9 clips of `X:\Recordings\PBU\C1371.MP4` (1920×1080 59.94), all **0.9x**, Scale 100,
  Position centre → the 16:9 picture sits in a band ≈ y420–1500 with black above and below; his hair top ≈ y470, so flames
  rise into the top black bar (a look decision to show him, not assume). Nothing above V1.

## Approach (advisor-checked 2026-10-31)
- **Higgsfield makes ONLY the fire** (flames on pure black, text-to-video, no audio). AI video-EDIT models (Kling Omni Edit,
  FLUX 3 Edit, Seedance video_edit) re-render every pixel incl. face/lips and output ~24 fps, so they cannot keep "nothing
  else changes".
- Head tracked per frame on the rebuilt cut (sequence space, speed/framing applied), smoothed WITHIN each clip, reset at the
  8 cuts. Plate blacks crushed to 0, feathered matte, base anchored on the hairline, scaled to head width.
- Deliverable: three layers above V1 (table above). Tied to the current cut: a re-cut needs a re-render (track.py →
  render.py --prep → --render). Proof: Premiere's own frames equal the overlay-free grabs exactly outside the layers' reach.
  The warm light on hair/forehead/wall is ON (he approved it in the realism stills); it only touches pixels near the fire.

## Tools (work/)
`track.py` (YuNet face + background-diff hair top, every frame, rebuild = sequence space) → `track.json`;
`comp.py` (plates, physics, crown; its own `--render` is STALE, unused); `still.py <t>` (the approved realism still, A/B);
`frames.py` (Premiere-exact frames); `render.py` (--prep / --still / --render, the full A look as 3 layers);
`pr/` (pr.py bridge + lock helpers, place.py, blendmodes.py, coretest.py, verify.py). Lesson: measure the hair contour on the rebuild frame against a rebuild plate; original-vs-rebuild diffs put flames on
compression noise (a flame down his temple at 16 s).

## Higgsfield preflight (get_cost, 2026-10-31, balance 1104.75)
Kling 3.0 10 s 9:16: 17.5 · Seedance 2.5 10 s 720p: 70 · FLUX 3 Video 20 s 720p: 120 · Seedance 2.5 25 s 720p: 175.
