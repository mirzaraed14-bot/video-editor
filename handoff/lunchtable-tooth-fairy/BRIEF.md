# lunchtable-tooth-fairy: Onyx sample Short for The Lunch Table (TFG Vlogs) (batch 9, ENHANCE, extended)

## ▶ STATUS: resume here
- 2026-11-12 22:12 (main) **SIGNED OFF (YouTube look) after fix round 1, checked from the Exports copy** (`X:\Claude Projects\Exports\lunchtable-tooth-fairy.yt.final.mp4`, identical to outputs/): 37.34 s, 1119 f, 29.97 fps, -12.1 LUFS / -2.2 dBTP, decodes clean. Every A shot shows its speaker; ladder 10c -> $5-10 -> $20, pillow + dime, the $20 bill, the receipt $5.84 (Delta Dental 2026 poll, via Delta Dental of Virginia's copy + Dentistry Today) now clear of the ladder, THIS MONTH: $5, pillow and calendar clear of the watermark. Flags for Affan: names not confirmed (label TFG VLOGS / LUNCH TABLE #48); the Mia shot holds 4.9 s of face (ladder on screen); "This is so stupid" given to the middle man (cross-talk, medium confidence); 37 s. Instagram look not built.
- 2026-11-12 FIX ROUND 1 DONE (v6 = final, same specs: 37.34 s, 29.97 fps, -12.1 LUFS / -2.2 dBTP, cue_check PASS, decode clean): receipt font 186 -> 150 px (clears the $20 rung by ~100 px); pillow moved down 75 px and the calendar scaled 0.85 and lowered inside their split panels (>= 40 px clear of the watermark). Watermark and captions untouched.
- 2026-11-12 (Sonnet builder): DONE. `outputs/lunchtable-tooth-fairy.sample-yt.final.mp4` (= v4), 37.34 s, 1119 f, 29.97 fps, 1080x1920, -12.1 LUFS / -2.2 dBTP, copy `X:\Claude Projects\Exports\lunchtable-tooth-fairy.yt.final.mp4`, proof sheet `outputs/lunchtable-tooth-fairy.sample-yt.proof-sheet.jpg`. cue_check PASS (all 9 cues -19.4..-19.6 dB under the voice, none weak on a phone), joint_sync 2/2, crop_audit (no white divider in any face frame), decode clean. One Sonnet reviewer: no blockers/majors.
- Rebuild: `bash work/cut/run_cut.sh` (repo root); `python yt/build_spec.py`; `uv run presets/youtube-shorts/onyx-samples-youtube/kit/yt_faces.py projects/<job> --step 1`; `python yt/clamp_faces.py`; `python yt/build_spec.py`; `yt_build.py <job> vN`; `python work/yt_finish.py vN+1` (grade + sharpen); sound: `python yt/tune_cues.py` then `yt_build.py <job> vN --skip picture,overlay`.
- Speakers (from the PICTURE, work/cut/msheet.py): hook L (grey tee); dime L; "What is that? ... choking hazard" M (pink hoodie); "five, ten dollars?" L; "I think it's customary ... at least a" M; "An Andrew Jackson?" R (onesie); Mia line M; "$20 minimum. In 2026." R; "This is so stupid" M (cross-talk with R, medium confidence); podcast line L; "First one ... $5" R; "Also ... She gave me $5" L.
- Names: no one is addressed by name (Sam, Kayla, Rafa, Mia are family). Label = TFG VLOGS / LUNCH TABLE #48, watermark THE LUNCH TABLE. Flag: Brandon / Abe / Steve unmatched to faces.
- Receipt: $5.84 = Delta Dental 2026 Original Tooth Fairy Poll (Feb 25 2026), copy at deltadentalva.com/newsroom/tooth-fairy-gives-kids-raise.html (deltadental.com returned 403 to automation); reference/delta-dental-poll-2026.txt.
- Flags: (1) Mia shot (M) is 4.9 s of bare face (ladder on screen). (2) ladder steps aside for both splits (they own the low band). (3) reviewer minors: watermark overlaps pillow top edge / calendar header; the cut to M at ~11.0 s lands ~0.2 s before L's "$10?" ends (free-cut lead). (4) one grade for all three cameras (the kit's grade is per shot kind, tuned on all three). (5) runtime 37.3 s (sequencing said ~40). (6) real-$20 scan shows a specimen serial number.
- Audio words vs sequencing: none differ. Cut out: a false start "That's a-" and an interjection "bro" between "What is that?" and "They were trying", L's "that you're in", R's stutter "in-" after "minimum". Caption "FIVE TEN DOLLARS?" (audio "five, ten dollars"); transcript JSON keeps "$10".

