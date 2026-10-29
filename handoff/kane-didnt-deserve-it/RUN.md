# RUN: "Why They Said Harry Kane Didn't Deserve The Ballon d'Or 😳" (Abundance Wisdom short, football)

## ▶ STATUS: resume here (2026-10-29 ~14:55 PST): RAW SEQUENCE PLACED in ABW10, waiting on his pass + direction
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
