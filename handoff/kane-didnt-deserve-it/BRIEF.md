# BRIEF: "Why They Said Harry Kane Didn't Deserve The Ballon d'Or 😳" (Abundance Wisdom short, football)

## ▶ STATUS: resume here (2026-10-29 ~19:30 PST): DELIVERED v2 (Final Renders + Exports), waiting on his review
- Built in code on his "start" + "handle everything yourself" (18:15). State + recipe: RUN.md. Report: REPORT.md.

## (previous) STATUS (2026-10-29 ~17:30 PST): HIS TELLA DIRECTION RESOLVED → waiting on his footage + 2 answers
- His walkthrough (https://www.tella.tv/video/affans-video-f4hkf37h, "Harry Kane Video Editing Instructions", 9:11,
  recorded 16:35) is resolved against his timeline in **§ HIS DIRECTION** below. His re-cut is the spec (41.55 s,
  `premiere/his_v1_edl.md`).
- Waiting on him: (1) **kids overlay vs the brief's hard rule 5** (no minors), (2) **is the smiling blonde woman his wife**
  (`proof/wife_candidates.jpg`), (3) **downloads** for the kick, goal and trophy overlays (§ Open with Affan, round 3).
- Then the code build (RUN.md § NEXT). Nothing touched in ABW10 since his save; his sequence was only READ.

## HIS DIRECTION (Tella, 2026-10-29 16:35), resolved against his timeline
Ingest: `review/guide.mp4` (Tella stream, never the browser) → `review/guide.json` (`win/asr_guide.py`, GPU; 338-444 s
re-run without VAD, the first pass hallucinated there). Every "this / here" was read off his timeline at the moment he said
it: `review/frames/tr_*.png` (transitions), `zm_*.png` (zooms), `pm_*.png` (overlays, program monitor), built by
`win/tl_sheet.py` / `win/pm_sheet.py`. Timeline TC is 60 fps (`ss:ff`, ff/60).

**The cut = his re-edit** (read back read-only, `premiere/readback_all.js` → `his_v1.tsv` → `his_v1_edl.md`; true out =
in + span, Premiere's outPoint reads ~0.19 s late). **41.55 s**. Changes vs my raw cut: B1 starts on "He's" at 61.35 /
63.35; B3 tail to 102.05; B5 first piece to 203.40, last to 206.37; B6 second piece from 557.22 ("Harry's the top man");
B7 restructured: "...behind the scenes. All that sacrifice (73.80-74.80), the time that, I'd love to be spending with my
kids, with my family and my wife, but it's all part of the dedication if you want to be at the very top level" (ends
85.12; "saunas, ice baths" and "some time and things" out); **B8 = "Here it is. We've done it" (549.80-551.30, no "So,")**;
my B7 Ronaldo cover removed. Words re-ASR'd from his rebuilt A1: `win/verify_his.py` → `seqref/his_a1.wav`.
Runtime is under the brief's 48-55 s and B8 lost "So,": both his edit, noted once, not re-asked.

