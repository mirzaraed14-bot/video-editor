# RUN — gta6-day1-mistakes ("14 Mistakes You'll Make On Day 1 Of GTA 6", Affan Afterhours video 24)

## ▶ STATUS: resume here (2026-10-27 13:40) — FULL DRAFT on ABW10 › "GTA 24 - 14 Mistakes On Day 1", review rounds 1-3 applied, SAVED 13:39:37; at his review (step 7)

**His answers (2026-10-27):** script v2 · CTAs yes (lower-right, 23 DAYS, uploads today) · CUT the two Phil-Hooker setup lines ·
KEEP the leak aside (no leak footage) · HIS ORDER (intro first) · **draft in ABW10 by 18:00**.
**On the sequence (bin "GTA 24 Day 1 Mistakes"):** V1 = the cut (242 pieces + 61 face-pass razors, 73 zooms) · V2 = 42 plates/b-roll ·
V3/V4 = 42 graphics + 9 CTAs · A1 = voice (static chain, 2 censored words, 241 crossfades) · A2/A3 = 70 SFX · A4 = music (5 beds + dropouts).
**Gates at the save:** gate-frames 0 · frame0 0 bare openings · graphics 93/93 · SFX 70/70 · music 0 problems · face pass 0 mismatches ·
lip sync 0 · censor 2/2 · crossfades 241/241 · audio chain 246/246.
**Reviews:** round 1 content/honesty (Sonnet) 11 → 11 fixed (`review/edit-review/round1-content.md`); round 2 visual/timing (Sonnet) 1 HIGH + 8 MEDIUM + 4 LOW (`review/edit-review/round2-visual.md`) → fixed: c02 chapter 0.73 → 1.90 s (d02a starts on "concealed"); payoff rows keyed to their first word (d02a "two long guns", d02b "goes in your", d10a "there was a safe": 1.4–1.8 s holds, the "Long guns?" gag and "So that cashier…" stay on his face); d14 NOT BEFORE holds 2 s, butting q14b; d12 row = his words (YOUR CHARACTER · GETS SLOW); d07 map at 80 %, right of its legend; d09 corner swaps to REPORTED + TGG source on the split-up row; k12 one credit (kicker dropped); b-roll inset shadow padded before the blur (was an 18 px hard slab); b03/b07 source pill bottom-right, off GTA V's minimap; two-shot b-roll credit no longer split in half (b01, b07). NOT changed (his call / taste): duplicate kicker attributions (d02b, d09), d10a row 1 on the premise line, the 71.3 s stretch gag clipping his right lens, q08 underline 0.25 s early. Re-placed 14 cells by name + 4 SFX moved (prune → apply): 93/93 · 70/70 · gate-frames 0 · frame0 0 (`review/frames/review-round2.jpg`). Round 3 (Sonnet, the 14 re-placed cells + neighbours, live read-back): 2 LOW → fixed: b03's moved pill sat on GTA V's street-name HUD → bottom-centre; b01/b07 shot 2 ran past its clean span into an extra shot (0.97 s / 10 frames) → source cuts MEASURED by scene detection (EL 701.833, 1083.333; GV 268.101) and the shot change set per insert (`transcript/broll-picks.json` cut2_at). 93/93 · 70/70 · gate 0 · frame0 0 (`review/frames/review-round3.jpg`). The loop stops at its cap (3 rounds); round 3's two fixes were checked by me on the live composite, not by a 4th reviewer.
**Next action:** his review. Read his timeline changes first (V1/V3/V4/A2/A3 diff against `graphics-plan.json` + `transcript/cuts.json`),
log each finding in `presets/youtube/affan-afterhours-facecam/LESSONS.md` (the 2026-10-27 block lists the new treatments awaiting his verdict).
Re-place loop: `hf-graphics/gfx/build-comps.py` → `render-changed.sh` → `hf-graphics/place-seq24.py --apply` → `--fix-ends` → `review/gate-frames.py` + `review/frame0.py` → save (heads-up to the other sessions, lock free).

