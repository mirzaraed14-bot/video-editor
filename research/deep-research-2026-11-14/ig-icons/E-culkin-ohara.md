# Gate E for "She Forgot Him TWICE" (Culkin x Catherine O'Hara): the source files, checked (Sat 14 - Sun 15 Nov 2026)

Files are in `ig-icons/src/<id>/`; tools in `ig-icons/tools/` (`e_checks.py`, `finish_test.py`); images in `ig-icons/proof/`.
All checks ran silently (ffmpeg to pipes / `-f null`; nothing was played).

## 1. Television Academy `cOxmrVZr5WQ`, "In Memoriam: 78th Emmy Awards" (the ending): downloaded 23:47 PKT
- **Probe:** 634.6 s, H.264 1920x1080 @ 30 fps (1.51 Mb/s), AAC 44.1 kHz stereo 127 kb/s. First-party (the Academy's own
  upload of the NBC broadcast). Plays from Pakistan: yes (downloaded here).
- **Layout** (`proof/emmys_sheet.jpg`, every 6 s; `proof/emmys_tribute_sheet.jpg`, every 2.5 s over 0:24-4:24):
  - 0:00-0:24: the announcer and the walk-on.
  - 0:24-4:21: the tribute. Mostly a medium three-shot (Culkin left in a cream suit, Annie Murphy centre, Dan Levy right); wides;
    her photo on the screen (0:26, 0:56, 1:54, 2:49, 4:01); audience cutaways (Brenda Song at 0:47-0:48 and 1:01/1:26, and
    other guests).
  - 4:24-8:24: the reel, with Noah Kahan's song.
  - 8:30-10:18: Jamie Lee Curtis's part.
  - No children seen in the 6 s and 2.5 s sheets (the cutaways are adult guests). The spans the sequence uses were not checked
    frame by frame, which is how the Walk of Fame toddler was first missed.
- **His words by ear** (WhisperX large-v3 + alignment, `asr/emmys/transcript/words.json`; times are file seconds):
  - 18.55 "Hi." 20.65 "Catherine O'Hara."
  - **22.37-28.07 "We remember her as the forgetful mother, right? Yeah, but we'll never forget about her."** (Hook A; the ASR
    marks "We" and "as" low-confidence, and TV Insider prints the same line: two sources)
  - 28.09-39.30 "There are all kinds of words I could use to describe Catherine. She was encouraging. She was warm. She was funny,
    but the word that I think of is mama."
  - 40.63-46.02 "You know, she wasn't just a wife and mother to Bo and Matthew and Luke."
  - **47.50-49.96 "She was my mom. She was our mama."** (Hook B) 51.00-53.34 "And by extension, she's all of our mama."
  - 54.48-57.69 "By the way, call your mother tonight, for real." 58.99-60.99 "But, yeah, right? Give it to mom." (laugh)
  - **66.55-91.67 the close** (then "Thank you." 92.45-92.73, left out): "But like a good mama, she always showed up when I asked her to. Because that was Catherine.
    That's what she did. She showed up. And this is the best that we can do for her tonight. We're showing up for her. So she
    may have forgotten me [1.5 s] twice. [4.9 s of laughter and applause] But we will always remember her. Thank you."
  - **"Mama" or "mom":** the ASR hears "like a good **mama**" at p 0.72, and he says "mama" three more times in the speech (38.99,
    49.60, 53.02); TV Insider prints "like a good mom". The card reports both rather than calling the print wrong.
  - The "twice" timing is a comic beat: the 4.9 s laugh between 84.69 and 89.61 must be cut to under 2 s (Affan's rule for
    pauses inside third-party clips), keeping a breath of the laugh.
- **Audio** (`e_checks.py audio`):
  - His speech 18.5-92.8 s: **-30.4 LUFS integrated**, LRA 8.3 LU; noise floor (50 ms RMS, p10) -55.9 dBFS against speech
    peaks (p95) of -28.6 dBFS, about 27 dB of separation. The close alone: -32.7 LUFS. It needs about +10 dB of clean gain
    (nothing like the UCLA -47 LUFS case).
  - **No music under his voice.** Spectrograms `proof/emmys_spec_18-62.png` and `proof/emmys_spec_62-95.png` show room tone and
    two bursts of laughter and applause in the gaps, with no sustained tonal lines. The walk-on band (`proof/emmys_spec_02-22.png`,
    6-16 s) ends before his first word at 18.55.
  - Method note: the automatic gap test read "tonal" (spectral flatness median 0.08). The spectrograms show why: tilted room tone
    and speech reverb tails, not music. The spectrogram is the evidence; the flatness threshold alone misreads a hall.
