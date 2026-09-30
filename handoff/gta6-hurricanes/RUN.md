# RUN — gta6-hurricanes (ABW8 · Sequence 16)

## ▶ STATUS: CREATOR'S PASS + THREE CALLS DONE (2026-09-30) — resume here
The creator cut Sequence 16 themselves (nests, cut zooms, zoom-insurance pushes, music on A2), then asked for three
things. All three placed, verified and saved. Backup taken first: `premiere-backup/ABW8-before-music-drops-sfx.prproj`.
- **Music out under every cut zoom** → `music-dropouts.py`: 22 cut-zoom ranges (`brief/cutzoom-ranges.json`, incl. the
  small 103 % at 105.64 s and 105 % at 231.18 s), music already silent in 5, razored + lifted in 17 (29.95 s), no
  ripple; A2 9 → 26 clips, 0 overlaps, worst edge 0.1 ms. Before/after: `brief/A2-before|after-dropouts.json`.
- **A pop on every overlay switch** → `overlay-sfx.py`: Epidemic "Cartoon, Pop, Mouth, Finger" (`sfx/es-pop-mouth-finger.wav`)
  on **A3**, 44 pops = 24 entrances + 20 internal switches, −6 dB clip level; exits back to the face silent. Proven
  by an A3-only bounce (`review/a3-only-bounce.wav`): 44 onsets, all on plan, peak −6.7 dBFS. The alternate
  "UI Click Select 01" is in the bin `Game Informer/SFX`, not placed. Plan: `brief/overlay-sfx.json`.
- **C02 without the zoom** → `ov-c02-v2.mov` (stills held dead still, `build.py` `NO_PUSH`), swapped on V4 at
  6.123–7.724; matte unchanged. Program proof `overlays/_tmp/pr/c02v2-proof.jpg` (inset still, matte moving).
- Everything else read back unchanged within 2 ms (`brief/seq16-after-sfx.json`): V1 46, V2 43, V3 24, V4 24, A1 140.
**Next action:** the creator's review. If C02 still reads fast: 2 stills at 0.8 s each instead of 4 at 0.4 s.

## ▶ (earlier) OVERLAYS PLACED (2026-09-30) — from the creator's Tella brief (`BRIEF.md`)
All 24 overlay slots the creator marked on V2 are placed on ABW8 · Sequence 16: **V3 = 24 animated colour mattes
(a different palette per slot), V4 = 24 overlays** (ProRes 4444 alpha, inset 85 %, rounded corners, baked drop
shadow). `place.py --verify`: 48/48 clips exact to the block edges; V1 (98) and V2 (43) unchanged; project saved.
Program-output proof: `overlays/_tmp/pr/program-proof.jpg`. Backup before: `premiere-backup/ABW8-before-overlays.prproj`.
Rebuild any slot: edit `overlays/build.py` SLOTS → `build.py --only N` → `place.py --apply` (skips placed slots;
remove the old V3/V4 clip first to re-place). Sources: `broll/` (YouTube), `overlays/gi/` (Game Informer),
`overlays/hf/` (Higgsfield Vice City bg, 0.5 credits), Extended Look + trailers from `projects/gta6-pc-release/broll/`.
**Next action:** the creator's review of the overlays.

## ▶ (earlier) rough cut — resume here (2026-09-30)
**ROUGH CUT DONE, ON SEQUENCE 16, SAVED.** ABW8 · `Sequence 16`: the creator's raw drop (3 clips) removed, sequence
set to 59.94 while empty (read back `4237833600`), EDL replayed: **122 clips on V1+A1, 6:48.4, 0 gaps, every in/out
0.00 frames off the EDL**, nothing on other tracks, project saved by the replay. Media `gta6-hurricanes-synced.mov`
in ABW8's root bin next to C1315. **Next action:** the creator's pass (cut zooms, 0.8x slow-downs, labels).

