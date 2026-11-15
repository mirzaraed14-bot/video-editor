# AW deep research run: 14-15 Nov 2026 (six sessions, one hub)

**Why:** Affan used a usage reset on Sat 14 Nov. The weekly meter was ~9 % at 16:45 PKT and resets **Mon 16 Nov 07:00 PKT (02:00 UTC)**.
He wants the usage spent on the deepest research possible: "Find me banger video ideas that we can make shorts on". Every session runs
at max effort (Opus, with the Fable advisor) and is held to `MAX-EFFORT-GATE.md` § **Idea research runs**. Read that section first.

His Harry Potter read (14 Nov): the Snape Short ("Radcliffe Thought Snape HATED Him") went to **#1 of the top-10 chart at first, then
fell to #5-6** (about 23K in the 14 Nov listing). "Our niche selection was good AKA Harry Potter but... our execution wasn't good",
so Harry Potter gets two beat-mining sessions over the whole franchise, any character.

## ▶ STOPPED Sun 15 Nov 17:55 PKT (hub): the meter is past the 82 % stop line (92 % at 17:47)
No new searches, downloads, page loads or subagents in any lane until the Mon 16 Nov 07:00 PKT reset or Affan's own word.
Finals are in; the ranked board is at the top of `HUB-BOARD.md`. Sub-sessions now run on Sonnet xhigh (his rule, 15 Nov).

## The six lanes (one session each; the hub is `local_3ae3a4cf-7107-4cdf-a50e-e1b313072860`)
| slug | lane | owns | hands off |
|---|---|---|---|
| `hp-cast` | Harry Potter, the cast and crew in real life | interviews, talk shows, reunions, pranks, auditions, friendships, fame, money, tributes and deaths (Rickman, Coltrane, Gambon, Maggie Smith), current news. **Also owns the Snape execution diagnosis** (`HP-EXECUTION.md`, due within ~3 h of its start) | a story about a SCENE or a CHARACTER, or how a film moment was made → `hp-films` |
| `hp-films` | Harry Potter, the films, characters and the making of them | the 8 films' characters and arcs, specific scenes, how scenes were made (stunts, improvised lines, deleted scenes), book-vs-film changes, the HBO series peg | an actor's own life story → `hp-cast` |
| `bolt-celeb` | Bolt-format (narrated) Shorts in the celebrity niche: Michael Jackson, Justin Bieber, other mega-celebrities | narrator plus real audio, Bolt Motivation's format | a source-audio-only stitch of an MJ family beat → `ig-mj` |
| `ig-mj` | Instagram beat mining: the MJ family lane (our proven lane) | Michael, Katherine, Prince, Paris, Bigi, the siblings, Jaafar and the biopic | the narrated version of a beat → `bolt-celeb` |
| `ig-icons` | Instagram beat mining: music, film and TV icons other than MJ | Bieber, Whitney, Britney, Eminem, Tupac, Rihanna, Selena, Will Smith, Robin Williams, Heath Ledger… | Harry Potter → the HP sessions |
| `ig-sports` | Instagram beat mining: athletes, internet creators, public figures | Ronaldo, Messi, Kobe, Tyson, Ali, LeBron, bodybuilding (CBum), MrBeast, streamers… | IShowSpeed is being BUILT already: not a lane |

Already made, rejected or in work (never re-pitch; see `AW-SHORTS-NOW.md` for every published title):
- **MJ:** Son, Brother (Jermaine) jealous, Brother saw him again (delivered 14 Nov), Burnt Hair, La Toya, Katherine, Paris, Conrad, Gangster, birthday, dad, kids, death lane
- **Others:** Bieber upbringing, Owen Hart, Diana, Patrick Stewart, Kane, Lunsford, CBum
- **Rejected:** Victory Tour, Beyoncé/Tina, Amy (Bolt), Dolly (clipped), Will Smith (killed 12 Nov), HP idea 3 Hagrid ("two topics")
- **Pending his call:** Whitney/Bobbi (`projects/whitney-bobbi-last-day/`), Whitney "good enough" (`projects/whitney-good-enough/`)
- **Building:** IShowSpeed "His Mom Kicked Him Out"

## Read first (only the parts you need; Grep before full reads)
- **The rules:** `MAX-EFFORT-GATE.md` (all, esp. § Idea research runs), `presets/youtube-shorts/abundance-wisdom/PITCH-CHECKLIST.md`,
  `projects/_onyx-batch3-2026-10/VIRAL-BAR.md`.
