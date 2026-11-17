#!/usr/bin/env bash
# batch15 (17 Nov 2026 ~23:50, Darren sequence "more bits"): (1) SpeedShor7s "Darren Watkins Jr." (ER5Jp2s0kCU, 6.5M, 14 s, scouting);
# (2) Club Shay Shay full episode (QaBBgNjc5Pg) video section 6064-6102 s, the trolls answer ("my whole life is just people trolling").
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch15.log
out=research/aw-speed-2026-11-17/src
chk() { [ "$1" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
    echo "$(date '+%F %T') speed-beats batch15: bot check or 429 on $2; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $2: flag set, stopping" >> "$log"; exit 9; fi; }
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
echo "== ER5Jp2s0kCU $(date '+%T')" >> "$log"
bash $P youtube yt-dlp -f "bv*[height<=1920][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1920]+ba/b" --merge-output-format mp4 --no-playlist --write-info-json -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=ER5Jp2s0kCU" >> "$log" 2>&1
rc=$?; chk $rc ER5Jp2s0kCU; echo "rc=$rc $(date '+%T')" >> "$log"
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
echo "== QaBBgNjc5Pg video 6064-6102 $(date '+%T')" >> "$log"
bash $P youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 --download-sections "*6064-6102" --no-playlist -o "$out/QaBB_trolls_6064-6102.%(ext)s" "https://www.youtube.com/watch?v=QaBBgNjc5Pg" >> "$log" 2>&1
rc=$?; chk $rc QaBBgNjc5Pg; echo "rc=$rc $(date '+%T')" >> "$log"
echo "BATCH15 DONE $(date '+%T')" >> "$log"
