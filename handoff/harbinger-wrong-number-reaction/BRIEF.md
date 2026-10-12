# harbinger-wrong-number-reaction: Affan's reaction to our Jordan Harbinger sample (ABW8 sequence "Jordan Harbinger reaction")

## ▶ STATUS: resume here
- 2026-10-12: Affan handed over RAW recordings (no rough cut this time): camera `X:\Recordings\Onyx\C1348.MP4` (1920x1080 59.94) +
  OBS `2026-10-12 05-24-59.mp4` (2560x1440 60, his mic + desktop audio; copied to `raw/`). His direction: "match the camera and the
  file yourself, sync the audio yourself… like the Chris Do and Rollo videos… more motion graphics, more refined, more premium,
  more expensive, crisp sound effects, mellow classy background music." He exports himself.
- DONE: sync (`../_onyx-batch-2026-10/reactions/s4849/sync-C1348.json`: camera = OBS + 6.37 s, −48 ppm, weak window dropped);
  transcript (WhisperX, `transcript/words.json`); voicemap (`work/voicemap.json`); ROUGH CUT `keep.json` → `author.py` → splice
  RENDER=0 + polish → 7 measured pins (`work/pins.json`) → `transcript/cuts.json` (104 segments, 318.95 s of 479.5 s), every joint
  slice-ASR'd (`work/cutcheck.txt`). Sequence built by `tools/build_seq.py` (OBS V1+A1, camera video-only subclip V2, his Seq 33-35
  split: screen 71 / face 65, seam y 1038), verified (camera in-points land 1-31 ms early on the 60 fps grid: inside lip-sync tolerance).
- **2026-10-12 ≈07:45: PREPARED in ABW8 "Jordan Harbinger reaction"** (5:18.95), `apply.py --verify` 0 problems. 9 face-only beats (20 %),
  36 graphics (channel card with his REAL yt3 avatar, lower third, title cards, 2 stats 60 % / 95 %, 2 checklists, steps, compare, mock hook
  title ON the Short, underline + arrow on its title, labels), 45 SFX on A2, white seam line under the captions on every split frame,
  "rise" entrances, captions on the y 1038 seam. Voice chain +5 dB → −6 dBFS on all 104 A1 clips (measured, verified). Bed "The Light"
  (Daniel Fridell) −17 dB from its 0.744 s entrance, 2 s tail fade. Program-monitor proof: `work/grabs-sheet.jpg`. He exports.

## Download log (batch approval 2026-10-12)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/jordanharbinger-youtube-avatar.jpg` | https://www.youtube.com/@JordanHarbingerShow og:image (yt3 s900) | ~60 KB, 900x900 | the channel card's REAL profile picture (REACTIONS-BRIEF rule 6) |
| m1 | `audio/ES_The Light - Daniel Fridell.wav` | Epidemic Sound recording 659cf05f-bdc3-492f-836f-92ef21d8c4a8 (MCP DownloadRecording, FULL, WAV) | 108.1 MB | the mellow, classy music bed (Affan 2026-10-12) |
