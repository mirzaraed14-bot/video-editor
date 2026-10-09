# RUN — nick-martin-same-night ("SAME NIGHT", Nick Walker vs Martin Fitzwater, Abundance Wisdom long-form #2)

## ▶ STATUS: v4 FIX PASS DONE + PLACED (2026-10-08, late) — resume here: the creator's review of v4
**2026-10-09: 3c swapped to the CLEAN Arnold source (the creator's ask: the rip's music made it unusable).** V1+A1
262.8-285.8 now play `broll/13_ArnoldSports_2026-03_Mens-Open-finals-clean.mp4` (his IDM download of
youtube.com/watch?v=MruhAiTETrE) from 2291.4333, aligned by SOUND (`broll/match-13.py`: picture 2291.067, sound
2291.433, no drift; the rip carried its sound 0.37 s off its picture). Only those two clips changed (diffed against
`premiere-backup/seq36-before-arnold-clean.json`; XML `Sequence36-before-arnold-clean.xml`). His V1 lock was lifted for
that one clip and restored (`replace-3c-v1.py`). Level 0 dB like before; the clean arena audio integrates -15.4 LUFS vs
the rip's -19.0. The creator re-edited Seq 36 after v4 (3a + c26 gone, 3c now at 262.8): `seq36-v4.json` is stale.
The creator's whole-video review list, all eight items (lessons 10-17 in `presets/youtube/abundance-wisdom/LESSONS.md`):
1. **Easy ease everywhere:** `hf-graphics/tools/ease-pass.py` (gsap default + soft()/camera() on sine.inOut). DONE (source).
2. **c14 zoom slowed** (2.5 % across the whole held comp; c12 the same). DONE (source).
3. **Builds finish before the cut:** measured settle per comp; HOLD dict in `make-comps.py` (+ `tools/hold-pass.py`),
   g01/c09/c11/c28/c34 land earlier. DONE (source).
4. **Subtitles on third-party speech:** `hf-graphics/subs.py` (+ `transcript/map-inserts.py` → `inserts-tl.json`),
   c16a c16b c18 c23 c37 c46 c47 c49 c52; cue log `hf-graphics/subs.json`. DONE (source).
5. **Cricket SFX replaced:** `audio/sfx/cue-pass-v4.py` → `sfx-plan-v4.json` (plan-v4.py keeps unchanged rows verbatim;
   `remove-stale.py` took the exact 10 old clips off). **PLACED + VERIFIED (99 rows) + SAVED.**
6. **c27 arrow:** walk freezes on Nick, dim + arrow + HANDSHAKE IGNORED, resumes on "but" (`chapters2.py`, `hs_a/hs_b/
   hs_frz` from 01 rip 497.8-499.2). DONE (source) + 3 new SFX placed.
7. **Face drift:** `host-zoom.py` keyed 90 C1330 clips (38 runs) BY NAME. **APPLIED + VERIFIED + SAVED.**
8. **1-frame flash:** `-bf 0` in `gfx/render.sh` (+ the preset reference). Every comp re-renders as a new version.
Also: **bleeps 5a/5g** (`bleep.py`: Level mute keys on the A1 clips at the measured word edges + 1 kHz tones on A5,
`audio/bleep/bleep-plan.json`) **PLACED + VERIFIED + SAVED.**
**Another Claude session shares this Premiere (Sequence 39 active, `ACTIVE-WINDOW.lock`):** everything here is applied BY
NAME (`--sequence "Sequence 36"` on place-sfx / place-graphics; host-zoom, bleep, backup-seq, dump-seq, preview all by
name). Never switch the active sequence. Backup before this pass: `premiere-backup/Sequence36-before-v4-fixes.xml`.
**All 56 comps re-rendered** (`-bf 0`, B-frames 0 on every file, frames >= slot) **and PLACED by name on V3: ALL PLACED 56/56, saved.** Snapshot `seq36-v4.json`. Review: `review/same-night-full-v4.mp4` (`review/build-full.sh v4`, replays the face drift). Still open from before: Content-ID ducking of arena music in the inserts; the creator's calls (THE FALLOUT, the cheer timing, Martin's 2025 freeze footage, "Nick Walker!" in the crown subtitle is from the script since the ASR heard only "Nick").

