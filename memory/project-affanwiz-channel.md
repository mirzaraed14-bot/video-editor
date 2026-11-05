---
name: project-affanwiz-channel
description: "AffanWiz = the creator's English personal-brand YouTube channel promoting their Skool community; its own preset folder, separate from Affan Afterhours and the Urdu @affanwizu reels"
metadata:
  node_type: memory
  type: project
  originSessionId: 26a2857f-411a-4f2c-917d-fb6059e77b46
  modified: 2026-11-04T02:28:56.555Z
---

**AffanWiz** (named 2026-09-23) is the creator's English personal brand, long-form YouTube with them on camera,
used to promote their **Skool community** (raw footage under `E:\Skool Recordings\`). They asked that every style,
asset and finding for this channel be stored SEPARATELY: `presets/youtube/affanwiz/` (README · PLAYBOOK · LESSONS).

**Why:** three channels now share this repo (Abundance Wisdom shorts, Affan Afterhours GTA, AffanWiz); rules from one
must not leak into another. Not to be confused with `presets/instagram/affanwizu/` (Urdu reels).

**How to apply:** read that folder before any AffanWiz job; write every direction they give into it the same turn.
Job 1 = `projects/monetized-before-gta6/` (from Premiere project ABW8 · Sequence 02). Workflow: they hand
over a Premiere sequence with an Enhance-Speech voice on A1; rough cut first, replayed ONTO their handover sequence itself (never a new sequence, told 2026-09-28), then THEY do the face cut, nests and zooms and drop overlays on V1, and I finish the overlays (jobs 1–2: README § 1a, 88.5 % fit + one plum/teal matte; superseded in size/matte/shadow by STYLE.md from 2026-10-04; tiny ones 50 % width and Higgsfield enhancement still hold). Never touch their nests.
They lay the music bed on A2 themselves; the music DROPS OUT under every punch-in (V1 Scale > 100, they use 127),
their emphasis device (job 2, 2026-09-28; PLAYBOOK § Music row).
**From the next video (told 2026-10-04) the look is `presets/youtube/affanwiz/STYLE.md`**: the creator ported their
Afterhours video "Everything Game Informer Just Revealed About GTA 6" (job gta6-hurricanes, ABW8 Sequence 16):
pushes on every face run, cut zooms 103–203 % with the music out, 85 % filled inset overlays on a varied matte each,
a pop on every overlay switch, no grade/slow-downs/captions. It is COPIED into the AffanWiz folder, not linked.
Job 3 (2026-10-04) = `projects/kick-fake-viewers/` (CA-003, ABW8 Sequence 27): the creator's scripts + research live in
`X:\Claude Projects\Personal Brand English - Skool Community\creator-shorts\CA-NNN-*.md`; they want TIGHT joints
(~2 frames out / 1 in), improvised bits kept, and every asset the script names gathered via their Chrome and laid in
the sequence (PLAYBOOK § Assets).
**2026-10-13: the look is STYLE.md v2 = the IGN-missions style** (Afterhours video 22, "GTA 6 Just Got A Whole Lot More
Interesting…", our job gta6-ign-missions / Seq 39): full-frame "IGN dossier" graphics (blurred footage plate on V2 + alpha
HyperFrames overlay on V3), b-roll inset over its own blur, premium SFX (whoosh/pen/ticks/chimes) on A3/A4, beds on A5 out
under every zoom, cut zooms median 135 %, no face push. Sequence 27 (CA-003, kick-fake-viewers) was restyled to it; the
reusable pattern is that job's folder. v1 (Game Informer port) kept as STYLE-v1-game-informer.md.
**2026-10-22: CA-007 "I Ranked Every Streamer's Content Machine"** (raw X:\Recordings\PBE\C1389.MP4, job
`projects/streamer-content-machines/`) built in a NEW bin + sequence "CA-007 Streamer Tier List" in **ABW10** (shared that
night with the Afterhours session doing GTA 23: lock + by-name + ask-before-save protocol). STYLE v2 + a tier-board spine
(side board on the face at each verdict) + chapter tags + side cards; fresh Epidemic SFX set.
**2026-10-23 revision 1** (his Tella review, four must-fixes) built, gated and SAVED in ABW10: lip sync (V1 rebuilt from his
A1), reading covers (face share 34 %), new SFX set `sfx2/` (110 cues / 67 files), a CTA about every minute (one as a chip
inside t25). Awaiting his re-review; he exports himself (RUN.md, review/REVISION-1.md).
**2026-10-27: CA-009 "Speed Bought the iPhone Duo. 20 Clippers Got Nothing."** (raw X:\Recordings\Onyx\C1410.MP4 — an AffanWiz
take despite the folder; job `projects/iphone-duo-clip-angle/`) built in ABW10, NEW bin + sequence "CA-009 iPhone Duo Clip Angles",
with CA-007's four fixes built in from the start: V1 pre-split from a video-only subclip (sync 0 off), reading measured by head pose
(sunglasses: reading = a head TURN, yaw), covered 0 s visible, fresh SFX `sfx/` (84 cues/54 files), CTA ~once a minute + plug card,
music beds on A4 incl. one new bed. 3 edit-review rounds, all gates green; at his review (RUN.md has the resume block + flags).
**2026-10-28: CA-009 uploaded; AffanWiz SHORTS start**, in the Scott Clary YouTube format: code-built with the onyx-samples-youtube
kit, no music (he scores it), swishes only, hook card 0–3 s, face ≤ 4 s. They live in their own channel folder
`presets/youtube-shorts/affanwiz/` (ENGINE/FINDINGS/RESULTS, prediction locked before upload); jobs go in `projects/<long-form>/clips/<name>/`.
- He sent his own text sequence (v3). It is built as `clips/reupload-wont-go-viral/`. He approved the check and the 60 fps FINAL was
  delivered 2026-10-28 (Exports `affanwiz-reupload-wont-go-viral.final.mp4` + thumbnail).
- Later the same day he re-ordered it (v2: his conclusion moved to the top, his duplicate spoken hook cut, abrupt end on the list). The v2
  is exported NEXT TO the v1 final (`...v2-reordered.final.mp4`). It was rebuilt without a new Topaz run: the shipped segments were
  re-ordered and the Iris frames split with the segment muxer (BRIEF.md has the recipe).
- Kit note: for a fast-moving speaker, use the chained head lock (`head_track: false`, `head_chain_n: 2`) and run the head-snap gate.
- Credit tag on his Shorts = VIRAL FACELESS CREATOR / 530K+ SUBSCRIBERS, never his name ("no one cares who I am", 2026-10-28;
  ENGINE.md). Still open: a Skool CTA or none.
- Small text fixes on a delivered Short: re-render ONLY the overlay (`yt_build.py <job> <ver> --skip picture,mix`), never the
  whole video (he asked for lean fixes, 2026-10-28).
- Short 2 is not chosen yet (candidate: "Same stream, 23 clips", `shorts/PICKS.md`).
**2026-11-02: CA-010 "The Viral Clip Method Big Shorts Channels Gatekeep"** (raw `X:\Recordings\Afterhours\C1427.MP4`, an AffanWiz take in the
GTA folder, first briefed as a GTA edit) → job `projects/viral-clip-method/`, ABW10 bin/sequence "CA-010 Viral Clip Method". Improvised one-pass
talk around script v2 (no demo, no cold open). Affan confirmed C1427 is the right file (he was surprised it sat under Afterhours). He OK'd
2 Sonnet reviewers; they found 48 hidden stumbles, so the cut went 13:20 → 12:41 (222 segs, gates green). 2026-11-03 he answered the sequencing
"Yes, use defaults" (MJ allegations line cut, whole talk kept, no cold open → graphics from frame 1). 12:32, 220 segs.
2026-11-03 15:04: DRAFT COMPLETE + SAVED on ABW10 › "CA-010 Viral Clip Method", at his review. The draft:
- 46 full-frame graphics + 18 side cards (11 Skool CTAs), built by 3 Sonnet builders he OK'd, 3 Sonnet review rounds;
- 109 fresh Epidemic SFX;
- his 5 beds + 1 new no-vocal bed ('fresh perspectives');
- 69 zooms.
Every gate is green. Proof: `outputs/CA-010-proof-frames.jpg`. Resume: its RUN.md.
2026-11-03 17:43: after the hand-off HE trimmed two lines (-1.07 s, rippled) and put his Enhance Speech v2 mp3 on A1 (his normal step: our A1 chain is temporary). On his "Yes, add it" the head-steady lock went on top of that: static Scale/Position per V1 piece, `work/head_steady.py`; 35/51 visible jump cuts locked (6 before), same-take pieces around a zoom tied to one framing. Saved 17:43; proof `outputs/CA-010-head-steady-proof.jpg`; method in LESSONS (CA-010 after the hand-off).
2026-11-03 evening: **CA-010 UPLOADED** (by him). He asked for a Short from it in the Scott Clary YouTube format: SEQUENCING FIRST (the script, which bits, source timecodes) as text for his OK, then the build. The CA-010 session owns it; the job goes in `projects/viral-clip-method/clips/<name>/`. Open question put to him: the credit tag under the 0–3 s hook (Short 1 had it there; his 2026-11-01 Scott rule says no).
20:15: the read-back showed nothing changed after 17:43, except one earlier hand change: the cold-open bed went −20 → −10.5 dB
(LESSONS § CA-010 UPLOADED). Proposed `clips/find-viral-angles/SEQUENCE.md` ("How I Find Viral Shorts Angles Nobody Has Made", ≈ 42 s:
call-out hook → MJ niche + 30M → angles → NFL → his Claude prompt). Waiting for his OK; nothing is built.
2026-11-04: his note on it (add "manual = hours, Claude = 10–20 min", motion graphics on the MJ explanation, the most value, ≤ 45 s;
the three general ones are now ENGINE § Format overrides) → v2 in the same SEQUENCE.md, ≈ 44 s, "How I Find Shorts YouTube Is Forced To
Push": question hook → niches → MJ biopic/30M → MJ angle map (MG) → manual vs Claude $20 → 10–20 min scour → his prompt. Then v3: + his NFL bit after the MJ angles, still ≈ 45 s (cut: niches line, money, $20, "of the NFL"). He approved it with the defaults; 2026-11-04 08:40 the 30 fps check went to Exports (affanwiz-find-viral-angles.check-30fps.mp4, 45.2 s, ends on the filled angle map). Review 1 the same day (REVIEW-1.md): his notes were the centre picture (now a real 1988 photo, CC BY 2.0 Alan Light, credit in the description), "the, the" said twice (WhisperX hid it inside "covered"), awkward pauses (quiet runs now cut at -34 dB), and the hook card ON the caption line, swapping to the captions. He said "start the 60fps", and the 60 fps final went to Exports at 13:42 (affanwiz-find-viral-angles.final.mp4 + thumbnail.jpg, 43.8 s; state in BRIEF.md). Before upload: his RESULTS row 2 prediction and the photo credit in the description. Review 2 the same evening (REVIEW-2.md): "the camera … snaps with my head" (cause: review 1's micro pause cuts on his face + the chained lock moving the crop at each, up to 148 px; fix: no face pause trims < 0.3 s, head_track + edge pin, hook card held via the new kit key hook.hold_end) and "remove the 30 million bit" + the "How many aspects…" line after it. 60 fps final re-delivered 23:22 (40.4 s, replaces 13:42).
CA-009's verdict (read off ABW10): all graphics kept, 81/84 SFX, he cut 1.6 % tighter.
**Folder ≠ channel:** always transcribe and match against `creator-shorts/CA-NNN-*` before choosing a preset.

Related: [[user-abundance-wisdom-editor]], [[feedback-long-term-self-improving]], [[feedback-every-video-better-than-last]].


## Index line archived from MEMORY.md (2026-11-02 compaction, verbatim)
- [AffanWiz channel](project-affanwiz-channel.md) — English personal brand (promotes their Skool); its OWN preset folder presets/youtube/affanwiz/, never mixed with Afterhours or @affanwizu; from 2026-10-13 the look is STYLE.md v2 = the IGN-missions style (Afterhours video 22; pattern: projects/kick-fake-viewers); CA-007 tier-list video built 2026-10-22 in ABW10 (projects/streamer-content-machines); 2026-10-23 review → revision 1 (sync rebuild, reading covers, new SFX, CTA each minute); 2026-10-27 CA-009 iPhone Duo (projects/iphone-duo-clip-angle) built in ABW10 "CA-009 iPhone Duo Clip Angles", at his review; 2026-10-28 AffanWiz SHORTS start (Scott Clary YT format, presets/youtube-shorts/affanwiz/): his own sequence built as iphone-duo-clip-angle/clips/reupload-wont-go-viral, 30 fps check in Exports, awaiting his OK
