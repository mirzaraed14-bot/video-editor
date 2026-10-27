# bradlea-ferrari-camry-reaction: Affan's reaction to our Brad Lea samples (ABW10 "Brad Lea reaction")

## ▶ STATUS: resume here
- **2026-10-27 13:09 PKT: v2 PREPARED (Affan's review)** — "Brad Lea reaction v2" (same bin; v1 untouched): **167.93 s (2:47.9)**, 61
  segments from `v2/keep.json` (v1's cut + the WHOLE intro "I do shorts for my own channels. I teach it and I do it for my clients as
  well. So it's kind of like my bread and butter. This is why I make these videos." − two tangents: "I've seen so many of his clips. It's
  not even funny. I have clipped a lot of moments from Brad's podcast." and "and at the end Brad says the dealer paid him 13,000 to
  actually drive the car"). Camera on the nearest frame (in-points −7.9…+8.2 ms, lip sync worst 8.8 ms); `v2/build_plan.py` = v1's
  plan + steps-cred2 (copy fixed 13:45) / title-bread / title-brand (stat-13k + sel-subs2 gone, a face beat over the channel page's last 0.4 s); 18 of 25
  graphics reuse v1 renders (`tools5/mgreuse.py`). SFX: fresh set `v2/sfx-src/` (SOURCES.txt), 23 cues, one per entrance, levels by
  loudness (`v2/work/sfxgate.txt`: PASS). Bed holes under their Short + our IG cut carried (his v1 edit). verify 0; intro 72/72 words;
  proof `v2/work/grabs-sheet.jpg`. Unused download: `sfx-src/es-riser-clean-01.wav` (refused: tonal 24 dB).
- **2026-10-27 09:15 PKT: PREPARED IN ABW10** ("Brad Lea reaction", bin "Onyx batch 5 reactions (2026-10-27)"): **168.78 s (2:48.8)**
  on the real sequence end (the bed was trimmed to V1, `tools5/bedtrim.py`), 62 segments; razored (34 at 23 edges), layout 101
  clip edits (--layout-check 0 leaks, 19 between-key slips max 1.2 px, `anim_kps=60`); V3 showcase frames (2) / V4 MG (24 graphics,
  21 events) / V5 captions; house chain on all 62 A1 clips: +11 dB his talk, +4 dB the four inserts (their Short + our three plays,
  level-matched: both −19 LUFS after the −6 dBFS limiter); 47 SFX (A2 28, A4 19) from the job's own slices (`sfx/`, hits −10 dB =
  5 under the voice peak, whooshes −19 dB); bed "Liquid Life" (Chill Cole) on A3 at −21.8 dB from 2.164 s (13.0 LU under his
  voice); 25 ms ramps at the 8 sample edges; **--verify 0 problems**; lip sync from the sequence: camera in-points −25…−3 ms off
  the sync line (≤ 1.5 frames, --verify's tolerance is 35 ms). Proof: `work/grabs-sheet.jpg` (25 Premiere grabs; on this loaded
  machine the program monitor lagged up to one grab behind, so a few tiles show their neighbour's moment). He exports.
- Look J: see build_plan.py docstring. Hero = the INK CUT into our YouTube cut (from Brad's face on their paused Short, 89.13-90.03).
  The lagging grabs never caught it: proven offline instead (stills at 89.45 / 89.85, and ink.mov's last frame vs play-yt1.mov's
  first frame over the panel: mean |d| 0.00, ink fully opaque), so the hand-off to the master card is seamless.
- Taste calls for Affan: "you were instantly hooked" (said OVER our playing sample, cut to keep one clean play); the hook card's
  "377K SUBSCRIBERS / and a one-minute stare" wording; the story runs hook (YouTube look) → payoff (Instagram look) instead of
  replaying the opening in the Instagram look; the cards sit at y 1410 on his chest like batch 3.
- Re-run quirks: after EVERY build_plan.py run, re-run facex.py (face x here is right, 910-1073, no chair hits); the graphics'
  sounds are cue times minus the slice's own offset (`sfx/slices.json`).
- Captions: `work/tightasr/` (CPU) + tightwords3 ops (`work/tightwords.ops.json`: "where he's who" → "Who"; falign scored "who cares"
  0.76 vs "where he's who cares" 0.49/0.33).
- Inputs: OBS `raw/2026-10-26 19-23-47.mp4` (copy; original in `E:\Shorts\...\Batch Batch\`), camera `X:\Recordings\Onyx\C1404.MP4`
  (camera = OBS − 119.257 s, −23 ppm, `../_onyx-batch5-2026-10/reactions/sync/sync-C1404-19-23-47.json`; NO camera before OBS 119.3 s).
- He played: their Short (YouTube page, "PETE DAVIDSON REVEALS WHAT HE THINKS OF INFLUENCERS"), OUR YouTube cut in the Claude app's
  browser pane (`X:\Claude Projects\Exports\bradlea-ferrari-camry.yt.final.mp4`), OUR Instagram cut in Films & TV full screen
  (`...ig.final.mp4`). The two masters share ONE audio track: each play was named by the higher xplay2 ncc (IG 1.00 vs YT 0.90 at 499-536).

## Catalog pass (copied from `../_onyx-batch5-2026-10/reactions/CATALOG-PASS.md` § J, 2026-10-27)
- FX-15 Red Ink Bleed: "and then boom, just go get into it" @294. New kind `ink_reveal`.
- FX-30 Whisper Card + FX-80 Black Beat: "let's just look at the examples" @385, "move on to the Instagram variant" @485. 0.3 s black dip, tiny "CUT 1 / CUT 2". Existing `label`; the dip is new.
- FX-40 Slow-Burn Portrait: "who cares? It's bad" @272. Bare face, slow creep, 4 s max. Existing face beat.
- FX-38 Hard Push Slide: YouTube cut to Instagram cut @485. `ba_wipe` with a slide param (new).
All new. Last five leaned on a wipe between the cuts.
**Hero:** the ink cut. On "boom" ink opens from Brad's face on their paused frame and grows over the panel, our hook ("I bought an F8") playing inside. A shape: no duration bar (I), no wipe (E).
**Accent:** Merriweather Bold Italic (installed).
**Better than I (DSH):** I drew the structure he teaches along their bar; here the cut he preaches happens on their own frame, on "boom".

**Decided (builder, 2026-10-27):** the ink is the ENTRANCE of our YouTube cut, not a preview on "boom": it opens from Brad's face on
their paused Short in the last 0.7 s before our first play and lands exactly on the master card's first frame, so our sample is
still introduced once and plays once (a preview on "boom" would show it twice and sit over the critique). Merriweather Bold Italic
accent; FX-40 (the slow push on "Who cares? It's bad"); FX-38's push becomes the card entrance language.

## The cut (keep.json → author3 → splice RENDER=0 → polish → splice → jointcheck → pins → seqmap3)
- Kept: intro (last of three "gentlemen today" takes), permission, name + 600 million; THEIR Short 6.65 s (Pete Davidson, "It's bad
  and it makes me sad…"); "I like this hook, I really don't like it for Brad" + his brand is big enough; the social-media-manager /
  stare-at-the-camera / formats-for-beginners / huge-podcast point; "it just goes on for a minute. Who cares? It's bad." + 10 seconds
  then boom; pauses = the editor's job; not enough editing, bold poppy look; only the important moments; OUR YouTube cut 0-8.38 + his
  read of the hook (Brad Lea's Ferrari vs a Camry, so many things going on, the overlays, the zooms, never simple on YouTube) + the
  GRAFT 8.38-13.995 from his second play; the Instagram variant (same short, rounded rectangle, minimalistic, motion graphics) + OUR
  Instagram cut 13.995-21.915 = the story's payoff, so ONE story runs hook → payoff across both looks; "Brad says the dealer paid him
  13,000 to drive the car"; how Brad's brand should be; good stories, a matter of clipping and packaging; I really love his clips;
  the LAST of five sign-off takes + next one.
- Cut for the 3:00 cap: "I do shorts for my channels / teach it / clients" (intro ≤ 12 s), "you were instantly hooked" (spoken OVER
  our playing sample: keeping it would double the sample under his voice; taste call for Affan), "this is for Brad to watch… my free
  time", "pretty sexy shirt", the restarted plays, the duplicate "it just goes on for one minute", the Claude-app screen 598-641.
- Pins (`work/pins.json`): '600' was squeezed by WhisperX into a 60 ms token and the real "six hundred" sat in the gap (now one
  shared boundary); "I like this hook" restored its "I"; "okay" out; five filler / next-word tails out ("you know" ×3, "i'm", "which
  is"); "and at the end you know" dropped (no dip).

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | `../_onyx-batch5-2026-10/reactions/avatars/bradlea.jpg` (yt3 og:image, see SOURCES.txt) | 80 KB | channel card |
| a2 | `audio/ES_Liquid Life - Chill Cole.wav` | Epidemic Sound recording 946eca99-f5ad-43ec-8b74-9e33328f9091 (WAV, full) | 60 MB | the bed (never used before; −10.6 LUFS over the used span) |
| a3 | `sfx/*.wav` | slices of the shared kit (`assets/sfx/epidemic`: mg-water-low, cd2-swell-deep, impact-clean-sub, mg-swish-bright, cd3-hit-bright, cd2-impact-reverb, cd3-ambient-hit, wd-soft-impact-1, mg-swoosh-wide, cd3-tom-hall) via `../_onyx-batch5-2026-10/reactions/tools5/sound5.py` | — | every slice ≤ 20 dB tonal, ≥ −15 dB in the phone band (the sub exempt) |
