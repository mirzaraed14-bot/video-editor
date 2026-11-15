#!/usr/bin/env bash
# batch20 = wave 2's single download (15 Nov 00:25): the 25 Feb 2021 Q&A upload DNiOLSkH94Q (age 16; the camera is the whole
# picture), the only wave-2 candidate that passed the size screen. Fetched WHOLE (7m34s) natively: a shorter lock hold than an
# ffmpeg section. One request through pace.sh youtube. Stops on a bot check / 429 (sets the flag). No cookies. Silent.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-pick-2026-11-13/yt/batch20.log
out=projects/speed-kicked-out-three-peat/assets/clips/old-streams
mkdir -p "$out"
if [ -f "$FLAG" ]; then echo "YouTube BLOCKED, not running ($(date '+%T'))" | tee -a "$log"; exit 75; fi
id=DNiOLSkH94Q
echo "== whole $id $(date '+%T')" >> "$log"
bash $P youtube yt-dlp --no-progress -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]" \
  --merge-output-format mp4 --no-playlist -o "$out/20210225_${id}_QA-upload.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
rc=$?
[ "$rc" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
  echo "$(date '+%F %T') aw-speed-research batch20: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"
  echo "BOT/429 on $id: flag set, stopping" >> "$log"; exit 9
fi
echo "DONE rc=$rc $(date '+%T')" >> "$log"
