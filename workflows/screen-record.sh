#!/bin/bash
# screen-record.sh — record ONE app window to an mp4 for a `screen-rec` graphic (step 5b, Stage 2).
#
#   ./workflows/screen-record.sh Chrome projects/<job>/assets/captures/g4.mp4 5      # biggest Chrome window, 5 s
#   ./workflows/screen-record.sh Finder out.mp4 4 2                                  # 2nd-biggest window
#   ./workflows/screen-record.sh --clicks Chrome out.mp4 5                           # show click rings
#   ./workflows/screen-record.sh --force Chrome out.mp4 5                            # overwrite an existing out (default: refuse)
#   ./workflows/screen-record.sh --list Chrome                                       # enumerate windows (+ bounds)
#   FPS=24000/1001 ./workflows/screen-record.sh Finder out.mp4 4                      # conform to the job's rate (default 30000/1001)
#
# The still counterpart is window-grab.sh (captures a COVERED window's own buffer, never fronts
# anything). Video cannot do that: `screencapture -v` ignores -l<windowid> and records the whole
# display (measured 2026-09-11), so this records the window's screen RECT and must bring the app
# to the front for the take. That is deliberate and brief: a capture is production footage, not a
# verification frame — say so in the report, and run it in the background so the session can
# drive the action (a scroll, a click, a timeline filling) while the clock runs:
#
#   Bash(run_in_background): ./workflows/screen-record.sh Chrome …/g4.mp4 6
#   ~1 s later: scroll / click via the browser or computer-use tools
#   the recording stops by itself at <seconds>
#
# Output: H.264 mp4 at a CONSTANT rate (FPS=30000/1001 default: pass the timeline's), native pixels (a Retina
# window records at 2x its point size — the printed WxH is what the comp scales). No audio. macOS only (Windows: OBS or Xbox Game Bar by hand).

set -u
case "$(uname -s)" in Darwin) ;; *) echo "[screen-record] macOS only — record the window with OBS / Win+G and drop the file in projects/<job>/assets/captures/" >&2; exit 3 ;; esac

LIST_ONLY=0; CLICKS=""; FORCE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --list) LIST_ONLY=1; shift ;;
    --clicks) CLICKS="-k"; shift ;;
    -h|--help) sed -n '2,23p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    --force) FORCE=1; shift ;;
    *) break ;;
  esac
done

APP="${1:-}"
OUT="${2:-}"
SECS="${3:-5}"
INDEX="${4:-1}"
[ -n "$APP" ] || { echo "usage: screen-record.sh [--clicks] [--force] <App> <out.mp4> [seconds] [index]   |   --list <App>" >&2; exit 2; }
case "$APP" in -*) echo "[screen-record] flags go BEFORE the app name: $APP" >&2; exit 2 ;; esac
command -v swift >/dev/null || { echo "[screen-record] needs swift (Xcode command line tools: xcode-select --install) to read the window list" >&2; exit 2; }
if [ "$LIST_ONLY" -eq 0 ]; then
  [ -n "$OUT" ] || { echo "[screen-record] missing output path" >&2; exit 2; }
  case "$OUT" in -*) echo "[screen-record] flags go BEFORE the app name: $OUT" >&2; exit 2 ;; *.rec.mov) echo "[screen-record] .rec.mov is the scratch name" >&2; exit 2 ;; esac
  case "$SECS" in ''|*[!0-9.]*|.|*.*.*) echo "[screen-record] seconds must be a number, got '$SECS'" >&2; exit 2 ;; esac
  case "$INDEX" in ''|*[!0-9]*|0) echo "[screen-record] index must be a positive integer, got '$INDEX'" >&2; exit 2 ;; esac
  if [ -e "$OUT" ] && [ "$FORCE" -eq 0 ]; then echo "[screen-record] $OUT exists — a capture already in a comp keeps its name; write a new one or pass --force" >&2; exit 2; fi
  for t in screencapture ffmpeg ffprobe osascript; do command -v "$t" >/dev/null || { echo "[screen-record] needs $t" >&2; exit 2; }; done
fi

