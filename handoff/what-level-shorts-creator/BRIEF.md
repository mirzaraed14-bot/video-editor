# what-level-shorts-creator: AffanWiz Short 3 "What Level YouTube Shorts Creator Are You?" (Scott Clary YouTube format)

## ▶ STATUS: resume here
2026-11-06 03:20: **60 fps FINAL DELIVERED, built after his OK on check 2 ("approved", 2026-11-06). He has not seen this file yet; done unless he has a note.** Sequence v1 approved 2026-11-05 ("Yes, use defaults"). Prediction locked (RESULTS row 3, 3K-50K). Not uploaded, nothing committed.
- **Files:** `X:\Claude Projects\Exports\affanwiz-what-level-shorts-creator.final.mp4` + `.final.proof.jpg` + `affanwiz-what-level-shorts-creator.thumbnail.jpg` (job copies `outputs/*.sample-yt.final.mp4`, `outputs/*.proof-final.jpg`, `outputs/*.thumbnail.jpg`). 1080x1920, 60 fps, 2056 frames, 34.27 s, 24.4 MB, CRF 16. The cover is `work/cover.py`: his script's WHICH LEVEL ARE YOU? (LEVEL gold) on cut frame 36, graded with this Short's look.
- **Gates, on the 60 fps file:**
  - **Reading (`work/reading_gate.py`, all 478 visible face frames):** face visible 7.97 s of 34.27 s in 6 runs (23 %), longest 1.97 s; **0 frames over 0.233, 0.00 s of visible reading**; |yaw| p95 0.137, max 0.17; 0 detector misses.
  - **Same picture he approved (`work/final_parity.py`, final frame 2j vs check frame j, per shot):** cards 36.5-38.3 dB, faces 31.2-32.5 dB (the Topaz difference), no outlier frame.
  - **Native cards (`work/card_parity.py`):** every even frame of the 60 fps cards vs the 30 fps cards 43-57 dB, so the same timeline; Chronos' own version of those frames read as low as 16 dB on motion windows, which is why they were replaced (1458 frames, `work/mg60.py`).
  - **60 fps cadence (`work/cadence_s01.py`, face zone only):** no duplicate frame (min step 1.0+), odd/even step ratio 0.99-1.03.
  - **Head:** no joint inside a face shot (`head_snap_gate.py picture.whip60.mov 2`: 0).
  - **Background (`work/bg_step.py` on the six face shots, `work/s01_motion.py` on the first):** median step 0.6-1.2 px per 60 fps frame. s01's 52 px at frame 4 is his hand crossing the right strip (response 0.02): at response > 0.5 the top wall reads max 5.2 px and the left strip 3.6 px over the whole shot, and 0.1-1.0 px on frames 1-14.
  - **Audio:** final vs base cut ncc 0.996-1.000 at lag 0.0 ms; -12.1 LUFS, peak -2.2 dBFS; 14 swishes, none weak on a phone, loudest -17.7 dB under the voice.
  - **Topaz:** no watermark on the frames viewed, 1028 of 1028 frames at 3840x2160.
  - **Frames viewed:** bar hand-off 232-246, hard cuts 330-333, 584-587, 1122-1125, 1474-1477, 2018-2025, the whip into the money card 674-704, full-size card and face frames.
- **Known and left, for him to look at:** on his two fastest gestures (frames 335 and 1133, about 5.6 s and 18.9 s) Chronos smears the hand on one 1/60 s frame; the face and the type stay clean there. Likely reads as motion blur, unproved: nobody has watched the 60 fps file at real speed, he is the first.
- **NOT RUN:** the fresh-eyes rounds of edit-review (usage tight, no subagents). Nothing watched at real speed or heard by ear (no playback here): the words were read against both verbatim passes at check 2.
- **A later note = data + ONE finish render, at 60:** overlay only: `yt_build final --skip picture`; a level only: `--skip picture,overlay`. A card: `python yt/cards.py <kind> yt/assets/broll60/<file> --dur .. --t .. --fps 60` (and the 30 fps one for the sidecar), `python work/mg60.py`, THEN delete `yt/work/picture.whip60.ungraded.mov` and `picture.whip60.raw.mov`, because grade and sharpen re-read their kept copies and would drop the new card; then grade, sharpen, `final --skip picture,overlay`. `yt/spec.json` is the 60 fps one now: `python yt/build_spec.py --no-cards` keeps it so.
- **Regenerable bulk, kept until he signs off:** `outputs/*.topaz.mov` 2.7 GB, `yt/work` 4.2 GB (four picture .mov + overlay.mov). Keep `yt/assets/broll60/`, `yt/`, `work/`, `transcript/`.

