# BRIEF: "Why Janet Jackson Couldn't Cry For Michael 💔" (Abundance Wisdom short, MJ × Janet)

## ▶ STATUS: resume here (2026-10-28 ~23:40): HIS REVIEW 1 applied (§ HIS REVIEW 1) → the review-1 export (`janet_v3_60.mp4` → `Janet Couldnt Cry.mov`; the file he reviewed = `Janet Couldnt Cry (v2).mov`); state in RUN.md
- Built from his re-edit (38.83 s) and his Tella direction (§ below); report `B8-REPORT.md`; state + re-render recipe RUN.md.

## HIS REVIEW 1 (Tella 2026-10-28 "Video Editing Revisions 🎬", 1:35)
Source: https://www.tella.tv/video/affans-video-bmmv4x8b → `brief/review1/guide.mp4` (stream URL from the page HTML, never
opened in a browser; his voice is quiet, −20.9 LUFS, transcribed from a dynaudnorm copy `guide_boost.wav`), transcript
`brief/review1/guide_words.json`, frames `brief/review1/frames/` (cursor crops `cur_*.jpg`). He reviewed the v1 export in
Premiere ("Janet Couldnt Cry - new cut"), playhead at 00:00:00:00 on the WR hook.
- **"only two revisions"**:
  1. **"the caption should be here where I'm placing my mouse"** (0–8 s): his cursor tip hovers on the hook's nostril line,
     tella y≈553 in a monitor spanning y89–930 → export **y≈1060** (v1 caption centre 1270.5) = **up 210 px**.
  2. **"drag this Janet Jackson footage up so the captions don't sit on her eyes ... or a bit more so it still sits under
     her lips with the new caption positioning"** (26–50 s, on screen: the BET letterbox) + **"same goes with this Michael
     Jackson footage"** (60–75 s: his video message) + "all of these things are placed too low just because the captions
     are themselves placed too low".
- **"we're pretty much good to go ... don't make any major changes, don't do complete renders, be as lean as possible."**
- **Resolved:** caption_shift −220 → −10 (measured caption centre y1058.5 on the hook still); BET (B1–B7) and Michael's
  message (M1–M2) lifted 210 px as an exact finish-side shift of the reviewed picture (`lift`), bands [483,1241] and
  [506,1410], their zoom pivots 1190 → 980, the BET AWARDS card y0 430 → 220 (same gap to the band, ink top y249). Full-bleed
  close-ups, overlays, cards otherwise, audio, captions text, Topaz picture: unchanged. One finish render, no Stage A/Topaz.

## (previous) STATUS (2026-10-28 ~19:00): HIS DIRECTION VIDEO RESOLVED → code build next
- His Tella (6:37, "you can now get to work") is resolved into § HIS DIRECTION below; his re-edit of the raw cut (38.83 s)
  is the cut. Next: catalog pass (§ Catalog pass) → overlays sourced + checked at full size → code build (copy
  `projects/joe-jackson-appointment/build/`, read its paths from `sources.json` `raw`, never the `seq_src/` proxies).
- Cost (unchanged quote): code build ~4–5 % of the week (~$90–120); Higgsfield only if an overlay is soft (ask first).

## HIS DIRECTION (Tella 2026-10-28 "Affan's video", 6:37 — wins over the brief)
Source: https://www.tella.tv/video/affans-video-e58hgmo0 → `brief/tella/guide.mp4` (stream URL from the page HTML, never
opened in a browser), transcript `brief/tella/guide_words.json`, deictics `brief/tella/deictics.txt`, his timeline read at
every "this" (`brief/tella/frames/ov_*.jpg` overlays/zooms, `tc_*.jpg` + `amb_*.jpg` transitions).
**His sequence = the cut** (`seqref/seq_his.tsv`, read-only dump of ABW10 "Janet Couldnt Cry - raw cut" 2026-10-28 ~18:30):
**38.83 s**. He REMOVED beat 3 (ABC09 "protective shield") and beat 4 (the WR book reading), and ENDS on Michael's own
video message to Janet (`E:\Bullshit Folder\Canelo\Michael's video message for sister Janet.mp4`, 640x480 29.97, 18.3 s):
"I love you, and I am honored and proud to be your brother." His A1 re-ASR'd clip by clip (`win/his_a1.py`,
`seqref/his_a1.wav`): every word whole, no repeats. Overlay slots = the clips he lifted to V3. Real clip outs =
inPoint + (end − start) (the dump's outPoint carries place_sequence's +0.2 s over-trim).
Transition colours = his AE labels (`transition_pass.py`): purple = brightness dip to −90 · dark green = brightness +30 ·
peach = Exposure Blur 50 → 0 · cyan = Gaussian Blur 50 → 0. Each sits on the cut at the END of the clip he selected.

