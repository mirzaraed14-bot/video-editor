#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src/aw_own
log=research/aw-speed-pick-2026-11-13/yt/batch11.log
P="C:/Users/affan/.cache/video-editor/whisperx-venv/Scripts/python.exe"
S="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/cpu_scout.py"
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
for id in I883j8Wu1kw MFBIqsJSocM; do
  echo "== audio $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --write-info-json -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/shorts/$id" >> $log 2>&1; chk; sleep 45
done
echo "== search: ishowspeed keystone therapist walked back $(date '+%T')" >> $log
bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch10:ishowspeed therapist stream clarifies explains mental health after" >> $log 2>&1; chk
for id in I883j8Wu1kw MFBIqsJSocM; do [ -f $d/$id.m4a ] && "$P" -I "$S" scout $d/$id.m4a >> $log 2>&1; done
echo DONE >> $log
