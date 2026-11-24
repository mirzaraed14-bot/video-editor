# RUN: abw11-seq23-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-24 ~12:40: DONE, caption_qa PASS, hand-off sent.** `abw11-seq23-short.srt`, 87 cues, 0 → 84.500 s, NORMAL yellow single-line style (his call: "normal caps"), baseline **y1161** (median chin y1046 + 115; lowest y1154 at 39.3 s).
Sequence: **ABW11 · Sequence 23**, 39 V1 clips of `X:\Recordings\Afterhours\C1502.MP4`, 60 fps, 3 timeline gaps (kept), 8 framings, cut 84.500 s (V2+ runs on to 90.5 s). Gate A OK. Read only, nothing changed in Premiere.

## Content
GTA 6's Cal is framed as the paranoid conspiracy guy, so viewers (younger ones especially) learn such opinions get you ignored = social engineering; intelligence agencies steer narratives through memes and edits (the Jeffrey Epstein edits when the files came out), so why wouldn't they use GTA 6.

## Steps
1. `sequence_reference.py "Sequence 23"` → 84.500 s. `chin-line.py` → median y1046.
2. `work/run_all.sh` first try (lock free): 357 words, transcript_check OK.
3. 2 probes (`work/probe.txt`): 49.4-53.9 is ENGLISH ("if you have these kinds of opinions, you're going to be treated like this, so it's better not to have them"): the ur pass translated it into Urdu, the English listener dropped it, only the en window + the hi transliteration ("if you hai this kind") kept it. "jason and lucy/lucia".
4. `captions.txt` → build.py `--y 1161 --srt --dur 84.500` → caption_qa FAIL "movies games shows" HANGING: he draws the list out (envelope shows no dropped words), re-split → **PASS** (connector warns checked: 4.28 hi "par", 56.40 "but" kept, 50-51 is the English stretch).

## Flags for his ear
49.4-53.9 the English lines · 38.00 "jason and lucia" · 2.64 "mai uska yahan" · 4.28 "par aapne dekha hoga".
