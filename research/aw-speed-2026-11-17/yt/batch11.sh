#!/usr/bin/env bash
# batch11 (17 Nov 2026 ~20:05, pass 3 rework): ONE audio-only section pull, the first 40 min of his own stream "I GOT A JOB AT KFC!"
# (o1_FvfJD8fg, 27 Sep 2026 15:29 UTC, 11 h after "Hi Me In 3 Years" went up), to find his reaction to the 18-year-old's message
# first-party (the Speedy Boykins re-upload nQs6jA11sQo is on the do-not-use list). Runs after batch10.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch11.log
out=research/aw-speed-2026-11-17/src
while ! grep -q "BATCH10 DONE\|BLOCKED\|BOT/429" research/aw-speed-2026-11-17/yt/batch10.log 2>/dev/null; do sleep 20; done
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
echo "== o1_FvfJD8fg audio 0-2400 $(date '+%T')" >> "$log"
bash $P youtube yt-dlp -f "ba[ext=m4a]/ba" --download-sections "*0-2400" --no-playlist -o "$out/kfc_0-2400.%(ext)s" "https://www.youtube.com/watch?v=o1_FvfJD8fg" >> "$log" 2>&1
rc=$?; echo "rc=$rc $(date '+%T')" >> "$log"
if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then echo "$(date '+%F %T') speed-beats batch11: bot check or 429; YouTube stopped; the hub clears this flag." > "$FLAG"; fi
echo "BATCH11 DONE $(date '+%T')" >> "$log"
