# RUN: "Why Janet Jackson Couldn't Cry For Michael 💔" (Abundance Wisdom short, MJ × Janet)

## ▶ STATUS: resume here (2026-10-28 ~19:45): v1 EXPORTED, waiting on his review
- **`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Janet Couldnt Cry.mov`** + identical copy in
  `X:\Claude Projects\Exports\` (= `outputs/Janet Couldnt Cry.mov`, MD5 6318d0ef…): 1080x1920 30 fps, 1165 f, 38.833 s,
  38.3 Mb/s BT.709, AAC 48 kHz, **−13.7 LUFS, −3.1 dBTP, export QA PASS**. From `outputs/janet_v2_60.mp4` (picture
  `renders/janet_picture_v2.mov` = v1 + his Topaz jitter tweak spliced into S6 and S10-S11 via `splice_ranges.py`,
  `renders/tweak_ranges.json`) via `build/export.py`. The first export (default Topaz everywhere) is kept as
  `outputs/Janet Couldnt Cry (v1).mov` (never reviewed; replaced in both folders 20:08). QA beyond export (sync, jitter,
  his extended outs): `B8-REPORT.md` § QA. Edges `proof/final_edges.jpg` (every cut on the 30 fps file: no stray frame), sheet
  `proof/final_v1_sheet.jpg`, end `proof/final_end.jpg`. **B8 report: `B8-REPORT.md`.**
- Re-render after a note: change `build/make_timeline.py` (or captions.txt / audio.py) → `python build/make_timeline.py`
  → (Stage A only if framing / sources change: `stage_a.py render` → `topaz_his.py` → `align_frames.py`) →
  `build/finish.py render ../renders/janet_picture_v2.mov ../captions/caps_capcut.mov ../outputs/janet_v3_60.mp4 --audio
  ../renders/janet_audio.wav` (from build/, GPU venv) → `python build/export.py …` → `python win/final_edges.py <mov>` →
  copy to both folders (keep the reviewed version as `Janet Couldnt Cry (v2).mov`). Captions: `captions/make_plan.py` → `render_caps.py
  render caps_code.mov` (uv: fonttools pillow numpy scipy) → `capcut_pass.py` (GPU venv). Audio: `python build/audio.py`.
- Next: his review → change ONLY what he names → his notes into `presets/youtube-shorts/abundance-wisdom/LESSONS.md`.

## (previous) STATUS (2026-10-28 ~19:00): HIS DIRECTION RESOLVED (BRIEF.md § HIS DIRECTION) → code build next
- He re-edited the raw cut to **38.83 s** (dump `seqref/seq_his.tsv`, read-only; ABC09 + WR-book beats removed; ends on
  Michael's video message "I love you, and I am honored and proud to be your brother") and sent his Tella direction video
  (`brief/tella/guide.mp4`, "you can now get to work"). Every overlay / zoom / letterbox / transition mapped to his
  timeline in BRIEF.md. His A1 re-ASR'd clip by clip: clean. **Do NOT re-run clear_ours.js / place.jsx: his timeline
  is the source of truth now.**
- Catalog pass DONE (BRIEF.md). Overlays PICKED (2026-10-28 ~19:30, sheets in `ov/`):
  - "about his death": `E:\Bullshit Folder\smilin.png` (1080x1920, adult Michael 2007, laughing) → grey + letterbox.
  - Katherine: 60 Minutes Australia 2013 (copy `../mj-kids-saw-day-he-died/raw/60M_Katherine_2013.mp4`; the `Drake\`
    original's name has a character the shell can't pass) **599.92–602.50**: teary, tissue up 601.0–602.4, one shot (no
    cut 596–606). Band set above the "60 AUSTRALIA" bug.
  - Bucharest: `E:\Bullshit Folder\Lonely\…Jam - Live in Bucharest October 1st, 1992 (4K60FPS).mkv` **28.00–30.48**
    (he stands still, light flares; shot 24.433–32.450), full screen (letterbox not said; 4K → sharp 9:16).
  - Grammy: `E:\Bullshit Folder\Henry\1993 'Grammy LEGEND' Award - Restored.mp4` **432.40–434.15** (Michael + Janet
    cheek to cheek, laughing; shot from 431.147; no burned-in subs, unlike the [SUB ITA] copy).
- **Build progress (2026-10-28 ~19:45):**
  - DONE: catalog pass; his A1 from RAW (`seqref/raw/a1.wav`, 25 clips, 38.833 s, = the proxy rebuild at 0 ms);
    `build/make_timeline.py` → timeline.json (25 shots, 14 zooms, 12 transitions, 3 cards) + `overlays/picks.json`;
    `stage_a.py track` (14 locked shots, 0 misses; `cover_clamp`: the lock holds only while the picture covers the frame,
    so S12's head lift moves in frame instead of exposing it); `proof/stageA_sheet.jpg`; Stage A `renders/janet_stageA.mov`
    (2329 f); captions (`captions/captions.txt` → plan → `caps_code.mov`, 49 captions, line ~y1250-1290 = 64 %);
    audio `renders/janet_audio.wav` (−13.6 LUFS; fresh Epidemic swishes `build/sfx/SOURCES.md`, 21 dB under the voice).
  - DONE (~20:00): Topaz → `align_frames.py` (1 duplicate at the 4.65 cut dropped, 4 holds inside Michael's 29.97 message)
    → `renders/janet_picture.mov` (2329 f); zoom layers (faces pivot on the lip line y1190, overlays on centre); captions
    `caps_capcut.mov`; finish stills `proof/test_v1..v3.jpg`. Fixes from the stills: skin levelled before his grade
    (sat_level dl/wr 0.62, Katherine 0.5 → sat 0.57-0.62, R/G 1.45-1.76, his finals 0.43-0.59); Michael's message gamma
    0.85; cards per the brief B3/B5 (BET + Paris cards in the top third, the beat-1 lower third above the bottom 20 %).
  - RUNNING: full finish `outputs/janet_v1_60.mp4`. NEXT: `python build/export.py outputs/janet_v1_60.mp4
    renders/janet_audio.wav "outputs/Janet Couldnt Cry.mov"` → `win/final_edges.py` + sheet → copy to Final Renders +
    `X:\Claude Projects\Exports\` → B8 report.
  - Framing calls to tell him: captions at 64 % (DL's close-up is too low for a mid-frame line), BET band ends above the
    AP/BET bugs (his 403.4 % kept), Bucharest full screen (letterbox not said), Michael's "I LOVE YOU" red (set lists none).
- **Code build plan** (copy of `projects/joe-jackson-appointment/build/`): `a1_his.py` (his A1 from the RAW files: DL =
  proxy + 1580 s) → `make_timeline.py` + `overlays/picks.json` → `stage_a.py track/sheet/render` → `topaz_his.py` →
  `align_frames.py` → `centers.py` + `finish.py centers` → captions (his A1 words → captions.txt → make_plan → render_caps
  → capcut_pass) → `audio.py` (level match, NR, transition swishes 19–23 dB under the voice, NO music) → finish stills of
  every shot → full finish → `export.py` → Final Renders + Exports.

## (previous) STATUS (2026-10-28 ~15:40): RAW SEQUENCE PLACED in ABW10, waiting on his pass + his direction video
- His answers 2026-10-28: raw sequence in ABW10 first · **no music bed** · fetch *the detail.*'s 4K BET and use it if
  sharper · caption what she says ("but things kind of") · WR close-ups over DL's cutaways OK.
- **ABW10 › bin "Janet Couldnt Cry" › "Janet Couldnt Cry - raw cut"** (clone of "Onyx reaction template (empty)",
  1080x1920 **60 fps**, unchanged, timecode display 108): V1/A1 36 clips, V2 4 WR close-up covers (picture only, A2
  empty), 5 beat markers (name + card + warning). **58.42 s** on the timeline (≤ 62: none of the brief's trim steps
  apply). Placement v3 (v1/v2 read-backs kept as `premiere/readback.v1/v2.tsv`). His active sequence restored by ID
  ("Shorts cooked reel", `d4035e3b…`). **Not saved** (he saves).
- Verified (`win/verify.py`, `win/edges.py`, `premiere/readback.tsv`): every in-point within one source frame (worst
  0.017 s); each WR cover spans its V1 piece exactly (lock 1: the Jackson 5 montage under "I was in Paris" never shows),
  cover sync −12…+30 ms; ABC09 real source ends (inPoint + duration; the read-back outPoint carries place_sequence's
  +0.2 s over-trim) 404.483 (< the 404.504 wide) and 408.450 (≤ 409.576); first + last frame of all 40 clips
  (`proof/edges_sheet.jpg`): no flash of another shot; A1 rebuilt (`seqref/a1.wav`) + re-ASR per beat = the brief's words.
  Framing sheet: `proof/placement_sheet.jpg` (Janet in every crop; Meredith only where she really is on screen).
- **`seq_src/` is a SEQUENCING PROXY only.** `sources.json` / `edl.json` / `placement.json` point `source` at the CRF 12
  transcodes; DL's is a 1506x1080 crop of a 60 s window (file time = DL − 1580). The code build and any dump of HIS
  re-edited sequence must map back to the `raw` paths (DL: + 1580 s, full 3840x2160 with the 416 px pillarbox, no
  3012 crop), or a copied Joe build renders from the proxies.
- **The V2 covers are not linked to V1.** If he trims a covered piece (hook "Out of everyone…moment", "to cry"; "I was in
  Paris"; "there were moments…and it"), its cover must move with it or the WR lips drift off the DL audio.
- **BET:** the 320x240 copy stays (the only copy with the speech audio for the whole beat). *the detail.*'s 4K
  (`2DDImwmzmD8`) IS sharper (`proof/bet_vs_detail.jpg`) but uses the speech as silent B-roll under Dateline audio and
  covers BET 0–17.2 s only (detail = BET + 6.78 in `dl_detail/detail_4k_489-510.webm`, picture-aligned
  `win/vis_align.py`). AP / RTVE / theGrio copies checked (`dl_alt/`), none carries the whole beat sharper.
  Build option: Topaz Iris on the old BET next to the 4K frame.
- **For his ear:** beat 3 "smile **but** things kind of get": the clean-source passes hear "but", both A1 re-ASR passes
  on the JOINED cut hear "when". Captioned "but" (his call) unless he hears "when" on his pass.
- Next on his direction video: catalog pass into BRIEF.md → (if he re-edits, dump HIS sequence read-only and rebuild from
  it) → code build (copy `projects/joe-jackson-appointment/build/`; the brief's lower third, cards, True You cover photo
  over "You wrote,", adult Michael still over "…just watching", captions, grade, audio −14 LUFS, SFX, no music).
- Re-place from scratch (only if he has NOT edited it; compare a fresh `premiere/readback.js` with `readback.tsv` first):
  `python premiere/make_beats.py` → `resolve_beats.py .` → `python premiere/make_beats.py --covers` → `resolve_beats.py .`
  → `uv run plan_placement.py . DL_Janet_Dateline_2011_w1580@11.1333 WR_Janet_BookQuote_2011@26.2262` →
  `place_sequence.py . "Janet Couldnt Cry - raw cut" "Janet Couldnt Cry" premiere/place.jsx` → `python premiere/pp.py`
  on `clear_ours.js`, `place.jsx`, `restore_active.js`, `readback.js > readback.tsv` → `win/verify.py` (whisperx venv,
  CPU). Every piece edge is in `premiere/make_beats.py` (measured, with the reasons).

## (previous) STATUS (2026-10-28 ~07:40): INTAKE + LOCKS DONE, waiting on his answers (BRIEF.md § Open with Affan)
- All four sources are in `raw/` (his go 2026-10-28: "you try"; B2's yt-dlp commands, plain, no cookies, all four worked).
  Every beat's words were found and timed (CPU re-ASR of the windows, `win/asr.json`), the pauses were measured
  (`win/pauses.py`), and locks 1–6 were checked on frames (below, sheets in `proof/`).
- Runtime: **~65.8 s** with every pause > 0.25 s tightened; the brief's trim steps 1 + 2 bring it to **~61.7 s** (≤ 62).
  Final number = measured on the real timeline.
- Still open with him: (1) music bed (default none), (2) raw sequence in ABW10 first vs straight code build, (3) a better
  BET copy, (4) lock 2 by his ear ("but things kind of get"), (5) the WR-picture swaps over DL's cutaways (one is a
  childhood montage).
- Next on his answers: `beats.json` from the ranges table below → `resolve_beats.py` (pieces split at the measured
  pauses, stutters trimmed) → either `place_sequence.py` into ABW10 (bin "Janet Couldnt Cry", clone of the 30 fps
  template, his active sequence restored, never saved) or the code build (copy `projects/joe-jackson-appointment/build/`).
- Loose end: the full-source WhisperX run (`transcribe.sh`, pids 59588/45108) was starved by the other sessions' GPU jobs
  (Scott Clary Topaz, Derek stills); its background task was stopped but the two python processes keep running orphaned
  (killing them was refused). When it ends it writes `transcript/words.json`; nothing depends on it.

## Job facts
- Format: AW short, 1080×1920, 30 fps export (B3/B6). Finish = code build (`projects/joe-jackson-appointment/build/`
  is the newest working pipeline), unless he wants the ABW10 raw sequence first.
- Export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Janet Couldnt Cry.mov` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- Standing rules on this job: work in silence; never save or export his Premiere/AE projects; censor any drug or
  self-harm word (B1.6 bans the drug/intervention/doctor/Murray lines outright anyway); no silence > 2 s inside a clip
  (B1.1 is stricter: ~0.25 s); no 1–2 frame promo frames at clip edges; no Fable subagents; quote cost before heavy
  steps; his review notes go into `presets/youtube-shorts/abundance-wisdom/LESSONS.md`.
