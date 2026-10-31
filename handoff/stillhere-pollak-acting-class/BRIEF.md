# stillhere-pollak-acting-class: Onyx sample Short for Still Here Hollywood (Steve Kmetko) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 18:20: BOTH 30 fps CHECKS DELIVERED; the 60 fps FINALS WAIT FOR THE GPU** (off-limits since 16:35 per the coordinator).
  Checks: `outputs/…sample-yt.check30.mp4` (= v4) and `outputs/…sample-ig.check30.mp4`, copied to `X:\Claude Projects\Exports  stillhere-pollak-acting-class.yt.check30.mp4` / `.ig.check30.mp4` (+ `.check30.proof-sheet.jpg` each): 1080x1920, 29.97, 821 f,
  27.39 s, −12.1 LUFS, −2.2 dBTP, AAC; built from the 1080p cut (no Topaz yet).
  **RESUME = `bash work/gpu_queue.sh all`** once the main session frees the card (every Topaz call inside `lock.sh gpu`): Topaz base
  (Iris 2x + Chronos per take) → watermark check (LOOK at `work/topaz_wm_check.jpg`) → `yt/build_spec.py` (fps_out 59.94, base_hq,
  cards at 59.94) → `yt_build final` → `yt/mg60.py` (native 59.94 card frames over Chronos' on s09/s10/s13: Chronos morphs type) →
  `sharpen-picture.py` (cards excluded: mg-*) → `yt_build final --skip picture,overlay` → cam60 (Chronos x2 of the 4K base; its
  watermark check) → `ig/build.py` 60 fps (that SC 2 / cam60 path has NEVER run yet) → `ig/sound.py --mux` → proof sheets. Then a
  person LOOKS at both watermark checks + the 4K stills, and only then `bash work/gpu_queue.sh export` (Exports `.yt/.ig.final.mp4`).
  `workflows/graphics-qa.py` does not apply (no hf-graphics plan in this kit); QA = cue_check (both), the verify scripts, the
  sonnet reviewer (r1) and the targeted r2 checks.
  Check after: the A-shot crops from the 4K base (`yt/work/stills/`), one dossier decode frame and one stamp frame at full size,
  `work/verify_yt.py` / `work/verify_ig.py` on the finals (frame numbers x2).
  QA r2 (targeted, on v4): split joint 294 locked (eye x 514 → 519); 270 left UNLOCKED (locking it snapped 62 px in v3; unlocked
  it slides with his move, as the v2 review passed); IG zoom continuous 755-780; IG "yes I do" line from frame 99 (voice 3.33 s);
  stamp inside x 148-931; caption outline clear of the watermark (1185).
  Checks so far: `outputs/…sample-yt.v2.mp4` (+ proof sheet), `outputs/…sample-ig.check30.mp4` (+ proof sheet); both −12.1 LUFS,
  −2.2 dBTP, 821 f, end 0.001 s after "took"; swishes 19-23 dB under the voice (yt/cue_check.py, ig/cue_check.py PASS subtle).
  **QA r1 (one sonnet reviewer, defects only, `work/review/`)** → fixed: (1) the split top's head snapped 90 px at joint 294 (head_lock
  covered A shots only: SPLIT joints added); (2) the IG zoom stepped 27 px at 767 (`wt("what")` found the FIRST "what": keys out of
  order; YT s14 had the same key) → the second "what"; (3) IG stage text carried commas → removed; (4) the IG "yes I do" line and the
  "I hate school" stack landed ~0.2 s late: WhisperX is 0.2-0.25 s late there → `patch_transcript.py` RETIME from the cut's envelope;
  (5) YT caption outline over the watermark's top → watermark_y 1185; (6) the EXCUSES stamp's slam reached x 45-1035 for a frame →
  172 px type, 1.22x slam; the excuses card opened near-black for 0.25 s → its first line is up from the card's first frame;
  IG wide shot: Pollak's cap touched the window edge → cx 0.47. Unsure/kept: the Improv picture and "FILE / LOS ANGELES" are not
  in the spoken words (his own telling just before beat 1 places it at the Improv in LA: GATE 5).
- Source clock: the RSS episode time EQUALS the YouTube time (FFT xcorr of ep2.mp3 740-920 s vs the source window: lag 260.011 s, ncc
  0.996), so **source t = episode t − 480 s**. `raw/pollak_section.mkv` = source 299.9997-429.9997 (frame-exact seek, both streams at 0,
  x264 CRF 12, PCM) = **raw t = episode t − 779.9997**. WhisperX large-v3 ran on CPU int8 (log `work/transcribe.log`: "cpu, int8").
