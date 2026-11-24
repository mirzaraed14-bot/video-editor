# RUN: abw11-seq21-short (GTA 6 on PC Short, English captions only, ABW11 › Sequence 21)

## ▶ STATUS: resume here
**2026-11-24 ~05:30 PKT: DONE (v2).** His words: "CAPS" (image of the Sequence 21 tab), then "retime them again i placed some things so its out of sync".
- **v2:** `outputs/seq21-captions-v2.srt`, 42 cues, 0 → 42.900 s, max 4 words (his last cap, Seq 19). Built on the cut as of ~05:25, with screenshot inserts at 4.4-6.05 s and 13.233-15.133 s (no captions over them) and his 0.8x pieces at 11.6 s and 35.18 s. The A1 was re-read unchanged right before import.
- **On Sequence 21 as caption track C2** (Premiere shows only the newest track). Checked on screen: "GTA 6 PC" at 41:50.
- **C1 is the old v1 (38.1 s) track, out of sync: he deletes it.** v1 files are in `v1-38s/`.
- Project NOT saved: his Ctrl+S. Default caption style (sits low); his Track Style if he wants it.
- **Flagged to him:** 24.6 s "have **Claude** by their side". large-v3 heard "clawed", medium.en "caught"; Claude is my reading. The GPU line is captioned "RTX 30 i3", as heard.
- Tool changes this job (`workflows/sequence-captions.py`): the clip clamp uses the last word's start; `import --srt <file>`.
- While importing, the project's active sequence read "GTA 41 - NPC Reactions" (another session's job, `gta6-npc-organic`, is working in ABW11). Not touched.

## Word fixes (v1, two listeners; re-apply on the new transcript)
- 4.8-5.1 s "30i 3" → "30 i3": "RTX 30 i3 12th generation processor". medium.en and large-v3 both hear "30i3"; the GPU model past "30" is not audible in the cut.
- 20.6 s "clawed" → "Claude": "these motherf*ckers have Claude by their side now".
  - large-v3 heard "clawed", and medium.en "caught" (plain and prompted).
  - "have ___ by their side" needs a noun, and the next line is "way more people are capable of doing this". **Flagged to him as my reading.**
- "for the summer of next year" (not "before"): confirmed by medium.en on the span.

## Lessons
- **A lock step must stop when the lock is busy.** On 24 Nov the second-listener command ran anyway after `mkdir` failed, then removed the ASR lock another session had taken. No transcription was running on the machine at the time, so no harm was done.
  - The pattern now: `if ! mkdir "$L"; then exit; fi; trap 'rm -rf "$L"' EXIT`.
- **He edits while the caption job runs.** Re-read the sequence right before `import`, and if it changed, rebuild first.
