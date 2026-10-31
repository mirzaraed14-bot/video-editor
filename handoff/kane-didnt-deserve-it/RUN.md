# RUN: "Why They Said Harry Kane Didn't Deserve The Ballon d'Or 😳" (Abundance Wisdom short, football)

## ▶ STATUS: resume here (2026-10-30): v3 DELIVERED (O6 = the kids, letterboxed), waiting on his review
- His answer 2026-10-30: **"Yes, that's her"**: the O7 stalls woman (BAYERN 650.6) IS his wife. No open questions left;
  the only pending call is his own review (incl. whether O6 should have Topaz Iris: REPORT § 6).
- **Delivered file now = v3** (MD5 56c55b4d…, 1246 f, 41.55 s, 48.0 Mb/s, −13.8 LUFS, −3.1 dBTP, QA PASS, 24 cuts clean
  `proof/final_edges.jpg`, O6 edges `proof/final_o6_edges.jpg`) in Final Renders + Exports; v2 kept as `(v2)` in both
  (MD5 dfa9da57…), v1 as `(v1)`. Only O6 changed: v2 vs v3 60 fps masters differ < 1/255 outside frames 2008-2170 (re-encode
  noise), audio bit-identical (`renders/kane_audio.wav` reused).
- His 23:15 "done" (file `raw/new/KIDS_Kane_son_AllianzArena.mp4`, 1080p30 1.6 Mb/s fan phone) + "if its low quality do
  letterbox format on it". Build: `make_timeline.py` v3 (O6 overlay without 'full', band [290, 1334] = his 440-1484 lifted
  150 px, twin 2.2 blur 18, zoom pivot [540, 812], sat_level O6 0.62; pick KIDS 9.20 0.9x scale 1.0 centre [870, 690]) →
  `stage_a.py render renders/kids_fix.mov 2008:2170` → **no Topaz** (Iris drew a dark band over the boy's 40 px face:
  `proof/kids_face_topaz_vs_raw.png`) → `splice_ranges.py` v3 picture + kids_fix → `renders/kane_picture_v4.mov` →
  `finish.py render` → `outputs/kane_v4_60.mp4` → `export.py`. Measured: son's chin ≥ ~60 px above the caption line; top
  glow bar y203 (first frame) → y288; chroma 0.37-0.45 (other shots 0.15-0.43). Sheets `proof/kids_finish_v3.jpg`,
  `proof/kids_caption_clearance.jpg` (that one is pre-saturation-fix).
- Previous data kept: `build/timeline.v2.json`, `overlays/picks.v2.json`, `centers.v2.json`, `zoom_layers.v2.json`.

## (previous) STATUS (2026-10-29 ~23:15 PST): HIS ANSWER "Use the kids" → O6 swap, WAITING ON HIS DOWNLOAD
- His words (2026-10-29 ~23:00): **"Use the kids"**: brief hard rule 5 (no Kane children) is LIFTED for O6 only
  (33.47-36.17, "time that I'd love to be spending with my kids, with my family"); his Tella ask = Kane with his kids,
  playing, having a good time. Every other overlay stays as delivered (fix only what he named).
