# jeremyminer-google-88k-reaction: Affan's reaction to our Jeremy Miner sample (ABW8 sequence "Jeremy Miner reaction")

## ▶ STATUS: resume here
- **2026-10-13 PREPARED IN ABW8 (main session)**: "Jeremy Miner reaction" razored at every beat/view edge, layout (171 clip edits, drift/eases baked, --layout-check: 0 leaks at keys), V3 showcase frames / V4 MG / V5 captions, house chain +6 dB into -6 dBFS on all 101 A1 clips, 55 SFX on A2 + A4 (a new rule in apply.py: overlapping sounds alternate tracks, never split), Swing bed on A3 at -19.8 dB from 4.93 s with a 2 s tail fade, 25 ms Volume ramps at the hard sample edges 73.40 / 233.90 / 247.28 / 275.38 (tools/afade.py), --verify 0 problems. Proof: `work/grabs-sheet.jpg`. Main-session edits to build_plan.py: the 600M stat says "VIEWS THROUGH short form" (his words), every spotlight lands on a hit-soft. He exports.
- **2026-10-13 PHASE 2 DONE (graphics plan, Reaction A of the variety matrix; Premiere untouched).** `build_plan.py` → `plan.json`
  (+ `facex.py`), every overlay rendered and probed: `overlays/captions.mov` (323.40 s, 60 fps) + 33 `overlays/mg/*.mov` (1080x1920, 60 fps,
  frames == round(dur*60), all checked), `overlays.py --check` 0 errors / 0 warnings.
  - **Hero move:** the HIS SHORT → OUR EDIT wipe (`hero-wipe`, ba_wipe rtl, 140.92-146.50, on "so how do we make this into something that
    everyone watches?"): their Short (reference file) and our YouTube cut in one card, line sweeps at 1.0 s, parks half/half 1.2 s, reveals
    at 2.9 s (sweep measured in the render). Echo: `wipe-variants` 247.35-252.33 (YOUTUBE → INSTAGRAM at the SAME sample seconds on "this is
    the same video, but the aesthetics completely change"), landing exactly on VLC's paused Instagram frame (sample 14.133, frame-matched).
  - **Counts:** 27 MG graphics = 28 events (1.23 per 10 s of his 227.7 s talk): select 8, cursor 1, spotlight 3 (pointing 43 %), stat 3,
    title_card 2, compare 2, checklist 2, steps 1 (left glass verdict cards, wipe-in, Playfair accent word), ba_wipe 2, label 2 (7 %),
    hook_title 1, channel_card 1 (474K, read off work/channel.html "4.74 lakh"); + 6 showcase frames (frame track). Face-only 76.5 s = 23.7 %
    (12 beats, 5 punch-ins incl. 165 on "might."). Camera: 5 eased snap-zooms (OBJECTION thumbnail, black bar, title, stock caption, sound disc;
    + 2 returns) and drift on the grid + the Short-page hold. SFX 52 cues, top sound whoosh-soft 25 %.
  - **Better than Rob Dial:** shown not told (the wipe), 0 pills in the top band, no label echoing the captions, no card over 6 s, our sample
    framed (showcase), punch-ins inside beats, the channel card under his chin.
  - **Review:** own pass over 11 sheets (`work/review-*.jpg`, index `work/review-index.txt`) fixed: taskbar in the title / bars / sound views,
    two cursors on the title (his real one is there: drawn one dropped), chip clutter, F3's fast lean (beat now starts 79.82), F10's last 9
    frames on the next take (ends on the camera edge 281.28), labels over the showcase tag. Fresh-eyes reviewer (sonnet), 2 rounds: round 1
    found sel-overlay's box wrong (fixed), steps row 2 visible < 1 s (fixed), card text echoing captions (cmp-who, cmp-mood, sel-his
    reworded), "600M+" (now 600M); its hero-wipe "sync" finding was a misread (line position measured in the .mov). Round 2: no defects.
  - **For the main session:** apply as usual (`--razor` → re-dump → `PYTHONUTF8=1 python build_plan.py` picks dump-layout.json → **re-run
    facex.py** (build_plan wipes face_x) → `--layout` → `--window` → `--overlays` → `--verify`). Tracks: screen 0, face 1, frame 2, MG 3,
    captions 4. music = ES_Swing - Molife.wav in 4.964, bed -19.8 dB; voice_gain 6. Overlays need no re-render unless times change.
  - **Notes:** VLC's seek tooltip "00:31" (~22x11 px) sits on the bottom of our paused Instagram card in the 281-316 s split stretches (not
    covered, too small to mask cleanly). Tool notes (shared tools untouched): apply.py's A2 `at()` match (9 ms) drops a cue placed at the same
    time as another, so overlays.default_sfx's "thud-thin under pop-glass" (UNDER_THUD, same t0) would keep only the thud; this plan spaces
    every cue >= 0.12 s and checks it. An SFX placed while an earlier one still rings truncates that one's tail (the whoosh into the thud on
    every verdict card relies on that).
- 2026-10-13: Affan handed over RAW recordings before bed: camera `X:\Recordings\Onyx\C1354.MP4` + OBS `2026-10-13 09-21-39.mp4` (copied to
  `raw/`). Same pipeline as the batch-2 reactions (REACTIONS-BRIEF.md status 2026-10-12) + his 2026-10-13 rule: this reaction must be
  BETTER than the last ones (critique + fresh research: `_onyx-batch-2026-10/reactions/research-2026-10-13.md`) and different from its
  three siblings. He exports. When all four are done: save ABW8, quit Premiere, shut the PC down (memory feedback-shutdown-after-overnight-job).
