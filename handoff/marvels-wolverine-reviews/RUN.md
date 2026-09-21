# RUN — marvels-wolverine-reviews

**Next action:** PAUSED at step 7 — the creator watches the Premiere timeline and calls taste adjustments (to do by hand in Premiere: the step-4 grade). Step 8 export only on the creator's go.

| | | |
|---|---|---|
| format | long-form YouTube | probed: 1920x1080 horizontal |
| lane | Premiere 25.0 (project format v43) | `projects/marvels-wolverine-reviews/premiere/marvels-wolverine-reviews.prproj` · sequence `marvels-wolverine-reviews` 1920x1080 59.94 |
| preset | `presets/youtube/default/` | |
| lane gaps | step 4 ⛔ ON THIS MACHINE | LANES says ✅, but the donor template + Look params are Premiere 26 (format v45); Premiere 25.0 cannot import them. Step 7 creator's; step 8 on the creator's go |
| source | 60000/1001 fps · 1821.32s (30:21) · h264 + PCM s16be | single continuous take → ONE section, no title cards |
| constraints | fresh build — nothing reused from an earlier job | |
| started | 2026-09-13 | |

## Steps

| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1284.MP4` copied from `E:\Skool Recordings\5 Sept Batch\`, size verified 13,892,791,646 B, original untouched |
| 2 | Rough cut | done | 229 segments · 9:42.57 (from 30:21) · polish + verbatim slice-ASR pass (~45 retakes/stutters/noise slivers fixed) · fresh-eyes: script-flow 1 accepted ("So number one" trimmed), mechanical 3 edge fixes accepted, 9 rejected (WhisperX merged-repeat fiction) · dead-air gate PASSED on final EDL · replayed 229/229 V1+A1, 0 frame mismatches, saved |
| 3 | Audio polish | done | +8 dB measured (kept speech −24.9 LUFS → −17; voice-gain.py's aselect overflows ffmpeg 9.0.1, so measured identically via concatenated kept WAV + ebur128) → Hard Limiter −6 dBFS on 229/229 A1 clips, `--verify` 229 verified, readback Amplify 0.72222 / Limiter 0.94 |
| 4 | Color grade | skipped (blocked) | `grade-layer`: importSequences of the v45 donor into Premiere 25.0 returns true and imports nothing. Look params minted on 26.3.2. Manual fix: adjustment layer on V2 → Lumetri → Creative > Look = assets/luts/rec709/Autumn-Rec709.cube, Intensity 70, Saturation 115 — or update Premiere to 26.x and run the scripted recipe |
| 5 | Graphics | done | 5c round 3 (cap): targeted re-check of round-2 fixes 7/7 PASS; motion found g72 '5 Years' touching the eyebrow; copy found g27 root arrow tips missing, g39 ray-traced crate identical to the flat one, g79 grid not person-shaped → all 4 fixed, targeted re-check 4/4 PASS. Loop stopped at the cap with every verified finding fixed; final full gate GREEN 0 FAIL · 76 warn · 2 waived; 119/119 placed (--verify). | 5c round 2 (verified evidence): motion/rhythm CLEAN (corridor fixes confirmed); copy/depiction 8 findings → 7 verified & fixed (g4 plan text: hand prop was cut, g31 switch+chip now land together on 'confirmed', g47 loop arrow built, g49 dotted trail draws dot-by-dot, g72 '5 Years' headline added, g93 'First Real Gameplay', g103 slide-off finishes before the cut), 1 refuted by measurement (g85 strike draws over 9 f: 1558→1810 px). · 5c round 1: gate green; 3 Sonnet reviewers; evidence compositor (ffmpeg 2-input overlay) intermittently dropped overlays → all 'missing graphic' findings discarded (renders verified intact by reviewer B + direct probe); accepted: g25/g27/g43 static back third (camera travel + pulse added), g85/g7 strike draw 7→9 f (registry DRAW); rejected: g53 '5' (sample 0.08 s before its pop). Round 1 does NOT count as clean for g1–g60 (bad evidence). · 5b done: 119/119 placed on V3/V4 (`place-graphics.py --verify` ALL PLACED, 0 extra), plan synced to placement (`--sync-plan`; re-running `plan-src/build_plan.py` now needs a `--sync-plan` after), `graphics-qa.py` GREEN 0 FAIL · 75 warn · 2 waived (`hf-graphics/qa-waivers.json`; run it with PYTHONUTF8=1 on Windows — cp1252 read turns × into an em dash) · 55 authored comps from `hf-graphics/gfx/build_gfx.py`+`scenes.py`, 64 text animations · composite spot-check at 3.6/24.4/66.9/398.6 s OK · 5a done: `graphics-plan.{json,md}` validated 0 FAIL · 119 graphics (64 text animations, 24 full-screens = 28.5%, 31 cards/lower-thirds, 25 push-ins, bare ≤5.6s) · low band y860–1030 · 5b: 64/64 text animations rendered (builder TOP_MIN 860) + 74 rows placed & verified; opening zoom-out + 25 push-ins baked on V1 at 36 frames (the locked 0.6 s at 59.94), keys read back 100.66/107.50/114.34 (zoom-out 100.94) · canonical transcript re-aligned first (kept-segment words from verbatim wav2vec2 alignment; original `transcript/words.whisperx.json`) |
| 6 | SFX | done | 567/567 placed on A2 (497) · A3 (62) · A4 (8), `place-sfx.py --verify` ALL PLACED 0 extra, levels within 0.2 dB, saved; slice edges floored to the 29.97 grid Premiere 25 imposes on audio items (backup `hf-graphics/sfx-plan.unsnapped.json`) — the tool's 1.5-frame tolerance at 59.94 is 25 ms, the item floor up to 33 ms; one stray clip from an interrupted apply removed · `sfx-plan.py` 567 rows (4 dropped by density), 16 hand rows in `hf-graphics/sfx-hand.json` (payoff words over racked scenes + g79 grid pop, times read from the comps); the 26 remaining ⚠ are the shell's unused `words()` helper body (a static-parse false positive) + g34 walkers (plain tl.to, no sound) |
| 7 | Review | paused for the creator | handed over: saved project, final timeline read back V1 229 · V3 107 + V4 12 = 119 graphics · A1 229 · SFX 567 · end 582.566 s; dead-air gate re-run on the final EDL PASSED; audio-qa.py skipped (Premiere lane, no flat render) |
| 8 | Export | — | |

## Request coverage
- Request: "RUN IT" + raw path → full default edit; no asked-for beats/omissions; no verbatim artifacts named.
- Hook read: "The Wolverine critic reviews are out. And it is not looking good." · takeaway: a good studio's game made through five terrible years (critics vs normal players; context not verdict).
- Closing passage kept complete: paid for it → Monday playing → coming back to tell you → "held the controller, which apparently is more than this game requires". Off-camera goofing after 1800s cut.
- Music: not asked for → skipped. Finish: Premiere timeline, pause at step 7.

## Flags to report
- Creator has ABW6.prproj open (Auto-Save folder, 98 sequences) — job project opens alongside; never close/save theirs.
- Tool bug (Windows): `polish-boundaries.py` writes literal `/tmp` → `E:\tmp`, while `splice.sh` reads Git Bash `/tmp` (AppData\Local\Temp). Worked around by copying; worth a repo fix.
- Tool bug (ffmpeg 9.0.1): `workflows/voice-gain.py` builds one aselect expression per job (229 between() terms) → "Cannot allocate memory"; worked around.
- `C1284 Audio Extracted.wav` beside the source; unused.
- Transcript flags: "same way these reviews landed" (= same day), "Same game, scale up" (= Skill Up), "Try it and test it" (≈ trying its best) — relevant to graphics copy.

- Premiere 25.0: QE exportFramePNG throws 'Unknown error'; program-frame proof = `exportAsMediaDirect` with the system PNG preset over a one-frame in/out, Windows backslash output path (scratchpad grab.py).
- Push-in / zoom-out frame counts doubled to 36 at 59.94 so the locked 0.6 s duration holds (preset numbers were written at 29.97).

- Motion blur: hyperframes caps render fps at 240, so at 59.94 the 8× lock is impossible; lower-thirds + light sliding scenes render MBLUR_SS=4 MBLUR_SHUTTER=3 (≈270° shutter).

- Tool bug (Windows): `place-graphics.py --sync-plan` rewrote graphics-plan.json through cp1252 → 64 strings double-encoded (· → Â·). Repaired in place (backup `hf-graphics/plan-src/graphics-plan.pre-mojibake-fix.json`); any later --sync-plan needs PYTHONUTF8=1.
- Tool bug (Windows): graphics-qa.py reads comps as cp1252 → '×' false-flags as an em dash; run with PYTHONUTF8=1.
- Evidence: review-frames.py's bridge grab is broken on Premiere 25.0; evidence composited from EDL + placed renders (per-layer ffmpeg extract + PIL stack; the 2-input ffmpeg overlay version dropped overlays and was retired). Push-in scale not in evidence frames.

## Skipped, and why
- Step 4 grade: blocked by Premiere 25.0 vs the lane's Premiere-26 templates (see step row).
- Background music: not asked for.
- Step 8 export: waits for the creator's go (Premiere lane).
