# ruslan-chappelle-kirk-receipt: Onyx sample Short for Ruslan KD (batch 9, ENHANCE, extended)

## ▶ STATUS: resume here
- 2026-11-12 21:57 (main) **SIGNED OFF (YouTube look), checked from the Exports copy** (`X:\Claude Projects\Exports\ruslan-chappelle-kirk-receipt.yt.final.mp4`, identical to outputs/): 47.6 s, 1428 f, 30 fps, -12.1 LUFS / -2.2 dBTP, decodes clean. Looked at 2 fps contact sheets of the whole file: leaked clip framed + LEAKED tag under the hook card; Ruslan's label once; MSG split; Charlie Kirk photo; "NEGATIVE" split; the "...BUT I FEEL BETTER." callback; Hollywood Bowl still; the tweet card word for word with read-along highlights; IT'S SINISTER & UN-AMERICAN. No PIP window or neon letters half-cut, no profanity. Flags for Affan: the leaked clip and the Hollywood Bowl still are soft (source limits); 47.6 s runtime; "justifiable even today" is not on the tape (the cut goes "are justifiable" -> "It's sinister and un-American"); the most politically charged sample in the batch. Instagram look not built.
- 2026-11-12 DONE (Sonnet builder, YouTube look only): outputs/ruslan-chappelle-kirk-receipt.sample-yt.final.mp4 (= v6), copy X:\Claude Projects\Exports
uslan-chappelle-kirk-receipt.yt.final.mp4,
  proof sheet outputs/...sample-yt.proof-sheet.jpg. 47.6 s, 1080x1920, 30 fps, -12.1 LUFS, true peak -2.2 dBFS; 9 soft swishes all -21 dB under the voice (label -23), cue_check PASS (5 read "WEAK on a phone" by 0.1-1.3 dB: soft by design).
  Reviewer (Sonnet, defects only) found: tweet card touching captions, highlights accumulating, Kirk card touching captions: all fixed in v6; left: soft Hollywood Bowl still, a head clip at f627.
  Reproduce: `python work/cut/make_edl.py /tmp/video-editor/<job>/cuts.json transcript/cuts.json` -> `bash .claude/skills/rough-cut/scripts/splice.sh projects/<job>` -> `python yt/build_spec.py` (renders yt/cards.py via uv)
  -> `yt_faces.py --step 1` -> `yt_build.py <job> vN --skip overlay,mix` -> `grade-picture.py` -> `sharpen-picture.py --mask 0.55 --sharp 0.40` -> `yt_build.py <job> vN --skip picture,overlay`.
  Cut/transcript/EDL reusable for the IG build. Kit change (backup .bak-2026-11-12-fxsplit): a SPLIT top may set fx_out (default 0.5, unchanged).
- Audio differences vs the sequencing: "maniac" is a clipped "armed maniac" (ASR "R-maniac"; the tweet says "armed maniac"; captioned ARMED MANIAC); the sequencing's
  "justifiable even today" is NOT on the tape: he says "justifiable, even-and even encouraged", so the cut ends on "are justifiable" (hard cut to "It's sinister...").
- Grade: the default POP crushed the dark shirt/beard, so the gentler Drea-room A look (spec grade_look) is used; splits take the mild DOC look.
- Flags: the Chappelle clip is only ~420x560 px inside the episode window (soft; floated at 560 px, never full-bleed); the Hollywood Bowl picture is a NY Post screenshot of the attack video
  (soft, real); the leaked-clip full-screen cutaway (file 4-9 s, with burned-in captions) was not used.

## The Short and the point
Their permitted Short: k9YzSZzcUoY "Dave Chapelle makes a disturbing joke…" (99 s): the episode's opening up to "resorting to the very same
things that he is critiquing"; it has no receipt. Ours keeps that moment and ends on the receipt that turns it: Charlie Kirk publicly
defended Chappelle in May 2022 after the Hollywood Bowl attack.
**The viewer gets:** the hypocrisy, with the receipt. **Title:** Charlie Kirk Once Defended Chappelle

## Beats: `projects/_onyx-batch9-2026-11/SEQUENCING.md` § 3 (4 beats; DIRECTION.md maps each to the episode)

## Teardown: their Short → ours
| Axis | Their Short (99 s) | Ours (~40 s) |
|---|---|---|
| Hook, first 3 s | a blurred zoom of the clip, small captions | the leaked clip itself, framed and tagged LEAKED, under CHAPPELLE'S LEAKED JOKE ABOUT CHARLIE KIRK |
| Layout | clip top / Ruslan bottom for 99 s | Ruslan, MSG, Charlie Kirk's face, the joke's own words, the attack, the tweet |
| Ending | his opinion ("resorting to the very same things") | the receipt: Kirk's own 2022 tweet defending Chappelle, landing on "It's sinister and un-American." |
| Length | 99 s | ~40 s |

## Catalog pass (CLAUDE.md rule 5), main, 2026-11-12
Read all of `research/effects-catalog/CATALOG.md` and looked at all 79 reference stills (two contact sheets, 2026-11-12).
- Used here: FX-29 Float Frame (the leaked clip, the photos), FX-27 Red Word Quote (the joke's last words over the frozen clip; the button),
  FX-34 Read-Along Highlighter (the tweet as he reads it), FX-42 Kin Tag (his label).
- New to Onyx samples: a rebuilt social post read along phrase by phrase; a callback quote over a frozen frame.
- Not used: maps, charts, the Harvard poll (left out of the sequence), any slow-motion or dramatic treatment of the attack.

## Better than the last one of its kind
The last commentary-style sample showed opinions; this one ends on a primary source the viewer can check (the tweet, word for word).

## Downloads (logged before pulling)
| File | Source | Size | Use |
|---|---|---|---|
| source/ruslan-xArul8ZoqkM-0-360.mp4 | YouTube xArul8ZoqkM, section 0-360 s, forced H.264 (pulled 2026-11-12 19:25 PKT through lock.sh, after Affan lifted the block) | 55.5 MB, 1920x1080 30 fps, 360.0 s | the episode window |
| (reference) `_onyx-batch9-2026-11/_shorts/ruslan.mp4` | YouTube k9YzSZzcUoY (their permitted Short), pulled by the hub 11-12 | 28.9 MB, 1080x1920 30 fps | teardown + the clip's sharper copy if it is |
| assets/img/msg.jpg | Wikimedia Commons "Madison Square Garden (MSG) - Full (48124330357).jpg" (CC BY 2.0), via upload.wikimedia.org (commons.wikimedia.org does not resolve here; en.wikipedia API lists it) | ~1-3 MB, 5411x3044 | beat 2 split panel: MSG |
| assets/img/kirk.jpg | Wikimedia Commons "Charlie Kirk (53952923573) (headshot cropped).jpg" (CC BY-SA 2.0), via upload.wikimedia.org | ~0.5 MB, 1222x1689 | beat 3 float frame: CHARLIE KIRK |
| assets/img/cand/* | Bing image candidates (curl, workflows/img-candidates.py) for the Hollywood Bowl attack, May 3 2022; up to ~10 small files, one picked | < 5 MB total | beat 4 float frame: HOLLYWOOD BOWL, MAY 2022 |
- 2026-11-12 audio-only fix: five WEAK cues raised ~1.5 dB (all now -19.5..-21.5 dB under the voice), cue_check PASS none weak; AAC remuxed, video stream copied bit-identical (md5 checked); previous file work/final.before-audiofix.mp4.
