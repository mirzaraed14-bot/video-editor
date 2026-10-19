# RUN — cbum-last-show ("THE LAST SHOW", Chris Bumstead, Abundance Wisdom long-form #3)

## ▶ STATUS: resume here
**2026-10-19 ~15:00: STEP 4 host grade BUILT OFFLINE (v4); before/after sent; waiting on the creator's OK, then the creator
applies it by hand once (Premiere's scripting cannot set a Lumetri LUT).**
- **Build:** `work/grade/host_grade.py` writes `work/grade/cbum-host-grade.cube` (33^3) and the vignette, measured with
  look.py's exact metrics over all 630 frames of the cut (`work/grade/measure.json`).
- **v4 against raw:**
  - saturation 0.68 → 0.415 (target ≤ 0.46)
  - corners/centre 1.21 → 0.665 (≤ 0.70)
  - whites 0.70 → 0.51 (≤ 0.80)
  - blacks neutral
  - face box brightness 103 %, face saturation 0.76 → 0.63
- **The look:** the violet wall becomes a slate/deep teal, the lit skin is protected and slightly amber, the neon is
  darker, the teal shadow tone stays out of the blacks.
- **Sheet:** `work/grade/before-after.jpg` (6 sections). Tuning history: v1 greyed the face, v2/v3 over-saturated
  (leather, tinted blacks).
- **Placement plan:** a master-clip effect on C1359 (Lumetri: Creative > Look = the .cube, plus the vignette), so it
  grades every host instance and never the archive inserts, and survives re-replays. Measure a grabbed frame after,
  to match the vignette.

**2026-10-19 ~14:30: STEPS 2 + 3 DONE on ABW10 › "THE LAST SHOW - rough cut". NEXT = step 4 grade (long-form: one adjustment
layer, V2) → step 5 graphics (storyboard draft-1 vs BRIEF first; the creator's Q1-Q9 + pending decisions below).**
- **Step 3:** done with the creator's OK to take the lock.
  - `work/active_window.py` proved the target (DOM + QE + A1 = 154), then ran
    `audio-polish.py --apply --gain 8` and restored Sequence 09.
  - The bridge reported "not running" on that long call, but the script finished.
  - By-name read-back: **154/154 A1 clips = Amplify +8 dB → Hard Limiter -6 dBFS**. Timeline re-verified 154/154, saved.
  - Lab note added (`lanes/premiere/lab-notes.md` 2026-10-19).
- **Video 01 still MISSING:** the direct download was blocked again on 10-19, and the creator is fetching it.
- **Before step 5:** read the storyboard against `work/eye-final.md` (91 % on camera; cover the 5 'want face' reading
  segments) and the final transcript (lines #4, #25, #31-32 absent; #124 ends on 'giants').

**2026-10-19 ~14:00: ON THE TIMELINE: ABW10 › "THE LAST SHOW - rough cut". NEXT = step 3 audio polish (needs the active
window: waiting on the creator's OK to take ACTIVE-WINDOW.lock again).**
- **Where it is:**
  - The creator's pick (10-19): ABW10, which is open from `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj`.
  - New bin "THE LAST SHOW (cbum-last-show)" holds `X:\Recordings\Abundance Wisdom\C1359.MP4`, a byte-identical original
    of `raw/C1359.MP4`.
  - Sequence "THE LAST SHOW - rough cut": 1920x1080, 59.94, V3/A3.
  - **154 clips on V1 + 154 on A1**, contiguous, every in/out within 1 frame of `transcript/cuts.json`, ending 317.300 s.
    Project saved.
- **Tool:** `work/premiere_seq.py`. All steps go by name (`--import`, `--prepare`, `--replay`, `--verify`, `--save`);
  only `--create` took the lock: 1.5 s, the prior active sequence was restored by id and confirmed by DOM + QE reads.
  The other session's active sequence (Sequence 09) was untouched.
- **Step 3:**
  - `lanes/premiere/audio-polish.py` adds its clip effects through QE on the ACTIVE sequence, so it needs the lock and a
    proven switch to our sequence (`projects/gta6-ign-missions/transcript/active-window.py` pattern, EXPECT_A1 = 154).
  - The creator authorised the lock only for the create, so ask first.
  - **Gain measured:** kept speech -24.6 LUFS, true peak -6.4 dBFS, LRA 4.5 LU, so **+8 dB** to the -17 LUFS target (Amplify v 0.7222) into the -6 dBFS limiter.
- A re-replay discards clip effects: never re-replay after the polish without re-running it.

**2026-10-19 ~13:30: STEP 2 ROUGH CUT DONE AND VERIFIED. NEXT = the Premiere replay. Waiting on the creator: which project.**
- **The cut:** `transcript/cuts.json`, 154 segments, all pinned. Host runtime **5:17** (317.3 s).
- **Final verification:**
  - `work/cluster_sweep.py` (every segment split into speech clusters, each re-heard alone, containment across joints)
    found **0 repeats in 236 clusters**.
  - Its 9 long-word flags are single emphatic words.
  - The sweep caught one more abandoned restart. "He chose to stand next to the giants" now comes from TAKE 1 (863.8), the
    only complete take (`work/fit_test.py`: forced-alignment fit 0.86 against 0.81/0.61 for the restarts).
- **Eye-line on the final cut** (`work/eye_final.py` → `work/eye-final.md`):
  - **91 % on camera** (287.9 s), 29.4 s reading, mostly Ch1/Ch2 results lines.
  - The cold-open pivot (#15-19) is **100 % on camera**, so F3 holds.
  - 5 segments (10.7 s) the storyboard wants on face are reading: cover them.
- The 12:30 note below is superseded where they differ.

**2026-10-19 ~12:30: STEP 2 ROUGH CUT DONE, verified. NEXT = the Premiere replay. Waiting on the creator: which project.**

**The cut**
- `transcript/cuts.json`: 154 segments, all pinned.
- `outputs/cbum-last-show.transcript.json`: 922 words.
- Host runtime **5:18** (raw 19:17). With the script's clips that is ≈ 10-11 min.

**Gates:** dead-air PASSED; no source overlap. The final joint re-hearing (`work/joint-asr.md`) shows only mishears and
window-edge words.

**Reviews:** both fresh-eyes passes ran on sonnet.
- Flow: 3 real defects, fixed.
- Mechanical: 7 more hidden false starts, each confirmed by sub-span re-ASR, fixed by forced alignment
  (`work/realign.py`).
- The lesson is saved as AW LESSONS #18.

**Rebuild from scratch:** `bash projects/cbum-last-show/work/rebuild.sh`, run from the repo root. Re-run `work/realign.py`
(GPU) only if a realign span changes.

**Premiere (2026-10-19 12:30):** the open project is **ABW10.prproj**, loaded from a nested *Auto-Save* folder
(`E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj`). Another session is active on "Wellness Wisdom
reaction". Do NOT open another project or switch the active sequence until the creator answers. The replay pattern is
`projects/gta6-ign-missions/transcript/replay-seq39.py`: by name, chunks of 30, with read-back.

**Creator decisions pending (asked 10-19)**
- Re-record "On top." (#4)?
- Re-record "He didn't tell anyone until after the show. Here's what it was:" (#31-32)?
- Re-record "…next to the giants in Prague" (#124)? It was spoken as "in the Olympia", which is wrong, so the line ends
  on "giants".
- Confirm "2026" (dropped; the ledger shows 2016) and "Mental space" (kept as said).
- Fetch video 01 (X0LLRvrSWu8).

**2026-10-19 ~10:30: ROUGH CUT EDL DONE, gates green so far, in fresh-eyes review. NOT on the Premiere timeline yet.**
- **The EDL:** `transcript/cuts.json` (153 segments, all pinned, frame-snapped) and `outputs/cbum-last-show.transcript.json`
  (925 words). Host runtime is **5:27** (raw 19:17). With the script's clips that is ≈ 10-11 min against the ~12:00 target.
- **Provenance:** `work/cuts-draft.json` (cut_plan) → splice → `polish-boundaries` (108 → 150 segments, 7 ⚠ listed in
  `work/polish-2026-10-19.log`, polished EDL kept as `work/cuts-polished-2026-10-19.json`) → `work/deadair_fix.py` (8
  quiet runs closed) → `dead-air-qa` **PASSED** (0 runs ≥ 0.65 s).
- **words.json was re-timed** at 26 words where WhisperX stretched a word over a retake (`work/words_patch.py`, idempotent;
  the WhisperX original is `transcript/words.whisperx.json`). Rerun the patch if words.json is ever regenerated.
- **Hidden retakes cut:** "with a disease he-", "Six… Six", "is entering an open bo-",
  "that same week-", "one of the la-", "called it a controversial-", "but think" (each in `work/keep-overrides.json` _why).
- **Running:** the script-flow reviewer (sonnet, background) on `work/cut-script.md`, and `work/joint_asr.py` (every joint
  re-heard → `work/joint-asr.md`). Next: the mechanical reviewer (sonnet) adjudicates the joint report + the 7 polish ⚠.
  Then fix, re-gate, replay onto Premiere (ABW8, by name; ACTIVE-WINDOW.lock), audio polish (step 3), report usage.
- **Known transcript mishears:** now fixed at the source in `work/words_patch.py`, not the dictionary.
- **~10:50, ROUND 2.** The flow reviewer (sonnet) and `work/joint_asr.py` (152 joints re-heard, 26 flagged) found six real
  defects; every one was confirmed by slice re-ASR, then fixed:
  - "Breon Ansley" was cut before the surname.
  - "You see… nobody knows now" was kept TWICE.
  - "2019" had its onset clipped.
  - Two more false starts were kept: "and one of the loudest wh-" and "and said a lot of people".
  - **The 863-884 passage was the wrong audio.** WhisperX painted the script over take 2 and skipped 20 s. It is now
    rebuilt from the heard takes.

  Spoken "…giants in the Olympia, in the show" is factually wrong, so #124 ends on "giants". **Creator decisions pending:**
  re-record "in Prague", "On top", and "He didn't tell anyone… Here's what it was"? Confirm "2026" and "mental space".
  The chain is now one script: `work/rebuild.sh` (repo root), running.

**2026-10-19 ~09:50: words.json DONE (09:24, cuda float16, 1051 words); draft cut BUILT, not spliced yet.**

**Files**
- `work/align.json` / `align.md`: the order-aware aligner's result.
- `work/keep-overrides.json`: the hand pass, each fix with its reason.
- `work/cut-plan.md` and `work/cuts-draft.json`: 100 segments, 473.7 s of host before silences are cut. They play in recording
  order, with no source overlap.
- `transcript/take-map.md`.
- `work/slice-asr.json`: independent re-ASR of the gaps.

**Script lines NOT in the recording (tell the creator)**
- #4 "On top." was never said.
- #31–32 "He didn't tell anyone until after the show. Here's what it was:" were never said, so 1a runs into 1b.

**Probable slips (creator to confirm; both ASRs agree)**
- "2016" was spoken as "2026": dropped, and the ledger card carries 2016.
- "Mental peace." was spoken as "Mental space,": kept as said.

**Fixed**
- The #18 stutter is grafted ("for the best bodybuilder, for the best bodybuilder alive").
- "The Open, by the name, has no cap" is grafted to "The Open has no cap".

**Running:** slice re-ASR of the 12 long-span words (→ `work/slice-asr-longspans.txt`), to find retakes hidden inside them
before `/tmp/video-editor/cbum-last-show/cuts.json` → `RENDER=0` splice.

**Video 01:** the direct yt-dlp attempt on 10-19 was bot-blocked again (429 + sign-in), so the creator is fetching it
(SnapDownloader is installed). The `youtube.BLOCKED` flag stays.

**2026-10-19 09:12: transcription QUEUED** behind the GPU lock (held by the Onyx `cutcheck.py` job since 09:11): log
`transcript/transcribe-2026-10-19.log`. Done while it waits:
- `work/align_script.py` is now order-aware. Long sentences anchor on their last strong take; short ones are searched
  between their neighbours' keeps. Years and numbers are normalised, and out-of-order and overlapping keeps are flagged.
- New `work/cut_plan.py` (align + eye-line + storyboard face plan → `work/cut-plan.md` + `work/cuts-draft.json`).
- `corrections.local.json`: name casing.

Both scripts were smoke-tested on the parked C1361 transcript. Then: take-map (`workflows/take-map.py`) for retakes →
align → cut_plan → hand pass → `/tmp/video-editor/cbum-last-show/cuts.json` → `RENDER=0` splice → polish → dead-air gate →
fresh-eyes reviewers, one at a time on `sonnet` (slice re-ASR via the whisperx venv through `lock.sh gpu`, not mlx).

**2026-10-19 (Mon): GO, in a FRESH session** (the creator's call; the old session ran too long). Sources: 9 of 10 IN
(IDM, all h264 1080p, copied into `broll/` under their source names; see the download log). **01 "THE END" (X0LLRvrSWu8) is
still MISSING**: it carries 0a, 4a, 4d, 4e, 4f, so ask for it, but don't block on it.
**State:** the transcription of C1359 NEVER FINISHED (it collided with another session's GPU job on 10-14 and died; no
`words.json`), so there is no rough cut and NO Premiere sequence yet. **First action:** rerun
`projects/_onyx-batch2-2026-10/lock.sh gpu bash .claude/skills/rough-cut/scripts/transcribe.sh projects/cbum-last-show --force`
(it queues behind the shorts sessions' GPU jobs; ≈ 5-10 min once the GPU is free). Then take-map → `work/align_script.py`
(script host sentences ↔ takes) → the cut. Budget (memory feedback-usage-budget; usage 1 % on 10-19): one step at a time, no
parallel agents, report usage at each gate (after the rough cut, after the cold-open preview). 2026-10-19: the creator said "no
Fable for now": run this job on the default model, and don't put subagents on Fable either.

**2026-10-14 19:00: the RIGHT raw is in: `raw/C1359.MP4`** (1156.66 s, 59.94 fps, 1920x1080, PCM 48k; A/V start 0/0; recorded
today). The wrong file (C1361, a MrBeast talk) + its transcript/eye-line are parked in `_parked-wrong-raw-C1361/` (job copies;
originals untouched).
- Eye-line on C1359 DONE: `transcript/eye-line-raw.{json,png}`: Otsu threshold +0.241, separation 3.45 SD = RELIABLE; 322
  segments, camera 494.5 s vs reading 654.2 s (43 % on the lens). Contact-sheet labels checked by eye: correct.
- Host look on the new set (`research/host-look-C1359/look.json`): luma 0.18, saturation 0.68, whites 0.70, corners 1.30 of
  centre (purple/blue neon wall brighter than the face) → the host grade must pull the wall/neon down (target sat ≤ 0.46,
  corners ≤ 0.70).
- WhisperX `transcribe.sh --force` RUNNING since 19:01 (PIDs 70180/64104, OUTSIDE the Onyx GPU lock) → `transcript/words.json`.
  20:10: still running: it collided with the Onyx `spi-link-in-bio` transcription (in the lock since 19:15); two large-v3 on the
  8 GB card overflow VRAM and both crawl. Stopping mine was refused by the permission classifier → left running, the creator
  told. Future GPU jobs from this job go through `projects/_onyx-batch2-2026-10/lock.sh gpu <cmd>`.
- Storyboard DRAFT-1 (Fable agent, 20:10): `brief/storyboard-draft.json`: 91 beats, every one FX-coded, all 128 host sentences
  covered once with a `cover` plan, cold open computed 2.33 changes/10 s, worst 20 s window 7, 0.87 SFX/10 s, 2 impacts, 3 text
  events, 0 % synthetic; est. 13:36 untrimmed / 12:28 with TRIM ORDER 1-5. Generator: `work/storyboard/build_storyboard.py`.
  Deviations + Q1-Q9 for the creator are in the agent's hand-back (summarised in the next checkpoint); review it against the
  BRIEF before building.
- Sources: the Onyx queue never ran (YouTube bot check 08:26-19:28, all blocked); IDM via the creator is the only route
  (`broll/IDM-LIST.txt`). Only 03 (trailer) is in.
**Next action:** words.json → take-map (last take wins) → align host lines to the script → map each kept host line to
camera/reading → rough cut EDL (`RENDER=0`) → Premiere (multi-clip replay once the sources are imported).

| | | |
|---|---|---|
| format | long-form YouTube | probed: 1920x1080 |
| lane | Premiere (`.setup-complete` lane=premiere) | ABW8 project (shared with other sessions: by-name writes, `ACTIVE-WINDOW.lock` for anything on activeSequence/QE) |
| preset | `presets/youtube/abundance-wisdom/` (LESSONS 1-17) + `research/effects-catalog/` (FX-01..81) | no README/PLAYBOOK yet: the look lives in BRIEF.md + the storyboard |
| lane gaps | read LANES.md before step 3 | |
| source | C1359.MP4 · 60000/1001 fps · 1156.66 s · PCM 48k stereo · one take | `raw/C1359.MP4` (copy; original in X:\Recordings\Abundance Wisdom untouched) |
| script | `brief/CBUM-LONGFORM.md` (LOCKED 10 Oct) + `brief/CBUM-LONGFORM-SOURCES.md` | 10 videos + B1 + S1-S3 |
| constraints | the creator exports himself (never exportAsMediaDirect); review renders stay on X: (never C:/Downloads); everything editable in Premiere ("make this in premiere not in yourself") | |
| started | 2026-10-14 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1359.MP4` copied (C1361 was the wrong file, parked); script + sources in `brief/` |
| 2 | Rough cut | done | `transcript/cuts.json` 154 seg / 5:17 host; dead-air ✓; 2 sonnet reviews ✓; cluster sweep 0 repeats; replayed onto ABW10 › "THE LAST SHOW - rough cut" (154/154, verified, saved) |
| 3 | Audio polish | done | +8 dB (measured: kept speech -24.6 LUFS) → Hard Limiter -6 dBFS on all 154 A1 clips, read back by name, saved |
| 4 | Color grade | built, awaiting OK | host LUT + vignette v4 measured (sat 0.415, corners 0.665, whites 0.51); not on the timeline yet |
| 5 | Graphics | — | storyboard first (FX codes), cold open + title built to final first |
| 6 | SFX | — | |
| 7 | Review | — | |
| 8 | Export | — | the creator exports |

## Flags
- 2026-10-14 07:10: every YouTube source bot-blocked (plain yt-dlp). No cookies. IDM list handed over.
- 08:15: 03 trailer IN (1080p, from the research download). 02 came in at 360p only (YouTube's fallback): parked as
  `02_…_360p-standin.mp4`; fetch.sh now requires ≥ 720p. Research: ALL THREE studies DONE (intro diagnosis, cinematic, face-led opens) → BRIEF § Decisions 1-22 + forks F1-F6.

## Sources: download log (probe each on landing: height ≥ 720, H.264, duration ≈ the YouTube length)
| # | file | status |
|---|---|---|
| 01 | `01_CBum_2024-11_THE-END.mp4` | **MISSING** (not in the 2026-10-19 IDM batch): the creator to fetch https://www.youtube.com/watch?v=X0LLRvrSWu8 |
| 02 | `02_CBum_2024-10_Retirement-speech.mp4` | IN 2026-10-19 (IDM), h264 1080p 29.97, 427.2 s; the 360p stand-in is now obsolete |
| 03 | `03_CBum_2026-10_The-Standard-trailer.mp4` | IN, 1080p, 24000/1001, 124 s |
| 04 | `04_CBum_2018-09_Hospital.mp4` | IN (IDM), h264 1080p 59.94, 1697.4 s |
| 05 | `05_GenerationIron_2019-05_Breon-Ansley.mp4` | IN (IDM), h264 1080p 23.976, 901.3 s |
| 06 | `06_CBum_2024-11_One-Last-Ride.mp4` | IN (IDM), h264 1080p 23.976, 1312.5 s |
| 07 | `07_NSP_2024-11_Prague-results.mp4` | IN (IDM), h264 1080p 29.97, 756.0 s |
| 08 | `08_GregDoucette_2024-11_It-wasnt-close.mp4` | IN (IDM), h264 1080p 29.97, 741.1 s |
| 09 | `09_CBum_2025-08_Honest-thoughts.mp4` | IN (IDM), h264 1080p 24, 1193.3 s |
| 10 | `10_NSP_2026-05_Comeback.mp4` | IN (IDM), h264 1080p 29.97, 761.2 s |
| B1 | `B1_CBum_2024-11_Prague-posing.mp4` | IN (IDM), h264 1080p 25, 173.9 s |
Queue format (verified 2026-10-14): our 10 lines use only `bv*[vcodec^=avc1][height<=1080][height>=720]+ba[ext=m4a]`, no
fallback, so a clip without a ≥ 720p H.264 stream fails (no file) and the Onyx session reports it; that one goes to the creator's
IDM. Still probe every landing; a sub-720 file is renamed `_<h>p-standin`, never cut from.
