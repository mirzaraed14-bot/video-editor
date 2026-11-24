# gta5-farewell: BRIEF

## ▶ STATUS: resume here (rewrite at every milestone)
- **18 Nov 16:25 (machine clock) · YouTube open, but `youtube.lock` is HELD** (a directory with an `owner` file, since 16:23):
  - It belongs to a multi-hour live-stream capture for Affan's GTA video.
  - YouTube itself was blocked 06:10-16:21 by a GTA research session, then cleared.
  - **Do NOT start a pace.sh youtube waiter.** After 4 h (~20:23) pace.sh takes the lock over even with its owner alive, and two
    streams would overlap.
  - Before any download, check `ls projects/_onyx-batch2-2026-10/.locks/youtube.lock`; download only once it's gone.
  - Passed to gta5-farewell-build. Its only YouTube want, a TGG face-cam video, waits for Affan's v3 notes anyway.
- **18 Nov ~03:45 · YOUTUBE OPEN AGAIN** (the hub's 03:40 probe answered normally; flag renamed `youtube.BLOCKED.cleared-2026-11-18`).
  Rules from now on, and in every brief:
  - downloads only, ONE video per `pace.sh youtube` slot (180 s apart);
  - never `--write-auto-subs`, captions or timedtext (they drew the 01:36 429);
  - words come from local ASR under `.asr-lock`;
  - a bot page or a 429 means stop, set the flag, tell the hub.
  No yt-dlp was running when the flag cleared.
- **18 Nov ~01:55 · Affan's own edit + ASK 2.**
  - He re-cut "13 Years Goodbye GTA 5 - raw cut" himself to ~30 s: Jelly "brought me up" → Shawn "saved me" → Slink "grew up"
    → Slink's thank-you → TGG. Beats 2/3/8 and most spares are dropped. **His edit is the base; never touch it.**
  - He asked the build session for more bits from other YouTubers. They are in a NEW sequence, "GTA 5 Farewell - more creator bits"
    (same bin, 15 bits: Jelly ×5, Caylus ×2, TGG ×4, DarkViperAU ×2, Ned ×2; `build/premiere_more/BITS.md`).
  - Placed 02:04: READBACK PASS, his playhead ticks identical (3077827200000), his sequence re-activated, Sequence 02 untouched.
  - Still pending: the TDAWG Short and Kreek video (downloaded, not transcribed; the ASR memory guard decides).
  - Next is unchanged: his Tella on his edit → § TELLA → the finish build.
- **18 Nov 01:36 · YOUTUBE BLOCKED** (`youtube.BLOCKED`, set by the hub): the build session's "more bits" pass ran one pace.sh slot
  of 5 `--write-auto-subs` caption requests, and the 5th got HTTP 429. **No yt-dlp at all until the hub clears the flag**
  (its probe is at ~03:40). Standing rule for every brief from now on: **no captions, no timedtext, no batched requests**
  (one video per pace.sh slot). Work from files on disk; the Premiere work needs no YouTube.
- **18 Nov 00:38 (machine clock) · STOP 1 REACHED: the raw sequence is in his ABW11, waiting for his Tella.**
  - Sequence "13 Years Goodbye GTA 5 - raw cut" (id 8a9eba7c…), bin "GTA 5 Farewell".
  - Picture: the v3 cut is 50.97 s. V1 holds the person or picture of each beat; V2 holds the game-footage top panels.
  - Audio: A1 voice spans, level-matched for review.
  - 17 markers. Seven spares after a 2 s gap, running to 103.0 s.
  - Checks: `build/premiere/READBACK.md` = PASS; his playhead ticks are identical (Sequence 13, 12992918400000).
  - Not saved or exported: ABW11 needs his Ctrl+S.
  - Comp vs code-final sheet: `build/premiere/proof/sheet_1.jpg`.
  - Next: his Tella → resolve it into this BRIEF (§ TELLA) → the finish build from HIS edit of the sequence.
- (earlier, 17 Nov ~23:55) Phase: STOP 1 = the RAW Premiere sequence (build session told, `build/premiere/`). Affan:
  "my workflow is this: text sequence -> premiere sequence -> tella video -> start the build". I skipped the Premiere step and
  the build session made a code-built final (`build/out/gta5-farewell.final.mp4`, 23:24). That file is NOT delivered and NOT
  handed to the hub. Stopped at ~23:50.
  - Now: "13 Years Goodbye GTA 5 - raw cut" in his open ABW11, bin "GTA 5 Farewell".
    - V1/A1: v3 beats 1-10. V2: game-footage covers. Markers per beat. Spares after the end. Raw only.
    - Recipe: the Dad job's `premiere/` scripts. premiere.lock + quiet gate; never save or export.
  - Then: wait for his Tella. Only after the Tella does the finish build start. The code final's work (1080p UiLcsgFnS4k
    for beats 1/2/9, the measured edges, the beat-3 re-cut) carries into the raw sequence.
