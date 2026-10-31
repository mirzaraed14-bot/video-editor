# Client Short from Affan's sequence: the lean recipe (≈ 40 tool calls)

For a client Short where **Affan picks the moment, cuts it in Premiere and records a Tella walkthrough**. Built from the first one,
`projects/_client-scott-clary/fubu-50-shirts/` (2026-10-15, BRIEF.md there). Look = this kit (README.md); this page is only the ORDER and
the commands that work. Budget: Affan caps a video at **$10 of Claude usage** → a FRESH session per Short, no subagents, no research,
one check sheet, no full-size image reads. Paths below are relative to the repo; `J=projects/<client>/<job>`.

## 1. Walkthrough → brief (3 calls)
- Built-in browser on the Tella link, then JS: `v=document.querySelector('video'); v.muted=true; await v.play();` wait 4 s, read
  `performance.getEntriesByType('resource')` for `prod-stream.tella.tv/media/manifest.m3u8?...`.
- `ffmpeg -i "<manifest url>" -map 0:v:0 -map 0:a:0? -c copy $J/guide/guide.mp4`, audio-only copy into `$J/guide/tx/raw/`, then
  `bash .claude/skills/rough-cut/scripts/transcribe.sh $J/guide/tx` (it only picks up VIDEO extensions: keep the audio in an .mp4).
- One overview sheet (`fps=1/8,scale=480:-1,tile=6x7`) + ONE full frame where his Premiere **Transcript panel** shows the whole
  sequence text. His words = the brief: write `$J/BRIEF.md` (direction, rules, sources table, ▶ STATUS) before cutting.

## 2. His sequence → the cut (3 calls)
- `python workflows/prproj-seq.py "--latest ABW10" "Sequence NN"` (newest autosave AFTER the walkthrough; prints every track).
  **V1 = the cut, V2 = a full-screen overlay slot (no split), V3 = a split slot.** Follow the sequencing strictly; nothing added.
- Doubled-frame check: `signalstats` YDIF over 1 s; alternating ~0.01 / ~1.5 = 30p doubled to 60p → cut the section at 30p:
  `ffmpeg -ss <a> -i source.mp4 -t <len> -vf fps=30 -c:v libx264 -crf 12 -pix_fmt yuv420p -c:a pcm_s16le $J/raw/<x>_section.mkv`
  (seek on an even 60p frame). Never put the whole episode in `raw/` (transcribe.sh takes every clip there).
- `python workflows/prproj-seq.py <proj> "Sequence NN" --edl /tmp/video-editor/<job>/cuts.json --offset <a> --clip <x>_section.mkv`
  (`cygpath -w` for the /tmp path), **copy it to `$J/transcript/cuts.json` too** (voice-gain.py reads that before splice.sh writes
  it), transcribe the section, `bash .claude/skills/rough-cut/scripts/splice.sh $J`.
