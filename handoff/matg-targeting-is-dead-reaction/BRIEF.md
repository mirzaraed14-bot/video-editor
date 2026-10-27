# matg-targeting-is-dead-reaction: Affan's reaction to our Marketing Against the Grain samples (ABW10 "MATG reaction")

## ▶ STATUS: resume here
- **2026-10-27 13:35 PKT: v2 PREPARED (Affan's review)** — "MATG reaction v2" (same bin; v1 untouched): **173.30 s (2:53.3)**,
  55 segments from `v2/keep.json`: v1's cut + the WHOLE intro ("i do it for my channels i teach and i do it for my clients as well so
  kind of like my bread and butter which is why i love to make these videos so without further ado let's get into the sauce"; the
  false start "which is like" out, pinned 64.333 → 64.18) + the stakes line "He said you're spending $300,000 to $400,000 a day."
  (plays between "Because of the stakes, right?" @78.9 and the resume "In July to $239" @85.2; the sample's own "$300K, $400K a day"
  hook stays in our first play @52.8) − the aside "I'm sure it did a lot better than it did here, like on Instagram". Camera nearest
  frame (−8.3…+12.0 ms; lip sync ≤ 8.4 ms on the talk clips). Plan = v1's + steps-cred2 (copy fixed 13:45) / title-bread / title-spend; 20 of 31
  graphics reuse v1 renders. SFX fresh set (`v2/sfx-src/`; the whoosh riser refused: tonal 29 dB, riser-a = a reversed airy swish),
  25 cues, gate PASS (`v2/work/sfxgate.txt`). verify 0; intro + stakes 96/96 words; proof `v2/work/grabs-sheet.jpg`.
- **2026-10-27 11:16 PKT: PREPARED IN ABW10** ("MATG reaction", bin "Onyx batch 5 reactions (2026-10-27)"): **163.48 s (2:43.5)**
  on the real sequence end, 53 segments; razored (34 at 19 edges), layout 95 clip edits (--layout-check 0 leaks, 7 between-key
  slips max 1.0 px); V3 showcase frames (5) / V4 MG (23 graphics, 20 events) / V5 captions; house chain on all 53 A1 clips: +11 dB
  his talk (−30.0 LUFS), +2 dB the inserts (−20.7 after the limiter vs his −19.8); 42 SFX (A2 23, A4 19) from the job's own slices
  (`sfx/`; whooshes −19, hits −10); bed "Morose Beatitude" (Twelwe) on A3 at −19.9 dB from 0.304 s (13.0 LU under his voice); 25 ms
  ramps at the 8 sample edges + 8 ms at the YouTube graft joint (48.83); **--verify 0 problems**; lip sync: camera in-points −29…−5 ms
  off the sync line (mean −17), his talk clips 8-30 ms by GCC-PHAT. Proof: `work/grabs-sheet.jpg` (29 grabs). He exports.
- Look L: see build_plan.py docstring. Hero = the quadrant "PICK THE moment" (ENTERTAINING × VALUABLE, their Short grey, THE
  MOMENT gold + ring), 111.6-120.1 s.
- Taste calls for Affan: the Scott Clary lines (486K in week one) were cut for the cap; the Serena example at the end of our YouTube
  cut was cut (the play stops on "smarter than the AI."); the player skipped 0.11 s at his resume (17.56 → 17.68 s of our cut), hidden
  in the pause he commented in; the glass cards are ~8 % see-through over bright paused frames (house style).
- Captions: `work/tightasr/` (CPU) for 0-137 s; the LAST stretch (137-163 s) came back from WhisperX with only its final sentence, so
  its words are seqmap3's raw-mapped ones (`work/tightwords.NOTE.txt`): re-running tightwords3.py overwrites that merge, redo it.
  Measured on 0-137 s, where both exist: raw-mapped vs tightasr word starts differ by a median 6 ms (p90 24 ms), so the fallback
  stretch is timed as well as the rest.
