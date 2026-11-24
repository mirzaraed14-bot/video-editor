# COLD READ 2: SEQUENCE.md v2.1 (19 Nov 2026)
Files only (SEQUENCE, COLD-READ, README, CANDIDATES, ig/IG-PASS-1, audio/*.txt + words.json, api/*.json, twitch/*.tsv, frames). No audio played.

## A. The 8 must-fix items from COLD-READ.md
1. **Proof per beat (views, link, clip used): PARTLY.** Beats 1, 2, 4 now carry clip URL and views, and the Proof paragraph says plainly the clips are tiny (1-78 views); the Brendaniel mismatch is disclosed. Beats 5-7 (xQc) have a VOD id but no URL or view figure, and beat 1's Fanum view count is wrong (new item 2).
2. **"Every quote checked" overclaim: FIXED.** §0 item 1 and the gate row "OPEN (audio by ear)" say the quotes were not heard; "or his voice" is gone.
3. **Judgment gate on an invented judgment: PARTLY.** It now cites real posts: the 13.7M reel caption, Twitch titles "BIG FOOT REAL" / "fanum finds out bigfoot is real" / "BIGFOOT GOT HIM" (all in the tsv), Lacy's chat "THATS THE FUCKING BIGFOOT" (visible in `frames/dense-lacy-bigfoot.jpg`), LazarLazar 140K (api). But "I FIND BIGFOOT in GTA VI 521K" (Willyrex) is in no file in this folder (new item 6), and no actual viewer comment on the reel is quoted.
4. **Beat 6 time label: FIXED.** New beat 5 `≈ VOD 15:01:09-15:01:13` matches pull start 14:37:30 + 1419.5 s; beat 6 15:01:35 and beat 7 14:54:42 also compute correctly.
5. **G2 creature on frame in 6-7: FIXED.** G2 now reads "1, 2, 4 (legs) and 5; beat 6 is a dark shape (named as such)".
6. **Asymmetric reactor counting: PARTLY.** The table now counts IG creator reels both sides and says the jet wins YouTube 6.6x. But "the jet has two" famous faces still ignores Leopard etc., and the IG total claim depends on a non-theft reel (new item 1).
7. **Source overlays and anchor test: FIXED (one wrinkle).** Per-source cover list added; anchor test is in the NOT-done list. Wrinkle: new item 7.
8. **Beats 6-8 not self-contained / "then": FIXED mostly.** Quest context is in § 2 and the order note, "then" is gone, the Kirk label exists. Still a stranger sees the deer-sighting question answered by "Nope. Skunk ape" with only the note, not the table, saying so. Acceptable if the build adds the label.

## B. NEW defects (most serious first)
1. **"The jet leads Instagram by total creator shares" is true only because a non-theft reel is counted.**
   - Line (§1 row 3 and "The bar"): `Typical Gamer 65K, Leopard 80K, itssmro 56K, nixstahh 156K (flying, not a theft), alphavoid 0.4K: about 357K` / `It leads ... Instagram by total creator shares`.
   - Wrong: IG-PASS-1 line 21 has nixstahh as "driving a plane in GTA 6 for the first time". Without it the jet total is about 201K against Bigfoot's about 229K, and the claim flips.
   - Fix: drop nixstahh from the jet column (or say "jet 201K, 357K with a plane reel") and delete or soften "leads Instagram by total creator shares".
2. **Beat 1 Fanum view count is wrong.**
   - Line: `"fanum finds out bigfoot is real", 66-78 views`.
   - Evidence: `twitch/bigfoot-clips.tsv` and `list-bf.tsv`: Fanum = 56; 78 is summit1g's "BigFoot Got 1G".
   - Fix: write "56 views".
3. **"Seconds" in beats 5-7 are pull-timeline seconds, not seconds in the named files; offsets also disagree.**
   - Lines: `xqc-chase-1370-1500.mp4 ... (file 1419.5-1423.6)`, `xqc-kirk-0940-1060.mp4 = VOD file 1032.0-1040.6`.
   - Wrong: a builder seeking 1419.5 in a 130 s file finds nothing; in-file times are 49.5-53.6 and 92.0-100.6. The ASR files are named `-1380` and `-0960` (different offsets from the mp4 names 1370 / 0940); the chase ASR is on +1380, the frames on +1370. "Our frames at 1033.75 and 1036.25" vs the frame files `...-93.5` / `-96.5` (= 1033.5 / 1036.5 on the 0940 base).
   - Fix: add a column "in-file seconds" and state each file's pull offset (1370, 940, ASR 1380, 960).
2b. (same area) see 4.
4. **Beat 6 has no audio support in its window and its f-word lands just after it.**
   - Line: `≈ 1445.0-1447.8 ... "Run! We're the prey! Run!" (subtitle)`.
   - Evidence: `xqc-chase-1380.txt` has "No, run! / Run!" at 54.7-55.7 (= file 1434.7-1435.7), nothing in 1445-1447.8, then "No!" 1447.5 and "What the fuck!" 1448.2-1450.4.
   - Wrong: the subtitle is on frame at 1445.5/1447, but the spoken line may not sit there; the out-point is 0.4 s before an f-word (censor row says "2 f-words" only).
   - Fix: re-measure the beat-6 edges on the VOD audio at build, and add the 1448.2 f-word to the censor row as a hazard.
5. **Kai Cenat is counted in the pitch but not in the Short.**
   - Lines: § 1 `Bigfoot has four of the biggest names (Kai Cenat, xQc, summit1g, Fanum), the jet has two`; § 2 `hunted xQc's (and Kai Cenat's) at night`.
   - Wrong: Kai's evidence is a 5-like IG re-up, his VOD moment is unlocated (§ 0 item 6), and no beat uses him. The Short shows three cams (plus Brendaniel, no cam). The "four vs two" argument therefore rests on an item not in the cut. (The `GTA Updates` YouTube title "KAI CENAT & FANUM FOUND BIGFOOT IN GTA 6", 874 views, is real evidence for Kai and could point to where he is, but is not cited.)
   - Fix: say "three in this cut, four if Q5 is yes", and remove "(and Kai Cenat's)" from the viewer-gets line.
6. **Evidence for "Willyrex 521K" is not in the folder.**
   - Line: `Willyrex "I FIND BIGFOOT in GTA VI" 521K, from the watcher`.
   - Evidence: no `api/` file, README or CANDIDATES has it (only an unrelated "Willy Shorts" 0.01M video). It is a Judgment-gate and Proof-line figure.
   - Fix: copy the watcher row (video id, views, time read) into `api/` or drop the figure.
7. **Fanum "crop to the game area" contradicts "every face cam stays visible".**
   - Lines: § 3 `Crop to the game area; our caption plate covers his captions` vs `Every face cam stays visible, with the name on the cam's bottom edge`.
   - Evidence: his cam is inside the 16:9 frame (`fanum-cams.jpg`); summit1g's `Khafen: $50.00` alert sits ON his cam (`cr-summit-16.0.jpg`), so "blur" covers part of the face beat.
   - Fix: state the crop rectangle that keeps cam and drops chat/counters, and move the alert-cover to a plate outside the face.
8. **Beat times do not close.** Beat 6 ends 0:23.7 and beat 7 starts 0:23.9 (0.2 s unassigned); beat 7 ends 0:32.5, so "about 32 s" is 32.5; beat 7 (8.6 s) is a quarter of the Short with xQc silent and no split. Fix: start beat 7 at 0:23.7 and state total 32.5 s; one line on why 8.6 s of a two-person subtitle dialogue holds.
9. **"1.3-1.5x the views per hour"** (§ 1 "bar"): 440K/h vs 325K/h = 1.35x; nothing gives 1.5x. Fix: "about 1.35x".
10. **Stale cross-file claims.** README Step 2 says "8 searches, `api/s1-8.json`" while SEQUENCE and the folder show 12 (`s1-s12`); IG-PASS-1 line 49 still says "No Kai/Speed/xQc reaction ... found", contradicting § 12's Kai confirmation. Fix: one-line edits in each.

## C. Verdict
v2.1 fixes the structural issues (quotes overclaim, timestamps, G2, overlays, self-containment). Remaining risk is numeric and builder-facing: one comparison (IG shares) flips when counted evenly, the Kai argument counts an element not in the cut, one proof number and one watcher number are wrong or unbacked, and the xQc beats' seconds are in the wrong frame of reference for whoever cuts them.