### Earlier: WHOLE VIDEO BUILT + PLACED (2026-10-08)
**Every V2 block (76/76) and every slate (7/7) is covered on V3** (56 comps: cold open g01–g08 + t01, then c09–c54),
**96 premium SFX on A3/A4/A5** (`audio/sfx/sfx-plan-v3.json`), music re-levelled under the voice for the whole sequence.
All verified by readback and saved. Snapshot `seq36-full-v1.json`; backup `premiere-backup/Sequence36-before-chapters.xml`.
Review render: `review/same-night-full-full-v1.mp4` (`review/build-full.sh`: picture in 60 s chunks + one mix pass).
- Comps: `hf-graphics/make-comps.py` (cold open) + `chapters.py` (Ch1–Ch2) + `chapters2.py` (Ch3–Ch5, no web stills)
  + `chapters3.py` (web-still beats). Footage cuts: `hf-graphics/cut-span.py` (v1 spans frame-locked to A1; src ranges).
  Maps: `hf-graphics/tools/maps.mjs` → `maps.json`. Words on the timeline: `transcript/map-words.py` → `words-tl.json`.
- Web stills + facts (verified, 5 quotes confirmed): `assets/web/` (`SOURCES.md`, `facts.json`). Cutouts via Higgsfield.
- **Flags for the creator:** (1) Title 2 reads THE FALLOUT (proposed, never confirmed); (2) the cheer callback in 3c sits
  at 290.7 s by eye (ASR hears nothing there); (3) Martin's freeze intro uses his 2025 Olympia footage (tagged so) since
  he can't be identified in the 2020 posedown; (4) 3a has no freeze circle (the pass isn't in one identifiable frame);
  (5) the voice is ~-29 LUFS: export with loudness normalisation.