## The Short and the point
Their permitted Short: StunDjBNuT4 "How Much Did You Get From The Tooth Fairy?" (33 s): the question → $10 → the dime → "subway beggars" /
jingling → a quarter; it stops before the $20 argument and the button. Ours rides the number up the ladder (a dime → $10 → an Andrew
Jackson → "$20 minimum in 2026") and lands on the joke, with one real number on screen.
**The viewer gets:** a laugh and a number to argue about: what the tooth fairy pays now. **Title:** The Tooth Fairy Got Expensive
Weakness (from the sequencing): comedy, no famous face, no lesson; their Shorts already do ~25K median (1.9 % of subs).

## Beats: `projects/_onyx-batch9-2026-11/SEQUENCING.md` § 4 (6 beats; DIRECTION.md maps each to the episode)

## Teardown: their Short → ours
| Axis | Their Short (33 s) | Ours (~40 s) |
|---|---|---|
| Hook, first 3 s | the question over one face | the question under THE TOOTH FAIRY GOT EXPENSIVE |
| Structure | stops on a quarter, no punchline | climbs a price ladder to "$20 minimum in 2026" and ends on the "$5 this month" button |
| Risky lines | "subway beggars" kept | dropped (too risky in a sample) |
| Visuals | three face crops | the ladder, a dime under a pillow, a real $20, one checked average from Delta Dental's poll, a calendar flip |

## Catalog pass (CLAUDE.md rule 5), main, 2026-11-12
Read all of `research/effects-catalog/CATALOG.md` and looked at all 79 reference stills (two contact sheets, 2026-11-12).
- Used here: FX-71 Funnel Count (the price ladder rungs), FX-33 Dust Void Drop (the $20 bill), FX-68 Data-Point Clipping (the one real
  number pinned at the ladder), FX-42 Kin Tag (labels).
- New to Onyx samples: a running price ladder carried through a comedy bit; a real poll number as the only "fact" in a joke.
- Not used: maps, documents, dark documentary treatments (wrong tone for a comedy table).

## Better than the last one of its kind
The last comedy-style samples ran the bit as is; this one gives the joke a spine (the climbing number) and a checkable fact to argue about.

## Downloads (logged before pulling)
| File | Source | Size | Use |
|---|---|---|---|
| source/lunchtable-48-XdkmCOQVEb4-2100-2640.mp4 | YouTube XdkmCOQVEb4 "Steve Is BACK ON YOUTUBE! / Lunch Table #48", section 2100-2640 s, forced H.264 (pulled 2026-11-12 19:33 PKT through lock.sh) | 118.5 MB, 1920x1080 29.97 fps, 540.0 s | the episode window |
| (reference) `_onyx-batch9-2026-11/_shorts/lunchtable.mp4` | YouTube StunDjBNuT4 (their permitted Short), pulled by the hub 11-12 | 9.3 MB, 1080x1920 29.97 fps | teardown |
| reference/delta-dental-poll-2026.txt | https://www.deltadental.com/tooth-fairy/press-release/ (page text, verifying the national average) | small text | receipt card number |
| reference/us20.jpg | https://upload.wikimedia.org/wikipedia/commons/b/bf/US20-front.jpg (Wikimedia Commons "US20-front.jpg", US Treasury work, public domain) | 13.7 MB, 7348x3092 | the Andrew Jackson bill card |

## Builder log (Sonnet, 2026-11-12)
- 19:5x: raw/secA_160.mkv = source 160-370 s (raw t + 2260 = episode s), transcribed (WhisperX, transcript/words.json). Strips measured: dividers are WHITE at x 640-663 and 1275-1297 (strips L 0-639, M 664-1274, R 1298-1919: the middle one is only 611 px, narrower than a full-height 9:16 window 607 + margin: every A crop is zoomed >=1.12 and clamped inside its strip).
- Receipt number VERIFIED: $5.84 (2026 poll, released 2026-02-25; from $5.01 in 2025) at Delta Dental of Virginia's own newsroom copy of the press release (deltadental.com's page returns 403 to automation); proof text in reference/delta-dental-poll-2026.txt.
- Names: no one is addressed by name in the segment ("Sam", "Kayla", "Rafa", "Mia" are family, not the three men). Show label only; flag.
