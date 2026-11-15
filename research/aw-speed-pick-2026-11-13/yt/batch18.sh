#!/usr/bin/env bash
# batch18 = wave 1 after the YouTube unblock: mom-moment dates + audio for MOM-MOMENTS.md § 7.
# Written 14 Nov 2026 ~17:40 by aw-speed-research.
# RUN ONLY after the hub has removed projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED, from ONE session, in the hub's order.
# REVISED 14 Nov ~21:55 (hub: the YouTube Data API replaces every yt-dlp search/metadata call): the meta + search steps were done
# through research/deep-research-2026-11-14/yt_api.py (results in MOM-MOMENTS.md § 4); only audio downloads remain, via pace.sh.
# OPTIONAL since Affan's Tella-2 cut (he dropped the extra mom clips): run only if the hub or the build still wants them.
# The build's mom/tools/queue.txt and yt/batch17.sh must NOT run at the same time.
# Stops on a bot check / 429 (re-sets the flag); skips age gates (no bypass). Then CPU transcripts (faster-whisper small.en).
# Silent: audio files only, nothing is played.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
L=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
R=research/aw-speed-pick-2026-11-13
log=$R/yt/batch18.log
out=$R/src/mom
mkdir -p "$out" "$R/scout/mom"
if [ -f "$FLAG" ]; then echo "YouTube still BLOCKED, not running ($(date '+%T'))" | tee -a "$log"; exit 75; fi

bad() { tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; }
stop() {
  echo "$(date '+%F %T') aw-speed-research batch18: bot check or 429 on $1; YouTube stopped; the hub clears this flag." > "$FLAG"
  echo "BOT/429 on $1: flag set, stopping" >> "$log"; exit 9
}
after() {  # $1 = rc, $2 = id
  [ "$1" -eq 75 ] && { echo "lock.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  bad && stop "$2"
  tail -6 "$log" | grep -qi "confirm your age" && echo "age gate on $2: skipped (not bypassed)" >> "$log"
  sleep 45
}
meta() {
  echo "== meta $1 $(date '+%T')" >> "$log"
  bash $L youtube yt-dlp --skip-download --no-playlist \
    --print "%(id)s | %(upload_date)s | %(duration)s | %(view_count)s | %(channel)s | %(height)sp | %(title)s || %(description).300s" \
    "https://www.youtube.com/watch?v=$1" >> "$log" 2>&1
  after $? "$1"
}
aud() {
  echo "== audio $1 $(date '+%T')" >> "$log"
  bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --write-info-json \
    -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$1" >> "$log" 2>&1
  after $? "$1"
}
srch() {
  echo "== search: $1 $(date '+%T')" >> "$log"
  bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" \
    "ytsearch10:$1" >> "$log" 2>&1
  after $? "search"
}

# 1. Dates and facts first
# (done via the API 21:50) meta t-RMVq_6hTQ    # C2's original ("cried in front of his mother, you don't love me"): after 21 Jan 2023 = he was 18
# (done via the API 21:50) meta HOk9WtMWDZ8    # "Adin PLANS Speed's Bday Party with HIS MOM" (21 Jan 2023): was his mom part of a surprise? (§ 1a)
aud  HOk9WtMWDZ8
aud  v-CQFdbVgCI    # C9 "the reason my mom kicked me out" (Nov 2021): the kick-out in his words at the time
# 2. Mother's Day 2023 (§ 4): the clip (what follows the hang-up?) and the "MOTHERS DAY" VOD (14 May 2023, 214 min)
aud  P4HHaMkbUi0    # Mother's Day hang-up clip (Ishowspeedclips, 15 May 2023, 1:13); the VOD is L2L9wxeipDk "MOTHERS DAY" (14 May 2023)
# (done via the API 21:50) srch "IShowSpeed MOTHERS DAY stream May 14 2023"
# 3. The old mom-house streams (his own streams are IN since his 14 Nov ruling), short clips first
aud  bcIJJb9-JjA    # C1a: locates the yelling inside his own 600K VOD D5FYQQm7IYs (28 Jun 2021)
aud  H81Qnad27jQ    # C2 clip
aud  _VSHiZ8G8B8    # C3 "Speed Mom Made Him Cry (Old Upload)"
aud  m_MxS1uvnYc    # C7 "Moms Gets Mad and Makes Him End Stream" (criterion 2)
aud  12bBWIGNjU4    # C5 "Mom Ruins Stream Again (speed says he's moving out)"
aud  ObWG_5dENy0    # C6 "Mom Tells Him To Stop Streaming"
echo "YT DONE $(date '+%T')" >> "$log"

# 4. CPU transcripts, one file at a time (parallel runs crash with mkl_malloc). Wave 2 (HD sections) follows from these.
P="C:/Users/affan/.cache/video-editor/whisperx-venv/Scripts/python.exe"
cd "$R" || exit 1
for f in src/mom/*.m4a src/mom/*.webm src/mom/*.opus; do
  [ -f "$f" ] || continue
  "$P" -I yt/cpu_scout.py scout/mom "$f" >> yt/batch18.log 2>&1
done
echo "ALL DONE $(date '+%T')" >> yt/batch18.log
