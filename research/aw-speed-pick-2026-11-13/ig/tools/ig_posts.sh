#!/usr/bin/env bash
# Anonymous (no cookies) yt-dlp image fetch of @ishowspeed's own 2021-22 posts, one pace.sh slot per post.
SP="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad"
REPO="/x/Claude Projects/video-editor-client/video-editor"
FLAG="$REPO/projects/_onyx-batch2-2026-10/.locks/instagram.BLOCKED"
log="$SP/igdl/run.log"
for code in "$@"; do
  [ -d "$SP/igdl/$code" ] && [ -n "$(ls -A "$SP/igdl/$code" 2>/dev/null)" ] && { echo "skip $code (done)" >> "$log"; continue; }
  bash "$REPO/projects/_onyx-batch2-2026-10/pace.sh" instagram || { echo "pace.sh refused ($?) at $code: stop" >> "$log"; exit 75; }
  mkdir -p "$SP/igdl/$code"
  echo "== $code $(date '+%T')" >> "$log"
  ( cd "$SP/igdl/$code" && timeout 180 yt-dlp --skip-download --no-simulate --ignore-no-formats-error --write-thumbnail --yes-playlist \
      --print "%(playlist_index)s|%(id)s|%(duration)s|%(width)sx%(height)s|%(vcodec)s|%(timestamp)s" \
      -o "thumbnail:$SP/igdl/$code/%(playlist_index)02d_%(id)s.%(ext)s" "https://www.instagram.com/p/$code/" ) >> "$log" 2>&1
  if tail -25 "$log" | grep -qiE "HTTP Error 429|rate.?limit|Please wait a few minutes|login required|checkpoint|challenge"; then
    echo "$(date '+%F %T') aw-speed-research: anonymous yt-dlp on Instagram hit a rate limit/login wall at $code; stopped" > "$FLAG"
    echo "RATE LIMIT at $code: flag set, stopping" >> "$log"; exit 9
  fi
done
echo "ALL DONE $(date '+%T')" >> "$log"
