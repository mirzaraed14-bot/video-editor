#!/usr/bin/env bash
# batch3 (17 Nov 2026): his own first-party Shorts "thank you ronaldo" (5 Nov 2026) and "i'm sorry ronaldo" (6 Jul 2026).
# One download at a time through pace.sh youtube (180 s cool-down). No cookies/proxies/extractor-args/captions/comments/playlists.
# Stops on a bot check or 429 (sets the flag, tells nobody else to retry). Silent: nothing plays.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch3.log
out=research/aw-speed-2026-11-17/src
for id in MSizEHlSsTs hMCusTW14xI; do
  if [ -f "$FLAG" ]; then echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; fi
  echo "== $id $(date '+%T')" >> "$log"
  bash $P youtube yt-dlp -f "bv*[height<=1920][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1920]+ba/b" --merge-output-format mp4 \
    --no-playlist --write-info-json -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  rc=$?
  [ "$rc" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
    echo "$(date '+%F %T') speed-beats batch3: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $id: flag set, stopping" >> "$log"; exit 9
  fi
  echo "rc=$rc $(date '+%T')" >> "$log"
done
echo "BATCH3 DONE $(date '+%T')" >> "$log"
