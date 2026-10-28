---
name: project-abundance-wisdom-longform
description: "Abundance Wisdom's first face-led long-form, Nick Walker \"The Body That Could Never Win\"; rough draft on ABW8 Sequence 24 (2026-10-03), job nick-walker-never-mr-olympia"
metadata:
  node_type: memory
  type: project
  originSessionId: e83a5461-9372-426b-acd3-91eb82cfebd1
  modified: 2026-10-26T11:07:34.795Z
---

**2026-10-26: every new AW long-form starts at `presets/youtube/abundance-wisdom/PLAYBOOK.md`.** It holds the gist of the look and
the procedure, distilled from Nick Walker → SAME NIGHT → THE LAST SHOW (projects/cbum-last-show, the current state of the art, uploaded
a few days before 2026-10-26). It is a starting point, never a style lock: each video does the whole FX-catalog pass and beats the last by ≥ 5 %
([[feedback-every-video-better-than-last]], [[feedback-aw-longform-documentary-rules]]).

**2026-10-26: the next one, Paris Jackson "BOTH VERSIONS" (locked script 22 Oct, ~15:30, publish within 7 days), job
`projects/paris-jackson-both-versions/`.** BRIEF.md (catalog pass, Beats-THE-LAST-SHOW list, lock conditions) + RUN.md are the state;
checkpoint 1 sent, waiting on his answers (project, a missing Ch1 host line, 8 IDM downloads). Its own rules: no AI, no stock, no minors
on frame, "suicide" never as on-screen text.
**State 2026-10-26 evening: the whole film is on ABW10 › "BOTH VERSIONS - rough cut" (13:47, tight pacing, his call), at his review.**
Every layer is placed and verified by script: the cold open, the clip layer, Ch1-6 scenes, face nests, the audio chain, DeNoise, the piano bed,
121 SFX, 3-frame host crossfades, 2 subscribe alerts and the end black. Final mix −14.2 LUFS / −1.3 dBTP. B8 report in `B8-REPORT.md`. He exports. Still waiting on him:
- the host LUT, which he applies by hand;
- OK on the IG original, the "…" captions and the 5a bleep.
**2026-10-27: his review 1 is applied (REVIEW-1.md, LESSONS 35-42).** The film is now 13:13. His own 10 pause cuts are kept. The changes:
- a scored music arc on A5;
- 21 censors;
- in-clip pauses capped at 2 s;
- late reveals re-timed;
- Willow's cutaways replaced by a word card;
- the promo frames cut;
- quieter SFX.

Final mix: −14.2 LUFS, −1.3 dBTP AAC. He watches next, then exports.

Live state is in work/review1/live.json (the old placement JSONs predate his cuts).

**2026-10-28: review 2 applied (REVIEW-2.md, LESSONS 43-47): "very close to upload material".** His notes:
- the Oprah word card's ending: it now finishes its line and carries into Chapter 3;
- paper SFX −3.5 dB;
- a fade to black at the end;
- an Ozzy callout on Jack.

His own edits (score under the cold open, a tabloid cut) are kept. Runtime is now 13:14. He watches, then exports. The live snapshot is work/review2/live-r2-after.json, and the frame proof is work/review2/frames/.

**Nick Walker: DONE (the creator confirmed 2026-10-07).** It was the template for the next long-form.

The Abundance Wisdom channel's first face-led long-form: Nick Walker, "The Body That Could Never Win" (LOCKED script v2,
2 Oct 2026, target ~9:15, publish by Oct 4–5 while the Olympia news is warm). Job folder
`projects/nick-walker-never-mr-olympia/` (RUN.md is the state). The creator records + syncs + cuts their own host
blocks in ABW8, then asks for the third-party clips to be laid between them; rough draft first, polish later.
State 2026-10-03: rough draft placed on **Sequence 24**, 9:41, 39 clips, polish to-dos as sequence markers; then the
creator's Tella direction (BRIEF.md) placed and verified: 68 cards, nested host zooms, MG, flash roll, highlighter, dips,
light leaks, press captions.

**The creator's standing overlay look for this long-form ("for all overlays from now on", Tella 2026-10-03):** every
third-party clip/screenshot is a CARD at ~90 % with bleeding edges and rounded corners over an animated golden-yellow
matte, with a subtle zoom; every on-camera host run is nested with a subtle zoom (their demo 100→104 over ~3 s);
dips to black use a Black Video with opacity keys 0→100→0 around the cut. Tools: the job's `overlays/card.py` +
`place-cards.py`, `lanes/premiere/face-nests.py`.

**Why:** the user researches the script with captions-sourced timestamps and speaker names; two of ~25 attributions
were wrong or unverified ("fighting for 10th place" was Bob, not Shawn; 5e turned out to be Shawn).

**How to apply:** every clip's in/out goes on WhisperX word timings, never the caption timestamps, and every
attributed quote gets a voiceprint check (lab-notes 2026-10-03) before it is captioned. Surface attribution
mismatches against the creator's recorded narration as flags; never re-word their narration. See
[[user-abundance-wisdom-editor]], [[feedback-youtube-sourcing]], [[feedback-creators-hand-is-not-a-bug]].
