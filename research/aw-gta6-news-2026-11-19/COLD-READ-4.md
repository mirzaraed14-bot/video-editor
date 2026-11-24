# COLD-READ-4: SEQUENCE.md v2.6 vs v2.5 (changed parts only). Files only, no audio/video played.

1. **§ 4, 150K re-lock is uneven between the two moments.**
   - Line: "Bigfoot, most likely | 90K | **150K**" and "Jet, most likely ... **90K ... unchanged**".
   - The factor table itself marks YouTube lane "jet +, still about 3x bigger" and jet entry tax "Typical Gamer 3.32M, same footage". Only the Bigfoot-favouring rows are applied to the centre, and the jet-favouring rows move nothing. The rule ("move only for a factor measured today") is applied one way.
   - The only comparable that carries the +60K is one fan upload (CaseOh, 543,004). The other measured streamer/Bigfoot Shorts in `api/t2/v_ids*.json` are Kai fan 139,163, Keoxer 69,506, Swagg 47,799, Poggers 39,570, Barış 36,659; same-day compilations ~2K.
   - Fix: either re-centre both on the stated rule (the jet's 3.3M same-footage Short is an entry tax and a lane lead), or state the weights and show the median of the comparables (~70-140K), which lands under 150K.
2. **§ 4 "Why 150K": the "closest comparable did 543K" is a single outlier, and the "join works" claim in G4 rests on n = 2.**
   - Lines: "The closest comparable ... did 543K in a day" and G4 "so the join works".
   - Evidence: the same files show 8+ same-day streamer Shorts still at 0.9K-2.1K. The 543K upload is a CaseOh fan page whose own Twitch Bigfoot clip the doc says (line 31) is a cocaine-mission dialogue, so "same angle (a streamer finds Bigfoot)" is not shown to be this creature.
   - Fix: say "two breakouts of about ten", and don't call the 543K Short the same angle without checking it shows the creature.
3. **§ 3 beat 6 and line 38: the "4 reactors hold mid-clip" standard is not met by Kai.**
   - Line 38 says the standard is "camera, creature and reaction in one clip". G2 and the table say the creature is "not clearly visible" in the beat-6 window.
   - Frames: `kai-22.5.jpg` / `kai-1080-sheet.jpg` show a dark shape, the objective "Chase Mr. Mangrove" and his cam; the creature and effigy appear only at ~50-58 s.
   - Fix: keep it at 3 on its own standard, or restate Kai as "cam + reaction + objective", and word the "four with the moment on frame" lines (§ 1 table, line 56) to match.
4. **Effigy reading is not applied everywhere.**
   - Supported: `frames/b-xqc-chase-1370-1500-52.jpg` and `kai-4up.jpg` (bottom-right: "What the... / Inspect the tree" prompt on the glowing figure) back an interactable object.
   - Still reading it as the live creature:
     - line 114: "the creature on frame next to Kirk in beat 5";
     - line 115: "linked by the creature on frame";
     - line 230: "beside the same glowing creature";
     - line 234: "glowing skunk-like animal" (historical, but unlabelled);
     - the "viewer gets" line ("hunted xQc's and Kai Cenat's at night") and beat-5 caption "He's hunting me!" imply a live hunter.
   - The figure note says the Short "claims only what is on screen"; "hunted ... Kai's" is not on screen (Kai chases an objective).
   - Fix: change 114/115 to "the effigy"; reword the viewer-gets line to "chased xQc's and Kai's at night" or drop the hunted claim.
5. **Beat 6 out-point clips the last word.**
   - Line: in-file "22.2-25.8"; ASR "OH MY GOD!" 25.54-25.84.
   - Fix: out-point at 25.9 or later (the beat becomes 3.7 s, so shift beat 7 and the total to 33.2 s), or end on 23.5 and drop the second shout.
6. **Kai Short rate looks wrong.**
   - Line: "139K (about 26K/h)".
   - Evidence: published 2026-11-19T13:11:10Z (18:11 PKT), so by 04:30 PKT it is ~10.3 h old, which is ~13.5K/h on its average. 26K/h only fits if you read an earlier count I can't find in the files.
   - Fix: cite the earlier reading, or use "about 13K/h average".
7. **Beat 6 "no minors" is asserted from one cam.**
   - Lines: "minors: none on frame" (§ 13), G-row "no real children on camera".
   - `kai-1080-sheet.jpg` (rows 2-3) shows an unidentified person standing behind Kai in his cam, and the chat usernames are legible in the strip. Covering the chat and counters is consistent with the frames (chat ~y 650-790, counters ~y 530-600, cam x 0-392, y 432-652), but the person in the cam is not addressed.
   - Fix: add "second person in the cam background, adult by size, cam kept small" or crop to Kai.
8. **Leftover wording.**
   - § 1 lines 53-54 (jet "leads YouTube by 6.6x"; Bigfoot "1.35x views/h, 10x shares") conflict with § 4 (about 3x; about 2x and about 12x). The header does say the table is the 19:45 snapshot, so this is minor.
   - Line 142: "the exception line ... no longer needed for Bigfoot" is OK, and I found no live "90K" for Bigfoot, "tried and stayed low" or "out of the cut" outside the labelled v2.5 column.
9. **Numbers checked and fine.**
   - 543,004; 139,163; lane 124K -> 204K/h and 100K+ 5 -> 10; jet 602K/h, 27.
   - Clip 4096145023: URL, 7 views, 60 s, 1080p/60, created 09:16:27 UTC (= 14:16 PKT).
   - ASR times match; beats 3.6 + 8.6 + earlier sum to 33.1 s.
   - Typical Gamer 3.31M in the watcher file vs 3.32M in the doc, and TmarTn2 3.66M vs 3.71M: minor, probably a later API read.
   - Instagram 15.8M/16.5M and shares are from UPDATE-2026-11-20-0430.md only (no raw file to cross-check).
