#!/usr/bin/env bash
# batch12 (17 Nov 2026 ~21:30, pass 3 rework): ONE video section pull of his own stream "I GOT A JOB AT KFC!" (o1_FvfJD8fg),
# 29:30-35:30, where its comments place the "Hi Me In 3 Years" watch ("31:00 hi me in 40 years"). Starts after 21:38 PKT so the GTA
# farewell session's three pulls go first (hub, 21:18).
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch12.log
out=research/aw-speed-2026-11-17/src
# (time wait removed 21:29: the hub says the GTA pulls are done)
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
echo "== o1_FvfJD8fg video 1770-2130 $(date '+%T')" >> "$log"
bash $P youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 --download-sections "*1770-2130" --no-playlist -o "$out/kfc_1770-2130.%(ext)s" "https://www.youtube.com/watch?v=o1_FvfJD8fg" >> "$log" 2>&1
rc=$?; echo "rc=$rc $(date '+%T')" >> "$log"
if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then echo "$(date '+%F %T') speed-beats batch12: bot check or 429; YouTube stopped; the hub clears this flag." > "$FLAG"; fi
echo "BATCH12 DONE $(date '+%T')" >> "$log"
