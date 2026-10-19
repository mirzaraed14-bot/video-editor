# abw10-seq12-short — ABW10 · Sequence 12 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-20, waiting on the creator's review.**
Deliverable: `projects/abw10-seq12-short/abw10-seq12-short.srt` (10 cues, 0 → 40.583 s, 60 fps grid). `caption_qa.py` PASSES.
Next: drag the .srt into ABW10 · Sequence 12 at 00:00, apply **"affanwizu yellow"**, baseline **y1445**.

**Flagged for the creator:** 4.1 s "insidious" (the film; Whisper heard ان سی ڈی ایس / इनसीडियस); 8.5 s "ab wo sar / kamot se ni"
(every decoder hears this; meaning unclear); 34.6 s "agar aap" (the sentence is cut there).

## The job
- Checked Urdu before forcing `--lang ur` (hi 0.84 / ur 0.14 / en 0.01), 1080×1920 60 fps. V1: 15 clips of
  `X:\Recordings\PBU\C1379.MP4` at 118 % with punch-ins to 356 %, plus 4 stills (3 screenshots, 1 webp); A1 voice; A2 the
  Undertaker theme, A3 a gunshot (neither in the rebuild). Voice/cut ends 40.583 s; adjustment layers run to 42.58.
  Chin y1330 (the 118 % framing sits low) → baseline **y1445** (inside y200–1620).
- **Mostly visual comedy:** 9.4 s of speech in 40.6 s (4.1–10.1, 18.5–23.7, 34.6–35.0). Captions show ONLY while he speaks
  (blank before 4.1 s, off over the stills/reaction stretches and after 35.2 s), the Seq 51 rule for real silences.
- Content: Insidious and Asian horror movies vs the ones he shows; "agar aap unme se jo goron ki movies dekh kar hi dar jate,
  to ye movies aap apne lye dekho".

## Better than the last one (CLAUDE.md learning loop § 5)
First reel with stills and big punch-ins on V1: `sequence_reference.py` framed every clip as Premiere does (stills included)
and the audio came from A1 only, so the music and gunshot never touched the transcript; a three-language decode (ur/hi/en)
resolved the film name the Urdu pass could not ("Insidious").
