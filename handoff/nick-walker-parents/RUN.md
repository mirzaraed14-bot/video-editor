# RUN — nick-walker-parents (ABW8 · Sequence 28, bin "Nick Walker Parents")

## ▶ STATUS: resume here
**2026-10-04: the creator RECUT Sequence 28 (43.83 s; beat 5 back, a '24 announcement line, parents' cutaways,
reaction tail gone) → HEAD LOCK applied in `ABW9.aep`, ABW8 Linked Comps 40–44, 17/17 layers, proven (worst drift
0.023 px; `headlock/`) → CAPTIONS on Sequence 28 as a caption track, 64 captions, max 3 words (`captions/`), seen
on screen at 5.6 s ("A QUITTER") and 10.2 s (italic narrator "HE DID THIS"). Neither project saved (the creator saves).**
**2026-10-05: ZOOM PASS (BlurMoCurves) on ABW8 Linked Comp 46** (the Topaz render `Nig_stab_chr2_iris3.mov`, 19
blocks, 5 yellow = pull out): 19 `Adjustment Layer 29` zooms on top, read back from AE (each Z Dist start / mid / end
as planned), fresh dump confirms each spans its block exactly, the grade layers and footage untouched. 8 face pivots +
2 pinned side pivots (`zoom/centers.override.json`): block 5 x100 (Nick at the left edge on the hug pull-out's first
frames), block 17 x360 (mom whole, dad's profile at the right edge: both can't fit a 0.70 push-in). Preview
`zoom/zoom-preview.jpg`. AE not saved.
**2026-10-05: TRANSITIONS on Comp 46** from the creator's labels (`transitions/transitions46.jsx`, log `.txt`): 17 made
(5 Dark Green +30, 7 Purple dip −90, 2 Peach exposure, 1 Pink flash, 3 Cyan blur; block 17 Aqua = none, block 19 last).
Each read back at its keys; the zooms (already applied) unchanged. AE not saved.
**2026-10-05: CAPCUT CAPTION RETURN CLEANED** — `Caption Exports/peace2.mp4` (in "peace2.mp4 Comp 1" → ABW8 Linked
Comp 47 L1) → `peace2_clean.mp4`: 528 frames repaired (the ~41 %-of-frame static frame every 2 s, plus faint 1-frame
specks on 150-frame runs every 10 s); verified on raw luma: no pixel above Y 40 touched, nothing moved > 6 levels.
Footage #441 re-pointed in place (`captions/capcut/peace2_replace.jsx`, undo "Clean CapCut caption export (Claude)"):
size/fps/duration and the precomp layer in/out MATCH, the effects stay. AE not saved.
Next on their call: Upgrade Captions To Graphics → styles (`captions/caption-colours.md`) → zooms / transitions after
labelling → CapCut return clean.

### Head lock (comps 40–44, `headlock/`)
- Read from AE: `headlock/read_comps4044.jsx` → `live4044.txt` (17 layers: Greg ×2, BTS interview ×13 incl. mom ×2
  and dad ×1 listening cutaways, `'24 Olympia Announcement.mp4` ×2) → `track.json` → `track_sheet.jpg` (dot on the
  nose in all 17) → `headlock4044.jsx` (1,450 Anchor keys + Motion Tile, undo group "Head lock (Claude)") →
  `headlock_read.json` read back from AE → on-screen nose drift ≤ 0.023 px per layer.
- Nothing left unlocked: the Scale-100 / 156 interview layers are 4K zoom-ins, not letterboxed.

### Captions (`captions/`)
- Read the live sequence with the VO: `sequence-captions.py read … --voice A1,A2` (A2 = the ElevenLabs narrator;
  A3 music left out) → WhisperX → `transcript/words.json` (`_fixes`: "said" → "says", 12.08 s).
- `captions.txt` → `make_plan.py --hang 0.8` → `make_srt.py … seq28-captions` → `sequence-captions.py import`.
  Narrator italic; Greg + Nick upright; f*ck censored; 17 of 64 coloured. Last caption "from now on" ends 41.11,
  the reaction (to 43.83) plays clean.

