# RUN · paris-jackson-both-versions ("BOTH VERSIONS", Abundance Wisdom long-form)

## ▶ STATUS: resume here (2026-10-26 ~17:45, THE FULL EDIT IS ON THE TIMELINE: at his review)
ABW10 › "BOTH VERSIONS - rough cut" (id ae5f2f5b-…), 13:47.37, saved after every verify exited 0 (cold open 20/20 · clips 111/111 ·
Ch1-6 33/33 + 2 subscribe alerts · nests 15/15 · bed 15/15 · SFX 121/121 · A1 crossfades 118/118 + 46 edge fades · reading on his
face 0.00 s · lip sync through the nests 222 probes, worst 0.00 frames). **Final mix (read back, offline): −14.2 LUFS integrated,
−1.3 dBTP true peak (WAV and AAC 320k), 0 events above −1.2 dBFS, archive spread max 1.6 LU** (`work/mixdown.py`, `work/peak_events.py`).
B8 report: `B8-REPORT.md` (re-run `work/b8_report.py` after any change). Waiting on him: the host LUT on the C1397 master clip (by
hand), OK on 3 defaults (IG original 5a/5b, "…" captions 3a/6a, 5a bleep), § 7 rest, his export (then measure THAT file, ebur128
to -f null), then his review → LESSONS entries.
**Final audio values:** `audio_chain.py --gain 14.8 --limit -4.0` · `denoise.py --limit -4.0 --amount 0.25` · `a1_fades.py` (3-frame
Constant Power on 118 host butt joints, 3-frame Level fades at host↔clip edges) · 11 SFX trims (`sfx_trim.py --verify`, `trim_db` in
work/sfx/placement.json: 9 true-peak collisions + 3 cues pulled to ≥ 8 dB under the voice). Ceiling path −2 → −3 → −4 dBFS.
Subscribe alert 8:10.9 DROPPED (after 4a's "strung out on drugs", LESSONS 32), its SFX cue removed: 2 alerts (4:00.9, 9:47.4).
- **Audio (B4), first pass (values superseded above):** `work/audio_chain.py --gain 14.2 --limit -2.0` = Amplify + Hard Limiter clip effects on A1 (141), A2 (60, +14.2
  + its level match, −0.8…+15.4 dB) and the A3 bleeps; A2 Level keys only ATTENUATE (0 dB plateau, 3-frame fades, 1b/5a mutes).
  `work/denoise.py --limit -2.0 --amount 0.25`: DeNoise 25 % on the 10 A2 clips of 01/02/05/07 (2009-2013), order read back
  Amplify > DeNoise > Hard Limiter (limiter re-added last). **Piano bed** `work/music_bed.py` on A5: Epidemic "Midnight in Tokyo"
  (Sayuri Hayashi Egnell), 15 pieces under host runs ≥ 4 s only, music time resumes per run, one loop X 160.2 → Y 119.0, bed
  alone −30.0 LUFS (gain −13.9 dB), ends 707.12 = before the last 2 min (both B4 dry rules hold literally). Read-back mixdown
  `work/mixdown.py` (all 5 tracks, AAC true peak, spread, silences): **−14.1 LUFS, −1.0 dBTP (WAV and AAC 320k)**, spread
  median 0.2 LU, max 2.3 LU (07 Oprah 1.8 s piece, since unclamped). The zero true-peak margin was fixed after the SFX (see the top).
- **Face nests** `work/face_nests.py` (plan frozen in work/face-nests.json): 15 "BV face nest NN" on V1 (runs with face showing;
  fully covered runs + the cold-open block left alone), one sine-eased push 0.35 %/s capped at 4 %, A1 untouched (141).
  ⚠ V1 now holds nests: assemble.py --verify (V1 contiguity of raw clips) no longer applies.
- **Also placed (2026-10-26 afternoon):** 3 s black after "hi, daddy." (`end-black-3s.mp4`, V4 824.37-827.37: B1.6; runtime now
  **13:47.37**) · 3 subscribe alerts (`hf-graphics/build_cta.py`, `c0-subscribe-alpha.mov`, V5 at 4:00.9 / 8:10.9 / 9:47.4, calm face
  windows only, LESSONS 32; `place_build.py cta --verify` 3/3) · 3c mark re-rendered as `k-tag-3c-alpha-b.mov` = Part A's card
  "ON PURPOSE · AUGUST 2026" (place_clips.py VERS map). work/levels.json: the 07 Oprah piece unclamped −15 → −17 dB (levels.py
  clamped to the old Level range; gain lives in Amplify now), applied at the ceiling retune.
- B7 measured so far: no minors in any of the 29 graphic assets (looked at every one), "suicide" never on screen (captions "…"),
  not spoken in the first 30 s, silences ≥ 1 s are only the title, the end black and speakers' own pauses. B8 draft:
  `B8-REPORT.md` (generator `work/b8_report.py`, re-run after the final audio).
- **SFX placed** (`work/place_sfx.py --verify` 122/122, A3 62 + A4 60, no overlaps, bleeps untouched): the agent's fresh Epidemic
  pool (69 takes, none from an earlier job, max 3 uses, `work/sfx/HANDOFF.md`, `POOL.md`, `cue-check.txt`). Headroom: dialogue
  ceiling lowered −2.0 → **−3.0 dBFS** (`audio_chain.py --gain 14.2 --limit -3.0`, `denoise.py --limit -3.0` verified); remaining
  collisions → `work/peak_events.py` → `work/sfx_trim.py NAME=dB --apply --verify` (trims stored as `trim_db` in the cue sheet).
  Rebuild SFX only with `build_sfx.py --tag _b2` (new names), never over placed slices.
- Track map V1 host · V2 clips · V3 graded pictures · V4 scenes · V5 marks/l3 · V6 subtitles · V7 eyelid · A1 host · A2 clips ·
  A3 bleeps (+ SFX) · A4 SFX · A5 music.
- Credits for the description (CC): UCLA hospital photo Fuzzy901 CC BY-SA 3.0 · Staples Center photo Amin Eshaiker CC BY-SA 3.0 ·
  Oprah photo aphrodite-in-nyc CC BY 2.0 (Ch1-2). Ch3-6 evidence tables: work/build/ch3|ch4|ch5/HANDOFF.md.
- Waiting on him: the host master-clip LUT (grade/host.cube, by hand), and 3 asks (IG original, "…" captions, export path).
Next: his review in Premiere (he exports; B6 target in B8-REPORT.md) → apply his notes (fix only what he names) → LESSONS entries.

## Job
| | |
|---|---|
| Format | long-form 16:9, host 1920×1080 59.94 (auto-detected: horizontal) |
| Lane | Premiere (`.setup-complete` lane=premiere); **project: ABW10** (his answer, 2026-10-26) |
| Preset | `presets/youtube/abundance-wisdom/PLAYBOOK.md` (gist) + LESSONS 1–32 |
| Script | `brief/PARIS-LONGFORM.md` 🔒 FINAL 22 Oct (Part A film, Part B instructions, B7 QA) |
| Raw | `raw/C1397.MP4` ← `X:\Recordings\Abundance Wisdom\C1397.MP4` (copied, 6,778,683,283 bytes, 14:50.9) |

## Constraints (recorded at intake)
- Built in one pass: nothing copied from an earlier job's comps, renders, plans or assets. Tool scripts adapted from
  `projects/cbum-last-show/work/` (transcribe-windows.py, fit_test.py pattern) are tools, not content.
- No AI imagery, no stock, no minors on frame, "suicide" never as on-screen text, real evidence only, he exports.
- Silence: no players, no media pages; ffmpeg to files or `-f null`. GPU jobs via `projects/_onyx-batch2-2026-10/lock.sh gpu`.
- YouTube is BLOCKED (flag since 2026-10-24 13:58): no YouTube requests of any kind; he downloads with IDM.

## Steps
| # | Step | Status | Produced / notes |
|---|---|---|---|
| 0 | Pre-production (catalog pass, Beats list, lock checks) | ✅ for checkpoint 1 | BRIEF.md; `work/catalog-pass/`, `work/sweep/`, `work/grade/`, `work/quote-map.json` |
| 1 | Intake | ✅ | `broll/`: 13 files under B2 names (7 IDM downloads 2026-10-26 + 6 local); memorial (his full CBS2 feed, 9490–9575 s) and Oprah kept as WAV only; TMZ/AH replaced by her original IG video (pending his OK); 3 local look-alikes (two are childhood footage) identified by content and their copies deleted |
| 2 | Rough cut (host) | ✅ 2026-10-26 | `transcript/cuts.json`: **140 segments, 4:29.6 of host** from 14:51 raw, 106 Part A sentences (Ch1 cliffhanger cut, his call). Take map `work/align.md` (LAST complete take); LESSONS 18: slice re-ASR (`work/slice-asr-pass1/2.txt`), words re-timed at the source (`work/words_patch.py`: January 2020 line, 3 hidden retakes, Oprah/Paris mishears), cluster sweep **0 repeats** (`work/cluster-sweep.md`), dead-air gate **PASS**. Chain: `bash work/recut.sh` (+ its dead-air feedback lines). Coverage diff vs Part A: only his own read drift. Reading (head-down) spans on the cut: 58 runs, 149.9 s; 56 of 106 sentences mostly reading → covered (`transcript/look-down.json`, `work/sentence-reading.json`, `review/look-down-sheet.jpg`) |
| 2b | Clip plan | ✅ 2026-10-26 | `brief/insert-plan.json` (by `work/clip_plan.py`): 33 clips, 547.1 s, every piece word-exact (match ≥ 0.9) and anchored after its Part A host sentence; trims inside ranges per Part A (filler, the lawyer's question, ET's emoji, the spaghetti demo); lock fallbacks applied (3b, 4a). **Runtime estimate 13:45** (host 4:30 + clips 9:07 + title 2 s + hold 1 s + black 3 s): UNDER B7's 14:30–16:30 window |
| 2c | Assembly on ABW10 | ✅ 2026-10-26 | `work/assemble.py` (--backup/--setup/--tracks in ACTIVE-WINDOW.lock, his Sequence 25 restored + proven each time; --place by name; --verify 0 problems; --markers 14; saved). In/out land up to ~1.3 source frames early on 23.976/29.97/30 fps sources (Premiere snaps to both grids): fades at the joints in the audio pass |
| 2d | Pacing (his call) | ↩ REVISED after his review (tight) | `work/pacing.py` → `work/pacing.json`: slow blocks (#1-22 cold-open host, #50-53 Ch3 opener, #107-108 last lines) 0.8 s between sentences, 0.45 s inside; 1.0 s silence after "this is what she says to him"; 0.4 s breath at every host↔clip joint; only his measured silent frames. Assembly re-placed chained to read-back ends (no 1-frame gaps), verify 0 problems |
| 2e | Cold-open look | ✅ placed, at his review | grade/, hf-graphics/ (kit.py evolved from THE LAST SHOW's code: Instrument Serif + Plex Mono, warm black, ash/warm VERSION colours, muted red), work/co_archive.py, work/co_host.py, hf-graphics/build_co.py, work/place_co.py, work/levels.py, work/preview_co.py |
| 3 | Audio polish | ✅ 2026-10-26 | `work/audio_chain.py`: Amplify +14.8 → (DeNoise 25 % on 01/02/05/07) → Hard Limiter −4 dBFS on A1/A2/A3-bleeps, A2 level match inside Amplify; with bed + SFX (9 trimmed): −14.2 LUFS / −1.2 dBTP (`work/mixdown.py`) |
| 4 | Grade | – | target band measured (BRIEF § 5) |
| 5 | Graphics | – | catalog pass done; storyboard after the cut |
| 6 | SFX | – | fresh Epidemic pool |
| – | Music (his ask, B4) | – | sparse piano bed, pull-under list, last 2 min dry |
| 7 | Review | – | |
| 8 | Export | – | HE exports; B6 path question open |

## Request coverage (from the brief + the session task)
Full edit on his Premiere timeline · every B7 item checked by measurement · B8 report · RUN.md current · LESSONS after his review.

## Flags / found (details: BRIEF § 4 and § 4b)
- Locks: 1 ✅ (estate B-roll 0:05–0:11 only, a childhood photo at 0:03–0:04; RTT's undated IG photos never shown); 2 ✅ bleep;
  3 → fallback (cut at "It was really hard."); 4 → fallback (pre-line skipped); 5 → her original IG video (his OK); 6 ✅ her voice
  (voiceprint 0.65 vs reporter 0.29), keep 5f; 7 ✅ keep the butterfly; 8 ✅ reporter seconds excluded by word times.
- YouTube still BLOCKED (probe 2026-10-26: HTTP 429 + bot check); he downloaded with IDM.
- Host vs Part A: the Ch1 cliffhanger "Two versions. Remember that. Because the next part, nobody saw." is NOT in the raw (9 s room
  tone at 262–271 s) → CUT, go without it (his call, 2026-10-26); "2009" not heard in "June 25th" (the dateline graphic carries it); "his fans" most
  likely read "her fans"; "January 2020. Twenty-one" ✅; a stray read of 6e's line at 836 s is cut.
- Grade band measured on the active picture of the MJ-family Shorts (BRIEF § 5).
- Runtime estimate 16:30–17:30 before trims (B7 wants 14:30–16:30; Part A's trim order applies).
