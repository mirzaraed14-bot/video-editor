# RUN: "Why Michael Jackson's Mother Never Got Over Him 💔" (Abundance Wisdom short, Katherine × Michael)

## ▶ STATUS: resume here (2026-10-29 ~14:45): RAW SEQUENCE v2 PLACED in ABW10 + verified, waiting on his pass
- **ABW10 › bin "Katherine Never Got Over Him" › "Katherine Never Got Over Him - raw cut"** (clone of "Onyx reaction
  template (empty)", 1080x1920 60 fps): **58.38 s**, V1/A1 31 clips, V2 = the Katherine backstage cover (picture only, its
  audio removed), 6 beat markers (name + card + warning), 78 Position keys on the 8 KAT clips. **Not saved** (he saves).
  His active sequence ("Sequence 34") restored after placing.
- Verified: read-back = plan (worst 13.4 ms, no gaps, scales/positions/key counts, `win/verify.py`); A1 rebuilt from the
  read-back (`seqref/a1_readback.wav`) re-ASR'd per beat + at every beat join with the neighbour in front
  (`win/asr_a1.py`): the brief's words, no leak. v1 (58.82 s, 3 leaks: Jermaine "but" / "be-cause", Michael "But") is kept
  as `premiere/readback.v1.tsv` + `place.v1.out`.
- Premiere froze ~14:30 right after an auto-save of ABW10 (opened from a 6-deep nested Auto-Save path on E:; E: 193 % busy,
  Premiere idle CPU, no bridge commands queued) and recovered by itself; lab-notes entry added. The clear call of the v2
  re-place answered "bridge unavailable" but had run (placer refuses a non-empty track; counts + 6 markers exact).
- Next: his pass on the raw cut (+ his Tella direction, as on Janet/Joe; the by-ear list below) → if he re-edits, dump HIS
  sequence read-only and build from it → catalog pass in BRIEF.md (CLAUDE.md learning loop 5) → quote → code build (copy
  `projects/janet-couldnt-cry/build/`). Re-place recipe (only if he has NOT edited it): fresh `readback.js` must equal
  `premiere/readback.tsv` → `active.js` → `restore_active.js` with that ID → `clear_ours.js` → `place.jsx` → `kat_keys.js`
  → `restore_active.js` → `readback.js > readback.tsv` → `win/verify.py` → GPU `win/asr_a1.py`.

## His answers (2026-10-29)
- "first create the sequencing in premiere" → raw sequence in ABW10 first (like Janet).
- KAT + JERM: try the brief's yt-dlp lines → both came down (KAT VP9 1080p 833 s; JERM's YouTube original = 854x480,
  same as the disk rip, so no sharper copy exists).
- Music: **none** (his 2026-10-27 rule; SFX stay).
- Beat 4 picture: **Katherine-only crop** of the 1988 backstage shot (25:16).

## Job facts
- Format: AW short, 1080×1920, 30 fps export. Export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Katherine
  Never Got Over Him.mov` + identical copy in `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- Standing rules: work in silence; never save/export his Premiere/AE projects; censor drug/self-harm words (none in these
  lines); B1.1 gaps ≤ ~0.25 s except Katherine's beat-6 pause; no 1–2 frame promo frames at edges; no Fable subagents;
  quote cost before heavy steps; his review notes → `presets/youtube-shorts/abundance-wisdom/LESSONS.md`.
- Don't reuse `projects/katherine-day-michael-died/` picks. Other sessions' jobs (Kane, Janet, Flex, Scott Clary…) are off limits.
- Cost so far: intake + sequencing ≈ 2–3 % of the weekly cap; the code build ≈ 4–6 % more (quote again before it).

