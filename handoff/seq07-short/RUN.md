# RUN: seq07-short (ABW8 · Sequence 07) — captions only

## ▶ STATUS: delivered (2026-09-25), waiting on the creator
`seq07-captions.srt` — 81 lines, **max 5 words each** (the creator's ask; the channel default is 3–5),
yellow deep-talks style, timed to the 68.18 s cut. Drag it onto the sequence at 00:00 and apply the
"affanwizu yellow" track style (scripted import is still broken on this machine).

- Cut: the creator's, untouched. 37 clips on V1 from `F:\DCIM\CAM_001\CAM_20260922180932_0309_D.MP4`
  (Scale 56, Position 0.4287), and **A1 is a separate voice mix** (`good-esv2-30p-bg-10p-music-10p.mp3`
  + its "Audio Extracted" wav) whose source times differ from the picture — the reference was rebuilt
  per clip, picture from V1 and sound from A1.
- **Language trap:** Whisper auto-detected `hi` and TRANSLATED the speech into English on the first pass
  (a clean-looking English transcript that was pure translation). Re-run with `--lang ur` gave the real
  322 Urdu words. Always confirm the language on an ABW8 sequence — that project holds both English
  archival shorts (Sequence 03) and Urdu talking-head reels (this one).
- Style call: Urdu talking head → @affanwizu yellow, NOT the Abundance Wisdom shorts caption style
  (Gretaros ALL CAPS, colour gradients) that the rest of ABW8 uses. Flip with `--style` if the creator wants it.
- Baseline **y1159** = chin 1044 + 115, measured on the rebuilt cut.

## Flags for the creator (unsure words)
1. 10.1 s "naam **lun ga** magar" (ASR: ملوں گا)
2. 20.0 s "**mujh se** bhi bade creators" (ASR heard پچھ سے)
3. 46.2 s "with a **crisp hook**" — could be "crispy hook"
4. 59.4 s "mai koi **khan sahab** thori hun"
5. 67.5 s "us se respect **thori tied** hoti hai" (ASR: ٹائیڈ)
