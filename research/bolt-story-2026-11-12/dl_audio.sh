#!/usr/bin/env bash
# Audio-only downloads of Bolt Motivation Shorts for the story-framework study (AW pick session, 2026-11-12).
# One request per >=65 s through lock.sh youtube. Nothing is played. Stops on ANY failure; a 429 / bot page sets the BLOCKED flag.
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
OUT=research/bolt-story-2026-11-12/audio
for id in "$@"; do
  if ls "$OUT/$id".* >/dev/null 2>&1; then continue; fi
  log=$(mktemp)
  bash $L youtube yt-dlp --no-warnings --no-playlist -f "ba[ext=m4a]/ba" -o "$OUT/%(id)s.%(ext)s" -- "https://www.youtube.com/shorts/$id" >"$log" 2>&1
  rc=$?; cat "$log"; echo "$(date '+%T') $id rc=$rc" >> "$OUT/../dl.log"
  if [ $rc -ne 0 ]; then
    if grep -qiE "429|not a bot|confirm you|Sign in to confirm|Too Many Requests" "$log"; then
      [ -f "$FLAG" ] || echo "429/bot AW-pick-2026-11-12 bolt audio $id $(date '+%F %T')" > "$FLAG"
      echo "$(date '+%T') BOT/429 -> flag written, stopping" >> "$OUT/../dl.log"; exit 2
    fi
    echo "$(date '+%T') failure rc=$rc, stopping" >> "$OUT/../dl.log"; exit 1
  fi
  rm -f "$log"; sleep 45
done
echo "$(date '+%T') done" >> "$OUT/../dl.log"
