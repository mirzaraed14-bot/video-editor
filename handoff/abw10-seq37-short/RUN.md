# abw10-seq37-short — ABW10 · Sequence 37 (captions only)

▶ **STATUS: DELIVERED 2026-11-02, waiting on the creator's review.**
Deliverable: `projects/abw10-seq37-short/abw10-seq37-short.srt` (54 cues, first at 00:00:00,000, 0 → 45.067 s, 60 fps grid).
`caption_qa.py` PASSES (the 6 LOOP warnings = his real football / hockey repetition, heard by every decoder).
Next: drag the .srt into ABW10 · Sequence 37 at 00:00, apply **"affanwizu yellow"**, baseline **y1187**.

**Flagged for the creator:**
- 31.11 s **"ab wo ijtimai hota hai"**: every decoder (WhisperX, ur, hi, en, even prompted toward English) hears استعمائی /
  इस्तेमाई "istemaai"; "ijtimai" (collective: the whole country comes for Pakistan vs India) is my reading.
- 19.02 s "pura hua hota hai bhai" (all decoders; en "it's full"); 15.61 / 18.21 s "chal li hai" (as heard).
- 41.85 s "oye hockey" (WhisperX + English listener hear "oye").

## The job
- 1080×1920 60 fps, 45.067 s. V1/A1: 19 clips of `X:\Recordings\PBU\C1412.MP4`, 18 at 1.1x and one at 0.8x; nothing above V1.
  `--lang ur`, CPU (GPU busy). Chin y1072 → baseline **y1187**. Speech runs the whole cut.
- Content: "genuinely" Pakistan has more football talent than cricket; nobody plays cricket in the galis now (futsal grounds,
  courts booked every Saturday), the hype is gone, the country only gathers for Pakistan vs India "or wo bhi hum hamesha haar hi
  jate hain, mashallah"; at his MMA gym, night and morning, football / hockey, "cricket ni chal rha hota".
- **Quotes:** the friends' lines only (“yar cricket ka plan hai” / “saturday ko aa jao”, “yar wo court book” / “kar dia hai” /
  “saturday ko aa jana” / “match hai”); his narration unquoted.
- Re-decoded ur + hi + en in overlapping 10 s windows (`work/redecode.txt`; a single 45 s pass hallucinated after ~30 s).

## Better than the last one (CLAUDE.md learning loop § 5)
Every disputed word was settled by three decoders in 10 s windows before writing, and the one word they all mis-hear is
flagged with its time, so the review is one listen.