- **Anchor test** (`proof/anchor_emmys.jpg`, 1:1 crops at delivery scale against the approved Prince ABC panels and Bieber's Oslo
  phone shot):
  - His face is 144 px wide in the source. In a full-screen 9:16 crop (x1.78) it is 256 px at delivery: clean, no blocking or
    noise, but softer than the AI-finished Prince panels (faces 517-564 px). A tighter punch-in (x2.5, 360 px) goes soft. Every
    raw tile is far above the Oslo phone shot.
  - This is Whitney's case (a 260 px face, passed after the Son recipe). The finish test on 2 s (Iris 1.0, then Proteus) is in
    `proof/finish_emmys/`: see section 3.

## 3. The anchor finish test (Emmys): PASS
- `tools/finish_test.py` under the GPU lock (23:56): t = 43-45 s, his face found at x437 (148 px), a 608x1080 crop scaled to
  1080x1920, then Iris 1.0, then Proteus prob-4 (details 0.6, blur 0.6): the Son build's ABC recipe, as Whitney's test.
- `proof/anchor_emmys_finish.jpg`: raw stage A (face 247 px) vs finished (253 px) vs the approved Prince ABC panels. The finished
  tile is crisp (beard texture, hair strands, eyes): the same AI-finished-TV class as Prince, with a smaller face, exactly
  Whitney's passing case. Far above Bieber's Oslo phone shot (`proof/anchor_emmys.jpg`).
- No Topaz watermark: `proof/finish_emmys_full.jpg` (the full 9:16 frame: Culkin head to knees in the cream suit, a sliver of
  Annie Murphy's dress at the right edge).
- Delivery note: full-screen 9:16 on him is the tightest framing that holds; a x2.5 punch-in goes soft (`proof/anchor_emmys.jpg`).

## 2. Access Hollywood `Z7-3xGyL_c0`, "Macaulay Culkin Tears Up Over 'Home Alone' Mom…" (the setup): downloaded 23:57 PKT
- **Download note:** the planned section (0:00-7:50) failed at 23:50. YouTube answered normally (page, player JSON, JS challenge
  solved); then ffmpeg got HTTP 403 on the googlevideo stream URL. That's ffmpeg's single unchunked request failing, not a bot
  page or a 429, so no flag was set. The full file came down through pace.sh on the native downloader (23:57). Lesson for the hub:
  `--download-sections` 403s on these player clients; full files for videos under ~15 min.
- **Probe:** 658.4 s, H.264 1920x1080 @ 29.97 fps (1.64 Mb/s), AAC 44.1 kHz stereo 127 kb/s. A press pool camera, edited by
  Access. Their chapters: 0:02 his speech, 3:10 thanking Brenda, 4:10 O'Hara's speech, 7:20 the two of them emotional, 7:42
  Natasha Lyonne.
- **Frames** (`proof/wof_sheet.jpg`, every 5 s; full frames `proof/wof_frame_0030.jpg`, `proof/wof_frame_0500.jpg`):
  - 0:00-4:10: him alone at the podium, medium close. He wipes his eyes at 0:30 and again near 3:55.
  - 4:15-7:40: O'Hara at the podium (left), with him standing beside her (right; sunglasses until about 4:50).
  - 7:35-7:45: the hug. 7:45-10:40: Lyonne. 10:45-10:58: Access end cards.
  - One static camera with no cutaways to the seated guests, **but a toddler in a teal coat, very likely his son, walks behind her
    during her closing lines**: behind her right shoulder at 441.5 s, by the tree at the podium's left at 448.5 s, and at the
    podium's left edge at 459.5 s (`proof/wof_child_zoom.jpg`, `proof/wof_minors_441-462.jpg`). The cold read caught it (Sun
    ~00:30); my earlier line here, "his children are never on frame in this file", was wrong. The fans behind the barricades are
    far and out of focus, but LESSONS (13 Nov) counts children in a fan crowd as a minors fail too, so every frame of a used span is
    checked at build.
  - **Access's logo is burned in at the bottom left** (about x100-430, y950-1020 of 1080). A 9:16 crop on O'Hara catches its right
    half in the bottom band (delivered y≈1690-1810, inside the bottom 300 px that stay background). A full-height 9:16 crop already
    uses every row, so it can't be lifted out; the fixes are the stacked split (its panels sit at y50-601), a blur patch, or the
    MaximoTV agency feed of the same speech (`iOEht-EvhFQ`, 4:22: a third download, on the hub's order).
    His tears at 0:30 crop clean of it.
- **Anchor test** (`proof/anchor_wof.jpg`, raw crops at x1.78): O'Hara 154 px src → 273 px delivered (t = 300, an earlier frame);
  his tears 215 → 382 px; him beside her 167 → 296 px (t = 300, in sunglasses); the hug (profile) 110 → 195 px. All far above the
  Oslo phone shot. My first "passes a fortiori" was wrong (the cold read): the split's faces (~225-240 px) and the hug sit under
  the Emmys raw tile, which itself passed only after the finish.
- **The finish test at the split's scale (Sun 00:35-00:43, GPU lock):** `tools/finish_test.py` on 2 s windows of the frames the
  sequence uses: her at 446.5 s (crop centred at x548), him beside her at 446.5 s, and the hug at 455.5 s (crop centred at x950),
  each 608x1080 → 1080x1920, then Iris 1.0, then Proteus prob-4 (the Son recipe). `proof/anchor_wof_finish.jpg`: her raw 235 px vs
  finished 225 px, him finished 231 px. Both finished faces are crisp (hair strands, beard texture): the AI-finished-TV class of
  Whitney's passing case, under the Prince panels' size. **PASS.** The hug is a profile with no measurable face; its finished
  frame is clean (`proof/finish_wof_full.jpg`, which also shows no Topaz watermark on any of the three).

## 4. The Walk of Fame words, by ear (WhisperX large-v3 + alignment, `asr/wof/transcript/words.json`; Access file seconds)
- **Her closing lines, 441.27-454.93 (the find of the night):** "Congratulations, you so deserve your star on the Hollywood Walk of
  Fame. And thank you for including me, **your fake mom who left you home alone not once but twice**, to share in this happy
  occasion. I'm so proud of you. God bless you." Then the hug (about 455-462; Access's chapter 7:20 "get emotional").
  - **The same joke in both voices:** in Dec 2023 she calls herself the fake mom who left him home alone "not once but twice"; in
    Sep 2026, after her death, he tells the same joke at her tribute: "So she may have forgotten me… twice. But we will always
    remember her." His "twice" pays off his own opening line that night ("We remember her as the forgetful mother, right?"); he
    never mentions her 2023 speech, so the card never says he answered her.
  - Word times for the cut (word starts to word ends): "And thank you for including me" from 445.53; "your fake mom" 447.01;
    "not once but twice" 448.68-449.62 (a 1.32 s pause follows, a laugh); "to share in this happy occasion" 450.94-452.46;
    "I'm so proud of you." 452.56-453.44.
