# crossexamined-300k-house-check-reaction: Affan's reaction to our CrossExamined samples (ABW10 "CrossExamined reaction")

## ▶ STATUS: resume here
- **2026-11-03 ≈13:08: Affan's note "the name is cut to 'Cross'" FIXED surgically.** My rebuild had cleared the sequence (renamed in ABW10
  "CrossExamined reaction (cleared - do not use)", NOT deleted: needs his yes). The pre-clear version was imported back from ABW10's 12:39:46
  auto-save (`work/abw10-autosave-1239.prproj`, importSequences, no duplicate media). It carried HIS hand: 166.10 s (he cut 16.7-23.07 incl.
  title-field, no bed under the plays). On it: the first talk clip extended to OBS 32.90 (+47 frames), everything after it shifted +0.783 s,
  captions held on CROSSEXAMINED over '-examined', bed tail fade moved to the new end. Now 166.88 s, camera sync unchanged, saved.
  The r3 plan/cuts files in this folder describe the abandoned rebuild, NOT the sequence: `work/dump-r3.json` is the truth.
- **2026-11-02 ≈15:43 (R2 builder): PLACED after R1 — "CrossExamined reaction" 2:52.5 (172.47 s), verify 0, ABW10 saved, lock released.**
  The R1 re-renders went into Premiere under NEW names (`plan.rev` r1 → `overlays/mg/<id>-r1.mov`, `overlays/captions-r1.mov`; the old
  in-place items had raised refresh modals, 5 were OFFLINE; all 28 removed from the bin after the swap, files kept). Program-monitor grabs
  inside every graphic: `work/grabs-sheet.jpg`. NEXT: title-pack + title-big as `-r2` (punctuation inside the accent run: "*packaging:*",
  "*results?*"; rendered, not yet placed), then `tools6r2/retire.py --apply` for the two -r1 items.
- **2026-11-02 ≈14:30 (R2 builder): R1 FIXES IN PROGRESS.** v1 of the v2 build was PLACED (174.25 s, verify 0) and reviewed (sonnet,
  `work/REVIEW-R1.md`): his Claude app showed at 141.4-142.3 / 130.7 → both now face-only; an "uh" and the silent sample starts trimmed
  (pins.json: the cut is now 172.75 s = 2:52.8); per-phrase voice gains from the 99.95th percentile (a desk click had set one phrase 5 dB low);
  glass cards opaque; sample tags moved off the top 200 px; typed email types early; scorebug 2.2K/5.9K held; SFX 2 dB up; "MY PHONE".
  The sequence was CLEARED and re-placed (V1/V2/A1 only, verify OK, dump-raw 172.75); NEXT = captions + MG render (running), then window B
  (`tools6r2/applyr2.py` --razor → dump-layout → build_plan → facey → sfxgate_r2 → --layout → --window → gainset.py → --overlays → --verify
  → grabs), proof.py, report. Tools: `../_onyx-batch6-2026-10/reactions/tools6r2/` (job-local R2 kit, docstrings).
- Look Q (build_plan.py docstring): join entrance, Palatino Bold Italic accent, ripple hero; bed "Time Waits for No One" 8.5 LU under his talk
  (bedlevel.py), no gaps; 37 cues from 8 fresh Epidemic sounds levelled per class (sfxgate_r2.py); captions on the seam, every face-only beat
  framed so his LOWER LIP sits at y 930 (r2geom.py, facey.py): the caption block top (~998) is 68 px under his lips.
