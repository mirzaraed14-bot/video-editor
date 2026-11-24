# barbell-logic-bench-shoulders: Onyx sample Short for Barbell Logic (Matt Reynolds), batch 17 Nov

## ▶ STATUS: resume here
- 2026-11-23 (builder, fix after Opus QC): frame 0 was mid-entrance (hook card sliding, first caption blurred). Fixed in `yt/build_spec.py` (overlay JS kills the kit's t=0 hook/first-chunk tweens and holds both static for the first frames; hook swish s01 dropped, 6 cues left). Final = v9, overlay re-run only. Same frame count (1084), -12.2 LUFS, cue_check PASS. Frames 0/3/10: `outputs/...frames-0-3-10.jpg`.
- 2026-11-23 (Sonnet builder): **BUILT, YouTube look, Option A / H1 / O1.** `outputs/barbell-logic-bench-shoulders.sample-yt.final.mp4` (= v6), copy `X:\Claude Projects\Exportsarbell-logic-bench-shoulders.yt.final.mp4`. 45.21 s, 1084 f, 23.976 fps native, -12.2 LUFS / -2.2 dBTP, 7 swishes (cue_check PASS, none weak on a phone), no bed. Proof sheet + shots sheet in outputs/ (`...proof-sheet.jpg`, `...shots-sheet.jpg`); QC frames `work/qc/`. Credit: BARBELL LOGIC watermark on every frame + name labels (Andrew, Niki). The link back to the original goes in the DESCRIPTION (not built).
- FLAGS: (1) Matt IS on camera for ~1 s in the Short (SEQUENCE said never). (2) Captions sit at ONE base y835, NOT just under the lips: both sources have the head at the top of frame (lips y 465-730 in output, p95 747, max lip bottom 772 on a lean), a full-height 9:16 crop cannot move a head down; the base clears the worst frame by ~17 px but is ~200 px under the median lip line. (3) Andrew is cropped 2.1x from 1080p, Matt/B-roll 1.5-1.8x: soft but not haloed; grade tuned per source (yt/grade_look.json), default sharpen. (4) No ghost / measured number in beat 2 (the Short's reps are handheld and do not register): SEQUENCE's plain-card fallback: cards COMMON ERROR, LOOSE SHOULDERS, LONGER RANGE / LESS STABLE over the loose rep; their baked pills are covered by a flat glass plate. (5) Red ring on the shoulder (beat 4) is a drawn overlay on real footage, not a drawn lifter; FX-28 readout is HEEL / FLOOR / PUSH. (6) Beat 3 ends on "motion|and" (no pause: 15 ms crossfade), beat 6 starts on "ground,|you're". (7) Picture is not tied to speech in beats 2, 4, 6, 7 (B-roll from other parts of the same two videos; fist demo beat 5 is in sync-ish, shifted 0.4 s early). (8) Matt has no name label (his 1 s is under the hook plate). (9) Weaknesses 1-5 of SEQUENCE stand: two coaches' fixes, lifters only, two shoots, Matt must OK Andrew's video, 45.2 s (over the 45 s note). (10) Burn-ins avoided by crop (Andrew window y 0-912 of 1080: the lower-third and handle/SUBSCRIBE bars sit below y 930); end frames of every used span checked: no promo frames. (11) Scratch: bash `/tmp` is C: Temp, so the splice runs from `work/cut/splice_local.sh` (scratch in work/tmp), nothing written to C: by this build except the transcribe.sh scratch json.
- RE-RUN WITHOUT REBUILDING: `bash projects/barbell-logic-bench-shoulders/yt/run_all.sh <v> overlay` after editing `yt/build_spec.py` (captions, cards, labels, ring, SFX; `work/cue_adj.json` per-cue dB) = ~3 min. `... grade` redoes grade+sharpen+finish (~10 min); `... picture` (default) redoes crops (`yt/bl_picture.py`, windows in build_spec.py, optional `yt/crops.json`). Promote: `python yt/finish.py <v>`. Cut: `work/cut/make_edl.py` (pieces, per-source gain), `AMPLIFY_DB=0 bash work/cut/splice_local.sh <job>`, then `python work/cut/retime.py` (adds the missing "A", drops stray "ground,"). Transcript verified by a large-v3 read of the cut: 162 words, verbatim.

- 2026-11-17 21:50 PST (Sonnet session local_c8b929f5, started by the Onyx hub): **SEQUENCE WRITTEN, WAITING FOR AFFAN'S OK. NOTHING IS BUILT.** `SEQUENCE.md` (this folder) holds Option A (recommended: "Bigger Bench: Push The Floor", Matt's Short + Barbell Logic's leg-drive video, ~46 s), A2 (the Short alone) and B (the seniors reroute), the hook/order variants, and what he must answer: which option (picking A = OK to use Andrew Jackson's leg-drive video) and YouTube only or both looks.
  Research done: 4 YouTube searches, 3 long-forms pulled + transcribed (CPU, draft times), the Short measured and looked at, catalog pass, two Sonnet cold reads, advisor x2, leg-drive audio measured (no music bed) and frames checked across every used span (baked handle/SUBSCRIBE bar in beat 4's span, name lower-third in beat 3's). NOT done: Instagram comparison (instagram.lock held by another session); the parent "how to bench press" video is Private.
  After his OK: WhisperX large-v3 under `lock.sh gpu` on the Short + the leg-drive video, hand-checked edges, then the build per BUILDER-BRIEF (batch 9) rules. Sources: reference/, source/, work/*.cpu.txt.
- 2026-11-17 ~21:30 PKT: Affan: "make the short for barbell logic in a new session" (overrides his 11-12 "drop both").

## The prospect
Barbell Logic, host + owner Matt Reynolds, https://www.youtube.com/@BarbellLogic (97.1K subs). His yes (11-02): "Please credit Barbell Logic and link back to the original" -> on-screen credit in the sample, the original's link in its description.
Permitted Short: **Z0slBdQC5nM "Want a bigger bench?"** (17.4 s, 720x1280, 30 fps, 10,995 views on 2026-11-17, uploaded 2026-10-07). Feed median 852 views (278 Shorts), so the permitted Short is already ~13x median (11th of 278). Their best ever: w-Y2fVDN5Aw "Best Exercise Program for Seniors!?" 91K.
Prior sessions (batch 7/8) judged the permitted Short "17 s of voice-over, nothing to enhance" and staged a REROUTE to the seniors strength piece (onyx-staging/batch8/, projects/_onyx-batch8-2026-11/SEQUENCING.md). Affan dropped Barbell + Remnant 11-12 before any OK.

## Downloads (logged before pulling; all via lock.sh youtube, H.264, spaced >= 60 s)
| File | Source | Use |
|---|---|---|
| reference/Z0slBdQC5nM-permitted-short.mp4 | copy of _onyx-batch7-2026-11/_shorts/barbell-logic.mp4 (pulled 11-05 by batch 7), 2.2 MB | the permitted Short, teardown + beats |
| source/cLsbvZiM4d8-leg-drive.mp4 | YouTube cLsbvZiM4d8 "How To LEG DRIVE! Increase Your Bench Press" (154 s, 153K views) | candidate beats: same subject (bench), Matt's best-viewed bench long-form |
| source/5xWyVUJAXJo-butt-on-bench.mp4 | YouTube 5xWyVUJAXJo "Butt on the Bench: Better Bench Press, Build Your Arch, Bigger Chest & Arms" (220 s, 12K views) | candidate beats |
| source/YFxTcOL4jzM-bar-out.mp4 | YouTube YFxTcOL4jzM "Take the Bar Out with Authority (Start Your Lifts Right!)" (280 s, 5.4K views) | candidate beats |
| (not pulled) YouTube sSXDYMy1f6c, the "how to bench press" video linked in the leg-drive description | PROBED 2026-11-17 21:40: "Private video" (plain access error, not a bot check). No file. |
| (already staged) X:\Claude Projects\onyx-staging\batch8\bb-full-A2jUBUdbJQo.mp4 | YouTube A2jUBUdbJQo seniors episode (94 MB, 1080p, pulled 11-09 by batch 8) | the fallback reroute |

## § 0 Platform pick (PLAYBOOK § 0)
YouTube-first. Evidence: (1) the permission email named a YouTube Short (Z0slBdQC5nM); (2) YouTube Shorts feed = 278 Shorts, median 852 views (0.9 % of 97.1K subs), the permitted Short 10,995 (11th of 278), best 91K (seniors); six most recent 1.3K / 788 / 334 / 10K / 275 / 2K; (3) INSTAGRAM COMPARISON NOT DONE: `.locks/instagram.lock` was taken by another session at 21:33 PST (and I could not find the lock's protocol file); their Instagram is instagram.com/barbell_logic. Posting frequency per 30 days not measured (the cached feed carries no dates).

## Viral bar (VIRAL-BAR.md A-I) for the permitted moment (restructured, "Option A")
| Gate | Verdict |
|---|---|
| A usable / reversal | PASS: a cue a lifter can use today (push the floor away, leave a heel print); Matt names the error |
| B universal stake | WEAK-PASS: lifters only (body, strength), not everyone |
| C loop | PASS: opens "Want a bigger bench?", ends "you can tell them a bigger number" (runs back into the hook) |
| D concrete vehicle | PASS: two real demos (fist block, loose vs tight rep) + a measured comparison |
| E title | "Bigger Bench: Push The Floor" (5 words, 28 chars) promises a how |
| F self-contained | PASS (no episode needed); cold read in SEQUENCE.md |
| G one subject | PASS: shoulder stability on the bench, hook to button |
| H simple | PASS |
| I famous face / value | value, so anyone may speak |
Weakness named first: the fix Matt gives (pinch and lower the blades, glue the shoulders) is ON-SCREEN TEXT only; the spoken fix comes from Andrew Jackson's leg-drive video, so the edit joins two coaches' words.

## Teardown: their Short -> ours (the reaction's talking points)
| Axis | Their Short (Z0slBdQC5nM, 17 s, 11K) | Ours (Option A, ~38 s) |
|---|---|---|
| Hook, first 3 s | Matt walks into frame holding a plate; a question under a black pill | the same question, Matt on camera, the claim as a card (loose shoulders hold your bench back), captions from frame 1 |
| Who | Matt barely visible, never named; "Barbell Logic" only in the channel name | the credit on screen ("Barbell Logic") from the first seconds, Matt/Andrew labelled |
| Picture | 720p, three black text pills across the middle of the frame | real demos at full size, our own graphics, no baked text on top of the lifter |
| Fix | on-screen text only ("pinch and lower shoulder blades"), in the description | spoken, shown and cued: push the floor away, leave a heel print |
| Ending | trails off on "Don't let this happen to your bench." | ends on the payoff and loops back to "Want a bigger bench?" |
| Length | 17 s | ~46 s |
Flag: their permitted Short is already ~13x their own median, so the gap to sell is the 91K seniors Short, not this one.

## Catalog pass (CLAUDE.md rule 5), 2026-11-17
Read all of research/effects-catalog/CATALOG.md (80 moves, FX-01..FX-81) and looked at all four contact sheets covering the 80 reference stills.
- Fit this video: FX-21 Red Silhouette Set (a line-drawn lifter on a bench, shoulder blades the ONE red element: nothing clean exists of "loose vs glued"), FX-71 Funnel Count (one measured number, big, with a small label), FX-70 Ring and Benchmark (a single ring on the J-hook height), FX-28 Dossier Readout (a spare readout for the cue: HEEL / FLOOR / PUSH), FX-37 Ghost Dissolve (loose rep ghosted over the tight rep), FX-80 Black-Beat Ident (a dip before the button).
- Not yet used on Onyx samples: the drawn lifter set and the measured-comparison number.
- Not used: maps, newsprint, documents (nothing here is a document), CRT frames.
## Better than the last one of its kind
Rise Above (the last true "how it really works" sample) leaned on a clock and a dossier. This one: a measured comparison taken from the host's OWN footage, a drawn scene for the thing nobody filmed, and a loop (button runs back into the hook).
