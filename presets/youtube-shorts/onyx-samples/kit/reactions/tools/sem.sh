#!/usr/bin/env bash
# sem.sh <cmd...>: run a heavy CPU command in one of 3 slots (main 2026-11-13: was 2; 28 cores, ~12 GB free, 7 render queues) shared by the batch-7 reaction builders (RAM is tight).
# A slot older than 60 min is treated as left behind by a killed run and taken over.
set -u
L="/x/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch7-2026-11/reactions/.sem"; mkdir -p "$L"
while :; do
  for s in a; do
    if mkdir "$L/$s" 2>/dev/null; then
      echo "$$ $(date '+%F %T') $*" > "$L/$s/owner"; "$@"; rc=$?; rm -rf "$L/$s"; exit $rc
    fi
    age=$(( $(date +%s) - $(stat -c %Y "$L/$s" 2>/dev/null || date +%s) )); [ "$age" -gt 3600 ] && rm -rf "$L/$s"
  done
  sleep 10
done
