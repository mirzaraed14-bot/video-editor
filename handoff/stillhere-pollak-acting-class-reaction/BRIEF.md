# stillhere-pollak-acting-class-reaction: Affan's reaction to our Still Here Hollywood samples (ABW10 "Still Here reaction", v2 standard)

## ▶ STATUS: resume here
- 2026-11-02 ≈16:55 PKT (R3): r2 PLACED (the sonnet review's fixes, § Reviewer r1 → r2): `prem6.sh ... patch`: 8 "-r2" graphics + `captions-r2.mov` imported (premcheck6 gate passed), bed ridden (bedride6 166/166 keys), verify 0, clipgain6 90/90, grabs `work/grabs-sheet-r2.jpg` = the offline stills, ABW10 saved, active restored. Placed plan = `work/plan.r2.json` (build_plan's version check reads plan.r1.json: point it at r2 before a next round). DONE: 2:46.7, Affan exports.
- 2026-11-02 ≈16:00 PKT (R3): PLACED in ABW10 as "Still Here reaction", 2:46.7, apply --verify 0, clipgain6 90/90, grabs `work/grab-*.png`, ABW10 saved, active restored. `work/plan.r1.json` = the placed plan (a changed graphic gets an "-r2" id). Sonnet reviewer done (fixes next: see § Reviewer).
- 2026-11-02 ≈15:10 PKT (R3 builder): OFFLINE BUILD DONE with the Drinkin' Bros reviewer's lessons folded in BEFORE the first placement
  (every-frame Claude check 0 exposed, face framing per beat from the 95th-percentile mouth, verdicts on their Short as splits, every last
  beat >= 1 s, play/pair tags out of the top band, audible SFX only). Cut 166.70 s (2:46.7), 90 segments. NEXT = `bash
  ../_onyx-batch6-2026-10/reactions/tools6r3/prem6.sh projects/stillhere-pollak-acting-class-reaction place`, then `PYTHONUTF8=1 python
  build_plan.py` (the plan switches to the razored dump), then `prem6.sh ... lay` (`check` if verify fails), proof6.py, the sonnet reviewer.

## Inputs
OBS `raw/2026-11-01 16-33-45.mp4`; camera `X:\Recordings\Onyx\C1422.MP4` in TWO sync pieces (a +71.6 ms step in the camera offset inside
OBS 210-239: pre +12.3767 s at 97 s, -25.2 ppm; post +12.4442 s at 307 s, -25.8 ppm; split at OBS 216.0;
`../_onyx-batch6-2026-10/reactions/sync/sync-C1422-16-33-45.pre/.post.json`). Transcript `transcript/words.json` (WhisperX large-v3).
Their Short "Losing Luke and Shannon - Jason Priestley 'Beverly Hills 90210'" (i_V9Lso4rt4: 95K views, 2.4K likes on the page in the
recording); their channel Still Here Hollywood Podcast w/ Steve Kmetko, @StillHereHollywood, 448K subscribers. Ours:
`X:/Claude Projects/Exports/stillhere-pollak-acting-class.yt/.ig.final.mp4`.
Plays (OBS s): their Short 76.54-84.98 (the opening), 160.13-167.06 (his replay of its pauses), 171.25-177.38 (its best moment); our YouTube
cut 231.715-246.42 and 321.25-333.92, our Instagram cut 348.19-352.52. The Claude app is on his screen at OBS 0.8-4.8, 210-223.7,
334.7-338.6, 368.5-370.2, 413-414.5: only 368.6-370.0 falls in the cut, under the YouTube/Instagram pair (opaque), checked frame by frame
by `tools6r3/claudecheck.py`.

## The cut (keep.json; author3 -> splice -> polish (two overlapping joints fixed by hand) -> tools6r3/tight6.py -> splice; pins.json)
- First word on frame 0 ("Gentlemen" at OBS 36.24, his THIRD take of the intro).
- THEIR Short gets 21.9 s in their own voice: the opening question (8.4 s), his replay of its pauses (6.9 s) and its best moment (6.1 s).
- Our sample told twice in YouTube (14.7 s + 12.7 s) and once in Instagram (4.3 s), then both side by side (ba_pair).
- Fillers and restarts pinned out by slice ASR (work/slice): "uh"s, "you know"s, "for for", "right", "just just", "you can say".

