# @affanwizu: the full reel recipe (what a finished reel IS)

Read off the creator's own finished reel on 2026-09-19: ABW6 · Sequence 18 → `Final Renders/ameer.mov`
(job `projects/dowry-beggars`). Every value below was measured on their timeline or their export.
The goal: raw take in, this finished reel out, with nothing touched by hand.
Procedure: [`PLAYBOOK.md`](PLAYBOOK.md) § 0. Caption look: [`deep-talks-style.md`](deep-talks-style.md).

## The timeline stack (1080×1920, 60 fps)

| Track | What | Values |
|---|---|---|
| V1 | the cut, from the raw MP4 | Motion **Scale 125**, **Position x ≈ 0.578** (face ~50 px RIGHT of centre: x≈591 on ameer), y 0.5 |
| V2 | **Black Video**, full length | Opacity 36 %, keyframed to **100 % over the last ~1 s** (23.45 → 24.40 s): the fade to black |
| V3 | **Adjustment Layer** (no effects) | Motion **Crop Top 17 %, Crop Bottom 16 %** → the letterbox: footage visible y326 → y1613, black bands above and below |
| V4 | captions | Essential Graphics text, one clip per line (the creator converted the .srt track to graphics) |
| V5 | title, full length | Ubuntu Light 48, gold, upright, in the top band (see Title) |
| A1 | voice, the creator's extracted WAV | clip gain 0 dB; the mix lands the voice ~+2.7 dB over the raw |
| A2 | music bed, full length | see Music |

`Black Video` and `Adjustment Layer` already exist as project items in ABW6, so they are laid with
`overwriteClip`. No import is needed (scripted import is broken on this machine, see `lanes/premiere/lab-notes.md`).

## The cut
- **Tight edges.** Against Claude's first cut the creator took a median **169 ms off every tail** and 69 ms off heads.
  Edges end 0–35 ms after the sound. → `POLISH_TAIL_MS=20 POLISH_LEAD_MS=15` on `polish-boundaries.py`.
- **Open on the strongest words**: the leading connective of the hook went ("agar aap jahez…" → "aap jahez…"),
  and so did a drawn-out "aur" at the head of a graft.
- Take choices all stood: last take of every repeated line, including dropping a joke that only existed in take 1.
- Length: 2:28 raw → 24.4 s.

## Punch-ins (hard-cut zooms on the beats)
Three per ~25 s reel, each a separate V1 clip (split at a phrase boundary when needed), same framing, bigger scale:

| Beat | Scale | Why |
|---|---|---|
| the line that names the target: "bhikari kehte hain / aap jaise logon ko" | **157** | the insult |
| a one-word payoff: the isolated "ho" closing "accept kese kar sakte ho" (0.45 s) | **170** (Position x 0.629) | the rhetorical sting |
| the closing punchline, split off its clip: "wo itne ameer wameer bhi ni hote" | **155** | the last laugh |

## Captions
- Ubuntu **Light 48**, gold #FFD700, **upright** on this reel (faux italic OFF: balcony had it ON; the latest reel wins),
  soft black shadow, centred, baseline ≈ chin + 115 px (y≈1103 on ameer; the creator did not move it).
- Timing as built (switch on the first word) was kept to the frame. One change: **no caption over the
  one-word "ho" punch-in**. The line before ends at that cut.
- Text: 21 of 23 lines shipped as written. Fixes: "aap jaise logon **ko**" (Whisper dropped the particle) and
  "bhai isse **kaam** karo apna" (Whisper: "haan").

## Title
- A **quote of the people the reel mocks**, in curly quotes, Sentence case: `“Aap apni khushi se deden”`.
- Ubuntu Light 48, gold, upright, centred in the top black band (baseline ≈ 25 px above the window top).
- The title is the creator's creative call. Propose one (a line the target would say), never ship one unasked.

## Music
- A recognisable Pakistani song's **instrumental/karaoke** (ameer: "Afsanay" by Young Stunners, instrumental),
  starting ~0.2 s into the track, under the WHOLE reel, ending with the picture.
- Level: the bed sits **~6.6 dB under the voice** (RMS, measured by subtracting the voice from the export). Clip gain
  0 dB, with a **−6 dB step from ~16.4 → 18.8 s** held to the end. No audio fade.
- The creator picks the song. Placement and level can be automatic once the song is named.

## Export
H.264 1080×1920 60 fps in a `.mov` with PCM audio, in/out = the cut (24.417 s), **−16.7 LUFS integrated**,
to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\<one word>.mov` (named after the key word: `ameer`).
