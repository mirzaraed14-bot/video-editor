# abw10-seq24-short — ABW10 · Sequence 24 (captions only)

▶ **STATUS: DELIVERED 2026-10-25, waiting on the creator's review.**
Deliverable: `projects/abw10-seq24-short/abw10-seq24-short.srt` (68 cues, first at 00:00:00,000, 0 → 52.767 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 24 at 00:00, apply **"affanwizu yellow"**, baseline **y1169**.

**Flagged for the creator (two judgement calls + one unsure word):**
- 12.5 s "koi generic **villain** / origin story ni hai": every decoder hears "viral" (ویرل / विरल / "viral"); written as
  "villain" because the film is a villain origin story.
- 20.2 s "koi film **ni** dekhi to": every decoder hears "film **hi** dekhi"; written "ni" because the next lines
  ("yar mai to samajh ni aye gi… ghanta farq ni parta") only make sense for someone who has NOT seen a DC film.
- 16.3 s "apni aankh mai kainchi / ghusa di" (Whisper: چکینچی گزا دی / चुकेंची उसादी).

## The job
- 1080×1920 60 fps, 52.767 s. V1/A1: 25 clips of `X:\Recordings\PBU\C1401.MP4`, 100 % speed, Scale 110; nothing above V1.
  Language hi 0.91 / ur 0.09 → `--lang ur`. Chin y1054 → baseline **y1169**. Speech runs the whole cut.
- Content: Clayface review (Matt Hagen; not a generic villain origin story; body horror; no DC homework needed; powers
  guessing; ending; Bahria Town cinema gold / platinum lounge, "not sponsored by the way"; pacing; good guy → bad guy).
- Re-decoded (ur + hi + en) 7 windows: the opening ("kal clayface dekh kar aya mai", WX: "dekhta hun"), "do not worry"
  at 17.8 (dropped by WX), "esi hi chale uth ke bhai", "esa ni ke wo foran bad guy" (Urdu in both Urdu-script passes, so
  not the English connector), "but absolute / banger" (absolute held 1.1 s: the gate's 2.05 s for 3 words is emphasis,
  so banger lands on its own line where he hits it).
- Quotes: the viewer's reaction ("oye bhai sahab / itni jaldi / itna sab kuch hogya"), "yar mai to / samajh ni aye gi",
  and the fence-sitters' "jana chahye / ni jana chahye / jana chahye / jana chahye".

## Better than the last one (CLAUDE.md learning loop § 5)
Two places where all three decoders agree but the meaning says otherwise were written for the meaning AND flagged with the
heard form, instead of silently trusting the ASR or silently correcting it.
