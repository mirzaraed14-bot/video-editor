#!/usr/bin/env bash
# Polite retry: wait out a YouTube rate-limit block, then fetch the missing reference clips one at a time.
cd "$(dirname "$0")"
for attempt in $(seq 1 14); do
  missing=$(cut -f1 sources.tsv | while read c; do [ -f "src/$c.mp4" ] || echo "$c"; done)
  [ -z "$missing" ] && { echo "ALL DONE"; ls -la src; exit 0; }
  bash fetch.sh > "work-fetch-$attempt.log" 2>&1
  grep -E "^FAILED" "work-fetch-$attempt.log" | tr '\n' ' '; echo "(attempt $attempt)"
  still=$(cut -f1 sources.tsv | while read c; do [ -f "src/$c.mp4" ] || echo "$c"; done)
  [ -z "$still" ] && { echo "ALL DONE"; ls -la src; exit 0; }
  sleep 300
done
echo "GAVE UP after 14 attempts"; ls -la src
