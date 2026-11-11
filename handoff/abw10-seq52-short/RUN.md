# RUN: abw10-seq52-short (@affanwizu captions, ABW10)

## ▶ STATUS: resume here
**2026-11-11: captions DONE, caption_qa PASS, hand-off sent.** `abw10-seq52-short.srt`, 71 cues, 0 → 56.250 s, yellow deep-talks, baseline **y1230** (chin 1115 + 115).
Sequence: **ABW10 · Sequence 52** (only one by that name, active), 25 V1/A1 clips of `X:\Recordings\PBU\C1463.MP4` at 1x, 60 fps, no gaps. Read only, nothing changed in Premiere.

## Content
Influencer awards: the Sistrology sister keeps crying in every vlog after "DHA wali maid" won; Mr Saad ur Rehman (Ducky bhai) said on his vlog "hamare ghar bhi bhijwa do"; he'd have backed the maid publicly instead; brand credibility going to zero; "a sore loser".

## Steps
1. `sequence_reference.py "Sequence 52" projects/abw10-seq52-short` → Gate A OK (56.250 s).
2. `chin-line.py` → median chin y1115 → baseline y1230.
3. `transcribe.sh --lang ur` (WhisperX, CPU, 9.3 GB free) → 277 words, complete; `transcript_check.py` OK.
4. `codeswitch_pass.py` (36 English words) · `work/redecode.py` (ur/hi/en 10 s windows) · `work/redecode2.py` (the two names, with and without a name prompt: the prompt changed nothing).
5. `captions.txt` → `build.py --style yellow --y 1230 --srt --dur 56.250` → `caption_qa.py` **PASS** (warns left on purpose: 55.10 "you are" = 3 windows; 55.56 "soul" → "sore loser").

## Flags for his ear (my readings)
0.00 "sistrology" · 1.81 "har vlog mai" · 36.62 "mrs iqra" · 39.12 "pata mai kia karta?" · 43.77 "unhone award jeeta hai" · 55.85 "sore loser".
