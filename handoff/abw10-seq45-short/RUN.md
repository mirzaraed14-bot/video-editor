# abw10-seq45-short — ABW10 · Sequence 45 (captions only)

▶ **STATUS: DELIVERED 2026-11-05, waiting on the creator's review.**
Deliverable: `projects/abw10-seq45-short/abw10-seq45-short.srt` (47 cues, first at 00:00:00,000, 0 → 45.000 s, 60 fps grid).
`caption_qa.py` PASSES; warning resolved: LONG WORD 12.68 'exfoliation' (all three decoders hear only that word).
Next: drag the .srt into ABW10 · Sequence 45 at 00:00, apply **"affanwizu yellow"**, baseline **y1193**.

**Flagged for the creator:**
- 24.76 s "tayar ni hona tumhen" (ur گھنٹی/گھنڈی, hi वेहन नहीं); 25.61 s "hamen jana hai" (decoders stop at جانے).
- 28.48 s "oh bhaisab" (codeswitch بھائی صاحب, ur بھائی سب); 29.54 s "o ammi" (ur + hi "wo ammi").
- 38.98 s "or kesa mojza hai" (all decoders کسی/किसी: my reading).
- One deliberate caption gap: 31.50-32.20, the beat before “nikal gya” (loudness envelope).

## The job
- 1080×1920 60 fps, 45.000 s. V1: 22 clips of `X:\Recordings\PBU\C1433.MP4` at 1.1x / 0.8x / one 1.2x. Chin y1078 → baseline **y1193**. `--lang ur`, CPU.
- Content: girls start getting ready at noon for an 8 pm event vs boys asleep at 7:30; ammi wakes him, the nara comes out of the shalwar, 3 min 25 s shower, the boy is still ready first.
- Transcribed with the low-RAM fallback (`work/transcribe_fw.py`, LESSONS 2026-11-05): 0.7 GB RAM free at the start. Re-decoded ur + hi + en in 10 s windows (`work/redecode.txt`).
