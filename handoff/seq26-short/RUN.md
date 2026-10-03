# seq26-short — ABW8 · Sequence 26 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-04, waiting on the creator's review.**
Deliverable: `projects/seq26-short/seq26-short.srt` (97 cues, 0 → 93.05 s). `caption_qa.py` PASSES.
Next: drag the .srt into ABW8 Sequence 26, apply **"affanwizu yellow"**, baseline **y1166**. After the creator
corrects any layers → learning pass into `presets/instagram/affanwizu/LESSONS.md`.

**Flagged for the creator:** 5.2 s "jab mene ye sab / shuru kara hai" (heard as "shuru karta hai"); 62.3 s "islye mujy
thora sa / ese lagta hai" (a word may be missing there); 75.3 s "creators ki zyada hoti hai" (Whisper heard a "ne" before it).

## The job
- ABW8 · Sequence 26, 93.05 s, no gaps. 30 V1 + 30 A1 clips of `X:\Recordings\PBZ\C1324.MP4` (1920×1080 at Scale 100,
  centre band), voice from the camera file. Rebuild 93.067 s (Gate A ✓). Chin y1051 → baseline **y1166**.
- Content: a video editor's portfolio is a bit fake (the client's brand carried the views); hire a creator rather
  than an editor, or both.

## What the gates caught (the worst transcript yet)
- **Gate B:** 10.2 → 15.8 s held 5.6 s of speech with no words, right after the Urdu pass LOOPED ("edit karta tha
  iske liye" ×3). Re-decoded 5.5–17.5 s: "to mai video editing karta tha / US based streamers ke lye / to unke bohat
  ache views ate thay … magar phir na jab mene khud apne lye videos banana shuru kari".
- **Four English phrases TRANSLATED by the Urdu pass**, all restored from the English listener + re-decodes:
  "the reason … is because" (اس کی وجہ ہے کہ), "but just because" (لیکن), "no offense to editors, it's just that"
  (ایڈیٹروں کو کوئی فرق نہیں …), "and that's a fact" (اور یہ ایک حقیقت ہے).
- New in `caption_qa.py` from this job: a LOOP warning, and وجہ / فرق نہیں / حقیقت added to the stand-in list.
