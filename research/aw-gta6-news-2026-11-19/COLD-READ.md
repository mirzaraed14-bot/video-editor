# COLD READ: SEQUENCE.md "Bigfoot Is In GTA 6" (19 Nov 2026)
Judged from the files only (SEQUENCE, README, CANDIDATES, IG-PASS-1, audio/*.json, api/, twitch/, frames, PITCH-CHECKLIST, MAX-EFFORT-GATE, VIRAL-BAR, gta5-farewell precedent). Extra stills I pulled for checking: `frames/cr-*.jpg`. No audio played.

## 1. MUST-FIX

1. **Beat proof has no views and no per-beat link; the Brendaniel proof names a different clip than the file used.**
   - Line (beat 2): `PROVEN: his clip "BIG FOOT REAL" is the most-viewed Bigfoot clip on Twitch (1,623)`.
   - Wrong: the brief wants each beat PROVEN with link/creator/time/views, and no beat carries views. "1,623" appears in no file; `twitch/bigfoot-clips.tsv` line 1 says 1,453. The clip actually used (`brendaniel-bigfootsighting.mp4`, §7, `NimbleCarefulEyeballRedCoat`) is titled "Bigfoot sighting in GTA VI" and has **1 view** (`twitch/thumbs/list-bf.tsv` line 3).
   - Same for the others: the summit file is "Bigfoot jumpscare" = 1 view (the proof cites his 78- and 45-view clips instead); Fanum = 56; xQc VOD views are never given. Honest numbers show Twitch demand for these clips is tiny, which the pitch never says.
   - Fix: give every beat its clip URL + creator + source time + views, cite the clip used, and say plainly that the Twitch clips are 1-1,453 views and the proof is the IG reel.

2. **"Every quote checked" overclaims, and the audio gate is open but not listed.**
   - Lines: §0 `each streamer's own words match his on-stream captions or his voice` vs §8 `The audio was NOT listened to`.
   - Only Fanum has burned-in captions (`frames/cr-fanum-4.6.jpg`). Summit's "What the F*CK is happening?" (beat 4) and Brendaniel's beats 2 and 5 are ASR-only. Summit's ASR timing is smeared (`words.json`: What 33.06, the 34.46, fuck 35.86, is 36.2), so the 32.9-37.3 window is not a measured edge.
   - MAX-EFFORT-GATE item 2/PITCH-CHECKLIST §1 want quotes heard by ear.
   - Fix: add "quotes heard by ear: NOT DONE" to the NOT-max-effort list and drop "or his voice".

3. **The Judgment gate is marked PASS on an invented judgment.**
   - Line: `PASS | the viewer's belief, set up by our hook ("they found Bigfoot"), is reversed...`.
   - PITCH-CHECKLIST: the judgment must be shown in real comments or posts, "a judgment we invent = FAIL". No comment on the frizzeyes reel was read (IG-PASS-1 has none). The only skunk-ape comment is one 701-like comment on a different reel (spectrexgaming, `vo-slate/ig-beats.md` line 16).
   - Fix: quote real comments/titles ("I found Bigfoot in GTA 6" caption, Twitch titles) as the held belief, or downgrade to OPEN.

4. **Beat 6 time label is wrong.**
   - Line: `≈ VOD 14:59:00-14:59:04` for VOD file 1419.8-1423.5.
   - Evidence: pull starts 14:37:30 (§7; `GTA 6/.../hunt-eggs.md` line 2, file 975 s = 14:53:46). 1419.8 s gives about **15:01:10**, which is what the Order note itself says ("about 15:01").
   - Fix: change to ≈ VOD 15:01:10-15:01:13.

5. **G2 claims the creature is on frame in beats 6-7; beat 7 shows something else.**
   - Line: `the creature itself on frame in beats 1, 3 and 6-7`.
   - `frames/cr-xqc-75.0.jpg` / `b-xqc-chase-1370-1500-75.5.jpg`: a dark hulking quadruped-looking silhouette with a yellow eye, not the tree-bodied, rope-waisted creature of beats 1/3/6. Nothing in the files ties it to the same creature. Beat 6 (`cr-xqc-49.9.jpg`) is fine.
   - Fix: prove the silhouette is Mr. Mangrove (a frame or the quest text), or cut beat 7 / say "creature on frame in 1, 3, 6".

6. **The pick is argued against the runner-up with asymmetric counting.**
   - Lines: `at least 4 named streamers with the moment on frame, reacting`; `The jet clears neither: ... 2 reactors`.
   - Bigfoot's 5 includes frizzeyes (6.5K followers, IG reel only, not downloaded; not "big") and HutchMF (an "aftermath" clip, audio empty, creature not shown). The Short itself shows only 3 cams (Fanum, summit1g, xQc).
   - The jet's count of 2 ignores the IG face-cam reels the same pass read: Typical Gamer (65K shares), Leopard (80K), nixstahh (156K shares), itssmro (56K), alphavoid. Jet moment shares across those reels are about 357K against Bigfoot's 226K + 3K; the pitch compares top reels only.
   - The brief ranks by views/h of best clips, where the jet wins about 6x (and also wins IG views, 15.5M v 13.7M). The bar was defined after the data.
   - Fix: count both moments the same way (IG reels with named creators too) or say the bar is chosen and that the jet beats Bigfoot on the brief's own metric.

7. **Source-quality gate: other channels' burned-in overlays are not named, and the anchor test is missing.**
   - Line: `Source quality | PASS (picture)`.
   - Fanum's clip (frame 1 of the Short) carries burned-in captions ("thing? **** ***", "Bro what is"), a chat panel, a viewer count (22,421), "DEATH COUNTER" and "Twitch Subs 7157 / 8,000" (`cr-fanum-4.6.jpg`). PITCH-CHECKLIST §2 lists "other channels' captions" and lower thirds as defects. The blur sentence covers only "chat, viewer counts, sub alerts"; AW's own captions from frame 1 would stack on his.
   - Also summit's cam has a named donation alert "Khafen: $50.00" and a "21,256" count (`b-summit-...-18.jpg`). The §2 anchor test (compare against the Prince ABC panel) is not done and not listed as open.
   - Fix: list every overlay to cover/blur per source, say how Fanum's burned-in captions are removed, and add the anchor test to the open list.

8. **Beats 6-8 are not self-contained, and the pitch's facts about the quest are incomplete.**
   - Line (§1): `The game itself then says it is NOT Bigfoot`.
   - `GTA 6/.../hunt-eggs.md` F2a: this is a **side quest** with mission text ("Chase Mr. Mangrove", "Return to the truck"); Kirk's talk comes before the encounter, and Jason's "You're saying I saw... Bigfoot?" answers a sighting of "something on the road getting a deer" (xqc-kirk ASR 49-67 s), not the knock-out shown earlier. G5 says "free roam (summit: no mission text)" and never mentions the quest.
   - A stranger sees "Kirk", "Jason", "him", "Mr. Mangrove" with no setup (VIRAL-BAR F). "then" contradicts the Order note ("Nothing on screen says it happened after the chase").
   - Fix: state the quest in G5, change "then" to the real order, and add one caption/line so beats 6 and 8 name who "him" is.

## 2. SHOULD-FIX

1. **G4 numbers are wrong.** Line: `YouTube "streamers find bigfoot" compilations: all under 1K views (Dropy, GTA Updates, TurkishProduction, Komnt)`. API: Dropy 1,930 ("Streamers Found BIGFOOT in GTA 6 on Day One"), Komnt 1,511, TurkishProduction 1,220, GTA Updates 874. Only one is under 1K. Fix: write 0.9K-1.9K. Also "KAI CENAT & FANUM FOUND BIGFOOT" (GTA Updates title) conflicts with README's "no Kai/Speed on either": check it, since Kai is the biggest face.
2. **README STATUS contradicts the pick.** `no Kai/Speed/xQc on either in IG or Twitch` vs xQc carrying beats 6-8. Fix the README line (xQc is on Bigfoot, in the VOD).
3. **Cross-refs and times.** `Cold read: pending (§ 9)`: §9 is Runner-ups. Fable call times: SEQUENCE 19:44 vs README 19:49. "README § 13" is AW's README, not this folder's. Beat 1 says Fanum's cam is "top-left"; it sits left, about 37-60% down the frame.
4. **Beat 8 window.** Short 27.0-35.0 = 8.0 s but source 1032.0-1040.9 = 8.9 s. "Cut on species" but "hmm" starts at about 1040.68 (xqc-kirk words 80.68 + 960) inside the window. Beat 5: the window 54.5-58.8 includes ASR "I could be the fur." (54.6-55.3) before "Oh my god. It's Bigfoot"; start at about 55.45.
5. **Stacked split on xQc contradicts its own rule.** The rule says the split is used "only where the face is the beat". Beat 6's words are Kirk's (game) and xQc is silent. xQc's cam is the softest (370 px, about 2.9x to 1080 wide, "no Iris on small faces"). Fix: use the split on a beat where xQc speaks, or no split.
6. **Two of 8 beats (2 and 5, about 10 s of 35) have no face cam.** The brief requires a visible face cam with name; Brendaniel is also not a big face. Fanum's own "Bro, what is that?" (29.98-31.22) is a cam option for beat 5.
7. **Max-effort list is incomplete.** Not stated: per-beat YouTube phrasings for the knock-out and the quest (only Bigfoot/skunk ape/streamers searched), the check of AW's own channel for repeats (checklist §3, gate item 1), and "cost to build / what's on disk" (checklist §6; the precedent has §9). Add each as done or NOT done.
8. **"Is his #1 now" and "newest-30 median 50K"** are copied from the 17 Nov precedent, not re-read. Say "unverified" or re-read `AW-SHORTS-NOW.md`.
9. **Prediction centre (60K, above the 50K median)** sits oddly with the pitch's own weakest point (YouTube Bigfoot: 2% of videos at 100K+, best Short 0.15M, compilations about 1-2K). Add a line on why above-median.
10. **"Knocks you out cold"** is inferred from frames (a figure lying down, blurred screen, "creature's legs over him"). No in-game line says it. Hasan's own clip titles say "Bigfoot drugged" / "stole all hasan's money" (`sheet-hasan-zerodollars.jpg`, `bigfoot-clips.tsv`), so the mechanism may be knock-out + robbery. Say "blacks you out" only if a frame or line shows it. If the Short uses "drugged", the censor row changes.
11. **VIRAL-BAR B is re-defined.** B asks for a universal stake (money/career/health/status...); the pitch marks "B: universal (Bigfoot, the biggest game) ✓". Write the stake honestly as entertainment (gate I: "entertaining as a scene").
12. **Set-aside list omits HasanAbi** though §0 says 6 clips including Hasan were read; CANDIDATES lists "about 10-12 named faces" as reactors while the Short holds 3. State why the other faces are excluded (creature not on frame).
13. **Duplicate-source note.** `summit-bigfootgot1g.mp4` and `summit-bigfootjumpscare.mp4` give identical ASR (same footage); list one.

## 3. TASTE (max 3)
1. TASTE: the creature is revealed full-frame in beat 1 (Fanum), then beat 2 is "the hunt" before the creature, then beat 3 reveals it again (summit). The second reveal weakens the first; consider opening beat 2 on a beat that moves the story on (e.g. Fanum "Bro, what is that?").
2. TASTE: the title "Bigfoot Is In GTA 6" states what the button refutes. It works as a reversal but could read as clickbait; "GTA 6 Says It's Not Bigfoot" is cleaner (6 words, too long), so trim, e.g. "GTA 6's Bigfoot Isn't Bigfoot" (5 words) is the Afterhours long-form title, so it conflicts. Keep, but flag the trade.
3. TASTE: the 14.7K/h YouTube number for Bigfoot invites "why not the jet?". Lead the pitch with the one fact that really favours Bigfoot (226K shares, +41.5K in about 6 h, 13.7M on 6.5K followers) before the table.

## 4. Verdict
A stranger would follow beats 1-5 from the table (monster, hunt, walk-up, knock-out, "It's Bigfoot") but would stall at beats 6-8: "Kirk", "him", Jason and the skunk-ape joke need the quest context the table never gives, and the one-line setup for "You're saying I saw... Bigfoot?" is missing. The button does pay off the hook's claim (the game corrects "Bigfoot" in its own voice and frame-checked subtitles match), but the "then" ordering is false and the line answers a different sighting than the knock-out shown. The pick is not honestly argued against the jet: it wins only under a bar set after the data, with reactors counted unevenly, while the pitch correctly names the YouTube weakness first. Proof is thin where the brief wants it (no views per beat, Twitch clips at 1-1,453 views, one wrong number), and the max-effort statement overclaims on quotes and omits several open gate items. Frame evidence for beats 1, 3, 4, 5, 6 and 8 is solid.
