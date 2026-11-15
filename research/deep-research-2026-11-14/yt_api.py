#!/usr/bin/env python3
"""yt_api.py: the one door to the YouTube Data API v3 for the AW research runs (Affan's key, 14 Nov 2026).

    python -I research/deep-research-2026-11-14/yt_api.py <session> <endpoint> name=value ...

    <session>  : hp-cast | hp-films | bolt-celeb | ig-mj | ig-icons | ig-sports | speed | hub
                 affanwiz = the AffanWiz research session (Affan's OK 15 Nov 2026: channel listings only, 0 searches)
    <endpoint> : search | videos | channels | commentThreads | playlistItems

Examples (from the repo root):
    ... yt_api.py hp-cast search type=video q="tom felton broadway" videoDuration=short order=viewCount maxResults=50
    ... yt_api.py hp-cast videos part=snippet,statistics,contentDetails id=ID1,ID2,ID3   (up to 50 ids; never add maxResults)
    ... yt_api.py hp-cast channels part=snippet,statistics,contentDetails id=UCxxxx
    ... yt_api.py hp-cast playlistItems part=contentDetails playlistId=UUxxxx maxResults=50
        (a channel's latest uploads: its uploads playlist is 'UU' + the channel id after 'UC'; 1 unit, so never `search` for that)

It prints the JSON answer on stdout and a one-line tally on stderr. It never prints the key.
What it enforces:
  - search = 100 units, everything else 1. The day's allowance is 10,000 units (100 searches), shared by every caller,
    reset at midnight Pacific. Each session gets 12 searches per Pacific day (the hub 20); all callers together stop at 95.
  - A request already answered in the last 12 hours comes from the cache, free.
  - Every call is logged in yt_api_log.jsonl next to this file (never the key).
  - HTTP 403 quotaExceeded writes yt_api.QUOTA, and every later call stops (exit 75) until the next Pacific day.
Nothing here touches youtube.com itself, and nothing plays or downloads media.
"""
import datetime
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
KEYFILE = r"X:\Claude Projects\Abundance Wisdom\API Key Abundance Wisdom YT Searcher.txt"
LOG = os.path.join(HERE, "yt_api_log.jsonl")
CACHE = os.path.join(HERE, "yt_api_cache")
QUOTA = os.path.join(HERE, "yt_api.QUOTA")
COST = {"search": 100, "videos": 1, "channels": 1, "commentThreads": 1, "playlistItems": 1}
SESSIONS = {"hp-cast", "hp-films", "bolt-celeb", "ig-mj", "ig-icons", "ig-sports", "speed", "hub", "affanwiz"}
CAP = {"hub": 20, "ig-mj": 18, "affanwiz": 0}  # ig-mj +6 on 15 Nov ~02:35 for his "go all out" MJ arc, from the idle lanes' unused searches
# affanwiz: the AffanWiz research session (creator-shorts). Affan OK'd this key for it on 15 Nov 2026 for channel
# listings only, so its search cap is 0: the 100 searches a day stay with the AW sessions.
DEFAULT_CAP = 12
ALL_CAP = 95
CACHE_HOURS = 12

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def die(msg, code):
    sys.stderr.write("yt_api: " + msg + "\n")
    sys.exit(code)


def pacific_day():
    # November is PST (UTC-8); the allowance resets at midnight Pacific.
    return (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=8)).strftime("%Y-%m-%d")