### Earlier: COLD OPEN v2 PLACED (2026-10-08)
The creator rejected v1 (too loud, too fast, wrong pro card, wrong title: `presets/youtube/abundance-wisdom/LESSONS.md`).
**v2 is on Sequence 36, verified + saved:** comps rewritten slow (`hf-graphics/make-comps.py`; v1 kept as
`make-comps-v1.py`), the built graphics stepped at 20 fps (`gfx/render-v2.sh`, comps.json `step`, catalog FX-81, his ask),
real footage smooth; pro card regenerated upright under a top light (`assets/gen/procard_upright*`), the title rebuilt as
FX-12 (tumbling medal/trophy/plate/dumbbell cut-outs, Montserrat gold title assembling from blur). V3 = g01-c, g02-b,
g03-b, g04-b, g05-c, g06-b, g07-b, g08-b, t01-b. **Music re-levelled for the WHOLE sequence** (`level-music.py`, plan
`brief/music-levels.json`): bed 12 LU (Rise) / 14 LU under the voice (-28.5 LUFS), swells only in voice gaps. **SFX v2:**
15 cues on A3/A4 (`audio/sfx/make-cues.py` → `placed-v2/`, plan `sfx-plan-cold-v2.json`), ~7-12 dB under the voice peak;
v1's 24 removed. A5 is an empty track I added for v1. Backups: `premiere-backup/Sequence36-before-music-level.xml`,
`Sequence36-before-v2.xml`. Review: `review/cold-open-preview-v2-review.mp4` (`preview.py` now plays every clip's REAL
level; the review copy is raised +12.5 dB uniformly to -16 LUFS so it's audible, the balance untouched).
NOTE: the voice integrates at ~-29 LUFS, so an export without loudness normalisation will be quiet.

### Earlier: COLD OPEN v1 BUILT + PLACED + SFX'D (2026-10-08)
**Cold open (0:00–0:41.4) is on Sequence 36:** 9 full-screen graphics on V3 (g01–g08 + t01 = S01–S14 + TITLE1, the
creator's V2 untouched underneath), 24 Epidemic SFX on A3/A4/A5 (A5 added). Both verified by readback and saved.
Backups: `premiere-backup/Sequence36-before-gfx.xml`, `Sequence36-before-sfx.xml`. Snapshot `seq36-after-coldopen-sfx.json`.
Review copy: `review/cold-open-preview-v1.mp4` (`preview.py`: rebuilt from the snapshot, music at a flat −9 dB, not the master).
- **Build:** `hf-graphics/make-comps.py` (all comps, one shared head) → `gfx/render.sh <id> full` (60 fps, ~30 s each; g05
  `MBLUR=1 MBLUR_SS=4 MBLUR_SHUTTER=3`, 60 fps caps SS at 4) → `hf-graphics/make-placement.py` (frame-snapped rows, newest
  version wins) → `uv run lanes/premiere/place-graphics.py projects/nick-martin-same-night --apply|--verify`.
- **Stills:** `hf-graphics/prep-stills.py` (Martin's Arnold cutout from the Higgsfield 4K upscale + bg removal, mirrored,
  gold/steel/grey), `prep-cutouts.py` (feathered Nick variants). g04 = LF1 broll 17 (prejudging replay) 537.85 s, Martin walking
  out alone under his name, half speed, mci to 60 fps, grey (`gfx/assets/video/worst_night.mp4`).
- **SFX:** `audio/sfx/fetch.py` (Epidemic IDs) → `audio/sfx/make-cues.py` (one slice per cue, trim/fades/level baked, onset or
  peak synced to the visual event; levels from the creator's own Seq 24 mix: hits ≈ −8 dBFS over a voice peaking ≈ −14,
  whooshes 10 dB under) → `audio/sfx/sfx-plan-cold.json` → `lanes/premiere/place-sfx.py --plan … --apply|--verify`.
- **Next:** the creator's look check on the cold open → Ch1 (S15 on, storyboard beats 9+) with the same loop; the cheer
  callback at 3c; Title 2 words (proposed THE FALLOUT); web stills; Content-ID ducking.

### Earlier: INSERTS + MUSIC DONE, OVERLAYS NEXT (2026-10-08)
The creator answered: (1) keep their reads of posts/comments, swap their read of NSP's Giles lines for the original clip
2a; (2) the cheer is from a third-party YouTube video (LINK STILL NEEDED; marker on the timeline at 3c); (3) title 2 at
~4:43 confirmed; (4) Higgsfield approved; and **"you have to do ALL overlays"**, every V2 block, from the catalog + the
Tella direction.
- **Inserts DONE + verified + saved** (`place-inserts.py`, plan `brief/insert-plan.json` from `brief/make-insert-plan.py`):
  20 edits, 35 pieces, Sequence 36 now **10:39.17**. Every original clip (V1/V2/A1/A2) at its exact mapped position,
  every piece frame-exact, no picture gaps. Titles/cards are labelled placeholder slates (`slates/`, same length as the
  final graphics will have). Markers: 2 BLEEPs (5a, 5g) + "3c: cut Martin's cheer in here". Snapshot
  `seq36-after-inserts.json`. Backups: `premiere-backup/Sequence36-before-inserts.xml` + `ABW8-before-inserts.prproj`.
- **Music DONE + verified + saved** (`fit-music.py`): 14 pieces on A2; the music pauses under every third-party clip
  (0.25 s out / 0.4 s in), runs under titles/cards, keeps the creator's alignment at each section's first host line and
  their level curves (Triple Five −10 dB bed, Seven Days −7 dB, Quantifications 0 dB); Rise runs under TITLE1;
  Quantifications starts under TITLE2; the bookend + END card are unscored. Content-ID ducking of arena music in the
  inserted clips is NOT done yet (needs an audio pass).
- **Storyboard DONE (2026-10-08), the creator approved the inserts first:** `brief/storyboard.json` (from
  `brief/make-storyboard.py`), 55 beats covering all 76 V2 blocks + 7 slates + 11 inserted-clip treatments, one visual
  system (look, palette, type, motion, sound) and a 20-treatment kit K01–K20 rooted in catalog FX codes. Review page:
  https://claude.ai/artifact/Cm6QnMFSCHcydK1WCHAZFZ (`brief/storyboard-page.html`). Slot times: `brief/overlay-slots.json`.
  Waiting: the cheer link (S04, 3c); Title 2 words (proposed THE FALLOUT); web photos to fetch (young Martin, Weinberger,
  Wilkin, the defenders) and Martin to find in the 2020 footage.
- **Next:** on the creator's go, build the kit (K01–K20 as reusable HyperFrames/PIL templates in the long-form kit),
  fetch + enhance the stills, the Higgsfield generations (pro card, steel figure, silhouette), then render and place
  beat by beat with SFX.

## Earlier: DIRECTION RECEIVED (2026-10-08)
The creator RECORDED and cut the host: **ABW8 · Sequence 36** (6:28; V1 face cut, 82 overlay slots pushed to V2, A1
voice, A2 music). Their Tella direction is resolved slot by slot in `BRIEF.md` § "THE CREATOR'S TELLA DIRECTION"
(`transcript/seq36-slots.txt` = the line in every block; `seq36-before-tella.json` = the untouched timeline).
Nothing on the timeline changed yet. **Waiting on the creator:** (1) their own reads of scripted clips (2a, 3b, 3d,
Text Card 1): keep or replace with the originals; (2) the source of the Martin cheer clip; (3) the ~4:43 title screen;
(4) Higgsfield credit approval for the generated images and enhancements.
**Plan once answered:** export an FCP XML backup → insert the script clips between blocks (V1/V2/A1/A2 shifted
together) → intro title + chapter titles → overlay storyboard for S01–S82 from the catalog (shown before building) →
build the kit + overlays → SFX → music re-fit.

### Before the recording (2026-10-07)
The plan, constraints and premium treatment live in `BRIEF.md`.
**Sources, 2026-10-07: ALL 12 IN** (`broll/`, every one H.264). The first pass was blocked (HTTP 429 + "not a
bot"). A plain retry ~10 min later went through (no cookies, no client switching); 11 needed one more retry (a 403
on the video data). Fallback the creator offered if it blocks again: their Chrome (Claude in Chrome) + IDM. 05 is
720p (2020) and B2 is 1280x702; the rest are 1080p. 04 = the finals, hardlinked from long-form #1.
`broll/fetch.sh` is re-runnable and skips what's already there.
**Transcripts: DONE.** `transcribe-windows.py` (copied from LF1) → `transcript/windows/<id>.json`, 11 windows
(`transcript/windows.json`) covering every scripted clip. Every quote found near its script time; **four script
out-points cut the quote short (1c, 1d/5h, 4a, 5f)**, word-accurate outs in `transcript/clip-notes.md`.
**Lock condition 2 (Arnold, 3c), first look:** in the rip, 10:25–10:39 is the presenters (Ronnie + the medal
presenter); the cut to the line-up at ~10:39.5–10:45 shows Nick (glasses), Hadi (beard, medal), the man in the gold
trunks and the man in the red trunks, but **no bald, light-skinned man = Martin** (taken to be the man with the
4th-place medal at 9:26, 9:50 and 11:20, matching B3). 10:46–11:23 = Nick's medal, then Andrew Jacked's win
celebration. 9:15–9:55 = Hadi's 3rd-place medal (Martin beside him ~9:25). **Result: Martin's cheer is NOT on camera in
this rip.** WhisperX heard nothing after 10:13 (crowd/music), so the exact time of "runner-up, Nick Walker" isn't
measured. The creator's Short (Sequence 30, `martin-fitzwater-12th`) DOES show Martin waving/cheering, but in close-ups
that are not in this rip (a different camera, a blurred band on top: likely a social re-upload). **Ask the creator for
that clip's original source** (title/link/date for the evidence tag) and confirm it's the moment after Nick's name.
Sheets: `review/lock2-*`, `review/arnold-*`, `review/short-seq30-shots.jpg`.
**Lock 1 (2020 posedown):** NOT decided. Nick = the young man in the red trunks (e.g. 3:06–3:26,
`review/lock1-na2020-186-206.jpg`); I can't tell which of the others is the 23-year-old Martin. The creator to confirm
by eye, else the fallback (B3 + the card). B1 (the full prejudging replay, kRjLT-6qCkw) was NOT
fetched; B2 covers the same shot. Fetch B1 only if B2 fails.
**Next:** sources → lock conditions 1–2 by eye → stills S1–S6 → the kit (BRIEF § 3) → the recording.

| | |
|---|---|
| channel | Abundance Wisdom, face-led long-form (the template is `projects/nick-walker-never-mr-olympia/`) |
| format | long-form 16:9, about 11:00 |
| script | 🔒 FINAL 6 Oct 2026, `X:\Claude Projects\Abundance Wisdom\NICK-MARTIN-LONGFORM.md` |
| sources | `X:\Claude Projects\Abundance Wisdom\NICK-MARTIN-LONGFORM-SOURCES.md` → `broll/` |
