# RUN: abw11-seq03-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-10: captions DONE, caption_qa PASS, hand-off sent.** `abw11-seq03-short.srt`, 62 cues, 0 → 52.800 s, yellow deep-talks, baseline **y1258** (chin 1143 + 115: he sits lower in this take than in the ABW10 reels).
Sequence: **ABW11 · Sequence 03** (only one by that name, active), 29 V1/A1 clips of `X:\Recordings\PBU\C1368.MP4`, some at 0.8x / 1.1x, 60 fps, no gaps. Read only, nothing changed in Premiere.

## Content
School hair checks (the finger test, scissors after assembly, "aao idhar display pe lao", the little kids staring) backfired into a long-hair obsession; his pitch: grow it as long as you like, just groom it, "funky rockstar shit ni chale ga school mai".

## Steps
1. `sequence_reference.py "Sequence 03" projects/abw11-seq03-short` → Gate A OK (52.800 s).
2. `chin-line.py` → median chin y1143 → baseline y1258.
3. `transcribe.sh --lang ur` (WhisperX, CPU, 8.5 GB free, ran normally) → 231 words; `transcript_check.py` DROP 12.55-17.40.
4. `codeswitch_pass.py` ("let me pitch this", "first of all") · `work/redecode.py` (ur/hi/en 10 s windows) → `work/redecode.txt`.
5. The drop was really 9.6-12.7 ("wahin kaato … maar do"); WhisperX had pulled "jaan ke aisi qainchi …" 3.2 s early into it. 0-17.2 timed from the windows (ur + hi agree to 0.1 s).
6. `captions.txt` → `build.py --style yellow --y 1258 --srt --dur 52.800` → `caption_qa.py` **PASS** (warn left: 46.40 CONNECTOR, the windows hear "koi farq ni parta").

## Flags for his ear (my readings)
2.36 "hamare hair mai" · 11.16 "iski rerh maar do" · 17.20 "itna strict" (heard "stretch") · 31.02 "kyun khara hai bhai" · 39.68 "karwana chahte na" · 41.30 "rule" (could be "role") · 42.98 "jitne bade karne na".
