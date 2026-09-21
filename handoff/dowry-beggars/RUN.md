# RUN: dowry-beggars (ABW6 · Sequence 18), FULL EDIT: cut + captions

## ▶ STATUS: SHIPPED (2026-09-19): `Final Renders/ameer.mov`, uploaded by the creator
Learning pass done: everything the creator added or changed is in `presets/instagram/affanwizu/reel-recipe.md`
and `LESSONS.md` (2026-09-19 learning pass). Nothing left to do on this job.

## (earlier) STATUS after the creator's trim
The creator trimmed Sequence 18 to **24.40 s** (their cut is final). `transcript/cuts.json` = THEIR timeline now
(Claude's version kept as `cuts.v1-claude.json`). Captions rebuilt for it: **`dowry-beggars-captions-v2.srt`**
(23 lines, editable caption track). Old caption lines: `captions/captions.v1.txt`.

## (earlier) STATUS 2026-09-19 07:12
First full edit for @affanwizu. **The cut is replayed into Sequence 18** (9 clips on V1 = C1251.MP4 picture,
9 on A1 = "C1251 Audio Extracted.wav", 27.38 s, Scale 125 / Position 0.5127,0.5). The raw take is untouched in
**"Sequence 18 RAW (backup)"**. Captions: `captions/hf-graphics/captions/renders/dowry-beggars-captions-yellow.mov`
(yellow, y1103). **Scripted import is still broken in Premiere**, so the creator drags it onto V2 or V3 at 00:00.
The creator adds music at the end. The project is NOT saved by us.

- Format: short-form 9:16 (the creator's 1080×1920 sequence), 60 fps. Preset `presets/instagram/affanwizu/`, style yellow.
- Hook = "agar aap jahez maangte hain…" (the opening line, last of 4 takes). Takeaway = asking for dowry,
  or making your parents ask for it, is begging; no shame, not fit for marriage.
- Transcript: `transcript/words.json` (Urdu, CPU, ~4 min). `transcript/roman-pass.json` = en pass (translated).
- EDL: `transcript/cuts.json` (polished, pinned, dead-air gate PASSED). Cut transcript: `outputs/dowry-beggars.transcript.json`.
- Captions job: `captions/` (built by `presets/instagram/affanwizu/cut_reference.py --scale 125 --x 0.5127`).
- Skipped: audio polish (not asked; the creator mixes music themselves), grade (short-form: none), SFX, title (theirs).

## Cut decisions
- Opening: kept take 4 (46.5–51.6) of 4. Killed takes 1–3 and the false start at 25.2.
- "larki ke abbu…" beat: kept take 2 (90.1–94.3). **Killed take 1 WITH its "ye jebein phati hui hain tumhari kya,
  paise girte rehte hain?" joke** (83.6–86.0): last-take rule. The flow reviewer argued it is distinct content;
  offer it back to the creator, as a graft after seg 4.
- "aur bhai doosre ki di hui cheez": graft onto the 2nd utterance (113.13).
- End chatter at 144.8 ("bas / okay this is enough") killed.

## Caption flags for the creator
- Mechanical re-ASR (2026-09-19 07:25): all 9 boundaries OK; "apna" confirmed; no audible "ko" → caption is "aap jaise logon".
2. 5.1 s "**bhikari** kehte hain"
3. 10.6 s "larki **ke** abbu bhai": "ke" isn't in the ASR
4. 22.1 s "**laiq** hi ni ho shaadi ke" (lā'iq, fit/worthy)
5. 25.8 s "wo itne ameer **wameer**" (ASR: امیر و امیر)
