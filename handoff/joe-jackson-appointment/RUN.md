# RUN — "Why Michael Jackson's Father Needed An Appointment To See Him 💔" (Abundance Wisdom short, MJ × Joe v3)

## ▶ STATUS: resume here (2026-10-27) — SHIPPED: v2 UPLOADED by Affan ("it's uploaded now"), no further notes. Job closed.
- Nothing pending. Re-open only on his word; the re-render recipe below still holds (picture = `renders/joe_picture_v2.mov`).

## (previous) STATUS (2026-10-27 ~06:25) — v2 EXPORTED (his v1 notes applied), waiting on his review
- **`Final Renders\Joe Appointment v3.mov`** = v2 (+ identical copy in `X:\Claude Projects\Exports\`; v1 kept beside both as
  `Joe Appointment v3 (v1).mov`): 1207 f @30, 40.233 s, BT.709, **-13.8 LUFS, -3.1 dBTP, QA PASS**. From `outputs/joe_v2_60.mp4`;
  sheet `proof/final_v2_sheet.jpg`, test `proof/test_v2.jpg`.
- His v1 notes (2026-10-27) and ONLY these changed (LESSONS 2026-10-27):
  1. Hook = the SAME interview (JJ), Joe silent staring toward the interviewer: JJ 832.6-834.8 (F0, letterboxed like his answer;
     v1 used the Larry King freeze). Re-rendered frames 0-131 only: `renders/seg_F0.mov` -> Topaz -> `seg_F0_aligned.mov` ->
     `splice_ranges.py` -> `renders/joe_picture_v2.mov`.
  2. JOW blurred background full screen: per-shot `twin_scale` 3.0 about the band centre (finish.py letterbox()).
  3. Music removed (his job; `audio.py` MUSIC = None), SFX unchanged. v1 mix kept: `renders/joe_audio_v1_music.wav`.
- Re-render recipe below now uses `renders/joe_picture_v2.mov`.

## (previous) STATUS (2026-10-26 ~20:00) — v1 EXPORTED, waiting on his review
- **`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Joe Appointment v3.mov`** (+ identical copy in
  `X:\Claude Projects\Exports\`, = `outputs/Joe Appointment v3.mov`): 1080x1920 30 fps, 1207 f, 40.233 s, H.264 43.3 Mb/s
  BT.709, AAC 48 kHz, **-13.8 LUFS, -3.0 dBTP, QA PASS**. From `outputs/joe_v1_60.mp4` (finish 60 fps) via `build/export.py`.
  Sheets: `proof/final_v1_sheet.jpg` (1 f/s), `proof/final_v1_end.jpg` (end fade), test frames `proof/test_v1_grid.jpg`.
- Picture chain: `renders/joe_stageA.mov` -> Topaz `renders/joe_stab_chr2_iris3_prob4.mov` -> `align_frames` ->
  `renders/joe_picture.mov` (2413 f; repaired frames all inside the O1 still slot or on cuts) -> `finish.py render`
  (his AE grade, JJ skin levelled gamma 0.74 + sat 0.58, letterboxes, stills, 12 zoom layers on the lip line, 11
  transitions, 4 cards, captions `captions/caps_capcut.mov`) + `renders/joe_audio.wav`.
- Re-render after a note: change `build/make_timeline.py` (or captions.txt / audio.py) -> `python make_timeline.py` ->
  (`finish.py centers` if zooms changed) -> `"$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" build/finish.py render
  renders/joe_picture.mov captions/caps_capcut.mov outputs/joe_v2_60.mp4 --audio renders/joe_audio.wav` (from build/) ->
  `python build/export.py outputs/joe_v2_60.mp4 renders/joe_audio.wav "outputs/Joe Appointment v3.mov"` -> copy to both folders
  (keep v1 as `... v3 (v1).mov`). Captions: `captions/make_plan.py` -> `render_caps.py render` (uv: fonttools pillow numpy
  scipy) -> `capcut_pass.py` (GPU venv). Audio: GPU venv `build/audio.py renders/joe_audio.wav`.
- Next: his review -> change only what he names -> LESSONS (presets/youtube-shorts/abundance-wisdom/LESSONS.md).

## B8 report (the brief's report-back)
- Runtime **40.23 s** (his cut; the brief's ≤65 s). The over-65 s trim was not needed; HE removed beat 6 and "He wouldn't
  have cared" in his re-edit; his second "Joe knew that" stays (0.72 s pause kept: his rejoined clip).
- Ranges (HIS edit, `seqref/seq_his.tsv`, source seconds): B1 JJ 676.05–677.42 · 678.67–679.88 · 680.08–682.88 ·
  683.67–685.38 · 686.30–688.10 (picture = LK freeze 107.774) | B2 WB-A 49.87–51.35 · 54.33–56.30 · 104.88–107.97 ·
  108.30–110.10 (under the suits photo) · 110.90–112.18 · 112.35–113.48 | B3 MF 267.72–269.53 · 271.05–272.35 |
  B4 JOW 2271.23–2273.33 (under Trump Tower) · 2274.23–2275.72 · 2275.95–2278.85 · 2278.98–2281.50 · 2281.63–2284.40 |
  B5 MF 944.57–946.10 · 946.23–947.35 (under the hand photo) · 947.93–949.37 · 949.57–951.48 · 964.62–968.60 | B6 cut by him.
- Locks: 1 OPEN (no name in either upload; generic card) · 2 kept hypothetical, starts on "Joe" · 3 JJ card "2009" · 4 JOW is
  a collage: beat 4 = an outdoor interview (after June 2009, date unknown), the WSJ question = a third source, beat 6 (~1993)
  cut by him; no original found (YouTube blocked) · 5 n/a (beat 6 cut) · 6 captioned "walked and said" (reads vary).

## (previous) STATUS (2026-10-26 ~19:45) — CODE BUILD RUNNING (his go: "Go ahead... use about 1.5 Higgsfield credits")
- Catalog pass in BRIEF.md (done first). Higgsfield: Trump Tower upscaled (bytedance 4k, job e172727a, **2 credits** — the
  nano_banana_2 2k enhance priced 2 cr too and would have cropped to 9:16; balance 1178.5 -> 1176.5) ->
  `build/overlays/src/trump_tower_hf4k.png` 2160x4945.
- Build = `build/` (copied from MJ Kids Saw). Done: his A1 `seqref/raw/a1.wav` (`a1_his.py`, 24 clips, 40.23 s);
  captions `captions/captions.txt` -> `caps_capcut.mov` (62 captions, 2414 f; words.json fixes: "in two sides of" ->
  "inside of", lock 6 "He said" -> "and said"); `build/timeline.json` (`make_timeline.py`: 21 shots, 12 zooms, 11
  transitions, 4 cards); `stage_a.py track` (13 locked shots, 0 misses); audio `renders/joe_audio.wav` (`audio.py`:
  per-speaker level match to the bodyguard, NR on JJ/JOW, fresh Epidemic set `build/sfx/SOURCES.md`, "Demure" piano 14 LU
  under, -13.8 LUFS).
- Framing (proof/stageA_sheet.jpg): lips ~y835 under the caption line (caption_shift 90 = his MJ Kids Saw position); faces
  high in frame scaled up so no mirror (bodyguard wide 2.4 / CU 1.95, Fiddes 2.75 = tight); JJ letterboxed in his
  440-1484 band (Katherine short's JJ precedent) so the NEWSONE / TV One bar stays out, nose y960 = captions on his nose
  (his Katherine note); LK freeze full-bleed 5.94; JOW in its own 657-1315 band at his 60.87 %. Code changes: finish.py
  per-shot `band` (letterbox + glow bars), stage_a.py `freeze`.
- Running: Stage A render -> Topaz (`topaz_his.py`) -> `align_frames.py` -> `renders/joe_picture.mov`.
- Next: `centers.py` on Stage A -> `finish.py centers` -> test stills of every shot -> full finish render (60 fps) ->
  `export.py` -> `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Joe Appointment v3.mov` + `X:\Claude Projects\Exports\`.

## (previous) STATUS (2026-10-26 ~19:00) — DIRECTION VIDEO RESOLVED (BRIEF.md § HIS DIRECTION), build quoted, waiting on his go
- His Tella video (10:07) transcribed + every "this" mapped to his timeline (BRIEF.md table). HIS cut = `seqref/seq_his.tsv`
  (40.23 s, beat 6 removed, V2 = overlay slots). Freeze-frame source: `E:\Bullshit Folder\Henry\Larry King Live- Joe Jackson
  denies abuse on Michael - 07-20-09.mp4` @ 107.774 s (picture only). Overlays fetched to `build/overlays/src/`: Getty 52322511
  Joe + Michael suits 2326x1748 (his Daily Breeze pick, same file via dailynews.com), Britannica Trump Tower 697x1600 (his pick),
  NYT jackson-obit-3 superJumbo 1594x2000 (same walk as his The Sun pick, 617x959; sharper and shows the hands). Sheet
  `proof/overlay_picks.jpg`. No child in any.
- Quoted: code build ≈ 4–5 % of the week (~$90–120); Higgsfield ~1.5 cr asked for the Trump Tower still (soft at full screen).
- Flagged to him: Trump Tower is NYC; Joe's story is the 2009 LA rehearsals (the brief's JUNE 2009 · THIS IS IT REHEARSALS
  card would sit on the tower). His call; built as he said unless he changes it.
- Next on his go: catalog pass into BRIEF.md → copy `projects/mj-kids-saw-day-he-died/build/` → his A1 rebuilt from
  seq_his.tsv → captions → picture chain (Topaz on faces, letterbox JOW at his 60.87 %, freeze, overlays) → zoom groups +
  transitions from BRIEF → audio (level match, NR on JJ/JOW, piano bed, SFX) → test frames → full render → 30 fps export.

## (previous) STATUS (2026-10-26 ~17:00) — RAW SEQUENCE PLACED, waiting on his pass + his direction video
- **ABW10 › bin "Joe Appointment" › "Joe Appointment - raw cut"** (clone of "Onyx reaction template (empty)", 1080x1920
  60 fps): 28 clips V1/A1 + 6 beat markers, **45.12 s**. Readback (`premiere/readback.tsv`) = plan: every in-point within one
  source frame (worst 0.017 s), V/A offsets identical. His active sequence restored to **Sequence 27**. Not saved (he saves).
- His order (2026-10-26): **"do only the sequencing first in premiere so that i can give you the creative direction video"**.
  Nothing creative built. Next on his video: catalog pass into BRIEF.md → resolve his direction video into BRIEF.md → (if he
  re-edits the raw cut, dump HIS sequence read-only like MJ kids saw `premiere/dump_his.js` and rebuild his A1) → code build.
- Open for him (BRIEF.md § Found at sequencing): beat 6 is a ~1993 interview (Tyson/Jordan line right after "I love him"),
  "I love him" plays over Michael B-roll, runtime 45.1 s vs the brief's ≈62–66 s, lock 1 (name), lock 6 + "inside" by ear.
- Re-place from scratch: `premiere/clear_ours.js` (this sequence only) → `place_sequence.py` → `premiere/place.jsx` →
  `premiere/restore_active.js` (WANT = his active sequence) → `premiere/readback.js`. Scripts run through
  `node lanes/premiere/premiere-bridge.mjs execute_extendscript`. The bin holds the job's `raw/` copies (ASCII names: three
  originals carry curly quotes / an em dash).

## Sources (`raw/`, originals in E:\Bullshit Folder\Henry; YouTube refuses this PC: bot check 2026-10-26, never bypassed)
| Code | File | Original | Format |
|---|---|---|---|
| JJ | `JJ_Joe_2009.mp4` | `EXCLUSIVE LEAK- Joe Jackson's FULL Interview.mp4` | 1920x1080 23.976 (upscaled SD), 905 s; NEWSONE.COM + TV One "one" bugs along the bottom edge (inside the Joe crop) |
| WB-A | `WB-A_Appointment.mp4` | `“Joe Jackson Yelled At Me” … At Michael’s House.mp4` (+ 4K VP9 .mkv beside it for the final crop) | 1920x1080 23.976, 228 s, gated podcast audio, "DIALOGUE" bug lower right |
| MF | `MF_Fiddes.mp4` | `“Michael Jackson Asked For Joe Jackson’s Help Days Before Death” — Ex-Bodyguard Reveals MJ Last Days.mp4` | 1920x1080 23.976, 1043 s, one locked-off wide |
| JOW | `JOW_JoeOwnWords.mp4` | `My Son, Michael Jackson - Joe Jackson In His Own Words - Full Documentary (4K 2160p) - the detail..mp4` | 1920x1080 **60 fps** (not 4K), 2557 s, "d." bug top right; a compilation of many interviews |
| WB-B (ref) | `win/alive/raw/ALIVE.mp4` | `“Michael Jackson Would Be Alive If Joe Jackson Was in His Life” – MJ Bodyguard on Michael’s Death.mp4` | reference only (its 1:07–1:20 = "the last time they was in contact, him and Joe…") |
Transcripts: `transcript/words.json` (all four, full); edge checks `win/snip/` (isolated faster-whisper large-v3 CPU) + 20 ms RMS.

## Ranges (source seconds; `edl.json` / `placement.json` hold the frame-snapped values)
| Beat | Src | Pieces (in → out) | Trimmed inside |
|---|---|---|---|
| 1 | JJ | 676.05–677.28 · 678.68–679.69 · 680.10–682.70 · 683.68–685.23 · 686.31–687.91 | 1.4 s pause mid-question; WhisperX "and was it" = interviewer's cut-off "and–" (679.72–679.84); 1.0 s + 1.1 s restaurant room tone between the "I tried so hard"s and before "But". Brief's 11:12–11:29 runs ~4 s early. |
| 2 | WB-A | 49.88–51.25 · 52.51–52.76 · 54.35–56.11 · 104.90–107.80 · 108.32–109.92 · 110.90–112.04 · 112.36–113.31 | "um" after "and" (52.76–53.20), pauses 1.5 + 1.3 + 0.5 + 1.0 + 0.3 s (gated silence). "And I went inside… Does Joseph have an appointment?…" (brief: removed). |
| 3 | MF | 267.73–272.18 | starts on "Joe" ("But" ends 267.66, Joe 267.70: nothing before it); "less" really ends ~272.1 |
| 4 | JOW | 2271.23–2273.13 · 2274.23–2275.52 · 2275.95–2278.65 · 2278.98–2281.30 · 2281.63–2284.33 | pauses + two clicks; "The last time I spoke… So I had gotten up to the apartment and" (brief: card carries it) |
| 5 | MF | 944.57–945.94 · 946.24–947.17 · 947.95–949.36 · 949.57–951.31 · 964.63–967.21 · 967.72–968.45 | a −57 dB breath between "up" and "together"; "but he just different type of relationship… Joe," (951.3–964.6) |
| 6 | JOW | 2364.70–2365.22 · 2374.35–2375.25 · 2375.58–2377.20 | "um… I can say this because Michael is a very, very big superstar. And" (brief's "Yeah… he's my son"); hard cut on "him." (2377.15) |
Edges for his ear: B2 "and" join (52.76, a −48 dB dip into "um"); B5 "son," → "Joe had" (951.30: "son, but" has no gap);
B3 in 267.69 (2 frames after "But").

## Locks
1. **Bodyguard's name — OPEN.** WB-A and WB-B are the same man, same set (one Art Of Dialogue session); neither audio names
   him; "Vegas" fits the Whitfield / Javon Beard team. Generic MICHAEL'S BODYGUARD · LAS VEGAS unless WB-B's YouTube title or
   description names Whitfield.
2. Beat 3 hypothetical — cut starts exactly on "Joe would have gone in there"; the voicemail claim before it is out. Never
   caption it as an event.
3. JJ date — upload 1 Aug 2009 (NewsOne / TV One, Smokey Fontaine, NEWSONE.COM bug on frame); the brief's "2009" holds.
   AUG 2009 not independently confirmed (NewsOne first published it 31 Jul 2009).
4. **JOW's sources — RESOLVED, and the brief's premise is wrong:** JOW is a collage. The WSJ will question (JOW 2310) sits on
   the Larry King Live set (Joe in the fedora), but Larry King Live 20 Jul 2009 (CNN transcript) has neither the WSJ line nor
   beat 4: there "They cut me off" is followed by "Now, what if Michael asked to see you?", so JOW spliced beat 4 in from
   elsewhere. **Beat 4** = the outdoor interview JOW shows under it (Joe in maroon suit + hat, young bearded interviewer, he
   laughs at the punchline; Joe's mouth moves on words at the checked frames): after June 2009 (he says "the last time I
   spoke with Michael"), date unknown → no date card beyond the brief's JUNE 2009 rehearsal card. **Beat 6** = a ~1993
   interview (Joe younger, SD; next words "Michael Tyson, Michael Jordan, then Michael Jackson, my son") → not 2009, said
   while Michael was alive. Original uploads not searched further (YouTube blocked here).
5. Beat 6 cut point — out 2377.19, on "him." (his next words "And he's a Michael…" at 2378.81).
6. **"walked [?] and said" — his ear.** WhisperX "walked through and said"; isolated re-ASR "walked us out"; re-ASR of the
   rebuilt A1 "walked in and said" then "walked. He said". Caption what he hears. Same for "I went in[to the side of] the
   apartment" (brief: "inside").

## Checks
- Re-ASR of the A1 rebuilt from the readback = the brief's words in order; no filler, no banned line (none of: sort this out,
  would he still be alive, I could never get to him, voicemail, AEG, Murray, drug/doctor words, abuse denials).
- No gap > ~0.25 s left (WhisperX "gaps" at 0.99 / 12.98 / 14.18 s are alignment artifacts: RMS shows 0.13 s, continuous
  speech, 0.14 s).
- No child on frame: `proof/crops_sheet.jpg` (every placed crop). Adult Michael only (B4 stage B-roll, B6 B-roll).
- Crops: B1 question frames the interviewer (he asks it); B4 outdoor pieces forced onto Joe x 0.765 (`framing.json`, the
  detector took the interviewer).

## Log
- 2026-10-26: brief pasted; he narrowed it to sequencing first. JJ found locally; WB-A + WB-B delivered 15:22, MF + JOW 16:17
  (SnapDownloader). All transcribed; beats.json → resolve_beats → plan_placement (+ framing.json, split JOW@2272.60) →
  place_sequence; readback check 1 found room tone at two joins (tighten's whole-file floor) → fixed, re-placed, verified.
