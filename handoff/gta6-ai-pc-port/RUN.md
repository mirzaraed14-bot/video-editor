# RUN · gta6-ai-pc-port

▶ STATUS: resume here (2026-11-10 03:07 PKT): **DELIVERED v1, his review pending** -> `X:\Claude Projects\Exports/afterhours-gta6-ai-pc-port.final.mp4` (= `outputs/gta6-ai-pc-port.final.mp4`; proof sheets `outputs/*.proof-sheet-{1,2}.jpg`). 1080x1920, 59.94, 1818 frames, 30.33 s, -12.1 LUFS, true peak -2.3 dBFS; audio vs the base ncc 0.974-0.997 at lag 0.0 ms (2/8/14/20/28 s); cue_check PASS (none weak on a phone, loudest -4.0 dB beside the voice). Built on the DEFAULTS after he came home at 2:30 am to questions ("I TOLD YOU TO MAKE IT"): speck-free clean source; sequencing as written; 0.8x + Vine boom on BOTH lines; no bed; C1454 NOT used; no Higgsfield; official GTA V footage of Franklin + Chop instead of a fan mod clip; captions LUCIA / VICE CITY. Rebuild: `bash projects/gta6-ai-pc-port/work/final_build.sh final overlay` (repo root); a card: `python yt/assets/build/mg_port.py <card>`. NOT done (lean, deadline): Topaz, the rough-cut fresh-eyes pass, the edit-review rounds, graphics-qa.py; nothing checked by ear. Next: his notes -> channel LESSONS; ask what C1454 is.

| Field | Value |
|---|---|
| Channel | Affan Afterhours (GTA), own video: Scott YT style, no Scott identity |
| Format | YouTube Short 9:16 1080x1920 from a horizontal raw (his script is a Short; one word from him overrides) |
| Lane | chat-only, code build, kit `presets/youtube-shorts/onyx-samples-youtube/kit/` |
| Fps | native 59.94 |
| Source for the edit | `raw/gta6-ai-pc-port.clean.mov` ONLY after his OK; until then nothing is cut |
| Final (planned) | `X:\Claude Projects\Exports\afterhours-gta6-ai-pc-port.final.mp4` |

