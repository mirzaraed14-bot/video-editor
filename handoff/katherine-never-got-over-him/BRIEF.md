# BRIEF: "Why Michael Jackson's Mother Never Got Over Him 💔" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-29 ~21:15): v1 EXPORTED (both folders, QA PASS), waiting on his review
- Built in code from his re-cut + Tella direction 1 + band C at his pick 2 (375 px). RUN.md has the state, B9-REPORT.md
  the report. His next notes go in a § HIS REVIEW 1 below, change only what he names.

## (previous) STATUS (2026-10-29 ~17:30): HIS RE-CUT (30.87 s) + TELLA DIRECTION 1 resolved + band = C; waiting on his go
- He re-cut the raw sequence himself in ABW10 to **30.87 s / 14 clips** and recorded a Tella
  (`guide/guide.mp4`, "Video Editing Sequence and Caption Guide", 4:37). **His cut is now the spec** and supersedes the
  locked brief below where they differ (see § HIS DIRECTION 1). Never re-place over his sequence; build from it.
- **Band picked (17:30): C** = lift + the AW §4 dimmed 198 % fill at 43 % + glow line under the lifted Katherine/Joe picture.
- Open: the go for the code build (quoted ~3–4 % of the weekly cap), plus his by-ear answers (non-blocking; defaults
  below). Everything else is resolved below with my reading stated.

## HIS DIRECTION 1 (Tella 2026-10-29 16:28, `guide/guide.mp4`; transcript `guide/guide_asr.json`; frames `guide/tl`, `guide/pm`, `guide/tx`)
Resolved against his timeline (selection boxes + playhead timecode at each word). His sequence, read-only dump
`premiere/his_cut.tsv` (real out = inPoint + duration; the dump's outPoint column runs ~0.17 s long):

| # | Seq time | Clip | Source | Words (his A1 re-ASR, `win/his_a1.json`) |
|---|---|---|---|---|
| 0 | 0.000–1.600 | KAT_w238 | 249.600–251.200 | He should have been burying me. |
| 1 | 1.600–3.267 | KAT_w238 | 251.300–252.967 | I shouldn't have been burying my child. |
| 2 | 3.267–5.383 | JOW | 1886.233–1888.350 | She's taking it real hard. |
| 3 | 5.383–7.700 | JOW | 1889.283–1891.600 | You start talking about Michael, she starts crying. |
| 4 | 7.700–12.250 | JERM | 44.367–48.917 | When I called my mother back, I heard the most horrible tone in her voice when she said, he's dead. |
| 5 | 12.250–14.700 | JERM | 53.117–55.567 | I've never heard this tone in her voice, but [for] her to say this. **(he extended: +"but her to say this")** |
| 6 | 14.700–16.117 | JERM | 84.050–85.467 | I go straight to my mother and I |
| 7 | 16.117–17.133 | JERM | 85.850–86.867 | consoled her. |
| 8 | 17.133–18.483 | JERM | 87.150–88.500 | And still to this day, she don't |
| 9 | 18.483–20.050 | JERM | 88.817–90.383 | even remember me hugging her **(+0.16 s: the "be-" of "because", 90.22–90.36, voiced)** |
| 10 | 20.050–22.733 | OPRAH | 1106.917–1109.600 | My mother's wonderful. To me, she's perfection. |
| 11 | 22.733–24.300 | KAT_w505 | 512.000–513.567 | Every morning that I wake up, |
| 12 | 24.300–25.883 | KAT_w505 | 515.633–517.217 | my baby's on my mind. |
| 13 | 25.883–30.867 | KAT_w505 | 524.783–529.767 | Oh gosh, I'm sorry. [pause] I'm sorry. I don't [/ I'm sorry], I didn't intend to do this. [0.37 s room tone] |

**What his cut drops from the locked brief:** beat 1's "The worst thing in the world is to lose a child"; beat 2's Larry
King line and "harder than I ever seen"; **all of beat 4** (Michael, Copenhagen) and with it the Katherine cover; beat 6's
"Even this morning" + its protected pause; the hard cut on "this" (now a fade-out); the 60–65 s runtime (now 30.87 s);
every label/card ("this will have no overlay, the footages themselves are more than enough").

