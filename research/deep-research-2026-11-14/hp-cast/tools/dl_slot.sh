#!/usr/bin/env bash
# hp-cast download slot (hub order 14 Nov 23:14): wait for 00:10 PKT, then 3 downloads ONE at a time through pace.sh
# (pace.sh holds the shared YouTube lock and sleeps the 180 s cool-down). Stops on a flag, a bot page or a 429.
set -u
ROOT="/x/Claude Projects/video-editor-client/video-editor"
PACE="$ROOT/projects/_onyx-batch2-2026-10/pace.sh"
FLAG="$ROOT/projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED"
SRC="$ROOT/research/deep-research-2026-11-14/hp-cast/src"
LOG="$SRC/dl_slot.log"
stamp() { TZ=PKT-5 date '+%H:%M:%S'; }
target=$(date -u -d '2026-11-14 19:10:00' +%s); now=$(date +%s)
if [ "$now" -lt "$target" ]; then echo "[$(stamp)] waiting $((target-now)) s for the 00:10 PKT slot" >> "$LOG"; sleep $((target-now)); fi
FMT='bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]'
COMMON=(--no-playlist --no-write-comments --no-write-subs --no-write-auto-subs --write-info-json -f "$FMT"
        --merge-output-format mp4 --retries 3 --fragment-retries 3 --socket-timeout 30 --no-progress)
run() {  # run <name> <url> <output template> [extra yt-dlp args...]
  local name="$1" url="$2" tmpl="$3"; shift 3
  local dir="$SRC/$name" rlog="$SRC/dl_$name.log"
  mkdir -p "$dir"
  echo "[$(stamp)] start $url -> $name" >> "$LOG"
  bash "$PACE" youtube yt-dlp "${COMMON[@]}" -P "$dir" -o "$tmpl" "$@" "$url" > "$rlog" 2>&1
  local rc=$?
  echo "[$(stamp)] rc=$rc $name" >> "$LOG"
  if [ "$rc" -eq 75 ]; then echo "[$(stamp)] STOP: youtube.BLOCKED (pace.sh refused)" >> "$LOG"; exit 75; fi
  if grep -qiE "HTTP Error 429|Too Many Requests|confirm you.?re not a bot|Sign in to confirm" "$rlog"; then
    echo "$(date '+%F %T') hp-cast yt-dlp saw a bot page or 429 on $url" > "$FLAG"
    echo "[$(stamp)] STOP: bot page or 429, flag set" >> "$LOG"; exit 76
  fi
  [ "$rc" -ne 0 ] && echo "[$(stamp)] FAILED $name (see dl_$name.log); going on" >> "$LOG"
  return 0
}
run yt_felton_hsc 'https://www.youtube.com/watch?v=pSWIM3Tc9y0' '%(id)s_%(section_start)s-%(section_end)s.%(ext)s' \
    --download-sections '*0:00:00-0:13:00' --download-sections '*0:25:30-0:33:00'
run yt_felton_debut 'https://www.youtube.com/watch?v=Ug1vk4ve2h8' '%(id)s.%(ext)s'
run yt_oldman_rickman 'https://www.youtube.com/watch?v=tVm7ajSlOIU' '%(id)s.%(ext)s'
echo "[$(stamp)] all done" >> "$LOG"
for d in "$SRC"/yt_*; do ls -la "$d" >> "$LOG"; done