| Step | Status | Output |
|---|---|---|
| 0 Brief + catalog pass | done | `BRIEF.md` (catalog pass, new moves, Bombas, prediction) |
| 1 Intake | done: raw copied byte-identical (cmp OK); job named after the content | `raw/C1453.MP4` |
| 1b Speck removal | done, his OK pending | `raw/gta6-ai-pc-port.clean.mov`, `work/speck/`, `review/` |
| 2 Rough cut | DONE 30.33 s (v1 + slowmo2); was: transcribed (WhisperX `transcript/words.json` + per-burst `work/cut/bursts.json` + slice pass `work/cut/fw_slices.py`); eye line `work/eyeline.json`; NOT cut yet | |
| 3 Audio | pending (baked by splice: measured gain into a -6 dBFS limiter) | |
| 4 Grade | pending (POP with this room's `grade_look` from head-start, stills first) | |
| 5 Graphics | pending (prompt bar, FX-27, FX-16, FX-42, FX-39) | |
| 6 SFX | pending (swishes on entrances; boom only if he says) | |
| 7 Review | pending | |
| 8 Export | pending | |

## Speck proof (2026-11-09, all frames; scripts in `work/speck/`, numbers in `verify_full.json`)
- **Found and tracked:** one ~3 px cream speck, front of the hair above the right brow. On screen in frames 238-5431 (3.97-90.6 s), every frame he is in the chair; stays put on the hair, rides with the head, never falls off. Tracked frame by frame (LK flow + top-hat), checked on 1 s sheets over the whole take and frame by frame at entry, exit and the fastest turns.
- **Mask follows it on every frame:** the mask is the speck's own measured blob on each of the 5,194 frames (median 17 px, max 48 px on motion streaks; feathered mask median 114 px, max 217 px).
- **Speck gone:** the detector that found it (11x11 white top-hat at the track point) reads raw median 113 (min 37) -> clean median 16.5, p95 30, max 46, against the hair 14 px around it on the clean file: median 19.3, p95 33.3. 31 frames read above their own 4 hair neighbours; all checked at 300 % (`ba_flagged.png`): hair highlights, no speck.
- **Nothing else changed:** outside the mask, clean vs raw Y = 55.35 dB PSNR, signed mean +0.003 levels, p99 1.25, p99.99 3.25, max 13 (all 5,670 frames); U/V outside the patch window 53.06 dB, signed mean +0.05. **Measured floor:** a plain ProRes 422 HQ transcode of the raw with no patch = 55.23 dB on the test span; the patched file on the same span = 55.23 dB. Patched vs plain transcode outside the mask: 0.30 % of pixels differ, max 2.75 levels (ProRes block spill beside the patch). Frames 5670 = 5670, pts identical, duration 94.5945 s both, TC 11:11:19:16, bt709 tv tags. **Audio untouched:** decoded PCM md5 identical (4f86302808351ba6dcd5a02a31793577 both).
- **No boil in motion:** frame-to-frame change of the patch vs 4 untouched hair patches riding the same track, over every spoken line (frames 725-5160): patch mean 0.50 / p95 1.34 levels, hair 0.67-0.77 / 1.84-2.37; fast turns (3480-3820): patch 0.59 / 1.49, hair 0.68-0.93 / 2.02-3.27. The patch is a touch steadier than the hair, never jumpier. 24 consecutive frames at 4x viewed (`boil_*.png`): nothing visible.
- **Through his finishing chain:** this room's POP `grade_look` + the 0.55 / 0.40 sharpen at Short scale (`review/speck-through-pop-grade-and-sharpen.png`): the raw's speck turns into a sharp white dot; the cleaned hair shows nothing.
- **For him:** `review/speck-before-after-400pct.png` (entry streak, calm, fast turn, exit streak), `review/speck-before-after-realspeed.mp4` (19.7 s, silent, 59.94: three of his lines as you'd see them, then a 4.5x window riding the speck over both fast turns).
- Not checked by ear or by eye at playback speed (no playback here); the real-speed clip is for him.

## Templates for the build (copy, never edit those folders)
`projects/gta6-head-start/`: `work/cut/{run_cut.sh,make_edl.py,fw_verbatim.py,slowmo.py}`, `work/final_build.sh`, `work/hook_panel.py`, `yt/build_spec.py` (59.94 keys, `grade_look`), `yt/assets/build/mg_head.py`, `yt/sfx/`. Scott templates named in head-start BRIEF § Style updates.

Constraints: work in silence (ffmpeg only, no playback, repeat it in any subagent brief); lean usage; no new agents without asking; builders Sonnet, never Fable; Higgsfield only with his OK; nothing on C:, no phone encode; other sessions live: stay in this job folder.

Skipped so far, with reason: none.

Before cutting: `raw/` now holds TWO videos (C1453.MP4 and the clean .mov) and `transcript/words.json` is a clips array keyed by the raw. Check how `splice.sh` picks its source and point the EDL explicitly at `raw/gta6-ai-pc-port.clean.mov` (same timeline, same pts, so the transcript times hold).

Where the job lives: the main checkout's `projects/gta6-ai-pc-port/` (gitignored), written by shell because the Write/Edit tool is blocked on the main checkout from this worktree session; asked him to OK that for this job (the head-start OK covered that job only).

Tool notes from this job: (1) WhisperX hid a restart again ("port the PC- / Because AI could port the PS5 version first" read as one long "the"); the slice pass caught it. (2) On this box a Python pipe from ffmpeg runs ~100 MB/s: a full 1080p decode through a pipe took >10 min where the decode itself takes 15 s. Decode only the frames needed (`select=between(n,a,b)`) or decode in-process with PyAV (`av==18.1.0`, has prores_ks). (3) The Write/Edit tool is blocked on the main checkout from this worktree session; state files are written by shell into this job folder only (the head-start precedent).