- Sync: `../_onyx-batch-2026-10/reactions/s5457/sync-C1354.json`. Transcript: `../_onyx-batch-2026-10/reactions/s5457/obs-09-21-39/transcript/words.json`.
- The sample he reviews: `jeremyminer-google-88k` (both looks in `X:\Claude Projects\Exports\`).
- **2026-10-13 ≈11:30: PHASE 1 DONE (rough cut, reaction agent; no Premiere / plan / graphics yet).** `transcript/cuts.json` = **101 segments,
  323.40 s (5:23.4) of 530.2 s raw**; every joint slice-ASR'd on the FINAL EDL (`work/cutcheck.txt`, GPU under `lock.sh gpu`), dead-air
  gate PASSED (`transcript/dead-air-qa.json`), `outputs/jeremyminer-google-88k-reaction.transcript.json`, `transcript/words.tight.json`,
  `work/seqmap.json`. Chain (reproducible): `keep.json` → `author.py` → `work/fix/prepin.py` → splice RENDER=0 → polish → `work/fix/overlaps.py`
  → splice → `work/fix/edits.py` → `tools/pins.py` (`work/pins.json`) → 1/60 snap → export-transcript → seqmap → `work/fix/sampleseq.py`
  (pre-pin EDL kept: `work/fix/cuts.pre-pins.json`; pins.py is not re-runnable on its own output, restart from that copy).
  - **What plays, sequence time** (`work/seqmap.json` sample_seq, segment-exact): Jeremy's Short 22.33-26.33, 65.85-73.40, 102.93-130.33;
    our sample YouTube look 166.57-172.90 + 188.13-214.42; Instagram look 233.90-247.28 + 264.67-275.38. Everything else = Affan.
  - **Sample plays made to run ONCE** (cross-correlated against the exported finals, lags in `work/fix/prepin.py`): the Short's LAST full
    play (he unmuted it mid-way at raw 39.6, then restarted); YT look = his restart from 0 (raw 294.93), and his VLC seek-back at raw 323.3
    grafted out at sample 9.11 s ('Google. | We've', 322.417 → 325.500, content-identical, 0.6 ms); IG look = his THIRD start (raw 400.92;
    two aborted starts + the black VLC window cut), ended at 'presentation.' (his pause split 'Oh, geez' — heard already in the YT look),
    resumed at 'You guys must have…' (IG audio is muted under his talk after 447.5). **One deliberate REORDER:** the Short's 1 s fragment
    'Where does that way of' (raw 178.38-179.17) now plays AFTER his music comment, so the line runs through once ("Where does that way of
    thinking come from in your life?"), proven in timeline order: `work/cutcheck-reorder.txt`. cuts.json seg 35 is out of raw order on purpose.
  - **Cut:** dead air (> 0.45 s), the 14 s of title-thinking + 4 earlier title tries (kept: "Genius way to counter this common objection"),
    'we will check his instagram' (never checked: a tease), 'it's very unfortunate', the 'I'll share this with Jeremy' line he says over the
    file browser (he says it again in the outro, last take kept), the 'how you attract someone… through short form' echo, 'So that's what I
    mean, right?', false starts/restarts (as far as and also the / and i've actually this is funny because / i'm not gonna obviously you know
    way / they and these are / one post- / i'm going to send both of these video / hopefully you guys), fillers where a dip allows (uh, um,
    'you know' ×6, 'Like it's not', the tag 'right?'s, 'so yeah', the first 'for some reason'). **Kept because coarticulated (no dip, measured):** "is like
    normally", "for like conspiracy", "appealing, right? There's", "whether you, you're", "Instagram is now normally pushes".
  - Words retimed in `transcript/words.json` (WhisperX mis-aligned the replays): 715-743 (YT plays), 983-1005 + 1021 (IG third play), 1081-1082,
    from the sample's own transcript + the xcorr lags; 105/177/412/782/1188 to measured edges; the Short's "Where does that way of thinking
    come from in your life?" tokens corrected (412-415, 441-446; old text in `asr`). Names in `corrections.local.json` (Affan, Miner, Mr.,
    SEO…); 'cap cut' (= CapCut, raw 173.6) flagged, not auto-applied.
  - **Screen to cover (raw):** NOTHING private reaches the cut — both private stretches sit wholly inside removed material: 272.9-288.9 (the
    Claude app "Batch 2: the picks for Affan's approval", then File Explorer + an error dialog) and 378.2-396.9 (Claude app, File Explorer,
    VLC opening black). Minor: VLC's file-name overlay "jeremyminer-google-88k.yt.final.mp4" raw 294.9-~296.9 (seq 166.6-168.5; the
    top-cropped VLC view hides it); a taskbar hover thumbnail of the YouTube tab raw 376.4-377.8 (seq 232.5-233.9, harmless). OBS UI 0-6.7 and
    526.9-530 is cut.
  - Hard starts/stops that are the sample's own (VLC/YouTube pause = instant digital silence; the IG look starts at full level): a 2-3 frame
    audio fade on those clip edges in Premiere avoids a click (seq 233.90, and the music-bed cut-offs at 247.28 / 275.38 / 73.40).
  - Tool notes (worked around in this job, shared tools untouched): author.py's overlap merge corrupts an intentional out-of-order pair;
    seqmap.py's word-based sample_seq clamps the reordered fragment onto his comment; cutcheck.py raises IndexError when the tail cut ends at
    the exact file end (rawcut tail = 530.15); pins.py fails when re-run on its own output.

## Download log (batch approval)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | https://www.youtube.com/@JeremyMiner og:image (yt3 s900) | 59 KB | the channel card's REAL profile picture |
| a2 | `audio/ES_Swing - Molife.wav` | Epidemic Sound recording dd86cb17-c142-4014-b7ac-2b47b2e1fd83 ("Swing - Molife", WAV full mix) | 116 MB | the mellow classy bed (new for this batch, never used before) |
