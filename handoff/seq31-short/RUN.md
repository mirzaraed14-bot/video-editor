# seq31-short — ABW8 · Sequence 31 (captions only, FIRST 3:45)

▶ **STATUS: DONE for 0 → 3:46 — caption track delivered 2026-10-06, waiting on the creator's review.**
Deliverable: `projects/seq31-short/seq31-short.srt` (274 cues, 0 → 226.0 s). The creator asked for the first 3:45 ONLY
(the sequence runs 11:47); 226.0 s is the natural break (a 3.7 s silence starts at 225.99, "ab kia kara" is the last line).
`caption_qa.py` PASSES on the 0 → 226 s span.
Next: drag the .srt into ABW8 Sequence 31 at 00:00, apply **"affanwizu yellow"**, baseline **y1205**.

**Flagged for the creator:** 0.0 s "mujy US based client aye" (first word unclear); 32.4 s "but ye winner hogya" (Urdu pass
heard لیکن = maybe "lekin"); 50.8 s “… to aap mujy budget / la kardo” (Urdu pass heard "low budget"); 136–139 s
"yar ese andhe pese / bana rahe ho".

## If the rest is wanted later
Everything for 3:46 → 11:47 is ready to resume: `raw/seq31-short-cut.mp4` (full 706.95 s, Gate A ✓), `transcript/words.json`
(2,442 words, full length). Still to do for that part: the English listener (`codeswitch_pass.py`, stopped), re-decodes of
the messy zones (gaps with speech at 555–565, 574–592, 611–617; a probable duplicate "just believe in the people" at
616–627; long words at 394, 495, 606), the GAP lines for 8 silent stretches (e.g. 381.9–393.8, 535.3–554.0), the lines.

## The job
- ABW8 · Sequence 31, 706.95 s, 114 V1 + 114 A1 clips of `X:\Recordings\PBZ\C1325.MP4` (1920×1080 at Scale 100), 7.8 s of
  timeline gaps kept. Rebuilt with the new `presets/instagram/affanwizu/sequence_reference.py` path (per-clip PCM audio):
  the one-filtergraph rebuild hit WinError 206 (command line too long) at 114 clips. Chin y1090 → baseline **y1205**.
- Content (first 3:45): the US-based client from the faceless brand, "Mr John Cena (for the sake of this argument)", the
  separate paid/organic channel idea, going all in at 10 shorts a day against advice, all hell breaks loose, the split.

## What the checks caught in 0 → 3:46
- **Translated English:** "for the sake of building the relationship" (Urdu pass: اس کی وجہ سے), "you're just putting cash
  into a furnace" (Urdu pass: فرنس میں کش کر رہے ہیں).
- **Squeezed words:** 29.8–32.4 s "basically pata ni kia / 20 hazar kyun aye thay / mujy yaad ni" was one stretched word.
- Re-heard: "US based client", "beech mai na" (not "peeche"), "70 80 views", "no shit sherlock holmes", "ache pese banaye".
