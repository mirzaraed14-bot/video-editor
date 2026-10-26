# RUN · paris-jackson-both-versions ("BOTH VERSIONS", Abundance Wisdom long-form)

## ▶ STATUS: resume here (2026-10-26, checkpoint 2 v2 — after his pacing note)
**His note (LESSONS 33-34):** the pauses were overboard and showed him turning to read the script; the face cam stays TIGHT, a pause
only where truly needed and only under an overlay; every reading span under an overlay, never his face. **Done:**
- `work/pacing.py` MODE tight: no sentence pauses, no host breaths; only Part A's two explicit holds survive (1 s after "Happiest
  Day of My Life" = HOLD, 1 s after "this is what she says to him"), both to go under overlays in the Ch6 build.
- Assembly re-placed tight on ABW10 › "BOTH VERSIONS - rough cut" (id ae5f2f5b-…), verify 0 problems, clip levels re-applied,
  saved. Runtime **13:47.3** incl. 3 s end black (B7 floor 14:30: tight is his call; Part A's runtime was an estimate).
- Reading map (`work/reading_map.py`, head YAW 2.73 SD; pitch rejected on this set): 75 s of reading in 4:32 of host.
  `work/face_gate.py` = the gate on the placed timeline.
- Cold open rebuilt on the tight times, placed 20/20, saved: **0.00 s of reading on his face**, face on screen 10.8 s, all eye
  contact (#1-2 "She was 11… only daughter", #7 "Last year Paris did something strange", #19 "at the very end…").
  Proof: `review/co-preview-v3.mp4` (offline composite, never played here), `review/co-preview-v2-frames.jpg`, `review/co-joints-face.jpg`.
- Whole film: 76.3 s of reading still on his face after the cold open (40 runs): covered by the chapters' graphics pass (gate must be 0).
**Waiting on him:** the cold open's LOOK. Not done: −14 LUFS chain, bleeps, Ch1-6 graphics + captions, SFX, music.

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
| 3 | Audio polish | – | static chain retargeted to −14 LUFS / −1 dBTP (B4), pending his OK |
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