- (earlier, 20:55) Phase: **BUILD running** in session `gta5-farewell-build` (local_d5a0f783-8e15-46e6-91a0-a21513499c58, Sonnet
  xhigh, writes only `build/`, state in `build/RUN.md`). Affan OK'd v2 at ~20:40 ("All in all I really like this sequence") with one
  note, end on the actors ("it's been quite a ride"), applied as **v3** (`SEQUENCE.md`; v2 in `research/SEQUENCE.v2.md`): after TGG,
  Slink "That was quite a ride, dawg" (2021 original 1047.18, fist bump, on the 39.0 drop) → Slink "On behalf of Lamar, Franklin,
  Trevor, Michael… thank you" (ref 717.54) → GTA VI. ~50 s. Next for me: check the build's render, then hand to the hub (it verifies and
  copies to the exports). Target final 18 Nov ~14:00 PKT.
- (earlier, 20:20) v2 sent to Affan; the summary below is v2's opening.
- The sequence: Arc A "what GTA 5 gave them → goodbye": Shawn "it kind of saved me" (hook, card "13 YEARS LATER, IT'S TIME TO SAY
  GOODBYE") → Shawn launch day → 2013 queue → Slink "grew up" (2021 original, 1080p, 17:41) → Jelly "brought me up" → TGG "GTA V
  changed my life" on the held "again" → black → GTA VI on the drop (39.0). Title `13 Years… Goodbye GTA 5 💔`. Decisions in § 1.
- Proven: speakers by face + pitch (Shawn ~100 Hz, Slink ~130-140 Hz); every quote verbatim except 3 marked trims.
- Open (named NOT done in § 0): 2013 queue + Rockstar 2011/GTA VI trailers + Shawn's 2023 1080p episodes still downloading
  (`sources/launch2013`, `sources/rockstar`, `sources/gamology_2023`); IG per person; Shawn's Topaz test; the muted word.
- On his OK: read SESSION-START.md + house style (`presets/youtube-shorts/abundance-wisdom/`), effects-catalog pass, verify the open
  sources, build; message the hub before final. If he picks E3, Ned Luke's finale VOD (18 Nov 04:00 PKT) is downloaded and read first.
- Weekly meter at send: 29 % (Fable 0 %). API: 18/20 gta-farewell searches used today (Pacific day 17 Nov).
- **Instagram (hub, 17 Nov ~20:25):** a soft throttle on Affan's account (the Speed session hit "No results" 3 times). No keyword
  search pages: only `/<name>/reels/` tabs and hashtag pages, through `pace.sh instagram`. One more "No results", a freeze or a
  challenge = stop Instagram for the day and tell the hub. Lean on YouTube for proof.

## The ask (Affan, 17 Nov ~18:30 PKT, voice, to the AW hub)
An emotional GTA 5 farewell Short timed to GTA 6 (two days out). Compile from his reference
(https://www.youtube.com/watch?v=zTPzck2mrug) PLUS other beats of creators getting emotional; NOT built from that one video only.
Strong emotional hook, strong ending. He lays the music himself (most likely "See You Again", the Paul Walker tribute): we ship
NO music bed and design the cut to breathe under it. Channel assumed AW ("a completely different niche"); he can redirect to Afterhours.

## Deadline facts
- GTA 6: **19 Nov 2026** (Take-Two stands by it). New Zealand unlock 18 Nov ~16:00 PKT (REPORTED in `X:\Claude Projects\GTA 6\`);
  US ET unlock 19 Nov 05:00 UTC = 10:00 PKT (REPORTED).
- Ned Luke's "The Final Mission: Finale" (Michael's actor finishing GTA 5; "ONE LAST RIDE") streams **17 Nov 6 PM EST = 18 Nov 04:00 PKT**
  (his own upload TCt_m9PfoMs, 16 Nov; scheduled item j346nGFSXYA).

## The reference (Gamology, "Goodbye GTA V... Thank You for Everything ❤️", 14 Nov, 12:08, 149K views / 3.8K likes on 17 Nov)
A compilation of Gamology's "GTA voice actors react" episodes: Ned Luke (Michael) on his stream cam, Franklin's/Lamar's actors in
the Gamology studio, intercut with the GTA V scenes they voiced; viewer questions on yellow cards; ends on the actors' thank-yous.

## Files
- `research/` API tables, IG log, reference analysis · `sources/` downloads (untrusted media, own folders) · `tools/` scripts
- `SEQUENCE.md` the sequence for his OK (not written yet)
