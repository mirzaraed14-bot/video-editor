# RUN: abw11-seq13-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-18 ~00:30: DONE in the URDU MIX style (his call: "caps for this but in the urdu mix style"), hand-off sent.**
- `outputs/abw11-seq13-short.urdu-mix-layer.mov`: transparent full-frame layer (qtrle RGBA, 73.6 s, 60 fps), both lines, for V2 at 00:00. Built from `work/bilingual/v2_lin` (linfix.py, background measured rgb 17,7,5).
- `outputs/abw11-seq13-short.urdu-mix-preview.mp4`: the same burned over the cut (sRGB, unfixed cues = what Premiere shows). `outputs/urdu-mix-stills.png`: 6 frames across both framings.
- Look = Seq 10 v2 exactly: Urdu Noto Nastaliq 48 px baseline y1346 (max descent 28 px, 12 px min gap), Roman Ubuntu Light 48 ALL CAPS baseline y1420 (widest 710 px), gold, glow, hard shadow.
- `abw11-seq13-short.srt` (73 cues, normal single-line style, baseline y1179 = chin 1064 + 115), caption_qa PASS: built for the switch times; use the layer OR the .srt, not both.
Sequence: **ABW11 · Sequence 13**, 36 V1 clips of `X:\Recordings\PBU\C1481.MP4`, 60 fps, 2 framings (Scale 100 band y420-1500 + a punch-in), cut 73.600 s (something on V2+ runs on to 78.55 s). Read only, nothing changed in Premiere.

## Content
Growing the Urdu page (47000 followers, 8.1 million views in 30 days): the number one thing he learned: don't just pick up the camera and talk (very beginner advice), find a proven viral format and put your topic in it: his slow-mo video copied a format, his spin was Karachi areas and funny topics, then the A6700 cinematic vibe; mask your topic in an already proven viral format and it goes viral, ustad.

## Steps
1. `sequence_reference.py "Sequence 13"` → 73.600 s, Gate A OK. `chin-line.py` → median y1064 (lowest y1333 at 2.8 s is the phone-in-face opening).
2. `work/run_all.sh` queued behind Seq 11 and another session's research ASR (~30 min wait on `.asr-lock`), then first try: 283 words. transcript_check DROPs = "followers dashboard hai", "million views 30 days" (both in the English listener), a pause at 41.6.
3. 3 probes (`work/probe.txt`): "slow jaati hai" (no "ho"), "maine apna A6700 liya / theek hai slightly background light / you know skool play button / full cinematic vibe di", "mask kar ke bolenge na to wo phir confirm viral jaye gi ustad".
4. `captions.txt` + `captions.ur.txt` (73 lines each) → build.py `--y 1179 --srt --dur 73.600` → caption_qa PASS (first run FAILED "8.1 million views" as HANGING: digits pack 5 spoken words into 3; joined with "30 days"). → render_cues.mjs (v2 params) → linfix.py → assemble.py (layer + preview).

## Flags for his ear
45.42 "usme maine apna spin dala" (listeners: "spend") · 58.23 "you know skool / play button" · 0.00 "mere hain urdu wale page par" · 30.10 "you wanna talk about" (WhisperX dropped it, timed off the windows).
