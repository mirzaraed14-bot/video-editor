# Instagram beat mining: the repeatable method

First run: 2026-11-07, about 08:30-11:00 UTC, in Affan's signed-in Chrome, read-only.

## What actually works

**The best proof surface is a creator's Reels tab, not search.** `https://www.instagram.com/<creator>/reels/` shows real view counts for their grid, without opening a single reel. Sort by views and the outliers jump out: a 2,918-follower page with a 4.7M reel, an 884-follower page at 1.2M.

### The procedure

1. **Start from FRAMEWORKS.md, not from emotion words.** Pick the shape and lane first.
2. **Find seed pages.** One keyword or hashtag search, open 5-6 reels, note who posted them. Fan pages are what you want. Big outlets (@jayshetty, @pagesix) are sources, not proof that a beat travels.
3. **Scan each page's Reels tab** and sort by views. Open only the outliers.
4. **Read the reel:** creator, date, likes, comments, reposts, shares, caption. Weight shares above likes. Take a frame if the caption doesn't reveal the beat.
5. **Score the outlier against views-to-followers.** A small page's huge number means the feed carried it.
6. **Trace the beat to the original upload.** Check Affan's drives first. The transcript store and `E:\Bullshit Folder` already hold most of it.
7. **Check his channel for reuse,** including titles that name a role.
8. **Check YouTube Shorts for that story and angle, and read the view counts. This step changes the answer, so do it before believing a pick.** It flipped both of this run's picks: the Bray letter from "fresh" to "tried 15 times, mostly under 20K", and the wig story from "fresh" to "18.4M already". A big competitor Short is both demand proof and a freshness risk. Report both.
   - Search `https://www.youtube.com/results?search_query=<story>+shorts`, scroll, and read every `a[href*="/shorts/"]`. Walk up from the link to the first parent whose text contains "views".
   - **`ytm-shorts-lockup-view-model` matches nothing on desktop search results, and the under-4-minutes filter returns regular videos. Both gave false "fresh" results here.**
9. **Write ideas with the FRAMEWORKS.md test and lock a prediction.**

### Why search still matters a little

- Keyword page: `https://www.instagram.com/explore/search/keyword/?q=<words>` returns a grid of up to 48 after a scroll. No view counts on the grid.
- Hashtag page: `https://www.instagram.com/explore/tags/<tag>/` works for names the keyword page refuses.
- Search results are weak at finding wounds: name-only gives gossip ("latoya jackson"), and "sad" in a niche gives memes ("bodybuilder sad").

## The "No results" mystery: solved

**It is not throttling.** New queries worked in between failed ones, at the same moment. The keyword page simply serves some phrases and not others.

| Worked | Returned nothing |
|---|---|
| paris jackson sad, michael jackson sad, latoya jackson, joe jackson, katherine jackson paris, wwe sad, bodybuilder sad, arnold schwarzenegger father, michael jackson wig, michael jackson plastic surgery | ilia topuria interview, ilia topuria sad, la toya jackson sad, latoya jackson sad, brooke hogan, michael jackson oxygen chamber |

