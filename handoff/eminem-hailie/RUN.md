# RUN: eminem-hailie ("She graduated with a 3.9")

▶ **TRANSITIONS (2026-09-26): DONE in `ABW7.aep` → ABW8 Linked Comp 18**, 16 from the creator's labels, each
read back at its cut. Undo group "Abundance Wisdom transition pass (Claude)", project NOT saved.
`transitions/transitions18.jsx` re-runs cleanly; its log is `transitions/transitions18.txt`.
- Purple dips (−90) at 1.65, 6.58, 11.58, 25.60, 29.60, 35.12 · Dark Green (+30) at 13.23, 15.42, 18.42,
  22.55, 31.47 · Peach uni.Exposure at 8.48, 16.90, 27.23 · Cyan blur at 4.75, 20.08. Aqua blocks: none.
- Stack: caption precomp (1) → transitions (2–17) → zooms (18–39) → glow bars → Adjustment Layer 32.
- Next: audio in Premiere (PLAYBOOK § 6), export.

▶ **ZOOM PASS (2026-09-26): DONE in `ABW7.aep` → ABW8 Linked Comp 18** (the build comp on the Topaz render
`Hailie_stab_chr2_iris3_prob4.mov`). 22 × S_BlurMoCurves ("Adjustment Layer 29"), layers 1–22, above the glow
bars and Adjustment Layer 32. Undo group "Abundance Wisdom zoom pass (Claude)", project NOT saved.
Plan + preview: `zoom/` (`apply.tsv`, `zoom-preview.jpg`, `zoom.txt` = the read-back).
- 5 pull-outs (yellow): 1.65–4.75, 11.58–13.23, 16.90–18.42 (the aesthetic doubles), the Higgsfield stills
  23.60–25.60 and 27.23–29.60. 17 push-ins. Depths by block length (0.85 / 0.78 / 0.70).
- **Doubles = one block** (100 % shot over its 198–229 % twin, same in/out: 6 of them), one zoom above both.
- 6 face pivots (y 515–701). The 6 "no face" blocks are black-and-white Tyson profiles; the preview at the
  deepest zoom shows every brow below y200 there too (only Tyson's scalp and the cap tops crop).
- Next: transitions (the creator labels for them after the zoom pass, LESSONS 2026-09-24).

▶ **CAPTIONS (2026-09-26): CAPTION TRACK ON ABW8 · Sequence 08, verified on screen.** 57 captions, **max 3
words**, 0.09 → 39.30 s wall to wall, ALL CAPS, italic on Tyson's and Anderson Cooper's questions, no commas or
full stops. From `captions/outputs/seq08-captions.srt`; styling guide `captions/caption-colours.md` (Gretaros /
Gretaris Italic + which word takes which colour style). Grabs: 0.3 s "HAILIE IS", 16.0 s *"HOW OLD"*.
Next for the creator: Upgrade Captions To Graphics → styles from the cheat sheet → Revised Light pop → export on black.
- Built from the LIVE recut (39.3 s, 34 A1 clips incl. the 60 Minutes stinger the creator added): the voice
  was rebuilt from A1 and re-transcribed (`captions/raw`, `captions/transcript`); measured fixes are in
  `words.json` `_fixes`, Whisper's original in `words.whisper.json`.
- **Flags:** (1) 15.40–15.66: the Tyson clip starts 0.25 s early and catches the end of his "I know". It
  reads as "No" and is left uncaptioned; trimming the in-point to 1965.58 removes it. (2) 37.43–37.69:
  Cooper's question is captioned "YOU NEVER / MET HIM SINCE?". "since" was heard on 2 of 3 passes
  (the other heard "so"). Retype if it's wrong.

▶ **HEAD LOCK (2026-09-26): APPLIED in AE `ABW7.aep` → ABW8 Linked Comp 07–13, all 20 layers, proven.
AE project NOT saved** (undo group "Head lock (Claude)": run 3 times, all 3 need undoing to revert).
Next: the creator saves, renders the stab comp → Topaz (PLAYBOOK § 3).
- The creator had recut Sequence 08 before replacing (20 clips, not my 32; a new Tyson clip at 3:34.6, 206 %),
  so the track was built from the comps' own layers (`brief/ae_comps0713.txt` → `brief/headlock_live0713.txt`
  → `track.json`, `headlock_map.json`), not from my placement.
- Per layer: Anchor Point keyed on every 60 fps frame (linear, 1,355 keys), Motion Tile 340 / mirror
  (Output Width 110 on comp 11 L1, the wide shot at the clean edge). **Nose held at its MEDIAN position**
  (`--hold median`), so the face stays where the creator's crop framed it; frame-1 holding parked comp 10 L1's
  face at x 180.
- **The 10 Tyson layers at 187.2 %** get "Border out (Claude)" (a Transform effect, 103.34 / 105.26 %) BEFORE
  Motion Tile, and their Scale is 181.18 / 177.87 %: the same 187.23 % framing at rest, but the lock's moves
  (up to 81 px vertically) can no longer drag the baked red frame into view or mirror it. Comp 10 L3 (206 %)
  has 97 px of clean margin and needed none.
