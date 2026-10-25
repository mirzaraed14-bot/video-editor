# bradlea-ferrari-camry: Onyx sample Short for Dropping Bombs (Brad Lea) (batch 5), "Why a Ferrari cost him less than a Camry"

## ▶ STATUS: resume here
- **IG 2026-10-24 ~16:45: IG FINAL DELIVERED (neon-window look, 60 fps), awaiting Affan's review.**
  `outputs/bradlea-ferrari-camry.sample-ig.final.mp4` = `X:\Claude Projects\Exports\bradlea-ferrari-camry.ig.final.mp4` (md5-identical
  8fccfcbb…; H.264 High 1080x1920 60 fps, 2516 f, 41.93 s, AAC 256k; decode clean; -12.3 LUFS, TP -1.8: limiter at -3 because the AAC
  overshot a -2.3 mix to -0.9 at 0.42 s). Last pass (after v2): the F8 card now reads "THE MODEL: FERRARI F8 TRIBUTO" (a show car, not
  Brad's own: GATE 5), and three sub booms were dropped 2-3 dB more on K-weighted momentary loudness (the loudest cue is now 3 dB under
  the voice). `ig/qa.py` PASS (bars black, no
  strays, punctuation, every word once, bare face cam <= 3.0 s); proof `outputs/…sample-ig.proof-sheet.jpg`. v1 (`…sample-ig.v1.mp4`) ->
  ONE Sonnet reviewer (defects only) -> v2 fixes: close cam starts on "They hold" (he leaned down at the cut-in, lips under the caption
  until 29.05 s; "Because they do that" now sits on the receipt), top-band type + tags + years line raised and the cam held at 1.00
  while type sits above his head (hair tufts at y 195-215), chart source line moved to the top and enlarged, frame 0 = the whole hook
  title, quote stage's bar on its first frame, a soft caption scrim on cam shots (the mic's beige logo plate), cues re-timed (kicker,
  YEAR 4) and re-levelled from a rebuilt SFX stem (sub booms 8-12 under, blips 5), +2 cues (Camry label, F8 line), bed 14 LU under with
  -1.5 dB from 37.5 s. Measured after: min mouth-to-caption gap 33 px on every captioned cam frame (YuNet).
- **IG 2026-10-24 15:15: IG v1 RENDERING at 60 fps (`ig/work/build60.log`).** Plate `ig/work/cam60.topaz.mov` = the 4K Topaz scaled to
  2560x1440 + Chronos x2 per take (2516 f; `ig/motion_check.py`: 4.1 % near-zero steps; no crop upscaled: <= 0.97 window px per plate px).
  Sound (`ig/sound.py`): 26 cues sliced from the YT builder's fresh Epidemic set (read-only), every slice tonal-checked (<= 18.8 dB);
  REJECTED as narrow tones: phone-buzz 27.6, riser-dramatic 29.0, riser-reverse-layers 30-32; bed = the YT look's "Blue Saga" from
  12 s, 13.5 LU under; mix -12.1 LUFS / TP -2.3. F8 photo card on the first receipt = the YT builder's Commons file (Calreyn88,
  CC BY-SA 4.0, credited on screen, the stranger's plate blurred).
