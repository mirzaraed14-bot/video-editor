# readystate-old-ankle-sprain: Onyx sample Short for The Ready State (Kelly Starrett) (batch 9, ENHANCE)

## ▶ STATUS: resume here
- 2026-11-12 20:45 (main) **SIGNED OFF (YouTube look), checked from the Exports copy** (`X:\Claude Projects\Exports\readystate-old-ankle-sprain.yt.final.mp4`, identical to outputs/): 41.58 s, 997 f, 23.976 fps, -12.2 LUFS / -2.3 dBTP, decodes clean. Looked at 2 fps contact sheets of the whole file + 8 full frames: hook card alone with captions 0-3.1 s on his face; anatomy shows only what he says (outside ankle bone, red only on "jammed forward"); drawn peanut, split anatomy (bone pinned), 20-30 PULSES, BEFORE/AFTER range, cut on "Lisa?". The 37.6 s "ambience hole" measured: a 50 ms dip at a word gap (-35.8 dB RMS), no dead air: not a defect. Flags for Affan: the mumbled "I just have" at ~15.5 s (captions say I JUST HAVE); the label rises in beat 3 (13.2 s), his face is half out of frame in beat 2; the beat-2 caption sits over his hand on the ball at 5.5-6.3 s; 20-30 PULSES sits on his sweater, not the low band; no ring on the bone (the handheld drifts). Instagram look not built (Affan: YouTube only for now).
- 2026-11-12 (builder, Sonnet) **DELIVERED, YouTube look**: `outputs/readystate-old-ankle-sprain.sample-yt.final.mp4` (= sample-yt.v3), copy `X:\Claude Projects\Exports
eadystate-old-ankle-sprain.yt.final.mp4`, proof sheet `outputs/readystate-old-ankle-sprain.sample-yt.proof-sheet.jpg`. 41.58 s, 997 f, 23.976 fps, -12.2 LUFS / -2.3 dBTP. 9 soft-swish cues, cue_check PASS (all full -19.3, none weak on a phone), no bed. Reviewer (Sonnet): no blocking defects.
- Rebuild: `bash projects/readystate-old-ankle-sprain/yt/run_all.sh <v> [grade|overlay]` from the repo root (the POP grade pass is ~30 min; `overlay` = captions/label/count/mix only; picture only: `yt/run_picture.sh`). Cut: `work/cut/run_cut.sh` + `retime.py`; crops `yt/crops.json`; cues `work/cue_loop.py --write`; promote `yt/finish.py <v>`. Cut/EDL/transcript (`transcript/cuts.json`, `outputs/<job>.transcript.json`, `outputs/<job>.mp4` 1080x1920) are reusable for the Instagram look.
- FLAGS: (1) "I just have a peanut" (15.5 s): the onset is mumbled; WhisperX "I just have", faster-whisper "Let's have"/"So I have": captions say I JUST HAVE, listen. (2) Hook starts on the "or | you" boundary (cut at 99.37 s in the source): listen to the first 0.2 s. (3) The peanut is DRAWN (his held one is hand-covered / ~100 px). (4) No ring on the bone (handheld close-up moves > 20 px). (5) 20-30 PULSES sits over his black sweater (y ~500-760), not the low band: hands + ball fill y 1300-1650. (6) Label rises at 13.2 s (beat 3, "So here's a simple way", his first clear face frame), not in beat 2 (his face is half out of frame there). (7) Hook card gone by ~3.1 s (the hook shot is 2.75 s: audio gives no more). (8) Beat 2's caption (5.5-6.3 s) sits over the ball contact; the ball/foot at the bottom of beats 5-6 reach y ~1625 (source framing, no room to lift). (9) Captions white; red wipe kept only on JAMMED FORWARD / AND LIMITS THAT. (10) Name label prints "DR KELLY STARRETT" (the kit strips the full stop). (11) AMBIENCE HOLE warning at ~37.6 s ("dorsiflexion | massively" pause cut, -8 dB room-tone dip). (12) Anatomy tick at 12.9 s sits ~25 px from the right edge. (13) Payoff report: first B-roll at 6.3 s (direction put the card there).
- Audio vs sequencing: none other than flag 1 (hook words "You sprained it ..." without "or"; beat 2 without "When I dorsiflex my foot,"; beat 6 from "when you just get").

## The Short and the point
Their permitted Short: YiN--sfQCCI "Ankle Mobilization with a Lacrosse Ball Peanut to Improve Dorsiflexion" (uploaded 6 Nov 2026, 108 s,
5.5K views on 391K subs = 1.4 %). A "Daily Dose" demo filmed vertical; the point ("an old sprain you never rehabbed still limits you") is
buried at 1:35 after 95 s of demo.
**The viewer gets:** why an old sprain still limits your ankle (the outside ankle bone stays jammed forward) and the 2-minute fix with two
taped lacrosse balls. **Title:** Your Old Ankle Sprain Isn't Healed

## Beats: `projects/_onyx-batch9-2026-11/SEQUENCING.md` § 1 (7 beats; DIRECTION.md maps each to the Short)

## Teardown: their Short → ours
| Axis | Their Short (108 s) | Ours (~48 s) |
|---|---|---|
| Hook, first 3 s | "Daily dose, got a simple mobilization of the outside ankle bone" over a hand on an ankle | Kelly pointing at the lens: "You sprained it and you never rehabbed it" under YOUR OLD ANKLE SPRAIN ISN'T HEALED |
| Who / what by 5 s | never named | the claim, then DR. KELLY STARRETT / THE READY STATE |
| The why | told, never shown | a side-view drawing: the outside ankle bone gliding back, then stuck forward in red |
| The how | 95 s of continuous demo, repeated | the peanut on an exhibit grid, the trapped-bone glide, 20-30 PULSES, then BEFORE / AFTER range |
| Ending | "See you tomorrow" | his deadpan button: "positive thinking ... Don't you, Lisa?" |
| Captions | none | seam captions from frame 1 |

## Catalog pass (CLAUDE.md rule 5), main, 2026-11-12
Read all of `research/effects-catalog/CATALOG.md` and looked at all 79 reference stills (two contact sheets, 2026-11-12).
- Used here: FX-21 line style for the anatomy (white hairlines on charcoal, one accent), FX-70 Ring and Benchmark (the ring on the bone;
  the BEFORE / AFTER arcs), FX-25 Exhibit Grid (the peanut as an exhibit), FX-71 Funnel Count (20-30 PULSES), FX-42 Kin Tag (the label).
- New to Onyx samples: a moving anatomy diagram, a product shown as an exhibit cut from the client's own footage.
- Not used: maps, headlines, photos (nothing to prove: it is his own demo), any glow or depth type.

## Better than the last one of its kind
The last how-to sample (Ron's 9mm) explained with props on a table; this one shows the mechanism itself (the bone that jams) before the
fix, so the viewer understands WHY the fix works, and lands the creator's own joke as the button.

## Downloads (logged before pulling)
| File | Source | Size | Use |
|---|---|---|---|
| source/readystate-YiN--sfQCCI.mp4 | YouTube YiN--sfQCCI, pulled 2026-11-12 14:28 PKT by the hub (copied from `_onyx-batch9-2026-11/_shorts/readystate.mp4`) | 27.4 MB, 1080x1920 23.976, 108.2 s | the source (their own recording) |
