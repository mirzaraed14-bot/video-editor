# abw10-seq22-short — ABW10 · Sequence 22 (captions only)

▶ **STATUS: DELIVERED 2026-10-23, waiting on the creator's review.**
Deliverable: `projects/abw10-seq22-short/abw10-seq22-short.srt` (94 cues, first at 00:00:00,000, 0 → 88.783 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 22 at 00:00, apply **"affanwizu yellow"**, baseline **y1228**.

**Flagged for the creator:** 8.2 s "NFT 2025 champion" (every decoder hears NFT; his Instagram says "1x National MMA Champion");
10.8 s "personally aage mujy / train kar rha hai / bohat dafa"; 54 s "or jo mene / comments mai logon ko tag / kar rhe hain"
(as said).

## The job
- 1080×1920 60 fps. V1/A1: 48 clips of `X:\Recordings\PBU\C1392.MP4`, 100 % speed, Scale 100 / 129. Voice and cut end at
  88.783 s; the Graphic (V4) and the adjustment layer run on to 98.62 s, so the captions end at 88.783 (last line holds).
  V2: a WhatsApp clip (10.85–12.95, its audio not on the timeline); V5/V6: 13 screenshots.
  Language hi 0.61 / ur 0.38 → `--lang ur`. Chin y1113 → baseline **y1228**. Speech runs the whole cut.
- Content: fundraiser for Shams Khan (Pakistan's no. 1 bantamweight), gold at the Pakistan Open MMA Championship in Lahore →
  qualified for the IMMAF World Championships in Georgia from 1st November; goal 7 lac on gohelpme.pk; "agar ham aik
  pakistani ko UFC mai dekh sakte hain" said twice (both kept, he left both in the cut).
- **Names from his own screenshots** (V5), not guessed: arslan ash (photo at 0–5 s; Whisper: ارشلین ایش / "Arsalan Ash"),
  shams khan, open MMA championship, IMMAF (the English listener heard "IMMF"), georgia, gohelpme.pk, 7 lac, UFC / ONE FC /
  bellator.
- **Transcript repair:** WhisperX heard only "موسیقی" over 5.2–14.8 s (DROP); the hi + en re-decode of 10 windows restored
  it and the English ("what if", "doesn't matter", "rather", "to cover the visas", "as of recording this", "before you
  contribute"), plus "ke **baat** government level tak pohnche" (WX: بعد).
- "registration / tickets / nutrition" are one line each: a slow spoken list (all three decoders put a pause after each
  word); on one line the gate read 2.3 s for 3 words as missing words.
- caption_qa warns "script" twice: the English listener echoing its own prompt sentence ("video script nahi ki") mid-segment,
  which `echoes_prompt()` misses (also on Seq 20). Warning only.

## Better than the last one (CLAUDE.md learning loop § 5)
Every proper noun was checked against the creator's own on-screen screenshots before writing, so names, the event and the
fundraiser address match what the viewer sees on the same frame.