- Re-run quirks: after every build_plan.py run, re-run facex.py (face x 651-830, no chair hits).
- CONFIRMED as MATG by its transcript: "today we are going to be reviewing marketing against the grain" (OBS 47.3 s).
- Inputs: OBS `raw/2026-10-26 19-57-22.mp4` (copy), camera `X:\Recordings\Onyx\C1406.MP4` (camera = OBS + 9.874 s, −32 ppm,
  `../_onyx-batch5-2026-10/reactions/sync/sync-C1406-19-57-22.json`; no camera after OBS ≈537.7 s, the cut ends at 524.3). Their
  Short: "AI Agents Are Already Buying Everything". OUR cuts: `X:\Claude Projects\Exports\matg-targeting-is-dead.yt.final.mp4` / `.ig.final.mp4`.
- Private screen stretch: OBS 420-441 (an interruption: "Hello? Huh?" + a conversation in Urdu) is cut.

## Catalog pass (copied from `../_onyx-batch5-2026-10/reactions/CATALOG-PASS.md` § L, 2026-10-27)
Clear of H (retitle, @107-122) and M (the Scott Clary winner).
- FX-13 Depth-Sandwich Type: "it's actually about the moment that you select" @358. Hero.
- FX-69/70 Lone Yellow Bar + Ring: "entertaining and valuable at the same time… not too niche… not too boring" @369-375. Two-axis diagram of his words, one gold dot ringed. New kind `quadrant`.
- FX-40 Slow-Burn Portrait: "I've made two shorts… a lot more valuable moments" @192-196. Existing face beat.
All new. Last five leaned on select chips on the Short's page.
**Hero:** "MOMENT" in giant extra-bold type behind his head on the thesis line, 20 fps stepped (FX-81). New kind `behind_type`; `workflows/behind-text.py` bakes the type, the head matte needs a cutout pass.
**Accent:** Bodoni Moda Italic (installed, variable).
**Better than I:** every mark in I sat on their Short; this is the first graphic that goes behind him.

**Decided (builder, 2026-10-27):** FX-13 behind-the-head type is NOT built: it needs a person matte and no matting model is on this
machine (only YuNet); fetching one is a download nobody approved. The hero is the catalog's own second move, the `quadrant`
(FX-69/70): his thesis drawn as two axes (ENTERTAINING × VALUABLE) with their Short's dot and the gold, ringed "THE MOMENT" dot, built
word by word on "entertaining and valuable… not too niche… not too boring… some spice". Bodoni Moda Italic; entrance `drop`.
The Scott Clary lines (a client's 486K winner) were cut for the 3:00 cap; that also keeps L clear of the reel M.

## The cut
- Kept: intro (after four "hello"s), permission, name + 600M through short form; their title "AI Agents Are Already Buying
  Everything" is vague, it has to be a lot more specific; THEIR Short 8.1 s (Stripe / Link's wallet); I like the motion graphics but
  it's more the Instagram style, it did better on Instagram; I've made two shorts, MATG has more valuable and entertaining moments; let
  me show you; OUR YouTube cut as ONE play in two passes: sample 0-3.26 (his 2nd start) + 3.26-17.47 (his 3rd start; he talked over its
  first 2.7 s), his read (the motion graphics fit the brand, valuable, hooked instantly because of the stakes), then 17.676-39.55 (the
  resume; the player skipped 0.11 s at the resume) to the payoff "smarter than the AI"; very valuable but entertaining; a style that
  goes viral on YouTube; but it's not about the style, it's the moment you select; understand the content, entertaining AND valuable,
  not too niche, not too boring, some spice; fundamentals first; OUR Instagram cut 0-8.9; minimalistic, Instagram friendly, rounded
  rectangles; so many moments not clipped properly, not doing the podcast justice; the eye for viral moments; Kipp can upload this;
  the outro.

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | `../_onyx-batch5-2026-10/reactions/avatars/matg.jpg` (yt3 og:image) | 119 KB | channel card |
| a2 | `audio/ES_Morose Beatitude - Twelwe.wav` | Epidemic Sound recording f799df81-fa59-4889-8589-9d7c3cccbe52 (WAV, full) | 67 MB | the bed (never used before; −12.9 LUFS over the used span) |
| a3 | `sfx/*.wav` | slices of the shared kit (cd2-whoosh-deep, cd2-thump-low, wd-thud-heavy, cd3-tom-trailer, mg-zoom-airy, wd-soft-impact-2, cd-hit-airy, cd3-taiko, wd-boom-low, mg-whoosh-classic) via `tools5/sound5.py` | — | ≤ 20 dB tonal, phone band ≥ −15 dB (the sub exempt) |
