#!/usr/bin/env bash
# lock.sh <youtube|gpu> <command...> : run a command holding a batch-wide lock (several agents share this machine, 2026-10-12).
#   youtube: ONE YouTube request stream at a time (four agents at once got the IP bot-blocked at 04:35), plus a 20 s cool-down after.
#   gpu:     ONE GPU job at a time (WhisperX, Topaz, faster-whisper): parallel ones run out of VRAM.
# A lock older than its stale limit (youtube 30 min, gpu 90 min) is treated as left behind by a killed run and taken over.
set -u
name=$1; shift
dir="/x/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch2-2026-10/.locks/$name.lock"
# 2026-10-14: a YouTube bot-block is a FLAG, not a retry signal: while .locks/youtube.BLOCKED exists every youtube call fails fast
# (exit 75) so no agent touches YouTube; only the main session removes the flag after one spaced probe answers normally.
blocked="/x/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED"
if [ "$name" = youtube ] && [ -f "$blocked" ]; then echo "lock.sh: YouTube is BLOCKED ($(cat "$blocked")): do not retry; read published text instead" >&2; exit 75; fi
mkdir -p "$(dirname "$dir")"
stale=$([ "$name" = youtube ] && echo 1800 || echo 5400)
while ! mkdir "$dir" 2>/dev/null; do
  age=$(( $(date +%s) - $(stat -c %Y "$dir" 2>/dev/null || date +%s) ))
  if [ "$age" -gt "$stale" ]; then rm -rf "$dir"; continue; fi
  sleep 10
done
if [ "$name" = youtube ] && [ -f "$blocked" ]; then rm -rf "$dir"; echo "lock.sh: YouTube is BLOCKED ($(cat "$blocked")): do not retry" >&2; exit 75; fi   # set while we queued
echo "$$ $(date '+%F %T') $*" > "$dir/owner"
"$@"; rc=$?
[ "$name" = youtube ] && sleep 20
rm -rf "$dir"
exit $rc
