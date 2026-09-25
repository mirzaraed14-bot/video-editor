# RUN — gta6-collectors-box (captions only)

▶ **STATUS (2026-09-25): CAPTION TRACK ON ABW8 · Sequence 06. Verified on screen.** 92 captions,
**max 3 words** (the creator's rule for this job), editable caption track (C1 "Subtitle") from
`outputs/seq06-captions.srt`. In a window grab, Program shows "big-ass Jason figure?" at 27.90 s.
Default Premiere caption look, no style applied. Project NOT saved by us.

| | |
|---|---|
| Channel | Affan Afterhours (GTA): vertical facecam short → `presets/youtube/affan-afterhours-facecam/` |
| Project | Premiere `ABW8.prproj` → **Sequence 06** (1080×1920, 60 fps), the creator's cut, untouched |
| Picture | 33 clips of `E:\Skool Recordings\5 Sept Batch\C1303.MP4` on V1 (0–61.9 s); their Adjustment Layer on V2 |
| Voice | A1 = `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Batch Batch\2026-09-25 10-14-03.mp4` |

## How it was built (`workflows/sequence-captions.py`)
1. `read projects/gta6-collectors-box "Sequence 06"` → `brief/tracks.txt`, `brief/sequence.json`,
   `raw/seq06-reference.mov` (A1 rebuilt sample-exact on the sequence clock).
2. `transcribe.sh` → `transcript/words.json`, 233 words, ≈ 226 wpm.
3. `captions.txt`: hand-chunked on phrase breaks, ≤ 3 words.
4. `srt --max-words 3` → 92 captions, mean 2.5 words, median 0.65 s (0.22–1.27 s).
5. `import` → importFiles + createCaptionTrack, both true.

## Transcript fix
- **56.05 s "$270,000" → "$270"** (`corrections.local.json`). Whisper's plain pass wrote the number.
  A digits-suppressed re-listen heard "two seventy", the speech lasts only 0.6 s, and the next line
  is "This is $400".

## Choices to flip with a word
- Mild words kept as spoken: "damn" (4.4 s), "big-ass" (27.5 s). Only the f-word is censored, as on Sequence 04.
- No punctuation except `?` / `!`; natural case (ALL CAPS is a style toggle).
- Shortest flashes (≈ 0.22 s): "with the" at 0.57 s, "I have a" at 37.85 s.

## Re-run after a text edit
Edit `captions.txt` → `python workflows/sequence-captions.py srt projects/gta6-collectors-box --max-words 3`
→ delete the old caption track in Premiere → `python workflows/sequence-captions.py import projects/gta6-collectors-box`.