## Pipeline
| # | Step | Status |
|---|---|---|
| 1 | Intake: five sources → `raw/` (copies) + `seq_src/` windows | ✅ (align 0–1 ms, `win/align_check.py`) |
| 2 | Words + pieces by ear-proxy + runtime | ✅ 58.38 s (v2), no trims needed |
| 2b | Raw sequence in ABW10 | ✅ v2 placed + verified 58.38 s (14:45) · his pass next |
| 3 | Audio: 4 eras level-matched, −14 LUFS / ≤ −1 dBTP on the encoded file, 2–4 frame crossfades | pending (build) |
| 4 | Grade: his warm MJ-family stack | pending |
| 5 | Picture + graphics: 3 labels + 1 card, captions w/ red words, B6 push 100→110 % | pending |
| 6 | SFX | pending |
| — | Music | ✗ none (his answer) |
| 7 | Test frames → his review | pending |
| 8 | Export + QA + B9 report | pending |

## Sources (`raw/` = copies; `seq_src/` = what ABW10 holds; file time = source − window start)
| Clip | Raw | Window | Notes |
|---|---|---|---|
| KAT_w238 / KAT_w505 | `raw/KAT_Katherine_studio.mp4` (yt-dlp yL39PTF-xmk; VP9 1920x1080 29.97, 833 s) | 238–256 / 505–532 | burned-in subtitle bar rows **788–939** on every frame; framed at **250 %, frame ends on row 784** (bar never in frame) + Position keys from a 5 fps face track |
| JOW_w1870 | `raw/JOW_Joe_own_words.mp4` (= Henry\ copy, 1080p60) | 1870–1910 | home interview CU to 1891.65 · cutaway 1891.65–1892.55 · **Larry King Live** split (Larry left) to 1896.45 · Joe solo |
| JERM_Jermaine_2011 | `raw/JERM_Jermaine_2011.mp4` (yt-dlp dL5h3zdrGJY, 854x480) | whole | 400 % fill (SD) |
| PHM_w1500 | `raw/PHM_Private_Home_Movies.mp4` (= Henry\ copy, 1440x1080 25) | 1500–1565 | stage to 1526.84 · Michael seat · crowd 1532.0–1536.64 (+ dissolve, last blended frame 1536.64) · Michael · music bed under the voice |
| PHM_kath_cover | PHM 1516.40–1517.82 at 0.808x (25 fps, picture only) | 1.80 s | V2 over the crowd, 204.55 % (= fill × 1.15), centred right of Katherine: Shannon + the face-blurred man out; an adult stands in the dark behind her (can't be cropped at ≤ 115 %) |
| OPRAH_w1095 | `raw/OPRAH_1993_4K.mp4` (= Henry\ copy, 1440x1080 50) | 1095–1120 | Michael CU, no cut |
`raw/JERM_SnapYT_480p.mp4` = the identical disk rip (unused).

## Pieces (source seconds; `premiere/make_beats.py` holds every edge + its reason)
| Beat | Src | Words (as heard) | In → out |
|---|---|---|---|
| 1 | KAT | "He should have been burying me." · "I shouldn't have been burying my child." · "The worst thing in the world is to lose a child." (approved reorder; "and, um [4.1 s]" + "but" out) | 249.60–251.20 · 251.30–252.98 · 241.46–243.92 |
| 2 | JOW | "She's taking it real hard." · "You start talking about Michael, she starts crying" · "Katherine is taking it very, very hard" (LK) · "She's really, really taking it harder than I ever seen her take anything" | 1886.22–1888.34 · 1889.08–1891.58 · 1892.82–1895.28 · 1896.96–1901.93 |
| 3 | JERM | "When I called my mother back, I heard the most horrible tone in her voice when she said, he's dead." · "I've never heard this tone [in her voice / before]" · "I go straight to my mother and I" · "consoled her" · "and still to this day she don't" · "even remember me hugging her" | 44.36–48.92 · 53.10–54.235 · 83.92–85.46 · 85.84–86.86 · 87.14–88.50 · 88.80–90.22 |
| 4 | PHM | "I remember one thing my mother said to me" · "we were in Copenhagen" · "and there was just a sea of people" · "and" · "her eyes were watering, she was on the side of the stage, and I said, mother what's wrong, why are you crying?" · "She said," · "when you were a baby and I was holding you in my arms, I would have never dreamt" · "you would have this kind of effect" · "on an audience" · "and I" · "gave her a hug" | 1524.60–1526.70 · 1527.24–1528.54 · 1529.90–1531.26 · 1534.58–1535.08 · 1535.38–1540.14 · 1540.56–1541.46 · 1542.92–1546.66 · 1549.52–1550.84 · 1551.42–1552.06 · 1552.62–1553.01 · 1553.48–1554.36 |
| 5 | OPRAH | "My mother's wonderful. To me, she's perfection." | 1106.84–1109.60 |
| 6 | KAT | "Even this morning, [1.16 s KEPT] every morning that I wake up," · "my baby is on my mind." · "Oh gosh, I'm sorry." · "I'm sorry." · "I didn't intend to do this." (hard cut) | 509.62–513.56 · 515.64–517.22 · 524.76–526.30 · 526.94–527.74 · 528.18–529.40 |
Out: PHM "200,000 people" tail (1533.6–1533.9), "um" (1542.0–1542.4), "that you would, you could, you would do this", "like
this", "I think"; JOW "Mm-hmm", ", you know" ×2, the "she's…" false start, ", yes"; KAT "You know what?", "I don't,".

## For his ear (captions follow the audio)
1. JERM "I've never heard this tone **in her voice** / **before**" (ASR passes split; brief: "of voice"; it is the brief's
   trim-1 line if he'd rather drop it). Beat 3's head: some reads hear "Then when": the real "then" ends 44.26, the cut is
   44.367 in silence (10 ms level), so it should read "When I called".
2. KAT "I didn't intend to do **this**" (full-file ASR + the burned subs) vs "**that**" (every piece-level pass); the subs
   also say "I **thought** I didn't" where she says "I don't, I didn't" (cut).
3. KAT "my baby **is** / **baby's** on my mind"; JOW "She's taking it real [uh] hard"; PHM "watering" (brief: "watery").
4. Beat 6: only the brief's pause is kept. She actually breaks in the **7.2 s before "Oh gosh"** and pauses 2.2 s after
   "wake up" (both tightened per rule 1). Runtime room: up to ~6.6 s.
5. Runtime 58.4 s is under the 60–65 s target: every word is in; joins are 0.16 s. Breathing the joins to ≤ 0.25 s or
   keeping more of her break would add time.

## Locks
1. **No minors:** PHM crowd (1532.0–1536.68) covered on V2; stage/seat/home video = adults; KAT, JOW, JERM, OPRAH adults.
2. **No interviewer/narrator audio:** JOW starts after "…through all this?" + "Mm-hmm"; JERM after the interviewer (≤ 15.0).
3. Beat 5 ends 1109.60 (< "I just wish…" 1110.1). Beat 3 ends before "because". Beat 6 hard cut on "this" (529.40).
4. **KAT subtitles:** cropped out (frame ends on row 784; the bar starts at 788). Never on screen with our captions.

## Log
- 2026-10-29 ~11:00: brief received; intake check; questions raised. JOW/JERM/PHM/OPRAH on disk, KAT not.
- ~13:10: his answers (sequencing in Premiere first, try yt-dlp, no music, Katherine-only crop). KAT + JERM downloaded.
- ~13:15–13:50: KAT ASR (beats at 241–253 / 507–532), edges by snippet re-ASR + level strips (`win/snip.py`,
  `win/variants.py`), offline A1 (`win/preview_a1.py`): dropped two non-words (PHM "people" tail, "um"), fixed 2.2 out.
  Framing: `framing.json` + `premiere/fix_framing.py` (KAT 250 % + keys, cover 204.55 %). Cover bug caught by the crop
  sheet (`-t` after `-i` truncated the retimed file to 1.40 s) → fixed (1.80 s); cover extended to 36.68 past the dissolve.
- ~13:55: placed v1 (58.82 s), verified; read-back A1 re-ASR → v2 edges. ~14:20: re-place blocked by an auto-save; Premiere
  froze ~14:30 and recovered (Affan: "we're back"). ~14:40: v2 re-placed (untouched check first), verified, 58.38 s.