- Proof: the track checked on each layer (the dot on the speaker's nose, inside the crop); AE's read-back
  anchors hold every tracked nose within 0.03 px (unlocked: 14–235 px). `headlock_read.json`.
- **Flag for the creator: comp 12 L2** (source 2011.77, the co-host reaction shot) carries L1's Position (77.5):
  at rest the frame shows the dark wall and a mic, and the co-host's face is off to the left. Locked as is, not reframed.

▶ **STATUS (2026-09-25): SEQUENCED on ABW8 · Sequence 08. Read back, audio proven.** 32 clips on V1+A1,
0 → **36.73 s**, 4 beat markers (B1 card "2002", B3 card "2019"). Built from **the creator's pasted
SEQUENCING, beats 1–4 only.** Their words: "do the sequencing that I've sent you", NOT the MD's other
drafts and NOT its 60 Minutes stinger (the `EMINEM 60 MINUTES INTERVIEW 2021 (NEW).mp4` in the bin is
unused). Project NOT saved by us. Next, per PLAYBOOK: the creator's pass, then head lock → Topaz → captions.

| | |
|---|---|
| Channel / preset | Abundance Wisdom → `presets/youtube-shorts/abundance-wisdom/` |
| Brief | the creator's paste = `E:\Claude Projects\Abundance Wisdom\EMINEM-HAILIE-CUT.md` → DRAFT 6 § SEQUENCING, beats 1–4 |
| Project | Premiere `ABW8.prproj` → **Sequence 08** (1080×1920, 60 fps), bin **Eminem** |

## Sources (all from bin "Eminem", `E:\Bullshit Folder\Henry\`)
| key | file | fps | note |
|---|---|---|---|
| hailie | `Eminem - Interview talking about Hailie (HD).mp4` | 25 | 1280×720, one continuous rooftop take (no cutaways, so no child frames) |
| tyson | `Eminem _ Hotboxin' with Mike Tyson.mp4` | 23.976 | 1920×1080 B&W, **baked red frame 26/30 px**, multicam (17 cuts in 32:40–33:52); transcribed window 32:00–35:00 |

## The cut (what the assembled audio says, re-transcribed from the READ-BACK in-points)
| beat | tl | words |
|---|---|---|
| 1 HOOK (2002) | 0.00–9.83 | "Hailie, she has been my main source of drive and motivation, especially when she was first born. I didn't have a career yet. I didn't have money. I didn't have a place to live." |
| 2 THE FEAR | 9.83–16.32 | "How am I going to raise her? I can't fail. I can't have her grow up and not be able to say her dad succeeded." |
| 3 THE ANSWER (2019) | 16.32–23.47 | Tyson "How old is she?" / "Hailie is 23. She's made me proud for sure. She graduated from college. 3.9." |
| 4 THE PAYOFF | 23.47–36.73 | "I have a niece that I have helped raise too, pretty much like a daughter to me. And then I have a younger one that's 17 now. So when I think about my accomplishments, that's probably the thing I'm the most proud of, being able to raise kids." |

Trims inside quotes, per the paste: "whether she's with me or not…" (1), "kicked me in the ass" (between 1 and 2),
the first of two "I can't fail." (the last take kept), the boyfriend chatter and "She's doing good" (3),
"that's kind of like a daughter", "and she is 26", "you know is that is" (4). **Fillers the transcript had
dropped, found by ear and cut:** "like" (my main *like* source), "uh"/"um" (Haley is *um* 23), the stumble "had".
**14 pauses tightened, 10.3 s** (0.13–2.57 s each; the 2002 take is very slow), so the head lock + zoom hide the jumps.

## Checked
- **Edges measured** (10–20 ms RMS + isolated Whisper re-listens), all in `beats.json` `_edges`.
  The aligner was wrong on "23" (really "twenty… three", 1969.1–1969.9), on "3.9" (1989.50–1990.56;
  its "Wow" was "point nine") and on "live" (a stray vocalisation at 24.4 was merged in).
- **Camera cuts never inside a clip:** a cut in a silent tail becomes the clip edge (3 would otherwise flash 1 frame).
- **Read-back:** 32/32 V1+A1 match the plan (timeline exact; in-points within 16 ms, all inside kept pauses; scale/pos exact).
- **Audio proof:** `outputs/seq08-audio-proof.wav` (rebuilt from Premiere's own in/outs) re-transcribes as the table
  above. Whisper reads the question as "Girl, how old…" only at the rooftop→studio join; alone, every start from
  1965.575 reads "How old is she?".
- No profanity in the cut (Tyson's lead-in ends before 1965.58; "our kids are f—ed up" is after the out).

## Framing (`framing.json`, contact sheets in the session)
Hailie: fill height 266.8 %, crop on the face (detector). Tyson: **187.2 %** (fills 1920 with the red frame
pushed out, not 177.9 %), faces set by hand where the detector found none.
**For the creator's eye (the broadcast's own camera, nothing better in that take):**
1. 16.32–17.52 "How old is she?" plays over a **whip-pan** co-host → wall → Tyson.
2. 19.33–21.00 "She's made me proud for sure": **wide room shot**, Eminem small at the right edge.
3. 27.45–28.70 "pretty much like a daughter to me": a **co-host reaction shot**.
4. Tyson listening shots under Eminem's words: 17.52–18.27, 20.99–22.32, 31.38–33.25.

## Re-run
`resolve_beats.py projects/eminem-hailie` → `uv run plan_placement.py projects/eminem-hailie` →
`clear_seq08.jsx` (refuses unless the sequence holds exactly Claude's 32/32 clips + 4 markers) →
`place_sequence.py … "Sequence 08" "Eminem" place_seq08.jsx` → `readback08.jsx`.
