# riseabove-death-row-guard: Onyx sample Short for Rise Above with Kevin Lanning (batch 9, NEW moment)

## ▶ STATUS: resume here
- 2026-11-12 22:06 (main) **SIGNED OFF (YouTube look) after fix rounds 1-2, checked from the Exports copy** (`X:\Claude Projects\Exports\riseabove-death-row-guard.yt.final.mp4`, identical to outputs/): 54.05 s, 1296 f, 23.976 fps, -12.1 LUFS / -2.3 dBTP, decodes clean. Round 1 head jumps (95, 497) fixed; round 2: the ECC alignment's stretched left border (take from 1140) is gone (left/right 260 px strips of 10 frames across every aligned take looked at: real picture only), 1139->1140 now eases in, sizes match by eye. Every graphic as directed. Flags for Affan: Steve Henley is our inference (Kevin confirms before upload); no 2009 photo of him, so the dossier is text only; two deliberate silent entrances (the hatch objects, the corridor); the last card sits on the episode's own gated room tone (near silent); 54 s. Instagram look not built.
- 2026-11-12 fix round 2: yt/fix_joints.py now clamps joint shifts (24 px, scale 0.95-1.06), adds a per-shot coverage zoom (pivot y300, x1.02-1.17) so no edge carries replicated pixels (numeric edge check clean, contact sheet outputs/riseabove-death-row-guard.edge-check.jpg), and an eased +8 % push on the end of the beat-8 take into the 1139/1140 cut. final/Exports/proof sheet = v4.
- 2026-11-12 fix round 1: head joints re-done by yt/fix_joints.py (ECC on the cap/face ROI of the graded picture: after-take shifted/scaled to the before-take, s05 gets an eased +8 % push instead of the step; joints 37,95,240,254,497,507,839,996,1140 corrected, run after restore_drawn); final/Exports/proof sheet = v4. YuNet single-frame numbers stay noisy (+-30 px on non-joint frames).
- 2026-11-12 21:35 (Sonnet builder): YT FINAL DONE. outputs/riseabove-death-row-guard.sample-yt.final.mp4 (= v3), copy X:\Claude Projects\Exports
iseabove-death-row-guard.yt.final.mp4, proof sheet outputs/...proof-sheet.jpg.
  54.05 s, 1080x1920, 23.976 fps, -12.1 LUFS, true peak -2.3 dBFS. Rebuild: cut = work/cut/run_cut.sh + retime.py; scenes = uv run yt/scenes.py yt; all = bash yt/run_all.sh <v> (grade takes ~25 min); mix/overlay only: yt_build --skip picture,captions.
  Flags: (1) Henley is our inference, Kevin must confirm. (2) TWO deliberate silent entrances: the beat-5 objects leaving through the hatch and the beat-6 corridor (hard cut in). (3) Dossier is text only (no 2009 photo exists in HQ results), CRIME row says CONVICTED OF KILLING ... (NBC: convicted, he claimed innocence).
  (4) Last card uses the PRINTED words: I'D LIKE TO SAY I HOPE THIS GIVES FRED AND EDNA'S FAMILY SOME PEACE. / FROM MY EXPERIENCE IN LIFE IT WON'T. (5) Room tone is the episode's own at -75 dBFS (gated mic) + the swell. (6) cue_check FAIL on cue 10 is an artifact (no voice beside it); it sits 22 dB under the voice peak.
  Deviations: cell B starts at "It was like he had left" (not only the last line) and the receipt holds through "enjoy it" (keeps every bare face run <= 4.9 s); clock shown real-time 1 s ticks; clock block at y640 not dead centre (caption band); SPLIT seam at y1092 so captions never change height.
- 2026-11-12 20:10 (Sonnet builder, YT look only): CUT DONE (work/cut/make_edl.py + run_cut.sh + retime.py; outputs/riseabove-death-row-guard.mp4 = 16:9 cut, 50.8 s,
  transcript/cuts.json = the EDL, reusable for the IG build; every mid-phrase joint settled by slice ASR, verbatim pass clean: work/cut/fw_cut_v3.*.txt). Scenes drawn (yt/scenes.py),
  spec built by yt/build_spec.py (15 shots, N 1296 = 54.06 s at 23.976). Next: picture build, grade test, overlay, mix, QA, reviewer, finals.