- **YT 2026-10-24 ~17:15 PKT (11:15 UTC): YT FINAL (v4) DELIVERED, awaiting Affan's review.** `outputs/bradlea-ferrari-camry.sample-yt.final.mp4` = `X:\Claude Projects\Exports\bradlea-ferrari-camry.yt.final.mp4` (md5 9c04d0d6d5bac0589c72ae3914376d35 both; H.264 High 1080x1920 60 fps, 2516 f, 41.93 s, AAC 48 k stereo; decode clean; -12.1 LUFS, TP -2.2; proof `outputs/…sample-yt.proof-sheet.jpg`). v4 = v3 + (a) the Commons photos credited ON SCREEN (`yt/composite_credits.py`, 22 px, s02 s04 s06 s12 s13b s14 s15 s16 + 'Photo: Toyota' on s17), (b) strangers' licence plates blurred (`yt/noplate.py` -> `*-np.jpg`), (c) the s13b receipt panel from the card's own alpha (no crop box). Built by `yt/work/final2.sh` (picture -> whips -> Chronos x2 -> `picture.whip60b.mov` -> credits composite; overlay.mov + mix.wav = the v3 final build's). v3 (no credits, plates visible) kept as `outputs/…sample-yt.v3.mp4`.
- **YT 2026-10-24 ~16:55 PKT (11:00 UTC): v3 final built (superseded by v4 above).** `outputs/bradlea-ferrari-camry.sample-yt.final.mp4`
  = `X:\Claude Projects\Exports\bradlea-ferrari-camry.yt.final.mp4` (md5 1c9fb39bb0965d95a6e2634c309c2e71 both; H.264 High 1080x1920
  60 fps, 2516 f, 41.93 s, AAC 48 k stereo; decode clean; -12.1 LUFS, TP -2.2; 65 caption chunks; 25 SFX cues; proof
  `outputs/…sample-yt.proof-sheet.jpg`). Built by `yt/work/final.sh` (picture 30 fps -> whips -> Chronos x2 under the GPU lock with
  segments = shot starts + the head_lock jump cuts, `yt/work/segs60.txt` -> `yt_build final --skip picture`); checked at the fixed shots,
  the jump cuts (802, 1704, 1962: no pop) and the whip cuts (no Chronos morph). Superseded drafts: v1, v2 (30 fps) in `outputs/`.
  **Taste calls for Affan:** "I'm like, oh shit" trimmed (no bleep) while "piss off Ferrari" stays unstarred; the hook reads "BRAD LEA'S
  FERRARI / VS A CAMRY" (no title for Brad: only the show's own words were verifiable); line 4 is Brad asking it himself (PICKS guessed
  Victor); the sales guy's emphasis chunks wipe white -> cyan (kit design); (the s13b panel box is fixed in v4).