### Check 2 (30 fps, approved), for the record
- **Files:** `X:\Claude Projects\Exports\affanwiz-what-level-shorts-creator.check-30fps.mp4` + `.proof.jpg` (job copies `outputs/*.sample-yt.v2.mp4`, `outputs/*.proof-check2.jpg`). 1080x1920, 30 fps, 1028 frames, 34.27 s. The grade comparison: `work/look-b.jpg` (in/out pairs), `work/grade-compare.jpg` (Scott's default numbers on this room).
- **Why there is no check 1 for him:** my v1 kept three jump cuts on his face. `work/bg_strips.py` measured 25-29 px camera steps at them, the same defect as find-viral-angles review 2. An advisor review caught that I'd filed this as a footnote, so v1 never went out. It also caught numbers he never says (a rolling counter, digits in the log window).
- **Gates, on the exported file:**
  - **Reading (`work/reading_gate.py`, every visible face frame, absolute yaw, threshold 0.233):** face visible 7.97 s of 34.27 s in 6 runs; **0 frames over, 0.00 s of visible reading**; |yaw| max 0.16 per shot, p95 0.139; 0 detector misses. Sanity (`work/gate_sanity.py`): known reading frames read +0.35..+0.49, lens frames +0.07..+0.13. About 9.3 s of the kept lines are reading: all under cards. Eyes viewed on v1's sheet (`work/eyes.jpg`, same takes): on the lens, the low lids are blinks.
  - **Face runs:** 1.97 / 1.23 / 1.63 / 1.70 / 0.87 / 0.57 s, all ≤ 4.
  - **Head:** NO joint inside any face shot (`head_snap_gate.py`: 0). Background inside the face shots: median step 1.5-3.7 px; the spikes at frames 3, 306 and 1019 are phase-correlation noise on the flat wall (response ≤ 0.12), the strip with a real response reads 3.5-5.5 px.
  - **Audio:** audio-qa 23 joints clean; final vs base cut ncc 0.996-1.000 at lag 0.0 ms; mix -12.1 LUFS, peak -2.2 dBFS; cue_check: 14 swishes, none weak on a phone, loudest -17.7 dB under the voice.
  - **Words:** every caption chunk read against both verbatim passes (`work/cut/fw_cut_v1.*`). One pass mishears "Claude" as "plod"; the other and the raw burst read "Claude". Nothing checked by ear (no playback here).
  - **Grade:** POP re-aimed at this room (`grade_look` in the spec): p5 0, p95 165, cheek hue 15-17.5, sat .69 (in: sat .82). Scott's default numbers crushed his face (cheek val .60 -> .43, the mic gone).
  - **Hand-off frames viewed:** the small bar lands from the big one with no ghost (`work/v2-handoff.jpg`, frames 116-123), hard cut to the face at 1011 clean.
- **NOT RUN (usage tight, no subagents):** the fresh-eyes rounds of edit-review.
- **Differences from the sent sequence:** see `SEQUENCE.md` § What changed at the build.
- **Rebuild:** `cd` job, `python yt/build_spec.py --30`, repo root `python presets/youtube-shorts/onyx-samples-youtube/kit/yt_build.py projects/what-level-shorts-creator v2`, then grade + sharpen `--mask 0.55 --sharp 0.40`, then `yt_build ... v2 --skip picture,overlay`; an overlay change alone: `--skip picture`; a level alone: `--skip picture,overlay`. A note = data + ONE finish render.
- **Then the 60 fps final:** Topaz Iris 2x (`topaz-iris.py outputs/<job>.mp4 outputs/<job>.topaz.mov --out-scale 2 --no-stab --segments <the six face shots' edges>`, GPU lock, check for running topaz-iris first), `build_spec.py` (60), `uv run yt_faces --step 1`, `yt_build final`, grade, sharpen, `final --skip picture,overlay`. Chronos morphs card type: put native frames back over the settled card frames (`--fps 60` on `yt/cards.py`), or use the native 59.94 path (`gta6-all-fit-inside`). Then the cover WHICH LEVEL ARE YOU? (LEVEL yellow, his script).

**Corrections to the sent sequence, all on the audio:** "if you want" IS said twice (short-slice read; I had told him one pass may have invented it): the cut uses the last take. Line 8 starts at raw 60.72.

## The ask (Affan, voice-dictated, 2026-11-05, relayed by the English Editor session)
"You will be creating this in the Scott Clary YouTube style. Make sure to contact it, I've updated its style set and everything, so you have to contact it before you start making it. And whenever I'm looking at the screen, again you will place overlays and motion graphics there, and it will be 1% improved on the previous short that we made."

## Channel: AffanWiz (not Scott, not Afterhours)
- The audio follows `X:\Claude Projects\Personal Brand English - Skool Community\creator-shorts\CA-011-SHORT-v2-levels.md` nearly word for word, and the Skool sign is behind him. The folder `Afterhours` doesn't decide the channel (C1427 was AffanWiz too).
- That file binds this Short: the level-bar device, the title, the cover (WHICH LEVEL ARE YOU?, LEVEL in yellow), the fact flags. Its "Locked prediction (never edit)" line stays as it is.
- **Standalone job folder:** the script says "recorded separately", and the CA-011 long-form's job isn't named yet (another session holds C1449 as `_c1449-intake`). So this is `projects/what-level-shorts-creator/`, not `clips/` under a long-form.
- Scott's look applies. Scott's name, credit and watermark don't: @AFFANWIZ, credit tag VIRAL FACELESS CREATOR / 530K+ SUBSCRIBERS (`presets/youtube-shorts/affanwiz/ENGINE.md`).

## What "contact it" turned out to mean
I read it as: get the current Scott style set before building, from the files and the session that built the newest Scott Short.
- **Files read:** Scott `ENGINE.md` (11-05), `UPGRADES.md`, `research/shorts-style-radar.md`, `onyx-samples-youtube/CLIENT-SHORT-RECIPE.md` + `LESSONS.md`, the AffanWiz `ENGINE.md`.
- **H1's build session answered (2026-11-05):** template = `projects/_client-scott-clary/herjavec-500m-billion/` (`yt/build_spec.py`, `yt/sound.py`, `work/v2_build.sh`). It knew of no verdict on H1 v2.
- **The analysis session (`local_2f48725f`) answered later, and `UPGRADES.md` confirms it:** Affan approved the whole H1 v2 check ("approved and also start the IG build"): POP grade + sharpen, the very tight cut, captions from frame 1 with the hook below, the money ladder, the jet push + circle, the B&W-to-colour family. No comment on any single move, so it isn't a ranking. These are Scott client rules; its note: "every pause closes" was stated for Scott only, so ask him for his own Short.
- **The set as it stands:** captions + watermark from frame 1 with the hook low (y 1340 / 1436); one key word coloured; POP grade + sharpen `--mask 0.55 --sharp 0.40` on every render including the check; a steady push-in `drift` 0.025 on every face shot, pops settling at 1.10; `head_track` + `head_lock`; face ≤ 4 s; 0.08 s tight pauses; whips only into a scene, crest on the cut, 19-23 dB under the voice, cuts back to the face silent; no music; mix -12 LUFS / -2 dBTP.

## Where Scott and his own-channel rules collide
| Topic | Scott (11-05) | AffanWiz | What this job does |
|---|---|---|---|
| Opening | Captions + watermark from frame 1, hook below | Hook ON the caption line, captions replace it (11-04) | **Question 1 in SEQUENCE.md.** Default = Scott's newest, because he asked for the updated set. It reverses his 11-04 note, so he's told. |
| Pauses on the face | Every pause closes, jump cuts wanted | Only pauses ≥ 0.3 s on his own face (11-04, "the camera snaps with my head") | **Question 2.** Default = his own-face rule (memory `feedback-head-steady-across-cuts`, 11-05: "the AffanWiz rule stays for his own face"). Under cards the Scott tight pass runs in full. |
| POP grade + stronger sharpen | Every Short (approved with H1 v2) | Never used on this channel | **On**, as part of the updated set he asked for; he's told. This room's warm key light is the orange-skin risk (Bolt memory), so skin hue is gated on the check. |
| Frame 1 | Speaker's own cam | His script: "the empty level bar, not a talking intro" | Both: his cam with four fingers up AND the empty bar already on it. |

## Reading coverage plan (measured)
`workflows/eye-line.py` on the raw: Otsu 0.266, separation 4.50 SD (reliable), 43 % on the lens, the pre-roll included. Frame scan: `work/reading_scan.py` -> `work/reading.json`, 10 samples/s over 27.5-102 s; sheets `work/reading-sheet-*.jpg` viewed.
- **Speech-only recalibration** (the raw Otsu included the 27 s phone pre-roll): Otsu 0.233, camera mean 0.087, reading mean 0.375. Kept lines total ≈ 36 s, ≈ 9.3 s of it reading (`work/cut/measure_spans.py`, `work/cut/lines.json`).
- **The final gate uses absolute yaw.** Negative samples viewed (`work/negyaw.jpg`): mostly him facing the lens, but 68.1 and 85.7 are real turns that YuNet flips negative. Both fall in gaps the cut removes.
- No sunglasses on this take. He reads off a screen to his left: a head TURN (yaw). Pitch stays 0.54-0.58 on every burst, so pitch doesn't separate anything here. The iris proxy stayed within ±0.1 and separates nothing, so it's dropped.
- **Read aloud: the two money lines, raw 54.90-64.76, 100 % reading** → one full-frame MG. "Level four," (raw 82.3-83.5, yaw 0.35-0.44) → full-frame.
- Everything else reads in the gaps, which the cut removes. The edges are where he turns (e.g. raw 74.0-75.0 reads 0.36-0.63 just before "Now your shorts"), so a cover runs until yaw returns to camera level (~0.1), not merely under Otsu: "a half turn is still reading" (his GTA 26 review).
- **Proof at delivery:** face-visible seconds above camera-level yaw on the FINAL, re-measured on the delivered frames. Target 0 s. Face runs ≤ 4 s.

## The 1 %: what this one does better
**Over Short 2 `find-viral-angles` (the last on this channel), his notes built in from frame 1:**
1. **POP grade + stronger sharpen** (never on this channel; Short 2's dark navy cards and flat face have no real blacks).
2. **Steady push-in `drift` on every face shot** (11-04 note on Scott; Short 2 has zoomkeys only).
3. **The level bar: one object carrying the whole Short**, always visible, so the viewer sees where they are ("Numbered stages", Cleo Abram, UPGRADES queue, never used). Short 2's map fills only in the middle.
4. **FX-70 Ring and Benchmark: a red line across the bar above level 2** on "most people never get past level two", staying on screen; levels 3 and 4 fill past it. New to the channel.
5. Carried over, not re-learned: head tracking + `head_edge_pin`, no face pause under 0.3 s, no word said twice, hook holds until its line ends, real pictures, gate the background and not only the eyes.

**Over Scott H1 v2 (the newest in this format):** H1's receipts are mostly photo cards on a blurred plate (radar: "overused, rest them"). Here every level is its own built scene on the same object, with **no photo-on-plate card at all**, and the one physical image is real (19 crisp dollar bills: Bombas B9, "a small physical image").

## Catalog pass (CLAUDE.md learning loop): `CATALOG.md` read in full, all 137 stills in `shots/` viewed on contact sheets
- **Fits this video:** FX-69 Lone Yellow Bar (four cells, one lit), FX-70 Ring and Benchmark (the level-2 line), FX-71 Funnel Count / `mg-cards.py ladder` ($0 → $19 → ~$4,000 on his words), FX-33 Dust Void Drop (the bills alone on black), FX-55 Red Pen Underline (one word struck: PAYCHECK).
- **Not used on this channel yet:** all five, plus the Johnny Harris coloured highlight bar on one caption beat (BE HONEST; radar).
- **The last videos leaned on:** the photo card on a blurred plate with a tilt and a whip into it (Scott); an angle map with thumbnails (Short 2).
- **Considered, not used:** FX-13 Depth-Sandwich (KILLED on seated close-ups, and his head fills ~50 % of the width here), FX-11 Rival Colour Split (no rivals), FX-43 Tape Morph (no then and now of one person).

## Rules
- Only his words and numbers on screen; spoken numbers beat the script's (cards say ~$4,000, not $3,800, and $19). No client name, no Scott, no Onyx.
- Captions ≤ 19 characters, only ! ? and quotes, read word by word against the audio.
- No music (he scores). Swishes only. Sharpen and grade every render.
- Nothing on C:. Exports only to `X:\Claude Projects\Exports\`. No phone copy. Work in silence: no players, ffmpeg to `-f null` only, and that rule in any subagent brief.
- A later note changes only what he named: data + ONE finish render.

## Source
- Raw: `X:\Recordings\Afterhours\C1450.MP4`, copied to `raw/C1450.MP4`, original untouched. 1920x1080 h264 **true 59.94p** (YDIF ~3 on every frame), PCM stereo 48 kHz, the camera carries the voice, 114.1 s.
- Transcripts: `transcript/words.json` (WhisperX, ONCE, 112 words; it hides the retakes), `work/cut/bursts.json` (per-burst faster-whisper, CPU: shows them). Times for the cut come from the 10 ms RMS (`work/cut/raw_db10ms.npy`).
- **Frame rate:** the 30 fps check as the line says. At the final, weigh the native-59.94 path (`gta6-all-fit-inside`) against Chronos, because Chronos morphs type and the bar is type.
