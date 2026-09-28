# RUN: seq11-short (ABW8 · Sequence 11) — captions only

## ▶ STATUS: delivered (2026-09-28), waiting on the creator
`seq11-captions.srt` — 170 lines, max 5 words each, yellow deep-talks style, timed to the **176.63 s of
content** (the sequence is 263 s long but everything after 176.63 s is empty). Drag onto the sequence at
00:00 and apply the "affanwizu yellow" track style.

- Cut: the creator's, untouched. 77 clips on V1 from `E:\Skool Recordings\5 Sept Batch\C1313.MP4` (4K,
  mostly Scale 33 centred, 4 clips zoomed/offset), voice on A1 from
  `TX01_MIC025_20260928_144412_orig Audio Extracted.wav` with its own source times. No music track.
- Language: **Urdu** (auto-detect said `hi` p0.97 — the ABW8 trap; forced `--lang ur`). 640 words.
- **A transcription LOOP was caught and fixed:** WhisperX hallucinated "us ki bhi aik tasveer hojaye gi"
  three times at 120–125 s. Re-decoding 4 spans (119.5–128.5, 131.5–137.5, 144.5–152.5, 157.5–163.5) with
  word timestamps gave the real lines (curation / script / hook / framing; "at least"; "chaar to ASMR
  unboxing hi daal li … teen testing"; "healthy range") and they were spliced into `transcript/words.json`.
  **Lesson: a phrase repeated 3× in a row is a loop artifact — always slice-verify it.**
- Baseline **y1216** = chin 1101 + 115. NOTE: 27 of 89 chin samples had no face (screen-recording shots of
  the brand's Instagram), so check the captions don't cover the on-screen numbers in those shots.
- Topic: a page audit of the perfume brand Scents & Stories — 250k followers but 5–39 likes, paid-ads reach
  vs organic, find formats in your niche and adjacent niches, one format wins and becomes the bread and butter.

## Flags for the creator (unsure words)
1. 43.7 s "**miri me** jo inka perfume hai" — the product name, spelled by ear
2. 61.8 s "**suniye to**" (ASR: سوئیے؟)
3. 133.8 s "hui shuru mai to **at least** aik hi chale ga"
4. 153.2 s "formaton ke liye **test** karen ge" (ASR: تشکیل)
5. 160.0 s "aik **healthy** range mai" — confirmed on the re-decode
6. 164.9 s "**37,000** followers" then 169.2 s "**30,000** followers" — you say both numbers
