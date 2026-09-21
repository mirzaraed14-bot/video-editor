---
name: reference-higgsfield-connector
description: Higgsfield AI video is connected as a claude.ai account connector (not .mcp.json); credits need approval before spending
metadata: 
  node_type: memory
  type: reference
  originSessionId: 16e49e33-bab8-4330-9a7e-da710bc35f95
  modified: 2026-09-15T02:22:42.925Z
---

Higgsfield (AI video/image generation) is connected as a **claude.ai custom connector** (Settings → Connectors, URL `https://mcp.higgsfield.ai/mcp`), tools appear as `mcp__<uuid>__generate_video`, `balance`, `models_explore`, etc. A project `.mcp.json` entry was tried first and its OAuth sign-in failed in the desktop app ("Couldn't complete sign-in"), so it was removed — don't re-add it. The `claude` CLI is not installed on this PC (desktop app only).

Plan: pro. Credits 349.5 on 2026-09-15. Preflight with `get_cost: true` (spends nothing); 5 s 16:9 silent test prices: Kling 3.0 pro 7.5, Veo 3.1 Lite 6 s 6, Seedance 2.5 1080p 45, Cinema Studio 3.0 1080p 50.

3D (preflighted 2026-09-15): Meshy 6 text-to-3D full + rig + canned animation = 25 credits; Tripo text-to-3D textured = 5. The 3D Jutsu scene builder (Blender 5.2 worker; `scene_builder_3d_*` tools, I write bpy code) has no cost preflight. MEASURED 2026-09-15 (project "Affan Afterhours - Hot Coffee reenactment test", id 4ca29e31-7b19-4b4b-93a9-a32eb40b4ae7): creating the project, a 69-object scene built in bpy, and a 1080p Eevee still all cost **0 credits** (balance 349.5 before and after). But the render took **192 s per 1080p still** (32 samples, raytracing), so animated renders on their worker are impractical: use it for STILLS only. Import is catalog-only (no people or monitors in the catalog; Meshy GLBs can't be imported), so figures have to be built from primitives, which gives a wooden-mannequin blockout, not Fern-quality people. The dark mood and lighting worked. Test still: `projects/gta-san-andreas-hot-coffee/broll/reenact-tests/blender-test-01-still.png`. **The pipeline that works (tested 2026-09-15, balance 349.5 → 340):** Blender blockout still (free) → `media_upload` + curl PUT + `media_confirm` → `generate_image` nano_banana_pro 2k with the blockout as `image_references` (2 credits; the job reports model nano_banana_2) → `generate_video` kling3_0 pro, sound off, 5 s, `start_image` = the image job_id (7.5 credits, ~2.5 min, outputs 1928x1076 24 fps, so scale to frame in Premiere). The result looked Fern-like. Fixes for next time: the image model invented a desk clock whose digits morph in the video (keep text out of generated shots; do the 11:37 PM slug as our own graphic); the screen UI looked Windows 7 (anachronistic for 2005, so prompt Windows XP); the head drifted toward profile by the end (prompt "head angle locked, back of head to camera"). Files: `projects/gta-san-andreas-hot-coffee/broll/reenact-tests/`. The rig animation library (678 actions) has sitting/idle/walking but no typing.

**How to apply:** show shot list + credit cost and get an explicit yes before any real generation. Intended use: S1 reenactment b-roll for the fern-inspired preset (`presets/youtube/fern-inspired/`), placed into the Premiere edit. Related: [[user-abundance-wisdom-editor]].
