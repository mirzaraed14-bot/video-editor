# mfm-nursery-rhymes: Onyx sample Short for My First Million (PILOT)

## ▶ STATUS: resume here
- 2026-10-04: the episode was transcribed and read in full → `angles.md` (A: Moonbug rebuilt, C: Shaan's Twitch story).
  **Affan picked A with hook A1 ("baby crack").**
- The cut is done: `transcript/cuts.authored.json` → `outputs/mfm-nursery-rhymes.mp4` (16:9, **32.8 s**, AMPLIFY_DB=-2
  because the YouTube source is pre-mastered). Numbers were verified; the Little Baby Bum "$65M" line was cut (undisclosed
  price, public estimate $8–11M).
- `storyboard.md` v1 was **approved by Affan on 2026-10-05** ("build the graphics and render it and sfx").
- The build lives in **`hf-sample/`**: `build.py` generates `index.html` + `plan.json` (re-run it after any change). Assets:
  `assets/base.mp4` = the cut with MFM's **22 px white episode border cropped** (crop 1876×1036+22+22, scaled to 1920×1080);
  logos are the channels' own avatars (800 px); `assets/broll/cocomelon-abc-song-oldest.mp4` = Cocomelon's first upload
  ("ABC Song", 2006-09-01, 320×240, 34.7M views). Accent **#CFAA5A** (MFM gold, from their avatar). The inner zoom per mode
  hides MFM's burned-in name label (it ends at 20.1 % of the width): CARD 1.04, SPLIT 1.15.
- `hyperframes check` passes (0 lint / runtime / layout / motion findings, 25/25 contrast). Render v1 →
  `outputs/mfm-nursery-rhymes.sample.v1.mp4`.
- QA round 1 on v1: 32 confirmed / 12 refuted (`work/qa/qa-v1-result.json`). The big ones: the cut truncated "$103 million"
  (segment 3 end → 562.333, no_refine; the cut is now **33.292 s**), and MFM's two-up layout at 22.967–26.067 (→ CARD16 crop
  into Shaan's box). Fixed in **build.py v2** (word-anchored; v1 kept as `build_v1.py`), base re-cropped 24 px.
- v2 rendered → QA round 2: every round-1 high fixed; 22 confirmed / 7 refuted (`work/qa/qa-v2-result.json`), mostly
  one-frame edges. Fixed in **build.py v2.1** (`work/patch_r2.py`, `work/patch_r2b.py`): the first in-point moved to 57.5 (Sam's
  "I" was cut mid-vowel), so the cut is now **33.625 s**; TWO_UP 23.300–26.400 and SAM_CUT 27.500 re-measured frame-exact; b10b
  eases its zoom from 1.82 (label-safe); word stamps patched relative to segment 3; caption rules; fades end before cuts.
- v3 → QA round 3 (final, cap 3): 17 confirmed / 2 refuted, no new classes (`work/qa/qa-v3-result.json`). Fixed by
  `work/patch_r3.py`: render-frame mapping measured as `frame n shows base floor(0.8n + 0.24)` → `rframe()` for TWO_UP
  (23.333–26.433), SAM_CUT (27.533) and the "baby" punch (3.600); the "none" stamp (RMS onset); bubble-entry caption
  clearance (0.28 s, ≤ 0.15 s after the word); lone-word rebalance; the ring off on exits. **Every fix was verified frame by frame on
  v4** (`work/qa/v4check/`).
- **FINAL = `outputs/mfm-nursery-rhymes.sample.final.mp4`** (= v4; 1080×1920, 30 fps, 33.63 s, -16.6 LUFS, TP -4.5), with a copy at
  `~/Downloads/Onyx sample - My First Million (Moonbug).mp4`. Predictions were locked in the engine's RESULTS.md.
- **Next:** Affan's taste review → then his reaction video (`reaction/`) → the delivery email (with the ask). Open: a music
  bed (his track choice).
- 2026-10-05, Affan's review: the look is fine (*"a classic minimalistic Instagram style"*), but there are too few SFX in places.
  **Platform (PLAYBOOK § 0, added after this review):** the permission email named a YouTube Short, so by rule 1 MFM is
  **YouTube-first**. This pilot was built before the rule existed, in the Instagram look. Rebuilding it in the YouTube look
  (`presets/youtube-shorts/onyx-samples-youtube/`) is Affan's call. → **Affan, 2026-10-05: YES, rebuild it in the YouTube look**
  (first job of that preset), with the sound copied from the reference and short borrowed clips allowed. Work lives in **`yt/`**
  (storyboard, B-roll, the two build passes); the approved cut is reused as it is. The Instagram version stays as the alternative.
- **YouTube look, 2026-10-05:** `yt/storyboard.md` v1 written (20 shots, B-roll sources and the download list) and **APPROVED** (all downloads,
  hook title A, music last).
  Built in parallel, on test footage: `workflows/whip-slide.py` (the whip pass) and
  `presets/youtube-shorts/onyx-samples-youtube/kit/yt-captions.{js,css}` (the caption system); tests in `yt/work/whip-test/` and
  `yt/work/caption-test/`. The music bed needs Epidemic Sound, which loads only in a session started in the video-editor folder.
- MFM's own Shorts baseline (last 50): median 14K, p90 92K, max 451K (959K subs).

## The prospect
- **Show:** My First Million (@MyFirstMillionPod, 959K subs). Hosts Sam Parr and Shaan Puri. HubSpot owns it.
- **Said yes:** Shaan Puri, 2026-10-03 09:11 PK, from puri.shaan@gmail.com, replying "Sure", 9 min after the
  permission email went out. A thank-you draft is in Gmail (not sent).
- **Short named in the permission email:** "The $3 billion business built on nursery rhymes" (`PcTU0yaDfd4`, 42 s,
  posted 2026-09-26, 51.7K views, 634 likes) → `reference/their-short.mp4`.
- **Same story, earlier Short:** "How This Guy Built a $3 Billion Business From Nursery Rhymes" (`Q2fX7137Re4`, 48 s,
  2025-05-02, **923K views**) → `reference/their-2025-short-923k.mp4`.
- **Source episode:** "This guy sold 3 YouTube Channels to Blackstone for $3B" (`PKQo1Q2QkME`, 2025-03-25, 47:46),
  chapter "3B of nursery rhymes rollup" 0:00–21:55 → `raw/mfm-episode-moonbug.mp4`.

## Their two Shorts, compared (contact sheets in `reference/sheets/`)
| | 2025 version: 923K (`Q2fX7137Re4`, 48 s) | 2026 version: 51K (`PcTU0yaDfd4`, 42 s) |
|---|---|---|
| Captions | Big bold ALL CAPS, white with black outline, 2–4 words | Small sentence-case words in grey pills |
| Opening | "...most viewed YouTube channel is?" over a MrBeast collage, then "MR BEAST?" over MrBeast's face: a misdirect tease | "Do you know what the most viewed YouTube channel is? I don't. Cocomelon." over a static talking head |
| Graphics | Ranking table, Rene Rechtman's photo, **split screen** (Shaan on top, "MOONBUG ENTERTAINMENT RAISES $145 MILLION, DEC 2018" card below), article screenshots, "RENE MAKES $300M" in big type | Cocomelon/YouTube screenshots, one article, a "John Robson" photo; otherwise talking head |
| Speaker | **Shaan Puri** (the host who replied "Sure"), solo, in both | same |

**Do not claim the edit caused the 18x.** The 2026 Short was also a REPOST of a story that had already gone viral on the
same channel. The Content Engine's sequel/freshness rule says repeats get a fraction of the original ("seen it" swipes).
The honest line for the reaction video: *different edit AND a repost*. The comparison still shows exactly what their
higher-performing version did differently.

## The story (from their Short's transcript)
Moonbug: Rene Rechtman noticed that none of the top 100 most-viewed children's brands online were owned by big
studios. He raised ~$150M and did three deals: **Cocomelon $103M, Blippi $70M, Little Baby Bum $65M**. About
**$400M** in total equity and debt became a **$3B exit**, roughly a **10X** on the capital. Payouts: **Rene $300M**,
co-founder $300M, head of M&A $60M, CFO $20–30M, for **four years of work**.
→ Numbers, names, logos and a multiplier. Ideal for the GRAPHIC and CARD modes.

## Look
`presets/youtube-shorts/onyx-samples/README.md` (v0). **Accent:** to be sampled from MFM's branding (TBD).

## Constraints
- Fully automatic MP4 (chat-only route), no Premiere.
- No CTA or Onyx branding on the sample.
- Storyboard approval by Affan before the build (pilot rule).
