# @affanwizu: per-reel procedure

## 0. FULL EDIT from a raw take (the creator hands over a sequence with ONE uncut take)
First run 2026-09-19 (ABW6 · Sequence 18 → `projects/dowry-beggars`). The fast path, in order:
1. Read the sequence (V1/A1 clips, source paths, Motion). Clone it as `<name> RAW (backup)` first.
   Hardlink the raw into `projects/<job>/raw/` (same drive = instant; `ln`, never move).
2. `WHISPERX_DEVICE=cpu transcribe.sh <job> --lang ur` whenever the GPU is busy (nvidia-smi > ~5 GB used).
   ~4 min for a 2.5 min take. In parallel: an `en` faster-whisper pass for meaning (it TRANSLATES, it does
   not romanize; still enough to read the retakes).
3. Author `cuts.json`: last take of every repeated line, the graft on mid-line restarts, end chatter dies.
   `RENDER=0 splice.sh` → `PYTHONUTF8=1 POLISH_TAIL_MS=20 POLISH_LEAD_MS=15 polish-boundaries.py` (the creator's tight
   edges) → `RENDER=0 splice.sh` → `dead-air-qa.py`. Open the hook on its strongest word (drop a leading "agar/aur").
4. Fresh-eyes: script-flow + mechanical (slice re-ASR) subagents, Sonnet, in the background.
   Urdu note for the flow reviewer: a trailing "agar …" clause belongs to the sentence BEFORE it (not dangling).
5. Replay into the creator's sequence: picture from the MP4 on V1, sound from the creator's extracted WAV
   on A1 (sample-identical to the MP4 audio, checked), then build the rest of the stack from [`reel-recipe.md`](reel-recipe.md):
   Scale 125 / Position x ≈ face + 50 px right, Black Video on V2 (36 %, end fade), Adjustment Layer crop 17/16 on V3,
   3 punch-ins (155–170) on the insult / one-word payoff / closing punchline. Propose a title and ask for the song.
6. Captions: `python presets/instagram/affanwizu/cut_reference.py projects/<job> --scale 125 --x <x>`
   → `projects/<job>/captions/` is a normal caption job (steps 3–5 below), then
   `build.py <job>/captions --style yellow --srt --dur <sequence end>` → an EDITABLE caption track (.srt):
   the creator drags it onto the sequence at 00:00 and applies the "affanwizu yellow" Track Style. No render.

## Captions only (the creator hands over a finished cut)

The creator hands over a **finished cut**. We return the same cut with captions, and touch nothing else.

## 1. Intake
- Job name = the reel's topic, kebab-case (`never-insult-the-little-ones`), never the file name.
- **Copy** the cut into `projects/<job>/raw/` (never move it). It must be the ONLY video in `raw/`,
  exported **without** captions, 9:16 (1080×1920; a 4K export renders the same look at 2×).
- Confirm the language: these reels are Urdu, but the shoot folders also hold English GTA takes.
  If in doubt, listen to a few seconds, or let Whisper detect it (Urdu often reads as `hi` or `ur`).

## 2. Transcribe (once)
```bash
.claude/skills/rough-cut/scripts/transcribe.sh projects/<job> --lang ur
```
→ `transcript/words.json`: Urdu-script words with frame-accurate timings (10 s chunks; the 30 s
default dropped 10 s of speech on balcony).
With After Effects / Premiere open the GPU is full and this crawls: prefix `WHISPERX_DEVICE=cpu` (~90 s for a 40 s reel).

