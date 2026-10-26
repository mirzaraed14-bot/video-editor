# abw10-seq26-short — ABW10 · Sequence 26 (captions only)

▶ **STATUS: DELIVERED 2026-10-26, waiting on the creator's review.**
Deliverable: `projects/abw10-seq26-short/abw10-seq26-short.srt` (109 cues, first at 00:00:00,000, 0 → 86.867 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 26 at 00:00, apply **"affanwizu yellow"**, baseline **y1261**.

**Flagged for the creator:**
- 8.9 s "invite tha" (ur/hi hear وائٹ تھا / वाइट था, the en decode "invite"; the English listener heard "right, the").
- 17.3 s "boti boti si speaker" (every decoder: بوٹی/पोटी/"booty"; meaning "flimsy" speakers).
- 79.2 s "pata hai logon / pages bhi hain mere" (every decoder hears لوگوں; maybe a word he clipped).
- 37.4 s "aik or khatoon ayin" (ur: خاتو نہیں ہوں, the English listener: خاتون آئی ہوں).

## The job
- 1080×1920 60 fps, 86.867 s. V1/A1: 41 clips of `X:\Recordings\PBU\C1366.MP4`, 100 % speed and scale; nothing above V1.
  Language ur 0.70 / hi 0.30 → `--lang ur`. Chin y1146 → baseline **y1261**. Speech runs the whole cut.
- Content: an invite-only Karachi speaking event where everyone performed English (announcer, ChatGPT scripts read off the
  podium, "demonistration" / "strejity"), why Urdu is not a lesser language, he left after 1.5 of 10 hours.
- **Quotes:** the mispronunciations he mocks (“demonistration”, “strejity”: only the Urdu-script pass spells the second
  word of each pair differently, which IS the mispronunciation), his inner voice at the event (“yar ye to achi cheezen /
  bata rhi hain yar”) and the viewers' line (“yar inki tarah bano”).
- Re-decoded (ur + hi + en) 8 windows: "invite only type shit" (WX: ٹائم شیٹ), "you know" before "ayre ghayre",
  "abey bhai aap log to pata ni ke", "inse khud parha ni ja rha / bakwas", "tooti phooti angrezi" (WX: ٹوٹی بھی).
- caption_qa `--fix` applied his spellings (hogya, isme ×2).

## Better than the last one (CLAUDE.md learning loop § 5)
A mocked mispronunciation was captured as said, in quotes, by comparing what each language pass spelled for the repeated
word, instead of normalising it to the dictionary word (which would have killed the joke).
