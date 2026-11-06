---
name: project-gta-documentary-channel
description: "Affan Afterhours — the user's GTA channel: the GTA 6 explainer is the default (doc paused); video 22 SHIPPED 2026-10-22; video 23 (gta6-world-stops, ABW10) review 1 applied 2026-10-23; video 24 (gta6-day1-mistakes, ABW10) full draft 2026-10-27; video 26 (gta6-feels-bigger, ABW10) review 1 applied 2026-11-03 (he re-cut zooms/jokes himself; reading spans filled), at his review — RUN.md; video 27 (gta6-complete-guide, ABW10) draft saved 2026-11-06, at his review, uploads that day; his face-zoom grammar in facecam CREATOR-HAND.md"
metadata: 
  node_type: memory
  type: project
  originSessionId: e1b9cd8c-a044-4294-9e79-318eb202a8a0
  modified: 2026-11-06T05:14:59.215Z
---

**Affan Afterhours** (https://www.youtube.com/@AffanAfterhours, ~2k subs, 51 videos). The user stays on camera.

**Two formats, decided 2026-09-19.** The **GTA 6 explainer** is the channel's engine — top videos 167k / 34k /
16k / 13k / 10k — and the **default** for what comes next: a bright colour-LED room, animated hands, ≥ 17 visible
changes/min, **opens on the face**, illustrated **stills in Rockstar's own VI key-art style** (flat vector, hard
shading, saturated pastels; Higgsfield, 2 cr, never video) placed at **85–90 over a dark colour matte + BCC Film
Grain** (dark red / dark blue / dark gold, never light), gameplay **zoomed out over the same matte**, posters with
ONE hot-pink keyword, motion graphics doing the heavy lifting with **people as animated PNG cutouts of the real
person** (a manager's cutout travels to the artist's, the artist's to the label's), ≤ 30 credits. The
**documentary format is PAUSED**: Hot Coffee (shipped 2026-09-18, `projects/gta-san-andreas-hot-coffee/`,
~900 credits ≈ $50) sits at 237 views; *"we can just pay an editor $20… that was an experiment video."*

