# abw10-seq30-short — ABW10 · Sequence 30 (captions only)

▶ **STATUS: DELIVERED 2026-10-27, waiting on the creator's review.**
Deliverable: `projects/abw10-seq30-short/abw10-seq30-short.srt` (36 cues, first at 00:00:00,000, 0 → 40.683 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 30 at 00:00, apply **"affanwizu yellow"**, baseline **y1312**.

## The job
- 1080×1920 60 fps, 40.683 s (sequence 40.70 with the "Get out" SFX). V1/A1: 16 clips of `X:\Recordings\PBU\C1369.MP4`
  at **1.1x and 0.8x** (the speed-aware rebuild, Gate A exact). A2 Chopin Nocturne Op. 9 No. 2 + "Get out" SFX, A3 gunshots:
  not in the transcript. Language hi 0.96 → `--lang ur`. Chin y1197 → baseline **y1312**.
- Content: the exam-day skit (comparing answers in the hall: "question 4 ka answer kia tha / 678 tha", "7 into 10 ki power
  97", "322 tha na", "minus 9,675", "janaza exam hall mai hi nikal dia gaya tha", "abbu ne pucha… acha hua tha").
- **Quotes:** every dialogue line and his inner voice, one pair per line; narration ("dusra aye ga na / ur ke aye ga achanak")
  unquoted. Caption off over the gunshot pause 29.05–32.04.
- Re-decoded (ur + hi + en): "wo 678 tha" (ur heard اوہ), "achanak" (WX missed), "ni" ×4 before "minus" (en + the English
  listener count 4, ur + hi 3; Whisper collapses repeats, so 4).
- **Tool fix:** caption_qa FAILed "minus 9,675" (4.5 s of speech for 7 spoken words) although every word is there: the clip
  plays at 0.8x. The hanging check now measures speech at normal speed using `transcript/sequence.json` (slowed clips only);
  Seq 12 re-checked, still PASS.

## Better than the last one (CLAUDE.md learning loop § 5)
Second speed-changed reel: the gate now understands clip speed too, so a slowed comic beat is captioned as one line the way
he says it instead of being chopped to satisfy the checker.
