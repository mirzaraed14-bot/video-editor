# abw10-seq20-short — ABW10 · Sequence 20 (captions only)

▶ **STATUS: DELIVERED 2026-10-23, waiting on the creator's review.**
Deliverable: `projects/abw10-seq20-short/abw10-seq20-short.srt` (190 cues, first at 00:00:00,000, 0 → 175.667 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 20 at 00:00, apply **"affanwizu yellow"**, baseline **y1201**.

**Flagged for the creator:** 29.97 "AyanGFX.com" (the commenter's handle as heard: "ayan G F X dot com"; spelling unverified);
0.00 "full hate mil li hai" (hi + en decodes hear it in the first 0.6 s, WhisperX does not); 63.7 "around 600 kuch";
66.4 "40 hazar something / ho jayen ge"; 68.9 "wo mene fresh monetize kara"; 92.05 "sahi hai jiska aap" (ur + hi agree,
en hears "whose"); 50.15 "hawabaz info".

## The job
- 1080×1920 60 fps, 175.667 s. V1/A1: 73 clips of `X:\Recordings\PBZ\C1390.MP4`, all 100 % speed, Scale 80, no gaps.
  Language hi 0.97 / ur 0.02 → `--lang ur`. Chin y1086 → baseline **y1201**. Speech runs the whole cut (no caption gaps).
- Content: reply to the hate on yesterday's "video editing is almost dead alone as a skill" reel: reads three comments
  (100 GB raw data in claude / "lol nice joke guys chill…" AyanGFX.com / "this is your answer") + "demotivational speaker",
  his channel numbers (530,000 subs, 466 million views), daily-wage editor vs agency CEO on retainers with 50 % deposits,
  AI agents vs "glorified employees", the time-saving pitch vs "X amount of views… until you do", competition is low.
- **Quotes:** every line of a comment he reads out and of the two pitches he imitates carries its own pair (the BELIEVE rule).
- **Transcript repair:** WhisperX dropped 46.3–49.6, 74.0–76.3 and 148.7–154.9 and looped "apni apni" ×9 at 146–151;
  a hi + en re-decode of 15 windows restored them ("demotivational speaker… ye to matlab funny tha actually",
  "magar the goal is", "and that's a very good thing", "majority pakistan mai video editors"), plus "that's fine" at 83.6
  (missed by both passes), "through retainers", "full hate mil li hai", "hath se control" (WX: ایسی طرح سے).
- `caption_qa.py` counted "AyanGFX.com" as ONE spoken word (FAIL HANGING, 1.52 s); fixed in the tool: a web address now
  counts as said (AyanGFX.com = ayan + G F X + dot com = 6).

## Better than the last one (CLAUDE.md learning loop § 5)
First reel that reads out comments: the quote rule measured on BELIEVE (one pair per line) applied to every read-out line,
and the three-language re-decode ran on ALL gate flags in one batch before writing, not after a review.
