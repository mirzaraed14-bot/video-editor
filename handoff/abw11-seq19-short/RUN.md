# RUN: abw11-seq19-short (GTA 6 Short, English captions only, ABW11)

## ▶ STATUS: resume here
**2026-11-20 ~07:30 PKT: DONE.** `outputs/seq19-captions.srt`, 31 cues, 0 → 37.833 s, max 4 words (his number), imported
into ABW11 and laid on **Sequence 19** as caption track C1 (Premiere's default caption style). His view untouched
(Sequence 19, playhead 0, idle 7 min before the write). Project NOT saved: his Ctrl+S.
His words: "can you put the english caps on this like make and srt file and max workd count per layer is 4" + "ABW11".

## Content
His own cut (Afterhours): Rockstar went ape shit on the Easter eggs: a UFO abduction, a demonic Bigfoot near a satanic
statue, a dead kraken at the bottom of the ocean, a giant mutant crab "Assassin's Creed style", "the game hasn't even been
out for a full day". V1/A1 = C1490 (speed 0.7-1.1x) with gameplay inserts (Henry: UFO, Skunk Ape, Monster Crab) and a
screenshot that have no A1; A2 = the Undertaker theme to 202.55 s (the sequence end; the cut ends 37.833).

## Steps
1. `sequence_reference.py "Sequence 19"` → `raw/abw11-seq19-short-cut.mp4` (A1 only, speed-correct), Gate A OK 37.833 s.
2. `transcribe.sh --lang en` on CPU (GPU held by Premiere), under `.asr-lock`. 93 words.
3. Second listener: medium.en on the cut (0-9.4, 12.2-19.5, 33-37.8) + on the source takes at in x speed. Agree on every
   word but one: 3.23 s "because" → **"cuz"** (both hear it; `_fixes` in words.json). 15.9 s medium.en "why did we pass it
   out" vs large-v3 "while we passed out": kept large-v3 (the sentence only parses that way).
4. `captions.txt` (natural case, ? only, f*ck / f*cking censored as on Seq 04, shit/ass as spoken) →
   `sequence-captions.py srt --max-words 4 --hang 0.8` → `import`. Tool fix: captions end on the voice clip before an insert.
5. Verified on screen (window grab, no fronting): C1 runs 0 → 37.8 s with gaps over the inserts; "Rockstar went" at frame 0.

## Flags for him
- Default caption style sits low (≈ y1810, inside the bottom 300 px platforms cover): apply his Track Style / move it up.
