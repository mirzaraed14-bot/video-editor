#!/usr/bin/env bash
# Phase A (the pitch): Prince's own GRWM vlog, then Sunrise. Waits for 23:50 PKT, then for the YouTube lock to be quiet 120 s
# (Speed, ig-icons, hp-films go first; capped at 00:30), then one at a time through pace.sh.
. "/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/ig-mj/tools/common.sh"
now=$(date +%s); t=$(date -d "today 23:50" +%s); [ "$t" -gt "$now" ] && sleep $((t-now))
cap=$(date -d "tomorrow 00:30" +%s); free=0
while [ $free -lt 120 ] && [ "$(date +%s)" -lt "$cap" ]; do if [ -d "$LOCKDIR" ]; then free=0; else free=$((free+5)); fi; sleep 5; done
echo "phase A start $(date '+%F %T') (lock quiet ${free}s)" >> "$log"
P=projects/mj-son-red-armband/sources
dl ESeXvAeuokU "$P/ESeXvAeuokU"
dl uNF0GMRPO1w "$P/uNF0GMRPO1w"
touch "$R/dl/.a_downloads_done"
post "$P/ESeXvAeuokU/ESeXvAeuokU.mp4"
post "$P/uNF0GMRPO1w/uNF0GMRPO1w.mp4"
touch "$R/dl/.a_post_done"
echo "PHASE A DONE $(date '+%T')" >> "$log"
