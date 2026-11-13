#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch6.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
sleep 30
sec(){ id=$1; a=$2; b=$3; tag=$4
  echo "== video $id $a-$b $(date '+%T')" >> $log
  bash $L youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 --no-playlist --download-sections "*$a-$b" -o "$d/hd/${id}_${tag}.%(ext)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45; }
sec 52pXQVGHwEE 0:00 2:20 fam
sec QaBBgNjc5Pg 1:43:20 1:44:30 support
sec auSbPov16vA 3:38 5:12 win24
sec fox09o3r2SU 3:08 4:40 win25
sec 52pXQVGHwEE 5:50 6:20 covid
sec CmpgXX7ZWJU 3:40 4:20 miz
echo DONE >> $log
