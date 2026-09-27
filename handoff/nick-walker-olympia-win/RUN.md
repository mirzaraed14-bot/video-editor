# RUN: nick-walker-olympia-win ("loser, quitter, has-been" → 2026 Mr. Olympia)

▶ **BLACK STATIC (2026-09-28): `Caption Exports/nickkk_clean.mp4` written** (17 lifted frames + 3 chroma-ringing runs
cleaned; same frames/size/rate/range). The AE caption comp still points at the uncleaned `nickkk.mp4` until the
footage is replaced (Project panel → Replace Footage → File).

▶ **TRANSITIONS (2026-09-27): APPLIED in `ABW7.aep` → ABW8 Linked Comp 25, read back. AE project NOT saved**
(undo group of the transition pass). 15 transitions from the creator's labels, layers 2-16 directly under the
caption (`nickkk.mp4 Comp 1`): 7 purple dips, 5 dark-green +30, 2 cyan blurs, 1 pink flash (10.233 s).
No transition after the 3 yellow posing cuts (17.4-19.6 s, left yellow = none) or the Aqua block at 28.0 s.
Every other layer checked unchanged, order and values (`transitions/transitions25.txt`, `after_comp25.tsv`).

▶ **ZOOMS (2026-09-27): APPLIED in `ABW7.aep` → ABW8 Linked Comp 25, read back. AE project NOT saved** (undo group
"Abundance Wisdom zoom pass (Claude)"). 20 "Adjustment Layer 29" S_BlurMoCurves on layers 1-20, one per block,
spans = the blocks exactly: 8 yellow pull-outs, 12 push-ins, 13 face pivots (`zoom/apply.tsv`, `zoom/zoom.txt`,
preview `zoom/zoom-preview.jpg`). The face picker was fixed first (it read torsos as faces; LESSONS).
Next: the creator relabels the blocks → transition pass.

▶ **CAPTIONS (2026-09-27): CAPTION TRACK ON ABW8 · Sequence 09, verified on screen.** 53 captions, max 3 words,
0.11 → 39.70 s wall to wall, ALL CAPS, italic on Fouad's question, "F*CKING" censored, no commas/full stops.
`captions/outputs/seq09-captions.srt` + cheat sheet `captions/caption-colours.md` (18 coloured, incl. Green Shade).
Grabs: 8.0 s *"BOB CICHERILLO SAYING"*, 33.8 s "NICK WALKER". Next: Upgrade Captions To Graphics → styles → pop → CapCut
→ **`clean_capcut.py` on the CapCut return before AE** (the black-static fix).
- Built from the LIVE recut (39.7 s, 21 A1 clips, Greg's new "NEW MR Olympia" reaction at the end, Runaway on A2),
  voice rebuilt and re-transcribed (`captions/`). Measured fixes in `words.json` `_fixes`: Cicherillo; Fouad =
  "you're not gonna **ever** win Mr. Olympia?" (best log-prob of the candidates); "Nick Walker" restored under the crowd.

▶ **HEAD LOCK (2026-09-27): APPLIED in `ABW7.aep` → ABW8 Linked Comp 19–22, all 9 layers, proven. AE project NOT
saved** (undo groups "Head lock (Claude)" ×2 and "Fill comp 22 (Claude)").
- **Comp 22 (creator: "fill the frame and lock"):** both layers set 100 → **177.867 %**, Position x **518.66 / 709.97**
  so Greg's median nose lands on the centre guide (x 540, the creator's own re-centring habit), then locked:
  167 keys + Motion Tile; read-back drift ≤ 0.02 px (unlocked 147–173 px). Files in `hl22/`.
- The creator recut before replacing: comp 19 = Greg "Nick Walker's a loser," · comp 20 = Greg's alt line from 0:20.0 ·
  comp 21 = the VOB host ×4 + Shawn Ray (L5, extended to 2.5 s) · comp 22 = a NEW source,
  `NEW MR Olympia -- Nick Walker.mp4` (Greg in a black tank, 1920×1080 at **Scale 100 = letterboxed**).
- Clip list from the comps' own layers (`brief/ae_comps1922.txt` → `brief/headlock_live1922.txt` → `track.json`,
  `headlock_map.json`); the track sheet put the dot on the right nose inside the crop on all 7. No baked borders.
- 674 per-frame linear Anchor keys + Motion Tile 340 / mirror, nose held at its median. Read back from AE: every
  tracked nose drifts ≤ 0.02 px (unlocked 60–137 px). `headlock1921.jsx` / `.txt`, `headlock_read.json`.
