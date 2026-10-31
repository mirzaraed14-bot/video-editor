# RUN: "Why Conrad Murray Says He Didn't Kill Michael Jackson 😳" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-31 ~18:30): DELIVERED — `Conrad Murray Guilty.mov` (49.37 s) in Final Renders + Exports
- `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Conrad Murray Guilty.mov` = `X:\Claude Projects\Exports\Conrad
  Murray Guilty.mov` = `outputs/Conrad Murray Guilty.mov` (sha256 cf0d0a43…): H.264 38.7 Mb/s 1080×1920 30 fps, PCM 48 kHz,
  -14.0 LUFS / -1.6 dBTP. § 8 QA + § 9 answers in REPORT.md. Lessons appended to the AW LESSONS.md (12).
- NEXT: his review. A note = data + ONE finish render (memory feedback-fix-only-what-he-named): picture notes → edit
  `build/make_timeline.py` / `seq/edl.py` → `build/stage_a.py render renders/stageA_flow.mov` (~20 min, flow in-betweens)
  → `build/finish.py render …` → `build/export.py`; captions → `captions/captions.txt` → make_plan → render_caps → capcut_pass;
  audio → `build/dialogue.py` + `build/mix.py`.

## (previous) STATUS (2026-10-31 ~17:45): HIS TELLA RESOLVED → CODE BUILD
- His Tella (`brief/tella/guide.mp4`, 5:13; transcript `brief/tella/guide.json`; frames `proof/tella/sheet0-1.jpg`) → BRIEF
  DECISIONS 15-24. Sequence v2 = `seq/edl.py` (v1 kept `seq/edl.v1.*`): no Murray listening covers in B2; B5 = Hayes synced →
  WIDE two-shot (60M 602.46) under "For his death? / None. / None? / Absolutely nothing?" → Hayes listening on his "Nothing."
  → Murray "Michael Jackson … is a drug addict"; "Jackson" re-measured (ends 598.855, 20 ms fade; the 598.72 cut was
  inside the "-son"); AFTER PRISON card on the two-shot. **49.37 s / 1481 f at 30 fps.**