- **The cut** (`work/cut/make_edl.py` pieces → splice refine → polish → `tight` TH −36 dBFS, every quiet run ≥ 0.08 s cut to 0.07 s):
  24 segments, 27.39 s, AMPLIFY_DB −2 (measured 0 ran the limiter hard; Onyx default −2), audio-qa: limiter transparent, timeline exact.
  Verbatim faster-whisper pass on the cut (CPU) reads the approved beats both ways (`work/cut/fw_cut_v2.txt`); the prompt-only "hmm"
  after "I thought" is invented by the prompt (plain reads clean; the envelope shows "I | thought | I hate" with no filler).
  Edge pins: "a woman" starts 5.595 (the polish onset was "But"), "she gave me" 32.895 (32.93 cut into the "sh"), the "uh" in "gave
  me, uh, a scene" FORCED out (33.40-34.04), the "um"s after "manager" and "listen" dropped between pieces.
  **"But" kept before beat 6's "those"**: "those" is fused with it (slice ASR from 114.93 / 115.02 / 115.05 still reads "But";
  only 115.075, inside the vowel, drops it), so the turn word stays rather than clip "those". Flag for Affan.
  audio-qa's one "JOINT CLICK" (4.37 s, "do. | she gave") is the "sh" fricative onset, not a step: |diff| rises 0.05 → 0.12 → 0.17
  over 15 ms and stays there 60 ms (measured). Two "ambience holes" (12.88, 16.55 s) are room-tone dips (−48..−56 dBFS) at joints.
  Lip sync: mouth-darkness vs voice xcorr, best lag 0 / −1 frame on the two clean spans (`work/cut/avsync.py`).
  `work/cut/patch_transcript.py` (RUN AFTER EVERY SPLICE) makes the caption transcript match what is heard: drops two phantom
  boundary words, adds "a", "other", "you", "those" (WhisperX never emitted them; the verbatim pass did).
- Camera map of the cut (frames): Pollak single 0-330, the show's WIDE two-shot 330-509, Pollak 509-658, Kmetko's single 658-704,
  Pollak 704-821. Joints `work/cut/segstarts.txt`; Topaz segments = joints + 330, 509, 658, 704.

## The job
- Show: **Still Here Hollywood** (Steve Kmetko, ex-E! News anchor; co-host Jim), 448K. Tone (handoff 2026-10-31): nostalgia, older
  audience, emotional moments land. Their own hit for reference: "Bruce Willis Is Not Aware There's An Issue - Kevin Pollak" (391K).
- Approved pick (Affan 2026-10-31, `projects/_onyx-batch6-2026-10/SEQUENCING.md` § 5 ★, miner table `stillhere/PICKS.md` C1 Variant A):
  **"The real reason he never took an acting class"** (Kevin Pollak, story, ≈45 s). Source: YouTube jVMm7reve0g "Kevin Pollak 'Usual
  Suspects'", 1080p30, window 0:08:00-0:21:00 = `source/jVMm7reve0g_0.08.00-0.21.00.mp4` (pulled by the main session).
- Both looks from ONE cut: YouTube (Sean Ryan look, `presets/youtube-shorts/onyx-samples-youtube/`) + Instagram (neon window,
  `presets/instagram/neon-window/`, newest kit = Pincus `ig/`).
