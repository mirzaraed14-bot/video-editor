---
name: reference-youtube-data-api-key
description: "Affan's YouTube Data API v3 keys (made 2026-11-14), one per job: the GTA 6 watcher (X:\\Claude Projects\\GTA 6\\watcher\\youtube-api-key.txt) and Abundance Wisdom research (X:\\Claude Projects\\Abundance Wisdom\\, how-to in YOUTUBE-API.md); what the API can and can't do; the allowance is per Google Cloud project"
metadata:
  node_type: memory
  type: reference
  originSessionId: ffe907a3-18b4-4e7c-a2b3-a104237da5b1
  modified: 2026-11-14T16:33:00.608Z
---

Affan created a free YouTube Data API v3 key on 2026-11-14 for the GTA 6 launch finds watcher.
- **Where:** `X:\Claude Projects\GTA 6\watcher\youtube-api-key.txt` (the key alone in the file). Never print it or
  paste it into chat. It is restricted to the YouTube Data API v3. Send it in the header `X-goog-api-key`, never in the URL.
- **Working code to copy:** `api_call`, `api_step` and `api_test` in `X:\Claude Projects\GTA 6\watcher\watcher.py`
  (tested live 2026-11-14: `python watcher.py --api-test`).
- **Allowance (Google's docs, read 2026-11-14), per PROJECT, not per key:** 100 `search.list` calls a day, 10,000
  units a day for everything else, 1 unit per `videos.list` / `channels.list` call of up to 50 ids. `maxResults` is
  rejected together with `id`. It resets at midnight Pacific.
- **What it can do:** search by words, upload date and view count (`videoDuration=short` returns Shorts too); exact
  views, likes, comment counts, upload time, length, description, tags; channel subscriber counts. No bot checks.
- **What it cannot do:** download video or audio, read transcripts or captions, or say for certain that a video is a
  Short. **It does not fix yt-dlp download blocks.**
- **Don't share this key between jobs.** From 19 Nov the GTA 6 watcher uses about 72 of the 100 daily searches.
- **Abundance Wisdom has its own key and project (made 2026-11-14, tested):**
  `X:\Claude Projects\Abundance Wisdom\API Key Abundance Wisdom YT Searcher.txt`. Affan: "tell it to use this for now
  for researches" (YouTube kept blocking that session). The how-to with a tested example is next to it:
  `X:\Claude Projects\Abundance Wisdom\YOUTUBE-API.md`. AW research uses this key, never the GTA 6 one.
- **Any other job** gets its own Google Cloud project and key the same way: the 10-minute steps are in
  `X:\Claude Projects\GTA 6\watcher\LAUNCH-DAY.md` step 4.

- **AW research uses it through ONE door (2026-11-14 ~21:40):** `research/deep-research-2026-11-14/yt_api.py <slug> <endpoint> ...`
  in the video-editor repo: it reads the key itself (never printed), caps searches (12 per session per Pacific day, hub 20, all 95),
  caches 12 h and logs every call. Affan: research sessions use the API "instead of their normal method" (yt-dlp) for every search
  and number; yt-dlp stays only for downloading a finalist's source file. Peer channels: `playlistItems` on the 'UU' uploads
  playlist (1 unit), never a search.

- **AffanWiz research may use the Abundance Wisdom key, for channel listings only (Affan, 2026-11-15: "Yes, use it").**
  That is the one exception to "don't share this key between jobs". It goes through the same door with the slug
  `affanwiz`: `channels`, `playlistItems`, `videos` and `commentThreads` at 1 unit each, about 500 units a day at most.
  Its search cap is 0 in the script, so the 100 searches a day stay with the Abundance Wisdom sessions.

Related: [[project-gta-documentary-channel]], [[feedback-youtube-sourcing]].
