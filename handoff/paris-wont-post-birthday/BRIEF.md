# BRIEF — "Why Michael Jackson's Daughter Won't Post On His Birthday 💔" (Abundance Wisdom short)

## ▶ DIRECTION VIDEO (2026-10-24, wins over the written briefs where they differ)
Tella "Video Editing and Overlay Tutorial" (`brief/raw/guide.mp4`, 11:00; transcript `brief/guide_transcript.txt`; frames
`brief/frames/`). **The cut = HIS edit of v2**: ABW10 "Paris Birthday - raw cut v2", 31.50 s, dumped read-only to
`seqref/seq_his_v2.tsv` (V1 = face, **V2 = his overlay slots**, A2 = his reference music: **"Don't put any music"**).
He dropped beat 4 (GMA) and 4b (stage), cut 1b to "Social media… these days", beat 3 to "My childhood… / There was no
Christmas, no birthdays / No normal pleasures of childhood / I cannot recreate that part of my life".

| Seq time | Track | Words | Picture | Zoom / frame | Transition INTO it |
|---|---|---|---|---|---|
| 0.00–4.03 | V1 IG ×3 | "I don't post anything… kill myself" | Paris IG; clip 3 his 127 % reframe (face centred) | ONE layer, **in** | — |
| 4.03–8.00 | V2 slot | "Social media is apparently… these days" | **MJ smiling to camera at the Grammys, GREYED OUT** (`E:\Bullshit Folder\Drake\Michael Jackson Wins Best Pop Vocal Performance For 'Thriller' - GRAMMY Rewind.mp4`, no sunglasses ~2:52–2:58) | **letterbox, in** | **purple** |
| 8.00–10.03 | V1 IG | "Back when he was alive, he used to" | Paris | **in** | **cyan gaussian** |
| 10.03–12.23 | V2 slot | "hate anybody acknowledging his birthday, wishing him" | **Bashir face-palm, COLOUR** (`E:\…\Henry\Living With Michael Jackson 4K UPSCALE PART 3.mp4` from ~0:32.6) | **letterbox, out** | **purple** |
| 12.23–17.23 | V1 IG ×3 | "a happy birthday… when his birthday was" | Paris | ONE layer, **in** | ? (not named; his selection path suggests none or peach — ASK) |
| 17.23–20.17 | V1 MJ93 | "My childhood was completely taken away from me." | Michael, Grammy 1993 | **in** | **peach (exposure blur)** |
| 20.17–22.23 | V2 slot ×2 | "There was no Christmas, no birthdays" | **young Michael crying, MICHAEL (2026) movie** ("He looks very sad and terrified") = `E:\…\Henry\Jackson 5 Childhood Scene - MICHAEL (2026) Movie CLIP 4K.mp4` ~3:47 | **letterbox, out** | **purple** (a 2nd purple/peach called at the slot split 21.30 — ASK) |
| 22.23–26.27 | V1 MJ93 ×2 | "No normal pleasures of childhood. I cannot recreate that part of my life." | Michael | ONE layer, **in** | **cyan gaussian** |
| 26.27–27.83 | V1 JO (Jack, his continuous clip) | "My relationship is the most" | Jack (no jump: "Jack is fidgeting") | **in** | (not named) |
| 27.83–30.47 | V1 JO ×3 | "beautiful relationship ever… no one's business" | Paris | ONE layer, **in** | (not named) |
| 30.47–31.50 | V2 slot | "That was my best friend" | **photo of MJ with Paris as a toddler** (his pick: Pinterest, white dress; "enhanced version in my Higgsfield") | **FULL SCREEN (no letterbox), out** | **none**; **fade out at the end** |

- **Lip sync**: the IG clips are out of sync — he slipped clip 1's VIDEO +0.10 s vs its audio (V1 in 42.50 / A1 42.40):
  "do this for all the Paris bits". The JO clips are "a bit out of sync" too (measure, then slip video).
- **Head lock** on every face shot; overlays NOT tracked.
- No music. Grade = his AE stack. Captions/SFX/lower thirds not mentioned in the video → the written brief + house style.
- **Conflicts to settle with him**: (1) two overlays put a CHILD on frame (the movie's young-Michael actor; toddler Paris) vs the
  brief's hard rule B1.4 "No minors on frame"; (2) the best-friend photo: his Pinterest pick is not among the last 140 Higgsfield
  images; the enhanced MJ-with-Paris images there are the umbrella one (4K on disk: `projects/mj-skin-son-tyson/assets/stills/
  mj_umbrella_with_paris_4k.png`) and one with Prince (Higgsfield 09-29) — `brief/frames/best_friend_photo_options.jpg`;
  (3) the two unclear transitions above.

## ▶ STATUS: resume here (2026-10-24)
- His brief, verbatim: `brief/edit-brief.md` (🔒 FINAL, 23 Oct 2026, five beats, ≈42 s, source audio only).
- **His order (2026-10-24): "first you will sequence it in premiere then once i approve then you will start".** Stage 1 =
  the raw sequence in Premiere; NO code build, download or render of the short until he approves it.
- Waiting on: the four sources. YouTube is blocked on this PC (never bypass): he downloads them.

## Resolved
| Item | Resolution |
|---|---|
| Job | `projects/paris-wont-post-birthday/` |
| Stage 1 | Raw sequence in **ABW10** (the MJ-siblings precedent; confirm the open project before writing): cloned from an empty template, 1080×1920 **30 fps** (B3), bin "Paris Birthday", V1/A1 = the five beats cut by ear, V2 = the beat-4 photo slot, one marker per beat with the words + notes. Never saved by us. |
| Sources | AH `V9IIkf5sd74`, MJ93 `KLm8lmmIhiI` (backup `oP35JqC6tnE`), MJ08 `lLPgkxg33jw`, JO `-kXLpqK0MaM`. Expected in `E:\Bullshit Folder\Henry\` (his download folder). |
| In/outs | Transcribe each source once (WhisperX), lock every edge by ear (10 ms RMS + re-ASR of loud edges, the MJ-siblings lesson); the words win over the timestamps. |
| Beat 4 picture | An adult photo of Michael alone, 2008 (lock 1). A frame from the MJ08 package if it has one; never the kids' photos. |

## Points where the brief meets his standing rules (raise before the code build, not before the sequence)
1. **Captions** at 62–68 % of frame height (y 1190–1306) vs his rule "just under the lips, one constant position".
2. **No letterbox** (B3) vs the AW letterbox band used for low-quality sources. Brief is his: it wins unless he says otherwise.
3. **Full-bleed vertical crop + "don't punch past ~115 %"**: a 16:9 source cropped to 9:16 is already 178 %; the AH phone
   video sits inside a news package (likely pillarboxed). Measure on the downloads and tell him what 115 % can mean.
4. **Face cam ≤ ~4 s without an overlay** (his 2026-10-23 rule) vs beats 2 (~11 s), 3 (~10 s), 5 (~8 s) with no overlays.
5. **Music bed** −30 dB under beats 1–4, out under beat 5 (new for the code build; `audio.py` has no music path).
6. **SFX** not mentioned; the AW standard is a premium, varied Epidemic set at the MJ-siblings levels.
7. **Export**: brief says `Paris Birthday.mov` → `E:\…\Final Renders`; standing rule = `X:\Claude Projects\Exports\` only.
8. **Grade** = his AE stack (`finish.py` `grade_mode` 'ae' + sharpening), matching the S**CIDE / Katherine renders.