## Catalog pass (CATALOG.md FX-01..81, the same read as Drinkin' Bros' today; stills re-checked on the 9 tiled sheets)
- Fits this video (a critique of a Short's title, its pauses and its packaging for a 448K channel): FX-18 quote as chips + FX-55 strike
  (HERO: their own words during the replayed pauses, the fillers struck and collapsed out), a two-circle audience map (who the title
  reaches), FX-55/23 rings on their title and on 448K, FX-33/52 a real still of their channel page, FX-46 side-by-side (YouTube vs
  Instagram), FX-52 two phones teasing both looks, FX-71 count-ups (600M), checklist cards.
- Not used on this channel's reactions before: the filler strip, the audience map, ba_pair, the channel still card, teaser2.
- Leaned on by the Drinkin' Bros reaction built the same day: the waveform hero, the episode bar, the grid: none reused here.
- Better than the last one: their pauses are shown on their own words (not an abstract waveform), the title critique points at the
  title itself, and both looks play side by side.

## Cut for the cap (every line he said that is not in the video)
- (intro) his first two takes ("reviewing Luke and Shannon's podcast", "reviewing Still Here Hollywood") and 'a... my versions of one of the Steve, uh'
- reading their title aloud: 'Losing Luke and Shannon. Jason Priestley, Beverly Hills 90210. Okay, so all of these things from my perspective, from a random viewer, right? Who is losing?' (kept: 'who is Luke and Shannon? I don't know')
- 'of people who know this particular person' (over their audio)
- 'there's no really like cuts where he's thinking, were you close, right'
- 'the editing is just' and 'for a channel like' (restarts; the kept takes follow)
- 'let's actually review' (the first of two)
- over our YouTube cut: 'It's very good. It's very dynamic. Kevin Pollak.'
- 'I make these videos to convey my point but also as an appreciation gift; he has given me permission, I don't make these videos without permission' (kept: Steve can upload these)
- 'as I've made, obviously for this exact video, I've made the Instagram version as' (a restart)
- 'This format doesn't really work for you. Instagram, it just' (a restart)

## Downloads (logged before pulling; batch approval = REACTIONS-BUILDER-BRIEF § Music + SFX)
| File | Source | Size (est.) | For |
|---|---|---|---|
| `audio/ES_Must Maintain - Matt Large.wav` | Epidemic Sound MCP DownloadRecording, id 181a4eda-f976-4ad4-83ae-6f6ed885264c (boom bap / old school hip hop, elegant, no vocals, 3:09, 85 bpm) | ~55 MB | the bed |
| `sfx/src/*.wav` (11 Epidemic SFX, WAV, each < 0.5 MB) | Epidemic MCP DownloadSoundEffect: 955a277a Swish Low Deep Cloth Movement Singular 01 · b4c664b4 Cloth Jacket Fast Single · 6a3cac7d Swish Short Office Style 02 · ec69ae2b Cloth Shorts Throw · 72d49db7 Designed Swoosh Wide · 551a738b Playing Cards Hand Slide On Table 02 · af766588 Notepad Page Turn 01 · 4ff188a3 Windows Knock Single Light · 1afd4bbf Cloth Impact Duvet Hit Hand · 985ab88b Pen Retractable Click 02 · 97c68af6 Panasonic DMC G2 Shutter | ~3 MB total | the SFX set (distinct from the Drinkin' Bros set; same measurement) |
| `sfx/src/sh-card-2.wav`, `sh-slide-1.wav`, `sh-tap-1.wav` (3 Epidemic SFX, WAV, each < 0.3 MB; added 2026-11-02 ≈14:30 from the Drinkin' Bros review: more entrance variety, transients that clear the bed) | Epidemic MCP DownloadSoundEffect: 4a018eba Games, Misc, Playing Card, Single, Slide, Pass On Table · 4f7410e3 Paperback, Slide Across Table 02 · 8ae41379 Objects, Book, Document, Thick, Many Pages, Slide On Table | ~0.6 MB | card/title entrances, taps |
## Levels (measured offline by `../_onyx-batch6-2026-10/reactions/tools6r3/audio6.py`, `work/audio-report.txt`, mix `work/mix.wav`)
- Voice: 90 A1 clips, each its OWN Amplify (clipgain6.py) so its loud words hit -6 dBFS into the -6 dBFS Hard Limiter; talk gains median
  +14.7 dB, held within +-6 dB of it; talk -16.2 LUFS, 68 % of 400 ms talk windows peak within 1 dB of -6 dBFS. Their Short / our
  samples normalised by peak, held <= talk + 2 LU.
- Bed: "Must Maintain" (Matt Large) at -13.1 dB = -24.3 LUFS short-term = 8 LU under his talk, RIDDEN +-4 dB (164 Volume keys,
  `tools6r3/bedride6.py`) so the gap stays ~8 LU: 3 s windows P10 6.8 / median 8.0 / P90 9.2 LU (flat it was 3.3-14.6); 2 s tail fade.
- SFX: 48 cues, 11 sounds; each cue's loudest 50 ms clears the bed in that same 50 ms by >= 6 dB where the peak caps allow (transients
  <= -8.5 dBFS, swishes <= -9.5, both >= 2.5-3.5 dB under his -6 peaks); weakest: 113.3 pop +1.9, 50.1 pop +2.5 (under their Short's
  own audio), 138.7 swish +2.7.
- Mix: -15.7 LUFS integrated, -1.7 dBTP.

## Reviewer r1 → r2 (sonnet fresh eyes on `work/proof/`, 2026-11-02; fixes placed as `prem6.sh ... patch`)
DEFECTS fixed: a Chrome tooltip "(1) Instagram - Google Chrome" on the channel page at 19.3-21.3 and the 95K pill sitting on another
Short's thumbnail (the face now holds through "without further ado, let's get straight into the business"; the pill moved to the low
band) · lt-affan's "SHORT-FORM EDITOR" on screen 0.3 s (now with the name) · the 600M stat's final value < 1 s (held into "I do it on",
counting 0.5 s) · the phones' labels and the checklist below y 1620 (raised) · the "WHAT works" card empty for 2.2 s (first row with
the card) · the "WHO ARE they?" chip on the 95K views figure (chip lowered, the title view moved down out of the top band) · the
channel-name ring clipped at the panel edge (ring on "Still Here Hollywood Podcast") · the bed's 3-15 LU spread (ridden) · weak pops
raised (caps -8.5/-9.5).
Not changed (taste, for Affan): face-only verdict beats with their cards (143.7-155, 89-93.5), the "misaligned" stage as type rather
than their grid, mouse cursors and edge text on his screen recording, static spans (a paused Short 29.7-49.8 with marks; the type
stages 93.5-113.1). The reviewer could not name live reference Shorts (YouTube off limits, TikTok/IG empty).