| His tl (s) | Words | Picture (his words) | Zoom (one adj. layer per group) | Transition at the end |
|---|---|---|---|---|
| 0–3.017 (V1 0–1 + V2 WR) | "Out of everyone in my family, I never had that moment / to cry" | Janet CU (WR close-up over DL's wide): **"head tracked, full screen"** | zoom IN (both, one layer) | **purple** at 3.017 |
| 3.017–4.65 (V3 0) | "about his death." | **OVERLAY: Michael smiling, GREYED OUT, letterbox** | zoom OUT | **purple** at 4.65 |
| 4.65–10.117 (V1 2–4) | "I don't know if it was / trying to shield the pain / or just trying to hold it all together because I saw" | Janet CU | zoom IN (all three, one layer) | **dark green** at 10.117 |
| 10.117–12.70 (V3 1) | "that everyone else around me was falling apart." | **OVERLAY: Katherine Jackson crying, 60 Minutes (Australia): she takes a tissue and wipes her tears; letterbox, REGULAR COLOURS (not grey)** | zoom OUT | **purple** at 12.70 |
| 12.70–18.117 (V1 5–9) | "My entire family / wanted to be here tonight / but it was / just / too painful." | BET: **letterbox ("too low quality… push it out like this"), blurred background, NO head tracking** | zoom IN (all five, one layer: "these four bits") | **peach** at 18.117 |
| 18.117–20.60 (V3 2–3) | "To you, / Michael is an icon." | **OVERLAY: Michael "aura": Bucharest 1992, he pops out of the stage and just stands there; or a higher-quality shot with the same effect** | zoom OUT | **purple** at 20.60 |
| 20.60–23.25 (V1 10–11) | "To us, / Michael is family." | BET (letterbox as above) | not said → zoom IN (default) | **dark green** at 23.25 |
| 23.25–24.50 (V1 12 + V2 WR) | "I was in Paris" | WR Janet CU over DL's childhood montage (lock 1) | not said → zoom IN | **cyan** at 24.50 |
| 24.50–26.817 (V1 13) | "and I just spent the night just watching" | DL (Meredith from 1591.133) | zoom IN | none (not named) |
| 26.817–29.517 (V1 14–15) | "all his videos / listening to his music" | Janet CU | zoom IN (both, one layer) | **purple** at 29.517 |
| 29.517–32.317 (V1 16–17 + V2 WR 3–4) | "And there were moments when I / felt to cry and moments that made me…" | WR Janet CU | zoom IN (both, one layer) | **purple** at 32.317 |
| 32.317–34.067 (V3 4) | "…laugh" | **OVERLAY: Grammy footage, Michael + Janet together and happy (1993 Grammy Legend), letterbox** | zoom OUT | **cyan** at 34.067 |
| 34.067–35.75 (V1 18) | "It was good for me. I needed it." | Janet CU | zoom IN | **purple** at 35.75 |
| 35.75–38.833 (V1 19–20) | Michael: "I love you, / and I am honored and proud to be your brother." | Michael's video message, **letterbox** | one zoom IN (both) | end (not said) |

Not in the video (set Part B defaults apply): word-by-word captions with red words, the beat-1 lower third, cards (BET
AWARDS · 3 DAYS AFTER HE DIED; MONTHS LATER · PARIS; the book card went with beat 4), grade matched to the recent MJ
finals, −14 LUFS / ≤ −1 dBTP, SFX, **no music bed** (his call), 1080x1920 30 fps export.
Overlay sources found on disk (2026-10-28): Bucharest "Jam" opener 4K60 `E:\Bullshit Folder\Lonely\Michael Jackson - Jam -
Live in Bucharest October 1st, 1992 (4K60FPS).mkv` (+ full concert `KIDS\…Live In Bucharest (The Dangerous Tour).mp4`,
`Michael Jackson Super Bowl 1993 [SNIPPETS IN HD].mp4`); Grammys `Henry\1993 'Grammy LEGEND' Award - Restored.mp4` +
`Henry\Michael & Janet Jackson - Grammy Awards, 1993 [SUB ITA].mp4`; Katherine 60 Minutes Australia (was
`Drake\…60 Minutes Australia.mp4`, moved; a copy is `projects/mj-kids-saw-day-he-died/raw/60M_Katherine_2013.mp4`).

## (previous) STATUS (2026-10-28 ~15:40): RAW SEQUENCE PLACED in ABW10, waiting on his pass + direction video
- His answers 2026-10-28 (all five points settled): **raw sequence in ABW10 first · no music bed · the detail.'s 4K BET
  if sharper · caption what she says ("but things kind of") · WR close-ups over DL's cutaways OK.**
- Placed: ABW10 › "Janet Couldnt Cry" › **"Janet Couldnt Cry - raw cut"**, 58.42 s, not saved. Details + verification:
  RUN.md § STATUS (incl. the two warnings: `seq_src/` is a proxy; V2 covers move with their V1 piece).
- His "use the 4K BET if it's sharper": it is sharper but only covers BET 0–17.2 s (the detail. used the speech as silent
  B-roll under Dateline audio), so the old copy carries beat 2. Build option: Topaz Iris on the old BET next to the 4K.
- For his ear on his pass: beat 3 "but" vs "when" (the joined cut reads "when" to the transcriber; source passes "but").
- Next: catalog pass (below) + his direction video → code build.

## (previous) STATUS (2026-10-28 ~07:40): SOURCES IN, WORDS + LOCKS DONE, five points with Affan
- The locked creative is `brief/JANET-COULDNT-CRY-CUT.md` (his FINAL set, 28 Oct 2026, a verbatim copy of
  `X:\Claude Projects\Abundance Wisdom\JANET-COULDNT-CRY-CUT.md`). Build it as written. Anything that can't be done as
  written gets stopped and raised with him (Part B).
- All four sources downloaded with B2's commands; every beat's words timed; locks 1–6 checked; runtime ~61.7 s after the
  brief's trim steps 1 + 2. Details: RUN.md § Ranges / § Locks. Nothing cut, placed or rendered yet.
- Next on his answers: catalog pass (below) where the build needs it → raw sequence in ABW10 or the code build.

## Open with Affan
1. **Music** (asked first reply, unanswered): B4's piano bed vs his 2026-10-27 rule "AW code-built shorts ship with NO
   music bed even when the brief names one" (Flex got "no music" twice today). → Default: **no bed**, SFX only.
2. ~~Sources~~: answered 2026-10-28 ("you try"); all four downloaded.
3. **Order** (unanswered): his standing order is raw sequence in ABW10 → his re-edit + direction video → code build (Flex
   got that today too). This set says "build it as written". → Default: raw sequence first.
4. **BET quality:** the upload is **320×240** (a full-bleed 9:16 crop ≈ 8×; B3 caps SD at ~115 % punch). Better copies on
   YouTube (not fetched): RTVE `5hVzq3mQQTQ` 640×480 (29 Jun 2009 news, may carry a Spanish voice-over) and *the
   detail.*'s 4K restore `2DDImwmzmD8` (11 min, "Michael's Passing in Janet's Own Words"). Fetch one?
5. **Lock 2, his ear:** beat 3 is heard as "I tend to smile **but** things **kind of** get a little painful" by every
   unprompted pass, not the brief's "when things… get". Captioned as heard unless he hears "when".
6. **Picture swaps (lock 5):** DL puts "I was in Paris" on a **Jackson 5 childhood montage**, and the hook's first line
   ("Out of everyone… that moment to cry") plus "there were moments when I felt to cry" on NBC's wide two-shot. WR is a
   longer cut of the same interview with Janet in close-up on all three (same take, audio-aligned), so the plan is: keep
   DL's audio, put WR's close-up on screen for those spans. WR is 336p (softer than DL's restore) → a visible quality
   step between shots. The ~1.5 s "…just watching" (both uploads cut away) gets the brief's optional adult-Michael
   music-video still.
- Not a question: the export goes to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Janet Couldnt Cry.mov`
  (B6) **and** an identical copy to `X:\Claude Projects\Exports\` (his no-C-drive rule).

## Cost quote (before any heavy step; his paid usage)
- Intake + transcripts + in/out locked by ear + locks 1–6 + raw sequence in ABW10: about **1.5–2 % of the week (~$35–45)**.
- Code build (Topaz chain, his AE grade stack, letterbox/zoom/transitions, captions, audio, test frames of every shot,
  export, B8 report): about **4–5 % (~$90–120)**, the same as the Joe build.
- Higgsfield: up to ~2 credits, only if the *True You* page/cover photo (beat 4) is soft at full size.

## Sources (searched 2026-10-28; downloaded the same day with B2's commands → `raw/`, RUN.md § Sources)
| Code | Brief's source | On disk before? | YouTube (format B2's selector picks · size) |
|---|---|---|---|
| DL | NDaCZEGkWuM · *Janet Jackson - Dateline 2011 'True You' Promo 4K 60FPS* · itzjakebitch · 2025-05-21 · 42:45 | no | AV1 3840×2160 60 fps · ~1.44 GB |
| ABC09 | NWIgABuRBYY · *Janet Jackson Breaks Silence on Michael* · ABC News · 2009-11-19 · 8:03 | no | AV1 1280×720 30 fps · ~56 MB |
| BET | h6G8pFOZgGA · *Janet Jackson at bet awards 2009* · JanetJacksontv1 · 2009-07-09 · 1:18 | no | AV1 **320×240** 30 fps · ~1.6 MB |
| WR | nE65HHRdJK0 · *Janet Jackson Opens Up About Her Brother Michael's Death* · themjconspiracy · 2011-02-08 · 2:54 | no | H.264 596×336 30 fps · ~6.5 MB |
- Searched by title words and video IDs over E:, D:, X:, `C:\Users\affan\{Downloads,Videos,Desktop}`, plus every
  `*SnapYT*` file by duration. MJ-family files on disk: `E:\Bullshit Folder\Henry` (Katherine, Joe, Paris, Tito, La Toya,
  Jermaine, Murray trial). Janet files on disk:
  - `Henry\Janet-Jackson-SnapYT.App.mp4`: **Janet × Piers Morgan, CNN 2011** (42:37, 1080p60). He gave it for the siblings
    job; it isn't in this set.
  - `Henry\Michael & Janet Jackson - Grammy Awards, 1993 [SUB ITA].mp4`: 1993, not in this set.
  - `E:\Bullshit Folder\Michael-Jacksons-Siblings-SnapYT.App.mp4`: *the detail.*'s siblings compilation (16:50, 1080p60),
    the file holding the Rebbie "lamp store" line. Reference only, never captioned as Janet.
- B2's format selector (`bv*[height<=2160]+ba/b`) picks AV1 for three of the four. That's fine for the code build
  (ffmpeg); a Premiere raw sequence needs H.264 (Premiere can't read AV1): transcode the `raw/` copies.

## Grade / caption reference (B3/B5: "match the recent MJ-family Shorts")
`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`: `MJ Sib FInal YT.mov`, `MJ Kids Saw.mov`,
`Joe Appointment v3.mov`, `joe final yt.mov`, `MJ Final Skin.mp4`, `Paris Life.mov`. Pipeline = the Joe build
(`projects/joe-jackson-appointment/build/`, copied from MJ Kids Saw).

## Catalog pass (CLAUDE.md learning loop: required before any edit)
Done 2026-10-28 ~19:15: all 151 lines of `CATALOG.md` read and all 137 stills looked at (sheets `win/cat/cat_0-6.jpg`).
His direction names every overlay, zoom and transition, so the catalog only shapes HOW those land, never adds moves.
- **Fits, used inside his direction:**
  - FX-14 Painted Sky Worlds → his "greyed out" Michael overlay as silver B&W with crushed blacks + a soft vignette, not a
    flat desaturate.
  - FX-50 Filmography Mirror → the Bucharest and Grammy overlays are Michael's own performances cut in as his life
    (moving footage, not stills).
  - FX-29 Float Frame → his BET letterbox over a blurred fill ("too low quality, push it out").
  - FX-40 Slow-Burn Portrait → his zoom-in layers on the tight Janet close-ups (slow creep, no text).
- **Fits, held back (his look is set):** FX-42 Kin Tag (the AW lower third stays: JANET JACKSON · HIS SISTER · 2011);
  FX-78 Cinema Vignette Montage (only the soft vignette on the grey Michael, nothing on his colour overlays); FX-37 Ghost
  Dissolve and FX-38 Hard Push Slide (he named every transition); FX-58 Speaker-Coded Subs (AW captions are locked).
- **New to the channel here:** FX-14 silver B&W on a "greyed out" overlay.
- **Doesn't fit a 39 s face-led short:** maps, charts, documents, host sets, CG, chapter cards, CRT/phone props, stepped
  motion (FX-01–13, 15–28, 30–36, 41, 43–49, 51–77, 79–81).
- **What the last one leaned on (Joe Appointment):** label transitions, the SD letterbox at his size, head-locked SD
  faces, name cards, three STILL photo overlays (617–2326 px). **This one is better by:**
  - all four overlays are moving footage from ≥ 1080p sources (Bucharest 4K60, Grammy Legend restored, 60 Minutes
    1080p) instead of stills;
  - the low-quality source floats over a blurred fill instead of black bars;
  - it ends on Michael's own voice (his edit).
