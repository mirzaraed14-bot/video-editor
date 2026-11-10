# ron-spomer-9mm-bear: Onyx sample Short for Ron Spomer Outdoors (batch 8, RESTRUCTURE mode)

## ▶ STATUS: resume here
- 2026-11-09 21:35 (main) **SIGNED OFF, checked from the Exports copies** (`X:\Claude Projects\Exports\ron-spomer-9mm-bear.yt.final.mp4` / `.ig.final.mp4`, proof sheets beside them): 43.04 s, 1032 f, 23.976 fps, -12.2 LUFS / -2.2 dBTP, decode clean, identical to outputs/. Fix rounds 1 + 2 verified frame by frame: Phil holds 6.2-8.88 with his label rising out before the cut; the plane is on the first frame after him (IG drawn, YT whip-slide, no blank frame); IG hook window bottom clean; the pass-through opens drawn. IG burns at ~6.1, 17.6, 30.9 (kit design, none inside the hook). The YT picture was re-rendered in full for round 2, so the whole YT file was re-checked (1 fps sheet = round-2 sheet, the .44 settles in frame by 9.5); labels: Ron (HOST) and Phil once each; all proof sheets viewed. Nothing left to build.
- 2026-11-09 18:50 (builder) **BOTH LOOKS DELIVERED**: `outputs/ron-spomer-9mm-bear.sample-yt.final.mp4` and `.sample-ig.final.mp4` (copies `X:\Claude Projects\Exports\ron-spomer-9mm-bear.yt.final.mp4` / `.ig.final.mp4`), proof sheets in outputs/. 43.04 s, 1032 f, 23.976 fps, both -12.2 LUFS / -2.2 dBTP. Cues: 16 soft swishes, cue_check PASS (full -18.7..-19.3 dB under, none weak on a phone; yt/sound.py band-limits the slices to 380-5500 Hz). No bed, no Topaz.
  FLAGS: (1) all three cartridges are product photos (Ron never holds the .500/.44 on camera; his 9mm is ~40 px); scaled by SAAMI length 125/172/245 px (1:1.38:1.96); the .500 is Hornady's own press image, the 9mm an Adobe Stock preview (faint watermark only on the white, cut out), the .44 a stock still. (2) Audio says "I also found THAT nine millimeter" (sequencing: "had that") and "that I was going to get a pass-through" (sequencing dropped the "I"): captions follow the audio. (3) Ron's hook (6.2 s) and the last line are SPLITS with a plain grid panel, not full A shots: Ron's lips and Phil's would sit on the seam captions in a 9:16 crop (measured with YuNet); beat 5 is a split with the 9mm alone on the grid. Beat 5 line is PHIL's. (4) Headline text verified through a web.archive.org snapshot (live site 403). (5) The headline card holds 1.8 s, the first Phil split only 1.0 s before the plane, the last line 1.1 s. (6) IG: splits sit inside the window (Phil on top, white line above the captions), Phil's first IG frame is a full cam and the .44 lands at the IG exhibit opening; bar max 38/255 at window corners (ringing). (7) NOT run: the fresh-eyes reviewer subagent (machine out of memory/fork resources during the build), no playback. (8) Phil's soft webcam is upscaled ~1.4-1.8x in the top panels. Grade: per camera `yt/build_spec.py grade_look` (RON lifted, PHIL gentle), sharpen .55/.40, panels restored.
- 2026-11-09 18:00 (builder, Sonnet): cut DONE (43.04 s, 1032 f at 23.976, 32 segments, `work/cut/make_edl.py` + `run_cut.sh`, words retimed by `work/cut/retime.py`); base for the picture = `outputs/<job>.halves.mp4` (Ron's half for the hook, Phil's for the rest); cards + panels drawn (`yt/cards.py`, `work/gfx.py`); SFX slices cut (`yt/sound.py`, 16 cues). In progress: YT build v1, grade/sharpen, then the IG look. Facts found: (1) the .500 / .44 are NEVER held up in Ron's footage and his 9mm is ~40 px, so all three cartridges are product photos (below); (2) the hook is 6.2 s on Ron's face (hook card + label + captions over it), the longest bare-ish face; (3) the audio of beat 2 says "I also FOUND I had a 9mm" (not "had that nine millimeter"), and beat 3 says "that I was going to get a pass-through" (the sequencing dropped the "I"): captions follow the audio; (4) beat 5 ("A defensive gun has to be with you all the time") is PHIL's: his mouth moves, Ron's is closed (secC 9.9-12.1); (5) Phil's lips clear the seam captions on a full A shot at fy_out .29 / z0 1.0 (YuNet landmarks), so beat 5 and the last line are A shots.
- 2026-11-09 16:50 (main): sources in place, sequencing approved by Affan 2026-11-09 (building on Phil's webcam feed OK'd), creative
  direction written (`DIRECTION.md`). Next: the Sonnet builder transcribes, cuts, builds the YouTube look, then the Instagram look.
