#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch8.log
P="C:/Users/affan/.cache/video-editor/whisperx-venv/Scripts/python.exe"
S="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/cpu_scout.py"
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
q(){ echo "== search: $1 $(date '+%T')" >> $log; bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch10:$1" >> $log 2>&1; chk; sleep 45; }
echo "== streamer awards latest $(date '+%T')" >> $log
bash $L youtube yt-dlp --flat-playlist --playlist-end 12 --print "%(id)s | %(view_count)s | %(duration)s | %(title)s" "https://www.youtube.com/@TheStreamerAwards/videos" >> $log 2>&1; chk; sleep 45
sotyid=$(grep -iE "speed.*streamer of the year 2026|streamer of the year 2026.*speed" $log | head -1 | cut -d' ' -f1)
if [ -n "$sotyid" ]; then echo "== download official SOTY 2026 $sotyid $(date '+%T')" >> $log; bash $L youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 --no-playlist --write-info-json -o "$d/hd/%(id)s_soty26.%(ext)s" "https://www.youtube.com/watch?v=$sotyid" >> $log 2>&1; chk; sleep 45; fi
for id in KCOIJjpLk1M CmnDmFYeRow cetcKaq5y4s; do echo "== meta $id $(date '+%T')" >> $log; bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(duration)s | %(title)s" --print "%(chapters)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45; done
q "ishowspeed visits house where he started streaming detroit"
q "ishowspeed detroit dad house irl stream"
q "kai cenat says ishowspeed is the best streamer"
q "ishowspeed greatest streamer of all time said interview"
q "iced coffee hour mizkif tier list streamers full episode"
for id in KCOIJjpLk1M CmnDmFYeRow; do echo "== audio $id $(date '+%T')" >> $log; bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --write-info-json -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45; done
echo "YT DONE $(date '+%T')" >> $log
cd research/aw-speed-pick-2026-11-13
for id in KCOIJjpLk1M CmnDmFYeRow; do [ -f src/$id.m4a ] && "$P" -I "$S" scout src/$id.m4a >> yt/batch8.log 2>&1; grep -n -i -E "my mom|my mother|mama|kicked|my dad|father|detroit|support|believe|proud|alone|lonely|cry|cried|quit|started streaming|first stream|streamer of the year|greatest|goat" scout/$id.scout.txt > scout/${id}_hits.txt 2>/dev/null; done
echo DONE >> yt/batch8.log