- 2026-11-12 19:15 (main, Opus): Affan approved v4 ("start to build", YouTube look ONLY for now; the IG look comes later from the same cut).
  DIRECTION.md written. A Sonnet builder runs `projects/_onyx-batch9-2026-11/BUILDER-BRIEF.md`. Builder (Sonnet) started 19:19.
- Open for Affan / Kevin: the executed man is NEVER named in the episode. Steve Henley (Feb 4, 2009) is our inference from David's dates;
  Kevin must confirm it when the sample goes for approval. Cecil Johnson (Dec 2, 2009) fits only if David started after Feb 2009.

## The Short and the point
Their permitted Short: "He was dopesick…so he robbed a Pharmacy" (J5OkkeBMNVs, 8.6K views, 179 s; `reference/J5OkkeBMNVs-their-pharmacy-short.mp4`).
Affan rejected that story ("2 is not good") and asked for a better moment of the show: this is a NEW moment from the episode "I Was a Death
Row Guard" (xKGU_cd9kx4, 586K views). Rerouted on Affan's 11-05 note; Kevin approves the moment AND the Henley name before anything is uploaded.
**The viewer gets:** what really happens in a condemned man's last days, from the guard who strip searched him, and the last-meal myth
answered. **Title:** He Watched A Man Find Out He Was Going To Be Executed

## Beats: `projects/_onyx-batch7-2026-11/SEQUENCING.md` § 2, "Death row v4" (10 beats; DIRECTION.md maps each to the episode)

## Teardown: their channel's Shorts → ours
| Axis | Their Short (pharmacy, 179 s) | Ours (~63 s) |
|---|---|---|
| Hook, first 3 s | mid-story, no claim card | David's own line "keep you fed ... until the state turns your lights out" under HE GUARDED DEATH ROW |
| Who / what by 5 s | the guest is never named | the claim card, then his label (raised Amish, former death row guard) |
| Length | 3 minutes, stops before the ending | ~60 s, one arc from the news to the last meal to the man's last words |
| Visuals | one face crop | a dossier on the man, the appeals struck out, the empty unit, a running 72-hour clock, the infirmary, the receipt, his real last words |
| Ending | none | the victims' closure, then his own last words: "From my experience in life, it won't." |

## Catalog pass (CLAUDE.md rule 5), main, 2026-11-12
Read all of `research/effects-catalog/CATALOG.md` and looked at all 79 reference stills (two contact sheets, 2026-11-12).
- Used here: FX-28 Dossier Readout (the man), FX-54 spirit for the appeals cards, FX-40 Slow-Burn Portrait ("checked out completely"),
  FX-21 Red Silhouette Set (the cell, the unit, the infirmary: nothing was filmed), FX-71 Funnel Count as a running 72:00:00 clock,
  FX-33 Dust Void Drop (the receipt), FX-80 Black-Beat Ident (the dip), FX-27 Red Word Quote (his last words), FX-42 Kin Tag (labels).
- New to Onyx samples: the dossier, the running countdown carried across beats, a voiceless closing quote card.
- Not used: maps, photos of the victims, any courtroom or execution imagery (nothing real exists of it; nothing invented that looks real).

## Better than the last one of its kind
The last true-story samples (Drea's Sopranos money, HPP) leaned on photos. This one carries a real clock through the story, names the man
with verified facts, and ends on a primary-source quote instead of a talking head.

## Downloads (logged before pulling)
| File | Source | Size | Use |
|---|---|---|---|
| source/1180-1600.mp4 | YouTube xKGU_cd9kx4, episode seconds 1180-1600 (pulled 2026-11-05 by the batch-7 session) | 54.7 MB, 1920x1080 23.976, 420.1 s | the episode window |
| reference/J5OkkeBMNVs-their-pharmacy-short.mp4 | YouTube J5OkkeBMNVs (their permitted Short) | 45.2 MB | teardown only |
| NBC page (AP copy, Feb 4 2009), https://www.nbcnews.com/id/wbna29018293 | curl, page text only (read in memory, not kept) | 0.37 MB | PULLED: verified the last words, the date, Fred and Edna Stafford, "Edna was still alive when the fire was set", "burned-out farmhouse" |
| Steve Henley photo candidates (3 Bing queries, 23 thumbnails) | curl Bing image search (workflows/img-candidates.py) | ~6 MB, deleted again | NONE USED: every hit was a later TDOC inmate (2020s mugshots), no 2009 photo of Henley exists in the results. The dossier is TEXT ONLY, as DIRECTION § 3 allows. |
