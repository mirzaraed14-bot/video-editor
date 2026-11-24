#!/bin/bash
# clip downloader: reads dlq.tsv (url<TAB>name), serialized via yt.sh lock. Stops when file STOP exists and queue is empty.
cd "$(dirname "$0")"; . ./yt.sh; touch dlq.tsv dl-done.txt
while true; do
  line=$(grep -vxFf dl-done.txt dlq.tsv | head -1)
  if [ -z "$line" ]; then rm -f .dlwant; [ -f STOP ] && exit 0; sleep 8; continue; fi
  touch .dlwant
  url=$(echo "$line" | cut -f1); name=$(echo "$line" | cut -f2); extra=$(echo "$line" | cut -f3)
  if [ ! -s "clips/$name.mp4" ]; then
    YT_TIMEOUT=240 yt -q -f "720p60/720/best[height<=720]/best" $extra -o "clips/$name.%(ext)s" "$url" >> dl.log 2>&1
  fi
  echo "$line" >> dl-done.txt; echo "$(date +%T) done $name $(ls -la clips/$name.mp4 2>/dev/null | awk '{print $5}')" >> dl.log
done