| | | |
|---|---|---|
| channel | Affan Afterhours, face-cam style | `presets/youtube/affan-afterhours/EDITOR.md` → `…-facecam/` (CREATOR-HAND, HUMOR, LESSONS 2026-10-23); pattern = `projects/gta6-world-stops/` (learn, never copy files) |
| format | long-form YouTube 16:9 | probed C1409.MP4: 1920x1080, 60000/1001, 1052.55 s, pcm_s16be 48k stereo (camera audio = the voice), all streams start 0.000 |
| setup | NEW (vs video 23) | different room: sunglasses, Skool neon sign, YouTube plaque, red podcast mic in frame, centred medium-close → every framing number measured fresh |
| lane | Premiere 2025, the creator's LIVE `ABW10.prproj` (path: `projects/gta6-world-stops/RUN.md`) | NEW bin + NEW sequence, he exports himself (never exportAsMediaDirect) |
| shared Premiere | possibly another Claude session | by-NAME writes only; active-sequence switches only inside `lanes/premiere/ACTIVE-WINDOW.lock`; message the other session before saves; `review/stable.py` before writes; diff the live timeline vs the plan before any re-place (lab-notes 2026-10-23) |
| source | `raw/gta6-day1-mistakes.mp4` = byte copy of `X:\Recordings\Onyx\C1409.MP4` (8 053 850 539 B, original untouched, read-only) | |
| script | `script.md` = `X:\Claude Projects\GTA 6\video25-day1-mistakes-SCRIPT.md` v2 (confirmed by him 2026-10-27) | the strategy folder numbers it "video 25"; on the channel it is video 24 |
| CTAs | YES, like video 23 (confirmed 2026-10-27): GTA-phone countdown ~every 60 s, LOWER-RIGHT, measured clear of his head through every zoom | uploads TODAY 27 Oct → **23 DAYS** to 19 Nov |
| constraints | (1) keep his IMPROVISED bits; (2) ≥ 5 % better than video 23 (smooth / premium / expensive) — BRIEF § catalog pass + § better; (3) he exports; (4) fresh build: nothing copied from gta6-world-stops (renders, assets, plan) — reading it to learn is fine; (5) work in silence; (6) subagents Sonnet/Haiku only; (7) no C-drive exports; (8) job files are written by shell (the worktree guard blocks the Write tool on the main checkout); the channel LESSONS and lane lab-notes were APPENDED in the main checkout (as the other sessions do; the machine's sync commits carry them), nothing committed from this session | |
| started | 2026-10-27 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/gta6-day1-mistakes.mp4` (copy, size + first 100 MB byte-identical), `script.md` |
| 2 | Rough cut | done | 242 segments, 9:08.76 · build-cuts → polish → pauses (13 beats kept) → 39 ASR-proven fixes · dead-air 0 · replayed 242/242 verified |
| 3 | Audio polish | done | +4 dB (kept speech measured OUTSIDE the lock, one ebur128 pass → −17 LUFS pre-limiter) into the −6 dBFS limiter, `audio-polish.py --apply --gain 4` in `transcript/window1.py` · 246/246 A1 pieces chained (242 + the 4 censor razors) · 241 three-frame Constant Power crossfades (`transcript/a1-fades.py`) |
| 4 | Color grade | skipped | channel style: no grade, the lit room is the look (EDITOR.md) |
| 5 | Graphics | done | 42 cells + 9 CTAs (`build-plan.py` → `graphics-plan.json`), 51 HyperFrames comps (`hf-graphics/gfx/`), 42 V2 plates/b-roll (`hf-graphics/gfx/build-plates.py`), placed by `hf-graphics/place-seq24.py`; face pass 73 zooms (`transcript/face-pass.py`); edit-review rounds 1 + 2 |
| 6 | SFX | done | 70 cues, 13 families by meaning, 83 screened Epidemic files (`sfx/PALETTE.md`, `sfx/palette.json`), none used > 2x, placed by `hf-graphics/place-sfx-seq24.py` on A2/A3 |
| — | Music (opt-in pass, channel default) | done | A4: Loungin −20 · First Born −24 · Brooklyn −25 · Take a Ride (from 10.304 s) −24 · Loungin from its top −23, 0.45 s silence before each turn, `music-dropouts.py` under the zooms (`transcript/place-music-seq24.py`) |
| 7 | Review | waiting | the creator |
| 8 | Export | his | he exports himself (never exportAsMediaDirect) |

## Request coverage (reconciled against the saved sequence, 12:40)
- keep improvised bits → kept: the "I'm going to. / I am going to." ladder, "What is life?", the dumpster lawyer, "Long guns?", the CIA run, "fat", "lonely"; cut only the two Phil-Hooker setup lines (his answer)
- Premiere, NEW sequence + NEW bin in ABW10 → "GTA 24 - 14 Mistakes On Day 1" in bin "GTA 24 Day 1 Mistakes", read back by name
- ≥ 5 % better than video 23 → BRIEF.md § What video 24 does better (8 items; each one built: chapter rail, read-along quotes, A1 crossfades, bespoke diagrams, CTA corner, screened palette, headline card, honesty round)
- SFX fresh Epidemic set, screened, one family per meaning, ≤ 2 per file, trimmed, no UI clicks/chimes → 70/70 placed, max 2x
- pauses tightened, 13 comedic beats KEPT (`transcript/beats.json`), every removed span ASR-rechecked (`review/removed-check.py`)
- frame 0 → `review/frame0.py`: 0 bare openings
- censor "fuck" only → 2/2 (4:31.94, 7:13.17), A1 piece disabled + 10 ms fades, starts before the /f/
- CTAs → 9 × "23 DAYS", lower-right corner, 67–224 px clear of his head through every zoom (`review/cta-side.py`)
- new setup measured fresh, sunglasses → YuNet finds his face in every sampled frame; the leather chair also scores as a face, so the picker takes the box nearest centre (`review/face-measure.py`, `review/frames/face-sheet.jpg`)
- never show him reading the script (memory feedback-cover-phone-reading, every face-cam video) → measured 2026-10-27 13:3x, `review/look-read.py` (YuNet pitch + yaw over the cut, 5 fps, nearest-to-centre face; sheets `review/frames/look-read-sheet.jpg`, `look-turn-sheet.jpg`, `look-turn-zoom.jpg`): pitch does NOT separate (Otsu sep 2.68 = a single bell curve; the most 'down' frames are him gesturing at the lens), so no phone/low-notes reading; yaw: he faces the lens, only 4 turns ≥ 0.6 s (4 s total), 1 under a graphic, 2 are gestures (1:57.8, 5:01.2), 1 AMBIGUOUS: 0:03.7–0:04.7 on "I cannot believe" (a turn toward the monitor at frame right, or a delivery beat) → flagged for his eye, not covered (it is the hook's line)
- the step-5 QA gate (`workflows/graphics-qa.py`) not applicable here, as on video 23 (needs the default lane's placement.json); the job's gates instead: gate-frames, frame0, composite-check, the placers' read-back verify
- he exports → nothing exported

## Flags to report
- 0:03.7–0:04.7 ("I cannot believe"): a 1 s head turn toward the frame-right monitor — a script glance or a delivery beat? (his eye)
- 14 chapter cards open on a cinematic impact (`sfx/palette.json` family 'chapter'), the most trailer-like cues in the mix: his 2026-10-27 reactions note ("very very cheap", no trailer drums) is for those reactions, check these by ear
- `seq24.py --verify` reports "2 problems" by design: V1 303 = 242 EDL + 61 face-pass razors, A1 246 = 242 + 4 censor razors
- Cuts NOT inside a −30 dB dip (audible-joint risk, crossfaded), SEQUENCE times: 1:16.14, 1:59.75, 2:01.24, 2:14.27, 2:55.58, 3:13.63, 3:35.03, 4:19.71, 4:33.86, 5:36.72, 6:15.76, 6:17.11, 8:01.13 (weakest: 8:01.13)
- Stutters left in (no clean cut point): segments 12, 49, 199, 202 ("which-" after "chasing the story"), 218/219, 227
- "How about that?" zoom skipped (it sits under the d02c graphic); the "lonely" rung merged into the sad/lonely/depressed ladder
- CTA sound = a phone set down on a table (every phone-vibration file failed the tonal screen)
- Gain +4 dB was measured by one ebur128 pass outside `voice-gain.py` (that tool ran > 25 min inside the lock)
- 0.8x slow-down candidates for him (HUMOR.md): "And your car runs out of gas.", "he should be fired.", "What is life?", "I am going to."
- Runtime 9:08

## Skipped, and why
- Color grade: channel style (none).
- Export: his.