**The cut lives in Premiere (the usual case):** read the sequence through the bridge
(`get_sequence_structure`, plus the V1 clips' Motion), rebuild it with ffmpeg from the edit points and
the same framing into `raw/`, and transcribe that. Gaps in the sequence stay gaps.

**GATE A — the rebuild must equal the sequence end.** `sum(clip durations)` is NOT the sequence
length: a concat of the clips silently closes every gap, and then every caption after the first gap
is early by the gap. Compare `ffprobe` duration against the sequence end BEFORE transcribing; if it
is short, insert `color=black` + `anullsrc` for each gap (seq17: one 3.27 s gap at 175.4 s, rebuild
181.65 → 184.93 s, sequence 184.92). A frame of rounding is fine; a tenth is not.

**GATE B — prove every silence is silent.** WhisperX drops speech in long Urdu takes without any
warning, and a dropped span looks exactly like a pause in `words.json`. For EVERY speech gap > 1.5 s:
```bash
ffmpeg -hide_banner -nostats -ss <t> -t <len> -i <cut> -map 0:a -af volumedetect -f null NUL 2>&1 | grep mean_volume
```
Real silence reads ≈ −55 dB. Anything near the take's speech level (≈ −26 dB) is **dropped speech** —
re-decode that span (faster-whisper, `language="ur"`, `vad_filter=False`, `word_timestamps=True`) and
splice the words back in. Seq17 hid 11 s of dialogue in two such gaps, including the reel's core stat.
Re-decode a WIDE, well-bounded span: short windows hallucinate (a 3.4 s slice invented a sentence that
a 16.5 s slice around it disproved).

## 3. Draft the phrasing
```bash
uv run presets/instagram/affanwizu/build.py projects/<job> --prep
```
→ `captions.draft.txt`: the Urdu words grouped by pauses, each line keyed by the `<word#>` it starts on.
This draft is only a timing scaffold. The phrasing in it is mechanical.

## 4. Write `captions.txt` (Claude)
Rewrite the draft as Roman Urdu, one caption per line, in the creator's spelling ([`roman-urdu.md`](roman-urdu.md)):
```
0   | mere physics ke teacher ne mujy
6   | aik baar kaha tha puri class ke saamne
14  | ke mai waiter banunga
@12.60 | aik larki ne na          # '@seconds' when Whisper missed the word the line starts on
```
- **Phrasing** = the creator's: a natural spoken phrase, usually 3–5 words, never over ~38 characters
  (one line, never wrapped). A word said alone between pauses gets its own line (`to`, `jo`).
- A line switches on the **start of its first word** and holds until the next line. There is never a
  gap, and the first line shows from frame 0.
- Fix Whisper's mishears from context (teacher, bezti, balcony, mentally…). **Show the creator every
  word you were unsure of.** Don't guess silently.
- **Unclear stretch = re-decode just that snippet with `language="en"`** (faster-whisper in the whisperx
  venv): the Urdu pass drops code-switched English ("opinions achay lage", "aurton ke baare mai").
- Style: `--style white` (commentary/rant reels) or yellow (aesthetic deep talks). Say which in the hand-off.
- Repeated line across takes → caption what's in the cut. (The cut is theirs, so retakes are already gone.)

## 5. Review sheet → creator
Send the lines with their timings (`build.py` prints the sheet) before rendering anything long.
Spelling fixes go back into `captions.txt`, and any NEW rule goes into `roman-urdu.md` + `LESSONS.md`.

## 6. Render
```bash
uv run presets/instagram/affanwizu/build.py projects/<job>            # burned → outputs/<job>.captioned.mp4
uv run presets/instagram/affanwizu/build.py projects/<job> --alpha    # transparent layer → hf-graphics/captions/renders/captions-alpha.mov
```
Burn = a finished file to post. Alpha = a ProRes 4444 layer the creator drops over their own timeline.
`--title "…"` adds the top title in the same style (off by default: the title is theirs).
`--until 10` = quick preview.

**Into Premiere:** import the alpha layer into a "Claude captions" bin and `overwriteClip` it at 0 on
the TOP EMPTY video track of the creator's sequence (never a track with clips on it), then read it back.
Don't save their project for them.

## 7. Hand-off
Copy the deliverable to `~/Downloads/`. Then log what the creator changed in [`LESSONS.md`](LESSONS.md).