- **The channel:** `presets/youtube-shorts/abundance-wisdom/HUB.md` (the top blocks), `LESSONS.md`, `README.md` § 12-13 (CTA, splits, cutaways).
- **His winners and losers:**
  - `research/deep-research-2026-11-14/AW-SHORTS-NOW.md` (all 274 AW Shorts with today's views: do NOT re-list the channel);
  - `X:\Claude Projects\Abundance Wisdom\RESULTS.md`;
  - `research/instagram-beat-mining/RESULTS-TRACKER.md`.
- **The method:**
  - `research/instagram-beat-mining/METHOD.md`;
  - `2026-11-08-run2.md` § Evening (how the Son Short was found: modern HD first-party interviews, unused lines, a news peg, proof);
  - the latest pitches as format models: `projects/mj-family-saw-him-again/PITCH.md`, `projects/speed-kicked-out-three-peat/PITCH.md`.

## Shared ledgers in this folder (append-only, never edit another session's lines)
- `CLAIMS.md`: grep it before any deep dive; append your claim; hand over what you found if another session got there first.
- `IG-SEARCH-LOG.md`: grep it before any Instagram search, and reuse logged results; append every search you run.
- Your own files:
  - the report: `research/deep-research-2026-11-14/<slug>.md`;
  - working files: `research/deep-research-2026-11-14/<slug>/`, with downloads in `<slug>/src/` (X: drive only, never C:);
  - full pitches: a NEW `projects/<kebab-job>/PITCH.md` + `RUN.md`.
- **The hub alone writes** HUB.md, LESSONS.md, RESULTS.md and memory. Put lessons in your report and the hub files them.

## Platforms: one IP, one Instagram login, six sessions
> **▶ pace.sh FIXED Sun 00:19 (two downloads overlapped at 00:14):** a lock is now taken over only when its owner process is
> gone, and an exit removes only its own lock. Before, any lock older than 30 min was taken from a live download, and every
> exit removed the lock, so one take-over cascaded. Tested in a scratch lock dir (4 cases).
>
> **▶ CLEARED Sat 23:13 PKT (one probe answered normally).** yt-dlp is for downloads only, one at a time through pace.sh,
> now 180 s apart, in the hub's slots: Speed's stream → ig-icons (now) → hp-films 23:35 → ig-mj 23:50 → hp-cast 00:10; bolt-celeb and ig-sports download nothing. Searches and numbers stay on the API.
>
> **YOUTUBE BLOCKED since Sat 14 Nov 16:42 PKT** (a "not a bot" page). Contributors: the hub's own channel listing burst at 16:34
> (about 10 requests in 24 s) and a Speed session batch. The hub makes ONE probe around **23:15 PKT**. Until then pace.sh exits 75: don't retry.
> Work Instagram, the web, transcripts already on disk and the local corpora; queue downloads in your file for after the unblock.
> When it clears, NO bursts: one request at a time through pace.sh, never `--sleep-requests` under 15 s inside a listing.
> **No YouTube by ANY route while blocked:** that includes reading YouTube pages in Affan's signed-in Chrome (a cookie/client bypass,
> and it puts the scraping on his Google account). For view counts use WebSearch snippets, third-party stats pages and the numbers on disk.

> **▶ THE YOUTUBE DATA API (Affan, 14 Nov ~21:40): use it INSTEAD of yt-dlp for every search and every number.** His words:
> "once you set the api up tell all the research sessions to use this instead of their normal method". Run only
> `python -I research/deep-research-2026-11-14/yt_api.py <slug> <endpoint> name=value ...` (read its header; tested 21:35).
> It reads his key itself: never open, print or copy the key file. Official, quota-limited, no bot checks, never touches youtube.com.
> - `search` = 100 units: **12 per session per Pacific day** (it resets at 13:00 PKT); all callers stop at 95. Plan them.
> - `videos` (up to 50 ids), `channels`, `commentThreads`, `playlistItems` = 1 unit each. A peer channel's latest uploads:
>   `playlistItems playlistId=UU<channel id after UC>`, then `videos` for the numbers. Never spend a search on a listing.
> - Every call is logged and cached (`yt_api_log.jsonl`, `yt_api_cache/`): grep the log before you search.
> - It cannot download video or audio or read captions. **yt-dlp is now only for downloading a finalist's source file**, through
>   pace.sh, after the hub's probe, in the hub's order.

> **Instagram is NOT blocked (hub, 18:50).** The "No results" pages are phrase refusals (health, death and minors words, and some
> plain phrasings), and grids keep loading between them. The freezes are Chrome freezing background tabs. Don't retry a refused
> phrasing back-to-back: use the hashtag or the account's Reels tab. Don't wait more than ~2 min on a frozen tab: close it and
> move on. Prefer `/p/<code>/` pages and their embedded JSON to screenshots.

