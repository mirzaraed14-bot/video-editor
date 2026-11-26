# RUN: abw11-seq26-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-26: DONE, caption_qa PASS, hand-off sent.** `abw11-seq26-short.srt`, 39 cues, 0 → 32.767 s, NORMAL yellow single-line style (he said only "caps": a funny skit + his last call "normal"), baseline **y1229** (median chin y1114 + 115; lowest y1254 at 25.3 s).
Sequence: **ABW11 · Sequence 26**, 13 V1 clips of `X:\Recordings\Afterhours\C1510.MP4`, 60 fps, 7 framings, cut 32.767 s (V2 adjustment layer + V3 black video run on to 42.85 s). Read only, nothing changed in Premiere.
**AUDIO:** his recorded voice clips on A2-A4 (Premiere Captured Audio: Audio 2_8, 3_4-3_7, 4_3; 12 clips) + the "Get out" SFX were MIXED into `raw/abw11-seq26-short-cut.mp4` at unity, so every voice is captioned; the A1-only rebuild is `work/a1only/`.

## Content
Power-company skit: the boss and his employee: a 60 hazar bill, "akhrot", 8 hours of load shedding, "maintenance ka bol do", lights on, off, on again, "mood ni ho rha", office closed, "kal aage karna hai yar".

## Steps
1. `sequence_reference.py "Sequence 26"` → 32.767 s (A1 only) → mixed A2-A4 in by hand (ffmpeg atrim + adelay + amix normalize=0, from `transcript/sequence.json`).
2. `work/run_all.sh`: transcribe failed twice on memory (other sessions busy), passed on try 3; 92 words; words.json drifts ~1.5 s late after 30 s.
3. 5 probes (`work/probe.txt`): "akhrot", "8 ghante ke lye / to wo complaints aa rahi hain", "ji sir / chalo / band karte hain", "sir mai zara ye light on inki kar ke chalen / haan".
4. `captions.txt` → build.py `--y 1229 --srt --dur 32.767` → caption_qa `--fix` (hogya, kardo, karhe) → **PASS** (warn "burn": ur + hi say "band").

## Flags for his ear
2.56 an unclear word before "sir ye to zyada" · 5.96 "akhrot" · 14.54 "to wo complaints" · 23.34 "band karte hain" · 32.30 the "Get out" SFX is not captioned · no quotes (all character dialogue).
