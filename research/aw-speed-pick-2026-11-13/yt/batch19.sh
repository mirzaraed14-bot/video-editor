#!/usr/bin/env bash
# batch19 = the build's Tella-2 ask (3): OLD stream footage of teen Speed streaming happily, talking to online friends.
# Written 14 Nov 2026 ~20:25, revised ~21:55 (advisor + hub: the YouTube Data API replaces every yt-dlp search/metadata call).
# RUNNER: aw-speed-research runs this ITSELF, after the hub's probe clears .locks/youtube.BLOCKED, in the hub's download order
# (the Speed build's mom-moment downloads first). The hub only clears the flag; no other session runs it.
# The target was found WITHOUT any yt-dlp call (API: his uploads playlist UUWsDFcIhY2DBi3GB5uykGXA + videos, 21:50):
#   n2wj5MV78UM, 21 Apr 2020, "COMP STAGE W/FACECAM // #300 SUB GRIND // JOIN UP // NBA 2k20", 3h07m, HD, 84K views. He was 15,
#   before the kick-out. Other face-cam streams: F14x9rBe-OM, hx_-Q-59ULU, GQsQ0JYlVqU, Rjo1iqWKXKw, 9wuLryY6-EU, u6uPqicdU0E,
#   SUK7NYl0TF4, maYyYGIveUw, 7TKPzJKLYz0 (21 Apr-19 May 2020).
# Wave 1 = ONE 18-minute section (05:00-23:00). The face-cam inset is then checked by eye at native size BEFORE any second download.
# One download only, through pace.sh youtube (45 s cool-down). Stops on a bot check / 429 (sets the flag). No cookies. Silent.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-pick-2026-11-13/yt/batch19.log
out=projects/speed-kicked-out-three-peat/assets/clips/old-streams
mkdir -p "$out"
if [ -f "$FLAG" ]; then echo "YouTube still BLOCKED, not running ($(date '+%T'))" | tee -a "$log"; exit 75; fi
id=n2wj5MV78UM
echo "== section 05:00-23:00 of $id $(date '+%T')" >> "$log"
bash $P youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]" --merge-output-format mp4 \
  --download-sections "*00:05:00-00:23:00" --no-playlist \
  -o "$out/20200421_${id}_sec05-23.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
rc=$?
[ "$rc" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
  echo "$(date '+%F %T') aw-speed-research batch19: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"
  echo "BOT/429 on $id: flag set, stopping" >> "$log"; exit 9
fi
echo "WAVE 1 DONE rc=$rc $(date '+%T'): check the face-cam inset by eye before any second download" >> "$log"
