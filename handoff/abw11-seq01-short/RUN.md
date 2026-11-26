# RUN: abw11-seq01-short (GTA 6 wishlist Short, English captions only, ABW11 › Sequence 01)

## ▶ STATUS: resume here
**2026-11-26 ~08:30 PKT: DONE.** His words: "caps" (image of the Sequence 01 tab), then "both are ABW 11" (Sequence 01 and 25).
- `outputs/seq01-captions.srt`: 47 cues, 0 → 50.417 s, max 4 words (his last cap, Seq 19/21), natural case, no punctuation except ? and !.
- Imported onto ABW11 › Sequence 01 as a caption track ("Sequence 01 | import true | createCaptionTrack true"). Not seen on screen (his view was on Sequence 25; never switch his view). The same import showed correctly on Sequence 25.
- The A1 track was re-read unchanged right before import (13 clips of `X:\Recordings\Afterhours\C1508.MP4`, the last at 0.8x).
- Project NOT saved: his Ctrl+S. Default caption style (sits low); his Track Style if he wants it.
- **Flagged:** 11.5 s "GTA **Vice** City Easter egg" (large-v3 heard "gta y city"; Tommy follows, so Vice City). "play as Tommy but he's going to be as Jason" is captioned as heard.

## How it ran
- `sequence_reference.py "Sequence 01"` → Gate A OK (50.417 s). Transcribe: the CUDA float16 load fell to the CPU floor and hit `mkl_malloc` (7 GB RAM free with Premiere open), so it re-ran GPU-only: `WHISPERX_NO_CPU=1 WHISPERX_COMPUTE=int8_float16 WHISPERX_BATCH=8`, under the ASR lock (abort if busy) and `lock.sh gpu`.
