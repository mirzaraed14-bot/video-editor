# RUN — gta6-vice-city-sign

## ▶ STATUS: resume here (2026-09-25)
**Rough cut DONE and on the timeline.** ABW8 / Sequence 05 now holds the cut: 146 clips on V1+A1 from
`gta6-vice-city-sign-synced.mov` (imported into ABW8's root bin), 0 gaps, every in/out frame-exact against the EDL,
ends 358.825 s; sequence set to 59.94 (read back `4237833600`) while empty; project saved 02:18. The creator's
raw two-clip sync drop was removed (it is in `premiere-backup/ABW8-before-rough-cut.prproj`).
**Next action:** the creator's pass (cut zooms, slow-downs, labels). Nothing else was asked for.

| | | |
|---|---|---|
| format | long-form YouTube, **the FACE-CAM style** | `presets/youtube/affan-afterhours-facecam/` |
| lane | Premiere 2025 (25.0) | creator's LIVE project `ABW8.prproj` (at `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW8.prproj`), target **`Sequence 05`**, which was **60.00 fps** (timebase 4233600000) against 59.94 footage |
| backup | `premiere-backup/ABW8-before-rough-cut.prproj` | taken before Sequence 05 was touched |
| subject | GTA 6 "Welcome to Vice City" sign on the Kaseya Center; the $975k-under-$1M loophole; the Miami takeover; the unverified GTA 6 box | `script.md` |
| camera | `E:\Skool Recordings\5 Sept Batch\C1299.MP4` · 1920x1080 · 59.94 · 1070.07 s | never copied; the master carries its video bit-for-bit |
| voice | OBS `2026-09-24 13-49-04.mp4` → `raw/originals/obs-2026-09-24-134904.mp4` | |
| master | `raw/gta6-vice-city-sign-synced.mov` (C1299 video + OBS voice, +22.9504 s, drift −34.9 ppm corrected, PCM 48k) | `audio/sync/sync.json`; the creator's own drop offset (22.950) matched |
| constraints | **keep improvised jokes** (the creator's explicit instruction, overriding the 2026-09-22 lesson that restated funny asides die) | |
| started | 2026-09-25 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | OBS copied; camera read in place; synced master built and measured (14 windows, ±3.6 ms) |
| 2 | Rough cut | done | replayed onto Sequence 05, 146/146 verified frame-exact · 146 segments · 358.8 s (5:59) from 1070 s raw · `transcript/cuts.json` + `outputs/gta6-vice-city-sign.transcript.json` · polish run · dead-air gate PASSED · fresh-eyes: flow + mechanical reviewers run, one real defect found and fixed (a "com-" before "another commissioner") |
| 3 | Audio polish | — | the creator's (Enhance Speech) |
| 4 | Color grade | skipped | none in this style |
| 5–8 | | — | the creator labels first, as last job |

## Rough-cut notes (what the transcript got wrong on this shoot)
WhisperX merged repeats and compressed timings badly on this OBS voice track: 11 kept rows hid a second
take inside them (e.g. "or through the Heat's last home game" said three times, "basically if you can…"
twice, "most of it is going toward turning" twice, "the Rockstar logo" twice). Found by transcribing the
ASSEMBLED cut, then locating each repeat with per-burst ASR (`runasr.py`) and proving every splice by
transcribing exactly the kept spans (`joinasr.py`, both in the session scratchpad). Worth doing on every
OBS-voice job: the words.json alone would have shipped the repeats.

## Request coverage
- **"rough cut of premiere pro abw8 sequence 05"** → steps 1–2, replayed onto Sequence 05 as trimmable clips.
- **"script attached for reference"** → `script.md`, used for STRUCTURE only.
- **"I improvise in some places for jokes, don't remove those"** → kept: "Pretty fucking big.", "Manhole covers!",
  "Would have been crazy though… Holy.", "It's kind of expected.", "I still haven't pre-ordered it. I'll get to it.",
  "sorry if I pronounce that name incorrectly", "I don't know how he got it", "Let's aim for… I don't know, I'm not
  that big of a YouTuber yet." Only retakes, stumbles, filler and dead air were cut.

## Flags to report
- Script beats NOT in the footage: the FAIR TURN section; the sheriff's quote as a spoken line (he said "She said,
  I've said this three times now" and stopped; likely an on-screen quote); "officially two editions, Standard and
  Ultimate"; "the sign is real, the box is a mystery" (the improvised close replaced it).
- Profanity kept: "Pretty fucking big." and two "pretty damn real/realistic".
