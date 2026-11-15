# FATHERHOOD-V3: beat verification for "The Dad Michael Never Had" (15 Nov 2026)

Method: local files only, no network, no playback (ffmpeg to files / `-f null`). Words = faster-whisper large-v3, CPU, one window at a time, times are SOURCE-FILE seconds
(window offset added back). Where large-v3 word times are stretched over a pause, I cross-checked the acoustic bursts (50 ms RMS) and give the burst-based in/out. Shots: scene detection
(`gt(scene,0.08)` and `0.25`) plus first/last frame of every shot in the window. Frames: `ig-mj/proof/v3_*.jpg` (each tile frame 400 px wide, label = timestamp).
H = `E:\Bullshit Folder\Henry\`.

## BREAKS THE DRAFT (read first)

1. **Hook speaker is MICHAEL, not Joe.** "And he didn't allow us to call him Daddy ... I'm Joseph to you" is Michael on camera (red shirt) in Martin Bashir's 2003 "Living with Michael Jackson"
   (same words in `H\Living With Michael Jackson 4K UPSCALE PART 3.mp4` 173.15-181.13, in the Bashir Part 3 scan). The Joe documentary's own caption card ("Joe Jackson on why he didn't allow his
   children to call him daddy", 535.5-537.37) frames it as Joe's topic. The doc edits: interviewer asks Joe "Michael was growing up. He didn't call you Pa or Daddy. He called you Joe, right?"
   -> Joe "Right." (539.94-540.06, low confidence) -> **Michael's Bashir clip as the answer** (picture: young Joe b/w still 537.37-541.87, then Michael 541.87-552.97) -> interviewer "Did you want it or
   because he was so respectful?" -> Joe on camera (553.0, ITV2 bug) answers "...he was my son and I was his father". Never describe the hook as Joe saying it.
2. **The same words are already USED** in an AW Short ("Never Hit His Kids", Bashir Part 3 ~151-195, see FATHERHOOD-BITS hard flag 1). Re-using the hook repeats published words.
3. **`Paris Jackson- I Love My Daddy So Much.mp4` is NOT the memorial.** It is a 23 s Access Hollywood home-video clip of Paris as a small child (roughly 5-7; picture = minor, audio only) thanking
   "Daddy" for a birthday cake. The memorial line ("Daddy has been the best father you could ever imagine") lives in `H\Michael Jackson Memorial Service 1958-2009 (4K).mp4` at **9525.3-9533.5**.
   The draft's PITCH row 5 points at the wrong file.
4. **Oprah window end is wrong.** 1187.80-1210.24 stops at "He's never heard me say..." (word "never" ends 1210.27). The sentence ends **1213.5** ("...I'm sorry, please don't be mad at me").
5. **Prince Sunrise 77.58-82.80:** the first 0.75 s is archive picture, then **a corrupt-decode burst 78.32-~78.9** (macroblock smear, dissolve into the studio shot; present on straight sequential decode, so
   it is in the source file). Do not use picture 78.30-79.2. Clean from 79.30.
6. **Walters "that way" = show business for his baby son** (context proven below). Safe to say "if his son wanted the stage". Not "if his son wanted to be like him in general".
7. ASR doubts: Oprah "Both. Both." (two passes disagree: one vs two "Both"); Joe doc "Right." speaker; Paris home clip 8.7-14.3 s unresolved mumble; Paris clip last line (see beat 6).

---

## BEAT 1. HOOK (Joe documentary, `My Son, Michael Jackson - Joe Jackson In His Own Words - Full Documentary (4K 2160p) - the detail..mp4`, 1920x1080 60p, 2557 s)

| Field | Value |
|---|---|
| Speaker | **Michael Jackson** (voice-over for the first ~1.6 s, on camera after 541.87). Question before it = interviewer to Joe; "Right." = probably Joe |
| Original | Bashir "Living with Michael Jackson" (aired 2003; year from the film's identity, not on any caption in the doc). The doc inserts it with no on-screen credit |
| Exact words (large-v3) | "Michael was growing up.[535.08-535.94] He didn't call you Pa or Daddy.[536.30-538.68] He called you Joe, right?[538.82-539.80] Right.[539.94-540.06?] **And[540.30] he didn't allow us to call him Daddy.[542.54] And I wanted to call him Daddy so bad.[545.16] He said,[546.40] I'm not Daddy.[547.64] I'm Joseph to you,[548.64] you know?[549.28]** Did you want it or because he was so respectful?[549.72-551.74]" |
| In -> out | **540.25 -> 548.80** (word times: "And" starts 540.30, "you" ends 548.64). The draft's 540.6 clips the start of "And he" by 0.3 s; 549.0 is inside "you know?" (cut at 548.80 to drop it) |
| Pauses | 542.54-543.02 and 545.16-546.40 (1.2 s gap before "He said"): tighten if wanted |
| Quality | -24.7 LUFS integrated over 540.3-549.3, peak -9.7 dBFS (quiet; needs about +6 dB) |
| Logo | small "d." mark top-right throughout (also 553+ with an "ITV2" bug top-left on Joe's shot) |

Shots in the window:

| Shot | Time | Picture | Minors verdict |
|---|---|---|---|
| Title card | 530.75-537.37 | black card "Joe Jackson on why he didn't allow his children to call him daddy" | none |
| Joe b/w still | 537.37-541.87 | young Joe Jackson, afro, black-and-white, small push; first frame 537.45, last frame 541.80 identical framing | adult (Joe young man); no child |
| Michael CU | 541.87-552.97 (first frame 541.95, last frame 552.90, no cut between) | Michael, red shirt, looks left, painting of nude cherubs behind head (frames show cherub legs, flag: crop or accept) | adult, no child. Cherub painting is art, not a child |
| Joe 2003 | 552.97-> | Joe in grey suit, ITV2 bug | adult |

**Alternative source (recommended for the hook picture):** `H\Living With Michael Jackson 4K UPSCALE PART 3.mp4` (1920x1080, 23.976, pillarboxed 4:3 inside the frame), ONE continuous shot, Michael alone, no logo,
-18.6 LUFS / peak -2.8 dBFS (6 dB hotter than the doc, no "d.", no Joe still over his voice). Large-v3 words: "And[173.15] he didn't allow us to call him daddy,[174.97] and I wanted to call him daddy so bad[177.67]
He said I'm not daddy.[180.11] I'm Joseph to you.[181.13] You know[181.81]". Cut 173.05 -> 181.25 (8.2 s). Frames: `proof/v3_hook_alt_bashir3.jpg` (167, 168.5, 172, 176, 181.3, 183, 186, 190: Michael alone every time).
Same words and same repeat-risk (USED). Frames of the doc version: `proof/v3_hook_joe.jpg`.

---

## BEAT 2. FEAR (`Michael Jackson - OPRAH WINFREY Interview (1993) 4K 50FPS UPSCALE.mp4`, 1440x1080 50p, 3937 s, a smooth upscale of 1993 SD)

| Field | Value |
|---|---|
| Speaker | Michael (on camera, red shirt). Oprah is off camera in the close-up: her lines are voice only |
| Exact words (large-v3) | "...um some may call it a strict disciplinarian or whatever, but he[1190.98] was very strict,[1191.56-1192.30] very hard,[1192.60-1193.16] you know,[1193.66] very stern[1194.12-1194.66] and just a look would scare you,[1195.30-1196.78] you know.[1197.00-1197.50] **Oprah:** And were you scared of him?[1197.50-1198.99] **Michael:** Very frightened.[1199.00-1200.42] There's been times when he'd come to see me and I would get sick.[1200.42-1203.52] **Oprah:** Really?[1203.52-1204.20] **Michael:** I'd start to regurgitate.[1204.20-1205.84] **Oprah:** As a child or as an adult?[1205.84-1207.60] **Michael:** Both.[1207.81-1208.15] (Both?[1208.2-1208.6, ASR doubt]) He's never heard me say this.[1209.61-1211.17] I'm sorry, please don't be mad at me.[1211.29-1213.51]" Then Oprah: "Well, I mean, I suppose that everybody has to take responsibility for what they've done in life."[1214.69-1219.31] |
| Burst-checked edges | "Some" begins about 1187.90 (silence 1187.35-1187.90); "but" 1190.62; last word "me" ends 1213.50, silence from 1213.70; Oprah's "Well" starts 1214.69 |
| Draft in -> out | 1187.80 -> 1210.24: **ends mid-sentence** (cuts "I'm sorry, please don't be mad at me"). Correct full beat: **1187.75 -> 1213.75** (26.0 s) |
| Loudness | -19.5 LUFS integrated (1186.9-1213.9), LRA 2.6, peak -5.0 dBFS |
| Logos | none visible in any frame |
| Smoothness | probable AI upscale: face is soft but no generation artefacts seen at 50 p; check per `mj-outthink-them` rule 3 |

Shots in the window (one camera move, otherwise one continuous take):

| Shot | Time | Picture | Minors verdict |
|---|---|---|---|
| Wide | before 1190.82 (incl. 1187.80) | Michael seated, red shirt, Oprah's hair/shoulder foreground left; first frame 1186.9, last frame 1190.78 | adult only, no child |
| Dissolve | 1190.82-1190.84 (2 frames, a crossfade) | wide to close-up | none |
| Close-up | 1190.84 -> 1216+ | Michael alone, red shirt, brown/yellow background; frames 1190.9, 1194.7, 1197.8, 1199, 1203, 1208.2, 1210.24, 1212 all Michael alone, eyes down at "regurgitate". At 1214-1216 he smiles as Oprah speaks | no child, no photo inserts. No children on frame anywhere |

Frames: `proof/v3_fear_oprah.jpg`. If you start at 1190.95 ("he was very strict") the cut sits on the close-up with no dissolve frames.

---

## BEAT 3. TURN (`Michael Jackson - Interview with Barbara Walters 1997.mp4`, 960x720 50p, 706 s, burned-in **RTL logo**)

Context (from the existing scan, 600-642): Walters: "Are you very involved with him? / Do you want more children? Yes. / You have been in the spotlight since you were a baby yourself. / If your son showed talent, by the way,
does he show any talent at nine months?" Michael: "When he's crying, to keep him from crying, you have to ... stand in front of him and dance ... And he stops crying. His tears turn to laughter." (Prince, born Feb 1997, so
"him" is the nine-month-old baby.) Walters then (large-v3): "Michael,[655.08] if this little boy says,[655.52-656.70] Daddy,[658.26-658.62] I want to go on the stage,[658.62-660.02] after what you've been through...[662.50-664.16]".
Michael: "Hold on now.[667.66-668.78] Hold on.[670.36-671.02] **If you do go that way,[672.04 (burst starts 672.45)-673.42] expect this, expect that, expect this, expect that.[673.50-676.82]**" Walters: "You'd lay it all out.[678.34-679.40]"
Michael: "I'd lay it all out.[679.56-680.76] You're going to get all this, and all this, and all this.[680.96-684.62] Are you ready to do that?[685.00-685.94] He says, yeah, I can't wait.[686.20-687.60] Go.[688.54-688.94]
And do it better than I did it.[690.00-691.60] But know what you're in for.[692.66-693.86] Know what you're in for.[694.16-695.12]".
(Check on the exact words: it is "Go. And do it better than I did it." with a pause after "Go", not "Go and do it".) Pause bursts: "Go" 688.25-688.55, "And do it" 688.90-689.40, "better than I did it" 690.40-691.65, "But know what you're in for. Know what you're in for." 692.60-695.50.

**"that way" = going on the stage / show business, for his baby son, and it is a hypothetical Walters put to him** ("If this little boy says, Daddy, I want to go on the stage, after what you've been through"). Michael answers as the father: I'd lay it all out; he says "I can't wait"
(the imagined boy); "Go. Do it better than I did it. But know what you're in for." Safe line: "Asked what he'd say if his baby son wanted the stage". Do not say his son actually asked, and do not say "if he follows in my footsteps" without the stage.

Speakers inside 654-696: Walters 655.08-664.2 (on camera wide), Michael 667.66-677 (CU), Walters 678.3-679.4 ("You'd lay it all out", wide shot with Michael's back), Michael 679.56-695.5 (CU).

**Tightest cut (11.7 s, both parts are the same Michael close-up shot):**
- Part A **672.40 -> 676.90** (4.5 s): "If you do go that way, expect this, expect that, expect this, expect that."
- Part B **688.20 -> 695.40** (7.2 s): "Go. And do it better than I did it. But know what you're in for. Know what you're in for."
- Cost: drops "Are you ready to do that? He says, yeah, I can't wait" (so "Go" is unprompted). Safe version adds **684.95 -> 688.20** between A and B (+3.3 s, total 15.0 s) which keeps the imagined boy's "I can't wait".
- Jump cut inside one camera (CU to CU). Picture is the same framing 672.4-695.4, so the head will jump a little on the joint; cover with a graphic or use the cut on "that." / "Go." (the pause between 676.9 and 688.2 is gone).

| Field | Value |
|---|---|
| Loudness | -18.6 LUFS (672-696), LRA 5.7, peak -2.7 dBFS |
| RTL logo | top-left, white boxed "RTL", about x 65-190, y 37-54 of the 960x720 frame (7-20 % across, 5-7.5 % down), on every shot of the window, also on Walters's shots. Crop or cover for a 9:16 reframe |
| Quality | 960x720 SD, soft; Michael's black hat shadows his eyes |

Shots (threshold 0.08; the 0.25 pass missed all of them because they are camera-to-camera cuts):

| Shot | Time | Picture | Minors |
|---|---|---|---|
| Walters CU | 639.82-641.24 | Walters speaking | adult |
| Wide | 641.24-654.70 | Michael (hat, seated, hands in lap) with Walters's back right | adult |
| Michael CU (frame before the cut) | ends 654.70 | smiling, hand to hat brim at 654.66 | adult |
| Wide, Walters on camera | 654.70-660.50 | Michael's hat/back foreground left, Walters seated centre | adult |
| **Michael CU** | **660.50-677.78** | Michael, laughing / listening; first frame 660.56, last frame 677.74 | adult |
| Wide | 677.78-680.82 | Michael's back/hand gesture foreground, Walters centre | adult |
| **Michael CU** | **680.82-702.26** | Michael; frames 688.9 and 695.6 both Michael CU (mouth open at 688.9) | adult |
| B-roll | 702.26- | dark green corridor, a hat figure from behind with entourage (outside the cut; at 700 no child recognisable, not checked past 702.3) | not cleared |

Frames: `proof/v3_walters_frames.jpg` (598.1, 600.4, 603.6, 603.74, 639.76, 639.88, 641.2, 641.3, 654.66, 654.76, 660.46, 660.56, 677.74, 677.84, 680.78, 680.88, 688.9, 695.6, 700).

## BEAT 4 (optional). "Do you like being a father?" "I love it." (same Walters file)

| Field | Value |
|---|---|
| Speaker | Walters (off camera, voice only): "Do you like being a father?"; Michael: "I love it." |
| Words (large-v3) | "why pass it on to him[596.00-597.04] do[597.04] you like being a father[598.48-599.52] I love it[599.52-600.36] are you very involved[600.36-601.68]" |
| Burst edges | question 598.05 (the "do" blip) / 598.45-599.70; answer 599.95-600.50; next question starts 601.15 |
| In -> out | **597.98 -> 600.55** (2.6 s). Do NOT start earlier: "why pass it on to him" is about the tabloids (FATHERHOOD-BITS correction) |
| Loudness | not isolated; same file, about -18.6 LUFS |
| Shots | one: Michael CU in black hat/jacket, 594.0-603.68 (first frame 598.1 neutral, last frame 600.4 grinning). Then Walters at 603.68 |
| Minors | none on frame |
| Logo | RTL top-left |

---

## BEAT 5. PAYOFF (Prince, Sunrise 2026, `projects/mj-son-red-armband/sources/uNF0GMRPO1w/uNF0GMRPO1w.mp4`, 1920x1080 25p)

| Field | Value |
|---|---|
| Speaker | Sunrise host (question, off camera) then **Prince** |
| Words | "What was he like as a dad?[77.58-78.72] Awesome.[79.38-79.80] Really fun to just spend time with.[80.12-82.80]" Then "I would love to have kids and take notes on what he did as a father but he was always on our level in a way..."[82.80-89.78] |
| In -> out | audio 77.58 -> 82.80 (5.2 s) |
| Loudness | -13.8 LUFS (77.5-83.5), peak -1.1 dBFS: hot, bring down to match |
| Logos | Sunrise lower third ("PRINCE JACKSON ON SUNRISE ..."), Channel 7 "7" bug, clock. Present on every shot |

| Shot | Time | Picture | Verdict |
|---|---|---|---|
| Archive | -78.32 | Michael in black hat and mask, an unnamed blonde woman in sunglasses, crowd behind; 77.58 and 78.26 clean | **adult only; the frame is tight and I see no child** |
| **CORRUPT** | 78.32-~78.9 | decode smear into dissolve (frames 78.32/78.36/78.40/78.44/78.48 broken); dissolve into Prince finishes by 79.3 | **do not use** (`proof/v3_payoff_glitch.jpg`, `proof/v3_payoff_glitch_seq.jpg`) |
| Prince | 78.32-82.92 | Prince, black polo, "Michael" sign behind; clean at 79.3, 80.5, 82.80, 82.88 | adult (29) |
| Wide | 82.92-87.92 | Prince and the Sunrise host | adult |
| Host | 87.92-89.72 | host listening | adult |
| Prince | 89.72-> | frame 89.66 | adult |
| **Unchecked shot 89.72-91.16** | host in navy suit, listening (frames 89.74, 90.4, 91.10), Prince's voice continues underneath ("...on our level in a way but I don't feel that he, and he made it a point..."). Cuts back to Prince at 91.16 (frame 91.20) | adult, no child, nothing odd (Sunrise lower third and bug only) |

Recommendation: use audio 77.58-82.80 with a J-cut: picture 77.58-78.30 archive (clean) then hold on Prince from 79.30 under the end of the question, or start at "Awesome" **79.30 -> 82.85** (3.55 s) and let the question be implied. Frames: `proof/v3_payoff_prince.jpg`, `proof/v3_payoff_clean.jpg`.

---

## BEAT 6. CLOSE

### 6a. `Paris Jackson- I Love My Daddy So Much.mp4` (640x480 30p, 23.0 s) is a **child home video, not the memorial**

| Field | Value |
|---|---|
| Who | a small girl (Paris as a child, about 5-7; the file name and an Access Hollywood caption say Paris). Picture is a minor: AUDIO ONLY |
| Exact words (large-v3) | "Daddy,[0.00-0.48] thank you for my birthday cake,[0.60-3.72] and I love you so much,[4.02-6.72] and I love my daddy so much.[6.92 ... 'love' stretched 8.74-14.28 ... my 14.28, daddy 14.52-14.88, so much 15.20-15.90] **You're the best daddy in the whole world.**[16.52-18.80] Thank you.[19.18-20.42] I love you more, Daddy.[20.86-22.64]" |
| ASR doubts | (i) 7.6-14.3 s is a rambling/mumbled stretch (ASR collapses it to one stretched "love"); (ii) **the last line**: the burned caption on screen from ~21 s reads "thank you, I love you more, paris", so the last word is **"Paris"** and the speaker is the voice replying to her (adult, unseen), not Paris saying "Daddy". The pitch of that line (about 240 Hz) is no clearer than her own (260-300 Hz). Ear-check before any use |
| Clean usable line | "You're the best daddy in the whole world." **16.50 -> 18.85** (2.35 s), or "Daddy, thank you for my birthday cake, and I love you so much" 0.00 -> 6.80 |
| Loudness | -27.8 LUFS, peak -15.7 dBFS: very quiet, needs about +10 dB |
| Logo | "Access Hollywood" star bottom-left on every frame, 640x480 SD |
| Shots | scene cuts at 16.47 and 19.03 (zoom changes). Child Paris in white headband and pyjamas throughout, arms up at 14.6-22.8. Whole clip = a minor: never on frame |
| Who else | nobody on screen; one off-screen voice at the end |

Frames: `proof/v3_close_paris.jpg`.

### 6b. The real memorial moment: `Michael Jackson Memorial Service 1958-2009 (4K).mp4` (1920x1080 60p, 9825.6 s)

| Field | Value |
|---|---|
| Speaker | **Paris** (11), the line is hers; **an adult** prompts her. Janet is next to her on camera (a prior brief names her as the prompter; I have not matched the voice) |
| Exact words (large-v3, VAD off) | Paris: "I just wanted to say...[9519.38-9521.54] **Adult:** Speak up, sweetheart. Speak up.[9521.54-9523.42] And get close.[9524.26-9525.26] **Paris:** Ever since I was born,[9525.30-9526.66] (sob pause 9527.5-9529.7) Daddy has been the best father you could ever imagine.[9529.30-9533.30] (9533.6-9540: crying) And I just wanted to say I love him so much.[9540.34-9544.70]" Then "Thank you."[9545-9548] |
| Tight in -> out | **9525.27 -> 9527.20 + 9529.62 -> 9533.55** ("Ever since I was born, ... Daddy has been the best father you could ever imagine", 5.9 s with the pause removed), or the whole 9525.27 -> 9533.55 (8.3 s). Optional "And I just wanted to say I love him so much" **9540.30 -> 9544.75** (4.5 s) |
| Loudness | -14.6 LUFS integrated (9520-9534), LRA 6.0, peak -0.4 dBFS (9520-9545: -15.0, LRA 11.6). It is 13.2 LU hotter than the home clip, and ambient crowd noise sits near -45 dB between words |
| Picture / logos | CBS News "Michael Jackson: The Farewell / CBS News Special Report" then "PARIS MICHAEL KATHERINE JACKSON, Michael Jackson's Daughter" lower third, red CBS "LIVE" bug, cbsnews.com. No scene cuts at the 0.1 level (one continuous moving shot) |
| On screen | Paris at the mic (11, crying), Janet beside her in black hat/pearls/sunglasses, men in dark suits behind (unnamed), at 9538-9544 a boy at the right edge (a minor, probably Prince, 12). **Whole picture = children: AUDIO ONLY** |

Frames: `proof/v3_close_memorial.jpg` (9519, 9523, 9527, 9531, 9534, 9538, 9541, 9544, 9547).

Loudness comparison: memorial -14.6 LUFS (peak -0.4) vs home video -27.8 LUFS (peak -15.7). The memorial is the stronger and the louder audio, but it carries crowd noise; the home video is dry and clean but tiny and low-fi.

---

## BEAT 7. OTHER TELLINGS (existing scans only)

**"I'm Joseph to you" (Janet).** `H\Janet-Jackson-SnapYT.App.mp4`, scan `Janet_Jackson_SnapYT_App_mp4.json`:
- 1321.0 "I would go over a friend's house when when mother would let me go"; 1328.3 "And I'd see my friends the relationship with their father"; 1332.8 "How they call him dad and"; 1335.8 "Sit on their lap and what do you call him Joseph? What was that done?" (interviewer)
- **1341.2-1350.1: "One time I tried to call him down. What happened? He said no, I said I'm Joseph you call me Joseph. I'm Joseph to you"** (ASR garbled: "call him down" is almost certainly "call him daddy/dad"; "He said no, I said" is "He said no, I'm Joseph, you call me Joseph"; interviewer's "What happened?" is inside the window)
- 1350.1 "So your father tells you one time, you don't do it again."; 1356.7 "So I've always called him Joseph."
- The same Janet account is quoted back to Joe by Piers in `Michael_Jackson_s_Father_Joe_Jackson_Piers_Morgan_Interview` scan 153.6-181.3 ("I'm Joseph dear ... why wouldn't you let your daughter call you dad?"), and Joe answers 181.3-198.3: "Well you had all those kids running hollering around and hollering dad dad dad, you know, it gets to be sounds kind of funny to me, but I didn't care too much about what they called me." (the same answer is in the Joe doc at 561.9-573.3). So Joe's own on-record answer to the "Daddy" story exists.
**Michael's own tellings of "Daddy/Joseph":** only Bashir 2003 Part 3 (173.15-181.13, USED) and its re-use in the Joe doc. No other Michael telling in any scan (no hit in Oprah 1993, Walters 1997, 60 Minutes, Lisa Marie, Take Two). Also Bashir Part 3 ~183: "I totally forgive him" and 189.5 "I don't allow my children to call me Michael. I say I'm daddy" (the father he chose to be, same file: USED).
**Prince on Michael as a dad** (`Prince_Jackson_Opens_Up...` KIIS scan; picture is a KIIS interview with KIIS-FM logo): 1043.1 question "Did you call him Joseph or Granddad?" -> **1044.8-1052.9 "I was lucky enough to call him Grandpa. I think later in life, my Grandpa kind of softened up a little bit and realized the error of his ways."** (Prince on Joe, strong for the arc); 1402.7-1410.0 "We took a lot of walks. We would go out in nature ... walks on the beach in the Middle East. We take a lot of walks through forests in Ireland."; 1424.7-1430.4 "spending a lot of time outside playing tag, or hide and seek, hiding behind trees and stuff."; 1436.2-1438.5 "it's shutting down toy stores."; 994.1-998.1 "that I had heard about my dad, we almost never hugged my grandpa." (check context); 252.0 "someone always has a story about my dad". Sunrise has the cleaner dad answers (beat 5).
**Paris on Michael as a dad** (`Paris_Jackson_First_Interview_about_Michael_Part_01` scan; she is about 14-15 in the picture: AUDIO ONLY): 574.2 "What kind of dad was he?" -> **576.9-581.1 "I can't imagine anyone having a dad not like him." 581.1 "He was just amazing." 586.6 "He was kind and just like the sweetest guy ever."**; 489.7-502.4 "there were a lot in Bahrain where we would like hang out on the roof or we were just like in Ireland, me and him went walking through the forest and it was just fun."; 507.3 "he was happiest when he was like in disguise ... we went to Disneyland several times". No other Paris scan JSONs exist for the adult interviews (Zane Lowe, Oprah, Red Table Talk are on E: but unscanned).

---

## PROPOSED CUT LIST (about 47.9 s, picture adult-only, children AUDIO ONLY)

| # | Beat | Source (in -> out) | Dur | Words | Picture |
|---|---|---|---|---|---|
| 1 | Hook | Bashir Part 3 `173.05 -> 181.25` (or Joe doc `540.25 -> 548.80`) | 8.2 | "And he didn't allow us to call him Daddy. And I wanted to call him Daddy so bad. He said, I'm not Daddy. I'm Joseph to you." (Michael) | Michael CU, one shot. Caption it "Michael, on his father" |
| 2 | Fear (lean) | Oprah `1190.95 -> 1200.10`, `1200.12 -> 1203.60`, `1209.55 -> 1213.75` | 16.8 | "he was very strict, very hard, you know, very stern and just a look would scare you, you know. [Oprah: And were you scared of him?] Very frightened. There's been times when he'd come to see me and I would get sick. ... He's never heard me say this. I'm sorry, please don't be mad at me." | Michael CU, one shot |
| 2b | Fear (full alt) | Oprah `1187.75 -> 1213.75` per the segment plan: `1190.95-1200.10`, `1200.12-1208.85`, `1209.55-1213.75` | 22.1 | adds "I'd start to regurgitate. [As a child or as an adult?] Both. Both." (ASR doubt on the second "Both") | same |
| 3 | Turn | Walters `672.40 -> 676.90` + `688.20 -> 695.40` | 11.7 | "If you do go that way, expect this, expect that, expect this, expect that. ... Go. And do it better than I did it. But know what you're in for. Know what you're in for." Frame it on screen as "asked if his baby son wanted the stage" | Michael CU (RTL logo top-left: crop) |
| 3b | Optional | Walters `597.98 -> 600.55` | 2.6 | "Do you like being a father? I love it." | Michael CU, grin. Put it before 3 if the cut has room |
| 4 | Payoff | Sunrise audio `77.58 -> 82.80`; picture: archive 77.58-78.30 then Prince from 79.30 | 5.3 | "What was he like as a dad? Awesome. Really fun to just spend time with." | adult Prince; avoid 78.30-79.2 |
| 5 | Close | Memorial audio `9525.27 -> 9527.20` + `9529.62 -> 9533.55` | 5.9 | "Ever since I was born, Daddy has been the best father you could ever imagine." | **no memorial picture** (Paris 11 and Prince 12 on frame); lay it under an adult picture of Prince, or the Sunrise shot |

Total with 1 + 2 + 3 + 4 + 5 = 8.2 + 16.8 + 11.7 + 5.3 + 5.9 = **47.9 s**. With 2b the cut is 53.2 s (drop beat 4's question or the optional lines). With 3b it is 50.5 s.
Bookend note: the hook has "Daddy" within 2.3 s of the start; the close has "Daddy" mid-line and ends on "imagine". For an ending ON "Daddy", the only clean candidate is the child home clip "You're the best daddy in the whole world" (16.50-18.85, minor audio only, -27.8 LUFS), which ends on "world".
Audio chain: Joe doc -24.7 / Oprah -19.5 / Walters -18.6 / Sunrise -13.8 / memorial -14.6 / Bashir -18.6 LUFS: level each to one target before the static limiter.

## FRAME PROOF (all under `ig-mj/proof/`)
v3_hook_joe.jpg, v3_hook_alt_bashir3.jpg, v3_fear_oprah.jpg, v3_walters_frames.jpg, v3_payoff_prince.jpg, v3_payoff_glitch.jpg, v3_payoff_glitch_seq.jpg, v3_payoff_clean.jpg, v3_close_paris.jpg, v3_close_memorial.jpg