| | | |
|---|---|---|
| channel | Affan Afterhours, **the FACE-CAM style** | `presets/youtube/affan-afterhours-facecam/` (HUMOR · PLAYBOOK · LESSONS) |
| format | long-form YouTube 16:9, probed 1920x1080 59.94 | |
| lane | Premiere 2025, the creator's LIVE `ABW8.prproj` | target **`Sequence 16`** (1920x1080, handed over at 60.00 fps timebase 4233600000) |
| backup | `premiere-backup/ABW8-before-rough-cut.prproj` | taken before anything touched Sequence 16 |
| subject | Game Informer's GTA 6 cover story: hurricanes and weather, what's confirmed vs guessed, GTA 5 rain handling, pedestrians hiding + the witness system, Red Dead 2 weather effects, animal count vs RDR2, quick-fire activities, a Twitter rumour on Jason/Lucia, the Vice City 2002 rain detail | no script this time |
| camera | `X:\Recordings\Afterhours\C1315.MP4` · 1920x1080 · 59.94 · 819.32 s · 6.2 GB | read in place |
| voice | OBS `E:\Shorts\...\Batch Batch\2026-09-29 22-54-18.mp4` → `raw/originals/obs-2026-09-29-225418.mp4` | 787.95 s AAC |
| master | `raw/gta6-hurricanes-synced.mov`: camera video stream-copied + OBS voice at **the creator's own offset** (camera = OBS + 19.3833 s, from their Sequence 16 in-points 48.7667 / 29.3833) + the camera mic from 807.3667 s, exactly where they switched A1 to it | **sync NOT re-measured: the creator said it was already synced** |
| constraints | keep improvised jokes (channel standing rule since 2026-09-25) | |
| started | 2026-09-29 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | OBS copied, camera read in place, master muxed in 6 s |
| 2 | Rough cut | done — on Sequence 16 | 122 segments · 408.4 s (6:48) from a 752.8 s voice take · `transcript/cuts.json` + `outputs/gta6-hurricanes.transcript.json` · dead-air gate PASSED · fresh-eyes: flow review 2 real (kept "in the, um," restart, "what happened—"), mechanical review of all 118 joints 5 real (incl. a "ha-" fragment, "I th-", "I, I, I", "the a store"); all fixed in `fixes.py`, each re-proven by exact-span ASR · replayed 122/122 frame-exact |
| 3 | Audio polish | — | the creator's (Enhance Speech) |
| 4 | Color grade | skipped | none in this style |
| 5–8 | | — | the creator labels first |

**How the cut is built (re-runnable):** `python transcript/build-cuts.py` (every keep commented) → `cp` to
`/tmp/video-editor/gta6-hurricanes/cuts.json` → `RENDER=0 splice.sh` → `polish-boundaries.py` →
`python transcript/fixes.py` (12 review fixes, each on a measured dip and proven by exact-span ASR) →
`RENDER=0 splice.sh` → `dead-air-qa.py`.

## What the transcript hid (again)
WhisperX merged retakes on this OBS voice exactly as on gta6-vice-city-sign: "In Rockstar games" x3, "Braking gets
worse" x3, "Snowstorms, dust storms" x2, "30 plus land" x2, "the weather hasn't— has never been", "I think the—
I think the big ones", "where was the, where was the tweet". Found by a per-burst transcription of the raw
(`review/raw-bursts.txt`) and by transcribing the assembled cut; every splice checked on the exact kept spans.

## Request coverage
- **"ABW 8 Sequence 16 do the rough cut"** → steps 1–2, replayed onto Sequence 16 as trimmable clips.
- **"the audio is already synced, don't waste time on that"** → the creator's Premiere offset used verbatim, no measurement.
- **"wherever… the cut zooms… remove the music in that particular block… for the whole video"** → 22/22 ranges silent on A2 (`music-dropouts.py`).
- **"sound effects through epidemic sound on the overlays… wherever the overlay switching… nice and poppy"** → 44 pops on A3, bounce-proven (`overlay-sfx.py`).
- **"the 2nd overlay… remove the fast zoom… keep it simple"** → `ov-c02-v2.mov` on V4, no push, program-frame proven.

## Kept on purpose (improvised)
"The zoo? We're gonna have a zoo?" · the hiking joke (long pauses trimmed to ~0.55 s, nothing cut) · "so... I don't
know why I did that" · "Where was the tweet? God damn it. Oh my God, I... I lost it." · "fancy schmancy" · the
Twitter backstory aside · the full outro incl. "Hot Coffee mod, that flopped / Wolverine video, that flopped".

## Flags to report
- "at the beginning of GTA 6, in the prologue" (snow): said as "GTA 6"; the snowy prologue everyone knows is GTA 5's
  North Yankton. Kept as spoken; the creator's call.
- Profanity: "Oh, shit" (hiking joke), "God damn it".
