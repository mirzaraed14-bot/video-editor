# abw10-seq09-short — ABW10 · Sequence 09 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-19, waiting on the creator's review.**
Deliverable: `projects/abw10-seq09-short/abw10-seq09-short.srt` (78 cues, 0 → 70.683 s, 60 fps grid, max 5 words).
`caption_qa.py` PASSES. Next: drag the .srt into **ABW10 · Sequence 09** at 00:00, apply **"affanwizu yellow"**, baseline **y1224**.

**Flagged for the creator:** 10.5 s "POV reels banata tha" (Whisper: کیو وی); 29.2 s "bache mera content dekhen ge"
(heard "de ge"); 70.2 s last line "ye dekhte hain" (heard "dekhen thay", the cut ends mid-sentence).

## The job
- First @affanwizu job in **ABW10** (job named `abw10-…` so it can't collide with ABW8's sequence numbers). Checked it is
  an Urdu reel before forcing `--lang ur`: 1080×1920, one face-cam take `X:\Recordings\PBZ\C1376.MP4` (Scale 75) with its
  own audio, language detect hi 0.85 / ur 0.14 / en 0.00. ABW10 also holds the English Onyx reactions; read-only, the
  active sequence (TFTC reaction) was never switched. 70.683 s, no gaps, Gate A ✓. Chin y1109 → baseline **y1224**.
- Content: switching from overacting POV reels for an immature audience to serious, real-person content; followers per
  10,000 views went from 4-5 to around 12, "pretty damn good".

## What the checks caught
- **Opening loop (0–7 s):** the Urdu pass looped "dekhne ke liye bhi difference hota hai, meri shuru mai" ×3; the real line
  is "views mai bhi difference hota hai / meri jo shuru mai audience thi / wo immature audience thi / jiski wajah se mene
  apna content format switch kara". The loop detector's 15-word window missed it → widened to 17 words (catches it and
  the Seq 26 loop, no false alarm on Seq 42–51 or the four reference reels).
- **Loop + drop (51.5–60.6 s):** "ایسی" ×9 then 7.3 s missing; `transcript_check.py` printed the English listener's text,
  re-decoded wide: "jo mai pretend kar rha tha / to overacting / … / ke followers per / 10,000 views / … / around 12
  followers / pretty damn good".
