# abw10-seq16-short — ABW10 · Sequence 16 (captions only)

▶ **STATUS: DELIVERED 2026-10-22, waiting on the creator's review.**
Deliverable: `projects/abw10-seq16-short/abw10-seq16-short.srt` (21 cues, first at 00:00:00,000, 0 → 29.817 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 16 at 00:00, apply **"affanwizu yellow"**, baseline **y1191**.

**Flagged for the creator:** 24.0–26.2 s "asal body ye / ye ye bhai" (two decoders hear ye ×3, WhisperX hears "ye hai bhai");
28.7 s "kia baat karhe ho yar" (Hindi pass: कर रहो; Urdu pass: kar rha hun); 17.3 s "rishta bhej" is the word his cut stops on.

## The job
- 1080×1920 60 fps, 29.817 s. V1/A1: 11 clips of `X:\Recordings\PBU\C1365.MP4`, all at 100 % speed, no timeline gaps.
  Language hi 0.86 / ur 0.13 → `--lang ur`. Chin y1076 → baseline **y1191**.
- Content: the gym-bro bit (shirt off, shouting through sets, "tumhare baap ka gym hai", 3 set triceps / biceps, story for the
  girls, "legs ni marni bhai… ye larkiyon ke kaam hai", chest / biceps / triceps / shoulder banao).
- Speech 23.2 s; silent 0–2.62 (the first line still shows from frame 0, their rule) and 9.73–12.22 (caption off).
- English kept English: shirt, set, gym, triceps, biceps, story, legs, body, chest, shoulder.

## Better than the last one (CLAUDE.md learning loop § 5)
First job on the speed-aware `sequence_reference.py` (no speed changes here, Gate A exact) and the first-cue-at-0 rule from
Seq 12 applied from the start; the two ambiguous phrases were settled with a third (Hindi-script) decode, not a guess.
