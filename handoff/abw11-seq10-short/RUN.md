# RUN: abw11-seq10-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-16 ~20:00: DONE, the FIRST REAL two-layer job (his "run it" on Sequence 10 right after the Seq 09 test), hand-off sent.**
- `outputs/abw11-seq10-short.bilingual-layer.mov`: transparent full-frame layer (QuickTime Animation, RGBA, 72.65 s, 60 fps) with BOTH lines: drop on V2 at 00:00. Variant A (his pick between A/B/C was not given yet): Urdu Noto Nastaliq 72 px baseline y1328, Roman Ubuntu Light 48 baseline y1420, gold #FFD700, glow fitted to the reference.
- `outputs/abw11-seq10-short.bilingual-preview.mp4`: the same burned over the cut (for phone review).
- `abw11-seq10-short.srt`: the usual single-line yellow Roman track (80 cues, baseline y1222 = chin 1107 + 115), caption_qa PASS. Use EITHER the layer OR the .srt, not both (the Roman line would show twice).
Sequence: **ABW11 · Sequence 10** (only one, active), 31 V1/A1 clips of `X:\Recordings\PBU\C1475.MP4`, 1x, 60 fps, Scale 100 (1920x1080 source: footage band y420-1500), no gaps, 72.650 s. Read only, nothing changed in Premiere.

## Content
"zameer aapko laanat deta hai" wali saying: insecurity stems from breaking promises to yourself (gym from tomorrow, then you don't go = you betrayed yourself; your subconscious aka zameer is disappointed); keep your word and the subconscious is with you, everything feels in reach; athletes' trash talk (conor mcgregor) is backed by an undeniable stack of proof.

## Steps
1. `sequence_reference.py "Sequence 10"` → Gate A OK (72.650 s). `chin-line.py` → median chin y1107, lowest y1193 (41.8 s).
2. `work/run_all.sh`: transcribe_fw → 8 windows → codeswitch, each retried until memory allows (the first chain died on mkl_malloc x3 while other sessions ran graphics-qa and Premiere held 9 GB; the retry started at 7.4 GB free and passed first time). 319 words, transcript_check OK.
3. 5 probes (`work/probe.txt`): one "insecurity" (not two), "mentally na", "baaton par utarte hain", "athletes mai bohat ye hota hai", "already yar".
4. `captions.txt` (80 cues) → build.py `--y 1222 --srt` → caption_qa PASS (three 6-word lines split, "apne aapko").
5. `captions.ur.txt` (80 Urdu lines, his English in Urdu letters) → `presets/instagram/affanwizu/bilingual/render_cues.mjs` → `assemble.py` (preview + `--alpha` layer).

## Flags for his ear
33.22 "baaton par utarte hain" (decoders heard adharte/udharte; the en pass translated "get down to your words") · 28.98 "mentally na" (all heard "ne") · 51.35 "athletes mai bohat / ye hota hai" · 70.10 "yar" (hi; ur "kia", English listener "ke") · 38.64 "beshak aap itna".
