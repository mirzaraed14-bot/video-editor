---
name: reference-instagram-reading-method
description: "How to read Instagram numbers in his Chrome without being blocked: DOM sections, not the private API; views from the reels tab; pace.sh instagram before every load"
metadata:
  node_type: memory
  type: reference
  originSessionId: 858cff19-5854-4cac-8410-49fdee79f795
  modified: 2026-11-24T01:52:04.526Z
---

Tested 24 Nov 2026 (GTA 42 secret-cars research, 67 posts read, no block):
- **Don't** call Instagram's internal JSON API (`/api/v1/fbsearch/...`) from the page with fetch. The auto-mode classifier denied it as unauthorized access.
- **Search grid:** navigate to `instagram.com/explore/search/keyword/?q=<query>` (or `/explore/tags/<tag>/`) and read the links with `querySelectorAll('a[href*="/reel/"], a[href*="/p/"]')`.
- **Post page** `/p/<code>/`:
  - the first `<section>`'s innerText = user + caption + top comments;
  - the second = **likes / comments / reposts / shares**, e.g. "2.1K / 39 / 100 / 2.9K";
  - the first `<time>` datetime = the post date in UTC.
  - Views are NOT on the post page. They show on the author's `/<user>/reels/` tiles.
- To look at a reel: `v=document.querySelector('video'); v.muted=true; v.pause(); v.currentTime=N`, then zoom on the video box. Half-scale browser views are "SEEN (browser)", never a 1080p frame.
- **Pacing is shared across every session:** run `projects/_onyx-batch2-2026-10/pace.sh instagram` right before EACH page load (it enforces 30 s between loads). On a 429, "Try again later" or a login wall, write `.locks/instagram.BLOCKED` and stop.
- A full 30-search crawl doesn't fit in one ~80 min agent run at that pace: ~15 searches + ~65 posts did. Prioritise the phrasings per beat.

Related: [[feedback-checklist-shape-is-a-gate]], [[feedback-max-effort-every-asset]], [[reference-youtube-data-api-key]].
