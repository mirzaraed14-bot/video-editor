#!/bin/bash
# pass 3 freshness for the "Hi Me -> I feel alone" join, 17 Nov ~18:45 PKT
cd "X:/Claude Projects/video-editor-client/video-editor"
SP="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/0a237a74-8ef9-4237-ac12-5362d544e623/scratchpad"
D=research/aw-speed-2026-11-17/pass3/api
run() { tag=$1; q=$2; extra=$3
  python -I research/deep-research-2026-11-14/yt_api.py speed-beats search part=snippet type=video "q=$q" videoDuration=short $extra maxResults=50 > $D/s_$tag.json 2> $D/s_$tag.err
  n=$(python -I -c "import json,sys;print(len(json.load(open(sys.argv[1],encoding='utf-8')).get('items',[])))" $D/s_$tag.json 2>/dev/null)
  if [ "$n" = "0" ] || [ -z "$n" ]; then echo "== $tag: 0 items, retry"; python -I research/deep-research-2026-11-14/yt_api.py speed-beats search part=snippet type=video "q=$q" videoDuration=short maxResults=50 > $D/s_$tag.json 2> $D/s_$tag.err; fi
  echo "===== $tag | $q"; python -I "$SP/stats.py" $D/s_$tag.json $D/v_$tag.json 20; }
run fr_hime "ishowspeed hi me in 3 years" order=viewCount
run fr_nobody "ishowspeed nobody understands me" order=viewCount
