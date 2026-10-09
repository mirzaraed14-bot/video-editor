# affan-afterhours-facecam — the simple face-cam explainer (the style that got the views)

**What this is.** The creator's own words (2026-09-21): *"we're dieting down our editing … go back to an editing style
which was working on our channel … the normal face-cam zoom-ins with some cut zoom-ins, and here and there a very
strong cut to get a point across funnily … sometimes I slow my voice down so it sounds more exaggerated … the
Extended Look is our bread and butter."* Top result 170k views. This folder is that style, **measured off the
creator's own masters**, so it can be reproduced from numbers rather than from memory.

**🔒 2026-10-08, the creator: "don't use my friends editing style, only use the ones I [edited]".** The Fuel System reference below (and every number measured off it) is the FRIEND'S hand — background only, never the spec. **▶ Read [`CREATOR-HAND.md`](CREATOR-HAND.md) first (2026-10-08).** It is measured off the creator's OWN shipped timelines (PC Release, Collector's Box, Game Informer), clip by clip, and wins wherever it differs from the numbers below — which were measured off two exports, the 170k one cut by the creator's friend. Biggest corrections: cut zooms are a razor + static scale at a median 121–136 % (not +25), the push is their saved "105/110 GTA LF Zoom Preset", slow-downs follow the jokes (0–11), overlays are inset over a colour matte (since 09-30), pops sit at ≈ −18 dB, and the meme layer (colour-bars glitch, Vine boom, memes, cricket) is theirs.

**Where it sits.** The channel is `presets/youtube/affan-afterhours/` (PLAYBOOK, LESSONS, sfx.json stay there and
apply). That folder documents two earlier looks — the documentary (paused) and the motion-graphics explainer
(`projects/gta6-travis-scott-hired/STYLE.md`). **This is the third, and the default for the next videos.** Each style
keeps its own folder; nothing here is read on a job in another style.

**References (the creator's exports, all 1080p60):**

| video | views | master | measured in |
|---|---|---|---|
| GTA 6's Fuel System Isn't The Problem…This Is (6:53) | 170k | `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\GTA Cars.mov` | `reference/fuel-system/` |
| Rockstar's RISKIEST GTA 6 Move Yet (5:32) | 35k | `…\Final Renders\Gta gun.mov` | `reference/riskiest/` |
| GTA 5 vs GTA 6: Everything You CAN'T Do Anymore (7:20) | 17k | no local master; YouTube `ZEDhaEk79I4` | **dropped by the creator 2026-09-22** ("leave the last video") — two references are the spec |

The numbers, side by side: [`reference/NUMBERS.md`](reference/NUMBERS.md). Per video: `report.md` (the derived
measures), `probe/summary.md` + `probe/sheet.png` (every cut as a frame), `visual-catalogue.md` (every overlay and
card, read frame by frame), `transcript/words.json`. The tools: `workflows/style-probe.py` → `style-set.py` →
`style-zoom.py` → `style-audio.py` → `style-report.py`; run them on any new reference the same way.

---

## 1. The shape of the edit (measured)

| | Fuel System (170k) | RISKIEST (35k) | the rule |
|---|---|---|---|
| visible changes | **19.6/min** | 26.5/min | **~20–25 changes per minute**, never a still frame for long |
| hard cuts | 11.3/min | 18.2/min | 11–18/min; the difference is the game-montage density |
| cold open (0–60 s) | 15/min | **44/min** | the first minute cuts 1.5–2.5x faster than the body |
| cut zooms (in) | **5.2/min** | 4.3/min | **~5 per minute**, one every 12 s on average |
| cut zoom size | x1.27 (p25–p75 1.22–1.39) | x1.26 (1.17–1.32) | **+25 %**, occasionally +40–60 % for a big hit |
| cut zoom hold | 1.2 s | 1.1 s | **~1 s then out** (or straight into the next change) |
| cut zoom on a hard cut | 31 % | 42 % | a third ride a jump cut; two thirds snap inside a held shot |
| gradual push | 0.99 %/s | 1.21 %/s | **~1 %/s**, so a 10 s run drifts 100 → 110 |
| reframes (same-size jump cuts) | 3.2/min | 4.2/min | the jump cuts land on gestures |
| face on screen | 79 % | 77 % | **~80 %**; overlays are seasoning, not the meal |
| face run | median 9.6 s, max 39 s | 7.2 s, max 44 s | a face run is a paragraph, 7–10 s |
| overlay runs | 3.3/min, median 3.8 s | 3.6/min, median 3.7 s | **3–4 per minute, ~4 s each**, almost all game footage |
| longest without the face | 22.8 s | 7.0 s | a game sequence can carry 20+ s when it is the evidence |
| posters / cards | **11** (9 designed + 2 plain text, 8 runs) | 4 | **1–1.6 per minute**, held ~5–6 s, on a quotable declarative punchline or a quote — the sentence being said, set in type (the motion-graphics explainer had 37 built scenes; these are typeset sentences) |
| words / min | 211 | 203 | fast, dense, pauses ≥ 1 s only 2–3 per video |
| slow-downs on the FACE | 1 | 2 | **1–2 per video**, ~0.5–0.6x speed, 0.5–2.5 s, pitch KEPT |
| slow motion on the INSERTS | routine (0.5x, 0.2x, 0.15x, down to a near-freeze 0.03x) | some | **game footage and reaction clips are slowed as a matter of course**; the face almost never is |
| luma | 0.34 | 0.28 | bright LED room; no dark cinematic frames |
| first / last shot | face / face | face / face | opens on the face, closes on the face |

**How to read it.** The 170k video is the calmer of the two on cuts and the busier on zooms and on posters: it changes
the picture ~20 times a minute, a third of those by snapping the face closer, and it typesets eleven of its own
sentences as cards. The 35k video cuts harder (a 44/min cold-open montage), zooms a little less and cards four times.
Both keep the face on screen four fifths of the time, use game footage in short bursts of ~4 s three or four times a
minute, slow the inserts rather than the face, and end cold on the face.

## 2. The face grammar (what the pipeline applies)

This is the same three-move grammar the channel already runs (`lanes/premiere/face-nests.py`), with this style's
numbers:

1. **Nest** every face run (a run = the face between two overlays).
2. **The gradual push on the nest:** ~1 %/s, so 100 → 110 over 10 s; a rate, capped at +10 % (LESSONS 2026-09-20).
3. **The cut zoom inside the nest:** an instant **+25 %** snap (range +17 to +40, a rare +50/+60 for the biggest hit)
   on the word that lands, **held ~1 s**, then back out or on to the next change. **About five per minute** — every
   12 s of face on average, so a 10 s run gets one, a 20 s run two or three. A third of them coincide with a jump
   cut (cut-and-zoom at once); the rest snap inside the held shot.
4. **The jump cuts** are the pace: ~4 same-size reframes a minute on top of the hard cuts, landing on gestures.

## 3. The two voice devices (measured, both real)

- **The slow-down.** 1–2 per video, on a punchline or a mock-serious line: **~0.5–0.6x speed, 0.5–2.5 s, audio pitch kept**
  (no pitch drop was measurable in either video; the stretch shows in word timing and in a periodic frame hold at the
  native 60 fps, which is how each one was verified). Fuel System 4:05 *"you pay to register your"* (~0.5x, 2.7 s);
  RISKIEST 4:32 *"moving, in more choice"* (~0.5x, 2.3 s) and a brief one at 2:38 *"warning if you"*. Premiere: a speed change on the face clip with **Maintain Audio Pitch
  on**, video frame-sampled (the frames step, they do not blend).
- **The hard chop.** The creator's "cut it midway while I'm saying it": rarer than it sounds — one measurable case in
  Fuel System (1:08.4, the word "the" cut at −12 dB) and none in RISKIEST. It is a spice, not a seasoning. Treat as
  **at most one or two per video, on a line whose joke is being cut off.**

## 4. Overlays (measured; the frame-by-frame catalogue per video is `reference/<video>/visual-catalogue.md`)

- **Game footage is the main overlay.** Fuel System: 31 inserts = ~20 game-footage runs + 8 card runs (11 cards) + a
  real interview clip + a screenshot + one meme clip. RISKIEST: 20 runs = 14 game-footage runs + 4 cards + 3 found
  stills + a logo card. The footage: the GTA 6 Extended Look and trailers, GTA V / San Andreas gameplay where the line
  is about the old games. Always **full-frame and sharp with the game's own HUD left in**, ~4 s a run, three to four
  runs a minute, dropped in **where the line names an action or a place that exists in the game**. Nothing is ever an
  inset, a PiP or a split screen.
- **Inside a game run the cuts are fast**: RISKIEST's cold-open montages cut every 0.4–0.7 s (44 cuts inside 20
  runs); Fuel System's are calmer (10 inside 23).
- **Cards are earned, and the 170k video earns more of them**: Fuel System 11 (1.6/min), RISKIEST 4 (one every 83 s).
  Each is a verbatim quote, a numbered rule or a tweetable declarative punchline — the sentence he is saying, set in
  type. Jokes played straight, opinions, asides and predictions get NOTHING; the face carries them. Found artefacts
  are cut in raw and unannotated: a real photo, a screenshot (the GTA V weapon wheel, a rival's channel page), the
  creator's own earlier thumbnail as a callback, a full-bleed Rockstar logo card.
- **Speed ramps live on the B-roll.** Fuel System slows its inserts routinely: the 9 s GTA V theft take at ~0.2x
  (the "wiggle wiggle hot-wire thing" in comic slow motion), a night drive at ~0.15x, the heist board at ~0.11x, and
  two near-freezes used as reaction shots — Rob Nelson's interview clip at ~0.03x with a slow push (a smug freeze,
  3.8 s) and the TGG channel page at ~0.07x. Most short GTA 6 inserts sit at ~0.5x.
- **The meme insert:** 1.4 s of an unrelated live-action clip (a man shoving a cheap Spider-Man) two seconds into
  the 170k video, pillarboxed, then punched to full width for a 24-frame beat. No setup, no callback.
- **The only bug:** a canned bottom-left SUBSCRIBE animation, twice per video (Fuel System 2:34.5 and 5:40.5, ~8.5 s
  each), dropped mid-sentence with no cue. Nothing else is ever on screen with the face: no logo, no lower-third, no
  name tag, no captions.
- **Two long graphic-free stretches per video** (36 s and the 39.5 s close in Fuel System): the argument, the asides and
  the opinion are face only.
- **The cold open** starts on the face (both videos), lands its first insert within 2–8 s, and has no title card, no logo
  sting, no channel branding.

## 4b. The poster template (read off RISKIEST's four cards, pixel-identical geometry)

- **The headline is the sentence he is saying at that instant, near verbatim** — not a summary, not a label. If the
  line would survive as a tweet, it gets a card. (All 15 cards across both videos.)
- **Geometry:** a 16:9 landscape card, **~72 % of the frame** (RISKIEST 1390×782 px, pixel-identical on all four),
  dead centre, rounded corners, hard edge, **soft drop shadow, tilted 1–3°** in Fuel System, over a **heavily blurred,
  darkened plate of GAME footage** (never the face shot — full-frame game inserts are always sharp with the HUD left
  in; card plates are always defocused, and that contrast is the whole showing-vs-telling language). It **grows 8–15 %
  over its hold (~2 %/s)** and nothing else on it moves: no text reveal, no element animation. Held **3.2–7 s (median
  ~5.5 s)**, one outlier at 10.6 s. Enters and exits on a **hard cut** — no fade, no wipe, no slide, in either video.
  Behind a long card the plate may hard-cut to other footage while the card stays put. **A run of cards** is allowed:
  Fuel System fires four escalating punchline cards back to back (3:23–3:46), each resetting smaller and growing again.
- **Art:** flat-vector Vice City sunset (deep blue → magenta → peach), palm silhouettes, a city skyline, thin white
  HUD corner ticks; or a photoreal GTA render with a HUD element (weapon-wheel arc, reticle brackets, a tracker box).
- **Type:** headline words **UPPER CASE** in a **heavy condensed grotesque** (Anton / League Gothic class), **cream**
  `#F6F1DC`–`#F7EFDA` (never pure white on a designed card), dark drop shadow; kickers in a **lighter condensed caps,
  letterspaced, small** (Oswald class). Fuel System also drops an **italic serif** for a wry aside ("you gambled on a")
  and a light serif for a sentence-case murmur — two or three type classes per card at most. The two plain-text
  posters ("STEP 1: YOU CHECK AN APP") are pure white with a black outline over a bright blurred plate.
  Text block left- or right-aligned against an image on the other side; **ONE accent word per card, the load-bearing
  one**, in hot pink `#EE2A9A` (orchid `#DF6BE1` over near-black). **A colour code:** pink = GTA 6 and the new rule;
  the one card about GTA 5 (the old way) is **green** `#A1D7AD`.
- **What earns a poster:** a verbatim quote or a stated rule with a number in it. Nothing else. A found artefact (a
  screenshot, a photo, an old thumbnail) is cut in full-frame, unannotated, with a slow scale, 1.8–2.6 s.
- **No other text exists:** no captions, no lower-third, no logo bug, no name tag, no end card. The "Rob Nelson"
  portrait at 0:48 carries no name.

## 4c. The comedy and emphasis devices (with the timecodes they were read off)

| device | what it is | RISKIEST | the rule for the next video |
|---|---|---|---|
| **punch to extreme close-up** | face jumps from base (~32 % of frame height) to ~59 % for ~1 s on the punchline word, then cuts away | 0:11.4 "impossible.", 2:44.4 double punch, the final shot 5:29.6 | one or two per video, on THE word |
| **the chronology cut** | "since 2001" hard-cuts GTA 6 into a 3 s retro montage (SA → Vice City → GTA 3) at 0.4–1.6 s per clip; the edit does the date | 0:29–0:34 | whenever the line names an era |
| **ugly on purpose** | the retro clips are soft, 4:3-ish, one carries another channel's watermark, uncropped, next to crisp GTA 6 | 0:30.6–0:33.8 | do not clean up old-game footage |
| **the self-callback** | his own previous video as a YouTube list row on black, no arrow, no "link below" | 1:43.4 | when a line references the last video |
| **the no-B-roll take** | the longest shot of the first half (18.6 s) is him miming with nothing to cut to; the void is the joke | 1:55–2:14 | when the joke is the mime, do not cover it |
| **the headless frame** | he stands up, the camera does not follow: torso and spatula-mic, head cut off, still talking | 2:10 | leave it; never reframe it |
| **the mimic cut** | "tap, tap, tap, tap" → four sprint clips in 3 s; a one-line aside → the densest 7-clip montage of the video | 4:50, 5:01 | let the cut rate act the line out |
| **the polite quote card after an insult** | "God damn it Rob" → Rob's own words set beautifully | 3:29 | the design politeness is the gag |
| **the cold ending** | extreme close-up, points at lens, drops the hand, flat stare, cut. No end screen, nothing kept clear | 5:29.6–5:32.4 | end on the face, cold |
| **the slow-down** | § 3 | 4:32 (Fuel System 4:05) | 1–2 per video |
| **the frozen reaction shot** | an interview clip slowed to ~0.03x with a slow push: the source frozen mid-half-smile while the narration promises his quote | Fuel System 0:36.6 | when a real person is about to be quoted |
| **comic slow motion on the action** | the 9 s hot-wire take at ~0.2x under a line about how fast it used to be | Fuel System 0:59–1:08 | slow the insert, not the face |
| **the zoom burst** | six crop levels in four seconds inside one continuous take, some held 0.2 s, the audio never cuts | Fuel System 6:04.8–6:08 | once, on a rant |
| **the broken composition** | the face shoved into the right third looking out of frame left on "what the—" | Fuel System 4:55.2 | on a reaction line |
| **the card run** | four escalating punchline cards back to back, 23 s | Fuel System 3:23.6–3:46.4 | when the jokes come in a list |
| **the meme insert** | an unrelated live-action clip, pillarboxed, punched full, never referenced again | Fuel System 0:02 | optional, once |

**The prop:** a wooden cooking spatula with the DJI lav clipped to its top, held like a stage mic (RISKIEST); a large
red-grille mic on a stand in the 170k video. **The set:** a lit back wall — lavender `#D299F4` (Fuel System) or LED
green `#5BAC5D` (RISKIEST) — the `skool` neon on the left, a brown leather armchair lower-left, a dark monitor edge
frame-right; medium close-up, face slightly camera-right of centre, generous headroom at the base size.

**And the cards ship with typos** ("PROPERTY'S ARE TOO TRACEA BLE", "alot", "leoonida"; RISKIEST "INFRONT"). Not a
style rule — but the pipeline's copy check will catch what a 5 a.m. build did not.

## 5. What this style is NOT

No motion-graphics scenes, no puppets, no per-line posters, no dark cinematic look, no captions. The Travis Scott
explainer's 37 graphics were the *previous* direction; this style spends that effort on cut rhythm and the face.
Google/Instagram pictures still get the channel's overlay frame and are enhanced in Higgsfield when soft
(`feedback-sourced-stills-must-be-hq`), and Higgsfield stills stay an option for a line no footage can show.
