# RUN: seq21-reel (ABW6 · Sequence 21) — captions only

## ▶ STATUS: delivered (2026-09-20), waiting on the creator
`seq21-captions.srt` — 44 lines, yellow deep-talks style, timed to the 49.92 s cut. The creator drags it onto
the sequence at 00:00 and applies the "affanwizu yellow" track style (scripted import is still broken here).

- Cut: the creator's, untouched. 21 clips of `C1247.MP4` on V1/A1, **Scale 100 (not framed yet)**, two clips
  reordered to the end (source 392–402 s before 356–360 s).
- `transcript/cuts.json` = the timeline read off Premiere. `raw/seq21-cut.mp4` = the cut rebuilt by ffmpeg at the
  channel framing (Scale 125, x 0.578) for chin measurement; transcription ran on that, so word times ARE cut times.
- Transcript: WhisperX large-v3, CPU (`transcript/words.json`), plus an `en` pass (`transcript/roman-pass.json`).
- Caption baseline **y1133** = measured chin 1018 + 115, assuming the creator frames at Scale 125 like ameer.
  If the reel ships at Scale 100 the chin sits higher — re-measure before rendering any burned version.
- Topic: buying things stopped feeling exciting (console → camera lenses; "retired army general" on the table).

## Flags for the creator (unsure words)
1. 33.0 s "or uske **baad** mene" — ASR heard "uske paas"; read as "baad" from context
2. 7.3 s "mene ghaur **kar rha hai** ke" — captioned as said; "kia hai" may be what you meant
3. 12.5 s "bhai **sab bawle hogaye**" — ASR garbled this one
4. 40.3 s "**jab bhi** mere andar" — could be "ab bhi"
5. 41.7 s "bechne ki **himmat** hi ni ai" — ASR wrote حمد

## Notes for next time
- large-v3 refused to load twice (mkl_malloc) with AE + Premiere + Photoshop + AME open: 87 of 91 GB committed.
  `WHISPER_MODEL` env override was added to `transcribe.sh` as an escape hatch, but medium failed too — the machine
  had no RAM at all. The creator closed Chrome/AME/AE/PS and large-v3 ran in 2m18. This is the case for the MacBook.