- Other sessions' jobs (Flex leg, Derek, AffanWiz, GTA, Scott Clary) and their sequences are off limits.

## Pipeline (per step: status · output)
| # | Step | Status |
|---|---|---|
| 1 | Intake: four sources → `raw/` | ✅ 2026-10-28 (`sources.json`) |
| 2 | Words + ranges + locks 1–6 + runtime | ✅ measured (below); pieces to be cut by ear at sequencing |
| 2b | Raw sequence in ABW10 (his order 2026-10-28) | ✅ 58.42 s, verified (STATUS) · his pass + direction video next |
| 3 | Audio: level-match three eras, light de-reverb on BET, −14 LUFS / ≤ −1 dBTP (measured on the ENCODED file), 2–4 frame crossfades | pending |
| 4 | Grade: his AE stack (match the recent MJ-family finals) | pending |
| 5 | Picture + graphics: full-bleed Janet crops, SD ≤ ~115 % punch, beat 5 push 100→108 %, one lower third (beat 1), cards (beats 2, 4, 5), captions word-by-word at ~62–68 % height with the red words | pending |
| 6 | SFX (his transitions' SFX; subtle set) | pending |
| — | Music bed (B4) | ✗ none (his answer 2026-10-28) |
| 7 | Test frames of every shot → his review | pending |
| 8 | Export + B7 QA + B8 report | pending |

## Sources (`raw/`, from YouTube 2026-10-28 with B2's commands)
| Code | File | Format | Notes |
|---|---|---|---|
| DL | `DL_Janet_Dateline_2011.mp4` | AV1 3840×2160 60 fps (a **4:3 SD picture pillarboxed** in 16:9), Opus, 2565 s | fan restore, soft + smoothed but no warping on Janet's face; faint NBC peacock lower left; no channel logo |
| ABC09 | `ABC09_Janet_RobinRoberts.mp4` | AV1 1280×720 29.97, Opus, 483 s | "abc" bug lower right |
| BET | `BET_Janet_2009.mp4` | AV1 **320×240** 30 fps, Opus, 78 s | AP bug lower left, BET bug lower right (outside a centred 9:16 crop) |
| WR | `WR_Janet_BookQuote_2011.mp4` | H.264 596×336 29.97 (16:9), Opus, 174 s | **a longer cut of the same NBC sit-down as DL**, with different camera cutting |
AV1 needs a transcode to H.264 before any Premiere import → **`seq_src/`** (what the ABW10 bin holds): ABC09, BET, WR
whole-file and DL as a 60 s window `DL_Janet_Dateline_2011_w1580.mov` (DL 1580–1640, pillarbox cropped
`crop=3012:2160:416:0` → 1506x1080 60 fps; file time = DL − 1580.000, verified on the shot cuts + audio), all H.264 CRF 12 +
PCM 48 k, sample-aligned with `raw/` (≤ 1 ms). `sources.json` keeps each `raw` path beside the placed `source`.
BET alternatives (2026-10-28, his "use it if it's sharper"): *the detail.* `2DDImwmzmD8` (4K; BET picture 0–17.2 s only,
under Dateline audio; `dl_detail/`, `proof/bet_vs_detail.jpg`), AP `1leCf6DefFg` 640x480, RTVE `5hVzq3mQQTQ` 640x480,
theGrio `iNIXBJ7Gv88` 480x360 (BET 31–46 only) in `dl_alt/`: none carries the whole beat.

## Ranges (source seconds; words from `win/asr.json`, pauses from `win/pauses.py`)
**Superseded for the placed cut by `premiere/make_beats.py`** (every piece edge re-measured at sequencing). Corrections
found then: beat 1 is "…that moment **to** [0.9 s] **to cry** [1.2 s] about his [0.25 s] **death**" (first "to" dropped;
"death." = 1614.30–1614.53, not 1614.05); BET has a ~3 s crowd pause after "My" (12.66–13.44 → "entire" 16.5) and "but"
is the 22.58 burst; no "I I" stutter in beat 5 ("when I [0.29] felt"); beat 5's "it was it was good" → "and it | was
good" (the second "was" at 1605.74); beat 3's "I tend to I [1 s] I have" → the second "I" dropped; WR "You [0.37] wrote,".
| Beat | Src | Words | Range | Picture under it |
|---|---|---|---|---|
| 1 | DL | "Out of everyone in my family, I never had that moment to cry about his death" | 1607.50–1614.05 (pauses 1610.18–1611.11, 1611.64–1612.87) | DL **wide two-shot** 1607.45–1611.68 → swap to **WR Janet CU** (WR 110.04–118.79, same take, DL = WR + 1496.40); DL Janet CU 1611.68–1615.27 |
| 1 | DL | (Meredith: "Why didn't you have that moment?" 1614.96–1617.02: OUT) | — | — |
| 1 | DL | "I don't know if it was trying to shield the pain [or just trying to hold it all together: trim step 1] because I saw that everyone else around me was falling apart" | 1617.55–1629.60 (pauses 1619.21–1619.50, 1621.18–1622.36, 1625.03–1627.43) | DL Janet CU 1617.57–1630.58 |
| 2 | BET | "My entire family wanted to be here tonight, but… it was just too painful" | 13.3–25.2 (first "my" 11.9 = a stutter, out; pauses 18.11–19.25, 20.75–22.34, 23.10–23.70) | one podium shot (1.77–71.87) |
| 2 | BET | "[To you, Michael is an icon: trim step 2.] To us, Michael is family." | 38.6–42.2 (pause 40.11–41.03) | same |
| 3 | ABC09 | "…you have to forgive me. I tend to… I have this thing where I tend to smile but things kind of get a little painful. I guess that's just my protective shield." | 394.20–408.40 (pauses 395.95–396.95, 399.08–399.89, 401.45–403.61, 405.22–406.65; one "I" of "I I" out) | Janet CU; the wide 404.50–406.14 falls inside a cut pause; **picture must end ≤ 409.576** (memorial dissolve) |
| 4 | WR | "You wrote," | 16.30–16.95 | Meredith → *True You* cover photo (brief) |
| 4 | WR | "I still have not seen the film This Is It. I still can't watch any of his videos, listen to his music. I'm certain that one day I'll again be able to enjoy the miraculous sound of his voice [and the marvelous sight of his dancing: trim step 3, not needed], but that day has not yet arrived." | 24.15–38.10 ("I can't describe our pain… losing their son" 17.02–23.76 out) | Meredith 22.86–26.23 → Janet B-roll; **Janet CU listening** 26.23–29.56; wide 29.56–36.24 → Janet B-roll or crop; **Janet CU** 36.24–40.07 |
| 5 | DL | "I was in Paris, and I just spent the night just watching all his videos, listening to his music, and there were moments when I felt to cry, moments that made me laugh, and it was good for me. I needed it." | 1587.30–1607.20 (pauses 1588.88–1590.23, 1590.55–1591.07, 1593.34–1594.38, 1595.26–1595.73, 1597.23–1598.71, 1600.17–1600.46, 1603.45–1605.26; "I I" and "it was it was" stutters trimmed) | see below |
Beat 5 picture: "I was in Paris" (1587.3–1588.7) is on DL's **Jackson 5 childhood montage** (until 1589.200) → swap to
**WR Janet CU** (WR 48.9–50.3; same take, r 0.96, DL = WR + 1538.41); DL Janet CU 1589.233–1591.133; Meredith
1591.133–1593.733 ("I just spent the night just watching"; WR shows the wide there too) → the brief's optional **adult
Michael music-video still (~1.5 s)**; DL CU 1593.733–1597.350; DL wide 1597.350–1601.650 ("there were moments when I
felt to cry") → **WR Janet CU** (WR 95.20–106.67, DL = WR + 1497.43); DL CU 1601.650–1607.450 (incl. "I needed it.",
hard cut ~1607.20 before the next line "Out of everyone" 1607.50).
Measured: tightened total 65.8 s (B1 14.0 · B2 14.3 · B3 9.4 · B4 13.6 · B5 14.4) → trim step 1 (~−2.1 s) + step 2
(~−2.0 s) = ~61.7 s. Optional call (ABC09: Janet from "I, I just" ~5:33, Jermaine's statement on picture/audio to ~5:32)
and "not one day" (it is in WR 69.9–77.0, not at DL 18:28 in this upload) stay out.

## Locks
1. **No minors on frame:** ABC09 beat 3 = Janet CU to **409.576** (last clean frame); the memorial dissolve (11-year-old
   Paris) starts 409.609 (`proof/abc09_memorial_cut.jpg`); "shield." ends 408.34, so the out is clear. **DL 1586–1589.200
   = a Jackson 5 childhood photo montage under the narrator and under "I was in Paris"** (`proof/dl_montage_cut.jpg`):
   never on screen; WR's close-up covers that line. BET, WR, DL 1589.233–1630.6: adults only (`proof/*.jpg`).
2. **Beat 3 by ear:** every unprompted pass hears **"I tend to smile but things kind of get a little painful"** (large-v3
   "but" p 0.54, medium.en p 0.67, YouTube's auto-captions "but things kind of you have"); a "when" prompt only reaches
   p 0.10. Not the brief's "when things… get". Pauses: smile [0.8 s] but things kind of get [2.2 s] a little painful.
   Captioned as heard ("but… kind of") unless his ear says "when". Full line: "you have to forgive me. I tend to… I have
   this thing where I tend to smile but things kind of get a little painful. I guess that's just my protective shield."
3. Optional call: not used (runtime ≥ 55 s). For the record: Jermaine's UCLA statement runs on picture to ~5:32 and his
   voice ends "2:26 p.m."; Janet starts "I, I just, I couldn't believe it" right after.
4. **DL restore:** no burned-in channel logo; faint NBC peacock lower left (outside a Janet crop); Janet's face is soft and
   smoothed (SD at 4:3, pillarboxed), no warping seen at full size (`proof/dl_face_2659.png`). Original NBC upload not
   searched further: WR (16:9, 336p) is the other copy of the same interview.
5. **Beat 5 picture:** DL is not B-roll over "I was in Paris…" but the childhood montage (lock 1) → WR close-up. Every
   other DL cutaway in beats 1/5 has a WR close-up except "…just watching" (~1.5 s, both uploads cut away) = the brief's
   Michael still.
6. **WR:** the reader is **Meredith Vieira**, in the same NBC sit-down as DL (same room, Janet in the white jacket, *True
   You* on the coffee table in the wide). WR is a fan upload of that broadcast (longer cut than DL's); the passage is not
   in DL (audio cross-correlation, r ≤ 0.31). Janet is on screen listening for part of it (26.23–29.56, 36.24–40.07).
   "FROM HER BOOK · 2011" holds.

## Log
- 2026-10-28: set received (via the session that started this one). Oriented; drive search: none of the four on disk
  (Henry holds Janet × Piers Morgan 2011 and the 1993 Grammys, neither in the set). Questions raised with him.
- 2026-10-28: his answer on downloads: "you try but you're pretty much never successful". All four downloaded with B2's
  commands (BET, WR, ABC09, DL 1.44 GB). Full-source WhisperX starved on the shared GPU → CPU re-ASR of the needed windows
  instead (`win/win_asr.py`); WR ↔ DL aligned by envelope cross-correlation (`win/xcorr.py`); pauses `win/pauses.py`.
- 2026-10-28 ~15:00: his answers (raw sequence first, no music, try the 4K BET, "but things kind of", WR swaps OK). BET
  alternatives fetched and aligned (none covers the beat). The orphaned WhisperX ended without writing; `transcript/words.json`
  built from `win/asr.json`. Edges measured (`win/runs.py`, `win/snip_asr.py`, `win/strip.py`), covers re-measured per piece
  (`win/xcorr_cover.py`). Placed v1 (59.63 s); the A1 re-ASR missed "death" in every pass → the out cut it (1614.13 vs the
  real 1614.30–1614.53) and showed "to … to cry"; v2 re-placed after a read-back proved the sequence untouched: 58.55 s.
  Edge-frame check (`win/edges.py`) found B5 "I just spent" opening on 0.1 s of close-up + one razor frame in Meredith's
  crop → in moved onto the cut (1591.1333; the piece alone still reads the full line) → v3 re-placed (untouched check
  again): **58.42 s**, verified, edges clean.
