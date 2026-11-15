#!/usr/bin/env bash
# Phase B: the ET Berlin family carpet (G2: Prince + Bigi in the armbands), then ET's Gary house tour (card 2).
# Starts after phase A's downloads; transcribes only after phase A's transcripts (no parallel ASR).
. "/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/ig-mj/tools/common.sh"
until [ -f "$R/dl/.a_downloads_done" ]; do [ -f "$FLAG" ] && exit 75; sleep 15; done
dl snMguJ8UuyI "projects/mj-son-red-armband/sources/snMguJ8UuyI"
dl 8Ys5IngU6wg "$R/dl/8Ys5IngU6wg"
w=0; until [ -f "$R/dl/.a_post_done" ] || [ $w -gt 5400 ]; do sleep 15; w=$((w+15)); done
post "projects/mj-son-red-armband/sources/snMguJ8UuyI/snMguJ8UuyI.mp4"
post "$R/dl/8Ys5IngU6wg/8Ys5IngU6wg.mp4"
echo "PHASE B DONE $(date '+%T')" >> "$log"
