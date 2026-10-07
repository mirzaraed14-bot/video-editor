# RUN — nick-walker-never-mr-olympia ("The Body That Could Never Win", Nick Walker long-form)

## ▶ STATUS: DONE (the creator, 2026-10-07) — closed, nothing to resume
The creator finished the polish themselves on Sequence 24. This job is the reference for the channel's NEXT long-form:
the standing overlay look (90 % cards on the golden matte, nested host zooms, Black Video dips), the cut method
(WhisperX word edges, voiceprint every attributed quote) and the tools (`overlays/card.py`, `overlays/place-cards.py`,
`lanes/premiere/face-nests.py`, `brief/make-insert-plan.py`, `place-inserts.py`) all carry over.

## ▶ STATUS: THE CREATOR'S TELLA DIRECTION, PLACED + VERIFIED (2026-10-03) — resume here
Direction: `BRIEF.md` (Tella https://www.tella.tv/video/affans-video-7oqw, every "here" resolved to Sequence 24 by the
playhead timecode in the recording). Backup before this pass: `premiere-backup/ABW8-before-tella-direction.prproj`.
**Next action:** the creator's watch of Sequence 24 → notes → the polish (music under the payoff, SFX, title card, bleeps).
- [x] **Host zooms, nested**: `lanes/premiere/face-nests.py` + `transcript/face-zooms.json`, 25 runs, one linear zoom
  each at the creator's demo rate (100→104 over 3.17 s), cap 8 %; their own keyed first block skipped. 25/25 verified.
- [x] **Every overlay a CARD** (`overlays/card.py`): 90 % (1728x972), rounded corners, baked shadow, animated golden-yellow
  gradient matte, H.264 1080p60. 44 conversions of the third-party clips already on the timeline (V2; the V1 clip's VIDEO
  disabled, its audio on A1 untouched) + 24 new overlays (V3, the MG on V4). Zoom keyed in Premiere on each card
  (100 → +1.26 %/s, cap 5 % so the edge keeps bleeding). The creator's own fade-ins copied onto 1a and 5a; a 0.4 s fade to
  black before the name (0c). Their V2 builds (Shawn nest 84, the 06 continuation, the Bro Chat overlay) and the two
  IronMag stills were REPLACED by cards built from them; originals logged in `overlays/removed.json`.
- [x] **MG** (V4 74.73): Ronnie Coleman, 2003 Olympia front lat spread, shoulders / waist / sweep drawn on the host's words.
  **Flash** (78.32): Arnold, Haney, Yates, Coleman, Cutler, Heath with a white flash per switch.
  **IronMag highlighter** (272.15): the paragraph that actually SAYS "his physique is too blocky", wide then cut-zoomed,
  highlighter sweeping through the phrase on the words.
- [x] **Dips** (V4, the creator's Black Video keys) at 58.117, 105.167, 158.467: the peak frame renders pure black.
  **Light leaks** (V5, generated, `overlays/lightleak.py` v2) peaking on 235.967 and 350.583.
  **Captions** (V6, `overlays/captions.py` v3, + `renders/captions-press-v3.srt`) over the five press-conference clips.
- `overlays/place-cards.py --verify`: 68 cards exact, 0 problems; V1 41 videos disabled, A1/A2 unchanged; saved.
  Program frames rendered by Premiere: `review/proof2/proof-sheet.jpg` (+ the dip peak, mean 0.00).
**Sources:** 41 downloads in `broll/` (sources.tsv), contact sheets in `broll/sheets/`.
**Fact flags:** the IronMag article ran **14 Oct 2025** (page metadata), but the host says "2026" and the script
"31 Jan 2026"; "fighting for 10th place" is Bob, not Shawn; his 6th place was the **2025** Olympia (the brief said
"2024 or 2023"; he withdrew from both).

## ▶ STATUS: ROUGH DRAFT ON SEQUENCE 24 (2026-10-03) — resume here
The creator recorded, synced and cut their host bits on ABW8 · **Sequence 24** (V1 camera `C1321.MP4`, A1 the synced
Enhance-Speech mp3, 118 butt-joined blocks, 4:05). Asked: "put the 3rd party bits in between those blocks according
to the script", rough draft first, polish later. **Done, verified, saved:** 39 clip pieces at 17 insert points from
the LOCKED script v2 (`brief/insert-plan.json`, built by `brief/make-insert-plan.py`), host blocks shifted on V1+A1
together, **9:41.4**. `place-inserts.py --verify`: host blocks + voice at their exact shifted positions and full
length, 39/39 pieces exact, V1 157 / A1 157 clips, no gaps or overlaps. IronMag still on V2 over "His physique is
too blocky." 17 sequence markers = the polish to-do list (title card, lower thirds, mid-rolls, 5 BLEEPs, the name
landing in 5b, captions, the end card). Proof frames: `review/proof/proof-sheet.jpg`.
**Backups:** `premiere-backup/ABW8-before-3rdparty.prproj` + `Sequence24-before-3rdparty.xml` (FCP XML).
**Next action:** the creator's watch of the rough → their notes → the polish pass (graphics, bleeps, music, SFX).