- Her other stories (not needed for the arc; on file): the 1990 matinee, two boys running out: "it's okay, no, it's just the mom"
  (258.8-290.7); the attic scene, "I was not yet a mother at the time, and I had no idea the kind of things that would come out of my
  mouth with my own two sons" (349.6-389.1); "this beautiful, dear little 10-year-old boy, was called a superstar, a moneymaker…
  How does anyone survive that?" (393.6-410.5).
- His lines (Access's edit puts his speech first; at the ceremony it followed hers): "there's so many people that I love, and to feel
  that love back is just amazing, so thank you" (20.74-27.0), then a 9 s pause in which he wipes his eyes (the tears at 0:30), then
  "Catherine, Natasha, thanks for all your kind words and your stories and stuff" (36.14-41.26). He closes on "Merry Christmas, you
  filthy animals." (245.3-247.5): Home Alone's line in his own voice, a Christmas-peg option.
- **Audio:** her speech 252.5-455.0 is -20.1 LUFS integrated (LRA 10.6); her twice line -22.3 LUFS; floor p10 -44.5 dBFS against
  speech peaks of -17.8 dBFS (about 27 dB). An outdoor PA with traffic rumble under 100 Hz and crowd noise; **no music**
  (`proof/wof_spec_436-466.png`: harmonics in the words, broadband crowd and applause after "God bless you"). His opening:
  -27.4 LUFS, floor -55.7 dBFS.
- Censor: none in any span the arc uses. (Lyonne's later part names "the Michael Alig murders": not used.)

## 5. Other tellings of the join (YouTube Data API searches 9-11, from 00:01 PKT, `yt-api/s9-*.json` to `s11-*.json`)
- q = `"not once but twice" catherine o'hara`, all lengths, since 30 Nov 2023, by views: **7 videos, 18.5K views in total.** Top:
  Buzz Room "Macaulay Culkin on Catherine O'Hara's Death: 'I Owed Her a Favor'" 15.3K (6 s, 13 May 2026).
- Search 10 (00:38), `catherine o'hara fake mom home alone twice`: 11 videos, 111.2K. **WarumErfolg's German 63 s Short "Macaulay
  Culkins Abschied von 'Fake-Mama' Catherine O'Hara" (87.0K, 19 Sep 2026) is possibly the same joke**: its description names the
  film's two forgettings and his Emmys promise, not her 2023 speech; content unchecked, since no download was ordered for it.
- Search 11 (00:38), `macaulay culkin forgot me twice catherine`: 15 Shorts of the Emmys line, 566.5K in total (8 of them also in
  search 8; 13 are 4-6 s fragments, 2 run 76-82 s)
  (humanity restored 177.8K, VIRAL EMPIRE 166.2K, Cremingo Buzz "Forgotten twice, remembered forever" 22.2K).
- So: one possible telling (German, 87K), none found in English across 26 distinct results (search 9's 7 are all in search 10).
- New fact from it, verified in four outlets: in May 2026 Culkin told Gentleman's Journal "I felt that we had unfinished business" and
  "I feel like I owed her a favor – and I don't like having an outstanding debt" (Variety Australia, KATV/Sinclair, Spokesman-Review,
  Tribune). **None says what the favor was**, so the card quotes it and never says the Emmys tribute repaid it.
