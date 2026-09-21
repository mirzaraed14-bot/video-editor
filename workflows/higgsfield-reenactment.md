# Higgsfield reenactment — the HOW (tested 2026-09-15 on gta-san-andreas-hot-coffee)

The mechanics for one faceless reenactment shot, app-independent. WHAT a shot looks like is the preset's call
(`presets/youtube/affan-afterhours/README.md` § 1). Runs only on an approved `SHOTS.md` row; every step that spends
credits is priced first and the creator has said yes to the list.

Connection: Higgsfield is a **claude.ai connector** (Settings → Connectors, `https://mcp.higgsfield.ai/mcp`), tools
`balance`, `models_explore`, `generate_image`, `generate_video`, `jobs_wait`, `media_upload`, `media_confirm`,
`scene_builder_3d_*`. The `.mcp.json` route fails to sign in from the desktop app; don't re-add it.

## The three stages, per shot

| Stage | Tool | Credits | Notes |
|---|---|---|---|
| 1 · Blockout still | `scene_builder_3d_create_project` → `scene_builder_3d_run_python` (bpy, Blender 5.2) → `scene_builder_3d_query_python` renders a PNG via `artifacts.file(...)` → `scene_builder_3d_get_artifact` (15-min URL) → `curl -o` | **0** | Sets the room, the pose, the lens and the camera move. ~3 min per 1080p Eevee still (32 samples): **stills only**, never an animation. Catalog import only (no people, no computers): figures are primitives (ellipsoid head, cone limbs). Skip this stage for a shot whose framing is simple; go straight to stage 2 with a text prompt. |
| 2 · Polish | `media_upload` (PNG) → `curl -X PUT` the presigned URL → `media_confirm` → `generate_image` `nano_banana_pro`, 2k, 16:9, the blockout as `image_references` | **2** | "Keep the exact composition, camera and lighting direction"; describe figure, room, period, mood; end with "No text, no logos, no watermark". `jobs_wait` until `completed`, then `curl -o` the `result_url`. |
| 3 · Animate | `generate_video` `kling3_0`, `mode: pro`, `sound: off`, 5 s, 16:9, `start_image` = the stage-2 job id | **7.5** | ~2.5 min. Output 1928×1076, 24 fps, h264: scale to frame in the editor. `get_cost: true` first when the settings change. |

**≈ 9.5 credits per shot.** Alternatives priced 2026-09-15 for 5 s silent 16:9: Veo 3.1 Lite (6 s) 6 · Seedance 2.5
1080p 45 · Cinema Studio 3.0 1080p 50. Check `balance` before and after a batch; log the spend in RUN.md.

## Prompt rules (each one cost a retake)

- **No text in the frame, ever.** The polish model invents clocks, labels and screens with words; the video model then
  morphs them. Dates, times and places are our own slug overlays.
- **Period-correct, explicitly:** name the year, the OS ("Windows XP"), the hardware ("bulky beige CRT", "PS2").
- **Faceless stays faceless:** "completely smooth featureless head, no eyes, nose or mouth"; for the video add
  "keeps facing away, back of head to camera, head angle locked".
- **One light source motivates the shot** (monitor glow, a desk lamp, a window at night); "deep near-black shadows".
- **Motion in the video prompt is small and specific:** "slow dolly push-in", "fingers typing then a pause and a lean
  in". Big actions make the figure drift.
- **Never a real person's likeness**, no brand logos, no copyrighted characters.

## Files and naming

- Shots land in `projects/<job>/broll/reenact/`: `r<NN>-<slug>-blockout.png`, `-still.png`, `-v<k>.mp4` (a retake is a
  new version, the old one stays). Tests live in `broll/reenact-tests/`.
- `SHOTS.md` row → `graphics-plan.json` cell: `kind: full`, the shot is a full-screen SCENE like any other (in, hold,
  out; the slug overlay on top is a separate cell). **Placement through the lane placer is UNVALIDATED for external
  mp4s** as of 2026-09-16: first real job proves whether the placer accepts a row pointing at `broll/reenact/…` or the
  file is copied into `hf-graphics/gfx/renders/<gid>.mp4`; write the answer here.
- Graded or ungraded is the creator's call at the style test (grade layer covers V1/V2; V3 sits above it).
