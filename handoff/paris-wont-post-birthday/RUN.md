# RUN — "Why Michael Jackson's Daughter Won't Post On His Birthday 💔" (Abundance Wisdom short)

## ▶ STATUS (2026-10-29): UPLOADED — v1 (`X:\Claude Projects\Exports\paris-wont-post-birthday.v1.mp4`) went out as built; job closed, session retired. Lessons: the AW LESSONS.md (2026-10-24 entries).

## (previous) STATUS (2026-10-24 ~12:10) — v1 EXPORTED, waiting on his review
**`X:\Claude Projects\Exports\paris-wont-post-birthday.v1.mp4`** (= `outputs/paris-wont-post-birthday.v1.mp4`): 31.50 s,
1890 f, 1080x1920 60 fps, AAC 48 kHz, **-13.8 LUFS, -2.9 dBTP measured on the mp4**. He approved the test frames
(`renders/ALL-SHOTS-test-v1.jpg`) and signed back in to Topaz; only prob-4 was re-run (`build/topaz_step3.py`, the step-2
iris file was clean end to end), then align -> assemble -> clean check of every shot (`renders/test5/`) -> finish render.
Re-finish after a note: `"$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" build/finish.py render renders/paris_picture.mov
captions/caps_capcut.mov outputs/<name>.mp4 --audio renders/paris_audio.wav`. Brief vs build (told him): 60 fps (brief 30),
captions under the lips (brief 62-68 %), fade out at the end (his video; brief: hard cut), no music (his video), export name/place
(brief: `Paris Birthday.mov` in E:\...\Final Renders; his rule: X:\Claude Projects\Exports only). Next: his review -> LESSONS.

## (previous) STATUS (2026-10-24 ~12:30) — TEST FRAMES SENT; BLOCKED ON TOPAZ SIGN-IN
- **Topaz went into WATERMARK mode** on the last run: prob-4 printed "Critical error refreshing token Could not establish
  connection" (topazlabs.com itself reachable): the app's login token expired; only he can sign in (open Topaz Video AI).
  The iris step of that run is clean; prob-4 output (`renders/paris_stab_chr2_iris3_prob4.mov`) + `paris_topaz_aligned.mov` +
  `paris_picture.mov` carry the "Topaz Labs" watermark: DO NOT USE. After he signs in: re-run the chain (Stage A is current,
  incl. the faint-line cache): `python ../aw-code-trial-parents/stageB/topaz_his.py renders/paris_stageA.mov renders paris`
  -> align_frames -> assemble -> stills (check: no watermark) -> full finish render -> Exports.
- Test frames sent to him: `renders/ALL-SHOTS-test-v1.jpg` (= test3: the last CLEAN Topaz run, current framing; the faint P6
  glitch line was fixed after it) + `renders/MJ93-topaz-vs-not.jpg`.

## (previous) STATUS (2026-10-24 ~10:45) — CODE BUILD RUNNING (his answers: both kid overlays OK, photo B, transitions OK)
- Engine = the MJ-siblings one, copied into `build/` and driven by `build/timeline.json` (written by `build/make_timeline.py`
  from his v2 edit): stage_a (head lock, overlays from `build/overlays/picks.json`), his Topaz chain on faces, align_frames,
  `assemble.py` (`build/assemble_plan.json`: overlays straight from Stage A), finish (his AE grade 'ae' + sharpen, zooms,
  transitions, letterbox, greyed Grammy overlay, FULL-SCREEN umbrella still (new `full` flag), lower thirds, captions, fade).
- A/V: IG +0.10 (his slip; measured +0.13 `build/av_offset.py`), JO -0.37 (measured on 7 shots + the 'my' lip closure,
  `brief/frames/jo_mouth_mydad.jpg`), MJ93 unchanged (not flagged by him). Jack held to the camera cut (28.2).
- Framing: IG 135 %, MJ93 185 %, JO 220 %; nose Y per setup so every lower lip sits at y1033-1069 (lip_check, zoom included),
  face push-ins pivot on the lip line (540, 1075). Movie overlay recentred on young Michael (scale 1.15).
