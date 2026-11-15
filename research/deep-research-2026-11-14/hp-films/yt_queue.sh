#!/usr/bin/env bash
# hp-films YouTube downloads, v5 (14 Nov 23:15 PKT). Searches and numbers are on the YouTube Data API (done). Hub slot: from 23:35 PKT.
# Two section downloads, ONE at a time, ONLY through pace.sh (global cool-down 180 s). <=1080p, no cookies, no comments, no listings.
# Any non-zero exit stops the queue (75 = BLOCKED). A bot page or 429 in the log means: set .locks/youtube.BLOCKED and tell the hub.
set -u
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
OUT="research/deep-research-2026-11-14/hp-films/src/yt"
mkdir -p "$OUT"
dl () {  # dl <tag> <section> <id>
  local tag="$1" sec="$2" id="$3"
  echo "[$(date '+%T')] start $tag $id $sec" >> "$OUT/queue.log"
  bash projects/_onyx-batch2-2026-10/pace.sh youtube yt-dlp --no-warnings --no-playlist \
    -f "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]" --download-sections "*$sec" \
    -o "$OUT/%(id)s_$tag.%(ext)s" "https://www.youtube.com/watch?v=$id" > "$OUT/dl_$tag.log" 2>&1
  local rc=$?
  echo "[$(date '+%T')] end $tag rc=$rc" >> "$OUT/queue.log"
  if grep -q -i -E "not a bot|sign in to confirm|HTTP Error 429" "$OUT/dl_$tag.log"; then
    echo "$(date '+%F %T') hp-films: bot page / 429 on $id ($tag)" > "projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED"
    echo "[$(date '+%T')] BLOCKED flag set" >> "$OUT/queue.log"; exit 75
  fi
  [ $rc -eq 0 ] || exit $rc
}
dl oldman2023_0800-1800 "00:08:00-00:18:00" 38pRftXvOmA
dl oldman2026_3800-4600 "00:38:00-00:46:00" BWMPDqyMc5Y
echo "[$(date '+%T')] queue done" >> "$OUT/queue.log"
