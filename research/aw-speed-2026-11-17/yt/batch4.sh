#!/usr/bin/env bash
# batch4 (17 Nov 2026): freshness content checks (three post-5-Nov tribute Shorts) + the Club Shay Shay HD section around
# "my top moment of my life" (full episode QaBBgNjc5Pg, 50:40-51:40). One at a time through pace.sh youtube. Same stop rules.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch4.log
out=research/aw-speed-2026-11-17/src
chk() { [ "$1" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
    echo "$(date '+%F %T') speed-beats batch4: bot check or 429 on $2; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $2: flag set, stopping" >> "$log"; exit 9; fi; }
for id in H_XiFqAcjr4 KK3tJr7byqQ FIrTZE9iGOc; do
  [ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
  echo "== $id $(date '+%T')" >> "$log"
  bash $P youtube yt-dlp -f "bv*[height<=1920][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1920]+ba/b" --merge-output-format mp4 \
    --no-playlist --write-info-json -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  rc=$?; chk $rc $id; echo "rc=$rc $(date '+%T')" >> "$log"
done
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
id=QaBBgNjc5Pg
echo "== $id section 50:40-51:40 $(date '+%T')" >> "$log"
bash $P youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]" --merge-output-format mp4 \
  --download-sections "*00:50:40-00:51:40" --no-playlist -o "$out/${id}_5040-5140.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
rc=$?; chk $rc $id; echo "rc=$rc $(date '+%T')" >> "$log"
echo "BATCH4 DONE $(date '+%T')" >> "$log"