- Their Short plays ~10 s in their voice ("I think we're about out of time ... Dogs certainly do. Cats don't. They're demonic ... I love cats,
  I really do. They taste like chicken."). Intro line found by large-v3 window ASR + his mouth on camera at OBS 28.8 (WhisperX had stamped it
  16 s early over other Shorts' autoplay).

## Inputs
OBS `raw/2026-11-01 15-40-12.mp4` (copy of E:\Shorts\...\Batch Batch\), camera `X:\Recordings\Onyx\C1419.MP4` (camera = OBS + 14.16 s;
`../_onyx-batch6-2026-10/reactions/sync/sync-C1419-15-40-12.w20.json`, 20 windows: the 7 strong ones (peak >= 10) agree within ~10 ms,
the 5-window report's +121 ppm came from weak windows). Transcript `../_onyx-batch6-2026-10/reactions/obs-15-40-12/` (copied to transcript/,
clip renamed to the OBS mp4). Their Short "Will We See Our Pets in Heaven?" (5McUucDfzIA; no file: YouTube blocked, so its airtime plays
from his screen recording). Ours: `X:\Claude Projects\Exports\crossexamined-300k-house-check.yt.final.mp4` / `.ig.final.mp4` (33.625 s).
Plays (xplay2): YT 271.00 (s0-8, he restarts) + 291.854 (s0-33.6, the clean one); IG 351.594 (s0-20). Avatar `../_onyx-batch6-2026-10/reactions/avatars/crossexamined.jpg`.
His Claude app is on screen at OBS ~0-5, 255-268, 340-346, 373-378 (never shown).

## The cut (keep.json from `work/mk_keep.py` → author3 → splice RENDER=0 → polish → splice → `tools6r2/tighten6.py` → seqmap3)
- v2 tight pass (his "13 ms / 5 frames / 20 ms of silence" notes): every quiet run >= 0.20 s (10 ms RMS < -38 dBFS) inside his talk is cut,
  60 ms kept after the voice and 50 ms before the next onset; his first word on frame 0. Sample plays untouched.
- Their Short gets ~13.6 s in THEIR voice: the question, "I think we're about out of time", "Well, ... dogs certainly do. Cats don't.
  They're demonic.", then "No no no... I know there's cat lovers. I love cats, I really do. They taste like chicken."
- Our YouTube cut plays ONCE, whole (0-33.6 s, the clean play 2); our Instagram cut 0-5 s.

## Cut for the cap (every line he said that is not in the video)
- their Short's 'No no no... I know there's cat lovers' (the cap; 'I love cats, I really do. They taste like chicken' kept)
- 'and making sure that the actual clip is well packaged' + 'right, very good' (the cap)
- 'just that the marketing which the clips can use, so much that' (the cap)
- 'So let's see.' (intro filler before 'let's get to business')
- 'Do animals go to heaven, but...' + 'Dogs go to heaven' (his scrubbing)
- 'it's um it's very like there are a lot of intentions like there' (restart)
- 'It goes into, like, the short itself is very good, but, you know' (a repeat of 'a very good comedic short')
- 'which is why I made a sample for this as well, but before we do that' (the sample is introduced after the phone analogy)
- 'it's a very weird thing that I'm saying but people are very lazy, I've seen it personally' + 'very niche thing but a lot of people don't know this'
- 'I know you just cat, I love cats I really do and this just feels right now' (over their Short's replay)
- 'this clip, it just feels like, you know, for example this is, um, this is the whole podcast, right' (restart of the phone line)
- 'that they're going on, because obviously this is a normal conversation so they are going to be tangents'
- 'so federal government' + 'keep in mind this is a different clip' + 'very good like' (spoken over our sample's first play)
- 'it's the federal government' (reading the sample)
- 'starting off strong, that's the thing personally I like to do, because if the hook is there people are going to be interested, otherwise you know they're not going to watch it at all' (said in his pause before the clean play; the cap)
- 'obviously we did the same thing with the Instagram version as well' (the next line says it)
- 'very same but it's different, the base style is different, so that's how it should be packaged' (a repeat of the Instagram line)
- '944,000 subscribers, it's not a like a blank shot in the dark' (the 944K is in his intro and on the scorebug)
- our Instagram cut after 5.0 s ('And so you think, okay ... the cost of housing': the story already ran in the YouTube cut)
- 'and they landed all on almost a million subscribers for their channel, they don't' (a repeat of 944,000)
- 'That should not' (restart)
- 'I'm genuinely, I'm not even joking around, like that's how strong these kind of channels are, and it's just that'
- 'so obviously I'll give this, I'll give these both videos to the team as well, I'll email them, and by the way guys, if you're, if'
- 'I'm happy to do so, I'm just an email away, uh' (the first take; the last take is kept)
- 'and yeah that's going to be video, yeah' (outro restart) + 'uh'

## Download log (logged before pulling)
| File | Source | Size (est.) | For |
|---|---|---|---|
| `audio/ES_Remember These Days - Matt Large.wav` | Epidemic Sound MCP `DownloadRecording` f937dad2-7753-3057-82c0-101c58fc0590 (FULL, WAV; boom bap / old school hip hop, no vocals, 89 bpm, 2:36) | ~27 MB | the bed |
| `sfx/src/cx-*.wav` (8 files) | Epidemic Sound MCP `DownloadSoundEffect` (WAV): 38a49746 Cloth Flap Single Soft · e62847da Whoosh Soft Short 02 · 073cf199 Designed Whoosh Soft Airy · 9e39ef94 Whoosh Airy Light 01 · 6a2298cb Paper Sheet Laminated Slide On Wooden Table · fad4c6c0 Notepad Laminated Page Turn Single · 985ab88b Pen Retractable Click 02 · 8ceb628f Wood Impact Thud Heavy Distant | < 2 MB each | the SFX set (sized per motion) |
| `audio/ES_Time Waits for No One - Matt Large.wav` | Epidemic Sound MCP `DownloadRecording` 68980666-02d1-4509-9da0-f3bbc88ce1ac (FULL, WAV; old school hip hop, hopeful, laid back, no vocals, 90 bpm, 3:17) | 57 MB | THE BED (replaces Remember These Days: 2:36 is shorter than the 2:54 cut) |

Remember These Days (downloaded 45 MB) is NOT used: 155.7 s < the 174.25 s cut.