**His notes, resolved:**
1. **No overlays**, no labels, no cards.
2. **Captions in the middle** (closes open question 5): the line of the last shipped AW short, **y≈1058** (Janet).
3. **"Bump Katherine's face up, she's more upward in position… same with Joe Jackson"**: lips just above the caption line
   (≈ y955). Measured in his framing (`win/lips_his.py`): KAT lips y1325–1355, Joe y1405–1437, Oprah y1075, Jermaine
   y670–725 (already above). Lifting KAT ~350 px exposes her burned-in subtitle bar at the bottom; lifting Joe past his
   picture needs the 115 % cap (204.5 %) and still leaves ~350 px at the bottom. Test frames: `proof/lift_options.jpg`
   (A now · B lift + black band · C lift + AW §4 dimmed 198 % fill + glow line). **He picked C (2026-10-29 17:30)**, then band size pick 2 (18:10): the ~375 px band of the test (edge y1545) for
   Katherine + Joe, lips clear while upright, the caption meets the mouth only in her bows / Joe's lowest moment
   (`proof/lift_choice.jpg`; pick 1, lips clear in every frame, needed 560–585 px). Oprah: ~194 %
   (109 % of fill) lifts Michael's lips to the line with no band.
4. **Zoom layers** (AW §3, one adjustment layer per group; push-ins unless noted):
   Z1 clips 0–1 (KAT, "these two… one zoom-in layer") · Z2 clips 2–3 (Joe, "same goes with this one") · Z3 clips 4–7
   (JERM, "all these four bits will have one") · Z4 clips 8–9 (JERM, "these two will have their own") · Z5 clip 10
   (Oprah, "this will have zoom-in as well") · ending: clips 11 and 12 push in ("when it's zooming in here", both
   selected), **clip 13 starts in and very smoothly zooms out** ("zoom in and then very smoothly zoom out, put emphasis
   on the fact that she's tearing up"), letting her pause run, then **fade out** after "I didn't intend to do this".
   ~~My reading of "these three will have their own zoom-in layers": 11 and 12 one layer each, 13 the pull-out.~~
   **Build reading (re-read at go, 17:55):** "these three will have their own zoom in layers, well but what we are going
   to do here… my baby's on my mind, so zoom in and then very smoothly zoom out" = the three KAT_w505 clips get their
   own layers apart from Oprah's: ONE push-in across 11–12 (one camera, the jump cut at 24.30 must not reset the zoom:
   memory "no same-camera punch-ins"), then clip 13 starts at that depth and pulls out with an easy ease, under the
   peach exposure fade at 25.883.
5. **Transitions** (AW §7 label colours):

   | Cut | Between | His words | Build |
   |---|---|---|---|
   | 3.267 | KAT → Joe | "this is gonna be purple fading into this" | Purple: brightness dip −90 |
   | 7.700 | Joe → Jermaine | "purple fading into this" | Purple |
   | 17.133 | JERM Z3 → Z4 ("consoled her" → "and still to this day") | "dark green fading into this" | Dark Green: +30 flash |
   | 20.050 | Jermaine → Oprah | "this will be purple fading into this" (Oprah selected on "into this"; clip 8 was still selected from before — read as the cut INTO Oprah, not 18.48) | Purple |
   | 22.733 | Oprah → KAT | "this will be dark green fading into this" | Dark Green |
   | 25.883 | "my mind" → "Oh gosh" | "a slight exposure fade again here when it's zooming out… an exposure fade effect as well" (playhead parked at 25:59 for both mentions = one transition) | **Peach: uni.Exposure Blur, slight** (Mix ≤ 50 → 0) |
   | end | — | "then we're just gonna fade out" | fade to black after "this", audio tail with it |

6. **Caption colours (recurring, now in the AW README §8 + LESSONS):** the last few shorts were only white + red; use a
   MIX across the short: white is constant, **one** accent colour per caption (never two accents in one caption):
   pink = love/affection · yellow = happiness/sunshine · red = evil/bad · blue = mellow/emotional · green = very positive ·
   orange in the mix too.