**THE FACE SHOT IS NEVER STILL — the creator's own grammar, in order (confirmed in the Hot Coffee export):** (1)
nest a face run's jump-cuts into one sequence; (2) inside the nest, a **"cut zoom"** on the emphasis word — an
instant scale snap, no ramp, **+25 in the explainer** (+5/+10 in the doc); (3) a **keyframed gradual zoom
100 → 110** on the nest clip itself. Stills get a ~5 % creep too. A replay that flattens the face destroys all
three; hand face runs back nested with the ramp on the nest. **The pipeline does it now** (2026-09-19, on the creator's ask): picks as data in the job's `transcript/face-zooms.json`, applied by `lanes/premiere/face-nests.py --apply/--verify`.

**Episode 2 — "How Rockstar Actually Hired Travis Scott For GTA 6"** (~8 min, the casting-call thesis). Job
`projects/gta6-travis-scott-hired/`. **SHIPPED 2026-09-20** (they exported and uploaded; 7:39). The learning pass is written:
`projects/gta6-travis-scott-hired/POSTMORTEM.md` — they KEPT 37/37 graphics, 163/164 SFX at identical levels, all 38 face
nests + 37 cut zooms and the cut itself; they ADDED three receipts (the real Club Shay Shay interview inserted 8.1 s where the
narration cites it, a credits card from Metro Boomin's *Superhero*, a Travis photo in the slot I could not source), REPLACED
the voice with an Adobe Enhance Speech v2 bounce (−22 LUFS, 128 kbps) and laid 4 Epidemic tracks on A7 with silences before
section turns. Rules that changed: the face gradual zoom is a RATE (~1.6 %/s), a cited on-camera source is PLAYED not drawn,
an unsourceable slot gets an alternative artifact offered, insert points snap to word boundaries.

**NEXT VIDEO (2026-09-21): the FACE-CAM style, measured in `presets/youtube/affan-afterhours-facecam/`** — the creator is
"dieting down" the editing back to the look that got 170k: face + ~5 cut zooms/min at +25 % held ~1 s + a ~1 %/s push,
3–4 game-footage runs/min of ~4 s (Extended Look is the bread and butter), 1–3 posters per video, 1–3 slow-downs at 0.6x
(pitch kept), ≤ 2 hard chops, opens and closes on the face, first minute cuts 1.5–2.5x faster. Measured off two masters
(`GTA Cars.mov` 170k, `Gta gun.mov` 35k) with `workflows/style-probe/-set/-zoom/-audio/-report.py`; the third reference
("CAN'T Do Anymore") was dropped by the creator on 2026-09-22 — the two measured masters are the spec. The script for the
next video is coming from the creator; the job runs in this style (its PLAYBOOK) with the channel PLAYBOOK/LESSONS.

**Why:** the creator wants each video cheaper and faster, in the style that already works for them, with better
explanation than a static poster gives.
**How to apply:** start with `PLAYBOOK.md` § 0a (two formats) and the job's `BRIEF.md` "▶ STATUS" block. The
overlay frame (matte + grain under an inset picture) is CHANNEL-WIDE — only the scale differs per format; the doc's
palette and mannequin rule do not carry to an explainer. Any web-sourced picture is enhanced in Higgsfield if soft
([[feedback-sourced-stills-must-be-hq]]). Get approval before any Higgsfield credit
([[reference-higgsfield-connector]]); never touch A2 ([[feedback-creators-hand-is-not-a-bug]]). Related:
[[user-abundance-wisdom-editor]], [[feedback-long-term-self-improving]], [[reference-epidemic-sound-connector]].

**2026-10-08 — CHANNEL AUDIT DONE; START HERE NOW: `presets/youtube/affan-afterhours/EDITOR.md`** (the GTA editor's handbook: reading order, the style on one card, where every asset lives). The creator's own grammar, read clip by clip off their three shipped face-cam timelines, is `presets/youtube/affan-afterhours-facecam/CREATOR-HAND.md` and wins over the reference numbers: saved presets "110 GTA LF Zoom Preset" (nests) / "105 GTA Lf Zoom Preset" (single clips); cut zooms = razor + static scale, median 121–136 %; slow-downs 0.8x only where jokes are (0–11); pops at −18 dB (they pulled them 12 dB down after Game Informer); music by clip gain −20…−27 dB, out under every cut zoom; their meme layer (colour-bars glitch, Vine boom, memes, cricket). `gta6-vice-city-sign` shipped as 'Collector's Box DISAPPOINTED Everyone', `gta6-hurricanes` as 'Everything Game Informer Just Revealed'. Audit data: `research/afterhours-channel-audit/`.

**2026-10-09 — video 22 "You Can't Just Play The Missions In GTA 6" (job `gta6-ign-missions`) edited on ABW8 › Sequence 39, at step 7 (the creator's review).** State + resume: `projects/gta6-ign-missions/RUN.md`. New graphics language ("IGN dossier": quote cards on blurred game plates, the recurring mission-line diagram, explainer diagrams, premium Epidemic SFX) logged for the creator's verdict in facecam `LESSONS.md` 2026-10-09 — read their verdict there before reusing any of it. Sequences 37/38 belong to the Onyx session; Premiere is shared (ACTIVE-WINDOW.lock).

**2026-10-22 — video 22 SHIPPED (he exported it himself); video 23 "The Day The World Stops For GTA 6" (job `gta6-world-stops`) edited on ABW10 › "GTA 23 - The Day The World Stops" (new bin "GTA 23 World Stops"), at step 7 (his review).** State + resume: `projects/gta6-world-stops/RUN.md`. New in 23: the receipts system (REAL / REPORTED / ESTIMATE / IMAGINED corner tags + source line on every card), IMAGINED dossier scenes, the November countdown rail, a 27-file Epidemic SFX palette, cut zooms gentler (median 130 %) for his new closer "relaxed" setup, a verbatim-prompted stutter guard on the cut. His verdicts go in facecam `LESSONS.md` before reusing any of it. Premiere ABW10 is shared with the English Editor session (AffanWiz CA-007): message before saves, ACTIVE-WINDOW.lock for any active-sequence switch, Sequence 19 restored.

**2026-10-23 — video 23 review 1 (his Tella walkthrough) applied and SAVED, back at his review.** Rebuilt on HIS cut (read
off the live timeline first; his two own zooms carried over by source time): pauses tightened 37/47 but the punchline AND
comedic beats kept (a first pass that cut the comedic ones was caught by a fresh-eyes review: his comedy is timing), the SFX
replaced by a screened one-family-per-meaning set (the old kit's most-used clicks were narrow tones, 42-60 dB tonal
prominence), every comp on screen from frame 0 (his "Number one" glitch), "fuck" cut from the voice 4x (A1 pieces disabled),
and 8 "27 DAYS" subscribe CTAs (his new ask, overrides the no-CTA default for this channel). Details: RUN.md + facecam LESSONS.

**2026-10-27 — video 24 "14 Mistakes You'll Make On Day 1 Of GTA 6" (job `gta6-day1-mistakes`) full draft on ABW10 › "GTA 24 - 14 Mistakes On Day 1" (new bin "GTA 24 Day 1 Mistakes"), saved, at step 7 (his review); he exports.** Raw X:\Recordings\Onyx\C1409.MP4 (one file), NEW SETUP: sunglasses, Skool neon sign, YouTube plaque, red mic; YuNet still finds his face but the leather chair is a false face (nearest-to-centre picker). His script v2; CTAs "23 DAYS" (upload 27 Oct); he cut the two Phil Hooker setup lines (payoff never recorded). 9:08, 42 graphics + 9 CTAs, 73 zooms, 70 SFX, 241 A1 crossfades. New treatments awaiting his verdict are listed in facecam `LESSONS.md` (2026-10-27). Resume: `projects/gta6-day1-mistakes/RUN.md`. Trap learned: never run audio-polish's gain measurement inside ACTIVE-WINDOW.lock (25 min; he switched sequences meanwhile) — measure outside, apply `--gain N` in a short window (lab-notes 2026-10-27).


**2026-11-03 — video 26 "Why GTA 6 Will Feel MUCH Bigger Than It Is" (job `gta6-feels-bigger`) full draft on ABW10 › "GTA 26 - Feels Bigger Than It Is" (bin "GTA 26 Feels Bigger"), saved, at step 7 (his review); he exports.** Raw X:\Recordings\Afterhours\C1425.MP4 only (C1427 = AffanWiz CA-010, his answer). Same room as 24, framed closer, and his hands sweep the lower right, so the "15 DAYS" CTAs (upload 4 Nov) were moved to hand-clear windows (`review/cta-scan.py`). Two Sonnet edit-review rounds (content 15 / visual 18 defects) converged; the builder fixes are worth porting (LESSONS 2026-11-03). New treatments await his KEEP/NEVER verdict in facecam LESSONS: baked 0.8x joke slow-downs, CITY redaction reveal, quiet part cards, footprint grid, receipts tags.


**2026-11-04 — first Afterhours SHORT in the Scott Clary YT Short style: `projects/gta6-all-fit-inside/` ("They All Fit Inside",
his v5 script in `X:\Claude Projects\GTA 6\sweeps\shorts-sweep-2026-11-04.md`; raw C1445, camera carries the voice).** Black + pink
MGs (`#EE2A9A`), no watermark, native 59.94 code build. He picked the full ~58 s cut; v3 (61.95 s, native 59.94, -12 LUFS, 18 swishes, no bed) DELIVERED 2026-11-04 to Exports/afterhours-gta6-all-fit-inside.v3.mp4 for his review; music answer still open; his v3 notes (0.8x + Vine boom on "All of them", smooth the choppy slow-mo B-roll) -> v4 (4K Iris + sharpen) delivered 23:49 (channel LESSONS 2026-11-04); WhisperX collapsed the
retakes, so cut times come from `work/cut/bursts.json` (per-burst faster-whisper). Resume at the job's BRIEF ▶ STATUS.

## Index line archived from MEMORY.md (2026-11-02 compaction, verbatim)
- [GTA channel: two formats](project-gta-documentary-channel.md) — **GTA jobs start at presets/youtube/affan-afterhours/EDITOR.md (audit 2026-10-08; creator's own grammar in facecam/CREATOR-HAND.md)**; Affan Afterhours; the GTA 6 EXPLAINER is the default (doc format PAUSED); episode 2 "Travis Scott" SHIPPED 2026-09-20 (POSTMORTEM.md); video 3 = the FACE-CAM style, presets/youtube/affan-afterhours-facecam/ (measured 2026-09-21); video 22 (IGN missions) SHIPPED 2026-10-22; video 23 (gta6-world-stops, ABW10 › "GTA 23 - The Day The World Stops") review 1 applied + saved 2026-10-23 (pauses, premium SFX v2, frame-0, censor, 8 CTAs); video 24 (gta6-day1-mistakes, ABW10 › "GTA 24 - 14 Mistakes On Day 1") full draft 2026-10-27, at his review — RUN.md + facecam LESSONS

**Video 26 review 1 (2026-11-03):** he revised the cut zooms + jokes HIMSELF and asked to learn from them (never undo them). Measured
lessons in facecam LESSONS.md (2026-11-03 review 1): zoom = the WHOLE payoff phrase (snap outward), no ladder on a joke's setup, no zoom on
bridge lines, weak tag asides cut, a stumble may be kept + punched 182 %. He also flagged uncovered script-reading spans: the 0.45 yaw
threshold was too high; gate reading with look-read's Otsu threshold on the PLACED timeline (review/his-review-1/yaw-gaps.py).
Fills f01/f02 (17:13) + f03 at 4:01.6 on his "yes, fill it" (19:35) placed and saved on ABW10; a reading fill ends where yaw returns to ~0
(a half turn is still reading). A4 bed restored under the 3 covered zooms on his yes (saved 19:51). Censor at 7:07.1: he said "Leave it audible" (2026-11-03). Outro stays on his face (his call). Review 1 fully closed; next = his notes or his export.

**Video 27 "GTA 6 Complete Guide: Do These Before November 10th"** (job `gta6-complete-guide`, C1447 only, ABW10 › "GTA 27 - Complete Guide", 9:32): draft saved 2026-11-06 03:31, at his review, uploads that day 8-11pm Pakistan time, he exports. His brief "1 % improved": the list and how each came out in its BRIEF.md; new treatments with verdict pending in facecam LESSONS (N/17 pill + rail + checklist, PREVIEW BUILD receipt, menu-path cards, line-drawn controller and minimap). Next = read his timeline diff, then write the verdicts.

**2026-11-06 — video 27's Short "The Head Start"** (job `projects/gta6-head-start`, raw C1448, script `X:\Claude Projects\GTA 6\video27-SHORT-head-start.md`, Scott YT style, black + pink, 59.94 code build): he picked version B by button (script as written, his Ultimate ad-lib out). Final 52.35 s in `Exports/afterhours-gta6-head-start.final.mp4`, **APPROVED 2026-11-06, first delivery, no notes** ("approved"), must post Sat 7 to Mon 9 Nov (before the pre-load). The defaults he never answered (no bed, 0.8x + boom on "value your time" only, drawn phone and PS5 menus, pauses closed on his face) passed with it, and the next Afterhours Short in this look starts from them; findings in the channel LESSONS 2026-11-06, tool notes in `lanes/chat-only/lab-notes.md`. The hook's split jump of ~65 px at 2.7 s passed too (splits aren't tracked, his rule). Traps: WhisperX collapsed restarts again and an RMS read hid it, so wait for the burst pass before quoting takes or lengths; POP grade needs the room's `grade_look` (this room's numbers in the job's build_spec), test a still first. A worktree session's Write/Edit hook blocks the main checkout even after a folder grant; he approved shell writes for that job folder, then for the channel LESSONS and the chat-only lab-notes, and the OK covers only the paths he named. Resume at its RUN.md.

## Moved from the MEMORY.md index (2026-11-06)
**GTA jobs start at presets/youtube/affan-afterhours/EDITOR.md**; the GTA 6 EXPLAINER is the default (doc format paused); face-cam style = presets/youtube/affan-afterhours-facecam/; latest: video 26 (gta6-feels-bigger) review 1 applied 2026-11-03 (his zoom/humor lessons in facecam LESSONS); 2026-11-04 Short gta6-all-fit-inside (Scott YT style, black+pink) v4 delivered 2026-11-04 (his notes: slow-mo+Vine boom on the joke, interpolated B-roll); full log in the file