SWIFT_SRC="$(mktemp /tmp/screc-XXXXXX.swift)"
trap 'rm -f "$SWIFT_SRC"' EXIT
cat > "$SWIFT_SRC" <<'SWIFT'
import CoreGraphics
import Foundation
let needle = CommandLine.arguments.count > 1 ? CommandLine.arguments[1].lowercased() : ""
// on-screen only: a window on another Space or minimized cannot be in front of the rect we record
let opts = CGWindowListOption(arrayLiteral: .excludeDesktopElements, .optionOnScreenOnly)
guard let list = CGWindowListCopyWindowInfo(opts, kCGNullWindowID) as? [[String: Any]] else {
    FileHandle.standardError.write("cannot read window list (Screen Recording permission?)\n".data(using: .utf8)!)
    exit(1)
}
var rows: [(Int, String)] = []
for w in list {
    let owner = (w[kCGWindowOwnerName as String] as? String) ?? ""
    if !needle.isEmpty && !owner.lowercased().contains(needle) { continue }
    if ((w[kCGWindowLayer as String] as? Int) ?? 0) != 0 { continue }
    let num = (w[kCGWindowNumber as String] as? Int) ?? 0
    let pid = (w[kCGWindowOwnerPID as String] as? Int) ?? 0
    let name = (w[kCGWindowName as String] as? String) ?? ""
    let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
    let x = Int((b["X"] as? Double) ?? 0), y = Int((b["Y"] as? Double) ?? 0)
    let wd = Int((b["Width"] as? Double) ?? 0), ht = Int((b["Height"] as? Double) ?? 0)
    if wd < 200 || ht < 200 { continue }
    rows.append((wd * ht, "\(num)\t\(pid)\t\(x)\t\(y)\t\(wd)\t\(ht)\t\(owner)\t\(name)"))
}
rows.sort { $0.0 > $1.0 }
for r in rows { print(r.1) }
SWIFT

ROWS="$(swift "$SWIFT_SRC" "$APP" 2>/dev/null)"
if [ -z "$ROWS" ] && [ "${APP#* }" != "$APP" ]; then
  FIRST="${APP%% *}"; ROWS="$(swift "$SWIFT_SRC" "$FIRST" 2>/dev/null)"
  [ -n "$ROWS" ] && echo "[screen-record] no window owner contains '$APP'; matched '$FIRST' instead" >&2
fi
if [ -z "$ROWS" ]; then
  echo "[screen-record] no ON-SCREEN window owner contains '$APP' (minimized / other Space / not running)" >&2
  OWNERS="$(swift "$SWIFT_SRC" "" 2>/dev/null | cut -f7 | sort -u | paste -sd, - | sed 's/,/, /g')"
  echo "[screen-record]   owners on screen right now: ${OWNERS:-none (Screen Recording permission?)}" >&2
  exit 1
fi

if [ "$LIST_ONLY" -eq 1 ]; then
  echo "$ROWS" | awk -F'\t' 'BEGIN{printf "%-8s %-7s %-18s %-28s %s\n","WINDOWID","PID","RECT(x,y,w,h)","APP","TITLE"}
                             {printf "%-8s %-7s %-18s %-28s %s\n",$1,$2,$3","$4","$5","$6,$7,$8}'
  exit 0
fi

ROW="$(echo "$ROWS" | sed -n "${INDEX}p")"
[ -n "$ROW" ] || { echo "[screen-record] no window at index $INDEX (have $(echo "$ROWS" | wc -l | tr -d ' '))" >&2; exit 1; }
PID="$(echo "$ROW" | cut -f2)"; X="$(echo "$ROW" | cut -f3)"; Y="$(echo "$ROW" | cut -f4)"
W="$(echo "$ROW" | cut -f5)"; H="$(echo "$ROW" | cut -f6)"; OWNER="$(echo "$ROW" | cut -f7)"; TITLE="$(echo "$ROW" | cut -f8)"

mkdir -p "$(dirname "$OUT")"
TMP="${OUT%.*}.rec.mov"

# front the owning process (by pid — CGWindow owner names are not always AppleScript app names)
osascript -e "tell application \"System Events\" to set frontmost of (first process whose unix id is $PID) to true" >/dev/null 2>&1 \
  || echo "[screen-record] could not front pid $PID — recording whatever is on top of the rect" >&2
sleep 0.4

echo "[screen-record] REC $OWNER — $TITLE  rect ${X},${Y} ${W}x${H}  ${SECS}s -> $OUT"
screencapture -x $CLICKS -v -V"$SECS" -R"${X},${Y},${W},${H}" "$TMP" || { echo "[screen-record] screencapture failed" >&2; exit 1; }
[ -s "$TMP" ] || { echo "[screen-record] wrote an EMPTY file" >&2; exit 1; }

# screencapture writes a VARIABLE-rate H.264 .mov (measured 19200/1 timebase, ~50 fps effective): a frame
# extractor fed VFR drifts, so conform to a constant rate (FPS=, default the house 29.97), drop any audio
FPS="${FPS:-30000/1001}"
ffmpeg -v error -y -i "$TMP" -an -vf "fps=$FPS" -c:v libx264 -crf 14 -pix_fmt yuv420p -movflags +faststart "$OUT" \
  || { echo "[screen-record] conform failed, keeping $TMP" >&2; exit 1; }
rm -f "$TMP"
echo "[screen-record] $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height:format=duration -of csv=p=0 "$OUT" | tr '\n' ' ' | sed 's/,/x/; s/ *$//') -> $OUT"
