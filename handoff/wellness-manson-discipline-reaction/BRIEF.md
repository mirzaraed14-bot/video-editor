# wellness-manson-discipline-reaction: Affan's reaction to our Wellness + Wisdom samples (ABW10 "Wellness Wisdom reaction")

## ▶ STATUS: resume here
- **2026-10-19 PREPARED IN ABW10** ("Wellness Wisdom reaction", bin "Onyx batch 3 reactions (2026-10-19)"): **171.40 s (2:51.4)**,
  63 segments; razored (112 clip edits, --layout-check 0 leaks at keys, 10 between-key slips max 4.1 px), V3 showcase frames / V4 MG
  (19 graphics) / V5 captions, house chain +6 dB into −6 dBFS on all 63 A1 clips, 40 SFX on A2 + A4, Kind Particles bed on A3 at
  −19.7 dB, 25 ms ramps at the hard sample edges 16.6 / 23.17 / 88.72 / 114.33 / 124.5 / 129.25, --verify 0 problems. Proof:
  `work/grabs-sheet.jpg`. He exports.
- Inputs: OBS `raw/2026-10-19 06-44-24.mp4`; cameras **C1381** (OBS 0-566.6, +8.39 s) and **C1383** (OBS 620.8-678.3, −620.760 s
  constant); seq.json "cameras" (tools3/build_seq3.py). The 54 s with NO camera (OBS 566.7-620.8) is not in the cut.
- He played (VLC, from Exports\batch3-drafts-preview): yt v2 preview + ig ig3 preview.

## The cut (tools3 pipeline: keep.json → author3 → splice/polish → jointcheck.py → pins → seqmap3 → tightasr.sh → tightwords3)
- Kept: intro (3rd take + the retaken ending "by none other than Josh Trent"), 76,000 subscribers, the title is a statement / make them
  curious enough to click, their Short 6.6 s ("the loneliest thing… nervous system of your parents"), music (no track here),
  pauses (it's the editor's job to cut them; if the person pauses, boom, they scroll), 1:07 vs at most 50 s, the most important thing
  (hook amazing, several points; the editor's job: as simple as possible; hook → payoff, no tangents), OUR YouTube cut 0-25.6 s, his
  verdict, OUR Instagram cut 0-4.75 s, "pretty much the same… captions minimalistic… refined, premium", the outro (easy to understand,
  no context, nice music; both cuts to Josh; cool flex; next one).
- **Three grafts give one clean pass of our YouTube cut**: sample 0-3.6 from his first start (raw 366.86), 3.6-23.4 from the 2nd
  (376.55; he read the hook text aloud over its first 2.5 s), 23.4-25.61 ("…the behaviors that you want to be taking.") from a later
  replay (430.25; the 2nd start stops at 24.9). The EDL is therefore out of raw order at one joint (jointcheck.py handles it).
- Cut for the cap: thumbnails, approvals, the first takes, "I would have done…" shaving demo, his paraphrase over the replay
  (426-452: the sample plays under his voice), "millions of reels", "not thinking like a clipper", "carrying the hand… understand everything".
- Pins (work/pins.json): leaked 'So again' / 'This is' / 'because' / 'right' / 'They have' / first-take 'this is the editor's job' /
  'and' / 'uh', the dropped 'obviously', plus four after the audible check: an 'uh' before "The original", the false start "pa- uh"
  before "parental", the plosive of a dropped 'because', the tail "fault"; and "the" of "the title" kept.

## Look (Reaction F, see build_plan.py): loupe-led review, Lora Italic, lift-in cards, focus-pull + hit-soft. Both sample plays are
master-file cards (ba_wipe without a wipe) because VLC printed the file name over the Instagram play and File Explorer covered its
first second. facex picked the leather chair at 49-51 s: `tools3/facefix.py plan.json 49.22=1050 50.18=1050` after every facex run.
Shared-tool note: a loupe has no "tag" (labels are grouped with it); a select's chip sits ~30 px above its box (keep the box top
≥ y 360 source on the VLC view).

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | yt3.googleusercontent.com s900 (URL from `_onyx-batch3-2026-10/wellness/meta/shorts_flat.json`) | 112 KB | channel card + Josh's chip |
| a2 | `audio/ES_Kind Particles - Static Glow Sounds.wav` | Epidemic Sound recording eac7c0a4-53cb-4acd-8f4b-a0305c5ef978 (WAV, full) | 56 MB | the bed (never used before) |
