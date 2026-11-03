# brotherlylove-protein-average-joe: Onyx sample Short for The Brotherly Love Pod (batch 6, ENHANCE mode)

## ▶ STATUS: resume here
- **2026-11-02 ≈16:40: LOUDNESS FIX (main's call: their Short measures −14.5 LUFS, ours played 2+ dB quieter side by side): mix-only
  rebuilds YT v6 (`yt_build.py … v6 --skip picture,overlay`, spec `target_i` −14.0 / `target_tp` −1.5) and IG v5 (`ig/sound.py v5 --mux`,
  same targets): ONE static gain (+2.7 dB) into the kit's oversampled limiter at −1.8 dBFS, no loudnorm; every relative level unchanged
  (voices matched, the bed 8.0 LU under, the cue offsets: cue_check identical, none weak). Re-finalized (finals + Exports + phone copy
  overwritten). Measured on the delivered files: **YT −14.0 LUFS / −1.8 dBTP, IG −14.0 LUFS / −1.8 dBTP, YT phone copy −14.1 / −1.7
  (24.1 MiB)**; pictures untouched (967 f). The −6 dBFS rule = a constant voice level, not a loudness ceiling (main 11-02).
- **2026-11-02 ≈16:35: FINALS DELIVERED, awaiting main / Affan.** `outputs/brotherlylove-protein-average-joe.sample-yt.final.mp4` (= YT
  v5, 38.1 MiB) and `.sample-ig.final.mp4` (= IG v4, 20.8 MiB), md5-identical copies in `X:\Claude Projects\Exports\`
  (`brotherlylove-protein-average-joe.yt.final.mp4` / `.ig.final.mp4`), the YT phone copy `…yt.phone.mp4` (24.1 MiB), proof sheets in
  outputs + Exports. Both: 1080x1920 H.264 24 fps, 967 f = 40.29 s, AAC 256k, voice peaks −6.0 dBFS (true), YT −16.7 LUFS (bed "Groundhog
  Day" ≈ 8 LU under, continuous), IG −17.1 LUFS (no bed), a 70 ms tail fade. `python work/finalize.py <yt> <ig>` re-finalizes.
  **Flags for Affan / main:** (1) beat 6 differs from the sequencing sent: "and understand," is KEPT (cutting it moved his head 40 px);
  the next joint is covered by the whole call (Jason + Christina) as a FIT card; (2) the asker is untagged (unconfirmed: Andy per their
  own caption, not Joey); (3) whips INTO a face are silent by the house rule; (4) the YT hook title has a swish and no hit (the kit's
  D9 warning, kept: no impacts on Onyx samples).
- **2026-11-02 ≈16:40: QA r1 (one sonnet reviewer, defects only, on YT v4 + IG v3; evidence in the session scratchpad `qa/`): no HIGH.**
  Fixed → YT v5 + IG v4 (rendering): (1 MED) the JASON tag's big line ran to x 995 (> 960) → tag x 185; (3) the herd / box / phone
  cards' top edges at y 169-200 → moved down 26-36 px; (4) Jason's open mouth on frames 230-231 touched "OBVIOUSLY" → s06 fy_out 0.30;
  (5) IG: the herd card straddled the caption line → 880 px at cy 468. **Kept by design (reported):** whips INTO a face (188, 700) are
  silent (cuts back to a face silent, the Roofing / Morgan rule); the host's payoff chunks wipe white → yellow (README § 5); 4 YT chunks
  show 0.2-0.3 s before their word where a pause precedes (chunks never go blank); their real ORGANIC BEEF label's fine print on the phone
  post (their own photo). Passed: every word once and in order in both looks, caption y constant, safe zones, no stray / black / frozen
  frames, head steps at in-shot joints ≤ 14 px (tracker), labels low, no invented brand or number, voice peak −6.0 dBFS constant,
  −16.7 / −17.1 LUFS, YT bed continuous ≈ 8 dB under, IG no bed, every graphic has its sound, no repeat back to back, start 0.09 s,
  end 0.03 s after "run", no glyph faults, longest bare face 3.58 s.
- Sound v3/v4: per-cue trims from cue_check (YT `yt/sfx/trim.json`, IG `ig/sfx/trim.json`): every cue now 10-18 dB under the voice
  beside it and none WEAK on a phone (v2 had 11 weak under the bed); the marker strokes start with their pen lines.
- **2026-11-02 ≈15:45: YT v1 built** (`outputs/…sample-yt.v1.mp4`, 943 f, −16.6 LUFS, peak −6.0; bed "Groundhog Day" 8 LU under;
  19 cues; payoff 2.07 s mean before the turn / 3.44 s after, last shot 3.58 s). Head gate on v1: joint 733 ("your farmer, | and that
  farmer", 1.25 s cut) stepped 40 px and stayed → **re-cut: "and understand," kept, only the doubled "and" goes** (make_edl b6), so every
  downstream edge re-derives (yt/build_spec.py + ig/build.py read the cut). IG v1 render (pre-re-cut) running; it is discarded. NEXT:
  re-splice (AMPLIFY_DB=2) → patch_transcript → verbatim pass → yt_faces → build_spec → YT v2 + IG v2 → cue_check both → ONE sonnet QA
  → fixes → finals + YT phone copy → BUILD.md row → main.
- **2026-11-02 ≈15:30: CUT DONE** (`outputs/brotherlylove-protein-average-joe.mp4`, 943 f @ 24 = 39.29 s, 19 segments, all pinned;
  `work/cut/make_edl.py` → splice.sh AMPLIFY_DB=2 (measured); audio-qa: timeline exact, 18 joints clean, peak −5.97 dBFS = voice peaks at
  the −6 limiter; one "ambience hole" flag at 18.63 s = the sentence break "in there. | We always" cut silence-to-silence, kept).
  RUN `python work/cut/patch_transcript.py` AFTER EVERY SPLICE. Verbatim faster-whisper on the cut (`work/cut/fw_cut_v3.txt`): plain reads
  every word clean. Stumbles found and CUT: "a genuine- a genuinely" (raw 21.333-21.792), "and, you know, these" → "and these" (WhisperX
  had hidden "you know" in a 0.74 s "and"; raw 41.25-42.208), "experience and, and be" → "and be" (84.625-84.875); a 0.37 s breath pause
  before "you're ultimately" forced out. Prompt-only repeats ("that- that", "Star- Starwalker", "or- or", "where- where", "I- I've")
  read clean without the prompt: kept. Main OK'd the sequencing 11-02 (asker untagged; YT bed ≈ 8 dB under). Next: assets (Starwalker
  site, Mixkit aisle, Epidemic bed + SFX) → faces → YT spec + cards → IG → QA → finals (+ YT phone copy).
- Intake done: `raw/main_section.mkv` = source 98.000-192.000 s (frame-exact, 24/1 fps, x264 CRF 12 + PCM 48 k, 2256 frames, both
  streams start 0). **raw t = window t − 98.0 = episode t − 2708.0** (window t0 = episode 0:43:30). The original cut is kept in
  `work/raw-orig/main_section.mkv`; the raw's audio carries ONE static gain step: the host span (raw < 34.0 s) × 0.5821 (−4.7 dB) so both
  voices sit at ≈ −18.6 LUFS before the splice chain (host −13.7 / peak −2.1 brick-walled by the show, Jason −18.4 / −2.0). Jason was NOT
  raised (that clipped his peaks in s16).
- Transcript: `transcript/words.json` (WhisperX large-v3, one clip). Their Short transcribed by faster-whisper: `work/ref/ref_words.txt`.
- A/V sync: no offset applied. Mouth-motion vs audio-onset cross-correlation peaks at +3 frames on the host close-up AND on their own
  Short's copy of the same shot (`work/cut/avsync.py`): the show's own sync, nothing introduced by the download.

## The job
- Show: **The Brotherly Love Pod** (the Lawrence brothers; studio in LA: three hosts' close-ups + a wide with the neon logo). Episode
  "Starwalker Organic Farms Is Here To Sustain The Brothers!" (YouTube QfjJh-mQjKE), the Starwalker farm couple joining on a remote
  feed (one 1920x1080 picture: him left, her right, under a tree, blown-out white sky).
- **Their Short (the permitted one, the spec):** "How to source quality protein, for the Average Joe!" (IvlkNNoc1u0, 52.0 s, 1080x1920,
  24 fps, 5.5K views) = episode ≈ 0:45:16-0:46:35 + a 6.9 s logo end card.
- **Speakers (verified):**
  - The question = the host in the black cap + glasses (raw 10.46-14.08 and 16.96-31.88 on his close-up). Voice: wespeaker cosine
    0.858 to his own span (`work/cut/spk.py`). **Not named on screen**: the pun ("average Joe, no pun intended, because you're well
    above average") is aimed at ANOTHER brother (the edit cuts to the NY-cap brother on it), so the asker is not Joey; their own Short
    burns "Thanks Andy" over the NY-cap brother at that moment, which points to Andy, but I cannot confirm it from our audio (WhisperX
    hears "know if"): no name tag for him.
  - The whole answer = **Jason** (Starwalker Organic Farms). Picture: one continuous remote-feed shot (raw 36.13-94), only the man's
    mouth moves, the StarWalker Organic Farms logo is on his shirt. Name: the episode intro (scout 0:00:29) says "Christina and Jason
    from Star Walker Ranch", and at window 0-17 s the WOMAN talks (picture: `work/ref/win0_20.jpg`) and says "Jason always sets the
    greatest picture of like when he's out in the field" → the man is Jason. Voice: every answer span scores 0.79-0.97 to the answer's
    own centroid, 0.14-0.23 to Christina, ≈ 0 to the host. No surname anywhere in the window: the tag says JASON only.
- Camera map of raw (scene cuts > 0.25 + 2 fps sheets `work/ref/raw_sheet_*.jpg`): 0-5.0 white-tee host · 5.0-10.46 wide · 10.46-14.08
  glasses host · 14.08-15.33 NY-cap host · 15.33-16.96 white-tee host · 16.96-31.88 glasses host · 31.88-36.13 white-tee host ("really lay
  it out for people if you can", cut) · **36.13-94.0 the remote feed (Jason talking, Christina listening), no cuts**.
- Rules (SAMPLE-ENHANCE-BRIEF + BUILDER-BRIEF + REACTIONS-V2): same point, same speakers; both looks from one cut; native **24 fps**
  (the source is 24/1, NOT 23.976: every copied kit number re-set), no Topaz; voice peaks −6 dBFS constant; **YT look: a continuous soft
  bed (lo-fi / mellow instrumental, no vocals, Epidemic) ≈ 8 dB under the voice, audible all the way (main's call 11-02, as on the SPI
  sample); IG look: no bed (the neon-window preset)**; SFX = a fresh, varied refined Epidemic set, each sound sized to its
  motion, never superhero / riser / sci-fi; face cam never > ~4 s bare; captions only ! ? and quotes; labels LOW; hook = claim only;
  no YouTube requests (NEEDS-YOUTUBE.md if ever needed); GPU jobs under `lock.sh gpu`; work in silence. Finals + Exports + **a YT phone
  copy < 30 MiB** (`<job>.yt.phone.mp4`).

## Teardown: their Short → ours (Affan's talking points)
| | Their Short (IvlkNNoc1u0, measured) | Ours |
|---|---|---|
| **Hook (first 3 s)** | Words: "Well, here's a question. How do, how does, how does the average Joe…" on the host's close-up, looking down. Picture: one face, no title. | First word on frame 0 is the real question, "How do people know that they're supporting a genuinely responsible farm…", under a 2-line claim title HOW THE AVERAGE JOE / **SPOTS A REAL FARM** (their own title's "average Joe", kept). By 1 s we're on Starwalker's real farm. |
| **Who / what / why by 5 s** | No. The question only lands at 10.8 s, after ~7 s of false starts and an inside joke ("no pun intended, because you're well above average… it should be debatable"). The word "farm" first comes at 13.6 s. Nobody is named. | Yes. The question (farm vs. packaging) is complete by ≈ 6 s. The farmer gets a LOW tag, JASON / STARWALKER ORGANIC FARMS, on his first frame. The show's name is the watermark. |
| **The answer** | Starts at 22.1 s. It skips the farmer's direct answer to "clever packaging". | Starts at ≈ 8 s, and restores his cut line from the same moment: "the packaging is deceiving… these companies buy other companies so they can have the same packaging, but putting different products or ingredients in there". That's the reveal the question promises. |
| **Captions** | Small white sentence-case on the chest, with commas and full stops, 1-3 words, no emphasis, no colour. | Big condensed caps just under the lips, one constant line. Colour = voice: the host's question in yellow, Jason white → red on the payoff words. Only ! and ?. |
| **Pacing** | 45.1 s of speech + a 6.9 s logo card = 52.0 s. Five "how do / how does" restarts and "if, if, well". Mean loudness 4.7 LU apart between the studio mic and the farm call. | ≈ 40.3 s of speech, no end card. Every restart and "you know" cut, pauses YouTube-tight. The two mics levelled to one voice level, peaks at −6 dBFS throughout. |
| **Visuals per beat** | 100 % faces: 4 framings (host close-up, NY-cap reaction, a stacked two-up of the call over the studio wide with no divider line, the farmer cropped). 0 B-roll, 0 graphics. The answer is 23 s of one webcam. | Every noun shown: Starwalker's own herd, box, pigs and product clip (their site), a built chilled shelf that deals the generic package, a parent company swallowing a farm brand, the same package returning under the red pen, its contents swapping, the farm → you line, a phone post with a heart, the farmer tagged YOUR FARMER, the whole call (both farmers), the herd returning under him on the button. Face cam never > 4 s bare. |
| **Ending / button** | "…be healthier in the long run" → 6.9 s neon logo card with a music sting (dead tail: the loop restarts on a logo). | Ends 0.1 s after "long run" on Jason's face with the zoom easing out. The last line ("trust your farmer… healthier in the long run") loops into the first ("How do people know…"). |
| **Sound** | Raw podcast audio; studio voice 4.7 LU louder than the farm call; no SFX; a sting on the logo card. | Both voices levelled, −6 dBFS peaks. A fresh, varied set of refined sounds (swishes, paper, card, marker), one per graphic, each sized to its motion. Cuts back to a face silent. YT: a lo-fi bed ≈ 8 LU under the voice; IG: no bed. |

## Sequencing (sent to main before the build; raw times = `raw/main_section.mkv`; exact words, ≈ 38 s)
**AS BUILT (differs from the text sent in 4 places):** beat 1 = a BUILT chilled shelf dealing the package (no meat-aisle clip: Mixkit had
none); beat 3 = Jason's face + tag, then the brand pulled into a PARENT COMPANY, the same package RETURNING full-frame with the red pen
ringing its label ("same packaging"), then a split whose bottom swaps the contents and the ingredients ("different products or
ingredients"); IG beat 3 = object stages (no type stages) + a corner card of the swap over his face; beat 6 = "and understand," KEPT (the
cut moved his head 40 px), "and that farmer doesn't even have to be perfect" over the whole call (Jason + Christina, FIT); beat 7 IG =
the herd card returns on "connection… trust your farmer", then his face (no TRUST YOUR FARMER stage).
HOOK title over 0-~2.8 s, claim only, 2 lines: "HOW THE AVERAGE JOE" / **"SPOTS A REAL FARM"** (REAL FARM coloured). It keeps their Short's
"Average Joe". The spoken question uses the LAST clean take, not the "average Joe" stumbles (CLAUDE.md: repeated line → last take).
1. **HOST (question, yellow captions)**, raw 19.18-27.80: "How do people know that they're supporting a genuinely responsible farm like
   Starwalker rather than buying something with clever packaging?" (out before it: "Well, here's a question. How does the average Joe,
   no pun intended, because you're well above average, know if… Well, it should be debatable. But no,")
   - YT: 0-0.9 s his close-up + hook title → whip to Starwalker's own farm picture ("a genuinely responsible farm") → their
     site / logo ("like Starwalker") → an unbranded supermarket meat aisle ("rather than buying") → a built package with marketing
     badges dropping onto a dark dusty field ("clever packaging", FX-33).
   - IG: his close-up full-window as the cover with the hook (Mark 10-31 type: small sans line over big bold sans, the key words on a red
     box), then the farm card dealt beside him and the package card.
2. **HOST**, raw 29.82-31.52: "I feel like it's easy for people to get fooled." (out: "Because I feel like that's a misconception.")
   - YT: his face (1.7 s).
   - IG: his face.
3. **JASON (red)**, raw 38.81-49.07: "Obviously the packaging is deceiving, and these companies buy other companies so that they can have
   the same packaging, but putting different products or ingredients in there." (out before it: the host's "We've kind of touched on it,
   but yeah, really lay it out for people if you can" and Jason's "No, and I think that's a great point because"). This line is the one
   their Short cut, restored as the direct answer (~10 s, from the same moment).
   - YT: his face with the LOW tag JASON / STARWALKER ORGANIC FARMS (≈ 2 s) → SPLIT, his face on top, below it the package with a red
     pen circling its FARM FRESH badge ("deceiving", FX-55) → a small brand card swallowed by a bigger company box ("companies buy other
     companies", no names) → SAME PACKAGING stays, the ingredients panel behind it blurs and swaps ("different products or ingredients",
     FX-35).
   - IG: his face + the tag low → stage: THE PACKAGING / **IS DECEIVING** → stage: SAME PACKAGING / **DIFFERENT INGREDIENTS**.
4. **JASON**, raw 50.83-53.95 + 54.27-56.35 + 57.55-58.29: "We always go back to, and I know this is hard for the average person to do,
   but to have some sort of connection from where you get your food." (out: "And so I think the thing is that"; "farm or" + the first
   "you get your" = his own restart, the LAST "you get your food" kept).
   - YT: his face, push in on "average person" (≈ 3 s) → a red dashed line drawn from a farm pin to YOU ("connection from where you get
     your food", FX-24).
   - IG: his face → stage: the line farm → you.
5. **JASON**, raw 58.93-59.71 + 60.05-63.27: "Even if that's just, hey, I've watched them on social media and I like what they do." (out:
   "you know" ×2; "or, you know, a friend of mine knows, you know, has a connection or something")
   - YT: a phone propped up, Starwalker's farm in a social-style post, a heart landing on "I like what they do" (FX-57).
   - IG: the same phone card in the window.
6. **JASON**, raw 67.94-70.29 + 70.54-72.29: "But if you can know your farmer and understand, and that farmer doesn't even have to be
   perfect." (out: his doubled "and"; after it "I'm not saying every farms in the US… doing the best they can. And, and, uh,"). v1 of the
   cut dropped "and understand, and" (1.25 s): his head moved 40 px across that gap (YT head gate), so the words stay (their Short kept them).
   - YT: his face with a pointer tag YOUR FARMER (FX-23) on "know your farmer".
   - IG: his face, the YOUR FARMER label low.
7. **BUTTON, JASON**, raw 79.32-86.81: "But if you have some sort of connection and you trust your farmer, you're ultimately going to get a
   better experience and be healthier in the long run." Ends 0.1 s after "run". Same point as their Short's last line; NOT the "steer
   away from big ag" / consumer-demand / Erewhon passage after it.
   - YT: SPLIT (his face top, Starwalker's pasture below) on "connection… trust your farmer" → his face full, zoom easing out on the last
     line.
   - IG: his face, the last stage TRUST YOUR / **FARMER** fading under the last line, then his face to the end.
- Loop: "…be healthier in the long run." → "How do people know that they're supporting a genuinely responsible farm…"
- Length ≈ 40.3 s after the tight pass (their Short 52.0 s).

## Catalog pass (2026-11-02; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on labelled
## sheets: 80 singles at 430 px in 4 sheets, 57 strips at 1500 px in 6 sheets, every tile read)
- **Fits this story** (a buyer's guide told by a farmer; the nouns are a farm, a package, companies, a social post, a farmer):
  - **FX-33 Dust Void Drop**: the generic meat package isolated on a dark dusty field, dealt on "clever packaging" (the one object).
  - **FX-55 Red Pen Underline**: one red mark per document: the red pen circling the package's FARM FRESH badge on "deceiving".
  - **FX-35 Blur-Isolate Row**: the ingredients panel behind the package blurs and swaps on "different products or ingredients".
  - **FX-24 Red Dash Map**: a red dashed line from a farm pin to YOU on "connection from where you get your food".
  - **FX-57 Propped Phone Call**: Starwalker's farm inside a propped phone, a social-style post, on "watched them on social media".
  - **FX-23 Pointer Tag / FX-42 Kin Tag**: JASON / STARWALKER ORGANIC FARMS low on his first frame; YOUR FARMER on "know your farmer".
  - **FX-79 Flash-Forward Echo**: the same package returns (the hook's object comes back as the deception, then as the swap).
  - **FX-29 Float Frame**: Starwalker's real farm photos as float frames over their own blur (no 1080p blow-ups).
- **Not used yet on this kind of video**: FX-24 (no map line in batch 6 so far), FX-57 (the phone post), FX-33 on a product.
- **Leaned on by the last ones, avoided here:** Roofing's FX-35 tax return + FX-72 flat line + FX-71 count, CrossExamined's FX-41 Year
  Ghost + inflating tag, Pollak's FX-27 quote card + FX-28 dossier, Pincus's read-along highlighters (FX-34), TCO's drawn backyard.

## What this one does better than the last ones (rule 5; Roofing r1, CrossExamined, TCO YT+IG)
1. **The enhancement is visible against their own cut**: the real question on frame 0 (their Short needed 10.8 s), and the farmer's
   packaging reveal they cut, restored. The before/after is the pitch.
2. **One object carries the argument** (the package): dealt as the trap, circled as the deception, kept identical while what's inside
   swaps, then replaced by a person (YOUR FARMER).
3. **Two mics levelled to one voice** at −6 dBFS peaks (their Short: the studio 4.7 LU over the farm call), and a WIDER sound set than
   Roofing's swishes: card slides, paper, soft pops, a pen stroke, each sized to its move.
4. IG: Mark Brazil's newest type with a remote-call guest whose bright sky is relit to the window's dark look.

## Sources (yt/assets/broll; the IG reads the same files)
| Use | File | From |
|---|---|---|
| "a genuinely responsible farm" (s02) and the button split (s14, FX-79): their herd crossing the pasture | sw-herd.png (2880 x 996, their drone still, shown at <= 1.0x as a float frame / a 1:1 crop) | starwalkerorganicfarms.com homepage banner (their own site) |
| "like Starwalker" (s03): their StarWalker box | sw-v2.mp4 10.62-11.04 s (606 x 1080, their product clip), held on its last clean frame | starwalkerorganicfarms.com homepage video 96e933ef… (their own site) |
| the phone post (s12): their pigs under Mt. Shasta, then their ORGANIC BEEF package | sw-pigs.png (1200 x 1108) + sw-v2.mp4 from 11.6 s | their site (rt-bg banner; homepage video) |
| the package, brands, map, phone, ingredients | mg-*.mp4 | built: `yt/cards.py` + `work/gfx.py` (generic, no brand, no numbers) |
| Bed (YT only) | yt/assets/audio/bed.wav = "Groundhog Day" (Auxjack), from 16.0 s, ~8 LU under the voice | Epidemic 05f54cdb-cb87-4a89-ab40-c9a41a72760f (lo-fi hip hop, hopeful, laid back, no vocals, 75 bpm, 2:28; not used by any earlier job: grep) |
| SFX | yt/sfx/*.wav sliced from assets/sfx/epidemic/bl-*.wav (`yt/sound.py`) | Epidemic (download log e2) |
Not used: their homepage videos sw-v1 / sw-v3 / sw-v4 (third-party creators' faces reviewing the product), Mixkit (no supermarket clip
showed meat: 49289 is diapers, 4178 a bazaar, 6102 produce; the shelf is built instead), Bing (region-skewed: mochi).

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `reference/IvlkNNoc1u0.mp4`, `source/QfjJh-mQjKE_0.43.30-0.49.00.mp4` | main session (YouTube, H.264) | 15 MB / 143 MB | their Short + the episode window (not pulled by me) |
| w1 | `work/img/sw/*.html` (home + a few product / about pages) | starwalkerorganicfarms.com (their own site; curl) | ≈ 0.1-0.5 MB each | find their real farm / cattle / product photos (the receipts for "a genuinely responsible farm like Starwalker" and the pasture on the button) |
| w2 | `yt/assets/broll/sw-*.jpg` (≤ 8 images listed in those pages) | starwalkerorganicfarms.com image CDN | ≈ 0.2-2 MB each | the real farm, cattle and products (FX-29 float frames, the phone post) |
| w3 | `yt/assets/broll/sw-v1..v4.mp4` (their 4 homepage videos: 6a24bbf9…, 96e933ef…, 42045306… (720p), 8862938c…) | starwalkerorganicfarms.com/cdn/shop/videos/… HD-1080p mp4 (their own site; URLs read in the built-in browser, no media played) | ≈ 5-30 MB each | their OWN farm footage (vertical) for the farm, the pasture on the button and the phone post |
| m1 | `work/img/mixkit/<tag>.html` (supermarket, meat, grocery listing pages) + `<id>-360.mp4` previews | mixkit.co / assets.mixkit.co (Mixkit free licence) | ≈ 0.2 MB / 1-3 MB each | an UNBRANDED supermarket meat aisle for "rather than buying something" |
| m2 | `yt/assets/broll/b-aisle-<id>.mp4` (720 or 1080) | assets.mixkit.co (Mixkit free licence) | ≈ 5-25 MB | the chosen aisle clip |
| e1 | `yt/assets/audio/bed.wav` (one track) | Epidemic Sound MCP `DownloadRecording` (lo-fi / mellow instrumental, no vocals) | ≈ 20-60 MB | the YT bed (main's call) |
| e1 ✓ | pulled: "Groundhog Day" (Auxjack) WAV FULL, 42.5 MB | Epidemic 05f54cdb… | | |
| e2 | `assets/sfx/epidemic/bl-*.wav` (≈ 10-14 takes; PULLED 11: 0495c3a2 Whoosh Short Mid Freq Dry 02, 11926555 Whoosh Short Mid Box Dry, 4ba14461 Swish Short Boosted Mid Freq Dry, 6d899eeb Whoosh Short Scrape Dry, 82044b85 Swish Short Boosted Mid High Freq Dry, 316bda5c Playing Card Slide On Table 03, 75851aab Playing Card Turn Over On Table 03, 91b5b50b Paper Friction Sheet Large Laminated Slide 01, a5da9fbb Paper Friction Envelope Slide, 4b1eeb52 Sheet Laminated Slide On Wooden Table 04, 9f76f0f2 Marker Pen Draw Line On Cardboard Sheet) | Epidemic Sound MCP `DownloadSoundEffect` (card slide, paper, soft swish, soft pop, pen stroke families; none used before: MANIFEST + BRIEFs grepped first) | ≈ 0.1-0.6 MB each | a fresh, varied set sized to each motion |
