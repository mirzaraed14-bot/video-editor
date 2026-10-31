# drinkinbros-berenger-inception: Onyx sample Short for Drinkin' Bros (Ross Patterson, Dan Hollaway) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 ~20:45: the CUT is done; next = assets (logged below before each pull), then the YT build, then the IG build.**
  `outputs/drinkinbros-berenger-inception.mp4` = 859 f @ 30 fps, 28.63 s, 20 segments (`work/cut/make_edl.py tight`, all pinned),
  AMPLIFY_DB −4 (−2 ran the −6 dBFS limiter on the hosts' laugh peaks), audio-qa: timeline exact, 19 joints clean; the 2 "ambience
  holes" (18.63 s, 21.10 s) are Berenger's GATED remote mic (digital silence in his pauses), not crossfade dips.
  `work/cut/patch_transcript.py` (RUN AFTER EVERY SPLICE) makes the caption transcript match what is heard. Verbatim faster-whisper on
  the cut, both with and without the filler prompt (`work/cut/fw_cut_v1.txt`), reads exactly the approved beats.
- Delivery rate: **30 fps native, NO Topaz, NO 60 fps** (Affan 18:30 via the coordinator); GPU only for transcription, under `lock.sh gpu`.
- Earlier builder (17:58, stopped after ~5 min): left `work/cut/rss.f32`, `src.f32` (an xcorr attempt) and `work/look/sheet.jpg`;
  re-measured here, nothing else reused.

## The job
- Show: **Drinkin' Bros Podcast** (Ross Patterson, Dan Hollaway, Jarred Taylor), 283K. Tone (handoff 2026-10-31): raw, irreverent,
  military / bro humor. Their Short named in the permission email: "Are Tier One Operators Born or Made?".
- Approved pick: `projects/_onyx-batch6-2026-10/SEQUENCING.md` § "Drinkin' Bros v3": **"Tom Berenger was IN Inception. He never
  understood it."** (ep 1719, YouTube wSjYleM4B_c; the viewer gets: even the cast was lost, and Cillian Murphy's answer).
- Source: `source/wSjYleM4B_c_0.45.00-1.05.00.mp4` (main session's pull: 1920x1080 30/1 H.264 + AAC 44.1k, 1200 s, both streams
  start 0). **Real faces, checked**: Ross in his studio (purple set), Berenger on a webcam with a grass virtual background, Dan in a red
  studio. The beats are inside the window: **source t = RSS t − 2665.156** (FFT xcorr of ep1.mp3 3230-3330 s vs the window, ncc 0.962;
  `work/cut/xcorr.py`), so the scout's 0:53:58-0:55:13 = source 572.8-647.8 s (YouTube ≈ 0:54:33-0:55:48).
- Section: `raw/berenger_section.mkv` = source 568.000-656.000 s (frame 17040 on, x264 CRF 12 + PCM; frame-matched: raw f0 = source
  f17040), so **raw t = source t − 568 = RSS t − 3233.156**.
- Both looks from ONE cut: YouTube (Sean Ryan look, `presets/youtube-shorts/onyx-samples-youtube/`) + Instagram (neon window,
  `presets/instagram/neon-window/`). Templates: the batch-6 siblings `projects/crossexamined-300k-house-check/` and
  `projects/tfts-we-need-to-talk/` (scripts only: beat plans, cards and SFX are this job's own).
- Deliver: `outputs/drinkinbros-berenger-inception.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\drinkinbros-berenger-inception.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## Who is who (verified on the picture, never by caption)
- **Ross Patterson = the host in the black HARD AF cap + white headphones, grey Ohio State quarter-zip**, purple studio (his own
  name is on the studio's trophy plate "ROSS PATTERSON COACH OF ..." and his book "The Final Inch" sits on the desk; he says "one of
  Dan and I's favorite movies", so he is not Dan). He asks both questions.
- **Tom Berenger = the white-haired guest on the webcam** (grass virtual background, black tee, cross pendant).
- Dan Hollaway (red studio, "ROSE 14" jersey) appears only in laugh cutaways, none inside the cut.
- Camera map of the section (scdet, raw s): Berenger 0-5.17 · Ross 5.17-15.80 · Berenger 15.80-17.73 · Dan 17.73-18.73 · Ross
  (laughing) 18.73-20.63 · Berenger 20.63-31.87 · **Ross with a burned-in INCEPTION FILM STILL inset (top-left, x 24-696, y 20-398 of
  1920x1080) 31.87-43.27** · Berenger 43.27-73.53 · Ross laughing 73.53+.
- In the cut (frames): Ross 0-125 (the program cuts to Berenger 4 frames into "No"), Berenger 125-130, Ross laughing 130-151 (under
  "Never did"), Berenger 151-351, Ross + film inset 351-445, Berenger 445-859.

## The beats (followed exactly; found by their WORDS; nothing added, nothing re-ordered)
1. HOOK (Ross): "Inception. Working with Christopher Nolan… When you read that script, did you understand it?"
   (raw 7.30-7.93 + 8.95-10.20 + 12.53-14.68; cut "I gotta ask you about one of Dan and I's favorite movies here," / the 1 s "uh" /
   "How was that? And, uh,")
2. (Berenger): "No. Never did from the time I started it till the time I finished. Never understood it. I didn't know where I was…
   I was just lost in space." (15.66-15.97 + 19.93-24.72 with the hosts' laugh 22.87-23.79 cut + 25.92-27.91 + 28.94-30.48; cut
   "Nope.", "I don't know", "What I was doing is")
3. (Ross): "When you watched the movie, did you even figure it out at that point?" (33.34-36.45; ends before "Because I've heard rumors")
4. (Berenger): "I saw that really fine Irish actor that was in there… I go, let me ask you something. Have you seen this? He goes,
   yeah, I saw it in London…" (45.04-45.37 "I" + 47.12-50.30 "saw that ... there" = his stumble "I was, I- well, I- I saw- saw" resolved;
   51.33-52.05 + 53.03-55.22 "I go, let me ask you something. Have you seen this?" (his 1 s hesitation after "let" cut); 56.66-57.98;
   cut "I- I saw him, and" and "I go, yeah, because he's English. Of course he would have.")
5. BUTTON: "And I said, well, did you understand it? And he said, I think so." (63.52-66.12 (cut "Um, he said-") + 66.42-67.60 +
   70.17-73.42) **+ the laugh, cut in the quiet before Ross's "Talking about Cillian Murphy"** (73.78).
- The scout's "Sylvia Murphy" is Ross's "Talking about Cillian Murphy" AFTER the button: outside the cut. The name is CARDED
  ("CILLIAN MURPHY") over "that really fine Irish actor", never captioned as a mishear.
- Loop: "…And he said, I think so." → "Inception." (the answer to a question about Inception runs back into the word itself).

## Decisions (with reasons)
- **The punchline pause is kept SHORT, not cut flat**: Berenger leaves a 3.2 s pause before "I think so" (his mic gate makes it
  digital silence). The YT look cuts pauses to 2-3 frames, but this one is the joke's timing: kept at ≈0.4 s. FLAG for Affan.
- **"No." lands on Ross cracking up**: the program cuts to Berenger 4 frames into "No" and back to Ross laughing 0.17 s later;
  those 5 Berenger frames are a flash, so the shot holds Ross (a 5-frame freeze of Ross listening, then Ross live, laughing at the
  "No."), and cuts to Berenger on "from the time I started it".
- **No Inception footage or stills anywhere** (third-party film): the show's own burned-in film-still inset (beat 3) is cropped out of
  every frame we use. Type, a built spinning-top prop (the film's totem as a generic object, drawn in code), real HQ photos of
  Christopher Nolan and Cillian Murphy (Wikimedia Commons, free licences, logged), real London B-roll.
- **No music bed; SFX = soft Patrón-style swishes only**, one per graphic entrance, sized to the move; cuts back to a face, text swaps
  and type silent (memory feedback-premium-sfx SUPERHERO + UNDER HIS MUSIC). A fresh Epidemic set.
- Captions run the whole video, under the hook too (CLAUDE.md Rules; the coordinator's batch-6 call). Colour = voice (YT): Berenger
  main (white, red wipe), Ross yellow, **Cillian quoted = cyan** ("yeah, I saw it in London", "I think so"), Berenger quoting himself
  stays main.
- No profanity in the cut; no sensitive words (censor rule: nothing to censor).

## GATE 5 (facts on screen)
- **Tom Berenger: "OSCAR NOMINEE"** (en.wikipedia API 2026-10-31: "nominated for the Academy Award for Best Supporting Actor ... for
  his portrayal of the Staff Sergeant Bob Barnes in Platoon (1986)").
- **Cillian Murphy** is in Inception's cast (en.wikipedia "Inception": "The ensemble cast includes ... Cillian Murphy, Tom Berenger");
  he is Irish (Berenger's own words: "that really fine Irish actor"). Robert's godfather Peter Browning is Berenger's role (Inception
  plot: "Robert's godfather Peter Browning") — used only if a card needs it, as "HE PLAYED HIS GODFATHER".
- "INCEPTION" / "Christopher Nolan" on the script cover: Nolan wrote and directed Inception (Wikipedia). The cover shows only the
  title and "by Christopher Nolan" (no invented script text).
- The dream-level stack ("LEVEL 1 / LEVEL 2 / LEVEL 3 / LIMBO"): the film's own structure (Wikipedia plot: three nested dream levels and
  Limbo), an illustration of "I didn't know where I was", no claim about Berenger.
- The spinning top that is "STILL SPINNING" at the end: the film's last shot (Wikipedia: the script concludes "the spinning top is STILL
  SPINNING"): the callback on "I think so" claims nothing.
- London: his words ("I saw it in London"); no premiere claim on screen.

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on the 9
## labelled tiled sheets built today in `projects/tfts-we-need-to-talk/work/catalog/` (79 singles at 480x270 in `singles_1-4.jpg`, 58
## strips in `strips_1-5.jpg`), every tile read)
- **Fits this story** (a famous film's cast member admitting he was lost, told as a two-man exchange with one quoted third man):
  - **FX-33 Dust Void Drop** → the spinning top isolated on an empty dark field (the film's totem as THE object of the Short).
  - **FX-79 Flash-Forward Echo** → the top returns on "I think so", still spinning (the film's own ending as the punchline's callback).
  - **FX-23 Pointer Tag** → a "YOU ARE HERE?" pointer hunting across the dream-level stack on "I didn't know where I was".
  - **FX-09 Demand Tree** (as levels) → the stack LEVEL 1 / 2 / 3 / LIMBO, built as he says "never understood it".
  - **FX-42 Kin Tag** → "OSCAR NOMINEE / TOM BERENGER" beside his face; Ross's own tag (HOST).
  - **FX-29 Float Frame** → the Nolan and Cillian photos as framed cards over their own blur (never blown up past their size).
  - **FX-55 Red Pen Underline** → a red hand-drawn "?" on the script cover on "did you understand it?".
  - **FX-58 Speaker-Coded Subs** → three voices, three colours (Berenger / Ross / Cillian quoted).
  - **FX-40 Slow-Burn Portrait** → the last line on his face with a slow creep in while the laugh lands.
- **Not used before on an Onyx sample**: FX-33 as a 3D-rendered prop, FX-23 as a moving "you are here" pointer, a quoted third
  person carded with a real photo and his own caption colour.
- **Leaned on by the last ones, avoided here**: CrossExamined's object-through-states check + FX-41 Year Ghost + FX-71 Funnel Count,
  TFTS's FX-11 before/after split + FX-09 rows list, Pollak's FX-27 quote card + FX-28 dossier, Pincus's FX-34 highlighters.

## What this one does better than the last ones (rule 5; vs CrossExamined, TFTS, Pollak YT/IG 2026-10-31)
1. **A built 3D object instead of flat cards**: the film's spinning top is rendered in code (lathe-shaded metal, real spin blur and
   precession wobble), the first rendered 3D prop on an Onyx sample; it frames the Short (lost in space) and returns as the punchline.
2. **Comedy timing as a design rule**: the cut keeps the one pause that is the joke and cuts every other one; "No." lands on the host's
   laugh (a reaction cut), the laugh lands before the cut-out.
3. **Three voices legible at a glance**: the quoted Cillian gets his own photo, name card and caption colour, so a stranger follows
   "he goes… I think so" without context (CrossExamined and Pollak had one voice, TFTS two).

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/wSjYleM4B_c_0.45.00-1.05.00.mp4` | main session (YouTube wSjYleM4B_c, window 0:45:00-1:05:00, 1080p30 H.264 + AAC) | 273 MB | the source (not pulled by me) |
| v2 | `raw/berenger_section.mkv` | LOCAL derivative of v1 (source 568-656 s) | 71 MB | the section the EDL cuts from |
| w1 | `yt/assets/broll/p-nolan-bfi-2024.jpg` | upload.wikimedia.org: File:ChrisNolanBFI150224 (10 of 12) (53532289710) (cropped).jpg (2251x1388, CC BY 2.0, via the en.wikipedia imageinfo API) | ≈ 0.5-1 MB | "working with Christopher Nolan": the real man |
| w2 | `yt/assets/broll/p-cillian-berlinale-2017.jpg` | upload.wikimedia.org: File:Cillian Murphy Press Conference The Party Berlinale 2017 02cr.jpg (1483x1977, CC BY-SA 4.0, Maximilian Bühn) | ≈ 0.5-1 MB | "that really fine Irish actor" = CILLIAN MURPHY card |
| w3 | `yt/assets/broll/p-cillian-2014.jpg` | upload.wikimedia.org: File:Cillian Murphy-2014.jpg (1333x1947, CC BY-SA 2.0) | ≈ 0.5-1 MB | alternate Cillian photo (pick the sharper at full size) |
| w4 | `work/img/inception-cast-premiere-2010.jpg` | upload.wikimedia.org: File:InceptionCastPremiereJuly10.jpg (1004x546, CC BY-SA 2.0) | ≈ 0.2 MB | check only: is Berenger in the real cast photo (a receipt for "he was IN it")? small, so a panel at most |
| m-prev | `work/img/mixkit/<id>-360.mp4` previews (london, cinema audience, stars) | assets.mixkit.co/videos/<id>/<id>-360.mp4 (Mixkit free licence) | ≈ 1-3 MB each | pick "I saw it in London" and "when you watched the movie" B-roll |
