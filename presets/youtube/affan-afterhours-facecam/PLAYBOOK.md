# PLAYBOOK — affan-afterhours-facecam (how a job in this style runs)

The channel PLAYBOOK (`../affan-afterhours/PLAYBOOK.md`) still governs intake, the creator's cut, the voice handoff,
the music and the learning loop. This file is only what DIFFERS in the face-cam style. Numbers: `README.md` § 1.

## Per pipeline step

| Step | In this style |
|---|---|
| 2 Rough cut | unchanged. The creator's own pace is 200+ words/min with 2–3 pauses over a second per video: cut tight, keep the setup→punch pauses (channel PLAYBOOK § C row 2). |
| 3 Audio | as the channel: bake any mute/bleep, hand a voice bounce for their Enhance Speech pass. |
| 4 Grade | none of ours. The LED room is the look (luma ~0.3, bright); the creator grades if at all. |
| **5 Graphics → "5 Overlays"** | **No graphics plan of cards.** The plan is an OVERLAY plan: 3–4 runs per minute of ~4 s, almost all game footage (Extended Look first, trailers, old-GTA gameplay for the "back then" lines), placed where the line names a thing in the game. **Cards at 1–1.6 per minute** (the 170k video has 11, the 35k has 4): the sentence being spoken, set in type, on a quotable declarative punchline or a quote — never on an aside, an opinion or a joke played straight (README § 4b). Found artefacts (a real photo, a screenshot, a callback to an earlier thumbnail) cut in raw and unannotated. **Slow the inserts, not the face:** game B-roll at 0.5x, an action take at 0.2x for comedy, an interview clip near-frozen as a reaction shot. One optional meme insert. The canned SUBSCRIBE animation twice, bottom-left, mid-sentence. The `graphics-plan.json` cell kinds used: `b-roll` (game footage, with the exact Extended Look timecode), `screenshot`, `clip-insert` (a real interview/clip, channel LESSONS 2026-09-20), `poster` (rare). Every Google/Instagram picture goes through the HQ check and the channel overlay frame. |
| **5b Face motion** | **`lanes/premiere/face-nests.py`** with this style's picks: cut zooms at ~5/min, +25 % (range +17–40, one bigger hit allowed), hold ~1 s; gradual push ~1 %/s capped at 10 %; picks land on the word that lands the clause. Add a **slow-down — 0.8x, pitch kept, and budget around TEN of them** (CORRECTED 2026-09-22 from the creator's own finished edit; the old "0.6x, 1–3 per video" came from the two reference videos and is wrong for their own work — see [`HUMOR.md`](HUMOR.md)). They go on the beat a joke lands or a claim drops, never on a fact, and a comic BUILD gets the whole run slowed, not just its last line. At most one or two **hard chops** (the word cut off) where the line is a joke — write both as picks in `transcript/face-zooms.json` so the creator can veto them by name. |
| 6 SFX | unchanged (`sfx-plan.py`, channel A3–A5 map); the first sound at 0.000. Whooshes on cuts to game footage, pops on the rare poster. **Overlays: a POP on every overlay entrance and every internal switch** (the creator 2026-09-30: "wherever the overlay switching… a sudden click… nice and poppy"), Epidemic "Cartoon, Pop, Mouth, Finger" at −6 dB clip level (−6 dBFS peak), exits back to the face silent; tool `projects/gta6-hurricanes/overlay-sfx.py`. |
| Music | the creator's, per section, with a silence before each turn (channel LESSONS 2026-09-20). **The music DROPS OUT under every cut zoom** (the creator 2026-09-30: the zoomed block plays voice only so the point lands): razor the bed at the zoom's in and out and lift what is inside, no ripple, no fades; the small 103–105 % jumps count. Tool `projects/gta6-hurricanes/music-dropouts.py`. |
| 7 Review | the creator's. Then phase D of the channel PLAYBOOK, always. |

## The cold open (first 60 s)

Face first, a game montage inside the first 10 s, and the first minute cuts 1.5–2.5x faster than the body
(15/min in the 170k video, 44/min in the 35k one). Plan the first minute's overlays at twice the body density.

## Definition of done for a draft in this style

- visible changes 20–25/min over the whole runtime, first minute higher — measured by `workflows/style-probe.py` +
  `style-report.py` on the draft export, the same tools that measured the references;
- face on screen 80–90 %; no overlay run over ~25 s unless it is the evidence; no stretch of face over ~12 s without
  a cut zoom or a jump cut;
- cut zooms ~5/min at +25 %, hold ~1 s; push ~1 %/s;
- **~10 slow-downs at 0.8x** with pitch kept, clustered on the comic runs rather than spread evenly; ≤ 2 hard chops;
- opens and closes on the face.
