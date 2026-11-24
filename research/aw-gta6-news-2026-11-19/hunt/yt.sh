# sourced helper: yt <args...>  -> serialized yt-dlp (own lock + machine-wide ps check), 4 s after each. YT_LOW=1 yields to the downloader (.dlwant).
LOCK="X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/hunt/.ytlock"
HUNT="X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/hunt"
yt() {
  if [ -n "$YT_LOW" ]; then while [ -f "$HUNT/.dlwant" ]; do sleep 3; done; fi
  until mkdir "$LOCK" 2>/dev/null; do sleep 2; done
  while ps -W 2>/dev/null | grep -qi yt-dlp; do sleep 3; done
  timeout ${YT_TIMEOUT:-150} yt-dlp --ignore-config "$@"; rc=$?
  sleep 4; rmdir "$LOCK"; return $rc
}
