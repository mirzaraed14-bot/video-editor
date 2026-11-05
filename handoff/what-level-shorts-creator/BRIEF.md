# what-level-shorts-creator: AffanWiz Short 3 "What Level YouTube Shorts Creator Are You?" (Scott Clary YouTube format)

## ▶ STATUS: resume here
2026-11-05: **SEQUENCING SENT, WAITING FOR AFFAN'S OK.** Nothing is cut or built. Text and questions: `SEQUENCE.md`.
**Next on his OK:** lock the prediction in `presets/youtube-shorts/affanwiz/RESULTS.md` row 3, then the cut (`work/cut/make_edl.py`), the 30 fps check, and the 60 fps final after his OK.

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