**1. Lip sync** ("the lips need to be synced… the lips and the audio are kind of not synced", said on B1).
Measured on ASH at three bilabials (`win/plosive_check.py`, mouth tiles + 5 ms energy; word times from `win/force_align.py`):
"Ballon" b closure audio 61.73-61.77 vs lips 61.52-61.58; "my" m audio ~63.53-63.57 vs lips ~63.36-63.40; "opinion" p audio
63.76-63.84 vs lips 63.60-63.68 → **ASH picture runs ~0.16-0.20 s AHEAD of its audio** (zero offset is contradicted at all
three: open teeth on every audio closure). Container start times are all 0. **Fix in the build: ASH picture in = audio in −
~0.17 s** (tune on re-tiled frames). **BAYERN (the B8 payoff picture) is in sync:** "my biggest" m closure audio
646.62-646.66 vs lips 646.60-646.68 (`review/frames/bay_biggest.png`; the B8 cover is synced to SPEECH by audio xcorr, so
BAYERN's own A/V is what matters). The other talkers (UNCLE, BRAZ, TS, SKY) get the same plosive check before render.
**2. Uncle (B2):** "make sure that it's head tracked" → head lock on the three uncle pieces (handheld; he hand-split 3.88-4.28
to reframe); "this is Spanish, do your due diligence" → the B2 English captions checked word by word against the Spanish.

**3. Overlays.** V2 slots = face clips he dragged up to V2 (replace their picture, keep the audio below). The BAYERN clips
on V2 are real picture and stay.
| slot | timeline (s) | words | picture | zoom |
|---|---|---|---|---|
| O1 | 5.88-7.23 | "There's nothing he does that" | NEW: **4K full-screen (not letterbox) Kane mid-kick** | out |
| O2 | 12.52-14.33 | "and a London-born player won" | BAYERN 8.20 hands-to-face, **his reposition** (x 0.61), "like this or zoomed in more" | out |
| O3 | 23.77-25.30 | "People see the end product" | **him receiving the Ballon d'Or** (BAYERN 51.52-57.80, Ronaldo hands it over) | out |
| O4 | 25.30-26.52 | "they see me scoring goals" | NEW: **his most famous goal, slow motion** | out |
| O5 | 26.52-29.38 | "on the pitch… winning games and trophies, but" | NEW: **Kane holding a TEAM trophy, slow motion** ("not slow motion… actually do slow motion": last word wins); NOT Ballon d'Or footage | one zoom out across |
| O6 | 33.47-36.17 | "the time that I'd love to be spending with my kids, with my family and" | NEW: **Kane with his kids, playing, having a good time** (conflicts with hard rule 5, asked) | one zoom out |
| O7 | 36.17-37.87 | "my wife, but it's all part of" | **his wife in the audience smiling, looking at him** (he extended this slot past the V1 cut to 37.87) | out |
| B8 | 40.05-41.55 | "Here it is. We've done it" | BAYERN synced lectern (656.43), **zoom out, no overlay on top** | out |
Face shots he wants as they are: "his actual overlay" = Kane's own face from 37.87 ("very top level").

**4. Zooms** (one continuous move per group, across the joints, never per-clip keys):
B1 0-1.95 in · B2 1.95-5.88 one stretched OUT · O1 out · B3 7.23-9.80 in · B4 9.80-12.77 in · O2 out · B5 14.33-17.43 in ·
B6 17.43-23.77 one stretched in · O3 out · O4 out (the VAD pass heard "zoom on"; settled by MFCC-DTW against his own 14
clear "zoom in/out" takes, 12/14 leave-one-out correct: O3 out by 0.25, O4 out by 0.11; every overlay he named zooms out) · O5 out · B7 face 29.38-33.47 in · O6 out · O7 out · B7 face 37.87-40.05 in · B8 out.

**5. Transitions** = his label-colour code (README § transitions: **Purple** −90 brightness dip · **Dark Green** +30 flash ·
**Peach** uni.Exposure Blur 50→0 over 0.5 s · **Cyan** Gaussian Blur 50→0 over 0.7 s). Where he corrected himself, the last
word wins. Every cut he did not name stays a straight cut (B1 1.15, B2 3.88/4.28, B3 8.62, B5 15.13/16.38, B7 32.47).
| # | cut (s) | from → into | colour |
|---|---|---|---|
| 1 | 1.95 | ASH → UNCLE | purple |
| 2 | 5.88 | UNCLE → O1 kick | peach |
| 3 | 7.23 | O1 → ASH | cyan |
| 4 | 9.80 | ASH → BRAZ host | purple |
| 5 | 10.17 | BRAZ → BRAZ (jump) | dark green |
| 6 | 12.52 | BRAZ → O2 hands-to-face | dark green |
| 7 | 14.33 | O2 → TS | purple |
| 8 | 17.43 | TS → Alan Brazil | dark green |
| 9 | 19.58 | Brazil → Brazil (jump) | dark green |
| 10 | 23.77 | Brazil → O3 award | peach |
| 11 | 25.30 | O3 → O4 goal | cyan |
| 12 | 26.52 | O4 → O5 trophy | cyan |
| 13 | 29.38 | O5 → Kane face | purple |
| 14 | 33.47 | Kane face → O6 kids | purple |
| 15 | 36.17 | O6 → O7 wife | cyan |
| 16 | 37.87 | O7 → Kane face | cyan |
| 17 | 40.05 | Kane face → B8 lectern | dark green |

**6. Captions:** "not just white and red": white + blue, white + pink, white + green… varied through the short, **gradient
styles, never flat** (README § 8 "Colour MIX", the same rule he gave on Katherine today). Height stays his y≈1060.
**Everything he did not mention stays as the brief says:** grade (B1-5 cold/desat, B6-8 warm from B6's first frame), labels,
−14 LUFS / ≤ −1 dBTP, no music, export to both paths.

## Catalog pass (CLAUDE.md learning loop: required before any edit)
Done 2026-10-29 ~18:15: all 151 lines of `research/effects-catalog/CATALOG.md` read and all 137 stills looked at (the
contact sheets `projects/janet-couldnt-cry/win/cat/cat_0-6.jpg`). His direction names every overlay, zoom and
transition, so the catalog only shapes HOW those land, never adds moves.
- **Fits, used inside his direction:**
  - FX-77 Clock in Flight + FX-78 Cinema Vignette Montage → his slow-motion goal and trophy overlays (O4, O5) as true slow
    motion with a soft oval vignette and crushed blacks, warm-dark (they sit after the B6 grade switch).
  - FX-50 Filmography Mirror → the kick, goal, trophy and award overlays are his own career footage cut in as his life
    while he talks about it.
  - FX-40 Slow-Burn Portrait → his zoom-in groups on Kane's own close-ups (slow creep, no text).
- **Fits, held back (his look is set):** FX-42 Kin Tag (the AW labels stay); FX-37 Ghost Dissolve and FX-38 Hard Push
  Slide (he named every transition); FX-58 Speaker-Coded Subs (AW captions are locked); FX-75 Scorebug Punch-In (no score
  story here).
- **New to the channel here:** native-60 fps slow motion (O1/O4 from the 1440p60 pack: no interpolated frames) with the
  FX-78 vignette.
- **Doesn't fit a 42 s face-led short:** maps, charts, documents, host sets, CG, chapter cards, CRT/phone props, stepped
  motion (FX-01–13, 15–36, 41, 43–49, 51–76, 79–81).
- **What the last one leaned on (Janet):** label transitions, the SD letterbox over a blurred fill, a greyed-out still-like
  overlay, four ≥1080p moving overlays. **This one is better by:** five moving overlays, two in native-60 fps slow motion;
  a measured A/V offset fixed at the source (Ashton's lips land on his words); the two-phase grade carries the story turn
  (cold doubters → warm answer on B6's first frame).

## HIS ANSWER, round 4 (2026-10-29 ~23:00): "Use the kids"
- Hard rule 5 is lifted for **O6 only**: Kane with his kids, playing (his Tella). Source: his download of
  https://www.youtube.com/watch?v=WSBoUJE9kjw (Kane kicks a ball with his son on the Allianz Arena pitch, 2026 title);
  alt https://www.youtube.com/watch?v=Gsj5-l9ZdKE. Wife (O7): CONFIRMED by him 2026-10-30 ("Yes, that's her"). State: RUN.md.
- 23:15 he downloaded it ("done") and added: **"if its low quality do letterbox format on it"**. It is (a fan's zoomed
  phone shot, 1080p30 at 1.6 Mb/s): O6 = his letterbox (native 100 %, 1044 px band lifted 150 px, blurred 220 % twin,
  glow bars), source 9.20-11.63 at 0.9x (his son dribbles, Kane points, they meet).

## Open with Affan, round 3 (2026-10-29 ~17:30)
1. **Kids overlay (O6) vs the brief's hard rule 5** ("No minors on frame. No Kane children"; beat 7 also says "No footage
   of his children"). Default: **hold O6 until he answers**; if the rule stands, O6 = Kane with Kate / family adults.
2. **O7: is she his wife?** BAYERN cuts to a blonde woman in the stalls at 10:32, 10:41-10:44, **10:50-10:54 (big smile,
   default)**, 10:59-11:02 (`proof/wife_candidates.jpg`). No children in those frames.
3. **Downloads (SnapDownloader, highest quality, 2160p where offered; YouTube is still blocked for me):**
   - O1 kick: https://www.youtube.com/watch?v=79oXmnxr2uk ("Harry Kane England 2026 Free Clips Pack, 4K UHD"); alt
     https://www.youtube.com/watch?v=1FToxy5aoj0 (4K, upscaled).
   - O4 goal: the halfway-line goal v Darmstadt (28 Oct 2023), https://www.youtube.com/watch?v=OM8hOlK9hPs ("Kane scores
     from OWN half!"); alt https://www.youtube.com/watch?v=9jqtkyvYJJk. Alt goal: the DFB-Pokal final spin-and-finish (23 May 2026).
   - O5 team trophy: DFB-Pokal 2026 lift, https://www.youtube.com/watch?v=2W8B6LwyAd0 ("FULL CEREMONY, Harry Kane & FC Bayern
     lift the DFB-Pokal"); alt his FIRST trophy, the 2025 Meisterschale, https://www.youtube.com/watch?v=Uf5lttOj8tw. Every
     frame I use gets checked for children (his kids were on the pitch at the 2025 celebration).
   - O6 kids: only after (1).
   - **18:10 his reply: OM8hOlK9hPs (goal) and 2W8B6LwyAd0 (DFB-Pokal ceremony) are "unavailable in my country"**; the rest
     are downloading (the 4K kick pack is already in `E:\Bullshit Folder\Henry\`, .mkv). Replacements sent: goal
     https://www.youtube.com/watch?v=9jqtkyvYJJk (beIN) → https://www.youtube.com/watch?v=b_TmJoQvwvc → full 8-0 highlights
     https://www.youtube.com/watch?v=xwK0qaa1ZiM; trophy https://www.youtube.com/watch?v=Cjfi6xRSfGE (FC Bayern's own
     "KANE HAT-TRICK WINS US THE CUP!", lift expected near the end) → https://www.youtube.com/watch?v=BNjuFmupf1Q → the 2025
     Meisterschale alt Uf5lttOj8tw. Channel geo-blocks can't be checked from here (YouTube is blocked for me, never bypassed).
4. Cost: this ingest ~1 %; the build with the new overlays, slow motion (Topaz interpolation), 17 transitions, the zoom
   groups and the lip-sync fix ≈ **5-6 % (~$110-135)**, up from the 4-5 % quoted before his direction.

## (previous) ▶ STATUS: resume here (2026-10-29 ~14:55 PST): RAW SEQUENCE PLACED (48.70 s), waiting on his pass + direction
- All his answers are below (§ HIS ANSWER to round 2 + his "Yes, short" = B8 on FC Bayern's synced picture, short
  version, Ashton's own line for the hook). State + next steps: RUN.md.

## (previous) ▶ STATUS: resume here (2026-10-29 12:45 PST): YOUTUBE BLOCKED 7 of 8 downloads → waiting on his files (RUN.md)
- His answers are in § HIS ANSWERS. The yt-dlp run hit YouTube's bot check; only TS came down, and only at 640x360.

## (previous) STATUS (2026-10-29 12:35 PST): WAITING ON AFFAN (§ Open with Affan), nothing downloaded or built
- Brief received, locked 29 Oct 2026 (verbatim copy at the bottom; his file:
  `X:\Claude Projects\Abundance Wisdom\KANE-EDITOR.md`, 12:21. The earlier v3 draft `KANE-1-OUT-OF-10-CUT.md` is
  background only: it names the uncle "Abdul" and says the upload window is **today, 29 Oct**).
- Questions 1–4 below went to him in the first reply. Nothing touched in ABW10 / ABW9, nothing fetched from YouTube.
- Next on his answers: download (brief § 2 commands, plain) → probe every source (resolution, fps, `idet`, audio) →
  window ASR per beat → lock ins/outs by ear → runtime sum → (raw sequence in ABW10 or code build, per his answer 4).

## HIS ANSWER to round 2 (2026-10-29 ~14:45)
- "the source videos are very weak"; his worry = the payoff (B8) if it is the AS looped still. Rule he gave: **keep the
  audio, swap the video for something that portrays the same message** wherever a picture is weak.
- B8: shown `proof/b8_as_vs_bayern.jpg` (FC Bayern's download = the real broadcast of the same speech, synced, with
  the cutaways to the woman in the stalls during the wife lines). Waiting on his OK + short vs Kate; B1 hook still open.

## Open with Affan, round 2 (asked 2026-10-29 ~14:30; evidence in RUN.md § findings)
1. **B1 hook is not Ashton's voice.** "Harry Kane's not a Ballon d'Or winner" (his file *Dean Ashton OUTLINES…*, 1:04-1:06)
   is someone else echoing him: Ashton's lips are closed through "not a Ballon d'Or winner", the pitch jumps, the
   director cuts away at 1:05.3. → Default: **Ashton's own line, "He's not a Ballon d'Or winner, in my opinion"**
   (1:00.9-1:03.8, frame 1 on "he's"). Red words unchanged. The name "Harry Kane" leaves the hook (label + chyron carry it).
2. **B8 picture.** The AS speech upload has no real picture (one looped stage shot + a waveform graphic over Kane).
   → Default: **FC Bayern's broadcast picture of the same moment**, synced (+106.66 s), under the AS audio (uses BAYERN
   beyond "B-roll only"). Version: **short** (~53 s total) unless he wants the "To my wife Kate" opening (~56 s). The
   broadcast cuts to a woman in the stalls at BAYERN 10:41-10:44 (on "my best friend" in the Kate version): he confirms
   who she is.
3. **B2 Yamal's face.** REACT is a fan's wide phone video of the stalls; no usable close-up of one face. → He gives a
   timestamp (REACT or BAYERN), or skip (uncle holds the whole beat). Default until then: uncle holds.
4. **B4 Guti photo.** No source on disk. → He drops one in `E:\Bullshit Folder`, or OKs fetching one from Wikimedia
   Commons. Default: a placeholder slot in the raw sequence.
5. **B7 part A picture.** Sky's own package puts arrival B-roll (Kane + entourage, crowd, dark) under "people see the end
   product … trophies" (0:50.2-0:57.0); Kane on camera from "but it's very rare". → Default: keep the broadcast's picture.
- Stated, no answer needed: B6 speaker = Alan Brazil (answers "Alan, would you knight Harry Kane?" on camera, 13:32-13:36);
  B6 caption "Harry's **the** top man" (as said); B8 "We done it" is what he says (acoustic fit beats "we've"); B6 opens
  with a 1-frame J-cut (he starts "Get" 20 ms before the camera cuts to him) so no frame of the presenter shows; Sky
  carries a low tonal bed under Kane's pauses (~20 dB under his voice; every joint crossfaded 2-4 frames); Guti's own
  clip not searched (YouTube bot-blocked); runtime ~53 s.

## HIS ANSWERS (2026-10-29 ~12:40, "Yes, defaults")
1. **No music bed** (SFX policy as on Janet/Joe). The beat-6 "music stop" box is N/A; the turn = hard cut + grade switch.
2. **Run the brief's yt-dlp commands once, plain** (he gave the go on the sources as linked).
3. **Captions at HIS height (y≈1060, on the speaker's lip line)**, not the brief's 62–68 %.
4. **Raw sequence in ABW10 first** → his re-edit + direction → code build.

## Open with Affan (asked in the first reply, 2026-10-29; ANSWERED above)
1. **Music.** § 5 scores a tense bed under 1–5, a hard stop on 6, a warm bed under 7. His 2026-10-27 rule: AW code-built
   shorts ship with NO music bed even when the brief names one (Flex and Janet both got "no music"). → Default: **no bed**.
   Then the beat-6 QA box "music stop" can't be ticked as written; the turn rests on the hard cut + the grade switch.
   Or he says "build the beds this time" (Epidemic, ~−28 dB, hard stop on 6, out under 8).
2. **Sources.** Links + risk flags below. Ask: go/no-go on quality (Flex lesson), and a yes to run the brief's yt-dlp
   commands once, plain (no cookies / proxies; worked for Janet on 10-28). Otherwise he drops the files in
   `E:\Bullshit Folder`.
3. **Caption height.** § 6 says ~62–68 % of the frame. Janet v1 was built at the brief's 64 % and his review moved the line
   up to his mouse at y≈1060 (55 %): "all of these things are placed too low just because the captions are placed too
   low". LESSONS 2026-10-28: a brief's % does not override his own position. → Default: **his height (y≈1060, on the
   speaker's lip line)**; still inside § 6's safe zones (bottom 20 % starts at y1536).
4. **Order.** His standing order (Joe, Janet, Flex): raw sequence in ABW10 → his re-edit + Tella direction → code build.
   This brief says "cut it exactly as written" and the v3 draft says upload today. → Default: **raw sequence in ABW10
   first**; or straight code build to the export if he wants it today.
- Not questions (stated): export = `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Kane Didnt Deserve It.mov`
  **and** an identical copy in `X:\Claude Projects\Exports\` (his no-C rule). Beat 4 upgrade: Guti's own El Chiringuito
  clip NOT found yet (articles only: Maxifoot, Foot Africa, El Gol Digital, footballtransfers); El Chiringuito's own
  channel gets checked once downloads are a yes. Beat 4 stays the talkSPORT host's report until then.

## Cost quote (his paid usage; 1 % of the week ≈ $22)
- Intake (8 sources) + probes + window transcripts + the Spanish line + ins/outs locked by ear + locks + raw sequence in
  ABW10: about **2–2.5 % (~$45–55)**.
- Code build (full-bleed reframes, Topaz on the SD ones, the two-phase grade, labels/cards, captions incl. beat 2's
  bigger two-line English, audio to −14 LUFS, test frames of every shot, export, § 9 report): about **4–5 % (~$90–120)**,
  as Joe and Janet.
- Music beds only if he asks (Epidemic search + placement): +0.3 %. Higgsfield only if a still is soft (ask first).

## Sources (brief § 2) and risk flags (judged from title/channel/date only; nothing probed yet)
| Code | Link | Use | Flag |
|---|---|---|---|
| ASH | https://www.youtube.com/watch?v=jQFm0ppDbpc | 1, 3 | low: talkSPORT studio, 26 Oct |
| UNCLE | https://www.youtube.com/watch?v=I2Bmkq5_xLo | 2 | **noisy bar under the voice; small 100 s AS upload, possibly phone footage** |
| BRAZ | https://www.youtube.com/watch?v=h6jag7BsM8I | 4, 6 | medium: long show upload (~14 min), studio two-shots; voice in 6 to confirm as Brazil |
| TS | https://www.youtube.com/watch?v=ZO5OaOYGLq0 | 5 | **2024 upload, the brief calls it SD** |
| SKY | https://www.youtube.com/watch?v=LiysaNUZpx0 | 7 | low: Sky Sports News; presenters' audio excluded |
| SPEECH | https://www.youtube.com/watch?v=o0JdYVpXoQY | 8 | medium: AS re-upload of the broadcast (bug / watermark?) |
| BAYERN | https://www.youtube.com/watch?v=407tY1wz-w0 | B-roll 4, 7 | low: FC Bayern official |
| REACT | https://www.youtube.com/watch?v=8a5ukyzTLlc | B-roll 2 (≤ 1.5 s) | **fan channel: watermark / low res / mirrored risk** |

## Checks to run right after transcription (before any placement)
- **Runtime arithmetic.** The brief's nominal ranges sum to ~64 s (4+7+8+4+7+7+23+4), over the 60 s hard max. Beat 7
  alone is ~23 s and its "…" hide words. Sum the words locked by ear; if filler-only trims still leave > 55 / 60 s, STOP
  and ask him which words go (rule 3 forbids meaning splices). The "To my wife Kate" +3 s option only if it fits.
- **Full bleed, no letterbox, no blur (§ 4).** Probe every source's resolution; an SD 16:9 source that can't fill 9:16
  within ~115 % of its fill scale is a "can't do as written" flag. Crop sheet before placing (studio two-shots fool the
  face detector: Derek lesson).
- **Rule 5 (no minors) on beats 7–8:** every frame of any audience / wife cutaway checked for the Kane children.
- **Interlacing:** `idet` on every broadcast / ceremony source (Derek lesson: bwdif if combed).
- **Beat 6 voice:** confirm by ear + frame that it is Alan Brazil; else the label changes to the real name.
- **Beat 2 translation:** the brief's English is given; caption it verbatim, English only, two lines, bigger.
- **Promo frames / pauses:** no 1–2 frame promo at clip edges; no gap > ~0.25 s (rule 1, stricter than his 2 s rule).

## Standing rules on this job
- Work in silence (no players, ffmpeg to `-f null`, no browser media tabs). Never save or export his Premiere / AE
  projects. Censor drug / self-harm words (none expected here). No Fable subagents. Quote cost before heavy steps. His
  review notes → `presets/youtube-shorts/abundance-wisdom/LESSONS.md`. Other sessions' jobs (Katherine, Janet, Derek,
  …) and their sequences are off limits.

---

## THE LOCKED BRIEF (verbatim)

# EDITOR BRIEF: "WHY THEY SAID HARRY KANE DIDN'T DESERVE THE BALLON D'OR 😳"
**Channel:** Abundance Wisdom · **Format:** YouTube Short, 1080×1920 · **Locked:** 29 Oct 2026

The creative is locked. Your job is to cut it exactly as written. **If anything can't be done exactly as written, stop and tell Affan before improvising.**

**What this Short is:** the doubters escalate (a pundit, Yamal's family, a Real Madrid legend's conspiracy theory, a 1/10 rating) until a talkSPORT legend snaps, "Get stuffed. Harry won it." Then Kane answers in his own voice and ends on two words to his wife.

**Target runtime: 48–55s (hard max 60s), measured on the timeline.**

---

## 1. HARD RULES (any one broken = redo)
1. **Someone is speaking at every moment.** No gaps over ~0.25s. Stills and B-roll sit **on top of speech**, never in silence.
2. **Source audio only.** No voiceover, TTS, AI voices or AI faces.
3. **Exact words only.** Trim filler ("uh", "um", repeats) inside a range. Never splice to change meaning, and never move a line to another beat.
4. **Voices allowed:** Dean Ashton (beats 1 and 3), Yamal's uncle (2), the talkSPORT host reporting Guti (4), Adrian Durham (5), Alan Brazil (6), Harry Kane (7–8). **No other presenters, interviewers or narrators.**
5. **No minors on frame.** No Kane children, no childhood photos. (Yamal is 19, so he's fine.)
6. **Hard cut on "We done it."** No end card, no music tail.
7. **Never caption "Yamal said"** anywhere. Beat 2 is his **uncle**.

---

## 2. SOURCES (download first)
```
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "ASH_DeanAshton_talkSPORT.%(ext)s"      https://www.youtube.com/watch?v=jQFm0ppDbpc
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "UNCLE_Yamal_uncle_AS.%(ext)s"         https://www.youtube.com/watch?v=I2Bmkq5_xLo
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "BRAZ_talkSPORT_GetStuffed.%(ext)s"     https://www.youtube.com/watch?v=h6jag7BsM8I
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "TS_Durham_1of10_2024.%(ext)s"          https://www.youtube.com/watch?v=ZO5OaOYGLq0
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "SKY_Kane_BallonDor_interview.%(ext)s"  https://www.youtube.com/watch?v=LiysaNUZpx0
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "SPEECH_Kane_BallonDor.%(ext)s"         https://www.youtube.com/watch?v=o0JdYVpXoQY
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "BAYERN_Kane_ceremony.%(ext)s"          https://www.youtube.com/watch?v=407tY1wz-w0
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "REACT_Yamal_Mbappe_faces.%(ext)s"      https://www.youtube.com/watch?v=8a5ukyzTLlc
```
| Code | Title · Channel · Date | Use |
|---|---|---|
| ASH | *Dean Ashton OUTLINES why he DOESN'T believe Harry Kane should win Ballon d'Or* · talkSPORT · 26 Oct 2026 | Beats 1, 3 |
| UNCLE | *LAMINE YAMAL's uncle on KANE's Ballon d'Or: "IF you LIKE FOOTBALL, you WANT to WATCH LAMINE"* · Diario AS · 28 Oct 2026 | Beat 2 |
| BRAZ | *"GET STUFFED!" Alan Brazil TAKES AIM at Lamine Yamal's family…* · talkSPORT · 28 Oct 2026 | Beats 4, 6 |
| TS | *Adrian Durham Awards Harry Kane A 1/10 For His Role In The 2024 Euro Final!* · talkSPORT · 15 Jul 2024 | Beat 5 |
| SKY | *Harry Kane's emotional 2026 Ballon d'Or winner's speech* · Sky Sports News · 27 Oct 2026 | Beat 7 |
| SPEECH | *HARRY KANE WINS THE BALLON D'OR! Full Speech* · Diario AS · 27 Oct 2026 | Beat 8 |
| BAYERN | FC Bayern, full reaction and speech | **B-roll only:** Ronaldo Nazário handing Kane the trophy; Kane's shocked face at the announcement |
| REACT | *Lamine Yamal & Mbappe Reaction to Harry Kane Winning* · Nexus Football | **B-roll only, ≤1.5s, no audio:** Yamal's face at the announcement |

- Export every range with **±3s handles**.
- **The timestamps come from YouTube captions and can drift 1–2s. Lock every in/out point by ear.** The words win over the timestamps.

---

## 3. THE SEQUENCE (cut exactly in this order)

### BEAT 1: HOOK
- **Source:** ASH · **~1:00 → 1:04**
- **Words:** "Harry Kane is not a Ballon d'Or winner."
- **Picture:** Dean Ashton in the talkSPORT studio. **Frame 1 is Ashton mid-sentence.** No intro, no title card.
- **On screen:** label **DEAN ASHTON · talkSPORT · HOURS BEFORE THE CEREMONY**
- **Red words:** NOT A BALLON D'OR WINNER

### BEAT 2: THE FAMILY
- **Source:** UNCLE · **~0:17 → 0:24** (Spanish audio)
- **He says:** "Si te gusta el fútbol, vas a ver a Lamine, no vas a ver a Harry Kane."
- **Captions (English only):** "If you like football, you watch Lamine. You don't watch Harry Kane."
- **Picture:** the uncle in his bar, then for the last ~1s, **Yamal's face at the announcement** (REACT, picture only).
- **On screen:** label **LAMINE YAMAL'S UNCLE**
- **Red words:** YOU DON'T WATCH HARRY KANE

### BEAT 3: THE PUNDIT AGAIN
- **Source:** ASH · **~1:31 → 1:39**
- **Words:** "…there's nothing he does that I think, wow, I could not do that."
- **Picture:** Ashton.
- **Red words:** NOTHING HE DOES
- **Beats 1 and 3 are the same clip, split around the uncle on purpose. Don't merge them.**

### BEAT 4: THE CONSPIRACY
- **Source:** BRAZ · **~8:59 → 9:03**
- **Words:** "…it was suspicious that the ceremony was held in London and a London-born player won…"
- **Picture:** a photo of Guti (Real Madrid legend / *El Chiringuito*), then **Kane's shocked face** at the moment his name is called (BAYERN).
- **On screen (MANDATORY):** card **GUTI · REAL MADRID LEGEND · SPANISH TV**. The clip starts mid-sentence, and this card is the only thing that tells the viewer whose claim it is. **Never caption it as fact.**
- **Red words:** SUSPICIOUS · LONDON-BORN
- **Upgrade:** if you can find Guti's own on-camera clip from *El Chiringuito* (26–27 Oct) saying the London venue plus a London winner was a suspicious coincidence, it **replaces** this beat. Tell Affan if you find it.

### BEAT 5: 1/10
- **Source:** TS · **3:19 → ~3:26**
- **Words:** "…one out of ten, and he's lucky to get that." (Start on "Harry Kane, he gets a one out of ten…" if it fits; otherwise start on "one".)
- **Picture:** Adrian Durham in the studio, or a Kane Euro 2024 final still (head down) over the audio.
- **On screen:** card **talkSPORT · 2024**
- **Red words:** ONE OUT OF TEN · LUCKY TO GET THAT

### BEAT 6: THE TURN
- **Source:** BRAZ · **~9:14 → 9:21**
- **Words:** "Get stuffed. Harry won it. Harry's a top man who's worked hard at his game. Look at his goal record. Get stuffed."
- **Picture:** Alan Brazil in the talkSPORT studio. **Hard cut in.** This is the momentum switch of the whole Short.
- **On screen:** label **ALAN BRAZIL · talkSPORT**
- **Red words:** GET STUFFED · HARRY WON IT
- ⚠️ Confirm by ear and on screen that this voice is Alan Brazil (the upload title names him). If it's a different presenter, change the label to that name.

### BEAT 7: KANE ANSWERS
- **Source:** SKY · **0:50 → 0:57**, then **1:11 → 1:27**
- **Words:** "People see the end product… it's very rare for people to see what goes on behind the scenes…" / "…all that sacrifice… time that I'd love to be spending with my kids, with my family and my wife…"
- **Picture:** Kane in the Ballon d'Or night interview. Over "time that I'd love to be spending…", 1.5s of **Ronaldo Nazário handing him the trophy** (BAYERN). **No footage of his children.**
- **On screen:** card **HIS ANSWER**
- **Red words:** BEHIND THE SCENES · SACRIFICE
- Use only Kane's voice. The SKY upload also has studio presenters, and none of their audio goes in.

### BEAT 8: ENDING
- **Source:** SPEECH · **~9:07 → 9:11**
- **Words:** "So, here it is. We done it."
- **Picture:** Kane on stage with the trophy. If the broadcast cuts to his wife Katie in the audience, use that reaction.
- **Red words:** WE DONE IT
- **Caption "We done it" exactly as said.** Don't correct it to "we did it".
- **HARD CUT on "We done it."**
- If the beat feels too abrupt, open it on "To my wife Kate, my best friend…" (~8:51) and cut straight to "So, here it is. We done it." That's about +3s.

---

## 4. PICTURE
- **1080×1920, 30 fps**, full-bleed vertical crop on each speaker. No letterbox, no blurred fill.
- **Grade:** beats 1–5 slightly cold and desaturated (the doubters), **beats 6–8 warm** (the turn). The grade switch lands on the first frame of beat 6.
- Labels and cards: small, top third, ~2s each, and only on a speaker's first appearance.
- SD sources (talkSPORT 2024, the uncle's bar footage): light sharpen, grain-match, **don't punch past ~115%**.

## 5. AUDIO
- **−14 LUFS integrated, true peak ≤ −1 dBTP.** Level-match the studio, bar and ceremony audio.
- **The uncle is in a noisy bar:** light denoise, keep the room.
- **Music:** a tense, low bed under beats 1–5 at about −28 dB. **Hard stop on beat 6** so "Get stuffed" lands dry. Then a warm, lifting bed under beat 7 at about −28 dB, **pulled out completely under beat 8.** Kane plays dry at the end.
- 2–4 frame crossfades on every dialogue cut.

## 6. CAPTIONS
- Word-by-word, burned in, in the same style as the recent Abundance Wisdom Shorts, at ~62–68% of frame height. Red words as listed per beat.
- **Beat 2 is captioned in English only (no Spanish text)**, bigger than usual and two lines at a time, so a non-Spanish viewer reads it instantly.
- Caption only spoken words. Don't caption names that aren't said.
- **Safe zones:** no text in the bottom ~20% or right ~12%.

## 7. EXPORT
- H.264 (≥20 Mbps) or ProRes 422 .mov, 1080×1920, 48 kHz.
- File: **`Kane Didnt Deserve It.mov`** → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`

## 8. QA CHECKLIST (tick every box before export)
- [ ] Beats 1 → 8 in order.
- [ ] Frame 1 = Ashton saying "Harry Kane is not a Ballon d'Or winner."
- [ ] Beat 2 has English captions only, and is labelled as the **uncle**, never Yamal.
- [ ] The beat 4 Guti card is on screen.
- [ ] Beat 6 lands as a hard cut, with the music stop and the grade switch.
- [ ] Only the allowed voices (rule 4).
- [ ] No child on frame.
- [ ] "We done it" captioned as said; hard cut on it.
- [ ] Runtime ≤60s on the timeline.
- [ ] −14 LUFS, true peak ≤ −1 dBTP.

## 9. REPORT BACK TO AFFAN
1. Final runtime.
2. The exact in/out points used per beat (file + timestamps).
3. Beat 4: talkSPORT host or Guti's own clip?
4. Beat 6: confirmed that it's Alan Brazil?
5. Beat 8: short version or the "To my wife Kate" version?
6. Anything that didn't match this brief.