- Deliver: `outputs/stillhere-pollak-acting-class.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\stillhere-pollak-acting-class.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## The beats (followed exactly; found by their WORDS; nothing added, nothing re-ordered)
1. HOOK (ep 0:13:05): "A woman came up… I'm a manager. Do you want a career as an actor? Yes, I do."
2. (0:13:25): "She gave me a scene. She said, take this to the other room and memorize it and come back in and let's see what you got.
   And I had never done that. So of course I was horrible."
3. (0:13:25): "She said, huh, well, listen, you're a great stand up. Acting's not really for everyone, you know."
4. (0:14:16): "Again, no formal training."
5. (0:14:42): "I thought, I hate school and I'm going to learn to act from someone who's not employed."
6. BUTTON (0:14:42): "Those, I realized years later, those were all excuses. I didn't want another person telling me I didn't have what
   it took." (SEQUENCING's beat 6 keeps "I realized years later"; ends on "took", before "And if I went to an acting class…")

## Decisions (with reasons)
- **No music bed; SFX = soft Patrón-style swishes only**, one per graphic entrance / whip into a picture, cuts back to his face silent
  (memory feedback-premium-sfx SUPERHERO + UNDER HIS MUSIC: Affan replaced the batch-5 sample beds with his own songs). A bed is a
  mix-only rebuild if he wants one. Flagged.
- **Ending on his face** (the confession is HOW he says it): the last shot ≥ 3 s with a slow push (FX-40), not a line on black.
- **No stock actor plays the manager or young Pollak** (README § 10): hands/objects, real photos of him, the real Improv.
- **No third-party film/TV footage.** His film credits are carried by the hook card (text) and, if used, POSTER stills (flagged).

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on
## labelled tiled sheets (79 singles at 480x270, 58 strips at 1600 px wide), not opened one by one)
- **Fits this story** (a told memory, no documents exist, one quoted verdict, one confession):
  - **FX-27 Red Word Quote**: the manager's verdict "ACTING'S NOT REALLY FOR EVERYONE" as a verbatim quote over the frozen, darkened
    previous frame, the key word red. The heart of the video.
  - **FX-55 Red Pen Underline** (as a strike): "I HATE SCHOOL" struck through by a hand-drawn red pen line on "excuses".
  - **FX-79 Flash-Forward Echo**: the verdict card returns, struck, under the button (the payoff answers the verdict).
  - **FX-28 Dossier Readout**: a casting-file line "FORMAL TRAINING: NONE" typed on "Again, no formal training" (his words, not invented).
  - **FX-29 Float Frame**: real photos (the Improv, him on stage) as framed cards over their own blur, never blown up past their size.
  - **FX-42 Kin Tag**: the credit stack beside his face (name / actor, comedian / the films) for the IG hook.
  - **FX-40 Slow-Burn Portrait**: the confession held on his face with a slow creep in.
- **Not used yet on this kind of video** (the last Onyx/Scott ones leaned on FX-34 highlighters, FX-29 page cards, FX-66 slabs, charts):
  FX-27, FX-28, FX-55-as-strike, FX-40. Not repeated from Pincus: read-along highlighters (there is no document in this story).
- **Leaned on last time, avoided here:** web-page DOC receipts with highlighters (Pincus x5), stat charts (Patrón, MATG).

## What this one does better than the last ones (rule 5; Pincus YT/IG 2026-10-31, MATG 2026-10-23)
1. **The quoted voice gets its own visual system**: the manager's lines in their own caption colour (YT) and as a full FX-27 quote
   card, so the stranger hears TWO people in a one-man story.
2. **The ending pays off a card from the middle** (FX-79): the verdict card comes back struck under "those were all excuses", the
   strongest structural echo any sample has had (MATG flipped a chart; this flips a sentence).
3. **Nothing stock stands in for a person** (batch-2 failure) on a story with no documents: real photos of the place and the man,
   type for the abstract nouns.

## IG variant (neon window; `ig/build.py`, kit = the Pincus IG of 2026-10-31)
- **Same cut, same beats, same pictures** as the YT; the four moments SEQUENCING names are Mark Brazil STAGE STACKS (a small white
  Inter lead-in over a giant red Playfair Black Italic hero, the stack IS the caption on its beat): "Do you want / *a career as an
  actor?*" → "Acting's not really for / *everyone*" (+ "you know", THE MANAGER) → "I thought, / *I hate school*" → the closing stack:
  "I hate school" and "someone who's not employed" struck in red marker, "But those, I realized years later, / those were all /
  ***excuses***" (the biggest); "what it took" is the last caption's red hero.
- Hook on frame 0 (Mark's 10-31 title type): "Kevin Pollak / The Usual Suspects / and [A Few Good Men]" over his camera card (left, so
  the label names HIS face) and the Hollywood Improv card dealt on "a woman came up"; no captions under the title (0-3.3 s: the
  title, then the first stack).
- His camera from the cut (1080p for the check, the 4K Topaz plate + Chronos x2 for the final), tracked on the face box, pinned at
  every take's edge, mouth at window y 552 (575 put two lower-lip frames 1 px from the caption line: `lips_check` now ≥ 22 px).
  The show's own WIDE shot fills the window on "So, of course, I was horrible" (both men inside the square, the neon sign over them).
- Captions: one whole line ≤ 4 words, a 14 px eased rise (Affan's 2026-10-31 standing rule), white Inter + one red Playfair hero.
- Sound: no bed; one soft swish per entrance (the hook cards, 3 burns, 3 stack openings, the photo card), the YT's fresh slices.
- **Better than the Pincus IG (the 1 %):** (1) the stacks carry the story's four turns, the last one striking the first one's words
  (a callback inside the type, not just a returning picture); (2) the show's OWN set and neon sign fill the window once, so the
  prospect sees his studio as part of the design; (3) the manager's verdict is a stack with its speaker named (THE MANAGER), so a
  two-voice story reads as two voices without a second caption colour.

## GATE 5 (facts on screen)
- Credits on the hook (both looks): **The Usual Suspects** and **A Few Good Men** — en.wikipedia API 2026-10-31: "his roles include Sam
  Weinberg in A Few Good Men ... Todd Hockney in The Usual Suspects". The poster's leftmost man is Pollak: the Gramercy publicity
  still's own caption reads "Left to right: Hockney (KEVIN POLLAK), McManus (STEPHEN BALDWIN) ..." (`work/img/cand/u05.jpg`); he is
  circled there on "a career". No other cast member is named anywhere.
- The manager is unnamed ("I wish I could remember her name"): never named or pictured; her lines are type and her caption colour only.
- "The Hollywood Improv" picture: his own telling just before beat 1 ("when you get to LA ... I'll get you stage time at the Improv ...
  the Improv would have showcase nights ... But a woman came up after"), so the place is his; the Improv on Melrose is the LA Improv.
- The dossier card prints only what he says: NAME Kevin Pollak, WORK stand-up comic ("you're a great stand-up"), FORMAL TRAINING none
  ("Again, no formal training"); "FILE / LOS ANGELES" is the frame (he was new in town in LA). The sides page is a generic PROP
  (an invented two-line scene, no claim it is the one she gave him).
- The excuses card quotes his two reasons in his words: "I hate school", "someone who's not employed".

## Sources (yt/assets/broll; the IG reads the same files)
| Use | File | From |
|---|---|---|
| The Hollywood Improv at night, its sign + the "THE HOLLYWOOD IMPROV" marquee (DOC card, w 760: native, never blown up) | b-improv.jpg (750x1000) | Yelp photo of Hollywood Improv, 8162 Melrose Ave (s3-media0.fl.yelpcdn.com/bphoto/iGV2bn2ewmXK4ZleYCRtug/o.jpg) |
| The Usual Suspects poster (the lineup; Pollak circled; the lineup row only on YT, no half title) | b-usual-suspects.jpg (1400x2100) | IMDb media (m.media-amazon.com …MV5BNTIyN2M0…_V1_.jpg), tt0114814. LICENSING flag: studio key art, as the Daymond / Pincus press stills |
| Pollak on stage with the mic, early 1990s (a frame of a TV stand-up special: SOFT, so a float card at ~0.75x, never full-bleed) | b-standup.jpg (1280x640) | collider.com "10 Great Actors You Never Knew Were Stand-Up Comedians" (static1.colliderimages.com/…/kevin-pollak.jpg). LICENSING flag (TV frame) |
| A hand pushing a wooden door (SPLIT bottom, "come back in") | b-door-35896.mp4 (1280x720, 25 fps; the 1080 file answers 403) | Mixkit 35896 (free licence) |
| An empty room, chairs up on the tables, bookshelves ("I hate school") | b-chairs-21591.mp4 (1920x1080 24 fps) | Mixkit 21591 (free licence) |
| The show's own WIDE two-shot with the STILL HERE HOLLYWOOD neon ("So, of course, I was horrible") | the cut itself, frames 330-369 | their episode |
| sides page, FX-27 quote, FX-28 dossier, the excuses card | sides.png, b-quote.mp4, b-dossier.mp4, b-excuses.mp4 | built: `yt/cards.py` (Anton, IBM Plex Mono, Courier) |
| Swishes | assets/sfx/epidemic/ph-cloth-01/02, ph-airy-wind01, ph-brushs (sliced by `yt/sound.py`) | Epidemic (Download log x1-x8) |
Not used: no YouTube B-roll was needed (no NEEDS-YOUTUBE.md); no stock person stands in for anyone; no film/TV footage.

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/jVMm7reve0g_0.08.00-0.21.00.mp4` | main session (YouTube jVMm7reve0g, window 0:08:00-0:21:00, 1080p30 H.264) | ≈ 135 MB | the source (not pulled by me) |
| p01 | `work/img/cand/p01.*` (candidate) | https://static1.colliderimages.com/wordpress/wp-content/uploads/2023/10/kevin-pollak.jpg (page https://collider.com/great-actors-stand-up-comedians/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p02 | `work/img/cand/p02.*` (candidate) | http://hipe.historicimages.com/images/rf/adp787.jpg (page https://historicimages.com/products/adp787) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p03 | `work/img/cand/p03.*` (candidate) | https://images.wolfgangsvault.com/m/large/ZZZ009639-PP/kevin-pollak-promo-print-1990.jpg (page https://www.wolfgangs.com/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p04 | `work/img/cand/p04.*` (candidate) | http://kevinpollak.squarespace.com/storage/layout/bio-COMEDY.jpg (page http://kevinpollak.squarespace.com/bio/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p05 | `work/img/cand/p05.*` (candidate) | http://media.baselineresearch.com/images/327774/327774_full.jpg (page https://www.tvinsider.com/people/kevin-pollak/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p06 | `work/img/cand/p06.*` (candidate) | http://media.baselineresearch.com/images/301972/301972_full.jpg (page https://www.tvinsider.com/people/kevin-pollak/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p07 | `work/img/cand/p07.*` (candidate) | http://media.baselineresearch.com/images/151847/151847_full.jpg (page https://www.tvinsider.com/people/kevin-pollak/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p08 | `work/img/cand/p08.*` (candidate) | http://media.baselineresearch.com/images/309207/309207_full.jpg (page https://www.tvinsider.com/people/kevin-pollak/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p09 | `work/img/cand/p09.*` (candidate) | http://media.baselineresearch.com/images/245075/245075_full.jpg (page https://www.tvinsider.com/people/kevin-pollak/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p10 | `work/img/cand/p10.*` (candidate) | https://cdn.sonemic.net/i/1200/s/dc4b9ead9eeabe0ebe5c2b6709c22761/1532893 (page https://rateyourmusic.com/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p11 | `work/img/cand/p11.*` (candidate) | https://m.media-amazon.com/images/M/MV5BOTY3NGM0MzUtMWI4YS00NmY0LTllNzYtNDZiNjY1OTEzZTZmXkEyXkFqcGc@._V1_FMjpg (page https://www.imdb.com/title/tt12815584/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| p12 | `work/img/cand/p12.*` (candidate) | https://swiftmedia.s3.amazonaws.com/pacific.swiftcom.com/images/sites/5/2016/09/15102954/TD_TD200410101160005A (page https://www.tahoedailytribune.com/news/coming-home-to-comedy) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: Pollak on stage / young |
| i01 | `work/img/cand/i01.*` (candidate) | https://media.timeout.com/images/100776589/1920/1080/image.jpg (page https://www.timeout.com/los-angeles/comedy/hollywood-improv) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i02 | `work/img/cand/i02.*` (candidate) | https://media.timeout.com/images/100776593/image.jpg (page https://www.timeout.com/los-angeles/comedy/hollywood-improv) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i03 | `work/img/cand/i03.*` (candidate) | https://i.improv.com/wp-content/uploads/2018/05/10185956/location-thumb.jpg (page https://improv.com/hollywood/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i04 | `work/img/cand/i04.*` (candidate) | https://s3-media0.fl.yelpcdn.com/bphoto/mAQwWIxLYoN-i54Xk3TTbg/o.jpg (page https://www.yelp.com/biz/hollywood-improv-hollywood) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i05 | `work/img/cand/i05.*` (candidate) | https://s3-media0.fl.yelpcdn.com/bphoto/KZ5bIR7m46EWux5SfWFYvQ/o.jpg (page https://www.yelp.com/biz/hollywood-improv-hollywood) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i06 | `work/img/cand/i06.*` (candidate) | https://s3-media0.fl.yelpcdn.com/bphoto/iGV2bn2ewmXK4ZleYCRtug/o.jpg (page https://www.yelp.com/biz/hollywood-improv-hollywood) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i07 | `work/img/cand/i07.*` (candidate) | https://s3-media0.fl.yelpcdn.com/bphoto/lr7y_6VZLnJ-mjFPS5Lsjg/o.jpg (page https://www.yelp.com/biz/hollywood-improv-hollywood) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i08 | `work/img/cand/i08.*` (candidate) | https://s3-media0.fl.yelpcdn.com/bphoto/F3gUC91MgvtV_iFJCrNNmg/o.jpg (page https://www.yelp.com/biz/hollywood-improv-hollywood) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| i09 | `work/img/cand/i09.*` (candidate) | https://s3-media0.fl.yelpcdn.com/bphoto/S1WyUtPD39RQrcuQ9mucXg/o.jpg (page https://www.yelp.com/biz/hollywood-improv-hollywood) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: the Hollywood Improv |
| u01 | `work/img/cand/u01.*` (candidate) | https://image.tmdb.org/t/p/original/rWbsxdwF9qQzpTPCLmDfVnVqTK1.jpg (page https://www.themoviedb.org/movie/629-the-usual-suspects) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: The Usual Suspects lineup (his credit) |
| u02 | `work/img/cand/u02.*` (candidate) | https://www.themoviedb.org/t/p/original/tH2daaaLsNHmQeye807szxvmjxY.jpg (page https://www.themoviedb.org/movie/629-the-usual-suspects) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: The Usual Suspects lineup (his credit) |
| u03 | `work/img/cand/u03.*` (candidate) | https://images5.alphacoders.com/339/thumb-1920-339250.jpg (page https://wall.alphacoders.com/big.php?i=339250) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: The Usual Suspects lineup (his credit) |
| u04 | `work/img/cand/u04.*` (candidate) | https://m.media-amazon.com/images/M/MV5BNTIyN2M0ZjUtMDQxZi00ZGVhLWI4MTUtNWJiM2M2M2FkMWYwXkEyXkFqcGc@._V1_.jpg (page https://www.imdb.com/title/tt0114814/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: The Usual Suspects lineup (his credit) |
| u05 | `work/img/cand/u05.*` (candidate) | https://www.xmarkstheshop.com.au/wp-content/uploads/2024/12/IMG_6554.jpg (page https://xmarkstheshop.com.au/) | ≈ 0.1-3 MB | Bing image search in the built-in browser (curl Bing is region-skewed today); candidate for: The Usual Suspects lineup (his credit) |
| m-prev | `work/img/mixkit/<id>-360.mp4` (previews: 14956 35954 48165 21595 21598 21591 21812 21813 21817 1123 2514 16293 2490 35896 46217 39849 45923 39856 23112 39848) | assets.mixkit.co/videos/<id>/<id>-360.mp4 (Mixkit free licence) | ≈ 1-3 MB each | pick the hallway/door, classroom, paper shots |
| m1 | `yt/assets/broll/b-door-35896.mp4` | assets.mixkit.co/videos/35896/35896-720.mp4 (1080 answers 403; Mixkit free licence: a hand pushing a wooden door, no face) | ≈ 10-20 MB | "take this to the other room" |
| m2 | `yt/assets/broll/b-chairs-21591.mp4` | assets.mixkit.co/videos/21591/21591-1080.mp4 (Mixkit: an empty room, chairs up on the tables, no people) | ≈ 10-20 MB | "I hate school" |
| x1-x5 | `assets/sfx/epidemic/ph-*.wav` (repo library) | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none used before (grep of MANIFEST + every BRIEF 2026-10-31; the TFTS builder took e435dfaf / e62847da today): a48476fb "Whoosh, Soft, Short 03" · 6cc8bdbd "Whoosh, Soft, Long 02" · e1c332ac "Swish, Low, deep, Cloth Movement, Singular 02" · 955a277a "Swish, Low, deep, Cloth Movement, Singular 01" · f50bf56c "Whoosh, Airy, Wind 01" | ≈ 0.1-0.5 MB each | the Patrón-family soft swishes, one per graphic entrance, sized to the move |
| x6-x7 | `assets/sfx/epidemic/ph-medium-wind.wav`, `ph-low-short02.wav` | Epidemic 8481181d "Swooshes, Whoosh, Medium, Wind" · 890e3d48 "Swooshes, Whoosh, Low, Short 02" (x1 Soft Short 03 + x2 Soft Long 02 measured 14.5 / 15.5 dB tonal, above the ~13 Patrón gate: not used) | ≈ 0.3-1 MB | more airy swishes for rotation |
| x8 | `assets/sfx/epidemic/ph-brushs.wav` | Epidemic 1a973b75 "Swooshes, Whoosh, Brushs" (x6/x7 measured 16.3 / 16.0 dB tonal: not used) | ≈ 0.5 MB | one more soft swish |