## Format / lane
Abundance Wisdom short, 9:16 1080×1920 60 fps, Premiere (sequencing) → AE. Preset `presets/youtube-shorts/abundance-wisdom/`
(PLAYBOOK § 0 Sequencing).

## Request coverage (the creator's paste, 7 beats)
| # | Beat | Status |
|---|---|---|
| 1 | VO "When Nick Walker finally won Mr. Olympia, after years of being called a" | ✓ A2 0–4.20 (VO pieces 1–2 untouched); V1 left empty for the creator's picture |
| 2 | Greg Doucette "Nick Walker's a loser, a quitter, a has-been." (nTw91_PwGGU 7:56) | ✓ 4.20–7.78, short (3.6 s) |
| 3 | VO "he didn't say a single word about them. Instead, he did this for his parents." | ✓ A2 7.78–12.40 (VO pieces 3–5 MOVED +3.583 s, in/out kept); V1 empty |
| 4 | BTS "Everyone says I should do this for me. Do this for me." | ✓ 12.40–15.42, cut before "It's impossible" |
| 5 | BTS "My parents have been with me since day one…" | ✗ DROPPED (creator's rule: first to go over 58 s; ~62 s with it). Anchors in beats.json `_dropped`, noted on the B4 marker |
| 6 | Finals "thank my mom and dad… crying her f- eyes out… they're the true winners tonight." | ✓ 15.42–22.93; BLEEP marker 20.80–21.14 ("fucking") — the bleep itself is the creator's to drop in |
| 7 | BTS "It's impossible… parents that I have. I am paying off all your debt. And I'm going to make sure that you guys can breathe in peace from now on." + reaction | ✓ 22.93–53.30; reaction 32.12–53.30 untouched (dad's hug, then mom's), out at source 421.50, before the interviewer's "Nick," (421.74) |

Total **53.30 s** (≤ 58).

## Sources (all in bin "Nick Walker Parents")
- greg: `E:\Bullshit Folder\Henry\The Real Reason Nick Walker Is Out Of The Olympia.mp4` (already on disk; also in bin "Nick Walker Olympia Win" — imported again into this bin, same file)
- finals: `E:\Bullshit Folder\Henry\2026 Mr. Olympia Finals Official Footage.mp4` (already on disk; the long-form job's `02-olympia-2026-finals-official.mp4` is a duplicate, NOT used)
- bts: `projects/nick-walker-parents/broll/Beyond The Stage - NICK WALKER IS MR OLYMPIA CHAMPION (5eP8GkXRuew) 4K.mp4` — the only download (another creator's video; H.264 3840×2160 60 fps)

## What was produced
sources.json · beats.json · framing.json (hand face-x from brief/frames/react/sheet*.jpg) · edl.json · placement.json ·
premiere/{vo_move.js, place.jsx, bleep_marker.js, readback.js, readback.tsv} · proof/{seq28_audio.wav, seq28_words.txt, crops_sheet.jpg}

## Proof
- Read back: 19 V1 + 19 A1 clips at plan, razors at 403.0 / 417.0 exact; A2 VO pieces 1–2 unchanged, 3–5 at 7.7833 / 9.8833 / 10.4833 (in 6.6333 / 9.35 / 10.4333 kept).
- Audio rebuilt from the read-back and re-transcribed (faster-whisper large-v3): reads the script start to end, nothing from the interviewer after the reaction.
- 9:16 crop sheet: every clip framed on Nick (the arena wide centred; the hugs framed on the hug).

## Flags
- Reaction framing is split in 3 static crops (400.3 Nick + crying mom / 403.0 dad's hug / 417.0 Nick + mom): a rough start, the AE head lock reframes.
- Beat 6 trims "And I might be Mr. Olympia, but" before "they're the true winners" (as in the paste).