def read_log():
    rows = []
    if os.path.exists(LOG):
        with open(LOG, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except ValueError:
                        pass
    return rows


def append_log(row):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    if len(sys.argv) < 3:
        die("usage: yt_api.py <session> <endpoint> name=value ... (see the top of this file)", 64)
    session, endpoint = sys.argv[1], sys.argv[2]
    if session not in SESSIONS:
        die("unknown session %r (one of: %s)" % (session, ", ".join(sorted(SESSIONS))), 64)
    if endpoint not in COST:
        die("unknown endpoint %r (one of: %s)" % (endpoint, ", ".join(COST)), 64)
    params = {}
    for a in sys.argv[3:]:
        if "=" not in a:
            die("arguments are name=value, got %r" % a, 64)
        k, v = a.split("=", 1)
        if k.lower() == "key":
            die("never pass a key: this script reads it from the key file itself", 64)
        params[k] = v
    if "part" not in params:
        params["part"] = "snippet" if endpoint in ("search", "commentThreads") else "snippet,statistics,contentDetails"
        if endpoint == "playlistItems":
            params["part"] = "snippet,contentDetails"
    if endpoint == "videos" and "id" in params and "maxResults" in params:
        del params["maxResults"]  # Google rejects maxResults together with id
    day = pacific_day()

    if os.path.exists(QUOTA):
        with open(QUOTA, encoding="utf-8") as f:
            if f.read().strip() == day:
                die("today's allowance is used up (yt_api.QUOTA); it comes back at midnight Pacific", 75)

    os.makedirs(CACHE, exist_ok=True)
    ck = hashlib.sha256((endpoint + "?" + urllib.parse.urlencode(sorted(params.items()))).encode("utf-8")).hexdigest()[:24]
    cpath = os.path.join(CACHE, ck + ".json")
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(cpath) and time.time() - os.path.getmtime(cpath) < CACHE_HOURS * 3600:
        with open(cpath, encoding="utf-8") as f:
            data = f.read()
        append_log({"t": stamp, "day": day, "session": session, "endpoint": endpoint, "params": params,
                    "units": 0, "cached": True, "ok": True})
        sys.stdout.write(data + "\n")
        sys.stderr.write("yt_api: %s from the cache (0 units)\n" % endpoint)
        return

    rows = [r for r in read_log() if r.get("day") == day and not r.get("cached") and r.get("endpoint") == "search"]
    mine = sum(1 for r in rows if r.get("session") == session)
    cap = CAP.get(session, DEFAULT_CAP)
    if endpoint == "search":
        if mine >= cap:
            die("%s has used its %d searches for Pacific day %s: use videos/playlistItems, reuse the log, or ask the hub"
                % (session, cap, day), 75)
        if len(rows) >= ALL_CAP:
            die("all callers together have used %d searches today; the rest is the hub's reserve" % len(rows), 75)

    with open(KEYFILE, encoding="utf-8-sig") as f:
        key = f.read().strip()
    url = "https://www.googleapis.com/youtube/v3/" + endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-goog-api-key": key, "Accept": "application/json"})
    row = {"t": stamp, "day": day, "session": session, "endpoint": endpoint, "params": params,
           "units": COST[endpoint], "cached": False}
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace").replace(key, "***")
        reason = ""
        try:
            reason = json.loads(body)["error"]["errors"][0].get("reason", "")
        except Exception:
            pass
        row.update({"ok": False, "http": e.code, "reason": reason})
        append_log(row)
        if e.code == 403 and reason in ("quotaExceeded", "dailyLimitExceeded"):
            with open(QUOTA, "w", encoding="utf-8") as f:
                f.write(day)
            die("HTTP 403 quotaExceeded: today's allowance is used up; stop until midnight Pacific", 75)
        die("HTTP %d %s: %s" % (e.code, reason, body[:400]), 2)
    except Exception as e:  # network trouble
        row.update({"ok": False, "error": type(e).__name__})
        append_log(row)
        die("network error: %s" % str(e).replace(key, "***")[:200], 3)
    row["ok"] = True
    append_log(row)
    with open(cpath, "w", encoding="utf-8") as f:
        f.write(data)
    sys.stdout.write(data + "\n")
    if endpoint == "search":
        sys.stderr.write("yt_api: search (100 units); %s %d/%d searches today, all callers %d/%d\n"
                         % (session, mine + 1, cap, len(rows) + 1, ALL_CAP))
    else:
        sys.stderr.write("yt_api: %s (1 unit)\n" % endpoint)


if __name__ == "__main__":
    main()
