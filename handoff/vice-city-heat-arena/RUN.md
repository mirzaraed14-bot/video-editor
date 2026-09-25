# RUN — vice-city-heat-arena (captions only)

▶ **STATUS (2026-09-25): CAPTION TRACK ON ABW8 · Sequence 04. Verified on screen.** 40 captions,
**max 4 words** (the creator's rule for this job), as an editable caption track (C1 "Subtitle"),
created from `outputs/seq04-captions.srt`. Checked in a grab of the Premiere window: the track spans
0–38 s and Program shows "One letter reportedly weighs" at 8.90 s. Default Premiere caption look: no
style applied (no shorts caption style exists for this channel yet). Project NOT saved by us.

| | |
|---|---|
| Channel | Affan Afterhours (GTA): a vertical facecam short. Filed under `presets/youtube/affan-afterhours-facecam/` |
| Project | Premiere `ABW8.prproj` → **Sequence 04** (1080×1920, 60 fps, 38.067 s), the creator's cut, untouched |
| Picture | 19 clips of `E:\Skool Recordings\5 Sept Batch\C1300.MP4` on V1 |
| Voice | A1 = `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Batch Batch\2026-09-24 14-08-05.mp4` (audio = video in + 5.717 s) |

## How it was built
1. Live V1/A1 read → `brief/seq04_tracks.txt`, `brief/seq04_probe.json`.
2. A1 rebuilt sample-exact on the sequence clock → `raw/seq04-reference.mov`; WhisperX (en, detected
   0.996) → `transcript/words.json`, 131 words. No remapping needed.
3. `captions.txt` = one caption per line, hand-chunked on phrase breaks, ≤ 4 words.
4. `python build_srt.py .` → `outputs/seq04-captions.srt`. The build fails if a caption goes over 4
   words or its text doesn't match the transcript. Captions run wall to wall. A start within
   −0.12/+0.05 s of a picture cut moves onto the cut. Everything snaps to the 60 fps grid.
   Stats: mean 3.2 words, median 0.90 s, range 0.33–1.53 s.
5. `import_srt04.jsx` (importFiles + `seq.createCaptionTrack(item, 0)`) → returned true.

## Choices to flip with a word
- **"fucking" is shown as `f*cking`** (23.18 s), matching the creator's censor rule on their other captions.
- Punctuation stripped except `?` / `!`. Quote marks wrap the sheriff's quote (26.40–30.27).
- Natural case, not ALL CAPS: caps can be switched on in the style; they can't be switched off.
- **No caption over 30.267–30.867**: the A1 clip there points at 184.3 s of a 177.4 s recording, so
  that insert plays silent. "criminal activity" ends on its cut.

## Re-run after a text edit
Edit `captions.txt`, then `python build_srt.py projects/vice-city-heat-arena`, delete the old caption
track in Premiere and run `import_srt04.jsx` through `premiere-bridge.mjs execute_extendscript`
(or drag the .srt onto the sequence at 00:00).
