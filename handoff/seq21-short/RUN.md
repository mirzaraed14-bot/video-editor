# RUN — seq21-short (ABW8 · Sequence 21, GTA short: the Game Awards juror vs GTA 6) — captions only

▶ **STATUS (2026-10-01): CAPTION TRACK ON ABW8 · Sequence 21 (import + createCaptionTrack both true; the .srt is in the
project). NOT yet checked on screen: the creator was working in Sequence 22, so the check was left for later.**
36 captions, **max 3 words** (the GTA-short rule from Seq 06; the creator gave no number this time), natural case,
no punctuation except ? and !, default Premiere caption look. `outputs/seq21-captions.srt`. Project NOT saved by us.

| | |
|---|---|
| Project | Premiere `ABW8.prproj` → **Sequence 21** (1080×1920, 60 fps, **36.267 s** after the creator's 0.15 s trim at 22.70) |
| Picture | `X:\Recordings\Afterhours\C1319.MP4` on V1; screenshots on V2 (0–4.93, 16.33–18.65) |
| Voice | `E:\…\Final Renders\Batch Batch\2026-10-01 17-12-13.mp4` on A1, 17 clips (the creator's jump cuts) |
| Language | **English** (p 0.99). NOT an @affanwizu Urdu reel despite the separate-voice pattern: checked before transcribing. |

## How it was built
1. `sequence-captions.py read` (twice: the creator trimmed 0.15 s mid-job; the second read is the one used; the first is
   in `brief/before-creator-cut/`). Gate A: rebuild 36.267 s = sequence end.
2. `transcribe.sh --force` (English). WhisperX was right on timing but wrong on several of the jump-cut fragments, so
   every A1 clip was re-decoded WITH context from the source recording (`transcript/context_decode.json`) and the
   doubtful stretches checked against 20 ms envelope blobs. Fixes in `transcript/words.json` `_fixes`
   (original `words.whisper.json`): the opening "Alanah Pearce, who's been a" (WhisperX: one "Elena"); name =
   **Alanah Pearce**; + "bar", a second "you're", "take", the closing "Red"; "re-voting" → "voting"; "Jeet" → "GTA";
   "read the truth, report, report" → "Red Dead 2 report report"; words cut by the creator end at the cut.
3. `captions.txt` (≤ 3 words) → `srt --max-words 3 --hang 0.8` → `import`.

## Flags for the creator
- The cut's own fragments are captioned as heard: "bar" (bar none cut), "some" (something cut), "take" (the first
  "could" cut), "GTA" (cut inside GTA), "report report", the final "Red". Delete any they don't want.
- The opening 0–3.02 s (screenshots, silence) is uncaptioned; the first caption starts with his voice.
- "I'll accept that" is on screen 0.28 s (his cut ends right after "that").

## Tool changes made on this job
- `workflows/sequence-captions.py srt`: the first caption is no longer pulled to frame 0 when the first clip is a
  silent shot; new opt-in `--hang <s>` ends a caption 0.25 s after its last word when a longer pause follows
  (default unchanged: wall to wall).
