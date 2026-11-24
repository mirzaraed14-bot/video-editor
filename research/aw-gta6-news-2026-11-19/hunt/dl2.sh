#!/bin/bash
# priority list puller: reads lq.txt lines "<channel> <range>"; shares yt.sh lock; yields nothing to pull.sh (sets .dlwant while busy)
cd "$(dirname "$0")"; . ./yt.sh; touch lq.txt lq-done.txt
while true; do
  line=$(grep -vxFf lq-done.txt lq.txt | head -1)
  if [ -z "$line" ]; then [ -f STOP2 ] && exit 0; sleep 6; continue; fi
  touch .dlwant
  ch=$(echo $line | cut -d' ' -f1); rng=$(echo $line | cut -d' ' -f2); out="lists/r-$ch-$rng.json"
  rm -f "$out"
  yt --flat-playlist --playlist-end 150 -J "https://www.twitch.tv/$ch/clips?filter=clips&range=$rng" > "$out" 2> "lists/r-$ch-$rng.err"
  echo "$line" >> lq-done.txt; echo "$(date +%T) list $ch $rng $(wc -c < $out)" >> dl2.log
done
