# successstory-vivian-5m-reaction: Affan's reaction to our Scott D. Clary (Success Story; guest Vivian Tu) sample (ABW8 sequence "Scott D Clary reaction")

## ▶ STATUS: resume here
- **2026-10-13 PREPARED IN ABW8 (main session)**: "Scott D Clary reaction" razored (38 razors at 32 edges), layout (137 clip edits, --layout-check 0 leaks), V3 showcase frames / V4 MG / V5 captions, house chain +6 dB into -6 dBFS on all 76 A1 clips, 26 SFX on A2 + A4, Spring Sometimes bed on A3 at -18.4 dB from 0.70 s with a 2 s tail fade, 25 ms Volume ramps at the music joints 38.93 / 71.05 / 172.55 (tools/afade.py), --verify 0 problems. Proof: `work/grabs-sheet.jpg`. Main-session edit to build_plan.py: whoosh-only spotlights land on a hit-soft. He exports.
- **2026-10-13: PHASE 2 DONE (graphics plan + renders; Premiere NOT touched).** `build_plan.py` → `plan.json` (facex run) →
  `overlays/captions.mov` (259 chunks, 243.483 s) + `overlays/mg/*.mov` (26 files, all 1080x1920 60 fps, frames == plan; 3.9 GB);
  `overlays.py --check`: 0 errors, 0 warnings. Review sheets + helpers: `work/plan-review/` (R01-R09 = in / mid / out of every graphic
  and every face switch).
  - HERO (Reaction C): a LOUPE-LED review. Every critique / praise of text on the page is a lens lifted out of the thing itself: the
    Short's title on its picture (7.1), its caption "there's earners" (52.6, after a select), the channel's "SUCCESS STORY PODCAST"
    thumbnail bar (62.2), our YouTube cut's split-line caption "IT WAS A GUY" (110.6), "SCOTT D. CLARY" in our Instagram cut's credit
    line (221.6, "videos I've made for him"); the two name chips lift out of Vivian's face (154.0) and out of that credit line (225.2,
    his channel chip, real avatar). Wide framings (`page` = the whole Short page, `channel`) with a 1.06 drift instead of zooms, so
    every lens lands in the page's empty dark half. Cormorant Italic accent (hook "Success Story", stat "Affan Baig"), thin-line marks,
    ONE stat card (600M), SFX focus-pull + hit-soft + ticks.
  - Counts (MG events, group items counted): select 10, loupe 5, spotlight 3, chip 2, hook_title 1, channel_card 1 (flies into the
    Short page's channel row at the 4.38 cut), stat 1 = 23 events = 1.38 per 10 s of his 167 s talk; pointing marks 78 %, label pills 0;
    + 7 showcase pieces (frame track: YOUTUBE / INSTAGRAM "variant one / two" tab). SFX 24 cues, 8 sounds, top tick-glass 29 %.
  - Face-only 10 beats = 17 pieces, 56.7 s = 23.3 %; punch-ins on "600 million", "one problem", "I practice", "packaging",
    "amazing branding" (150) and "a dead video" (165).
  - Better than Rob Dial: 0 label pills (he had 12 of 23, in the unsafe y 150 band), 78 % pointing marks (he had 2 marks), the channel
    card under the chin + flip into the page, our cuts in a showcase frame, no static hold without a drift / frame, 6 punch-ins.
  - Views: `yt_top` / `ig` (z 1.31) crop VLC's file-name overlay (y 1088-1250); the switch yt_top → yt sits on our cut's own cut
    (105.9167). The IG look stays cropped (its picture is black below y 1076). "Now this is more Scott's branding" (169.75-172.0) is
    on the split (the crop hides the file name), spotlighting the IG cut's title.
  - Fresh-eyes review: 1 round (Sonnet). Fixed: the caption list lacked "this video" (114.6-115.9: WhisperX stretched both words
    across the kept joint; restored in build_plan.py into seqwords.json, timed off the joint's measured syllables). Kept by design:
    "24/7" (the slash is the number's form, not sentence punctuation), silent showcase frames (no SFX over our cuts' audio),
    lenses/chips overlapping the edge of our cards (never a face), "Affan Baig" (his name, as on his earlier lower thirds).
  - Toolkit note for the main session (not fixed, shared tool): `apply.py --overlays` places A2 cues with `at(tr, t)`; two cues at the
    SAME time remove each other (e.g. default_sfx's thud-thin under pop-glass at a card's t0). This plan has no coincident cues.
  - Downloads: none (no Vivian avatar fetched: her chip uses the gold initial).
- 2026-10-13: Affan handed over RAW recordings before bed: camera `X:\Recordings\Onyx\C1356.MP4` + OBS `2026-10-13 09-42-34.mp4` (copied to
  `raw/`). Same pipeline as the batch-2 reactions (REACTIONS-BRIEF.md status 2026-10-12) + his 2026-10-13 rule: this reaction must be
  BETTER than the last ones (critique + fresh research: `_onyx-batch-2026-10/reactions/research-2026-10-13.md`) and different from its
  three siblings. He exports. When all four are done: save ABW8, quit Premiere, shut the PC down (memory feedback-shutdown-after-overnight-job).
- Sync: `../_onyx-batch-2026-10/reactions/s5457/sync-C1356.json`. Transcript: `../_onyx-batch-2026-10/reactions/s5457/obs-09-42-34/transcript/words.json`.
- The sample he reviews: `successstory-vivian-5m` (both looks in `X:\Claude Projects\Exports\`).
- **2026-10-13 ≈12:31: PHASE 1 DONE (rough cut, REACTION-AGENT-BRIEF steps 1-6; no plan / graphics / Premiere yet).**
  `transcript/words.json` (= s5457/obs-09-42-34, clip set) + `corrections.local.json`; voicemap (ref raw 6.3-20.9 s);
  `keep.json` → `author.py` → splice RENDER=0 + polish → splice → `work/pins.json` (13 ends, 15 starts) → `pins.py` →
  `work/split.py` (4 splits pins.py can't do + grid snap + all-pairs overlap check) → **`transcript/cuts.json` 76 segments,
  243.48 s (4:03.5) of 366.1 s raw**, every boundary on the 1/60 grid; `outputs/<job>.transcript.json`; `work/seqmap.json` +
  `transcript/words.tight.json`. Proof: `work/cutcheck.txt` (raw order), `work/seqcheck.txt` (TIMELINE order: every joint's
  5 ms RMS + a whole-cut Whisper diff against the kept words: only ASR variance left), `transcript/dead-air-qa.json` passed.
  To re-apply the pins: copy `transcript/cuts.prepins.json` over `cuts.json`, then `pins.py` and `work/split.py`.
- Cut (fillers / restarts / retakes / echoes, all measured): the "Gentlemen, today's" false start; the fumbled "this is his
  part, this is one of his videos from, obviously from his podcast episode, uh yeah"; "With-"; "this is the first time you're
  watching this video"; "I help others" (last take "I do it also for other people" kept); "So this kind of like"; "So yeah"
  x4; "A lot of,"; "It's very..."; "it's just... it's just" (last take); "if if we have, if we had, you know, what's the";
  "could you know"; "I've obviously"; "you know" x7 (4 hidden inside words WhisperX stretched) and filler "like" x4 (1 hidden); "uh" x4; the
  false start "More."; the retake "that it, it doesn't, this video" (kept: "Now, I know this video style doesn't directly
  fit"); the stutter "what, what"; "That's why I've made him two variants" (echo of his closing "that's why I give them two
  variants"); "so yeah, that's what I've done here as well"; "right"; take 1 of "I'm not going to play the whole video / the
  next variant" (last take kept); "and like makes it for"; "and stuff"; "they're"; "but definitely, uh, I, you know"; "and
  yeah, like"; "I like the consistency" (grafted: take 1 + take 2's "in the thumbnails as well"); dead air.
- **Sample-play ranges (sequence time):** the Success Story Short 19.650-38.933 + 71.050-82.350 (he paused it, talked, then
  replayed from "thousands of dollars": the replay is grafted sample-exact at "great for you | but like then", lag 49.136 s,
  so it plays through ONCE, his packaging/channel commentary between); our YouTube look 100.533-110.450 + 139.650-149.467 (his
  own pause after "It was a guy.", resumes exactly where he paused; ends on his pause at "and I am", the "de-" fragment
  trimmed); our Instagram look 172.000-198.117 (his restart "We have" + the resume after his pause, grafted one frame past
  the VLC-resume silence; ends on "hospital.", the "he" fragment trimmed).
- **EDL is NOT source-ordered at segs 50-53:** "Now this is more Scott's branding" (raw 269.28-272.58, said over the paused
  Instagram look) plays at seq 169.75-172.00, BEFORE that look's "We have" (raw 268.42). refine/polish/splice skip
  out-of-order pairs; `tools/cutcheck.py` can't see those joints (`work/seqcheck.txt` proves them).
- **Private screens: none inside the cut.** Raw 0-2.5 and 364.0-366.1 = the OBS window; raw 149.80-162.22 and 259.12-266.92
  = the Claude app, a file browser and the Windows task view (both fully cut). VLC shows its file-name overlay
  ("successstory-vivian-5m.yt.final.mp4" raw ~162.2-165 = seq ~100.5-103.3; "...ig.final.mp4" raw ~266.9-270.5 = seq
  ~169.75-172.55, over Affan's comment and "We have").
- For phase 2: the Short's own audio ("earners and owners") plays under "when you look at the shorts like these" (raw
  97.6-98.9, seq ~66.8-68.0: he clicked the Short; not separable). Seq 38.93 (Short → Affan) and 71.05 (Affan → Short
  resume) cut through the Short's music bed (-31 dB); seq 172.55 butt-joins the Instagram look's music (-27 dB): a 1-2 frame
  audio crossfade hides each.

## Download log (batch approval)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | https://www.youtube.com/@scottdclary og:image (yt3 s900) | 83 KB | the channel card's REAL profile picture |
| a2 | `audio/ES_Spring Sometimes - Sugoi.wav` | Epidemic Sound recording 7adc989a-5350-433e-b9c9-80fae4b7b3ea ("Spring Sometimes - Sugoi", WAV full mix) | 126 MB | the mellow classy bed (new for this batch, never used before) |
