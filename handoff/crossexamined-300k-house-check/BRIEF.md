# crossexamined-300k-house-check: Onyx sample Short for CrossExamined (Frank Turek) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 20:40: FINALS DELIVERED, awaiting the main session / Affan's review.** `outputs/crossexamined-300k-house-check.sample-yt.final.mp4`
  (= YT v5) and `.sample-ig.final.mp4`, copies `X:\Claude Projects\Exports\crossexamined-300k-house-check.yt.final.mp4` / `.ig.final.mp4`
  (md5-identical), proof sheets `outputs/…sample-yt.proof-sheet.jpg` / `…sample-ig.proof-sheet.jpg`. Both: H.264 1080x1920 24 fps,
  807 f, 33.625 s (ends 0.055 s after "houses."), AAC, −12.1 LUFS, TP −2.3 / −2.2, decode clean; swishes 18-23 dB under his voice
  (`yt/cue_check.py`, `ig/cue_check.py` PASS subtle).
  **QA r1 (one sonnet reviewer, defects only; scratch `work/review/`) → fixed:** (1) head hops at the jump cuts: the 60 ms cut
  "but | think" (raw 36.02-36.08) made a 5-frame take → removed (`make_edl.py` MIN_CUT 0.08; the cut is now 15 segments, 807 f);
  the YT eye track overshot 56-80 px right after joint 171 (a one-sided edge fit while his head moves fast) → **kit opt-in
  `head_edge_pin`** (`kit/yt_picture.py`, backup `.bak-2026-10-31`; specs without the key render bit-identical), spec 12 frames:
  eye step at 171 now 7 px vs 13 around, 340: 8, 546: 12 px (`work/headgate.py` on the delivered frames); IG: the edge pin takes the
  median of the 3 detections nearest the edge (an outlier box at 170) and head x follows the EYES (he turns his head across 171:
  box 16 px, eyes 38 px) → 18 px vs 10 around; 504: 4 px. (2) invented numerals on the check (cheque No., MICR line, cents, 00/100)
  → removed (`work/gfx.py`): the check carries only his $300,000. (3) the YT memo split showed "$ 30" at the right edge → the amount
  box sits off-frame. (4) IG credit now "Dr. Jay Richards / Heritage Foundation". (5) IG PRICE-tag swish over "the" → 3 dB down.
  (6) IG: the opening words were uncaptioned under the hook title → captions now run from frame 0 (CLAUDE.md Rules: "never suppress
  them under a hook"; the coordinator's TFTS fix), the hook's two cards shrunk to 460x330 between the title and the caption line.
  Kept by design: two YT
  chunks lead their word by 0.20-0.21 s (the kit's lead + joint pin; 1 frame over the 0.18 s spec); "DR JAY RICHARDS" (the kit's
  caption cleaner drops the period in the tag); the leak burns' 1-2 bright frames (designed).
  `workflows/graphics-qa.py` does not apply (no graphics-plan.json on this kit path); the kit's gates + `yt/cue_check.py`,
  `ig/cue_check.py`, `ig/build.py` lips_check, `work/headgate.py` and full-res frame checks (f285 big number vs caption + watermark:
  clear; f325 memo split: the amount box off-frame, the watermark over the dark scrim) stood in for it.
  OPEN for Affan: IG captions now run under the hook (coordinator, CLAUDE.md Rules) vs his War Dogs note "no captions while the hook
  text is up" (neon-window LESSONS 2026-10-31 #1).
- 2026-10-31 19:40: YT v3 + IG v1 built (24 fps, 805 f, 33.54 s), then ONE sonnet reviewer.
  YT: `outputs/…sample-yt.v3.mp4` (v1: A shots at z0 1.2 put the captions on his mouth → **the caption line / split seam moved to
  y 1180 for the whole video**, A z0 1.04 with the eye line at 0.33: his webcam face is 43 % of the source height, so this is the
  widest full-height crop; v2: the memo split's check sat under the captions + watermark → a dark scrim over the panel's top).
  Swishes 19-23 dB under the voice (`yt/cue_check.py`; a few read "WEAK" on that script's −20 phone bar, which is the old loud bar;
  the subtle Onyx band is ig/cue_check's −28). The kit captions "$300,000" as "$300K" (numerals rule); the cards print "$300,000".
  IG: `ig/build.py` (Pincus/Pollak kit + this beat plan + `work/gfx.py` objects) → `ig/work/picture24.mp4` → `ig/sound.py --mux` →
  `outputs/…sample-ig.v1.mp4`; `ig/cue_check.py` PASS subtle (loudest −18.0 dB). Mouth at window y 540 (lips_check ≥ 20 px).
  The cut: `work/cut/make_edl.py` pieces → splice refine → polish → `tight` (TH −31 dBFS, quiet runs ≥ 0.08 s → 0.07 s, MIN_CUT 0.06 so
  a weak fricative inside a word is never cut) + FORCED cuts "uh" (raw 55.80-56.27) and "crazy" (64.52-65.14); AMPLIFY_DB −2
  (Onyx default). 16 segments. audio-qa: timeline exact, 15 joints clean, limiter transparent; 2 "ambience holes" (8.62 s, 14.92 s)
  = room-tone dips at joints. Verbatim faster-whisper on the cut (`work/cut/fw_cut_v1.txt`, `fw_cut_v1b.txt`, GPU under the lock)
  reads the approved beats; his drawn "a— massive" stays (continuous voice, no gap to cut). `work/cut/patch_transcript.py` (RUN
  AFTER EVERY SPLICE): drops the phantom "which", adds "our" (parents), re-times "for" / "$300,000" / "say" from the envelope.
  Camera in the cut: Jay full 0-358, the show's two-up 358-472 (covered by the inflate card), Jay full 472-805; joints
  `work/cut/segstarts.txt`. Faces scanned every frame (`yt/work/faces.json`, copied to `ig/work/`): eyes y ≈ 413, mouth ≈ 597 px.
  YT spec: `yt/build_spec.py` (13 shots: 3 face A, 2 FIT real footage + 1 B, 2 SPLIT, 5 built cards from `yt/cards.py` +
  `work/gfx.py`), 49 chunks, 13 soft swishes (`yt/sound.py`), head lock [171, 176, 338, 544].
- **CHANGE from Affan (coordinator 18:30), overriding BUILDER-BRIEF steps 3 + 6: NO Topaz (no Iris, no Chronos) and NO 60/48 fps.**
  Both looks build at the source's native **24 fps** straight from the 1080p cut; the QA'd render IS the final. No GPU needed
  (WhisperX / faster-whisper stay on CPU).
- A/V sync of the section: no gross offset. Mouth-open frames around the pause before "almost" (raw 62.26-62.60) open 2-3 frames before
  the voice onset (normal anticipation); the face-tracked mouth-darkness xcorr on 28-36.8 s peaks at lag 0 (r 0.27); both stream
  start_times 0 (`work/cut/avsync.py`, `avsync2.py`, `work/sync_62.jpg`).
- Words (faster-whisper large-v3, both with and without the filler prompt, `fw_slices_r1.txt`): he says "a percentage of **our**
  income" and "compared to, say, **our** parents or grandparents" (WhisperX dropped the second "our"); "for $300,000" = "for" 40.34-40.66,
  "three hundred thousand" ≈ 40.70-41.77 (RMS), no "dollars"; a 0.45 s pause after "check" (39.87-40.33).
- Source clock: FFT xcorr of the RSS ep1.mp3 (1880-1940 s) vs the source window: **source t = RSS t − 1430.19** (ncc 0.975), so
  YouTube t = RSS t − 1430.19 + 1500 (YouTube runs ~70 s later than the RSS). `raw/richards_section.mkv` = source 460.000-540.000
  (frame-exact seek at 24 fps, x264 CRF 12, PCM 44.1k, both streams at 0) = **raw t = source t − 460 = RSS t − 1890.19**.
- Layout of the raw section (scene cuts): Jay full-frame webcam 23.125-45.042, the show's two-up (Frank left, Jay right) 45.042-52.208,
  Jay full 52.208-80. Burned-in: the CE bug (top-right, x 1778-1857, y 55-135) and a "PREMIERE" badge (bottom-right, x 1510-1820,
  y 975-1030). Jay's face is a big webcam face (lips ~55 % down the frame): measure before choosing A vs SPLIT.

## The job
- Show: **CrossExamined** (Frank Turek; Christian apologetics ministry), 939K. Tone (handoff 2026-10-31): keep it clean and respectful.
- Approved pick (Affan 2026-10-31, `projects/_onyx-batch6-2026-10/SEQUENCING.md` → "AFFAN'S REVIEW 2026-10-31" → "Revisions sent" →
  **CrossExamined v2**, APPROVED in "AFFAN'S REVIEW #2"): **"Why houses cost so much: imagine a $300,000 check"** (guest Dr. Jay
  Richards, ≈40 s). Source: YouTube cz2c6hceXF4 "Is Socialism More Christian Than Capitalism? with Dr. Jay Richards", 1080p24, window
  0:25:00-0:38:00 = `source/cz2c6hceXF4_0.25.00-0.38.00.mp4` (pulled by the main session).
- Both looks from ONE cut: YouTube (Sean Ryan look, `presets/youtube-shorts/onyx-samples-youtube/`) + Instagram (neon window,
  `presets/instagram/neon-window/`). Templates: the batch-6 sibling `projects/stillhere-pollak-acting-class/` (scripts only, beat plans
  rewritten; no renders, cards or SFX slices copied) and the Pincus `ig/` kit.
- Deliver: `outputs/crossexamined-300k-house-check.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\crossexamined-300k-house-check.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## The beats (followed exactly; found by their WORDS in raw/richards_section.mkv; nothing added, nothing re-ordered)
1. HOOK: "The federal government does things to the mortgage market to try to help people buy homes. And so you think, okay, that looks
   good on the surface, but think of it this way." (raw 28.13-36.79; "in which" before it cut)
2. "Imagine that the government sent everyone a check for $300,000. But the only thing they could use it for would be to buy a house.
   What is going to happen to the price of housing?" (36.85-46.82)
3. "It's just going to inflate the cost of housing. And so that's, unfortunately, what has happened." (49.38-53.40; "If you remember
   your first lesson from economics," 47.18-49.28 cut: not in the approved beat)
4. "Houses as a percentage of [our] income end up just being a massive, massive amount compared to, say, parents or grandparents in
   the 1970s," (54.08-62.26; "so that" before it cut; "massive, massive" is his emphasis and stays)
5. BUTTON: "almost entirely the result of … housing policies that were intended to help people afford houses." (62.60-68.44; "crazy"
   64.64-65.12 cut; ends on "houses." before "Same thing, unfortunately, in college")
Out (SEQUENCING): Frank's immigration line before it (raw 0-13.5) and everything before "the federal government".
Loop: "…intended to help people afford houses." → "The federal government does things to the mortgage market to try to help people
buy homes." (reads as one thought).

## Decisions (with reasons)
- **No music bed; SFX = soft Patrón-style swishes only**, one per graphic entrance / whip into a picture, cuts back to his face, text
  swaps and stamps silent (memory feedback-premium-sfx SUPERHERO + UNDER HIS MUSIC; Affan lays his own beds on the samples). A fresh
  Epidemic set, rejected by title first, then tonal p90 ≤ ~13.
- **GATE 5 is tighter than the README's receipts rule here** (the task: "a data card is fine only for numbers he says"): the only
  figures on screen are **$300,000** and **the 1970s**, both his. No income-share numbers, no chart of real data, no named agency or
  program (he names none), no politician. The check is HIS hypothetical, so it is a built, generic check (no real agency seal).
- **His credit:** "DR. JAY RICHARDS" / "HERITAGE FOUNDATION" (en.wikipedia API 2026-10-31, "Jay W. Richards": "an American analytical
  philosopher ... the William E. Simon Senior Research Fellow ... at the Heritage Foundation"; the episode title calls him Dr. Jay
  Richards). Never "economist".
- **Delivery rate 24 fps, no Topaz** (Affan 18:30 via the coordinator: "30 fps is good enough for prospecting"; this source is 24p).
- **No stock actor stands in for anyone** (README § 10); hands, houses, documents and real 1970s photos only.

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on
## labelled tiled sheets: 79 singles at 480x270 in 4 sheets, 58 strips at 1600 px wide in 9 sheets, every tile read)
- **Fits this story** (an economics thought experiment told with ONE hypothetical object, two spoken figures, no documents):
  - **FX-33 Dust Void Drop**: the $300,000 check isolated on an empty dark field with sparse dust as it is dealt on "check".
  - **FX-71 Funnel Count**: "$300,000" as huge type with a small caps label under it (HOUSES ONLY) — the number he says, nothing else.
  - **FX-55 Red Pen Underline**: one hand-drawn red mark on the check's memo line "A HOUSE" on "the only thing ... buy a house".
  - **FX-41 Year Ghost**: "1970s" in a heavy wide grotesk over a real 1970s photo on "parents or grandparents in the 1970s".
  - **FX-29 Float Frame**: the real 1970s photo as a framed card over its own blur (archive never blown up past its size).
  - **FX-79 Flash-Forward Echo**: the check returns on the button ("housing policies that were intended to help people afford
    houses"): the same object, now the cause.
  - **FX-40 Slow-Burn Portrait**: the last line held on his face with a slow creep in.
  - **FX-42 Kin Tag** (YT `tags` / IG credit): his name + Heritage Foundation beside his face on the hook.
- **Not used yet on this kind of video**: FX-33, FX-71 (as the number itself, not a counter), FX-41 (Year Ghost has never shipped on
  an Onyx sample), the price tag that physically INFLATES (the verb drawn).
- **Leaned on by the last ones, avoided here:** Pollak's FX-27 quote card + FX-28 dossier, Pincus's five read-along highlighters
  (FX-34), Patrón / MATG data charts (no data may be shown here).

## What this one does better than the last ones (rule 5; Pollak YT/IG + Pincus YT/IG, 2026-10-31)
1. **One object carries the whole argument through its states**: the check is dealt (FX-33), its amount writes on "$300,000", its
   memo is marked HOUSE ONLY, its money is shown pouring into a house's price tag that inflates, and it returns on the button as the
   policy (FX-79). Pollak's echo returned a card; here the object IS the cause-and-effect chain.
2. **The verb is drawn literally**: "inflate the cost of housing" = a price tag that swells like a balloon on "inflate", not a chart.
3. **Zero invented numbers**: only the two figures he says land as big type (FX-71 $300,000, FX-41 1970s); the comparison to the
   1970s is a real 1970s photo, not a made-up statistic.
4. IG: Mark Brazil's 10-31 type (small sans label over big bold sans, key words on a red box) for the stage beats, where Pollak's IG
   used the older Playfair stacks.

## IG variant (neon window; `ig/build.py`)
- Same cut, beats, shot edges (read from yt/spec.json) and objects as the YT. Hook 0-1.88 s on frame 0: Mark Brazil's 10-31 title
  ("Dr. Jay Richards / Heritage Foundation" / "Why houses" / [cost so much] on a red box) over his camera card + the US Capitol card
  dealt on "government" (two 460x330 cards above the caption line); captions run from frame 0. Then float cards of the real footage (hands signing, house keys), his camera (tracked, pinned at every
  take's edge), the stage beats carrying the check (dealt, "$300,000" on a red box, memo circled), the inflate stage (suburb card +
  PRICE tag), his camera on "Houses as a percentage of our income" (the YT's split becomes cam → stage at the "income | end" joint),
  the massive stage (tag vs pay stub), the 1973 suburb full-window with "1970s", the callback stamp, the last line on his face.
  Three warm leak burns where the source changes (to the footage, to the check, to the 1973 photo).
- Captions: one whole line ≤ 4 words, a 14 px eased rise (Affan 2026-10-31), white Inter + one red Playfair hero per line.
- **Better than the Pollak IG (the 1 %):** the stage beats carry ONE object through its states (check → memo → tag → callback) instead
  of type stacks; the real footage plays as moving float cards (not stills); the comparison to the 1970s is a real 1973 photo with
  the SAME tag, small.

## GATE 5 (facts on screen)
- $300,000: his number ("a check for $300,000"). "1970s": his words. "HOUSE ONLY" / "HOUSES ONLY": his condition ("the only thing they
  could use it for would be to buy a house"). Nothing else numeric.
- Credit: Wikipedia (above). No agency, program, party or politician named or pictured.
- Illustrations, not data: the check's memo "A house only" is his condition in plain words; the PRICE tag inflating ("inflate the cost
  of housing"), the tag dwarfing a pay stub labelled OUR INCOME ("houses as a percentage of our income ... a massive, massive amount")
  and the same tag SMALL on the 1973 suburb ("compared to ... the 1970s") carry no numbers, axes or percentages (no ratio is claimed).
- The check reads "THE GOVERNMENT" (his words: "the government sent everyone a check"), no seal, no agency, no bank.

## Sources (yt/assets/broll; the IG reads the same files)
| Use | File | From |
|---|---|---|
| "government" — the US Capitol, a hyperlapse drive up to it (FIT float frame: 720p, never blown up) | b-capitol-11800.mp4 (1280x720 29.97, src_in 0.6) | Mixkit 11800 (free licence; the 1080 file answers 403) |
| "mortgage market" — hands signing papers at a table (no face) | b-sign-307.mp4 (1920x1080 23.976, src_in 1.0) | Mixkit 307 (free licence) |
| "help people buy homes" — a hand holding up house keys (FIT with a crop that leaves her blurred face out) | b-keys-15065.mp4 (1280x720, src_in 6.0, crop x 0.02-0.62, y 0.36-1.0) | Mixkit 15065 (free licence) |
| the inflate card's house (a float frame over its own blur) | b-suburb-24945.mp4 (1280x720, src_in 2.0) | Mixkit 24945 (free licence) |
| "in the 1970s" — a new suburban development near the Potomac River, April 1973 (FX-41 over it) | b-1973-suburb-547211.jpg (2001x3000) | NARA 547211, DOCUMERICA (US EPA), public domain, via upload.wikimedia.org |
| the check, the memo, the price tag, the pay stub, the stamp | mg-check / mg-memo / mg-inflate / mg-massive / mg-seventies / mg-callback.mp4 | built: `yt/cards.py` + `work/gfx.py` (LibreBaskerville, Dancing Script, IBM Plex Mono, Anton) |
| Swishes | assets/sfx/epidemic/cx-cloth-blanket, cx-low-long02, cx-whooshs, cx-short-low-dry (sliced by `yt/sound.py`) | Epidemic (Download log x1-x6) |
Pulled, not used: b-roofs-48394.mp4, b-bills-18262.mp4 (the plan changed to built cards). No YouTube B-roll needed (no NEEDS-YOUTUBE.md).

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/cz2c6hceXF4_0.25.00-0.38.00.mp4` | main session (YouTube cz2c6hceXF4, window 0:25:00-0:38:00, 1080p24 H.264) | 143 MB | the source (not pulled by me) |
| m-prev | `work/img/mixkit/<id>-360.mp4` (previews: 41161 49851 11800 5717 31214 46504 307 15065 36159 6518 3420 30995 2890 28603 44382 18299 47006 39167; round 2: 48394 24945 1303 9532 18262 9533 27396 42336) | assets.mixkit.co/videos/<id>/<id>-360.mp4 (Mixkit free licence) | ≈ 1-3 MB each | pick the Capitol, mortgage-signing, keys, suburb and money shots (faceless) |
| m1-m6 | `yt/assets/broll/b-capitol-11800.mp4`, `b-sign-307.mp4`, `b-keys-15065.mp4`, `b-suburb-24945.mp4`, `b-roofs-48394.mp4`, `b-bills-18262.mp4` | assets.mixkit.co/videos/<id>/<id>-1080.mp4 (720 if 1080 answers 403; Mixkit free licence) | ≈ 10-40 MB each | the Capitol drive ("federal government"), hands signing ("mortgage market"), keys handed over ("help people buy homes"), suburb aerials ("houses" / "price of housing"), $100 bills ("a check for $300,000" plate) |
| w-prev | `work/img/nara/<n>.jpg` (800 px thumbnails: NARA 547211, 553130, 547829, 557361, 557360, 557367) | upload.wikimedia.org thumbs via the en.wikipedia imageinfo API (DOCUMERICA, US EPA 1971-77, public domain) | ≈ 0.1-0.3 MB each | pick a real 1970s house / family-at-home photo for "parents or grandparents in the 1970s" |
| w1 | `yt/assets/broll/b-1973-suburb-547211.jpg` | https://upload.wikimedia.org/wikipedia/commons/0/04/THE_CLEARING_IS_A_NEW_SUBURBAN_DEVELOPMENT_NEAR_THE_POTOMAC_RIVER_-_NARA_-_547211.jpg (NARA 547211, DOCUMERICA, April 1973, public domain) | ≈ 2-4 MB (2001x3000) | "in the 1970s": a real new suburb of 1973 from the air (no people) |
| x1-x6 | `assets/sfx/epidemic/cx-*.wav` (repo library) | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none used before (grep of MANIFEST + every BRIEF / sound script 2026-10-31; today's TCO / TFTS / Pollak builders took 8f1a6bfe 38a49746 073cf199 f040a2a4 c52cf22f a22e3c51 279037ea 79611651): abbebdeb "Cloth, Flap, Flap, Blanket, Whoosh" · abbe24be "Swooshes, Whoosh, Low, Short 01" · 56f2ebeb "Swooshes, Whoosh, Low, Short 04" · ed8a466b "Swooshes, Whoosh, Low, Long 02" · be924dac "Swooshes, Whoosh, Short, Low, Dry" · 81383ee2 "Swooshes, Whoosh, Whooshs" | ≈ 0.2-0.6 MB each | the Patrón-family soft swishes (the approved shorts-cooked set used Low Short 03 / 05 of the same family), one per graphic entrance, sized to the move |
