# RUN — destiny-unvaulted (captions only)

▶ **STATUS: captions delivered as an editable caption track + .srt. Creator takes it from here.**

| | |
|---|---|
| Not an Abundance Wisdom video | a Destiny / Bungie reaction, but built to the Abundance Wisdom caption rules |
| Creator's project | Premiere `ABW6.prproj` → **Sequence 23** (49.65 s) |
| Picture | `E:\Skool Recordings\5 Sept Batch\C1297.MP4`, 19 cuts |
| Audio | screen recording `2026-09-22 08-38-26.mp4` + its extracted WAV, 20 clips |
| Scope | captions only |

## What was done

1. Rebuilt the sequence audio from the 20 A1 clips (`raw/seq23.mp4`, 49.649 s vs the timeline's 49.650).
2. WhisperX once (`WHISPERX_DEVICE=cpu`) → `transcript/words.json`, **155 words, 187 wpm**, single speaker.
3. `captions.txt` written by hand to the channel rules: 3 words per caption, 4 on the fast lines,
   no commas or full stops, `?` and `!` kept.
4. `make_plan.py` → `captions-plan.json` — **55 captions**, every word checked against the transcript.
5. `make_srt.py` → `outputs/seq23-captions.srt` + `caption-colours.md`.
6. Imported and **created a caption track on Sequence 23**. Project left **unsaved**.

## Colour choices (the channel's meanings, applied to gaming copy)

- **yellow (payoff / energy):** BACK!, UNVAULTED, CREDIT, COPIUM, 100%, CLASSIC, DESTINY 3
- **blue (names / key nouns):** BUNGIE, RAIDS, DESTINY, ASTACROSS, STATE OF PLAY, PLAYSTATION, CAPTAIN AMERICA
- **red (the grievance):** VAULTED, DISAPPOINTED
- **pink (warmth):** THANK YOU
- **italic:** the quoted Bungie statement (9.74 → 16.20 s) — another party's words read aloud

## Flagged for the creator

- **32.29 "PEOPLE RATED THE"** — ASR heard "rated"; in context this is probably **"raided"**. Left as heard.
- **44.26 "BRING BACK RIGHT"** — the line is garbled in the ASR; likely a product name. Needs a listen.
- **16.20 "NEW"** — a false start ("New… Now credit where credit is due"). Caption it or cut it.
- One caption wraps to two lines: **"DISAPPOINTED / DESTINY COMMUNITY"** (39.96–41.66).
