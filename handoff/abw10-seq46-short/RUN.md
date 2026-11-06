# abw10-seq46-short — ABW10 · Sequence 46 (captions only)

▶ **STATUS: DELIVERED 2026-11-07, waiting on the creator's review.**
Deliverable: `projects/abw10-seq46-short/abw10-seq46-short.srt` (123 cues, first at 00:00:00,000, 0 → 103.917 s, 60 fps grid).
`caption_qa.py` PASSES. Warnings stay: CONNECTOR 0.03 (the first word is clipped by the cut: "lekin" by ur + hi, en "See", codeswitch دیکھیں; no fricative in the audio, so not "see"; could be "but"), LONG WORD 42.03 (resolved: WhisperX's span was wrong, "continuously" is 41.80-42.40).
Next: drag the .srt into ABW10 · Sequence 46 at 00:00, apply **"affanwizu yellow"**, baseline **y1154**.

**Flagged for the creator:**
- 42.40 s "hote ja rha hai" (ur + hi ہٹے/हटे, en+prompt hote); 47.36 s "sur" (ur سر, en voice); 56.56 s "bulwana" (ur گلوانا, hi गिलवान, en melt).
- 34.75 s "mai andar hall ke ye"; 35.65 s "taha g"; 36.40 s "concert wonsert"; 58.93 s "tri fit" (en Tri-Fet); 60.75 s "chop chop wok" (all hear "work").
- 97.21 s "bohat appreciated hun", as said (he may have meant appreciative); 0.00 s "lekin".

## The job
- 1080×1920 60 fps, 103.917 s. V1: 56 clips of `X:\Recordings\PBU\C1452.MP4` at 1x. Chin y1039 → baseline **y1154**. `--lang ur`, CPU; WhisperX ran normally (6.6 GB free).
- Content: not roasting the Pakistan Influencer Awards; Super Biscuit's speaker and 1 lac incentive to scream "shehar mai shehar mai / gaon mai gaon mai"; the noise drove the big boys outside; a regulatory body should manage vendors; next time better managed.
- WhisperX dropped 8.65-16.95 and 46.10-47.36 and garbled 31.85-40.4 (Hindi and English passes rescued "sing their hearts out", "taha g"). Re-decoded ur + hi + en in 10 s windows (`work/redecode.txt`, `work/redecode2.py`).
