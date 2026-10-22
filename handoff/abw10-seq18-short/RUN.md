# abw10-seq18-short — ABW10 · Sequence 18 (captions only)

▶ **STATUS: DELIVERED 2026-10-22, waiting on the creator's review.**
Deliverable: `projects/abw10-seq18-short/abw10-seq18-short.srt` (77 cues, first at 00:00:00,000, 0 → 77.567 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 18 at 00:00, apply **"affanwizu yellow"**, baseline **y1236**.

**Flagged for the creator:** 4.1 s "or kafi in skill hai" (every decoder hears "in skill"); 33.9 s "mai aik launde ko / deta hun"
(Whisper hears لوڈ کو / "a Lord"; "hun" vs "tha" split); 57.5 s "itni saari agency" (heard singular).

## The job
- 1080×1920 60 fps, 77.567 s. V1/A1: 36 clips, C1373 (0–54.58) then C1374, all at 100 % speed, Scale 76, no gaps.
  Language hi 0.94 / ur 0.04 → `--lang ur`. Chin y1121 → baseline **y1236**. Speech runs the whole cut (no caption gaps).
- Content: video editing is no longer a skill you can sell on its own (US clients, "please esa na kariye ga", 2021 → now,
  value proposition, $300/200/100 race to the bottom, tie it to a result: "20 hazar / 50 hazar / 1 lac views den ge",
  agencies with 5–10 editors get 20 likes, be a viral creator for others and package their raw).
- English the Urdu pass translated, restored from the English listener / en + hi re-decodes: **need** (WX wrote ضروری),
  **US ke clients** (WX: ایسے کلائنٹوں کے لئے), **convince**, **instead**, **guaranteed**, **long form**, **result tie**,
  **effects**, **package up**, **raw**, **for others**.
- Numbers: "20 hazar / 50 hazar / 1 lac" (Whisper printed 1,00,000 with lakh grouping → said in Urdu), "2021", "300 dollar",
  "5 10 editor", "10 20 dollar".
- "seedhi si baat hai" (WX: سی دی سی بات ہے; the en decode "simple thing").

## Better than the last one (CLAUDE.md learning loop § 5)
The connector check now works both ways: WhisperX translated "need" and garbled "US ke clients", and both came back from the
English listener + a Hindi-script decode before a line was written, instead of after a review.