- Next: the creator saves, renders the stab comp → Topaz (PLAYBOOK § 3).

▶ **STATUS (2026-09-27): SEQUENCED on ABW8 · Sequence 09. Read back, audio proven.** 16 clips on V1+A1,
0 → **47.02 s** (target 45–50 s), 8 markers: one per beat (labels + warnings in the comments) and **BLEEP at
30.66–31.04 s** ("I will f- win"). Built from the creator's pasted BEATS; the optional beat 6 is kept (under 50 s).
Project NOT saved by us. Next, per PLAYBOOK: the creator's pass, then head lock → Topaz → captions.

| | |
|---|---|
| Channel / preset | Abundance Wisdom → `presets/youtube-shorts/abundance-wisdom/` |
| Project | Premiere `ABW8.prproj` → **Sequence 09** (1080×1920, 60 fps), bin **Nick Walker Olympia Win** |
| Sources | `E:\Bullshit Folder\Henry\` — windows + camera cuts in `sources.json` |

## The cut (re-transcribed from Premiere's read-back in-points)
| beat | tl | who is on screen | words |
|---|---|---|---|
| 1 hook | 0.00–3.70 | Greg Doucette | "Nick Walker's a loser, a quitter, a has-been." |
| 2 verdict | 3.70–8.95 | Greg (last 0.7 s: his cutaway to Nick's "I WILL NOT BE COMPETING" clip) | "I'm going to explain why Nick Walker's bodybuilding career, it's completely over." |
| 3 announcer | 8.95–12.97 | Fouad (asks) + Nick (listens), grid right column | "What do you think about Bob Cicherillo saying you're not going to win Mr. Olympia?" |
| 4 a month out | 12.97–22.10 | VOB host, then **Shawn Ray** on "That's true" | "Bro, listen. I got news for you. In reality, if everybody did show up at 100%, he'd be fighting for 10th place." / Shawn: "That's true." |
| 5 defiance | 22.10–31.45 | Olympia TV questioner + Nick | "Who's the one you have to beat in order to win?" / "Nobody. 'Cause you know what I'm tired of? … If everyone's on 100%, I will [BLEEP] win." |
| 6 tension | 31.45–36.22 | arena wide (lectern), then both finalists, then Nick | "And I think Bob is a little nervous, too." / "Why would he be nervous?" / "Bob will be eating crow." |
| 7 the win | 36.22–47.02 | both finalists → Nick | "…and the title of 2026 Mr. Olympia, to your winner tonight…" [1.1 s crowd] "And new Olympia champion, Nick Walker." → arms up, confetti (commentators: "That's it. Yep.") |

## Changes from the sheet (the creator decides)
1. **Beat 2 swapped to the sheet's own alt (0:18.67–0:23.76).** At 6:38 the man on camera is **Nick's coach** (Juventus
   shirt): "Nick and I had a very intentional conversation… He can't get in shape… He will never win the Mr. Olympia
   title. Rather than that, I'd rather see him just say…" — he is voicing what critics would say, not a verdict, and it
   isn't Greg. Swap back: `beats.json` B2 → `["greg2", "He can't get in shape.", "Mr. Olympia title."]`.
2. **Beat 4 misattribution.** The "10th place" line is said by the **VOB host** (left; he addresses "Sean" just before).
   Shawn Ray (right, teal FLEX shirt) says "That's true." The label belongs on Shawn's line, and the host is unnamed.
3. **Beat 7:** kept 1.1 s of the 6.6 s crowd roar after "tonight" (it is not silence, −19 dB), and the end is the
   arms-up/confetti push-in 2.2 s after "Nick Walker" — **no Sandow/check lift happens within 2 s of the name.**

## Checked
- Edges measured (`beats.json` `_edges`). Whisper spellings for captions: Chikorilla = Cicherillo, "eat and grow" =
  "be eating crow" (isolated re-listen), Fouad's line = "you're not going to win" (with the context hint; crosstalk).
- Framing from full frames (`framing.json`); crops checked on a 9:16 contact sheet. Olympia TV has burned-in chat
  comments along the bottom (inside the bottom 300 px band).
- Read-back: 16/16 match, in-points within 12 ms. Audio proof `outputs/seq09-audio-proof.wav`: the rebuilt audio
  reads as the table above; the proof pass's leading "If" is a Whisper artefact (the first 1.6 s alone reads
  "Nick Walker's a loser." three times).
