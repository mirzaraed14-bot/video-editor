# abw10-seq40-short — ABW10 · Sequence 40 (captions only)

▶ **STATUS: DELIVERED 2026-11-03, waiting on the creator's review.**
Deliverable: `projects/abw10-seq40-short/abw10-seq40-short.srt` (72 cues, first at 00:00:00,000, 0 → 66.983 s, 60 fps grid).
`caption_qa.py` PASSES; warnings resolved: LONG WORD 0.31 (hid "wo reel dekhi hui hogi na", captioned), CONNECTOR 28.30
(the English listener itself wrote یقین: "aap yaqeen manen" stays Urdu), CONNECTOR 55.08 ("aisa", all decoders), ENGLISH 62.56
("of" = a stumble before "inspired"), ENGLISH 66.00 ("extent" vs en + hi "accent": "apna accent sahi bethana").
Next: drag the .srt into ABW10 · Sequence 40 at 00:00, apply **"affanwizu yellow"**, baseline **y1175**.

**Flagged for the creator:**
- 10.82 s **"f*cking hell bhai"** (en decoder "F**king hell, bro"): censored with *; retype if this reel keeps it plain.
- 16.39 s "kai dafa log" (decoders: tez dafa / titha pana / thi taba); 40.34 s "aisi wali kar ke" (WhisperX ایشیوی);
  29.88 s "kaam kia hai" (en "worked"); 0.00 s "bhai" (English listener; hi "wo").
- 22.46 s "itna gay lagta hai" captioned as said.

## The job
- 1080×1920 60 fps, 66.983 s. V1/A1: 24 clips of `X:\Recordings\PBU\C1438.MP4` at 1x; nothing above V1. `--lang ur`, CPU.
  Chin y1060 → baseline **y1175**. Speech runs the whole cut. The first WhisperX run left no words.json (it ran alongside the
  Seq 39 job); re-run alone, it wrote it.
- Content: the reel about Pakistani call centers faking English accents ("faltu tareen accent", “this is james” / “calling from
  the”), made-up names (affan → arthur); he has only worked with US clients his whole career, never changed his name, 4500 loom
  videos speaking English → an accent you can't tell; "in logon se inspired ni hona bhai… apna accent sahi bethana".
- Re-decoded ur + hi + en in 10 s windows (`work/redecode.txt`).
