# seq41-short — ABW8 · Sequence 41 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-10, waiting on the creator's review.**
Deliverable: `projects/seq41-short/seq41-short.srt` (86 cues, 0 → 69.867 s). `caption_qa.py` PASSES.
Next: drag the .srt into ABW8 Sequence 41, apply **"affanwizu yellow"**, baseline **y1110**.

**Flagged for the creator:** 19.6 s "job bhi karhe hote ho" (the English listener didn't hear "karhe hote ho"; the Urdu and
English re-decodes did); 64.4 s "unke koi aap / sage thori hue" (as heard).

## The job
- 34 V1 + 34 A1 clips; picture `X:\Recordings\PBU\CAM_20261009214139_0315_D.MP4` at Scale 73, voice
  `C:\Users\affan\Downloads\Music\blue-esv2-32p-bg-10p-music-10p.mp3`. The cut ends at 69.867 s; an Adjustment Layer on V2
  runs to 74.533 s. Rebuilt with `sequence_reference.py` (Gate A ✓). Chin y995 → baseline **y1110**.
- Content: creators who call their life hard vs a 9 to 5; "big respect to 9 to 5 wale bhai".

## What the checks caught
- **Loop + drop at 12.7–21.9 s:** the Urdu pass wrote "bohat" ×15 and then nothing for 5.9 s. The English listener had the
  real words with good timing: "way way easier / than a 9 to 5 / shuru mai haan / mushkil hota hai / koi do do cheezain /
  sath karni parti hoti / kyunke aapko ni pata hota / ye sab kaam kare ga / to aap side pe / job bhi karhe hote ho / phir
  baad mai". A narrow-window Urdu re-decode of the same span compressed its timestamps by ~8 s, so the English listener's
  times were used.
