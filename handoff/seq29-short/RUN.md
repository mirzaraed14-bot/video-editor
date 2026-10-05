# seq29-short — ABW8 · Sequence 29 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-06, waiting on the creator's review.**
Deliverable: `projects/seq29-short/seq29-short.srt` (36 cues, 0 → 32.483 s). `caption_qa.py` PASSES (no warnings).
Next: drag the .srt into ABW8 Sequence 29, apply **"affanwizu yellow"**, baseline **y1130**. After the creator
corrects any layers → learning pass into `presets/instagram/affanwizu/LESSONS.md`.

**Flagged for the creator:** 13.5 s "bolo le bhai honestly" (both decodes hear "le"; could be "bolo na").

## The job
- ABW8 · Sequence 29, 32.483 s, no gaps. 11 V1 + 11 A1 clips of `E:\Skool Recordings\5 Sept Batch\PBU\C1250.MP4`
  (1920×1080 at Scale 100, centre band), voice from the camera file. Rebuild 32.483 s (Gate A ✓).
  Chin y1015 → baseline **y1130**.
- Content: take constructive criticism; when you're learning, ask without shame, "mujy hi to sawal karna hai".

## What the gates caught
- **The ending, for the third reel (Seq 17, 20, 29):** `words.json` ended at 25.9 s, the cut at 32.5 s, 6.3 s of speech
  in between. WhisperX had dropped "is tarah aapko or confidence mile ga ke mai to naya hun, mai kyun dar rha hun
  sawal karne ke lye, mujy hi to sawal karna hai, or kisne karna hai phir" and pulled "jo professional hai wo" 6.7 s
  early. The last nine lines are timed from a wide ur + en re-decode of 22.8–32.5 s.
- The English listener discarded two chunks as prompt echoes (10–17 s and 30–32 s), so the middle was checked against
  the en re-decode instead: "honestly", "learning phase", "insult", "professional" all said in English.
