# RUN: abw11-seq11-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-17 ~23:45: DONE, caption_qa PASS, hand-off sent.** `abw11-seq11-short.srt`, 120 cues, 0 → 111.100 s, yellow deep-talks (single line, lowercase), baseline **y1233** (median chin y1118 + 115; lowest chin y1239 at 85.8 s).
**His call: NORMAL style, not the Urdu mix** ("caps but it normal style this is a funny video so it wont suit").
Sequence: **ABW11 · Sequence 11**, 52 V1 clips of `X:\Recordings\PBU\C1477.MP4`, 60 fps, no gaps, Gate A OK. Read only, nothing changed in Premiere.

## Content
Karachi airport, international flight (comedy): 22 relatives seeing one person off, the naughty security uncle's bad touch, the officers' questions, 0.5 kg overweight, 5 passport counters with 2.5 running, manual stamps checked twice, rehmat e shereen, the empty duty free, a Lal Qila stall, the horizontal escalator people camp on, a second bad touch ("body count plus one"), overpriced coffee, a guy asleep across a whole row.

## Steps
1. `sequence_reference.py "Sequence 11"` → 111.100 s. `chin-line.py` → median y1118.
2. `work/run_all.sh` (transcribe_fw → 12 ur/hi/en windows → codeswitch), first try. 457 words. transcript_check: LOOP 28.27 is real repetition (kahan ja rahe ho / yahan ja rahe ho / le kar ja rahe ho, hi + en agree); DROP 36.18-37.75 = a drawn-out "sirrr" (probe).
3. 8 probes (`work/probe.txt`, run with the whisperx venv python, queued on `.asr-lock` behind another session's research ASR).
4. `captions.txt` → build.py `--y 1233 --srt --dur 111.100` → caption_qa **PASS** (warns left: 25.36 "officer" vs "afsar": ur + hi both "afsar", 0.33 s fits two syllables; 28.27 loop is real; 70.00 'ایسا' dropped, probes say "bharosa ni hai"). Spelling fix taken: "isme se".

## Flags for his ear (my readings)
79.25 "lal qila ka bhi aage ja ke aik stall aata hai" (ur "laal kalar kabhi", en "red killer") · 36.20 "sirrr" · 83.40 "horizontal type shit escalator" · 24.34 "ab aapki check in hogi" (or "checking") · 14.78 "aapko bhi scanner se guzarne" · 25.28 "afsar" (English listener: "officer").
