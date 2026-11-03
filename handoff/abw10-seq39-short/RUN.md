# abw10-seq39-short — ABW10 · Sequence 39 (captions only)

▶ **STATUS: DELIVERED 2026-11-03, waiting on the creator's review.**
Deliverable: `projects/abw10-seq39-short/abw10-seq39-short.srt` (65 cues, first at 00:00:00,000, 0 → 59.733 s, 60 fps grid).
`caption_qa.py` PASSES (LONG WORD 18.57 resolved: it hid "income tax … aap log", captioned).
Next: drag the .srt into ABW10 · Sequence 39 at 00:00, apply **"affanwizu yellow"**, baseline **y1187**.

**Flagged for the creator:**
- 18.26 s **"income tax dekho aap log"**: all three decoders hear "de wo / devo"; "dekho" is my reading.
- 9.60 s "khalli walli" (as heard: ur خلی ولی, hi खल्ली-खल्ली); 0.00 s "jab" (English listener; ur/hi/en hear ab / tab / now).
- 43.69 s "claude ka zamana hai bhai" (en "Claude's"; Whisper ur: کلوڈ).

## The job
- 1080×1920 60 fps, 59.733 s (the sequence runs to 64.13 s: something on an audio track past the picture; V2+ empty).
  V1/A1: 27 clips at 1x. `--lang ur`, CPU. Chin y1072 → baseline **y1187**. Speech runs the whole cut, to the last frame.
- Content: 5-6 crore cars on show vs "aap 2010 wale daur mai reh rhe hain" (school → college → university → nokri); petrol /
  bijli / grocery vs graduates' 80,000 per month; far less talented people make 100x if not 500x; this era's leverages (skill,
  youtube channel, funnel, low-ticket info product to the US, profile → foreign clients); "claude ka zamana hai"; the forced
  “ye tumhari hai destiny”; times have changed; inflation; "genuinely aap far more talented hain aise logon se".
- Re-decoded ur + hi + en in 10 s windows (`work/redecode.txt`).
- The last line was split at "logon se" (59.16) so it holds to the cut end: the final cue otherwise ends 0.4 s after WhisperX's
  last word (59.42), and he talks to 59.73 (caption_qa UNCAPTIONED).
