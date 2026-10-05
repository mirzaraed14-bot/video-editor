---
name: reference-topaz-video-ai
description: "Affan's Topaz Video AI 5.0.4 is installed and scriptable (its own ffmpeg with tvai_* filters); his Iris recipe is wrapped in workflows/topaz-iris.py — use it for soft faces and low-res footage"
metadata:
  type: reference
---

**Topaz Video AI 5.0.4** (Affan says "Video AI 5"; a newer "Topaz Video" app also exists on the machine but he asked for
Video AI 5) is installed at `C:\Program Files\Topaz Labs LLC\Topaz Video AI\`, signed in, on an RTX 3060 Ti (8 GB).
Its own `ffmpeg.exe` carries the AI filters (`tvai_up`, `tvai_fi`, `tvai_stb`, `tvai_cpe`) and needs
`TVAI_MODEL_DATA_DIR` = `TVAI_MODEL_DIR` = `C:\ProgramData\Topaz Labs LLC\Topaz Video AI\models`. It has no libx264
(ProRes, FFV1 and NVENC only). Iris, Proteus, Artemis, Gaia, Nyx, Theia and Chronos models are downloaded.

**His recipe** (shown in the app on 2026-10-05, and identical to the commands in his own export logs under
`%APPDATA%\Topaz Labs LLC\Topaz Video AI\logs\*.tzlog`, which are the ground truth for the slider→CLI mapping):
Iris (iris-3), manual, fix compression 84, improve detail 73, sharpen 42, reduce noise 14, dehalo 20, anti-alias/deblur 14,
focus fix Strong (scale to ¼, Iris ×4), Chronos replacing duplicate frames (sensitivity 10 → rdt=0.01), full-frame
stabilization strength 50 (tvai_cpe pass, then tvai_stb ref-2 smoothness=6 full=1). His saved "Iris Preset" is in
`C:\ProgramData\Topaz Labs LLC\Topaz Video AI\presets\`.

**How to apply:** `python workflows/topaz-iris.py IN OUT [--out-scale 2] [--segments f1,f2,...]`. `--out-scale 2` keeps
his Iris values but outputs 2× (focus fix ½), which won clearly on the MFM vertical crops (2026-10-05 face test). Always
`--segments` at every cut and camera change of a spliced base, so the stabiliser and the interpolation never cross a cut.
Topaz appends a duplicate last frame; the script trims it. Speed: ~23 s of processing per second of 1080p→4K.
Related: [[project-onyx-sample-shorts]], [[feedback-sourced-stills-must-be-hq]].
