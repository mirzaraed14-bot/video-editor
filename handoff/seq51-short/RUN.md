# seq51-short — ABW8 · Sequence 51 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-13, waiting on the creator's review.**
Deliverable: `projects/seq51-short/seq51-short.srt` (174 cues, 0 → 167.8 s, 60 fps grid, max 5 words). `caption_qa.py` PASSES.
Next: drag the .srt into ABW8 Sequence 51 at 00:00, apply **"affanwizu yellow"**, baseline **y1265**.

**Flagged for the creator:** 0.0 s first word dropped (heard مجوری: "majority"/"majboori"?) → starts "mai aapko bata dun";
49.2 s "sab ka dimagh hai ke" (heard "dimagh barhti hai"); 137.2 s "uthani uthani / uthani uthani" (4×, both decodes agree).

## The job
- 49 V1 + 49 A1 clips of `X:\Recordings\PBZ\C1345.MP4` (Scale 100, two Position y values), music on A2 (Seven Days,
  0–28.6 s, not in the rebuild). 167.8 s, 60 fps, two timeline gaps 27.05–35.88 and 42.85–49.15 → captions OFF there
  (`@27.05 |`, `@42.85 |`). Gate A ✓. Chin y1150 → baseline **y1265**.
- Content: the reality of influencer brand deals — small creators DM brands, brands expect value (sales, follows, a metric),
  every deal dents you as a person, "mai khud pehnta hun, mujy ache lagte hain".

## What the checks caught
- **The ending dropped again (4th time):** words stopped at 163.1 s, 4.7 s of speech after it; the main pass squeezed
  "mujy ache lagte hain / theek hai… ni promote karta" 4.7 s early and lost "aapko pata hai, sunglasses mene promote kardi
  kyunke mujy asli mai ache lagte hain / mai khud pehnta hun". Last 13 lines timed from the wide re-decode.
- English restored: "easy mode" (Urdu pass: آسان موڈ), "they expect something in return" (heard "in it"), "sunshine and
  rainbows", "you know behind the scenes", "I don't give a shit", "that's not the case", "ad rights excluded", "as a person",
  deodorant / NVMe / DJI / JBL. "bhikari bana" re-heard (Whisper: بیغاری).
