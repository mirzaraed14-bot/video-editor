# bpmoney-umbrella-policy: Onyx sample Short for BiggerPockets Money (Scott Trench & Mindy Jensen) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 ≈20:10: DELIVERED, both looks, 24 fps native (no Topaz / no 60 fps), awaiting Affan's review.**
  - YT: `outputs/bpmoney-umbrella-policy.sample-yt.final.mp4` (= `…sample-yt.v5.mp4`, md5 fdba2a99…) = `X:\Claude Projects\Exports\bpmoney-umbrella-policy.yt.final.mp4`,
    proof `outputs/…sample-yt.proof-sheet.jpg`.
  - IG: `outputs/bpmoney-umbrella-policy.sample-ig.final.mp4` (= `…sample-ig.v3.mp4`, md5 27d87104…) = `X:\Claude Projects\Exports\bpmoney-umbrella-policy.ig.final.mp4`,
    proof `outputs/…sample-ig.proof-sheet.jpg`.
  - Both: 1080x1920 H.264, 24 fps, 682 frames, 28.42 s, AAC 48 k; -12.1 LUFS, peak -2.1 / -2.2 dBFS; no music bed; soft swishes
    only (YT 13, IG 11), each 21-22 dB under the voice beside it (`yt/cue_check.py`; a few read "weak on a phone": the subtle mode's trade-off).
  - Tad's tile is read from the main session's hi-res re-pull (`--hires`: YouTube's best is ALSO 1080p, VP9 4.2 Mb/s, a little crisper);
    frame identity proved at every joint (`work/tile_match.py`, offset 24.000 s by audio xcorr 1.000). He is never past 1.87x (YT call
    frame 1.70-1.87x; IG card 1.56-1.64x; insets 0.78-0.80x).
- **Flags for Affan (decisions, not defects):** (1) the YouTube edit shows a SLIDE over every approved word, so Tad exists only as a
  576x324 webcam tile: built as a call frame / corner inset (FX-29/57/53), never full-screen; (2) IG red type "$50M CLIENT" and
  "ONE LAWSUIT" are the approved SEQUENCING type, but "client" / "lawsuit" are not his words in the cut; (3) the approved YT "$50,000,000
  counter" now RISES whole on "fifty" (blue rule on "million"): a count-up showed figures he never says (advisor, v5); the $10M label rises too;
  (4) the YT hook card slides in (kit design), so frame 0 shows it as a blur streak (IG frame 0 is clean); (5) the London bus clip
  carries readable bus ads (wellman, "bus driver vacancies"); (6) "And" before "Umbrella insurance" was dropped (19.15/19.18 read
  clean both ways); the cut ends on "today" (main session); (7) lip sync not measurable on a 40 px mouth (r <= 0.12 at every lag):
  the section was cut with both streams at 0 from the show's own upload, no shift applied; (8) IG captions show the hero "$3,000"
  WITH its thousands comma (the YT kit writes "$3K"): a grey area for the punctuation rule.
- How to rebuild (from the job folder): `python work/cut/make_edl.py …` + splice (see § The cut) → `python work/patch_transcript.py`
  → `python yt/sound.py` → `bash yt/run.sh panels.py [--hires]` → `python yt/build_spec.py` →
  `python ../../presets/youtube-shorts/onyx-samples-youtube/kit/yt_build.py projects/bpmoney-umbrella-policy vN` (from the repo) →
  `python yt/cue_check.py`; IG: `bash ig/run.sh build.py [--hires]` → `bash ig/run.sh sound.py --mux N` → `python yt/cue_check.py ig/work/mix`.
  Shared word anchors: `yt/plan.py`. Tad's tile: `yt/panels.py` TileSource (1080p cut, or `--hires` + `work/hires_offset.json`).
- **2026-10-31 ≈19:20: cut DONE (28.42 s, 682 f @ 24), BRIEF written.**
- Cut: `work/cut/make_edl.py` → `transcript/cuts.json` → `outputs/bpmoney-umbrella-policy.mp4` (splice.sh, AMPLIFY 0 dB measured,
  audio-qa joints clean; the 5 "ambience holes" are the source's own gated-mic silence, -70..-80 dB between words, not a crossfade fault).
- **The picture constraint (told the main session ≈18:58):** YouTube's edit shows Long Angle's slide #21 (+ Tad in a 576x324 webcam
  tile at (1303, 378)) over EVERY approved word: the screen-share runs source 489.5-622.9 s (YouTube 0:36:09-0:38:23). No full-frame
  Tad exists for these words. Main session (≈19:05): a hi-res re-pull of YouTube 0:36:00-0:38:30 is first in its queue (lands as
  `source/OAY3d8zRPDo_0.36.00-0.38.30_hires.mp4`, t0 = YouTube 0:36:00 = window src 480); build everything now, Tad's panel swappable;
  if it isn't there at render time, render from the 1080p tile at <= 1.9x and say so.
- Main session (≈19:05) Q2: **end on "...go buy this today." and cut** ("That's the highest value thing you can do right now." dropped).
- The slide: allowed only as a brief PiP if every figure shown matches his words; it carries $500-$2,750, "1 in 5 with $25M+", a
  State Farm 120 % line → **kept OFF screen** (no crop of it shows only his numbers).

## QA round 1 (one sonnet fresh-eyes reviewer, defects only, on YT v3 + IG v2; scratch `work/qa-r1/`) -> fixed in YT v4 / IG v3; YT v5 = the $50,000,000 figure rises whole (no count-up), frames 56-113 checked: only $50,000,000 ever reads
1. MED (YT): "UNDER $3,000" ran to x 1006 (YouTube's button zone) -> the price bar + label moved left, label 56 px (x 485-935).
2. MED (IG) / LOW-MED (YT): the "Umbrella" / "UMBRELLA" label rode the growing layer's top through the caption line (and the YT
   watermark) -> anchored LOW inside the layer, just above ENDS.
3. LOW-MED (YT): the "$10 MILLION" label counted through $2 / $7 / $9 MILLION -> it now rises in whole (only his number shows).
4. LOW (IG): the red hero "top" sat on the red block -> that line has no hero.
5. LOW (YT): the header "UMBRELLA INSURANCE" ended 11 px from the inset -> 36 px.
- Kept, with reasons: IG "$50M CLIENT" / "ONE
  LAWSUIT" (approved SEQUENCING type, flagged); YT hook blur on frames 0-4 (the kit's slide-in); four YT captions 0.21-0.23 s early after
  a pause (the kit's never-blank chain, as on TFTS); the bus ads (harmless, flagged); the hook card "He told a $50M man / buy this
  today" (true to the source: the button is what he told that man; the cut only drops "And I was like,").
- Passed: format (682 f, 24 fps, both), audio (-12.1 LUFS, TP -2.1/-2.2, 13 joints click-free), the end (0.027 s after "today", no
  extra syllable), all 109 words in order in both looks, chunk <= 19 chars, only ! ? quotes, the quoted line yellow (YT), constant
  caption y, lips never covered, every graphic on its word (<= 0.25 s), no stray / black / frozen frames, no stock faces, no watermarks.
- `workflows/graphics-qa.py` does NOT apply (long-form 16:9 only): skipped on record, as on TFTS.
- Head steps at the joints inside the webcam tile (only the s07 inset and none of the T shots carry joints): <= 8.1 tile px
  (<= 6.5 px in the 0.8x inset) (`work/faces/tile_faces.json`).

## The job
- Show: **BiggerPockets Money** (Scott Trench & Mindy Jensen; part of BiggerPockets), 123K. Their Short named in the permission email:
  "Best Type of FI?". Handoff tone: personal finance / FI; in-house media (a long shot); must be a BP **Money** clip (it is).
- Approved pick: `projects/_onyx-batch6-2026-10/SEQUENCING.md` § 9 "★ Pick: The under-$3,000 policy he told a $50M client to buy
  today" (APPROVED by Affan 2026-10-31). Guest **Tad Fallows, managing director at Long Angle** (the episode's own intro, ep2 scout
  0:00:43). Long Angle is a paid sponsor of the show: no logo, no plug; the kept span has none ("most of our members" is cut).
- Source: YouTube OAY3d8zRPDo "The Banks, Credit Cards, and Insurance the Top 1% Recommend", window 0:28:00-0:44:00 =
  `source/OAY3d8zRPDo_0.28.00-0.44.00.mp4` (1920x1080, **24 fps**, H.264 2.4 Mb/s, AAC 44.1 k; main session's pull). No formats.txt.
- Clock map (FFT cross-correlation of the RSS mp3 against the window's audio, normalised peak 0.999, `work/scout/xcorr.py`):
  **window src = mp3 - 1817.31 s**; raw section `raw/bpm_umbrella.mkv` = window src 504.000-618.000 (frames 12096-14832, x264 CRF 12,
  PCM 48 k, both streams start 0, 2736 f); **raw t = src - 504 = YouTube t - 2184**.
- **NO Topaz, NO 60 fps** (Affan 2026-10-31 18:30): the QA'd native-rate (24 fps) render is the final. GPU = transcription only, under lock.sh gpu.
- Deliver: `outputs/bpmoney-umbrella-policy.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\bpmoney-umbrella-policy.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## The beats (followed exactly; found by their WORDS in raw/; beat 2 re-ordered as written)
1. HOOK (raw 94.75-102.90): "I was actually literally yesterday talking with a guy who has, I don't know, north of $50 million. And
   he's like, oh yeah, I've heard of this umbrella insurance. Tell me what that's about."
2. (raw 5.79-11.08 + 17.13-18.71): "there is some tail risk that I'm driving along and I hit a bus full of young doctors … that could
   totally ruin someone."
3. (raw 19.17-25.92): "Umbrella insurance basically picks up your liability wherever your normal insurance ends and adds a lot of money
   on top of it."
4. (raw 32.29-37.71): "the price is incredibly low. It's under $3,000 a year. You can get $10 million of coverage."
5. BUTTON (raw 103.58-106.25): "you need to stop everything else you're doing and go buy this today." (cut there, main session Q2)
- Voices: Tad only. The $50M man is QUOTED by Tad ("oh yeah, I've heard of this umbrella insurance. Tell me what that's about.") →
  his own caption colour (README § 5). No Mindy / Scott inside any kept span (checked on the words).

## The cut (measured; `work/cut/make_edl.py`, re-ASR `work/cut/fw_slices.py` / `fw_words.py` WITH and WITHOUT the filler prompt)
- Hook start 94.75: WhisperX dropped a fast **"you know"** (94.45-94.70) between "successful." and "I"; faster-whisper hears it with
  context, prompt or not. 94.75 sits on the -40 dB gap and reads "I was actually" both ways (94.44 / 94.58 / 94.625 all kept "you know").
- Dropped connectives: "But" before "there is"; "but" before "that could" (17.06-17.10 burst); "And" before "Umbrella" (19.06-19.17:
  19.15 and 19.18 read "Umbrella insurance" both ways; earlier cuts read "Braille"); "but" before "the price"; "And I was like," before
  "you need to". End 106.25 in the -31 dB dip after "today" ("you know" follows at 106.28).
- Pauses (10 ms RMS < -36 dB for >= 0.15 s) cut to ~0.09 s at 8 places (2.10 s); the room is a gated mic (pauses -70..-80 dB).
- Full-cut stumble pass (`work/cut/fw_cut.py`): N reads the approved words exactly; P adds a "you know" before "tell me" (N clean; a
  0.15 s lip/breath burst 101.82-101.97 sits in the cut pause, only its -35 dB tail 101.96-101.97 is kept).
- Number word times (cut clock, envelope-checked): "fifty" 3.82, "million" 4.06-4.70; "three thousand" 22.92-23.61; "ten" 24.62,
  "million" 24.80-25.13: WhisperX within 2 frames, kept.

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on
## 9 labelled sheets made for this job, `work/catalog/singles_1-4.jpg` (79 singles) + `strips_1-5.jpg` (58 strips))
- **Fits this video** (a remote guest in a call tile; one mechanism told with three numbers that are his words):
  - **FX-29 Float Frame + FX-57 Propped Phone Call** ("a recorded video call is never shown full-screen") → Tad's webcam is never
    blown up: it floats as a rounded frame over a blurred, darkened plate of his own room. The constraint becomes the look.
  - **FX-53 HUD Host Inset** → the cards fill the frame while Tad stays LIVE in a small corner inset (the show's own screen-share
    grammar), so his lips are on screen beside every number (face-cam rule: never > 4 s of face alone).
  - **FX-71 Funnel Count** → "$50 MILLION" as a huge counted number with a tiny caps label, landing on "million".
  - **FX-65 Team Banner Bars** (as stacked layers) → YOUR NORMAL INSURANCE as a grey layer, ENDS marked on its top, the UMBRELLA layer
    stacking on top on "on top of it".
  - **FX-69 Lone Yellow Bar** → the price-vs-coverage pair: a tiny UNDER $3,000 A YEAR bar beside the one tall $10 MILLION bar in the
    accent; the umbrella layer from the stack IS that tall bar (one object that returns and evolves).
  - **FX-23 Pointer Tag** → TAD FALLOWS / MANAGING DIRECTOR, LONG ANGLE beside his frame.
  - **FX-58 Speaker-Coded Subs** → the $50M man's quoted line in its own colour.
  - **FX-33 Dust Void Drop** → the button's plain policy form as a single artifact on a dark field (approved YT plan: "the button over a
    plain policy form").
- **Not used before on an Onyx/Scott sample:** FX-29/FX-57 as the speaker's own frame, FX-53 with a live guest inset over cards, FX-71
  as the hook's number, FX-65 stacked layers.
- **Leaned on recently, avoided here (batch variety rule):** TFTS's hero set (FX-11 before/after split, FX-09 rows, FX-18 quote,
  FX-16 portal), Pollak's (FX-27 red word quote, FX-79 echo, FX-28 dossier, FX-40 portrait), Pincus's read-along highlighters (FX-34)
  and web DOCs.

## What this one does better than the last ones (rule 5; vs TFTS 2026-10-31, Pollak 2026-10-31, Pincus 2026-10-31)
1. **A webcam tile built as a designed frame, not an upscaled crop**: earlier samples cropped 9:16 out of studio cameras; here the guest
   only exists at 576x324, so he floats as a call frame over his own room and rides as a live inset over the cards (lips always in sync
   on screen, nothing blown up past 1.8x).
2. **One object carries the whole mechanism**: the $50M count → the insurance stack (normal policy ends, the umbrella layer on top) →
   that umbrella layer becomes the $10M bar beside the tiny $3,000 one. Every number on screen is a number he says, landing on his word.
3. **Tighter**: 28.4 s, every pause over 0.15 s cut to ~0.09 s, a filler WhisperX never saw caught by a context re-ASR.

## GATE 5 (facts on screen)
- Numbers on screen are ONLY his: "$50 MILLION" (north of), "UNDER $3,000 A YEAR", "$10 MILLION" (of coverage). No advice card of our
  own; the button is his sentence. The slide's figures stay off screen.
- Tad's tag = the episode's words: "managing director at Long Angle". No Long Angle logo.
- Hook card: "HE TOLD A $50M MAN / BUY THIS TODAY" (his story, his words; no claim about the man's coverage).

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/OAY3d8zRPDo_0.28.00-0.44.00.mp4` | main session (YouTube OAY3d8zRPDo, window 0:28:00-0:44:00, 1080p24 H.264 + AAC) | 285.6 MB | the source (not pulled by me) |
| v2 | `raw/bpm_umbrella.mkv` | LOCAL derivative of v1 (src 504-618 s) | 97.8 MB | the section the EDL cuts from |
| b1 | `yt/assets/broll/mk18208-umbrella-open.mp4` | Mixkit 18208 "Fashion woman dressed in red" (opens a black umbrella), 2160p, Mixkit Free licence | 51.0 MB | "this UMBRELLA insurance": the literal noun (hands + umbrella opening, no face as a stand-in) |
| b2 | `yt/assets/broll/mk18218-umbrella-vertical.mp4` | Mixkit 18218 "Young woman in a park opening her umbrella to cover", 1080x1920 native vertical | 33.9 MB | alternate for b1 (native 9:16) |
| b3 | `yt/assets/broll/mk72-steering-wheel.mp4` | Mixkit 72 "Dashboard of a car" (hands on the wheel), 2160p | 83.7 MB | "I'm DRIVING along" |
| x1-x4 | `audio/sfx-src/<id8>.wav` | Epidemic Sound SFX (`DownloadSoundEffect`, WAV), the soft swish family only (SUPERHERO rule), none used in any earlier job (grep of projects/): 287d8894 "Swooshes, Swish, Organic, Cloth" (5.8 s) · e8991406 "Swooshes, Whoosh, Airy, Cloth, Movement 02" (4.8 s) · 1c9e4e2b "Swooshes, Whoosh, Airy, Light 03" (4.7 s) · 5a77c212 "Swooshes, Whoosh, Airy, Light 02" (5.7 s); each slice tonal-checked before use | ≈ 1-2 MB each | one soft swish per graphic entrance, rotated, sized to the move |
| b4 | `yt/assets/broll/mk4263-london-bus.mp4` | Mixkit 4263 "Ride through the streets of London" (red city buses), 1080p | 62.5 MB | "I hit a BUS" (a bus passing; no crash, nobody hurt) |

