#!/bin/bash
# cs.sh "vid:term" ... : comment searches (1 unit each), prints top hits by likes
R=/Users/affanbaig/video-editor/research/aw-gta6-reviews-2026-11-21
for pair in "$@"; do
 v=${pair%%:*}; t=${pair#*:}; tag=$(echo "$t"|tr ' /' '__')
 $R/y.sh "c-$v-$tag.json" commentThreads part=snippet videoId=$v "searchTerms=$t" maxResults=100 textFormat=plainText 2>&1 | grep -v "^yt_api: commentThreads" 
 echo "== $v [$t] $(python3 -c "import json;print(len(json.load(open('$R/api/c-$v-$tag.json')).get('items',[])))")"
 python3 $R/ct.py "$R/api/c-$v-$tag.json" ${N:-8}
done
