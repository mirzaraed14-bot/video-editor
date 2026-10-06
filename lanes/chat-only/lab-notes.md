# Chat-only lane: lab notes

- **2026-10-06: yt-dlp section downloads start the audio after the video (0.05–4.9 s).** The rough-cut tools read audio from
  time 0 of the stream while `splice.sh` trims on container time, so every cut landed early by the offset. Workaround (and
  rule): normalise at intake with `aresample=async=1:first_pts=0` (details: `.claude/skills/rough-cut/SKILL.md` § Gotchas).
  Found on batch 1 of the Onyx samples (`projects/mindsetmentor-23k-call`, 52 ms; `pomp-blockfi-ftx`, 4.86 s).

## 2026-10-06 — finalize.sh promotes a `--preview` render
`./finalize.sh <job>` picks the NEWEST render in `outputs/`, and the Onyx kits (`ig_build.py`/`yt_build.py --preview`) write the 720p
`*.preview.mp4` a moment after the full file, so the dry run said `PROMOTE <job>.sample-ig.v6.preview.mp4 -> <job>.final.mp4` and would have
DELETED the full-quality v6. Workaround until fixed: promote by hand (`cp outputs/<job>.sample-ig.vN.mp4 outputs/<job>.final.mp4`, then the
Downloads copy) and skip `--apply`. Fix to make: exclude `*.preview.mp4` from the promote candidates.

## 2026-10-06 — on Windows, Python's `/tmp` is NOT Git Bash's `/tmp`
A native-Windows Python resolves `/tmp/video-editor/<job>/cuts.json` against the CURRENT DRIVE (`X:\tmp\...`), while `splice.sh`
(Git Bash) reads `C:\Users\<you>\AppData\Local\Temp\video-editor\...`. A re-cut written from Python silently left splice
replaying the stale EDL. Workaround: write the EDL from bash, or resolve the path with `cygpath -w /tmp/video-editor/<job>` first.
(A stray `X:\tmp\video-editor\rationalmale-hacked\cuts.json` from this mistake is safe to delete.)