- No kids footage anywhere local: TROPHY (Sky 2025) has only mascot children (25-29 s), BAYERN ceremony / SKY / PACK have
  none; drives searched (`E:\Bullshit Folder\Henry\` = the job's own files). Dailymotion: 5 candidates pulled into
  `review/kids_dl/` (sheets there), none with his kids.
- Asked him to download (YouTube is blocked for me, never bypassed): **https://www.youtube.com/watch?v=WSBoUJE9kjw**
  ("Bayern Star Harry Kane kickt mit Sohn in der Allianz Arena": Kane kicking a ball with his son Louis on the pitch
  after the 2026 title v Stuttgart); alt https://www.youtube.com/watch?v=Gsj5-l9ZdKE (FC Bayern "Kane Hat-trick at the
  Title Party", 2026 title party, family photo on the pitch).
- NEXT on the file: probe → contact sheet → pick ~2.7 s of play (0.9x if 25/30 fps, native slow-mo if 50/60) →
  `build/make_timeline.py` O6 pick (keep his zoom out + the purple in / cyan out transitions) → `stage_a.py render` frames
  2008:2170 (60 fps timeline, 33.467-36.167 s, same convention as O1 = 353:434) → Topaz only if the source is SD →
  `splice_ranges.py` → `finish.py render` → `export.py` → `win/final_edges.py` → deliver, keep v2 as `(v2)`.

## (previous) STATUS (2026-10-29 ~19:30 PST): DELIVERED (v2 replaces v1), waiting on his review + 2 answers
- **Delivered file now = v2** (MD5 dfa9da57…, 48.2 Mb/s, −13.8 LUFS, −3.1 dBTP, QA PASS, 24 cuts clean) from
  `outputs/kane_v3_60.mp4`: picture `renders/kane_picture_v3.mov` = v2 picture + the uncle (frames 117-353) re-framed
  (scale 2.0, nose y600, zoom 0.97 on the caption line, 160 px mirror-filled lift: `make_timeline.py` v2c,
  `stage_a.py` expose_bottom) through `workflows/topaz-iris.py --no-stab` (the stabiliser smeared his handheld face),
  spliced (`renders/unc_ranges.json`); audio: no swish on B6 (DRY). The first delivery is kept as `(v1)` in both folders
  (MD5 ee2b00c2…). Lip sync on the final render: `proof/lip_final_others.png` (Kane, Brazil, host OK; uncle's lips hidden).
  Mixed-audio per-piece re-ASR: no cut-filler fragment at any handle (`win/asr_mix_pieces.py`).

## (previous) STATUS (2026-10-29 ~19:15 PST): v1 DELIVERED
- **`Final Renders\Kane Didnt Deserve It.mov`** + identical `X:\Claude Projects\Exports\Kane Didnt Deserve It.mov` (= `outputs/`,
  MD5 ee2b00c2…): 1080x1920 30 fps, 1246 f, 41.55 s, 46.6 Mb/s, −13.8 LUFS, −3.1 dBTP, export QA PASS. From
  `outputs/kane_v2_60.mp4` (picture `renders/kane_picture_v2.mov` = Topaz picture + O1 re-rendered from 75.25 via
  `build/splice_ranges.py`, `renders/o1_ranges.json`). The never-delivered first export (1 stray wide frame at O1) is
  `outputs/Kane Didnt Deserve It (v0 stray frame).mov`. Report: `REPORT.md` (brief § 9 + what differs and why).
- Open with him: kids overlay vs rule 5 (default kept: O6 = family in the stalls); is the stalls woman his wife; O4 = an
  England 2026 goal (the Darmstadt goal is only a 720p wide shot here).
- A note → change ONLY what he names (memory: data + ONE finish render): `build/make_timeline.py` → (overlay pick change:
  `stage_a.py render <seg> a:b` + `splice_ranges.py`; face/framing change: Stage A + Topaz + align_frames) → `finish.py render`
  → `export.py` → `win/final_edges.py` → copy to both folders (keep the reviewed file as `(v1)`).

## (previous) STATUS (2026-10-29 ~18:35 PST): CODE BUILD RUNNING (he said "start", then "handle everything yourself")
- His 18:15 messages: "start" + "I'm going for two three hours so handle everything yourself like all the downloads". Defaults
  taken (stated to him): brief rule 5 KEPT (no children; O6 = his family in the stalls, BAYERN 641.5), O7 = the 10:50
  smile (identity for him to confirm), O4 goal = a 1440p60 England 2026 goal (the Darmstadt halfway-line goal only exists
  here as a 720p wide shot from Dailymotion `raw/new/GOAL_dm_x8p6v48.mp4` ~64-66 s: unusable full-screen vertical).
- Downloads: YouTube geo-blocks (9jqtkyvYJJk, b_TmJoQvwvc) and the bot check (rest) → not bypassed. His SnapDownloader
  files: 4K pack (1440p60 VP9) → `raw/new/PACK_Kane_England2026_1440p60.mkv`; Sky Sports Bundesliga 2025 trophy →
  `raw/new/TROPHY_Bundesliga2025_SkySports.mp4` (ASCII copies of `E:\Bullshit Folder\Henry\…`).
- Catalog pass: BRIEF.md § Catalog pass. Picks: `build/make_timeline.py` (picks + timeline + centers.json), sheets
  `review/src/*.jpg`, framing `proof/stageA_sheet2.jpg`.
- DONE: `build/a1_his.py` → `seqref/his_a1_xf.wav` (2-frame equal-power crossfades, 22 cuts); `stage_a.py track`
  (17 face shots, 0 misses) → `renders/kane_stageA.mov` (2493 f); ASH lip sync on the render within ~1 frame
  (`proof/lip_ash_*_render.png`, picture slipped 0.18 s); captions (`captions/cap_words.py` force-aligned words,
  `captions.txt` colour MIX, `big:` = B2 English 1.35x two lines, `render_caps.py` local `_draw_big`, shared engine
  untouched) → `captions/caps_code.mov`; audio `build/audio.py` → `renders/kane_audio.wav` (−13.8 LUFS pre-encode, fresh
  Epidemic swishes `build/sfx/SOURCES.md` 21 dB under, cyan silent, no music; speaker gain handed over as a 20 ms curve,
  not Janet's ramp-to-zero); finish.py: `temperature` keys (cold −1 → warm +1 on B6 frame 1) + single-line cards;
  zoom layers built.
- DONE 18:45: Topaz (`../aw-code-trial-parents/stageB/topaz_his.py`, 15 min, no watermark: `review/frames/topaz_check.jpg`,
  before/after `proof/topaz_vs_stageA_31s.jpg`) → `align_frames.py` (2495 → 2493: dropped 1525/2493/2494, held 1538) →
  `renders/kane_picture.mov`; `capcut_pass.py` → `captions/caps_capcut.mov` (2493 f); test stills `proof/test_v1*.jpg`
  (captions measured at y1040-1090; the '·' card bug was finish.py reading timeline.json as cp1252: fixed, utf-8).
- RUNNING (~18:55): full finish → `outputs/kane_v1_60.mp4`.
- NEXT: check the Topaz output for a WATERMARK (lapsed login) → `build/align_frames.py renders/kane_stab_chr2_iris3_prob4.mov
  renders/kane_stageA.mov renders/kane_picture.mov` → `captions/capcut_pass.py caps_code.mov caps_capcut.mov` (GPU venv) →
  `build/finish.py stills` on every shot → `finish.py render ../renders/kane_picture.mov ../captions/caps_capcut.mov
  ../outputs/kane_v1_60.mp4 --audio ../renders/kane_audio.wav` → `build/export.py outputs/kane_v1_60.mp4 renders/kane_audio.wav
  "outputs/Kane Didnt Deserve It.mov"` → edges check → copy to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\`
  + `X:\Claude Projects\Exports\` → § 9 report.

## (previous) ▶ STATUS: resume here (2026-10-29 ~17:30 PST): HIS RE-CUT + TELLA DIRECTION IN, waiting on footage + 2 answers
- He re-cut "Kane Didnt Deserve It - raw cut" himself (41.55 s, saved) and recorded a Tella walkthrough. Both are resolved
  in BRIEF.md § HIS DIRECTION (overlay slots, zoom groups, 17 colour-coded transitions, lip sync, captions). His sequence
  was only READ (`premiere/readback_all.js`, one call, title checked for autosave first) → `premiere/his_v1.tsv`,
  `his_v1_edl.md`; his words re-ASR'd from the rebuilt A1 (`win/verify_his.py`).
- Measured: **ASH picture leads its audio by ~0.16-0.20 s** (three bilabials, BRIEF § 1); **BAYERN lectern (B8) in sync**
  (m of "my", 646.6). O4 zoom settled = out (MFCC-DTW vs his own takes). Other talkers not yet checked
  (my first ROIs missed the mouths: BRAZ Alan's mouth ≈ (954, 465), SKY presser ≈ (945, 285) in source px).
- Waiting on him: kids overlay vs hard rule 5; wife confirm (`proof/wife_candidates.jpg`); downloads for O1 kick, O4 goal,
  O5 trophy (links in BRIEF § round 3). 18:10: the 4K kick pack is in `E:\Bullshit Folder\Henry\` (.mkv); the goal and
  DFB-Pokal links are geo-blocked for him, replacements in BRIEF § round 3.
- NEXT (on his files): probe them (res/fps; 2160p for O1 full-bleed) → pick the moments (frame check for children) → code
  build from `projects/janet-couldnt-cry/build/` driven by `his_v1_edl.md`: catalog pass in BRIEF.md first (CLAUDE.md
  learning loop) → ASH picture slipped ~0.17 s + plosive check on every talker → Stage A framing (uncle head lock; his V1
  positions as the start point) → Topaz (SD sources; interpolation for O4/O5 slow motion) → zoom groups → his 17
  transitions (`transition_pass` kinds) → grade (cold B1-5, warm from B6) → labels → captions (gradient MIX, y≈1060, B2
  English two lines) → audio −14 LUFS / ≤ −1 dBTP, no music → export both paths.

## (previous) ▶ STATUS: resume here (2026-10-29 ~14:55 PST): RAW SEQUENCE PLACED in ABW10, waiting on his pass + direction
- **ABW10 › bin "Kane Didnt Deserve It" › "Kane Didnt Deserve It - raw cut"** (clone of "Onyx reaction template (empty)",
  1080x1920 60 fps): V1/A1 26 clips, V2 4 picture-only covers (A2 empty), 8 beat markers (name + card + warning).
  **48.70 s**. His active Sequence 34 restored. **Not saved** (he saves). In/out table: `premiere/inout_table.md`.
- Verified (`win/verify.py`): in-points within 13 ms of plan; B8 picture sync +23 / −27 ms; A1 rebuilt
  (`seqref/a1.wav`) and re-ASR'd per beat + per piece: every beat reads the brief's words (B8 "So here it is, we
  done it": Whisper writes "we've", the CTC fit says "we done"). Remaining quiet flags: B6 "Get stuffed. [0.21-0.29]
  Harry won it" (kept, his ear); B7 "games [and] trophies" (weak "and", real silence ~0.06 s after the cut); B7
  "saunas" (sibilant, not silence); **B2 the uncle**: the bar noise hides his pauses (voice-band strips inconclusive,
  `win/strip_bp.py`) → his ear.
- Round 2 on placement (v1 → v2, readback.v1.tsv / placement.v1.json kept): pauses cut at B3 (wow|I), B4 (London and|a,
  breath 542.30-542.65), B7 (games|and 55.64-55.78; and|my wife 80.27-80.55), each join re-ASR'd first (`win/join_test.py`).
- 14:15 incident: Premiere froze ~15 min ("Auto Saving Project: ABW10", then "Not Responding" at ~0 % CPU) while my
  `create_seq.js` call was pending; it recovered on its own (14:31), the clone had been made, nothing else ran. Since
  then every bridge call checks the window title for "Auto Saving" first.
- NEXT (his move): his pass on the raw cut (re-edit freely: his timeline becomes the source of truth) + his direction
  (Tella or text). Open with him: Yamal face timestamp (B2), a Guti photo (B4), the uncle's pauses (B2).
- Then the code build (copy `projects/janet-couldnt-cry/build/`): dump HIS sequence read-only → catalog pass in
  BRIEF.md (CLAUDE.md learning loop) → Stage A framing/head lock → Topaz → grade (B1-5 cold/desat, B6-8 warm, switch on
  B6 frame 1) → labels/cards (top third, ~2 s, first appearance) → captions at y≈1060 (his height; B2 English only, bigger,
  two lines; red words per beat; "Harry's the top man", "We done it") → audio −14 LUFS / ≤ −1 dBTP, uncle light NR,
  2-4 frame crossfades, NO music → B6 1-frame J-cut → export `Final Renders\Kane Didnt Deserve It.mov` + `X:\Claude Projects\Exports\`.
  Burned-in chyrons (ASH "DOES HARRY KANE DESERVE…", BRAZ "YAMAL'S UNCLE AIMS SWIPE…") sit in the frame's bottom band.

## (previous) ▶ STATUS: resume here (2026-10-29 ~14:20 PST): BEATS LOCKED, PLACING IN ABW10 (Premiere was auto-saving)
- His OK (~13:50): all five defaults + B8 short version on FC Bayern's synced picture (BRIEF.md).
- Edges locked: `premiere/make_beats.py` (every in/out measured, 25 fps grid; strips `win/snip_asr.py`, `win/runs.py`,
  wav2vec2 `win/force_align.py` → `win/fa/`). `edl.json` 49.33 s, 23 pieces + 4 V2 covers (B4 shocked face BAYERN 8.2,
  B7 Ronaldo handover BAYERN 52.4, B8 x2 BAYERN synced); cover `to_src` nulled (Derek lesson). `framing.json` pins 5
  crops (Sky B-roll, shocked face, handover, uncle split at 21.20); sheet `proof/crop_sheet_v2.jpg`.
- 14:15: `create_seq.js` timed out (45 s): Premiere's title read "Auto Saving Project: ABW10.prproj"; the chained
  place / restore / readback calls then hit "bridge unavailable" (not executed). NEXT: when the autosave ends, run
  `premiere/state.js` → if "Kane Didnt Deserve It - raw cut" exists and is empty, run `place.jsx`; if it doesn't exist,
  `create_seq.js` first; then `restore_active.js` (his Sequence 34, 3574bc31…) → `readback.js > premiere/readback.tsv`.
  One call at a time, check each result.

## (previous) STATUS (2026-10-29 ~14:30 PST): CHECKS DONE, 5 questions with Affan (BRIEF.md § round 2)
- Cuts (scdet): ASH 65.32/66.36 · BRAZ 536.72, **554.32 (to Brazil; "Get" onset 554.30 → 1-frame J-cut)** · SKY 50.20,
  57.00, 90.04 · BAYERN 7.92-12.56 (shocked face) · 51.52-57.80 (Ronaldo hands over the trophy) · 655.04-659.40 (Kane at
  the lectern under B8) · UNCLE, TS: none in the beat.
- Sources are 25 fps: Premiere snaps ins/outs to 40 ms, so leave >= 40 ms past every word edge.
- Next on his answers: sources.json + beats.json (premiere/make_beats.py, Janet pattern) → resolve_beats → plan_placement
  (crop sheet) → place_sequence into ABW10 (bin "Kane Didnt Deserve It", clone of the template) → readback + A1 re-ASR.

## (previous) STATUS (2026-10-29 ~14:00 PST): SOURCES IN, ASR + checks running (findings below)
- His 8 SnapDownloader files (`E:\Bullshit Folder\Henry\`, 13:18-13:23) copied to `raw/` under the brief's names
  (`raw_map.tsv`); the yt-dlp 360p TS kept as `raw/TS_ytdlp_360p_fallback.mp4`. All 8 = H.264 1920x1080
  progressive, AAC 44.1 kHz; 25 fps except REACT (50).
- Whole-file ASR (GPU faster-whisper large-v3, `win/win_asr.py` → `win/asr/<stem>.json/.txt`).
- Findings so far (sheets in `proof/`):
  - **B1 hook: "Harry Kane('s) not a Ballon d'Or winner" (ASH 63.98-65.86) is NOT Ashton.** His lips close at ~64.7 while
    "not a Ballon d'Or winner" plays (`proof/ash_mouth_60.4-66.4.jpg`, 10 fps), the pitch jumps 112 → 140-173 Hz, and the
    director cuts to the other host at 65.3. It is the host echoing him as a question ("…not a Ballon d'Or winner?" →
    "No, because…"). Ashton's own line: "his numbers are staggering, **but he's not a Ballon d'Or winner, in my opinion**"
    (57.52-63.98). Rule 4 (Ashton only) → ask Affan.
  - B3 ASH 97.28-101.88 "there's nothing he does that I think, wow, I could not do that" ✓ (brief ~1:31: drift +6 s).
  - B2 UNCLE 18.48-22.70 "si te gusta el fútbol, tú vas a ver a Lamine, no vas a ver Harry Kane" ✓ (the interviewer
    names him "Abdul" at 0.4 s; uncle is the only voice in the beat).
  - B4 BRAZ 538.70-544.08 "it was suspicious that the ceremony was held in London and a London-born player won" ✓
    (the female host; preceded by "And Real Madrid's Guti has suggested").
  - **B6 BRAZ 554.24-561.28 = Alan Brazil, confirmed**: the same man (glasses, headphones, maroon jumper) answers "Alan,
    would you knight Harry Kane?" at 812-816 on camera; his lips move through the whole line (`proof/braz_mouth_*`).
    Words: "Harry's **the** top man" (brief: "a top man") → caption as said.
  - B5 TS 202.38-206.28 "Harry Kane, he gets a 1 out of 10, and he's lucky to get that" ✓ (Durham alone on camera, Euro
    2024 media room; the 1080p copy is sharp).
  - **B8: the AS SPEECH upload has NO real picture**: one stage shot looped for 9:38 with an audio-waveform graphic
    across Kane's body (`proof/speech_all.jpg`). BAYERN is the full broadcast of the same speech: BAYERN = SPEECH +
    106.66 s (xcorr r 0.92 at 5 points, `win/xcorr.py`). → picture from BAYERN, synced, under SPEECH's audio (ask).
  - BAYERN: Kane's hands-to-face at the announcement 8-12 s (beside his wife); Ronaldo Nazário hands him the trophy
    52-57 s (stage); audience cutaways during the speech.
  - REACT: a fan's phone video from the stalls, wide crowd (0-47 s), stage (48-82), photo wall (83-96). No clear
    close-up of any one face at the announcement; I can't pick out Yamal myself → Affan to point at him (or skip).
  - SKY: 0-18 studio, 18-330 Kane's podium presser with B-roll cutaways (arrival 48-58, shirt 90-92, training 126-132,
    match 156, 198, 276), 336+ studio analysis (presenters: their audio stays out).
  - **B7 words (SKY):** A = "people see the end product, they see me scoring goals, they see me on the pitch, they see me
    winning games and trophies, but [you know] it's very rare for people to see what goes on behind the scenes"
    50.90-60.78 (the brief's 0:50-0:57 is short of "behind the scenes" by ~4 s; the middle is not filler, kept);
    picture under 50.0-57.0 = Sky's own arrival B-roll (Kane + entourage + crowd, dark; adults only as far as visible,
    `proof/sky_broll_50-57.jpg`), podium from 57.0. B = "[and] all that sacrifice in saunas, in ice baths, time that
    [you know] I'd love to be spending with my kids, with my family and my wife, but it's all part of the dedication, if
    you want to be at a very top level you have to sacrifice some time and some things" ~73.4-88.16, podium throughout.
    Pauses to tighten: 72.94-73.41, 76.39-76.82, 86.41-86.91; fillers "you know" 56.62-57.72 and 77.72-78.14.
  - **B8 "We done it" is what he says**: CTC fit (wav2vec2, `win/ctc_compare.py`) prefers "here it is we done it" over
    "we've done it" by 3-4.5 loss units on SPEECH (2 windows) and on BAYERN's copy; Whisper normalised it to "we've".
    Words: "so [uh] here it is, we done it" SPEECH 549.04-551.10 ("uh" 549.30-549.84 trimmed). "To my wife Kate, my
    best friend" option = SPEECH 530.82-534.58 (pause 533.32-534.00).
  - BAYERN under B8 (SPEECH + 106.66): 655-658 Kane at the lectern; the broadcast cuts to a blonde woman in the stalls
    at 632-634, 641-644, 650-654, 659-662 (during the wife lines; her identity for him to confirm). Not under the short
    beat's ~2.3 s; in the Kate version 641-644 lands on "my best friend".
  - Runtime estimate (pauses > 0.25 s tightened, fillers out): B1 ~2.6 (Ashton's own line) · B2 ~3.6 · B3 ~4.3 · B4 ~5.0
    · B5 ~3.4 · B6 ~6.3 · B7 ~24-26 · B8 ~2.3 → **~52-54 s**; with the Kate opening ~56 s (both ≤ 60).

## (previous) STATUS (2026-10-29 12:45 PST): YOUTUBE BLOCKED, waiting on Affan to drop 7 sources in
- His answers (BRIEF.md § HIS ANSWERS): no music · run yt-dlp once, plain · captions at his height (y≈1060) · raw
  sequence in ABW10 first.
- Ran the brief's 8 yt-dlp commands once, plain (12:36): **7 of 8 refused** ("HTTP 429 Too Many Requests" then "Sign in to
  confirm you're not a bot"; no PO token). Not retried, no cookies / proxies (never bypass). Log: `download.log`.
- The one that came down, `raw/TS_Durham_1of10_2024.mp4`, is the **fallback format 18: 640x360 25 fps H.264, AAC 44.1 kHz,
  291.4 s**, not the best copy (the bot check hid the HD formats). Usable for beat 5's audio; picture is very soft at 9:16.
- Asked him to download with SnapDownloader into `E:\Bullshit Folder` (as on MJ Siblings), best quality: ASH, UNCLE, BRAZ,
  SKY, SPEECH, BAYERN, REACT, plus an HD copy of TS if YouTube has one.
- Next when the files land: copy to `raw/` under the brief's names → probe (resolution, fps, `idet`, audio) → window ASR
  per beat (CPU faster-whisper, `projects/janet-couldnt-cry/win/win_asr.py` pattern) → ins/outs locked by ear
  (`runs.py` + `snip_asr.py` pattern) → runtime sum (stop + ask if > 55 s after filler trims) → `premiere/make_beats.py`
  → `resolve_beats.py` → `plan_placement.py` (crop sheet) → `place_sequence.py` into ABW10 (bin "Kane Didnt Deserve It",
  clone of the 30 fps template, his active sequence restored, never saved) → readback + A1 re-ASR verify.

## Job facts
- Format: AW short, 1080×1920, 30 fps export, full bleed (no letterbox / blur), −14 LUFS / ≤ −1 dBTP, no music.
- Pipeline to copy: `projects/janet-couldnt-cry/` (sequencing: `premiere/`, `win/`; code build: `build/`) and
  `projects/joe-jackson-appointment/build/`.
- Export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Kane Didnt Deserve It.mov` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- Started by session local_3ae3a4cf (the parent); shared notes folder
  `C:\Users\affan\AppData\Roaming\Claude\side-session-notes\local_3ae3a4cf-7107-4cdf-a50e-e1b313072860\`.

## Sources
| Code | File in raw/ | State |
|---|---|---|
| TS | TS_Durham_1of10_2024.mp4 | 640x360 25p fallback (format 18), 291.4 s; HD copy asked for |
| ASH, UNCLE, BRAZ, SKY, SPEECH, BAYERN, REACT | — | YouTube bot check 2026-10-29; waiting on his downloads |
