# RUN — nick-martin-same-night ("SAME NIGHT", Nick Walker vs Martin Fitzwater, Abundance Wisdom long-form #2)

## ▶ STATUS: PRE-PRODUCTION (2026-10-07) — resume here
Not recorded yet. The plan, constraints and premium treatment live in `BRIEF.md`.
**Sources, 2026-10-07: ALL 12 IN** (`broll/`, every one H.264). The first pass was blocked (HTTP 429 + "not a
bot"). A plain retry ~10 min later went through (no cookies, no client switching); 11 needed one more retry (a 403
on the video data). Fallback the creator offered if it blocks again: their Chrome (Claude in Chrome) + IDM. 05 is
720p (2020) and B2 is 1280x702; the rest are 1080p. 04 = the finals, hardlinked from long-form #1.
`broll/fetch.sh` is re-runnable and skips what's already there.
**Transcripts: DONE.** `transcribe-windows.py` (copied from LF1) → `transcript/windows/<id>.json`, 11 windows
(`transcript/windows.json`) covering every scripted clip. Every quote found near its script time; **four script
out-points cut the quote short (1c, 1d/5h, 4a, 5f)**, word-accurate outs in `transcript/clip-notes.md`.
**Lock condition 2 (Arnold, 3c), first look:** in the rip, 10:25–10:39 is the presenters (Ronnie + the medal
presenter); the cut to the line-up at ~10:39.5–10:45 shows Nick (glasses), Hadi (beard, medal), the man in the gold
trunks and the man in the red trunks, but **no bald, light-skinned man = Martin** (taken to be the man with the
4th-place medal at 9:26, 9:50 and 11:20, matching B3). 10:46–11:23 = Nick's medal, then Andrew Jacked's win
celebration. 9:15–9:55 = Hadi's 3rd-place medal (Martin beside him ~9:25). **Result: Martin's cheer is NOT on camera in
this rip.** WhisperX heard nothing after 10:13 (crowd/music), so the exact time of "runner-up, Nick Walker" isn't
measured. The creator's Short (Sequence 30, `martin-fitzwater-12th`) DOES show Martin waving/cheering, but in close-ups
that are not in this rip (a different camera, a blurred band on top: likely a social re-upload). **Ask the creator for
that clip's original source** (title/link/date for the evidence tag) and confirm it's the moment after Nick's name.
Sheets: `review/lock2-*`, `review/arnold-*`, `review/short-seq30-shots.jpg`.
**Lock 1 (2020 posedown):** NOT decided. Nick = the young man in the red trunks (e.g. 3:06–3:26,
`review/lock1-na2020-186-206.jpg`); I can't tell which of the others is the 23-year-old Martin. The creator to confirm
by eye, else the fallback (B3 + the card). B1 (the full prejudging replay, kRjLT-6qCkw) was NOT
fetched; B2 covers the same shot. Fetch B1 only if B2 fails.
**Next:** sources → lock conditions 1–2 by eye → stills S1–S6 → the kit (BRIEF § 3) → the recording.

| | |
|---|---|
| channel | Abundance Wisdom, face-led long-form (the template is `projects/nick-walker-never-mr-olympia/`) |
| format | long-form 16:9, about 11:00 |
| script | 🔒 FINAL 6 Oct 2026, `X:\Claude Projects\Abundance Wisdom\NICK-MARTIN-LONGFORM.md` |
| sources | `X:\Claude Projects\Abundance Wisdom\NICK-MARTIN-LONGFORM-SOURCES.md` → `broll/` |
