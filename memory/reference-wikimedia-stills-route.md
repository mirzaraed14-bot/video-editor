---
name: reference-wikimedia-stills-route
description: "How to pull licensed Wikimedia stills from this machine (commons.wikimedia.org doesn't resolve, upload.wikimedia.org 429s fast)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 03b68cbb-760f-44ad-9217-a4d590d1bf98
  modified: 2026-11-18T22:57:13.048Z
---

On this PC (2026-11-19) `commons.wikimedia.org` does not resolve and `upload.wikimedia.org` answers 429 (Retry-After 120 s; every retry before that resets the timer) after a handful of file pulls.

**Working route:** list files and licences through `en.wikipedia.org/w/api.php` (`prop=images` on an article, then `prop=imageinfo&iiprop=url|size|extmetadata`), then download each file with `https://en.wikipedia.org/wiki/Special:Redirect/file/<File_name.jpg>?width=1920` (it redirects to thumb.wikimedia.org, not throttled). Generic `-A` client name, about 6 s between files, never a loop that retries inside 120 s.

**Why:** a Sonnet stills agent sat 27 min on Commons and produced nothing; the Jobs / Apple HQ stills for the Partovi Short came this way in under 5 min. Record author + licence per file (CC BY / BY-SA need attribution in the video description).

**How to apply:** any Scott / AW job that needs a licensed photo; see [[feedback-sourced-stills-must-be-hq]] for the quality bar.