- Flags for Affan so far: (1) the "guns on Ron's table" in the sequencing are cartridges he holds up (.500 S&W, .44 Mag, 9mm): the size
  comparison uses those, scaled to their real lengths; (2) Phil's webcam is soft, so his beats are split screens (his cam in the top panel,
  ~1.1x instead of a 1.8x full-frame crop); (3) the transcript has "I also FOUND that nine millimeter" where the sequencing wrote "had":
  the captions follow the audio.

## The Short and the point
Their Short: "Bear Protection Handguns Choose the Right Caliber & Ammo!" (ppAMb4pjDJ0, 11.3K views, 42 s, 1080x1920 23.976, 2026-10-09).
It is Ron's own summary read back to his guest at 35:40-36:20 of episode 511: one face, a static white title box, green keyword captions,
a checklist of ammo advice, and it ends on "am I on the right track so far?".
Ours (title: **He Killed A Brown Bear With A 9mm. A Bigger Gun Would Have Killed His Client**): opens on Ron's own line about the "silly"
9mm Phil used, then the man himself tells it: the 44 left in the plane, the thought that a 44 would have gone through the bear and killed a
client, why a big gun fails in a charge, and the fire-extinguisher button in his words.
**The viewer gets:** the belief "in bear country, bring the biggest gun you can" reversed by the man who killed a brown bear with a 9mm:
the gun you'll actually carry, can draw and can hit with beats the hand cannon.

## Beats (`../_onyx-batch8-2026-11/SEQUENCING.md`, order exact, words exact; episode times, file = episode − 300 s)
1. HOOK, Ron (5:15-5:27): "That silly nine millimeter that Phil actually used to kill a brown bear that was standing over his clients."
2. Phil (12:34-12:56): "I had a 44 Magnum I'd carried for 20 years in the back seat of the airplane, and I also had that nine millimeter, and I thought, we're just going fishing for a little bit. I'll just put it on."
3. Phil, the twist (13:04-13:16): "I was thinking, if I'd had that 44 when the incident happened and the bear was standing on my clients, that was going to get a pass-through and kill a client."
4. Phil (7:36-8:06): "When a bear charges you and you can hear it and you know it's close, all your fine motor skills are gone. You may be the best thing on the range with that great big 500, but you try to draw it out of your holster and shoot it in a second and a half and hit anything."
5. Phil (7:08-7:13): "A defensive gun has to be with you all the time."
6. BUTTON, Phil (23:29-23:44): "Having a handgun is like having a fire extinguisher in your home, or a life jacket on a boat. It's just for an emergency."
Left out: the bear-spray, black-bear and long-gun sections; Ron's summary (it IS their Short).

## Teardown: their Short → ours (Affan's talking points)
| Axis | Their Short (42 s) | Ours (43 s) |
|---|---|---|
| Hook, first 3 s | "handguns for bear protection to sort of a fire extinguisher" mid-sentence, a white box "Bear Protection: What Ammo Penetrates Vitals?" over his cap | Ron calling the 9mm "silly" while a card says HE KILLED A BROWN BEAR WITH A 9MM: a claim that sounds wrong, so you stay |
| Who / what / why by 5 s | Ron is never named, the guest never appears; it is advice with no story | Ron named after the hook; the man who did it, Phil Shoemaker, named on his first frame as an Alaska bear guide of 48 years |
| Captions | all-caps green/white words over his chest | the show's seam captions, Phil and Ron in their own colours |
| Pacing | one 42 s face shot reading a checklist, ending on a question to his guest | a story in five beats with every pause closed; a new picture every 2-4 s |
| Visuals per beat | none: his face and a title box for 42 s | the real cartridges side by side at true scale, the 44 in the plane's back seat, Phil's own 2016 American Hunter headline, a line drawing of the pass-through that would have hit a client, a real charging bear, a 1.5-second draw timer |
| Ending | "am I on the right track so far? / you're right track" | the fire extinguisher line in Phil's words, after the story earned it |
| Sound | the show's mix | the show's voices, soft swishes on graphic entrances only, no gunfire, no bed (Affan picks the song) |

