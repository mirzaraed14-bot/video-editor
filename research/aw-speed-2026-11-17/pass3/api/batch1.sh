#!/bin/bash
# pass 3 framework pricing, 17 Nov ~18:05 PKT. One search per framework query, then videos stats.
cd "X:/Claude Projects/video-editor-client/video-editor"
SP="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/0a237a74-8ef9-4237-ac12-5362d544e623/scratchpad"
D=research/aw-speed-2026-11-17/pass3/api
run() { # tag query
  tag=$1; q=$2
  python -I research/deep-research-2026-11-14/yt_api.py speed-beats search part=snippet type=video "q=$q" videoDuration=short order=viewCount maxResults=50 > $D/s_$tag.json 2> $D/s_$tag.err
  n=$(python -I -c "import json,sys;print(len(json.load(open(sys.argv[1],encoding='utf-8')).get('items',[])))" $D/s_$tag.json 2>/dev/null)
  if [ "$n" = "0" ] || [ -z "$n" ]; then
    echo "== $tag: 0 items, retry without order"; cat $D/s_$tag.err | head -3
    python -I research/deep-research-2026-11-14/yt_api.py speed-beats search part=snippet type=video "q=$q" videoDuration=short maxResults=50 > $D/s_$tag.json 2> $D/s_$tag.err
  fi
  echo "===== $tag | $q"
  python -I "$SP/stats.py" $D/s_$tag.json $D/v_$tag.json 18
}
run f1a_alone "ishowspeed feels alone"
run f1a_therapist "ishowspeed i need a therapist"
run f6_thrown "ishowspeed objects thrown at him world cup"
run f6_messi "messi ignored ishowspeed"
run f6_ksi "ksi laughing at ishowspeed crying"
run f1c_mom "ishowspeed ignored his mom"
run f3_final "ishowspeed mom didn't come world cup final"
run f4_dad "ishowspeed dad song about him"
run f5_dog "ishowspeed dog died"
