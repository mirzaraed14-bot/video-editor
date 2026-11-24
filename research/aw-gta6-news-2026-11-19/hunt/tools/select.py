import sys, json, glob, re, os, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# usage: select.py <outjson> <list-glob...>  -> merges lists per channel (dedupe by id), picks keyword matches + top-N vague by views
KW = re.compile(r"bigfoot|big foot|skunk|sasquatch|mangrove|effigy|monster|creature|scream|scared|scary|jump ?scare|spooked|wtf|what is that|knocked|passed out|swamp|\bape\b|kirk|drone", re.I)
CH = "kaicenat ishowspeed xqc ludwig adinross jynxzi lacy caseoh_ summit1g fanum asmongold timthetatman sodapoppin ohnepixel clix typicalgamer valkyrae pokimane shroud nadeshot n3on plaqueboymax agent00 emiru mizkif hasanabi esfandtv quin69 ninja dream ranboo tommyinnit stableronaldo jasontheween theburntpeanut brendaniel hutchmf swagg".split()
out = sys.argv[1]; globs = sys.argv[2:]
by = {}
for g in globs:
    for f in glob.glob(g):
        b = os.path.basename(f)
        m = re.match(r"(?:r-)?(.+?)(?:-(24hr|7d|all))?\.json$", b)
        ch = m.group(1)
        try: j = json.load(open(f, encoding="utf-8"))
        except Exception: continue
        for e in j.get("entries") or []:
            by.setdefault(ch, {})[e["id"]] = e
rows = []; log = []
for ch in CH:
    es = list(by.get(ch, {}).values())
    match = [e for e in es if KW.search(e.get("title") or "")]
    rest = sorted([e for e in es if e not in match], key=lambda e: -(e.get("view_count") or 0))[:15]
    log.append((ch, len(es), len(match)))
    for e in match: rows.append(dict(ch=ch, kind="match", id=e["id"], title=e.get("title"), views=e.get("view_count"), dur=e.get("duration"), ts=e.get("timestamp"), url=e["url"], thumb=e.get("thumbnail")))
    for e in rest: rows.append(dict(ch=ch, kind="top", id=e["id"], title=e.get("title"), views=e.get("view_count"), dur=e.get("duration"), ts=e.get("timestamp"), url=e["url"], thumb=e.get("thumbnail")))
json.dump(dict(rows=rows, log=log), open(out, "w", encoding="utf-8"), ensure_ascii=False)
print(len(rows), "rows;", sum(1 for r in rows if r["kind"] == "match"), "matches")
for l in log: print(l)
