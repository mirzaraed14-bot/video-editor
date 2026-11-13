# RUN: abw11-seq05-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-14: captions DONE, caption_qa PASS, hand-off sent.** `abw11-seq05-short.srt`, 49 cues, 0 → 42.983 s, yellow deep-talks, baseline **y1182** (chin 1067 + 115).
Sequence: **ABW11 · Sequence 05** (only one by that name, active), 20 V1/A1 clips of `X:\Recordings\PBU\C1432.MP4` at 1x, 60 fps, no gaps. Read only, nothing changed in Premiere.

## Content
After inter / A level take a gap year (unless you're 100% sure); no faltu harkatein, try everything (coding, AI automation, high ticket sales, personal branding, accounting, architecture, law); the thing you keep coming back to is the one you'll grow in (his: making and editing videos).

## Steps
1. `sequence_reference.py "Sequence 05" projects/abw11-seq05-short` → Gate A OK (42.983 s).
2. `chin-line.py` → median chin y1067 → baseline y1182.
3. `transcribe.sh --lang ur` (WhisperX, CPU, 8 GB free) → 160 words; it looped "apni apni …" over 0-2.1 and dropped 2.2-7.8 (`transcript_check.py` DROP).
4. `codeswitch_pass.py` · `work/redecode.py` (died on mkl_malloc while codeswitch ran beside it; re-run alone, OK) · `work/redecode2.py` (the hook, 0-8.4 s, short windows; stopped once hi + en agreed).
5. 0-7.7 timed from the hi + en windows; WhisperX times from 7.76 on.
6. `captions.txt` → `build.py --style yellow --y 1182 --srt --dur 42.983` → `caption_qa.py` **PASS** (warn left: LOOP at 0.21 = WhisperX's garbled opening, replaced from the windows).

## Flags for his ear (my readings)
0.00 "aapne inter kar lia" · 1.36 "gap year aap zaroor lo" · 9.00 "faltu harkatein" · 17.54 "law" · 37.18 "long term" · 40.41 "kar pao ge" · 40.99 "khud basis pe".
