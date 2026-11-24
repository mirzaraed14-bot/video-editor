#!/usr/bin/env bash
# avatar.sh <job> <@handle>: their channel avatar (900 px) -> projects/<job>/work/avatar.jpg, ONE channel-page request through the shared YouTube queue (lock.sh youtube, 20 s cool-down).
# A network request: never part of a dry run. plan.json graphics reference it as "work/avatar.jpg".
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1
if [ $# -lt 2 ] || [ "$1" = "--help" ]; then sed -n 2,3p "$0"; exit 0; fi
J=projects/$1; H=$2; T=presets/youtube-shorts/onyx-samples/kit/reactions/tools; mkdir -p $J/work
[ -s $J/work/avatar.jpg ] && { echo "avatar exists"; exit 0; }
bash $T/lock.sh youtube yt-dlp --skip-download --flat-playlist --playlist-items 0 -J "https://www.youtube.com/$H" > $J/work/avatar.json 2> $J/work/avatar.err || { tail -n 5 $J/work/avatar.err; exit 1; }
python - "$J" <<'PY'
import json, sys, urllib.request
J = sys.argv[1]; d = json.load(open(f"{J}/work/avatar.json", encoding="utf-8"))
th = [t for t in d.get("thumbnails", []) if "avatar" in (t.get("id") or "")]
print(d.get("channel"), d.get("channel_follower_count"), [t.get("id") for t in th])
if th:
    url = th[-1]["url"]; url = url.split("=s")[0] + "=s900-c-k-c0x00ffffff-no-rj" if "=s" in url else url
    urllib.request.urlretrieve(url, f"{J}/work/avatar.jpg"); print("saved", f"{J}/work/avatar.jpg")
PY