Fallback when a name returns nothing: the hashtag page (#iliatopuria, #topuria, #brookehogan all worked).

The search box on Explore only matches account names. Pressing Enter does nothing, so it cannot reach reels.

## Safe pace used

- Searches at least 60-75 s apart. Reel and profile pages about 12-13 s apart. No block, captcha or challenge across 22 searches and hashtag pages, about 95 reels and 10 Reels tabs. YouTube: about 13 searches and 15 watch pages at 30-60 s spacing, one session, no block.
- That is one run, not proof it is safe forever. The earlier five failures were probably wording, not a block, but this is not fully proven.
- Stop at any block, "try again later" or login challenge. Never use internal endpoints, cookies, proxies or third-party IG sites.

## What failed, and how to avoid it

| Problem | Rule |
|---|---|
| **A click landed on Explore, keystrokes went to the page, and the Notifications panel opened** on his main account. His badge was probably cleared; Likes checked afterwards, no new like | **Never type on Instagram without checking `document.activeElement` first,** and make the check throw so the batch stops |
| Parser read lone "." as a count | Require a digit: `/^\d[\d.,]*[KMB]?$/`. A "." means the counts are hidden |
| With 2-3 numbers, labels shift | Treat as `likes/comments/...` and do not call the third number reposts |
| Reel page text includes the next 15 reels | Stop at the first number block |
| `zoom` after seeking a video froze Chrome's capture twice | Use `screenshot` at low scale on video pages |
| JS output cut off at about 1,000 chars | Keep each read short |
| Output containing URLs can come back as `[BLOCKED]` | Strip URLs before returning |
| A batch over about 3 minutes timed out and lost its output | Keep batches under 2 minutes |
| YouTube sort-by-views search is mostly music and AI cartoons | Search per story, not per subject |
| YouTube transcript panel is empty on some uploads (Police, MTV, Jonah, MrBeast) | Note as unread, don't guess |

## The transcript store: a large free asset

Chrome's localStorage on www.youtube.com, key `trs`, holds 236 transcripts with title, channel, date, views and duration: `JSON.parse(localStorage.getItem('trs'))[videoId]`. Regex search across it costs **zero YouTube requests**. This is how Katherine's wig line turned up. It covers only 20 of his Shorts, so it cannot prove a line is unused.

The stored `getTrCode` script opens the normal transcript panel on a watch page.

## Measured cost

Weekly plan read **76 % at the start and 76 % at the end,** across about 2.5 hours. The display rounds and may lag, so the true cost is somewhere under about 1 point of the week. That excludes the orchestrator's earlier attempt. Context reached about 59 %. No subagents. If that holds, a daily run is affordable, but re-read it after a day to confirm.

## What a daily version needs

1. A seed-page list per lane that grows each run (start below).
2. The `FRAMEWORKS.md` test as a hard gate on every idea.
3. A log of reels already scanned, so days don't repeat.
4. A full reuse ledger of what each channel Short actually says. Titles are not enough, and the store only holds 20.
5. **The results table filled in honestly for at least 4-6 Shorts before building a skill.** The method is unproven on YouTube until then.
6. Not yet: no skill or routine has been built, as asked.

## Lessons from Affan's sequencing note (7 Nov)

"It's not the editing, it's the sequencing and scripting that makes a Short go viral." So the first script was too thin: it came from one interview. **Before sending any script, list everyone who was there (family, friend, hair, makeup, director, doctor), read a documentary on the story to find them, then choose the sharpest line from each.** That round found Tito, the director and Miko Brando in about an hour. Also check the channel's newest brief for the same angle before calling a line fresh: La Toya on Dr. Drew looked perfect until La Toya Betrayed turned out to be the same reversal.

Mute-and-pause alone doesn't get past YouTube ads. Pre-rolls can block a seek, but `getTrCode` still saves the transcript to `trs`, so read it from there.

## Run 2 lessons, 8 Nov

- **Reuse check by transcript, including our own long-forms.** Run 1 checked titles. Run 2 read the 1K-view long-form's transcript and found the pulse line already used at 8:12; a title check would have passed it.
- **Frames: a muted `play()` for about 1 s, then pause, then screenshot.** Seeking a paused video returned the same stale frame four times.
- **Name the judgment in a third party's voice** (Inside Edition, a 1984 news report). For a topic with no existing belief, say so and lower the prediction. Don't call it F1.
- Helpers `__yv`, `__awx` and `__awp` were removed at the end of the run; `getTrCode` and `trs` stay. The tab was closed.

## Stress test on Scott Clary, 8 Nov: the proof check failed there

Run by the Scott Clary Editor; details in `presets/youtube-shorts/scott-clary/FINDINGS.md` § 2026-11-08 and `projects/_client-scott-clary/research/proof-check/`. As it reports: no separation between hits and flats (0.53 as registered, 0.41 corrected, against a 0.80 pass mark). It would have rejected Bombas (subject 5.6K) and backed Morgan (4.3M elsewhere, 1.4K on Scott's channel). That is business-podcast data, one channel, 3 hits. It says nothing either way about AW, where the method is still untested, but it is a real reason not to treat outside views as proof until the AW tracker has results.

Two more traps from that run:
- In a hidden browser pane the search page stays blank, so `a[href*="/shorts/"]` returns nothing and reads as a false "fresh". `window.ytInitialData` still holds the results (walk `shortsLockupViewModel`, `reelItemRenderer`, `videoRenderer`) with no extra request. Shelf items carry no upload age.
- Matching stories by title terms misfired on 8 of 28 values, so a person must check every match.

## Seed pages so far

| Lane | Page | Followers | Best reel |
|---|---|---|---|
| Jackson | @mskatherinejackson_ | 262K | 10.3M |
| Jackson | @veronica__298 | 17.8K | 7.4M |
| Jackson | @sparkles_29aug58 | 2.9K | 4.7M |
| Jackson | @mjthe_humanitarian | 22.3K | 1M |
| Jackson | @jase.mj.12 | not read | 218K likes |
| Jackson | @justsayjoshua | 208K | Mostly not MJ. Filter |
| Jackson | @celebclassified | 5K | 46K. Their Joe interview may be an original source |
| WWE | @wrestlelegacy | 884 | 1.2M |
| WWE | @itsjonibek | not read | 201K likes |
| WWE | @squaredcircle_24x7 | not read | 120K likes |
| UFC | @wicked.mma | 109K | 178K in a day |
| UFC | @khabibtm_off_mma | 1.2M fan page | 556K, not Topuria |
| Movies, biopic | @bingelog | 59K | 9M, subjects unchecked |