## Catalog pass (CLAUDE.md rule 5), main, 2026-11-09
Read all of `research/effects-catalog/CATALOG.md` and looked at all 79 reference stills (two contact sheets, no strips).
- Used here: FX-25 Exhibit Grid (the cartridges as real cut-out objects on a dark grid floor), FX-21 Red Silhouette Set (the plane and the
  pass-through, events nobody filmed, drawn in thin white line with one red element), FX-54 Dark Headline Card + FX-55 Red Pen Underline
  (Phil's own 2016 headline, rebuilt), FX-29 Float Frame (the charging bear), FX-42 Kin Tag (both labels, kept low), a timer in the spirit
  of FX-77 Clock in Flight (the 1.5 s draw).
- New to Onyx samples: the exhibit grid, the headline card, the line-drawn reconstruction. The last ones leaned on photos and counters.
- Not used: maps (the refuge isn't in the beats), depth type, CRT/phone treatments for the webcam (Affan OK'd the feed as is).

## Better than the last one of its kind
It turns a guest's first-hand story into proof on screen (real cartridges to scale, his own published headline, the exact 1.5 seconds he
names), and it is the first sample where the guest's soft webcam is framed so it looks deliberate (split panels) instead of upscaled.

## Downloads (logged before pulling)
| File | Source | Size | Use |
|---|---|---|---|
| source/ron-ep511-300-1440.mp4 | YouTube JVG08GzbVTY, episode 5:00-24:00 (pulled 2026-11-09 by the mining session) | 332 MB, 1920x1080 23.976, 1140 s | the episode window |
| source/ron-ep-JVG08GzbVTY.webm | YouTube JVG08GzbVTY audio (mining) | 38 MB, opus, 2839 s | transcript audio only |
| reference/short-ppAMb4pjDJ0.mp4 | YouTube ppAMb4pjDJ0 (their permitted Short) | 15 MB, 1080x1920 23.976, 42 s | teardown only |

### Downloads added by the builder (2026-11-09; image search via Bing/curl, no YouTube)
| File | Source | Size | Use |
|---|---|---|---|
| assets/img/cart3/n91.jpg | Adobe Stock preview as2.ftcdn.net (9mm FMJ side view, white; faint stock watermark on the white only) | 1000x667 | 9mm Luger cut-out |
| assets/img/cart3/n441.jpg | westend61.de still-life of a .44 Magnum JHP cartridge (beige plate) | 1232x821 | .44 Rem Mag cut-out |
| assets/img/cart3/n5004.jpg | static.hornady.media press centre, .500 S&W 500 gr FP XTP (Hornady's own product shot) | 600x624 | .500 S&W Mag cut-out |
| assets/img/photos/bear5.jpg | wildnatureimages.com "Charging Brown Bear" (Ron Niebrugge; credit strip cropped) | 2000x1333 | beat 4 charging bear |
| assets/img/photos2/fe2.jpg | images.unsplash.com photo-1652419675207 (dry-chemical extinguisher on a room wall) | 3000x2000 | beat 6 fire extinguisher |
| assets/img/photos/lj8.jpg | freepik (older contributor id 10585, real photo) life jackets on a boat rail, sea behind | 2000x1333 | beat 6 life jacket |
| work/ah.html | web.archive.org snapshot 20260215202544 of americanhunter.org (live site = Cloudflare 403) | 156 KB | headline text verified: "Alaska Outfitter Defends Fishermen from Raging Grizzly with 9mm Pistol" / by Phil Shoemaker / posted on August 10, 2016 |
Ron's own footage: the .500 / .44 are never held up on camera (file 341-371: he looks down at the table), and his 9mm at file ~523-529 is ~40 px, so ALL THREE cartridges are product photos (flag).
