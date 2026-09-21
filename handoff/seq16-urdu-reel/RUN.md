# RUN: ABW6 · Sequence 16 (Andrew Tate opinions reel), captions only

## ▶ STATUS: resume here (2026-09-18, after the creator's review)
Creator asked for the YELLOW deep-talks style + an English fix (8.6 s "especially around women etc").
Done: `captions-alpha-yellow-v2.mov` is on V3 (the creator dragged it in; scripted import broke, see
lanes/premiere/lab-notes.md). Its clip ended at 35.72 s on the drop, so the last line (39.2–40.9) needs the clip
extended to 40.917. The five spelling flags below were accepted as they are ("the captions themselves are fine").

## (earlier) status 2026-09-18 13:40
First caption test for @affanwizu. **Captions are placed on V3 of Sequence 16 in ABW6.prproj**
(`captions-alpha.mov`, 0 → 40.917 s, read back), in bin "Claude captions". The project is NOT saved
by us (the creator saves). **Waiting on the creator's spelling review** (the flags below).

- Preset: `presets/instagram/affanwizu/` · style **white** (`white-style.md`), baseline **y1140**
  (chin median 1026 + 115). Chosen because it's a commentary/opinion reel framed like oushi/SAFAI;
  the yellow style is one flag away (`--style yellow`).
- Cut: the creator's, untouched. 17 clips of `E:\Skool Recordings\5 Sept Batch\PBU\C1246.MP4` on V1,
  Motion scale 125 / x 566. **Gap 35.717 → 39.200 s** (no clip): no caption over it.
- `raw/seq16-reference.mp4` = the cut rebuilt by ffmpeg from the 17 edit points with the same framing,
  used for transcription + the preview only (the deliverable lives in Premiere).
- Transcript: `transcript/words.json` (Urdu, WhisperX large-v3, **CPU**: the GPU was full with AE/Premiere/Topaz).
- Lines: `captions.txt` (36 lines). Preview: `outputs/seq16-preview.captioned.mp4`.

## Flags for the creator (unsure words)
1. 13.2 s "nahi bhai tumhe / **iske opinions achay lage?**": heard as "opinions chilak"
2. 12.1 s "dimagh se guzar ni **paati**" (Whisper: paata)
3. 14.6 s "tum to phir misogynist **hai** bhai" (hai vs ho)
4. 30.4 s "wo **files** wala scene hai" (Whisper: "filed")
5. 40.4 s the last two words after "agree karta" are unclear, so they're left uncaptioned (the line holds)

## Re-render after fixes
```bash
uv run presets/instagram/affanwizu/build.py projects/seq16-urdu-reel --style white --y 1140 --alpha
```
Premiere picks the new file up in place (same path); if not, right-click the clip → Refresh Media / Replace.