- **Stumbles WhisperX drops (Morgan, 2026-10-26):** "a- the- the claw", "they- they- there's" never reach words.json, so an energy
  pause cut keeps them and Affan hears hesitations. Run faster-whisper large-v3 (the whisperx venv; torch's `lib` on the DLL path)
  with a filler-friendly `initial_prompt` on the spliced cut, cut what it finds, and accept an edge only if the candidate reads clean
  BOTH with and without the prompt (a prompt containing the words it hunts can invent them). An edge inside a consonant burst
  clicks (audio-qa JOINT CLICKS): move it into the closure before it. Write `work/cut/joints30.txt` (segment starts
  + any camera cut inside a segment, from `select='gt(scene,0.3)'`).
- Background: `python workflows/topaz-iris.py $J/outputs/<job>.mp4 $J/outputs/<job>.topaz.mov --out-scale 2 --no-stab --segments <joints>`
  (~10 min; launch with run_in_background, not `( … &)`).

## 3. Overlays (6-10 calls)
- **Real photos**: `python workflows/img-candidates.py <dir> "tag|query|n" …` (curl Bing, never python urllib (region-skewed junk): `curl -s -A <UA> "https://www.bing.com/images/search?q=<q>&first=1"`,
  → files + sources.txt + ONE numbered `_sheet.jpg`; ≥ 700 px; Pinterest /originals/ tried first). Skip Getty/Alamy
  watermarks. A brand's own product shots are often transparent PNGs (a ready cutout).
- **Stock video**: Pexels/Pixabay return 403 to curl. Mixkit works: page `https://mixkit.co/free-stock-video/<tag>/`, ids from
  `assets.mixkit.co/videos/<id>/<id>-360.mp4`, download `<id>-1080.mp4`. Pexels via the browser (same-origin `fetch('/search/videos/<q>/')`)
  only for ids; its stock rarely shows a specific scene.
- **Higgsfield** (Affan asked for it on image overlays): soft image → `media_import_url` (no presigned PUT, no huge URLs) →
  `upscale_image` 2k (≈ 2 cr) → `jobs_wait` → curl the result. A scene no stock shows (a FUBU bouncer at a velvet rope) →
  `generate_image` `gpt_image_2_5` 9:16 (0.25 cr) then upscale. Never a real person generated. Log every source in BRIEF.
- **Popularity beats: the face a casual viewer names instantly** (Affan: 50 Cent, not LL Cool J).
- A "speaker silent and listening" opener: his own camera from a silent stretch, `setpts=PTS/0.75,minterpolate=fps=30:mi_mode=mci`.

## 4. Spec, faces, build (5 calls)
- Copy `fubu-50-shirts/yt/build_spec.py` and edit: chunks (assert word count; ≤ 19 chars; only ! ? and quotes; profanity starred
  + `audio.mute`), shots on HIS slots, free cuts = first word frame − 4, one A shot per same-camera run (his jump cuts stay; no
  punch-in), `"cut"` whips on the same camera, `SPLIT` with `"flip": true` when he wants the speaker BELOW, A `fy_out` 0.35 (lips
  above the seam captions), hook card = the credit with "/" (the hook font has no "·"), watermark = the show's name, **no bed**
  (he adds music), SFX on every overlay. **Premium sound (Affan 2026-10-26, Morgan v2: the kit's stock cues "don't sound premium ...
  don't fit the motion graphic"): never the kit's blips / glass ticks / glass pops.** Copy `morgan-claw-machine/yt/sound.py` (cinematic
  slices, HP-filtered hits, one sub layer under the 3 big moments, a fresh Epidemic pull per job) and its `CUES` block in
  `yt/build_spec.py` (`auto_sfx: False`): a whip cut = a short whoosh crested ON the cut, ~12 dB under; a card value = a hit or a
  thud on its first VISIBLE frame; a number winding up = a reverse swell ending on the landing; cuts back to the face and prop exits
  silent. Gate: `yt/cue_check.py` PASS (no LOUD, no WEAK on a phone), levels near the Chris Do IG mix (hits -5..-12 dB full).
- Two shot extras (Bombas, 2026-10-17): `"prop": {src (RGBA cutout), f0, f1, xy, h, angle}` on a shot = a product that whips in,
  hangs mid-frame and whips out (leave ≥ 3 frames before the cut); a "stronger zoom" = its own A shot, `r` 0.22-0.25, starting at
  the previous A shot's end zoom (`z0 = z0_prev * (1 + r_prev)`) so the cut never jumps scale.
- **Read the words against the audio for mishears before the first render**, proper nouns above all (Serhant v1 shipped "MAYBE SAID" for "said" and
  "ARE LISTENING" for "Dollar Listing"; Affan caught both). The chunk TEXT is free, only its word count must match.
- `cd $J && python yt/build_spec.py`, then `uv run presets/youtube-shorts/onyx-samples-youtube/kit/yt_faces.py $J`.
- `python presets/youtube-shorts/onyx-samples-youtube/kit/yt_build.py $J v1` (background, ~4 min).

- **Head lock + 60 fps (2026-10-19, from AW):** `python workflows/cut-frames.py outputs/<job>.mp4 work/cut/joints30.txt > work/cut/joints_measured.txt`,
  then `head_lock=` those joints, `head_track=True` (CALM: the crop follows the EYES, sigma 12 frames, no size-following; A `fy_out` 0.32 = the eye line, `z0` 1.12;
  scan faces with `yt_faces.py --step 1`) and **`zoomkeys` per speaker shot** (eased, zoom only on emphasised lines and back out; a quick
  zoom-in after a whip; never a scale jump at a cut). Splits are not tracked (Affan 2026-10-20 Tella feedback); `fps_out=60` makes `yt_build.py` double the finished picture with
  Topaz Chronos per shot (`topaz-iris.py --fps-mult 2`, never across a cut) and render the captions at 60. Both on by default for Scott.
  Inside a SPLIT, the takes also break at its base-cut joints and its B-roll panel's own hard cuts (2026-10-31, `split_edges`; the build
  log prints them as "Chronos: N more take edges inside SPLIT shots").
- **Before the build (Scott):** freshness check + locked prediction + pre-mortem + title + thumbnail in
  `presets/youtube-shorts/scott-clary/RESULTS.md` (ENGINE.md has the line; `thumbnail.py` draws the locked cover format).

## 4b. When Affan says "no need to sequence" (Peter Cuneo, 2026-10-21, `projects/_client-scott-clary/marvel-board-vs-rdj`)
- The cut comes from the agreed text draft: `work/cut/make_edl.py` holds (beat, start, end, pin) on the VIDEO clock. A podcast RSS
  MP3 lines up with his YouTube download by cross-correlation (0.04 s there), so its WhisperX words can draft the EDL while the video
  transcribes. Where WhisperX stretches or squeezes a word (a "the" across a 0.8 s pause; "$525 million" squeezed into 0.4 s of a
  3.7 s phrase), measure the 50 ms RMS, re-time those words in `transcript/words.json` (keep `words.whisperx.json`) and pin the
  segment (`no_refine`): refine-cuts otherwise moves the edge to the wrong word.
- **Measure the face before choosing the layout.** A webcam guest sat so close (face 45 % of the height, eyes at 67 %) that every
  9:16 crop was an extreme close-up with the mouth under the caption line: his beats became standard SPLITS (face on top, captions on
  the seam under the chin), with one prebuilt bottom clip per long split (`yt/split_bottom.py`: hard cuts between stills, a baked
  lights-on) so the untracked top stays ONE shot.
- `hook.t0` (s) lands the credit card late, on the line that names him; a magazine cover of the guest (DOC) proves the authority.
- Cards: `workflows/mg-cards.py collateral` (a number rolls up, a list pops in, a verdict plate) is the template for a "what was at
  stake" beat; `--r0/--r1` land the roll on the spoken number. The caption numeral rule spells decimals out: write the words he says.
- Topaz and WhisperX hang when another session holds the GPU: build at 30 fps first, run the 60 fps final once the GPU is free.
- (War Dogs, 2026-10-23) Overlay devices in `yt_overlay.py`: `tags` (a name tag beside the guest's head: dot, line, label; place it
  from `yt/work/faces.json`, on the side with room), `stamps` (a word slams in and holds), `glints` (a star flash on a word). Cards in
  `mg-cards.py`: `counter --money` ($ + commas), `craigslist`. Scott's YouTube uploads wipe an ad graphic in near ad reads: check the
  last frames of the cut (YDIF) and freeze the last shot before the wipe (A shot `"freeze": [[f0, N]]`). A tight close-up camera
  wants z0 1.0 (1.12 cut the head).

- (Chris Do, 2026-10-24) When Affan asks Claude to fetch the episode: ONE plain `yt-dlp` request (no cookies, no workaround; stop on a
  bot check) and only the story's stretch: `--download-sections "*<a>-<b>"` with the avc1 format (8 min of 1080p60 in ~2 min). The RSS
  MP3 can carry extra ad seconds (5393 vs 5385 s there): measure the offset (FFT cross-correlation), never assume it. Cards in
  `mg-cards.py`: `sneaker --mode real|fake|rule|button` (a product cutout, its price stepping on the spoken numbers, a sponsored-ad
  mock with a marker ring + FAKE written on, the real-vs-fake pair and its callback), `replies` (rates out, Yes / Yes / No.),
  `dayrate` (a rate stepping up + bars), all timed by `--steps v@t` / `--t1` from the transcript in build_spec. A webcam guest whose
  head fills a 9:16 crop: open on a FIT panel of his cam so a `tags` pointer has room (`"plate": true` on a busy background), and
  check captions vs lips on a FULL-SIZE frame (the 1/4-size proof sheet exaggerates overlaps). Snap every shot edge within 4 frames
  of a cut ONTO the cut: a 1-2 frame sliver between a word-led shot edge and a joint kills the 60 fps Topaz pass (`IndexError` in
  topaz-iris.py, final v1).

## 5. One check, then final (4 calls)
- **Sharpen, every Scott Short (Affan asked twice, 2026-10-26 / 10-28):** after each yt_build render, `python workflows/sharpen-picture.py projects/<job>` then `yt_build.py <job> <version> --skip picture,overlay`. The 30 fps check gets it too (he judges the look on it).
- **Before sending a check:** the proof sheet must show the name tag fully inside the frame and nothing landing on it (`yt/tag.json` from the measured head + label width), and every number caption on its spoken word (WhisperX interpolates digits: cross-check with faster-whisper + RMS).
- ONE 16-frame sheet (`select=eq(n\,…)`, `scale=270:480,tile=8x2`). The v1 defects last time: captions on the lips, a face cropped,
  the subject outside a 16:9 → 9:16 crop (set `cx`), a missing glyph. Fix in the spec, re-run `build_spec.py` (it picks up
  `base_hq` once Topaz is done), build `final`. A picture-only change: `--skip overlay,mix`.
- Deliver: copy to `$J/outputs/<job>.final.mp4` and `X:\Claude Projects\Exports\<client>-<job>.final.mp4`, the sheet as
  `outputs/<job>.proof-sheet.jpg`, `ebur128` for LUFS / peak, BRIEF ▶ STATUS. The MP4 is > 30 MB: only the desktop app shows it.
