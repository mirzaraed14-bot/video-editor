#!/usr/bin/env bash
# ighold.sh <seconds>: take the shared Instagram pace slot and HOLD it while this session's page does its own loads >= 31 s apart
cd "/x/Claude Projects/video-editor-client/video-editor"
bash projects/_onyx-batch2-2026-10/pace.sh instagram bash -c "echo HELD \$(date +%T) > research/aw-hp-2026-11-26/ig.held; sleep $1; rm -f research/aw-hp-2026-11-26/ig.held"
