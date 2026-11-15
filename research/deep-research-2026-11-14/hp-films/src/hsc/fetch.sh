#!/usr/bin/env bash
# Download HSC episode audio from the show's own RSS enclosures (megaphone), sequentially, tracker prefixes stripped. Not YouTube.
set -u
cd "$(dirname "$0")"
while IFS=$'\t' read -r slug url; do
  direct="https://traffic.megaphone.fm/${url#*traffic.megaphone.fm/}"
  [ -s "$slug.mp3" ] && { echo "have $slug"; continue; }
  echo "[$(date +%T)] get $slug"
  curl -sS -L --fail --max-time 900 -A "Mozilla/5.0" -o "$slug.mp3" "$direct" || echo "FAIL $slug"
  sleep 5
done < urls.tsv
for f in *.mp3; do ffmpeg -nostdin -v error -y -i "$f" -ac 1 -ar 16000 "${f%.mp3}.wav"; done
ls -la
