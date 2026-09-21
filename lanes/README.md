# lanes/ — everything app-specific, one folder per finish surface

**The preset says WHAT, the lane says HOW, [`LANES.md`](../LANES.md) is the per-step index between them.**
Everything in here would be wrong on a different editor; the universal tools stay in `workflows/`.
This table is the ONE file inventory for `lanes/`.

| Folder | App skill (the HOW doc) | What is in the folder |
|---|---|---|
| [`premiere/`](premiere/) | `.claude/skills/premiere-pro` | `premiere-bridge.mjs` (headless bridge: `replay`, `zoom`, `frame`, `grade-layer`, `diff-edl`, any tool), `premiere-up.sh` (launch + autostart), `premiere-pid.sh` (THE "is it running" check), `premiere-dismiss.sh` (invisible modals), `grade-lut.py` (Lumetri LUT written into the `.prproj`), `place-graphics.py` (V3/V4 placement, readback-verified), `review-frames.py` (step-5c evidence: bridge frame grabs, per-graphic contact sheets, INDEX.md), `place-sfx.py` (step-6 SFX rows onto A2–A4, readback-verified), `place-music.py` (the opt-in bed onto A5: onset-trimmed, −20 dB through the keyframe, 2s tail, bounce-proved), `audio-polish.py` (step 3: the measured Amplify + Hard Limiter on every A1 clip, readback-verified), `premiere-grading.md` (the step-4 lane sheet), `premiere-templates/` (adjustment-layer donor + minter, CEP autostart patch, locked-screen tools), [`lab-notes.md`](premiere/lab-notes.md) |
| [`resolve/`](resolve/) | `.claude/skills/davinci-resolve` | `resolve-grading/` (color groups + DCTL playbook), `resolve-audio-polish/` (the step-3 ReplaceClip pass), `resolve-export.md` (delivery render truth table), `resolve-templates/` (fps-matched `.drp` + minter), [`lab-notes.md`](resolve/lab-notes.md) |
| [`capcut/`](capcut/) | `.claude/skills/capcut` | `capcut-bridge.py` (file lane + live AX lane + export), `premultiply.sh` (straight → premultiplied alpha, required before every `add-overlay`), `capcut-templates/` (schema donors), [`lab-notes.md`](capcut/lab-notes.md) |
| [`chat-only/`](chat-only/) | `graphics-build` (chat-only mechanics) | `incremental-graphics.md` (the ffmpeg assemble + part-by-part recomposite sheet) |

**Adding a lane** = a folder here, a skill, a column in `LANES.md`. Nothing in any preset.

