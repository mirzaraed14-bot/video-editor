#!/usr/bin/env bash
# hp-cast YouTube batch 1 (14 Nov): Snape metadata+comments, 2 discovery searches, 5 benchmark Short downloads.
# Every call goes through pace.sh (global lock, 45 s cool-down); +20 s here so my own calls are >=60 s apart.
set -u
P="/x/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch2-2026-10/pace.sh"
H="/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/hp-cast"
log(){ echo "$(date '+%H:%M:%S') $*"; }
run(){ log "START $1"; shift; bash "$P" youtube "$@"; rc=$?; log "rc=$rc"; if [ $rc -eq 75 ]; then log "BLOCKED flag: stopping"; exit 75; fi; sleep 20; }
run snape_meta yt-dlp --skip-download --write-comments --extractor-args "youtube:max_comments=150;comment_sort=top" -J "https://www.youtube.com/shorts/h7ze3Ckj830" -o "%(id)s" > "$H/meta/snape_h7ze3Ckj830.json" 2> "$H/meta/snape.err"
run search_rickman yt-dlp --flat-playlist -J "ytsearch30:alan rickman daniel radcliffe" > "$H/meta/search_rickman_radcliffe.json" 2> "$H/meta/search1.err"
run search_cast yt-dlp --flat-playlist -J "ytsearch30:harry potter cast interview shorts" > "$H/meta/search_cast_interview_shorts.json" 2> "$H/meta/search2.err"
for id in -1pCzmPHp5A oJ0qurGHmyo BjI7mNh4aII weDpwqowz6U r8x-B43Ayn8; do
  run "dl $id" yt-dlp --no-playlist -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/b[height<=1080][ext=mp4]/b" --merge-output-format mp4 --write-info-json -o "$H/src/bench/%(id)s.%(ext)s" -- "https://www.youtube.com/shorts/$id" > "$H/meta/dl_$id.log" 2>&1
done
log "DONE batch1"
