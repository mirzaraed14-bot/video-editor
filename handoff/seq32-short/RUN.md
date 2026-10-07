# seq32-short — ABW8 · Sequence 32 (captions only; part 2 of the Seq 31 story)

▶ **STATUS: DONE — caption track delivered 2026-10-08, waiting on the creator's review.**
Deliverable: `projects/seq32-short/seq32-short.srt` (241 cues, 0 → 197.117 s). `caption_qa.py` PASSES.
Next: drag the .srt into ABW8 Sequence 32, apply **"affanwizu yellow"**, baseline **y1209**.

**Flagged for the creator:** 91.6 s "ab wahan pe / mujy maarne lage ke" (Whisper heard پڑھنے; "taane maarne"?);
169.2 s "jo bilkul farigh thay" (heard فارق); 181.6 s "warna ulta or nuqsan / aapka hi hoga" (heard "unhone … ho gaye").

## The job
- 63 V1 + 63 A1 clips of `X:\Recordings\PBZ\C1325.MP4` (same take as Seq 31), no gaps, 197.117 s. Rebuilt with
  `sequence_reference.py` (first job on it, Gate A ✓). Chin y1094 → baseline **y1209**.
- Content: the split, the new agency buttering them up, "we'd like you to step off from this channel", the 50 % payment,
  30,000 → 29,000 followers vs 1,500 → 37,000, "just believe in the people you have hired".

## What the checks caught
- **Loop + drop at 85–91.6 s:** "mujhe" ×14, then 3.4 s missing. Re-decoded: "matlab off the table / unhone mujy matlab /
  basically nikal hi diya / acha ab kia hua / ke na meri na / pichli videos ki / payments due thi".
- **Misplaced sentence at 132.5–140 s:** the main pass jumped from "payment dene mai" to "jab mene unke sath…" 3 s early and
  lost "aaj bhi mai, ab wo obviously, mujy unka channel pata hai, unka instagram, mujy sab pata hai". Re-timed from a wide re-decode.
- 168–184 s re-heard: "magar it was / worth a shot", "agar magar na kara karen", the quoted "kisi or ko utha ke le lo".
- English listener run after delivery: 4 fixes in v2 — "just because of this", "let’s get to work", "mere peeche behind the scenes", "even though".