- Build (Patrick's kit, copied + adapted): `build/make_timeline.py` → `build/timeline.json` (49 shots, 14 zooms: 60M out,
  letterbox + verdict in; 7 transitions purple/cyan/peach); Proteus x4 SHAF2 / SHAF demo, x2 KATPM (`renders/*_prob*.mov`,
  no watermark); `build/stage_a.py track` + `win/shot_y.py` (per-run face heights so the mouth clears his caption line:
  corners <= 950 listening / 920 Hayes talking / 890 Murray talking) → `renders/stageA.mov` (60 fps, 2962 f).
  Bottom band exposed by a lift = `soft_fill` (blurred real bottom edge stretched + darkened; the hard mirror drew a
  collar "V" / his lips); M60 + M911 may expose 600 px (Murray leans in on "I did not kill" / sits low in the 911 clip),
  M911 at 1.95x. Letterbox bands = the clean rows only (CNN lower thirds can't show), tops 260 / 250 so the top glow bar
  stays below y200 at the end of the push; twin blur 40 / 60. Skin levelled per SETUP before his grade (R/G 2.7 → 1.5-1.7):
  `sat_level` M60 0.46 (+ gamma 0.85), H60 0.55, M911 0.72, H911 0.85.
- Captions: `captions/make_words.py` → `captions.txt` (61, 25 coloured, 6 accents incl. new PURPLE, Hayes italic,
  DR*G ADDICT) → `make_plan.py` → `render_caps.py` → `capcut_pass.py` → `renders/caps_capcut.mov`.
- Audio: `build/dialogue.py` → `renders/dialogue.wav`; `build/mix.py` (fresh Epidemic set `build/sfx/SOURCES.md`, swishes
  -21 dB on transitions, -24 dB on labels, no music) → `renders/mix.wav` -14.10 LUFS / -1.60 dBTP.
- Labels (DECISION 17): `finish.py lower_thirds` = AW glow rule drawn from the centre + name rises + role/year follow.
- **Topaz on Stage A DROPPED** (the per-shot stb reduce=2 + Chronos pass ran at ~7 of 49 segments in 25 min on the shared
  GPU, another session's finish render on it = ~3 h). Instead the 25p / 29p cadence is evened IN Stage A: every source < 60
  fps gets Horn-Schunck flow in-betweens (`stage_a.interp_frame`, seq_render.flow_interp's model, cached per frame pair;
  test: no held frames, no warping on lips / nose, `proof/flow_test.jpg`), head-lock anchors interpolated the same way.
  The stabiliser isn't missed on these tripod interviews (the head lock steadies every talking shot); the SD sources had
  their Proteus pass before Stage A. Said in the report.
- Audio fix (final-mix re-ASR): Murray's 2nd "Yes" is a near-whisper (-33 dB) and the B3 swish's pre-roll masked it: +8 dB
  on that piece (`dialogue.py SEG_GAIN`), that swish starts ON the cut, and a label entering with a transition shares its
  swish. Mix -14.00 LUFS / -1.60 dBTP; isolated re-ASR hears "Yes".
- RUNNING: `build/stage_a.py render renders/stageA_flow.mov` (~22 min). NEXT: `build/finish.py render`
  → `build/export.py` → `Conrad Murray Guilty.mov` → `win/final_edges.py` + § 8 QA on the FILE + final-mix re-ASR → copies
  to Final Renders + Exports → REPORT.md → LESSONS + memory.

## (previous) STATUS (2026-10-31 ~15:00): SEQUENCE PREVIEW RE-SENT → waited for his Tella (arrived 15:40)
- 15:00 he asked for the sequence video to record his Tella on: `seq/preview.mp4` re-rendered with BLEEPS = [] (no tone,
  measured), copied over `X:\Claude Projects\Exports\Conrad Murray Guilty - SEQUENCE PREVIEW.mp4` and sent; the separate
  "beat 5 uncensored" clip deleted from Exports (the main file now is that version). His Tella times = this file's times.
- Sent to him: `X:\Claude Projects\Exports\Conrad Murray Guilty - SEQUENCE PREVIEW.mp4` (= `seq/preview.mp4`, 49.23 s,
  1477 f, censor default ON: "drug" bleeped, label ANESTHESIA EXPERT) + `… (beat 5 uncensored).mp4` (8 s, B5 as written).
  Preview = rough 9:16 crops, beat/speaker/source tags, labels/card as plain text; no grade, captions, Topaz or SFX.
- Checked: every cut frame by frame (`proof/preview_edges.jpg`, no title-card or stray frames), 1 s sheet
  (`proof/preview_sheet.jpg`, no children, no CNN/CBS/60 bugs), preview re-ASR = the brief's words in order (+ Murray's
  "Nothing."), −14.6 LUFS (preview only; the build measures the encoded file).
- Source findings that need his call: BRIEF DECISIONS 8–14 (B5 speakers, B1/B2 Murray covers, KATPM copy, tightened
  pauses, SD full bleed). Defaults 1–7 sent at intake. **Answered: DECISION 1 = caption DR*G ADDICT, "drug" AUDIBLE**
  ("do it like dr*g addict" + "Audible, caption only"); `seq/edl.py` BLEEPS emptied; label ANESTHESIA EXPERT.
- **NO EDITING until his Tella.** Then: ingest it (memory/feedback-walkthrough-videos.md) → DECISION 15+ in BRIEF.md →
  catalog pass section in BRIEF → quote → code build from the Patrick kit (`projects/patrick-stewart-father-angry/build/`,
  `captions/`): Topaz Proteus on SHAF2 / SHAF_demo (+ KATPM if soft), skin R/G per source BEFORE the finish (Patrick
  lesson), captions re-ASR'd against the audio, labels, AW grade cool B1–5 / warm B6, soft swishes, no music → export.

## Job facts
- Format: AW short, 1080×1920, 30 fps export, full bleed, −14 LUFS / ≤ −1 dBTP, no music. Runtime ~48 s (45–52).
- Export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Conrad Murray Guilty.mov` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- The sequence is data: `seq/edl.py` → `seq/edl.json` (pieces with SPEAKER tags, forced-aligned edges `win/fa_all.py` →
  `win/fa/`, measured overrides, covers, cards, bleeps, xfades, push). Preview renderer `seq/preview.py`
  (`--uncensored`). In/out table `seq/inout.md`.
- Tools added here: `win/who.py` (voice match Hayes vs Murray), `win/listening.py` (finds Murray listening close-ups),
  `win/pitch.py`, `win/asr_file.py` (re-ASR a render). GPU scripts run int8 (the GPU is shared).

## Sources (raw/)
| Code | File | Origin | State |
|---|---|---|---|
| 60M | 60M_Murray_2013.mp4 | his drive copy of Sa2taDu2W5A (`E:\Bullshit Folder\Lonely\WORLD EXCLUSIVE- The man who killed Michael Jackson - 60 Minutes Australia.mp4`) | 1920×1080 25p; 60 bug bottom-left x≤280 |
| 60M911 | 60M911_Murray_2013.mp4 | M7TZWLflW54 | 1080p25; EXTRA MINUTES title card 0–2.52, bug x≤390 |
| SHAF2 | SHAF2_Shafer_court_2011.mp4 | Xv6vWTkEdU4 (HLN) | 640×360 30p; CNN lower third "Dr. Steve Shafer" from row ~293 (confirms the speaker) |
| SHAF_demo | SHAF_demo_court_2011.mp4 | fcbX7wIbgKU (HLN) | 360p; hands/IV close-up shot 66.57–71.1 used |
| VERD | VERD_verdict_2011.mp4 | Z5qT5p6aX00 (CBS) | 1280×720 29.97p; Murray profile 18–74 s; CBS bug x≥973 |
| KATPM | KATPM_full_p2.mp4 | 2WOCXNNunfk (Absolutely Definite 2/5) | 1280×720; CNN lower third from row ~553 |
| (unused) | KATPM_Katherine_PiersMorgan_2012.mp4 (wh3po5ErEh0, 360p), KATPM_full_p1/p3/p4/p5, TRIAL240 (Alvarez testimony, 240p) | | |

YouTube: the first pass hit the bot check (HTTP 429, 12:25); a plain retry 3 min later worked (never bypassed). Subtitle
requests kept getting 429: download video and subs separately.
