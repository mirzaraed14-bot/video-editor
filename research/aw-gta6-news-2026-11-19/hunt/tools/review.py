import sys, json, glob, re, os, time, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
KW = re.compile(r"bigfoot|big foot|skunk|sasquatch|mangrove|effigy|monster|creature|scream|scared|scary|jump ?scare|spooked|wtf|what is that|knocked|passed out|swamp|\bape\b|kirk|drone", re.I)
STRONG = re.compile(r"bigfoot|big foot|skunk|sasquatch|mangrove|effigy|monster|creature|swamp|\bape\b|kirk|knocked|passed out", re.I)
ch = sys.argv[1]; TOP = int(sys.argv[2]) if len(sys.argv) > 2 else 15
by = {}; rngs = []
fl = glob.glob(f"lists/r-{ch}-*.json") + glob.glob(f"../twitch/r-{ch}.json") + glob.glob("../twitch/kai-7d.json" if ch=="kaicenat" else "../twitch/none")
for f in fl:
    m_ = re.search(r"-(24hr|7d|all)\.json$", f); rng = m_.group(1) if m_ else "old24"; rngs.append(rng)
    try: j = json.load(open(f, encoding="utf-8"))
    except Exception: continue
    for e in j.get("entries") or []:
        e["_rng"] = rng
        by.setdefault(e["id"], e)
es = list(by.values())
match = sorted([e for e in es if KW.search(e.get("title") or "")], key=lambda e: -(e.get("view_count") or 0))
rest = sorted([e for e in es if e not in match], key=lambda e: -(e.get("view_count") or 0))[:TOP]
print(f"# {ch}: ranges={sorted(set(rngs))} clips={len(es)} grep-match={len(match)} strong={sum(1 for e in match if STRONG.search(e['title']))}")
rows = []
for kind, L in (("M", match), ("t", rest)):
    for e in L:
        r = dict(ch=ch, kind="match" if kind == "M" else "top", id=e["id"], title=e.get("title"), views=e.get("view_count"), dur=e.get("duration") or 0, ts=e.get("timestamp"), url=e["url"], thumb=e.get("thumbnail"))
        rows.append(r)
        print(f"{kind} {r['views'] or 0:>7}v {r['dur']:>4.0f}s {time.strftime('%m-%d %H:%M', time.localtime(r['ts']))} {e['_rng']:>4} | {r['title'][:70]} | {r['id']}")
os.makedirs("sel", exist_ok=True)
json.dump(dict(rows=rows, log=[(ch, len(es), len(match))]), open(f"sel/{ch}.json", "w", encoding="utf-8"), ensure_ascii=False)
