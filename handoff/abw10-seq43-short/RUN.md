# abw10-seq43-short — ABW10 · Sequence 43 (captions only)

▶ **STATUS: DELIVERED 2026-11-05, waiting on the creator's review.**
Deliverable: `projects/abw10-seq43-short/abw10-seq43-short.srt` (64 cues, first at 00:00:00,000, 0 → 60.550 s, 60 fps grid).
`caption_qa.py` PASSES with no warnings. Next: drag the .srt into ABW10 · Sequence 43 at 00:00, apply **"affanwizu yellow"**, baseline **y1193**.

**Flagged for the creator:**
- 14.74 s "baat cheet waghera hui" (ur ساچیت, hi पाची: my reading); 17.65 s "idea aaya kisi ko" (ur آئے, hi है); 16.74 s "maine matlab" (ur only).
- 32.91 s "direct counter bheja" (ur بھیگا); 36.90 s "mukka pare" (ur also پڑا ہے); 46.73 s "bahar se le sahi hai" (the "le": ur + hi).
- 53.80 s "phenk de ga" (ur پھے گے گا); 59.66 s "whatever it doesn’t matter" (ur وہی تھا ڈازن میٹر, hi वो इता डाजन मेटर).
- Two deliberate caption gaps: 28.05-29.05 (no speech before the slip) and 30.43-32.05 (the "that smile" still, silent).

## The job
- 1080×1920 60 fps, 60.550 s (the sequence runs to 60.767: something on V2+ past the picture). V1: 30 clips of `X:\Recordings\PBU\C1434.MP4`
  at 1.1x, some 0.8x, + `that-smile-v0-aekqhvk8zj8g1.webp` at 30.43-32.05. Chin y1078 → baseline **y1193**. `--lang ur`, CPU.
- Content: thought the gym teaches you to fight; first boxing class, 2023: 80 kilo vs a 43 kg guy, sparring, "faltu tareen stance", he slips the jab and counters to the eye,
  white flash, reality check; "wolf bane hue aap or andar se aap koi dumbe hain"; everyone should do combat training once a week, whatever the sport.
- **Transcription ran the fallback:** WhisperX on CPU died four times (mkl_malloc / segfault, ~3-5 GB RAM free with Premiere headless + AME + Photoshop + AE open).
  `work/transcribe_fw.py` = same large-v3 int8, unbatched faster-whisper with 10 s chunks, model freed, then the same wav2vec2 ur alignment. It dropped "body waghera banate" 0.2-1.1 (the windows have it).
- Re-decoded ur + hi + en in 10 s windows (`work/redecode.txt`).
