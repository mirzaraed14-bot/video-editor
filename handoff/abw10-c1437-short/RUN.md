# RUN: abw10-c1437-short (@affanwizu captions, ABW10)

## ▶ STATUS: resume here
**2026-11-08: captions DONE, caption_qa PASS, hand-off sent.** `abw10-c1437-short.srt`, 70 cues, 0 → 59.583 s, yellow deep-talks, baseline **y1165** (chin 1050 + 115).
Sequence: **"MJ Showed His Mother - raw cut v2"** in ABW10.prproj. He REUSED that sequence (the MJ AW Short's raw cut, already built and delivered as v1-v3 from the snapshot `projects/mj-showed-his-mother/premiere/his2_readback.tsv`) for this new reel: 31 V1/A1 clips of `X:\Recordings\PBU\C1437.MP4` at 1x, 60 fps, no gaps. Read only, nothing changed in Premiere.

## Content
Load-shedding while gaming with US friends ("yar power out hogyi hai"), ashamed to explain it; the middle class's day revolves around road, bijli, pani, gas; they pay the most tax; at the elders' gatherings that's all anyone talks about; you pay the bills, facilities should come; how will the country move forward when you keep people stuck here.

## Steps
1. `sequence_reference.py "MJ Showed His Mother - raw cut v2" projects/abw10-c1437-short` → Gate A OK (59.583 s).
2. `chin-line.py` → median chin y1050 → baseline y1165.
3. `work/transcribe_fw.py` (5.1 GB free: the low-RAM route, no WhisperX batched run) → 281 words, ends 59.56.
4. `codeswitch_pass.py` (16 English words; "video script" at 21/26 s = prompt echo) · `work/redecode.py` (ur/hi/en, 10 s windows) → `work/redecode.txt` · `transcript_check.py` OK.
5. `captions.txt` by hand → `build.py --style yellow --y 1165 --srt --dur 59.583` → `caption_qa.py` **PASS** (warn left: 26.04 ENGLISH "script" = prompt echo, en window = "They also pay the most tax").

## Flags for his ear (my readings)
0.00 "gaming" (first word, cut on its onset) · 2.69 "chali jati thi" (both hear "chale aati") · 10.79 "kese bataye aadmi" · 16.11 "rakha hua hai" (heard "rakha wa") · 34.32 "gaur karo ge" · 42.60 "road hoga" · 47.46 a short filler before "khud sochen" left out · 53.02 "kyunke bill de rhe ho".
