# RUN: abw11-seq06-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-14 ~16:10: v2 DONE, caption_qa PASS, hand-off sent. He trimmed Sequence 06 to 141.783 s** (74 clips; 8.78 s removed at v1 15.20-15.85, 32.97-33.30, 40.95-41.57, 89.39-96.12, 140.04-140.49) and punched in on some clips (16 framings, up to 180 %). `abw11-seq06-short.srt` = v2, 155 cues, 0 -> 141.783 s, baseline kept at **y1173** (v2 median chin y1069, +11 px: noise; his track style stays valid). v1 kept in `v1/` (captions, srt, sequence, words, codeswitch, cut). Method: `work/remap_v2.py` maps v1 time -> source -> v2 time by the A1 clips (pure arithmetic, no re-transcription), `work/make_v2.py` writes captions.txt + remapped words/codeswitch, `work/probe_v2.py` re-decoded the 5 joins on the v2 cut: 3 were pauses (text unchanged), 'wo' cut before 'organic hain', 'yar' + the boom diggy stretch + the first 'montage' cut (9 cues dropped). Note: Sequences 03 and 05 in ABW11 now hold OTHER videos (affancuts titles header, Scott pbd urine prank) and Sequence 07 is the MJ 'Brother Saw Him AGAIN' Short.

**2026-11-14: captions DONE, caption_qa PASS (with codeswitch.json: 88 English words; "you know" added at 46.92), hand-off sent.** `abw11-seq06-short.srt`, 164 cues, 0 → 150.567 s, yellow deep-talks, baseline **y1173** (chin 1058 + 115). 
Sequence: **ABW11 · Sequence 06** (only one by that name, active), 71 V1/A1 clips of `X:\Recordings\PBU\C1480.MP4` (A1 = `C1480 Audio Extracted.wav`), 1x, 60 fps, picture Scale 80 / Position 0.588,0.5, no gaps. Read only, nothing changed in Premiere.

## Content
Page review of LUNA Coffee (Karachi; name checked against Profit and ProPakistani, Nov 2025) and its founder Fahad bhai: the pinned reel is a paid ad, Fahad's own videos (the 300 wali coffee) are organic; Fahad should go all in on personal branding; low-light cinematic, lifestyle-based montages on trending songs (boom diggy diggy); "collab on luna", not the other way around.

## Steps
1. `sequence_reference.py "Sequence 06" projects/abw11-seq06-short` → Gate A OK (150.567 s).
2. `chin-line.py` → median chin y1058 (14 no-face samples) → baseline y1173.
3. `transcribe.sh --lang ur` (WhisperX, CPU) → 554 words; `transcript_check.py`: LOOP 98.9-108 + DROP 101.6-106.5 + LONG 72.9.
4. Window re-decode, 15 windows ur/hi/en → `work/redecode.txt`. The one-process run died on mkl_malloc after 3 windows; finished with `work/redecode_one.py` (one process per window, **cpu_threads=2**) driven by `work/run_rest.sh` (skips done windows, never two decoders at once, waits for commit headroom). See LESSONS 2026-11-14.
5. The loop was "stay with me"; the drop was "obviously aap product dikhayen ge … by the way"; "expensive" is said once. Every line timed from the windows.
6. `captions.txt` → `build.py --style yellow --y 1173 --srt --dur 150.567` → `caption_qa.py` **PASS** (HANGING "lifestyle based" fixed: he says it slowly, life 96.15 / style 96.90 / based 97.30 by the loudness envelope, so it is split into two cues; `work/probe_span.py`).

## Flags for his ear (my readings)
3.52 "braces lage hain" · 8.68 "2500 likes" (heard "dhai hazar") · 14.90 "ye product base hai reel" · 18.50 "ye oh ye / aap log piyen bhai" · 44.42 "86,000" · 55.40 "ye zara peeche karun" · 85.88 "banwayen aap" · 147.52 "jab ye fahad bhai ne" (ur/hi heard "maine"; the English pass and the context say Fahad made the 300 video).