- **YouTube:**
  - **Search and numbers: ONLY the API through `yt_api.py`** (above). **Downloads: ONLY `bash projects/_onyx-batch2-2026-10/pace.sh youtube
    yt-dlp ...`**: plain yt-dlp, a global 45 s cool-down, the same lock as `lock.sh`, finalists' source files only.
  - Keep your own downloads 60 s or more apart. No `ytsearch` and no `-J` metadata calls through yt-dlp any more: the API does those.
  - No cookies, proxies or client switching. No caption or timedtext fetches: transcribe locally.
  - **No comment fetches and no channel or playlist listings (hub, 20:56):** `--write-comments` pulls page after page back-to-back,
    and a listing is a burst too (the 16:34 lesson). If comments matter, read them on the page in a browser later, or skip them.
  - **A bot page or 429:** write `.locks/youtube.BLOCKED` (the command is in pace.sh's header), stop YouTube, tell the hub. Only the hub clears it.
- **Instagram:**
  - Use Affan's own Chrome (claude-in-chrome), READ-ONLY: no likes, saves, follows, comments or DMs, and no stories (opening one marks it seen). Never type a password.
  - Run `bash projects/_onyx-batch2-2026-10/pace.sh instagram` right before EVERY page load: one load at a time across all sessions, 30 s apart.
  - Create your own tab, always pass its tabId, never touch a tab you didn't create, and close it when you're done.
  - Mute and pause media with JS on every load.
  - **A 429, "Try again later", a challenge or a login wall:** write `.locks/instagram.BLOCKED`, stop Instagram, tell the hub.
  - Only the main session browses Instagram; subagents don't.
- **GPU:** `bash projects/_onyx-batch2-2026-10/lock.sh gpu <cmd>` for WhisperX. Fall back to CPU or a lighter model when VRAM is busy. Never kill
  another session's process.
- **Silence:** never play audio or video. ffmpeg goes to `-f null`, and page media is muted.
- **Premiere:** don't touch it. This is research only, and nobody saves or exports his projects.

## His standing rules every idea must respect
- **Minors:** real-life children are never on frame. HP film footage of the young cast is OK (his 10 Nov ruling); BTS or press footage of child actors gets flagged for his call; the HBO series' child cast is real children, so they're out.
- **Censor:** drug, self-harm and suicide words get flagged for his call.
- **Format:**
  - claimed Shorts are 60 s or under;
  - no music bed (music is his job);
  - two subtle subscribe prompts, no end screen;
  - labels low, captions just under the lips;
  - titles 5 words max, a blunt hook (his style).
- **Sources:** first-party, HQ audio and video (no far-away mics). A filmed ending beats a photo under audio.
- **The bar:** below-bar ideas are never pitched ("no pick" is an honest result). Every idea carries "the viewer gets: ___".
  **The bar as a number (hub, Sat 19:20, from ig-icons' derivation; his to change):** a locked center of 150K or more, and a
  range whose top reaches 1M+. His approved MJ ideas carried 150K-800K centers; the Amy ruling put a ~60-70K center below the
  bar. State every center against it, with the comparables it rests on. Under it = a LEAD, and the lane says "no pick" first.
  Calibrate on results, not on old predictions: Son 200-500K → 445K, Burnt Hair 300-800K → 83K, La Toya 300-700K → 19K.

## Subagents, advisor, cold read
- **Subagents:** encouraged for parallel gathering (searching, reading, transcribing, frame sheets).
  - Pass `model` explicitly: Sonnet for gathering, Opus for judgment. NEVER Fable agents.
  - Every subagent brief carries these platform rules (pace.sh, silence, read-only, no Instagram).
  - **From 18:50, ONE subagent at a time per session** (hub pacing; it was three).
- **Fable advisor (from 18:50): only at its two required points**, before committing to the finalists and on the final report.
  The Fable meter was 24 % at 18:47; if it fills, nobody gets the advisor.
- **Cold read:** an independent Opus subagent cold-reads the FINAL report (files only). Apply every fix.

## Budget, clock, stop lines
> **▶ PACE DOWN (hub, Sat 18:50 PKT).** The shared meter went 9 % (16:45) → 33 % (18:47), about 12 points an hour. At that rate
> the 75 % line falls ~22:30, before the interims and the YouTube probe, with nothing left for the gate items that need YouTube
> or for building the ideas you find. So:
> - **Gate items only.** Spend only on your open A-K items, and stop widening the pool once a count is met.
> - **Park when blocked.** When everything left needs YouTube: write your state, send the interim, end your turn. Parking costs
>   nothing; the hub wakes you after the probe.
> - **Lean helpers:** one Sonnet subagent at a time (Opus only for the cold read), the advisor only at its two points, no
>   full-size screenshots, no re-reads of big files.
> - **Meter checkpoints:** past 50 % before 23:00 → send the interim at once and park. Finals at ≤ 72 % by Sun 10:00. The stop
>   lines below are unchanged.
> - **A counted YouTube queue in your report:** finalists only, one line per request (metadata or download, the id, why), and a
>   total. After the probe the hub sets the order and the rate, the Speed build's downloads first: about 17 spaced requests
>   tripped this block, so nobody knows yet what YouTube will take.

- **Each session's cap:** about 10 % of the weekly plan. Check `get_usage` at milestones, and write findings to file as you go.
- **The live weekly meter is shared with every other hub:**
  - at 75 %: finish within the hour and deliver;
  - at 82 %: stop and deliver what's there, with "NOT max effort yet" first if anything is open.
- **Interim shortlist:** by **Sat 14 Nov 23:00 PKT (18:00 UTC)**, append your top candidates and their state to your report, and send
  the hub 3-5 lines.
- **Final report:** by **Sun 15 Nov 10:00 PKT (05:00 UTC)**. That leaves Affan time to pick, and the builds time to run before the reset.
- **Delivery:** your final message (to the hub; it reads every note) opens with the statement or "NOT max effort yet". Then the ranked
  idea cards in short form, and the file paths. The hub verifies the reports and gives Affan ONE ranked board across all six sessions.