| | | |
|---|---|---|
| project | `ABW8.prproj` (live auto-save path), **Sequence 24**, 1920x1080 60.00 fps | bin `/Nick Walker LongForm` |
| channel | Abundance Wisdom (ABW project; the script bridges to the channel's two Nick Walker Shorts), first face-led long-form | no long-form preset yet |
| format | long-form 16:9 | |
| script | LOCKED v2, 2 Oct 2026 (pasted in chat; ~9:15 target, publish Oct 4–5) | |
| constraints | sources ≤1080 H.264; every f-word bleeped; no gear/health talk beyond Nick's words; quote exactly | |

## How each cut was set (re-runnable)
`transcribe-windows.py` (WhisperX large-v3 + alignment, GPU) → `transcript/windows/<id>.json` for the host track
and a window round every scripted timestamp → each in/out set on the real word edges (`words.py`, `show.py`), never
the caption times → `brief/make-insert-plan.py` → `place-inserts.py --plan / --apply / --verify`.
Host block text per V1 block: `transcript/host-blocks.txt`.

## Lock conditions (the script's four), resolved by measurement
1. **5e is SHAWN RAY**, not Bob (voiceprint vs Bob/Shawn references: Shawn 0.60 / 0.71, Bob −0.05). Caption it
   "SHAWN RAY · 4 DAYS LATER" — the script's biggest reversal.
2. **5j is his DAD** (0.80 against the dad's other lines; interviewer 0.24, mom 0.07) → the video ends on Dad.
3. **5b: the name lands at ~1:08:51.3** in the finals (the crowd erupts after a 5 s held pause; ASR cannot hear it).
   Marker on the timeline at 415.9 s.
4. **1c is GREG** (a different, high voice, median 179 Hz vs Nick 100 Hz, talking TO Nick on Greg's channel) → 1c
   and the Greg twist line stay.

## Flags for the creator
- **FACT: "he'd be fighting for 10th place" is BOB, not Shawn** (voiceprint Bob 0.70; he opens "here's the funny part,
  Sean"); Shawn only agrees ("That's a true statement. I'll stand with you on that.", kept in 4b). Two recorded host
  lines credit Shawn: the cold open's "a two-time Mr. Olympia runner-up said he'd be fighting for 10th place" and
  "On Bob's show, Shawn Ray... answers that exact quote". The script's own rule is "quote him exactly".
- The T-shirt line ("And Nick? He printed the line on a T-shirt.") was not recorded, so the shirt still is in the bin
  but not placed; the optional 2 s Bob replay skipped (the host says "You already heard it at the start").
- 3b sits after "According to him, his peak didn't go as planned." (a line the creator added), so "him" reads as Nick.
- 2b keeps Nick's ~5 s silence mid-sentence ("it sucks because ... second year in a row"): the voice-cracking beat.
- 4d keeps Bob's "You could go as high as fourth" in front of Nick's "still low-balling me", which answers it.
- Interviewer, not a parent: "none of that f***ing matters because it's Mr. Olympia" (not used).
- 0c freeze: the broadcast is a wide stage shot at that moment, so the freeze holds Nick and Samson, not Bob's face.
- IronMag still fills the frame but the headline is small: push in or crop on it in the polish.
- Clip audio is raw (no level matching yet); 5 f-words marked, not yet bleeped.

## Steps
| # | Step | Status | |
|---|------|--------|---|
| 1 | Intake | done | 17 sources + 2 stills in the bin; host voice copied to `raw/host-voice-enhanced.mp3`; camera read in place |
| 2 | Rough cut | done (creator's own host cut) + **3rd-party inserts placed** | see STATUS |
| 3 | Audio polish | — | |
| 5 | Graphics | — | the markers are the list |
| 6 | SFX / music | — | |
| 7 | Review | **next: the creator watches the rough** | |
