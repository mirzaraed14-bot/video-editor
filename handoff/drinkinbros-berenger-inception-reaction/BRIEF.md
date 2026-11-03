# drinkinbros-berenger-inception-reaction: Affan's reaction to our Drinkin' Bros samples (ABW10 "Drinkin Bros reaction", v2 standard)

## ▶ STATUS: resume here
- 2026-11-02 ≈16:50 PKT (R3): r3 PLACED (the Still Here review's checks run here too: bed ridden ±4 dB = 159 Volume keys, SFX caps +0.5-1 dB, teaser + both steps cards above y 1620, the 600M stat held, the brand card no longer empty): `prem6.sh ... patch` then `check`: verify 0, clipgain6 88/88, bedride6 159/159, grabs, ABW10 saved, active restored. Placed plan = `work/plan.r3.json` (a later change gets `-r4` ids). DONE: 2:40.2, Affan exports.
- 2026-11-02 ≈15:35 PKT (R3): r2 PLACED (the reviewer's fixes, see § Reviewer r1 → r2): `prem6.sh ... patch` (layout, unface6 for the verdict split, clipgain6, clear6 + overlays from a clean slate), 8 leftover r1 SFX clips (page/tick and their chopped tails) removed, `prem6.sh ... check`: apply --verify 0 problems, clipgain6 88/88, Premiere grabs `work/grabs-sheet-r2.jpg` = the offline stills; ABW10 saved, active restored (Paris Shock Therapy - raw cut). DONE unless Affan asks for changes. 2:40.2.
- 2026-11-02 ≈14:10 PKT (R3): PLACED in ABW10 as "Drinkin Bros reaction" (bin "Onyx batch 6 reactions (2026-11-01)"), 2:40.2, apply --verify 0 problems, Premiere grabs `work/grabs-sheet.jpg` match the offline stills, ABW10 saved, active restored. Proof `work/proof/` (sheets every 1.5 s + first 5 s every frame). Sonnet reviewer DONE: fixing its defects now (a 1-frame Claude app at 2.77, caption over the lips at ≈109, lt-affan 0.87 s, stage phases < 1 s, teaser clip, Cillian chip collision, verdict beat 58.2-62.2 → split, SFX audibility check), then a patch under the lock.
- 2026-11-02 ≈13:00 PKT (R3 builder): OFFLINE BUILD DONE, Premiere next. Cut 160.22 s (2:40.2), 88 segments, joints proven (Whisper
  `work/jointcheck.txt` + acoustic `tools6/endcheck.py`); plan.json (look Q, docstring of build_plan.py); captions + 32 MGs + 3 showcase
  frames rendered by `../_onyx-batch6-2026-10/reactions/tools6r3/mgx6.py`; mix measured offline (`work/audio-report.txt`, `work/mix.wav`).
  NEXT = `bash ../_onyx-batch6-2026-10/reactions/tools6r3/prem6.sh projects/drinkinbros-berenger-inception-reaction place`, then `... lay`.

## Inputs
OBS `raw/2026-11-01 16-16-12.mp4` (copy of E:\Shorts\...\Batch Batch\), camera `X:\Recordings\Onyx\C1421.MP4` (camera = OBS + 19.607 s at
214 s, -26 ppm: the line through the 28 strong windows of `../_onyx-batch6-2026-10/reactions/sync/sync-C1421-16-16-12.w40.json`; the
11-window run was contaminated by two playback windows). Transcript `transcript/words.json` (WhisperX large-v3 on the OBS audio).
Their Short "Are Tier One Operators Born or Made?" (bxUUfsosJ4c, on youtube.com/shorts in the recording: @DrinkinBrosPodcast, 106 likes;
their channel page read at full size: Drinkin' Bros Studios, verified, 283K subscribers, 4.8K videos). Ours: Exports/drinkinbros-berenger-inception.yt/.ig.final.mp4.
Plays (xplay2, the YT and IG masters share one audio track): ours 212.117-227.117 (sample 0-15), 312.06-322.06 (sample 14-24, under his
'I also made this Instagram format' line), 326.547-345.547 (sample 0-19, the Instagram look on screen).
The Claude app is on his screen only at OBS 20-30, 196, 326 (none of it shows: the intro there is a face beat).

## The cut (keep.json; author3 -> splice -> polish -> tools6r3/tight6.py: every quiet run >= 0.12 s inside his talk cut to 0.08 s)
- First word on frame 0 ("Gentlemen" onset 22.69, segment start 22.683).
- THEIR Short gets 23.3 s in their own voice: the question (94.45-103.47: "Are tier one operators born or made? In my experience I have seen
  guys go to the national level that you would have never thought") and the answer (132.23-146.53: "He is mid-pack ... I'd probably lean
  towards they can be made because then when you see them at a national level, they are a different person.").
- OUR sample told once: YouTube look sample 0-7.99 ("...never understood it"), Instagram look 7.99-17.95 ("I didn't know where I was ...
  that really fine Irish actor that was in there"); his "Look at that, Cillian Murphy in the short" moved after the Instagram play (the
  screen at that line shows the paused Cillian frame).
- Slice-ASR fixes (work/slice: faster-whisper large-v3 both ways): "I just" after "pauses as well", the restart "if I- if I'm", "the Drinkin'
  Bros, uh, or for", "like", "gets", a lip smack, the sample's "I" after "in there": all out.

## Catalog pass (CATALOG.md FX-01..81 read in full; all 137 stills looked at on the 9 tiled sheets `projects/tfts-we-need-to-talk/work/catalog/`)
- Fits this video (a reviewer pointing at a Short's pauses, a channel's size, an episode's buried moments): FX-60 Tape Deck Waveform
  (their audio as the evidence: HERO), FX-68/70 Data-Point Clipping + Ring and Benchmark (the episode bar, three markers), FX-69 Lone
  Yellow Bar (283K vs 10-20K, honest scale), FX-66 Trading Card Wall (the grid: don't clip everything, the gold few), FX-39 Source Handle
  Tag (their Short credited), FX-55 Red Pen Underline / FX-23 Pointer Tag (rings on the page: 283K subscribers, Cillian Murphy), FX-52
  Corner Exhibit Box (our edit teased in the intro), FX-71 Funnel Count (600M, 50K count-ups), FX-18 quote as comments ("who are you?").
- Not used on this channel's reactions before: FX-60, FX-68/70 as a timeline, the comments stack, the teaser, the source tag. Leaned on by
  the last batch (TCO/BP/Roofing v1): steps cards, ba_wipe showcases, one soft swish family: the steps card stays once (credentials), the
  showcases stay for our sample (Affan's own showcase language), the swish family is replaced by an 11-sound set sized per motion.
- What this does better than the last one: see build_plan.py's docstring (their Short airtime, screen when he points, never a bare face,
  captions under the lips, YouTube-tight cuts, -6 dBFS voice, an audible lo-fi bed, a varied SFX set).

## Cut for the cap (every line he said that is not in the video)
- (intro) 'And at the end I'm gonna also show you my version of a clip' (a false start: the last take is kept) and 'the clip of uh' (stumble)
- (intro) their Short autoplaying under his intro at 39.8 s ('Are tier one operators born or made?': it plays properly later)
- his line over our YouTube cut's replay at 311.7 s ('I also, by the way, made this Instagram format of this exact short': our sample plays ~12 dB louder under it, unusable; a card introduces the Instagram cut instead)
- 'I'm not going to play the whole thing because obviously this will go above the three-minute mark on Instagram' (meta)
- 'it's not according to their brand'
- 'and and you'll exactly see what i mean when i'
- 'I never'
- 'forcefully pick out bits to make shorts'
- 'so that i can make more money'
- 'i really want to focus'
- 'those are fairly decent numbers for a channel that size'
- 'that's a mistake'
- 'short form is the marketing through which they are going to understand'
- 'oh you guys have this podcast the full episode is out etc'
- 'Literally, you guys can see I gave you live examples.'
- 'I like my shorts when I'm making for clients. I make them in a way that it's just bam, bam, bam, bam.'
- 'i'm going to show you the sample as well that we made'
- 'very entertaining short by the way'
- 'christopher nolan so many characters'
- 'and it should be because they have 283 000 subscribers'
- 'I picked this moment from their podcast.'

## Downloads (logged before pulling; batch approval = REACTIONS-BUILDER-BRIEF § Music + SFX)
| File | Source | Size (est.) | For |
|---|---|---|---|
| `audio/ES_Hip Hop Healing - Osoku.wav` | Epidemic Sound MCP DownloadRecording, id d2eeed2c-ac57-44a4-ab3a-679ea402697c (old school hip hop, 1990s, no vocals, 2:53, 90 bpm) | ~50 MB | the bed |
| `sfx/src/*.wav` (11 Epidemic SFX, WAV, each < 0.5 MB) | Epidemic MCP DownloadSoundEffect: 61fa6548 Swish Short Classic Noise Filter Dry · e1c332ac Swish Low Deep Cloth Movement Singular 02 · 073cf199 Designed Whoosh Soft Airy · 58c05c01 Swish Short Bag · c52cf22f Designed Swoosh Light · 4a018eba Playing Card Single Slide Pass On Table · 95327caf Notepad Page Turn 02 · 3ff28fbf Pops Dull Swallow · bd17a7d5 Glass Impact Window Object Hit Soft · d07ba97a Mechanical Gears Clicking Ticks 02 · cad01d18 Canon EOS 5D Shutter | ~3 MB total | the SFX set (chosen from 62 previews by envelope / tonal / phone-band measurement, `tools6r3/sfxpick.txt`) |
| `sfx/src/db-card-2.wav`, `db-slide-1.wav`, `db-tap-1.wav` (3 Epidemic SFX, WAV, each < 0.3 MB; added 2026-11-02 ≈14:30 after the reviewer: card entrances alternated only 2 swishes, page/tick lost to the bed) | Epidemic MCP DownloadSoundEffect: 5d709714 Playing Card, Slide On Table 02 · 388ab893 Sheet, Laminated, Slide On Wooden Table 02 · 135c886b Wood, Impact, Light Hit 02 | ~0.6 MB | card/title entrances, comment bubbles |
## Levels (measured offline by `../_onyx-batch6-2026-10/reactions/tools6r3/audio6.py`, `work/audio-report.txt`, mix `work/mix.wav`)
- Voice: 88 A1 clips, each its OWN Amplify (clipgain6.py) so its loud words hit -6 dBFS into the -6 dBFS Hard Limiter; talk gains median
  +14.9 dB, held within +-6 dB of it (r2: was +-4, 22 clips sat on the rails); talk -16.2 LUFS, 66 % of 400 ms talk windows peak within
  1 dB of -6 dBFS. Their Short / our samples normalised by peak, held <= talk + 2 LU.
- Bed: "Hip Hop Healing" (Osoku) at -16.2 dB = -24.3 LUFS short-term = 8 LU under his talk, RIDDEN +-4 dB (r3: 157 Volume keys,
  `tools6r3/bedride6.py`): 3 s windows P10 7.1 / median 8.0 / P90 8.8 LU (flat it was P10 6.3 / P90 9.8, extremes 1.9-16.9); the 2.7 LU
  minimum sits at 119.8 s, a window that straddles our Instagram cut's own audio; 2 s tail fade.
- SFX: 49 cues, 12 sounds; each cue's loudest 50 ms clears the bed in that same 50 ms by >= 6 dB where the peak caps allow (transients
  <= -8.5 dBFS, swishes <= -9.5 since r3, both >= 2.5-3.5 dB under his -6 peaks); weakest: 154.5 s swish-m2 +2.6, 130.3 shutter +3.0.
- Mix: -15.7 LUFS integrated, -1.9 dBTP.

## Reviewer r1 → r2 (sonnet fresh eyes on `work/proof/`, 2026-11-02; fixes placed under the lock as `prem6.sh ... patch`)
DEFECTS fixed: a 1-frame Claude app at 2.77 (the intro face beat now ends ON the V1 cut 2.80; `tools6r3/claudecheck.py` now checks EVERY
frame of both reactions: 0 exposed) · the caption on his lips at 109 (face framing per BEAT from the 95th-percentile mouth of a 0.25 s
scan, escalated until his lowest mouth keeps the lips above the caption: `facex6m.py`) · the verdict 58.2-62.2 is a split over their
Short (rule 5), its checklist in the top panel · lt-affan 0.87 → 1.6 s · stage beats < 1 s (THAT GO viral, THOSE GET views, PAUSES =
LOWER VIEWS) now 1.2-1.5 s, build_plan refuses a last beat < 1 s · teaser still t 3.2 (2.6 caught a caption mid-slide) · Cillian chip
off our sample's caption (chip_dy) · "made for @..." tag dropped (it crossed the gold rule) · play tags at the card bottom (they sat at
y 93) · the 4.8 s freeze of the paused Instagram frame → our YouTube cut plays on, muted (play-more) · ticks before their card removed
· inaudible sounds swapped (page/tick/slide measured 0-3 dB over the bed in 50 ms) + a third card sound (card-2) · caption "TO BE DOING"
→ "REVIEWING" (faster-whisper both ways + the joint check) · voice clamp +-6.
GAPS left for Affan (taste, not defects): their Short plays as a 560 px column with the YouTube chrome (not zoomed); no loop-back ending;
the hook (their channel tag) makes no promise by his own rule; the red X on "THE PACKAGING: VERY BASIC" and "A SHORT THAT FEELS 10-20K"
are his words but read critical to the prospect. The reviewer could not name live reference Shorts (YouTube is off limits here,
TikTok/IG pages render empty); its page-level references: cut.pro hooks 2026, opus.pro editing tips, filmora reaction formats.
r3 (the Still Here review's checks run on this one too): the bed ridden (above), SFX caps +0.5-1 dB, the teaser and both steps cards
above y 1620 (the teaser reached 1702), the 600M stat held into "I do it on" (its value sat < 1 s), the brand card no longer empty for
2.6 s (it opens on "in a lot more"); build_plan now refuses an empty card > 1.2 s and a last beat < 1 s.