- **YT 2026-10-24 ~16:50 PKT: FINAL BUILDING (60 fps, `yt/work/final.sh` -> `yt/work/build-final.log`).** v2 (`outputs/…sample-yt.v2.mp4`,
  30 fps) went to ONE sonnet reviewer (defects only, `yt/work/qa-r1/`); fixed for the final: (1 HIGH) the Carscoops card glided off the
  right edge (w 820, drift 0.15); (2) "NO" x5 (medium.en's timed count + the PICKS RSS text); (4) s13b receipt moved inside the safe band
  (`ledger-b-panel.png`, SOLD row ~y 1526); (5) the 84 px head pop at the jump cut 852 (split tops now head-tracked, `track: true`);
  (6) voice-first: booms 3-4 dB down with shorter tails, the whoosh under the +$13,000 hit dropped; (7) split entrances get a landing hit
  (paper-slap / money-bang / shutter-film); (8) close-up split tops z0 1.0 (crown kept); (9) ledger-c "FOR 3.5 YEARS" +26 px.
  KEPT by design: (3) the white -> cyan wipe on the sales guy's emphasis chunks (README § 5: another voice's emphasis chunks wipe white ->
  colour, plain ones are solid); (10) two chunks snap onto shot cuts (kit `snap`, lead < 3 f); (11) the f581 joint (low confidence,
  re-ASR clean; a re-splice would shift the whole timeline). v1 -> v2 had fixed s03, s10, s17 (Toyota's own Camry photo) and 3 short chunks.
  Spec = `yt/build_spec.py` (19 shots, A 22 % / SPLIT 16 % / B+DOC+MG 62 %; 65 chunks, Brad main + the quoted sales guy cyan; 25 fresh
  SFX cues; head_track + head_lock [401, 852, 981]; zoomkeys 12-24 % per speaker run; face runs <= 2.7 s, asserted <= 4 s); MG clips by
  `yt/mg_ferrari.py` (the LEDGER x3 + the CALL card).
- **IG 2026-10-24 ~14:40 PKT: IG BUILDING (neon-window look, IG builder; files in `ig/` only).** Everything anchored to the cut's WORDS in
  `ig/plan.py` (shots, 33 caption blocks, events, the 4 s face-cam rule asserted); look library `ig/look.py`; picture `ig/build.py`.
  Framing (`ig/tools/takes.py` -> `ig/work/takes.json`): mouth at window (522, 640) on all three cams, face 370 px (side/front), the
  close-up at full frame height; **static per-take anchors** (never per-frame tracking: neon-window LESSONS 2026-10-23) solved so the
  head lands in place at every same-camera joint (residual <= 9 px; Affan 2026-10-19 head steady), pushes anchored ON the mouth and
  continuous across jump cuts. Camera plate = `ig/tools/plate.sh`: waits for Topaz DONE, scales to 2560x1440, Chronos x2 per take
  (26 segments) under `lock.sh gpu` -> `ig/work/cam60.topaz.mov` (60 fps = 2x the 30 fps cut). Better than MATG's IG: the receipt
  (PAID $367K / OFFERED $500K / SOLD $380K / +$13,000) is ONE object that returns and evolves on the stage; the type sits in the dark
  band above his head (Mark's "diagram above the heads") instead of on stills; the button is a hairline value chart (his F8 flat vs the
  average Camry falling). GATE 5 extra fact: the Camry line = iSeeCars via SlashGear (2026-04-28): a 2021 Camry at 68.9 % of its
  original price after 5 years (source line on screen); 31-36 % figures seen only in search summaries were NOT used.
- **2026-10-24 14:25 PKT: CUT FINAL, `work/READY.json` written for the IG builder; Topaz queued on the GPU lock (behind the FF Topaz);
  YT graphics next.** Cut = `outputs/bradlea-ferrari-camry.mp4`, **1258 f @ 30 = 41.933 s**, 25 pinned segments (`work/cut_plan.py`),
  AMPLIFY_DB -2, audio-qa joints clean, dead-air PASS, no silence >= 0.12 s left (10 ms envelope), re-ASR (medium.en, large-v3 on the 13K
  line) reads the six approved lines. Topaz -> `outputs/bradlea-ferrari-camry.topaz.mov` (Iris 2x + FI, `--segments` = every joint + the two
  source camera cuts, `work/cut/joints30.txt`, log `work/topaz.log`). **YouTube is BLOCKED again** (bot check at 08:58 UTC on a metadata
  call, flag `projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED` written by this job): B-roll comes from official press sites, page
  captures and free stock instead.

## The job
- Approved (Affan 2026-10-24): `projects/_onyx-batch5-2026-10/bombs/PICKS.md` § 4 = `SEQUENCING.md` § 1 pick 2. Six lines, in order,
  trims inside lines only. Look: `presets/youtube-shorts/onyx-samples-youtube/` (Sean Ryan) + README § 13 devices. Template:
  `projects/matg-targeting-is-dead/`. Deliver `outputs/bradlea-ferrari-camry.sample-yt.final.mp4` + byte-identical
  `X:\Claude Projects\Exports\bradlea-ferrari-camry.yt.final.mp4`. Deadline: Brad's 48 h window closes ~2026-10-25 03:00 UTC.
- Source: `raw/PJyDs4_-DVo.mp4` = YouTube "One Dinner in Miami Got Him a Lamborghini Dealership" (BRAD LEA TV, 2026-10-17, 1:18:08,
  1080p30 H.264, English original audio track 140-2). Guest Victor Young. The story sits at 19:51-20:21, 26:56-27:25 and 29:03-29:08 of
  the YouTube file (the RSS times in PICKS were not used: matched by words on a WhisperX large-v3 transcript of 12:00-31:00).
- Cameras in the cut (all Brad): medium side angle (L1-L2, f 0-581), wide front (f 581-826, 1092-1258), close-up (f 826-1092).

## The cut (what is on the tape vs PICKS)
| # | Line on the tape (cut) | Raw (s) | Notes |
|---|---|---|---|
| 1 HOOK | "I bought an F8, paid 367, drove it off the lot. Someone offered me 500. This is when they're hot." | 1191.57-1200.37 | false start "I bought a..." dropped |
| 2 | "I'm about to sell it. I called my sales guy and he goes, no, no, no, no. Can't do it. You won't get another car. He said, you'll be done. And I'm like, well, I'll just buy 'em used. He goes, no, you won't. I'm like, what do you mean? How can they stop me? He goes, Brad, trust me, if you like Ferraris and you ever want another one, don't sell it." | 1204.67-1221.33 | **"I'm like, oh shit" + a stutter TRIMMED** (no bleep needed); "Don't do it x3. And I said, what do you mean?" dropped; "Can't do it", "He said, you'll be done" and "I'm like, what do you mean?" kept (continuous speech, no clean cut point before "How") |
| 3 | "Didn't sell it, because I didn't want to piss off Ferrari. Drove it for three or four years and just sold it for 380." | 1616.30-1626.00 | Victor's "yeah" before and after dropped; "um" dropped; "piss off" kept (mild, not starred) |
| 4 | "How did you buy it for 367 and sell it for 380?" | 1627.53-1630.43 | **BRAD asks it himself, not Victor**: wespeaker embedding simBrad 0.76 / simVictor 0.13 (`work/check/emb.py`), camera on Brad. Captioned in Brad's colour |
| 5 | "Because they do that. They hold their value, most of them. But if you think about that, they paid me thirteen thousand dollars to drive their car for three and a half years." | 1631.10-1645.27 | three "yeah"s dropped; his 1.3 s pause before the number cut, and his 0.22 s break INSIDE "thir- / -teen" cut to 0.07 (an earlier cut that dropped "thir-" read "$10,000" to three ASRs: fixed) |
| 6 BUTTON | "your Toyota Camry costs more at the end of the day than that Ferrari does." | 1743.63-1748.10 | "Dude, that, that," dropped; the tape says "costs" (PICKS: "cost"); a filler burst after "more" dropped |
- Pacing (Affan 2026-10-23): every silence > ~0.15 s cut to ~2-3 frames on the 10 ms envelope (leftover 0.05-0.10 s; >= ~15 ms after
  decays, >= ~25 ms before onsets). The source's pauses are noise-gated to digital silence, so audio-qa's "ambience holes" at the joints
  are the source's own gate (the bed covers them), not a crossfade fault.
- Spoken numbers: "three sixty-seven" = $367K, "five hundred" = $500K, "three eighty" = $380K, "thirteen thousand dollars" = $13,000.
- Loop: "...than that Ferrari does." -> "I bought an F8, paid 367..." reads as one thought.

## GATE 5 (facts on screen)
- Every number (367, 500, 380, $13,000) is BRAD'S OWN CLAIM: attributed on screen as his ("as Brad tells it" / source "Brad Lea, Dropping
  Bombs"). Never shown as a market price.
- On-screen text says only **"F8"** (what Brad says; he never says Tributo and a Spider is as plausible). The photos/clips are F8s (Commons
  titles + the twin round tail-lights / louvred engine cover checked at full size); the Geneva photo's own badge reads "F8 TRIBUTO" (the
  car's badge, not our claim). ferrari.com answered a bot check (not bypassed).
- Brad Lea: the episode description (the show's own words): "His top-rated podcast, Dropping Bombs"; "LightSpeed VT is Brad's brainchild".
  On screen only his name ("BRAD LEA'S FERRARI / VS A CAMRY") and the watermark DROPPING BOMBS: no unverified title (lightspeedvt.com did not resolve).
- Toyota: toyota.com/camry captured 2026-10-24 ("2027 Camry", "Starting MSRP $29,700*"), shown as Toyota's own page, nothing computed from it.
- Ferrari resale enforcement receipt: Carscoops, Chris Chilton, 2024-10-20, "Ferrari Dealer Sues Customer For Flipping His Purosangue"
  (Ferrari of Houston v. a buyer who signed a first-refusal agreement for 18 months). A real case about a dealer, not about Brad's F8: shown
  as "this is how they stop you", never as Brad's story.

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/PJyDs4_-DVo.mp4` (+ info.json, download.log) | https://www.youtube.com/watch?v=PJyDs4_-DVo (downloaded by the main session) | 1.0 GB | the source |
| d1 | `yt/assets/broll/doc-carscoops-purosangue.png` 2560x3200 | https://www.carscoops.com/2024/10/ferrari-dealer-sues-customer-for-flipping-his-purosangue/ , `workflows/page-record.mjs` still 2026-10-24, no login | 1.0 MB | "How can they stop me?" receipt |
| d2 | `yt/assets/broll/doc-toyota-camry.png` 2560x3200 | https://www.toyota.com/camry (Toyota's own page: "2027 Camry", "Starting MSRP $29,700*"), page-record still 2026-10-24, no login; the cookie banner sits below the crop | 3 MB | "your Toyota Camry" (DOC, underline on "2027 Camry") |
| d3 | `yt/assets/broll/camry-toyota-official-front.png` 3600x2700 | Toyota's own press/gallery photo on toyota.com/camry (Adobe CDN `.../as/CAM_MY25_0012_V001.png`, listed in the page HTML, fetched 2026-10-24): a Camry driving at camera in a city | 11.6 MB | s17 "your Toyota Camry" (replaced the d2 page DOC) |
| c1-c4 | `work/dl/camry/*.mp4` | toyota.com/camry's own CDN videos (Overview 16:9, TJA, two 900x600 clips) | 1-8 MB | looked at, NOT used (renders of the hybrid system / traffic) |
| p1-p6 | `yt/assets/broll/px-8443861…, px-8443860…, px-8443781…` (2560x1440 30p), `px-5309380` (Ferrari shield, 1080p25), `px-13358188` (a red Ferrari in a showroom, 1080x1920 60p), `px-13643101` (Toyota badge, unused) | Pexels free licence (videos.pexels.com, ids from a same-origin fetch in the built-in browser on pexels.com/robots.txt, no media played) | 5-60 MB | the F8 (twin round tail-lights + louvred engine cover = F8 Tributo, checked at full size) driving in Abu Dhabi; the shield for "piss off Ferrari"; the showroom under "if you like Ferraris" |
| w1-w6 | `yt/assets/broll/f8-*.jpg` (3200-3840 px) + `commons-sources.json` | Wikimedia Commons, CC BY-SA 4.0 / CC BY 4.0 (Calreyn88: sf25, Ferrari F8, Ferrari Lyon showroom, 2022 F8 1; RegionVisitor90: Mount Torrens rear; Alexander Migl: Genf 2019 debut) | 1-3 MB each | real F8 stills (the ledger plates, s02, s14 "they hold their value" = the 2019 Geneva debut crowd, s15 split) |
| m1 | `yt/assets/audio/ES_Soundbed - Blue Saga.wav` | Epidemic Sound recording 5a2536b3-2ec2-4b9b-bc45-00abbf620352 "Soundbed" (Blue Saga; ambient, drone, mysterious, pulses; no drums stem), WAV FULL; not used by any earlier job (grep of every BRIEF 2026-10-24); bed_in 13.4 s so its lift (track 39 s) lands on the turn (25.6 s) | 35 MB | the bed, 13.5 LU under the voice |
| x1-x15 | `yt/assets/sfx/*.wav` | Epidemic SFX, WAV, none used before in this repo (id grep 2026-10-24): b61ceeac whoosh vehicle airy · 911508a4 whoosh wind soft 02 · 808aa0f8 whoosh organic wind · 47d83a22 boom heavy hit rumble · 95c4ca16 boom clean impact sub · 5189480e boom dark low · bc6116c7 money notes bang table · 8c36b7c6 paper newspaper slap · bac9ad16 pen on paper · 69df2ab0 analogue film shutter 04; REJECTED on tonal prominence > 20 dB (files kept, unused): 29ee2675 phone vibrate 27.6 · ff0f74c4 receipt printer 24.2 · 34b7b0fb riser dramatic 32.8 · 05f99b55 Nikon shutter 35.3 · e95aa280 reverse riser 29.6 | 0.1-2 MB | one cue per graphic, variety |
| x | — | yt-dlp metadata for Ferrari's "F8 Tributo - Official Video" (y12f7NxFgkw): bot check -> YouTube flagged BLOCKED, not retried, nothing downloaded | — | — |

## Better than the last sample (MATG)
- **The maths is ONE object that comes back**: MATG put its numbers on three different receipts/charts; here THE LEDGER (a paper receipt
  "AS BRAD LEA TELLS IT") returns three times and evolves on the words (PAID 367K -> OFFERED 500K on "500" -> OFFERED struck, SOLD 380K on
  "380" -> +$13,000 counting up on "thir-teen thousand dollars" -> FOR 3.5 YEARS), so a stranger can follow a four-number story.
- **A quoted voice gets a visual, not a stock actor**: the sales guy is a CALL card whose waveform is driven by the actual voice track.
- **Affan's 2026-10-23 rules are asserted in the spec**, not eyeballed: face runs <= 4 s (max 2.7 s here; MATG's s14 Kipp ran 2.8 s
  untouched at the end), zoomkeys on every speaker run (MATG used a 2 %/s drift), head_track + head_lock, the hook's small line at cap 51
  (MATG 46), 60 fps delivery.
