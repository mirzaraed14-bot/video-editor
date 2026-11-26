# RUN: twohottakes-weird-party (Onyx sample, Two Hot Takes / Morgan Absher)

## ▶ BUILDER STATUS (Sonnet, 08:30): picture build running
- Raw fixed by main (07:30): cut re-run on the fixed raw (work/cut/run_cut.sh + retime.py), 16 pieces, 67.97 s + 8-frame dip = 68.23 s (planned 63.5 s: SEQUENCE counted word times, the measured speech edges and kept pauses add ~4.5 s).
- 4K base (work/raw-hq/tht-s5-hq.mkv) spliced frame-locked: yt/prep_hq.py -> yt/work/base_hq_ext.mp4 (MSE vs the 1080p cut 2.2 on 480x270).
- Shots follow DIRECTION § 0b (s04 SPLIT, s08 A Ashby, s10 A Morgan + her label, s10b SPLIT, s11 from "to check for murderers"). 13 drawn scenes done (yt/scenes.py), cue sounds made (yt/sfx_make.py), spec = yt/build_spec.py.
- Next: picture v1 -> grade tests per camera -> grade/sharpen -> overlay + mix -> QA -> finals. Rebuild: bash yt/run_all.sh <v> [picture|grade|overlay].

## ▶ STATUS 2026-11-26 ~07:10 PKT: APPROVED ("Yes, YouTube look" = Option A ~63.5 s). BUILD RUNNING (Sonnet builder, background, started ~07:10).
- Main wrote BRIEF § Catalog pass, `DIRECTION.md` (shot by shot) and `BUILDER-BRIEF.md`. Builder executes; main does Opus QC on the exported final.
- Main is probing YouTube for a sharper episode stream (the 1080p avc1 is ~1.2 Mbps); marker `work/raw-hq/STATUS.txt` (PENDING / READY / NONE).
- Defaults taken without asking (flag in the delivery note): caption reads SEX (not S*X); no music bed (his song later).
- Transcript hole 467-489 s is after the cut's last word (465.46): no re-ASR needed for Option A.
- Earlier: WAITING FOR AFFAN'S OK on SEQUENCE.md v3 (resolved 2026-11-26 ~06:50).
- Next after his OK: his look pick (YouTube recommended) -> the build in a fresh Sonnet builder (catalog pass in BRIEF first) -> Opus QC -> finals to X:\Claude Projects\Exports\ -> REACTIONS-LEAN prep (re-pull their Short at 1080p) -> JOBS.md cost log.
- 04:30-04:50: every ASR try failed (large-v3 GPU fp16 and int8, then medium.en CPU): Windows commit was exhausted (1 GB free of 91 GB) by other sessions' ASR jobs run OUTSIDE the GPU lock (`chunks/c2|c3/work/row_asr_retry.py` x3 at ~7.3 GB each, `research/aw-hp-2026-11-26/asr.py`) plus Premiere 8.3 GB and Photoshop 5.6 GB. The CUDA 'out of memory' was host commit, not VRAM (2.2 GB of 8 used). The waiter starts large-v3 (GPU lock) when >= 8 GB is free and no other ASR runs, or >= 14 GB free.
- Gate (Affan): research incl. Instagram -> the sequence in text -> his OK -> only then the build. Nothing is built.
- Session: one fresh session for this prospect (launched 2026-11-26 ~02:20 PKT). Builders = Sonnet; Opus picks the moment and does QC; no Fable agents.
- Locks: `projects/_onyx-batch2-2026-10/pace.sh youtube|instagram`, `lock.sh gpu` for every ASR job; never two large-v3 at once.
- Never send email (the main Onyx email session sends the sample). Never touch Barbell Logic. Work in silence.
- Condition from the host: tag @TwoHotTakes on every platform it is posted on.

| Step | State | Output |
|---|---|---|
| Platform pick (PLAYBOOK § 0) | measured | YouTube Shorts 14/30 d, median 30,070 (2.9 %). Instagram @twohottakes 483K, 14/30 d, median ~687K (142 %). This story: YT 52K vs IG 1.9M. BRIEF § Platform pick. |
| Pull sources | DONE 04:35 | reference/zB7i3tNVjHQ.mp4 + qDwRNaquIB0.mp4 (480p: my height<=1080 filter caught the vertical Shorts; re-pull 1080p for the reaction), work/raw-orig/gDA2zhH5fhA_s5.mp4 (1080p 29.97, 12:10) -> raw/tht-s5.mkv |
| Transcripts | DONE 05:25 | canonical large-v3 `transcript/words.json` (section; HOLE 467-489 s, re-ASR that slice at build); Shorts large-v3 `work/tx-ref/transcript/words.json`; draft small.en `work/tx-s5/DRAFT-small.txt` |
| Sequence (text) | v3 DONE ~06:10 | `SEQUENCE.md`: Option A ~63.5 s, B ~92 s; YouTube look recommended; camera map; edge check; teardown; cold read (27 items fixed) + re-read; Fable advisor x2 |
| Affan's OK | DONE ~06:50 | "Yes, YouTube look" (Option A). SEX vs S*X unanswered: default SEX |
| Build | RUNNING ~07:10 | Sonnet builder per BUILDER-BRIEF.md + DIRECTION.md |
| Opus QC / export | waiting on the build | |