7. **Note 2 (chat, 2026-10-29 ~17:40): "The silent pause where Katherine is crying you will put a caption of quote
   unquote tears up."** Measured on his A1 (`seqref/a1_his.wav`, 50 ms RMS): after "Oh gosh, I'm sorry" (ends 27.08) a
   breath runs to ~27.30, then room tone (−43 to −49 dB) **27.35 → 28.15**, then she speaks again ("I'm sorry", voiced
   from 28.15; the re-ASR's 27.86 start is early). That 0.8 s is the only silence inside clip 13. **Build:** a caption
   card **"tears up"** (quote marks shown, as dictated; the AW §8 rule allows quotes) from **27.30 → 28.15** (frame-snapped),
   at the same y≈1058 line and caption style as the speech; the accent goes on "tears" in **blue** (mellow/emotional), "up"
   stays white. It ends where "I'm sorry" begins, with no gap and no overlap. It covers the start of the clip-13 zoom-out,
   which he described as "put emphasis on the fact that she's tearing up".

**My bug, to fix in the build:** clip 9 (JERM 88.82–90.38) is framed on the cabinet + his hand (Position x −0.1976, my v2
placement: the face detector picked the wrong side; Jermaine sits at x≈0.20–0.30 in that shot). v2's verify compared the
read-back to the plan, not to frames.

**Defaults stated to him (change with a word):** the fade-out fits the 0.4 s of room tone he left after "this" (ends
30.36 in his cut; source clean to ~530.4, so a longer fade means letting the tail run past his out). The lift puts
Katherine's forehead / Joe's brow at or above y200, and the push-ins (pivot on the lip line) crop a little more at the top;
the build aims the LOWER lip just above the caption (the Joe test panel aimed the mouth corners, so its caption sits on his lip).

**For his ear (captions follow the audio):** JERM "this tone in her voice, but [for] her to say this"; the "be-" now at the
end of clip 9; KAT "I don't" vs "I'm sorry" before "I didn't intend"; "baby's" (contracted, per the joined re-ASR).

## Catalog pass (CLAUDE.md learning loop: required before any edit)
Done 2026-10-29 ~17:50: all 151 lines of `research/effects-catalog/CATALOG.md` read and all 137 stills looked at (sheets
`../janet-couldnt-cry/win/cat/cat_0-6.jpg`, made 2026-10-28; neither the catalog nor `shots/` has changed since 10-08).
He ruled out every overlay ("the footages themselves are more than enough") and named every zoom and transition, so the
catalog only shapes HOW those land and adds nothing on top.
- **Fits, used inside his direction:**
  - FX-40 Slow-Burn Portrait → his zoom-in groups on the four tight faces (slow creep, the caption the only text).
  - FX-40 reversed on clip 13: the take starts pushed in and slowly pulls out while she breaks down, the "tears up" card
    on the silence, then the fade (his "emphasis on the fact that she's tearing up").
  - FX-29 Float Frame → his pick C: the lifted Katherine/Joe picture over the AW dimmed fill + glow line (not black bars).
- **Fits, held back (his look is set):** FX-78 Cinema Vignette Montage (no added vignette on the ending; his grade
  only); FX-37 Ghost Dissolve and FX-80 Black-Beat Ident (he named every transition, and the end is his fade-out);
  FX-42 Kin Tag (no labels, his call); FX-58 Speaker-Coded Subs (AW captions are locked; his colour mix only).
- **New to the channel here:** a stage-direction caption ("tears up") on a wordless beat; one take that zooms in, then out.
- **Doesn't fit a 31 s face-only short:** maps, charts, documents, host sets, CG, chapter cards, CRT/phone props, archive
  inserts, stepped motion (FX-01–39 except 29, FX-41–77 except 40, FX-79, FX-81).
- **What the last one leaned on (Janet Couldn't Cry):** four moving overlays, a letterboxed BET insert over a blurred
  fill, label transitions, white + red captions at y1058. **This one is better by:**
  - the caption colour MIX (white + one varied accent per caption), the first AW short built on it;
  - every face measured so the lips sit just above the caption line (Janet was moved after his review; this one is
    measured before the first render);
  - the ending is one continuous take, zooming in and then out, with a fade, instead of a hard cut;
  - the wordless crying beat is carried by a caption rather than covered.

## (previous) STATUS (2026-10-29 ~14:30): RAW SEQUENCE in ABW10
- His answers 2026-10-29: sequencing in Premiere first · yt-dlp worked for KAT + JERM · no music · Katherine-only crop.
- "Katherine Never Got Over Him - raw cut" in ABW10: **58.38 s**, placed + verified 14:45 (v2). Next: his pass +
  direction → catalog pass → code build.
- KAT subtitles (§2): **no clean original found** (web search for both quotes) → **covered by the vertical crop**: KAT is
  framed at 250 % so the frame ends on source row 784; the bar is rows 788–939, so it is never on screen.
- Over-65 s list: **none used** (all words in = 58.4 s). Questions 5 (caption height) and 6 (runtime) stay open for the build.

## Open with Affan (asked 2026-10-29; 1–4 answered, see RUN.md § His answers)
1. **Music.** §5 asks for a soft piano bed at −30 dB under beats 1–5. Your 2026-10-27 rule is that AW code-built shorts ship
   with no music (Flex: no music, SFX stay). Default: **no bed**, SFX kept. Does that hold here?
2. **KAT + JERM download.** KAT is not on disk. `E:\Bullshit Folder\Lonely\Katherine Jackson Finally Speaks Out - Rare
   Details About Michael's Death.mp4` has the same pink suit (possibly the same session, late 2011 after the Murray
   verdict; its set is warm wood + sunflowers, not dark), but none of beat 1 or beat 6's lines, and burned-in subtitles too.
   Web search for both quotes found no clean original (only Dateline 2010, Piers Morgan 2012, Oprah 2010 hits). JERM IS on
   disk but only as an 854×480 SnapYT rip: full-bleed 9:16 = a 270 px column blown up ~4×. Janet's sources came down with
   the brief's plain yt-dlp commands after your "you try" (no cookies). Try the KAT and JERM lines the same way, or will
   you drop the files in? (JOW on disk is 1080p despite its "4K" name; fine as is.)
3. **Route.** Raw sequence in ABW10 first (Janet, Joe: your re-edit + Tella direction, then the code build), or straight
   to the code build from this brief?
4. **Beat 4 picture.** The only Katherine home video in that PHM passage (1988 backstage, 25:05–25:13 and 25:16–25:18) has
   Shannon and a face-blurred person beside her: the shot §3 bans at 25:10. 25:18–25:20 shows her tiny in a corner behind
   Michael's legs. Options: (a) a Katherine-only 9:16 crop of the 25:16 shot, (b) another adults-only Katherine clip
   from elsewhere in PHM (full-transcript scan running), (c) Michael on camera throughout. The concert-crowd shot under
   "sea of people / her eyes were watering" (25:32–25:36) is not in the brief's picture list and a crowd cannot be cleared
   of minors, so it stays off screen.
5. **Caption height.** §6 says ~62–68 % (y1190–1306). Your Janet review moved the line to y1060 ("the caption should be
   here"), and your approved finals sit at y940–1129. Your line or the brief's %? It also decides KAT's subtitle bar: a
   tight crop can push the bar off frame, otherwise a black band under our captions.
6. **Runtime fallback.** After all three listed trims it is ~63 s + Katherine's beat-6 pause (and the "…" after "my mind"
   may hold a second crying gap). If it is still over 65 s, which goes next? Measured candidates: (a) B3 start on "I heard
   the most horrible tone" (drop "When I called my mother back", −1.1 s); (b) B4 drop "she was on the side of the stage"
   (−1.2 s); (c) B4 drop "we were in Copenhagen" (−2.0 s); or (d) allow > 65 s.

## Found at intake (for the B8 report)
- **Beat 2 is two 2009 interviews** joined by the detail.'s edit (the brief's words span both, so no choice, but it is not
  one "2009 interview"): "She's taking it real hard… she starts crying, you know" = the home interview (black hat,
  close-up, the interviewer's question just before); a ~1 s cutaway (31:31.6–31:32.5); "Katherine is taking it very, very
  hard… harder than I ever seen her take anything" = **Larry King Live** (beige jacket, lips match the words). Larry King
  fills the left half 31:32.6–31:36.3 → crop to Joe's half. Trim 3 would join the two interviews mid-sentence (picture
  jump black → beige).
- **Words as heard** (captions follow the audio): JOW "She's **taking** it real [uh] hard", "Katherine **is taking**";
  JERM "I've never heard this tone **in her** voice"; PHM "her eyes were **watering**", "in Copenhagen **I think**",
  "dreamt that you would, you could, you would do this, you would have this kind of effect on an audience **like this**".
- **Runtime** (speech spans, joins ≤ 0.15 s): beats 2–5 measured **52.7 s** (B2 13.7 · B3 12.4 · B4 24.3 · B5 2.3).
  KAT estimated ~23 s + her beat-6 pause → **~76 s + pause** untrimmed. Trim 1 ≈ −2.1 s, trim 2 ≈ −2.2 s, trim 3 ≈ **−8.7 s**
  (not −4). All three → **~63 s + her pause**: it fits 65 s only if her pause is ≲ 2 s. Final number after KAT is measured.

---

## AFFAN'S LOCKED BRIEF (verbatim, received 2026-10-29)

# EDITOR BRIEF: "WHY MICHAEL JACKSON'S MOTHER NEVER GOT OVER HIM 💔"
**Channel:** Abundance Wisdom · **Format:** YouTube Short, 1080×1920 · **Locked:** 29 Oct 2026

The creative is locked. Your job is to cut it exactly as written. **If anything can't be done exactly as written, stop and tell Affan before improvising.**

**What this Short is:** Katherine Jackson's love for Michael, and his for her:
1. Her worst sentence.
2. Joe: she's never taken anything this hard.
3. Jermaine: the moment she said "He's dead".
4. Michael: his mother crying side-stage, and "To me, she's perfection".
5. Katherine breaks on camera: "Every morning that I wake up, my baby is on my mind… I'm sorry."

**Target runtime: 60–65s (hard max 65s), measured on the timeline.**

---

## 1. HARD RULES (any one broken = redo)
1. **Someone is speaking at every moment.** No gaps over ~0.25s. **One exception:** Katherine's own pause inside beat 6. She's holding back tears, so leave it in.
2. **Source audio only.** No voiceover, TTS, AI voices or AI faces.
3. **Exact words only.** Trim filler inside a range. Never splice to change meaning. **The only approved reorder is beat 1** (two of her consecutive sentences swapped).
4. **Voices allowed:** Katherine, Joe, Jermaine, Michael. **No interviewers, presenters or narrators.** (JOW is a compilation with a narrator; take Joe's voice only.)
5. **No minors on frame.** No childhood photos of Michael, and no children in any home video or memorial footage.
6. **Hard cut on "I didn't intend to do this."** No end card, no music tail.
7. **Caption only what's spoken.** Don't add names or dates that aren't said.

---

## 2. SOURCES (download first)
```
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "KAT_Katherine_studio.%(ext)s"    https://www.youtube.com/watch?v=yL39PTF-xmk
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "JOW_Joe_own_words.%(ext)s"       https://www.youtube.com/watch?v=tFC0bg3tlPQ
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "JERM_Jermaine_2011.%(ext)s"      https://www.youtube.com/watch?v=dL5h3zdrGJY
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "PHM_Private_Home_Movies.%(ext)s" https://www.youtube.com/watch?v=-L1R3qTolKA
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "OPRAH_1993_4K.%(ext)s"           https://www.youtube.com/watch?v=jKlqIh4STt8
```
| Code | Title · Channel · Date | Use |
|---|---|---|
| KAT | *Katherine Jackson breaks her silence about Michael Jackson's death* · MJ Classified · 24 Feb 2024 (studio interview, pink suit, dark set, c. 2010–11) | Beats 1, 6 |
| JOW | *My Son, Michael Jackson \| Joe Jackson In His Own Words* · the detail. · 21 Aug 2025 | Beat 2 (Joe's voice only) |
| JERM | *Jermaine Jackson on the Death of Michael Jackson* · hudsonunionsociety · 2011 | Beat 3 |
| PHM | *Michael Jackson - Private Home Movies (Full Version)* · RΔҒΔΣL · 2003 Fox special | Beat 4 |
| OPRAH | *Michael Jackson - OPRAH WINFREY Interview (1993) 4K 50FPS UPSCALE* · CINEKYD MEDIA | Beat 5 |

- Export every range with **±3s handles**.
- **The timestamps come from YouTube captions and can drift 1–2s. Lock every in/out point by ear.** The words win over the timestamps.

### ⚠️ KAT has burned-in subtitles
The MJ Classified upload has a black subtitle bar at about 70–85% of frame height.
1. **First, look for a clean original** of this Katherine interview: search YouTube/Google for the exact quotes "every morning that I wake up, my baby is on my mind" and "he should have been burying me". Same pink suit, same set.
2. **If there's no clean copy:** set the vertical crop so the bar sits under our caption plate, or cover it with a solid black band and put our captions on top. **There must never be two sets of subtitles on screen at once.**
3. Report which option you used.

---

## 3. THE SEQUENCE (cut exactly in this order)

### BEAT 1: HOOK (Katherine)
- **Source:** KAT · **~4:08 → 4:17**, then **~3:58 → 4:07** (**reordered on purpose**)
- **Words, in this order:** "He should have been burying me. I shouldn't have been burying my child." / "The worst thing in the world is to lose a child."
- In the source she says the second sentence first. Cut "He should have been burying me… my child" to the front, then "The worst thing in the world is to lose a child." Smooth the joins with a 2–3 frame crossfade.
- **Picture:** Katherine, tight. Frame 1 is her face.
- **On screen:** label **KATHERINE JACKSON · HIS MOTHER**
- **Red words:** HE SHOULD HAVE BEEN BURYING ME · THE WORST THING IN THE WORLD

### BEAT 2: JOE
- **Source:** JOW · **~31:26 → 31:41**
- **Words:** "She's taken it real hard. You start talking about Michael, she starts crying… Katherine has taken it very, very hard… she's really, really taking it harder than I ever seen her take anything."
- Start on Joe's voice, **after** the interviewer asks "How's Katherine been holding up…". **No narrator audio.**
- **Picture:** Joe on camera (2009 interview).
- **On screen:** label **JOE JACKSON · HER HUSBAND · 2009**
- **Red words:** SHE STARTS CRYING · HARDER THAN I EVER SEEN

### BEAT 3: JERMAINE
- **Source:** JERM · **~0:42 → 0:52**, then **~1:19 → 1:30**
- **Words:** "When I called my mother back, I heard the most horrible tone in her voice when she said, 'He's dead'… I've never heard this tone of voice…" / "…I go straight to my mother, and I consoled her, and still to this day she don't even remember me hugging her."
- Stop right after "hugging her". Don't run into "because she was such in the day…" or anything about Randy.
- **Picture:** Jermaine on camera.
- **On screen:** label **JERMAINE JACKSON · HER SON**
- **Red words:** THE MOST HORRIBLE TONE · DON'T EVEN REMEMBER ME HUGGING HER

### BEAT 4: MICHAEL, COPENHAGEN
- **Source:** PHM · **~25:24 → 25:52** (trim inside). **Start on "I remember one thing my mother said to me".** Don't use anything from 25:10, because it shows another person.
- **Words:** "I remember one thing my mother said to me. We were in Copenhagen… there was just a sea of people… and her eyes were watery. She was on the side of the stage, and I said, 'Mother, what's wrong? Why are you crying?' She said, 'When you were a baby, and I was holding you in my arms, I would have never dreamt you would have this kind of effect on an audience.' And I gave her a hug…"
- **Picture:** Michael on camera (2003, red theatre seat), then the PHM home video of **Katherine** backstage. **Adults only.**
- **On screen:** card **MICHAEL · ABOUT HIS MOTHER**
- **Red words:** WHY ARE YOU CRYING · HOLDING YOU IN MY ARMS · I GAVE HER A HUG

### BEAT 5: MICHAEL, "PERFECTION"
- **Source:** OPRAH · **~18:25 → 18:30**
- **Words:** "My mother's wonderful. To me, she's perfection."
- **Cut before "I just wish I could understand my father."** That line must not be in.
- **Picture:** Michael at Neverland, 1993.
- **Red words:** SHE'S PERFECTION

### BEAT 6: ENDING (Katherine)
- **Source:** KAT · **~8:23 → ~8:50**
- **Words:** "Even this morning… every morning that I wake up, my baby is on my mind.… Oh gosh, I'm sorry. I'm sorry. I didn't intend to do this."
- **Keep her pause** between "even this morning" and "every morning" (see rule 1).
- **Picture:** Katherine, the tightest frame of the video, with a slow push-in (100→110%).
- **Red words:** EVERY MORNING · MY BABY IS ON MY MIND
- **HARD CUT on "I didn't intend to do this."**

---

### If you're over 65s, cut in this order
1. Beat 3: drop "I've never heard this tone of voice" (−3s).
2. Beat 4: drop "there was just a sea of people" (−3s).
3. Beat 2: keep only "You start talking about Michael, she starts crying… harder than I ever seen her take anything" (−4s).

---

## 4. PICTURE
- **1080×1920, 30 fps**, full-bleed vertical crop on each speaker. No letterbox, no blurred fill.
- **Grade:** warm, matched to the recent MJ-family Shorts (`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`). Level-match the four eras (1993, 2003, 2009, 2011).
- SD sources (PHM, JOW 2009, JERM): light sharpen, grain-match, **don't punch past ~115%**.
- Labels: small, top third, ~2s, and only on each speaker's first appearance.

## 5. AUDIO
- **−14 LUFS integrated, true peak ≤ −1 dBTP.**
- **Music:** one soft, sad piano bed at about −30 dB under beats 1–5. **Pull it out completely under beat 6.** Katherine plays dry.
- 2–4 frame crossfades on every dialogue cut (especially the beat 1 reorder).

## 6. CAPTIONS
- Word-by-word, burned in, in the same style as the recent MJ-family Shorts, at ~62–68% of frame height. Red words as listed per beat.
- Caption exactly what's said, including "she don't even remember" (Jermaine's grammar).
- **Safe zones:** no text in the bottom ~20% or right ~12%.
- **Cover KAT's burned-in subtitles** (see Section 2).

## 7. EXPORT
- H.264 (≥20 Mbps) or ProRes 422 .mov, 1080×1920, 48 kHz.
- File: **`Katherine Never Got Over Him.mov`** → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`

## 8. QA CHECKLIST (tick every box before export)
- [ ] Beats 1 → 6 in order.
- [ ] Beat 1 opens on "He should have been burying me", reordered as written.
- [ ] Only Katherine, Joe, Jermaine and Michael are heard. No narrator from JOW, no interviewer.
- [ ] Beat 5 stops before "I just wish I could understand my father."
- [ ] No child on frame anywhere.
- [ ] KAT's subtitle bar is never visible together with our captions.
- [ ] Katherine's pause in beat 6 is kept; hard cut on "I didn't intend to do this."
- [ ] Runtime ≤65s on the timeline.
- [ ] −14 LUFS, true peak ≤ −1 dBTP.

## 9. REPORT BACK TO AFFAN
1. Final runtime.
2. The exact in/out points used per beat (file + timestamps).
3. KAT subtitles: clean original found (link), or covered?
4. Any trims used from the "over 65s" list.
5. Anything that didn't match this brief.
