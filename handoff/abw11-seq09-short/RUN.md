# RUN: abw11-seq09-short (@affanwizu captions, ABW11)

## ▶ STATUS: resume here
**2026-11-16 ~01:30: captions DONE, caption_qa PASS (with codeswitch.json: 56 English words), hand-off sent.** `abw11-seq09-short.srt`, 71 cues, 0 → 68.950 s, yellow deep-talks, baseline **y1209** (median chin y1094 + 115; 138 samples, 0 no-face).
Sequence: **ABW11 · Sequence 09** (only one by that name, active), 32 V1/A1 clips of `X:\Recordings\PBU\C1482.MP4`, 1x, 60 fps, picture Scale 100 / Position 0.5,0.5, no gaps. Read only, nothing changed in Premiere.

## Content
Aura on your profile: viewers' private accounts are a personal brand too (250-300 followers); people won't follow funny but "chapri type" content because they don't want to attach themselves to it; the follow economy goes to elevated-status profiles; guys follow to impress a girl; a rough estimate for creators: 1 lac views → 80 to 100 followers is healthy, less means something is wrong.

## Steps
1. `sequence_reference.py "Sequence 09" projects/abw11-seq09-short` → Gate A OK (68.950 s).
2. `chin-line.py` → median chin y1094 → baseline y1209.
3. Machine: Premiere + Media Encoder + Photoshop open, ~6 GB physical / ~6.7 GB commit free (limit 72 GB), so NO batched WhisperX. `work/transcribe_fw.py`: faster-whisper large-v3 int8, cpu_threads=2, unbatched, under the machine-wide `.asr-lock` (`projects/_onyx-batch9-2026-11/reactions/.asr-lock`, mkdir) with a memory guard (phys ≥ 3 GB, commit ≥ 4.5 GB) → 276 words; `transcript_check.py` OK.
4. Queued behind the same lock, one at a time: `work/redecode.py` (7 ur/hi/en windows, one process, resumable) → `codeswitch_pass.py` (OMP/MKL threads 2) → `work/probe.py` (9 short probes) → `work/probe.txt`.
5. Probes settled: "public figure **theek hai**" (WhisperX dropped it; hi window + English listener + both probes), "kese / **bhai** aap logon ke", "ke **you know** jinka content", "thora **sa na matlab** chapri type lage" (not "thora zyada"), "to wo **unhein** kabhi follow ni karte".
6. `captions.txt` → `build.py --style yellow --y 1209 --srt --dur 68.950` → `caption_qa.py` **PASS** (warn left on purpose: 3.36 CONNECTOR 'حقیقت': every ur/hi pass and both probes say "haqeeqat baat bata rha hun", the en pass translates it "I'm telling you the truth"). No `?`, commas or full stops in the `@` lines; numbers as digits (250, 300, 1 lac, 80 to 100).

## Flags for his ear (my readings)
3.36 "haqeeqat baat bata rha hun" · 12.46 "bhai aap logon ke" (ur "log", hi "logon") · 14.02 "aapke unke 250 follower" · 53.62 "usne aa kar dekh lia" (ur + English listener + en "she came and saw"; hi + WhisperX "agar") · 56.23 "mai chale gyi" (said "chale").
