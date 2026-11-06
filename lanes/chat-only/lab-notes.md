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

## 2026-10-28 · YT Shorts kit: head tracking lags a fast head at jump cuts (CA-009 Short)
- **Symptom:** `head_track` (track_eye, sigma 12, linear edge blend) left the eyes 100-140 px off at three in-shot joints of a
  fast-moving speaker (short takes, a hand gesture). An offline replay at sigma 3 still gave 132 px.
- **Workaround:** `head_track: false` (the chained eye lock) plus the new opt-in spec key `head_chain_n: 2` (default 4) in
  kit/yt_picture.py `eye_track`.
- **Gate:** step the eye midpoint across each in-A joint on the delivered frames. Script:
  `projects/iphone-duo-clip-angle/clips/reupload-wont-go-viral/work/head_snap_gate.py`.

## 2026-11-06 · YT Shorts kit, Afterhours mic (`projects/gta6-head-start`)
- **WhisperX collapses restarts on this mic, and an RMS read does not show them.** The first sequencing said "one clean pass"; four lines had
  restarts and the lengths were 3 s out. Workaround: per-burst faster-whisper (`work/cut/bursts.json`), force-aligned burst by burst
  (`work/cut/align_bursts.py`), `FW_DEVICE=cpu` while the GPU lock is held. Rule: no takes or lengths quoted before the burst pass.
- **A doubled word in a verbatim read can be a Whisper window seam.** "obviously obviously" read once on a re-read of the slice, both passes;
  "don't - don't" appeared only with the filler prompt. Test: a stumble counts only if it reads the same with and without that prompt.
- **`workflows/grade-picture.py` only knows whole shots.** A SPLIT is graded whole, so its drawn bottom panel shifts (channel pink 235,39,152 ->
  253,58,185) while every other card is excluded, and every non-A shot gets the DOC look, so a split's face does too. Workaround: set
  `grade_look` for DOC as well as A; `work/hook_panel.py` puts the panel back from `picture.whip.ungraded.mp4` after sharpen and keeps sharpen's
  fingerprint. Fix to make: a per-region exclusion in the grade.
- **POP defaults crush a low-key room** (mic and shirt to black, face dark orange). Set `grade_look` per job and test on stills before a full
  render; the approved numbers are in the channel's `LESSONS.md` 2026-11-06.
- **In a worktree session the Write/Edit hook blocked the main checkout even after a folder grant.** Writing from the shell needs his OK, and
  the OK covers only the paths he named.
