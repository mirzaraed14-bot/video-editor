# abw10-seq33-short — ABW10 · Sequence 33 (captions only)

▶ **STATUS: DELIVERED 2026-10-28, waiting on the creator's review.**
Deliverable: `projects/abw10-seq33-short/abw10-seq33-short.srt` (58 cues, first at 00:00:00,000, 0 → 45.967 s, 60 fps grid).
`caption_qa.py` PASSES (2 cues ALLOWED by ear, `qa-allow.json`). Next: drag the .srt into ABW10 · Sequence 33 at 00:00,
apply **"affanwizu yellow"**, baseline **y1264**.

**Flagged for the creator:** 7.4 s "wapis gaye" (all three decoders; meaning unclear in context); 44.5 s "fucking rehearsals"
(as said; not a censor-rule word, so not bleeped in the caption).

## The job
- 1080×1920 60 fps, 45.967 s. V1/A1: 24 clips of `X:\Recordings\PBU\C1367.MP4` at 1.1x / 0.8x; nothing above V1.
  Language hi 0.71 / ur 0.27 → `--lang ur`. Chin y1149 → baseline **y1264**. Speech runs the whole cut.
- Content: kids made to stand and chant "good morning teacher, assalam o alaikum" again and again; at university they
  greeted respected teachers while seated; teach kids to greet elders, not "fucking rehearsals".
- **Quotes:** the sung chant (twice), the teacher's imagined "baith jao bhai / ese hi mujy / salam alaikum bol do", the reply
  "walaikum assalam" ×2, and the advice "beta jab koi / bare ate hain / to aap bethe bethe / aap salam kar den".
- Re-decoded (ur + hi + en): the chant is sung ONCE (Whisper's 1.3–1.4 s "teacher"/"assalam" are drawn-out vowels, not merged
  repeats); "aapko kia ghar mai" (WX's "allah" not heard by any other pass); **"bethe bethe"** (his spelling of baithe,
  roman-urdu.md) at 33.4 and 41.6 (the fast one decodes as "pete pete", the second clearly بیٹھے / बैठे).
- **Tool:** a sung chant held 2.1–2.4 s for 3 words, so caption_qa FAILed HANGING with nothing missing. New per-job allow-list
  `qa-allow.json` ({"hanging": [{"t", "reason"}]}): a cue checked by ear prints as ALLOWED with its reason, never silently.

## Better than the last one (CLAUDE.md learning loop § 5)
A chant stays one sung line per phrase (how a class sings it) instead of being chopped to satisfy the gate, and the
exception is written down with its evidence where the gate prints it.
