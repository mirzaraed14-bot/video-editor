# crossexamined-300k-house-check: Onyx sample Short for CrossExamined (Frank Turek) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 18:55: BRIEF + catalog pass written; source section cut + transcribed (CPU int8, `work/transcribe.log`); A/V sync
  checked; faster-whisper slice pass done (`work/cut/fw_slices_r1.txt`), joint tests running (`work/cut/fw_join_r1.txt`); B-roll
  candidates being pulled (Mixkit previews). Next: the EDL (`work/cut/make_edl.py`) → splice → tight pass → transcript patch.**
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

## GATE 5 (facts on screen)
- $300,000: his number ("a check for $300,000"). "1970s": his words. "HOUSE ONLY" / "HOUSES ONLY": his condition ("the only thing they
  could use it for would be to buy a house"). Nothing else numeric.
- Credit: Wikipedia (above). No agency, program, party or politician named or pictured.

## Sources (yt/assets/broll; the IG reads the same files)
| Use | File | From |
|---|---|---|
| (filled as each is chosen) | | |

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/cz2c6hceXF4_0.25.00-0.38.00.mp4` | main session (YouTube cz2c6hceXF4, window 0:25:00-0:38:00, 1080p24 H.264) | 143 MB | the source (not pulled by me) |
| m-prev | `work/img/mixkit/<id>-360.mp4` (previews: 41161 49851 11800 5717 31214 46504 307 15065 36159 6518 3420 30995 2890 28603 44382 18299 47006 39167; round 2: 48394 24945 1303 9532 18262 9533 27396 42336) | assets.mixkit.co/videos/<id>/<id>-360.mp4 (Mixkit free licence) | ≈ 1-3 MB each | pick the Capitol, mortgage-signing, keys, suburb and money shots (faceless) |
| m1-m6 | `yt/assets/broll/b-capitol-11800.mp4`, `b-sign-307.mp4`, `b-keys-15065.mp4`, `b-suburb-24945.mp4`, `b-roofs-48394.mp4`, `b-bills-18262.mp4` | assets.mixkit.co/videos/<id>/<id>-1080.mp4 (720 if 1080 answers 403; Mixkit free licence) | ≈ 10-40 MB each | the Capitol drive ("federal government"), hands signing ("mortgage market"), keys handed over ("help people buy homes"), suburb aerials ("houses" / "price of housing"), $100 bills ("a check for $300,000" plate) |
| w-prev | `work/img/nara/<n>.jpg` (800 px thumbnails: NARA 547211, 553130, 547829, 557361, 557360, 557367) | upload.wikimedia.org thumbs via the en.wikipedia imageinfo API (DOCUMERICA, US EPA 1971-77, public domain) | ≈ 0.1-0.3 MB each | pick a real 1970s house / family-at-home photo for "parents or grandparents in the 1970s" |
| w1 | `yt/assets/broll/b-1973-suburb-547211.jpg` | https://upload.wikimedia.org/wikipedia/commons/0/04/THE_CLEARING_IS_A_NEW_SUBURBAN_DEVELOPMENT_NEAR_THE_POTOMAC_RIVER_-_NARA_-_547211.jpg (NARA 547211, DOCUMERICA, April 1973, public domain) | ≈ 2-4 MB (2001x3000) | "in the 1970s": a real new suburb of 1973 from the air (no people) |
| x1-x6 | `assets/sfx/epidemic/cx-*.wav` (repo library) | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none used before (grep of MANIFEST + every BRIEF / sound script 2026-10-31; today's TCO / TFTS / Pollak builders took 8f1a6bfe 38a49746 073cf199 f040a2a4 c52cf22f a22e3c51 279037ea 79611651): abbebdeb "Cloth, Flap, Flap, Blanket, Whoosh" · abbe24be "Swooshes, Whoosh, Low, Short 01" · 56f2ebeb "Swooshes, Whoosh, Low, Short 04" · ed8a466b "Swooshes, Whoosh, Low, Long 02" · be924dac "Swooshes, Whoosh, Short, Low, Dry" · 81383ee2 "Swooshes, Whoosh, Whooshs" | ≈ 0.2-0.6 MB each | the Patrón-family soft swishes (the approved shorts-cooked set used Low Short 03 / 05 of the same family), one per graphic entrance, sized to the move |
