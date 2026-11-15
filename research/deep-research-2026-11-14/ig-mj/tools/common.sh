# shared by dl_a.sh / dl_b.sh (ig-mj, 14 Nov 2026). Hub 23:14: slot from 23:50, ONE download at a time through pace.sh
# (global 180 s cool-down), <=1080p H.264, no cookies, no comments, no listings, --sleep-requests 15. Bot page / 429 -> flag + stop.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
L=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
LOCKDIR=projects/_onyx-batch2-2026-10/.locks/youtube.lock
R=research/deep-research-2026-11-14/ig-mj
log=$R/dl/dl.log
FW=$R/tools/fw2.py
mkdir -p "$R/dl"
dl() {  # $1 = id, $2 = its own new empty folder
  local id=$1 out=$2
  [ -f "$FLAG" ] && { echo "$(date '+%F %T') BLOCKED flag present, not requesting $id" >> "$log"; exit 75; }
  mkdir -p "$out"
  echo "== $id $(date '+%F %T')" >> "$log"
  bash $L youtube yt-dlp --no-playlist --no-cookies --no-cookies-from-browser --no-write-comments --sleep-requests 15 \
    -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/b[height<=1080][ext=mp4]/bv*[height<=1080]+ba/b[height<=1080]" \
    --merge-output-format mp4 --write-info-json --no-progress \
    -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  local rc=$?
  echo "rc=$rc $(date '+%T')" >> "$log"
  [ $rc -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -40 "$log" | grep -qiE "HTTP Error 429|Too Many Requests|not a bot|Sign in to confirm"; then
    echo "$(date '+%F %T') ig-mj: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $id: flag set, stopping" >> "$log"; exit 9
  fi
}
post() {  # $1 = mp4: probe, loudness, 8x8 frame sheet, CPU transcript with word times (silent: files only)
  local f=$1 b=${1%.*}
  [ -f "$f" ] || { echo "post: missing $f" >> "$log"; return; }
  echo "== post $f $(date '+%T')" >> "$log"
  ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,sample_rate,channels:format=duration,bit_rate -of default=nw=1 "$f" > "$b.probe.txt" 2>&1
  ffmpeg -nostdin -hide_banner -i "$f" -vn -af ebur128=framelog=quiet -f null - 2>&1 | grep -E "I:|LRA:|Peak:" >> "$b.probe.txt"
  local dur iv; dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  iv=$(python -I -c "import math;print(max(1,math.ceil(float('$dur')/64)))")
  ffmpeg -nostdin -loglevel error -y -i "$f" -vf "fps=1/$iv,scale=320:-1,tile=8x8" -frames:v 1 "$b.sheet_every${iv}s.jpg"
  ffmpeg -nostdin -loglevel error -y -i "$f" -vn -ac 1 -ar 16000 "$b.16k.wav" && \
    uv run --no-project --with faster-whisper python -I "$FW" "$b.16k.wav" "$b.fw.txt" medium.en >> "$log" 2>&1
  rm -f "$b.16k.wav"
  echo "post done $f $(date '+%T')" >> "$log"
}