- Done: `renders/paris_stageA.mov` (1890 f), `renders/paris_audio.wav` (-13.8 LUFS, fresh Epidemic SFX in `build/sfx/`).
  Captions DONE (Sonnet agent, `captions/NOTES.md`): `captions/caps_capcut.mov` 1890 f, 48 captions, 16 coloured, the
  brief's 9 red phrases, VERIFY PASS.
- Fixes found on the first test frames: (1) her IG video carries a thin bright GLITCH LINE (dashed, 2-8 px) on ~24 % of the
  used frames (109/450): `build/ig_line.py` detects it per frame (row brighter than both rows +-5 px over >35 % of the width)
  and repairs it by vertical interpolation inside Stage A (seq_render frames are H x W x 3 uint8!), before Topaz. (2) ~40 ms of
  Paris's 'like' before 'My' (26.27) muted in `build/a1_from_his.py` (my raw-cut in-point had floored a frame).
  (3) the line also comes FAINT (18-35 % of the width) in bursts next to strong ones: `python build/ig_line.py cache <ig>`
  -> `build/ig_lines.json` (strong tier + faint rows within 15 frames / 60 rows of a strong band; 225 frames; 14 sampled = all
  real), read by stage_a per source frame. (4) Paris's IG face raised 30 px (PI nose y930 -> 900): open-mouth lips reached
  y1078-1089 vs caption top 1093 on P1/P5. Measured after: lower lips y824-1056.
  MJ93 with vs without Topaz compared (`renders/test2/MJ93-topaz-vs-not.jpg`): the 'Restored' upload is already AI-smoothed,
  both read waxy; kept his chain (faces get Topaz), comparison offered to him.
  Running: Stage A re-render -> Topaz -> align -> assemble (`renders/paris_picture.mov`). Next: centres ->
  test frames of EVERY shot to him -> full render after his OK -> `X:\Claude Projects\Exports\`.

## (previous) STATUS (2026-10-24 ~10:30) — DIRECTION VIDEO RESOLVED → BRIEF.md (top); 3 questions out to him
- His Tella direction video is resolved in BRIEF.md "DIRECTION VIDEO" (the table = the build plan). His cut = his edit of
  v2 in ABW10 (31.50 s), dumped `seqref/seq_his_v2.tsv`. Asked him: minors in two overlays, which best-friend photo, two
  unclear transitions. Code build starts on his answers (test frames of every shot first).

## (previous) STATUS (2026-10-24 ~10:00) — v2 RAW SEQUENCE PLACED (63.23 s), waiting on his review
- Final check (`seqref/a1_v2_check.txt`): every beat reads as brief v2 (with his v1 trims), "fifty" restored (an in at 73.00
  had dropped it; 'fifty' = 72.88–73.08, 71.14–71.40 is crowd noise). Gaps ≤ 0.34 s by ASR edges, the 0.42 s after
  "cartoons" is his own extended tail. Runtime measured on the timeline at 30 fps: **63.23 s**.
- Options given to him for 48–55 s: drop 4b (→ ~50.4 s) or 1b (→ ~52.6 s), or keep 63 s.
- His brief v2 (`brief/edit-brief-v2.md`): adds 1b (social media = love), extends beat 3 (…struggle and pain… I cannot recreate
  that part of my life), adds 4b (Paris on stage that same night). It was written believing v1 ran 16 s (the TC display bug);
  v1 really ran 32.23 s, so v2 lands at **63.47 s vs the brief's 48–55** — reported, nothing dropped on my own. 5b not used.
- **ABW10 → "Paris Birthday - raw cut v2"** (bin "Paris Birthday", 30 fps, display 104), 34 clips V1/A1, 7 markers, no V2
  (he deleted v1's photo slots), left ACTIVE for his review (his v1 "Paris Birthday - raw cut" untouched at 32.23 s). Not saved.
- Built by `build/plan_v2.py` → `v2/placement.json` → `premiere/place_v2.jsx`: HIS 18 v1 clips copied from his read-back
  (`premiere/readback.now.tsv`) and verified identical (in-point + duration); new pieces measured (`build/edge_rms2.py` +
  per-beat A1 re-ASR `build/rebuild_a1.py premiere/readback_v2.tsv seqref/a1_v2.wav`).
- 4b source = HER Instagram video's stage part (60.4–88.0 s, one continuous vertical phone shot from the crowd): no AH
  package / lock-5 fallback needed. Beat-4 photo still open (lock 1).
- Premiere in-point rule found: an in-point is FLOORED (source grid, then sequence grid) and on a 59.94/25 fps source a value
  ON the sequence grid can still drop a frame: pass the first source frame at/after it (+ one more frame for 514.9667
  empirically) and VERIFY against the read-back. Re-place v2: `python build/plan_v2.py` → place_sequence.py `v2` →
  `premiere/clear_v2.js` → `premiere/place_v2.jsx` → `premiere/readback_v2.js`.

## (previous) STATUS (2026-10-24 ~08:00) — HE IS EDITING the raw sequence; his timeline = source of truth
- His "the runtime is just 16 seconds": NOT missing material. The clone kept the template's 60 fps TIMECODE display (108)
  after `setSettings` moved the timebase to 30 fps, so Premiere counted 970 frames as 60 fps timecode (16.17 s). Fixed with
  `premiere/fix_display.js` (display 104 = 30 fps TC, clips untouched). Same cause as the silent QE razor failure.
- **His edits seen 2026-10-24 (`premiere/readback.now.tsv` vs `readback.placed.tsv`) — decisions, never overwrite; do NOT re-run
  `clear_ours.js` / `place.jsx` again:** B3 "There was no Christmas" in 510.87→511.00; "there was no birthdays" in 512.53→512.90
  (drops the second "There was" → "…no Christmas, no birthdays"); "It was not" in 514.83→514.97; Michael's answer out
  54.45→54.93 (longer tail after "cartoons"); BOTH V2 photo slots deleted. Runtime now 32.23 s.

## (previous) STATUS (2026-10-24 ~07:30) — RAW SEQUENCE PLACED, waiting on his approval + 6 decisions
- **ABW10 → "Paris Birthday - raw cut"** (bin "Paris Birthday", 1080×1920 **30 fps**, cloned from "Onyx reaction template
  (empty)"). 19 clips V1/A1, 2 photo slots V2, A2 empty, 5 beat markers (words + notes). **32.33 s.** NOT saved (he saves).
  ABW10 is open from the nested Auto-Save path (`E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj`).
  His active sequence restored by ID: "Sequence 22" (`02b67784-…`).
- Verified: read-back (`premiere/readback.tsv`) → A1 rebuilt (`seqref/a1.wav`) → re-ASR = the brief's words; inter-word gaps
  ≤ 0.28 s by ASR edges, except "business. → That" 0.32 s (her "-ness" sibilant runs to the cut, RMS-measured).
- **Decisions asked of him (no code build before his OK):**
  1. f-word: CUT (default, "people lose their minds") vs keep + `F*CKING` caption (channel style).
  2. B1 start on "I don't post" (default; co-articulated with "where", re-ASR clean) vs "There have been times where…" (lock 4).
  3. Lock 2 word: ASR hears "probably BE SAFE with my children" (2 passes); ABC's own on-screen quote card says "have a
     little cake" — his ear.
  4. Beat-4 photo: placeholder = the GMA package's own photo of Michael alone (lock 1), but 320×240 at 800 % — needs an HQ
     adult 2008 photo (he supplies / I find the original / Higgsfield enhance = credits, ask first).
  5. Beat 5: the podcast camera is on JACK for "My relationship is the most" (1.7 s, left on Jack) and for "That was my
     best friend" (V2 photo slot, placeholder). Options: Jack (real feed) / Michael photo / Paris picture-only (lips off).
  6. Runtime 32.3 s vs the brief's ≈42 (QA 40–45): exact words + no gap > 0.25 s. Not padded.
- Next on his OK: the code build per the MJ-siblings pipeline (head lock, Topaz on faces, his AE grade + sharpening,
  zooms/transitions, lower thirds + card, captions under the lips, SFX + piano bed, −14 LUFS) → test frames of EVERY shot first.

## Sources (searched E:, X:, C:\Users\affan on 2026-10-24; copied to `raw/`, transcript `transcript/words.json`)
| Beat | File in `raw/` | From | Used (source time) |
|---|---|---|---|
| 1 | `paris-ig-birthday-2023.mp4` (1080×1920 30) | `E:\Bullshit Folder\Henry\Paris Jackson about her father's birthday.mp4` = HER ORIGINAL IG video (replaces the AH package) | 42.40–44.38 · 44.80–45.575 · 45.855–47.16 (f-word 45.575–45.855 cut) |
| 2 | same | same | 5.92–7.97 · 8.267–12.36 · 12.55–14.42 · 14.55–16.07 |
| 3 | `mj93-grammy-legend-restored.mp4` (1440×1080 59.94) | `…\Henry\1993 'Grammy LEGEND' Award - Restored.mp4` (brief's BACKUP) | 507.80–510.72 · 510.88–512.13 · 512.567–513.88 · 514.867–516.47 |
| 4 | `mj08-50th-birthday-gma.mp4` (320×240 25) | `…\Henry\Michael-Jackson-50th-SnapYT.App.mp4` (his download 2026-10-24) | 46.85–49.18 (question) · 50.433–54.45 (answer, one piece); V2 photo 54.90–61.23 |
| 5 | `jo-paris-trying-not-to-die-2026.mp4` (1920×1080 30) | `…\Henry\Paris Jackson On Grief, Music _ Growing Up In The Spotlight.mp4` (his download) | 3032.86–3033.80 · 3034.30–3035.033 │ 3035.033–3035.82 (camera cut) · 3036.40–3036.86 · 3040.40–3041.767 · 3056.67–3057.70 (+ V2 photo) |
Premiere floors in-points (some land one frame earlier); exact placed values in `premiere/readback.tsv`.

## How to re-place (after any change to `build/plan.py`)
`uv run build/plan.py` → `python ../../presets/youtube-shorts/abundance-wisdom/place_sequence.py . "Paris Birthday - raw cut" "Paris Birthday" premiere/place.jsx`
→ `python build/pp.py premiere/clear_ours.js` → `python build/pp.py premiere/place.jsx` → `python build/pp.py premiere/restore_active.js`
→ `python build/pp.py premiere/readback.js > premiere/readback.tsv` → `<whisperx-venv python> build/rebuild_a1.py` (words + gaps).

## Found the hard way (2026-10-24) — candidates for LESSONS / lab-notes
- **QE razor silently did nothing** on a cloned template whose frame rate was changed 60 → 30 by `setSettings` (no error, no
  cut). Fix used: camera cut = two butt-joined clips split ON the source frame grid. (lab-notes candidate: `lanes/premiere`.)
- **Premiere FLOORS in-points**: `3035.0333` (4-decimal rounding of frame 91051) became 3035.0000 → one frame of the wrong
  shot + 33 ms audio repeat. Pass in-points a hair PAST the frame time (+1e-4).
- **A "pause" on a phone line can be a quiet word**: the A1 re-ASR reported 0.66 s after "I'll"; cutting it deleted
  "probably" (51.12–51.44). Trust the snippet re-ASR over a whole-file pass on phone audio; re-ASR after every cut.
- **Whole-file WhisperX VAD drops quiet phone speech** (Michael's answer vanished from one pass): re-ASR the window alone.
- **A word-timed snippet caught "best friend, SO."** (the first ASR had merged "so" into "friend"): hard cuts get a
  word-timed snippet that runs PAST the out-point.
- The podcast's program camera cuts to the HOST while the guest speaks: check speaker-on-camera for every kept word.

## Rules for this job
- Change only what he names; test frames of every shot before any full render; his AE grade + sharpening untouched.
- Every rawvideo pipe tagged BT.709; one-pass assembly; overlays skip Topaz; Topaz only on faces.
- No minors on frame (beat 4 included). Mute every anchor/reporter (MJ08: only the one question + Michael).
- Silence (no playback). Never save/export his Premiere projects; restore his active sequence. Exports → `X:\Claude Projects\Exports\` only.
- Shared checkout with another AW short session: touch only this folder (+ AW LESSONS appends). Commit nothing unless asked.
