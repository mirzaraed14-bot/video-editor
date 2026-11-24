import sys, json, glob, re, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
KW = re.compile(r"bigfoot|big foot|bigg+foot|skunk|sasquatch|mangrove|effigy|monster|creature|scream|scared|scary|jump ?scare|spooked|wtf|what is that|knocked|passed out|swamp|\bape\b|kirk|drone", re.I)
STRONG = re.compile(r"bigfoot|big foot|bigg+foot|skunk|sasquatch|mangrove|effigy|monster|creature|swamp|\bape\b|kirk", re.I)
CH = "kaicenat ishowspeed xqc ludwig adinross jynxzi lacy caseoh_ summit1g fanum asmongold timthetatman sodapoppin ohnepixel clix typicalgamer valkyrae pokimane shroud nadeshot n3on plaqueboymax agent00 emiru mizkif hasanabi esfandtv quin69 ninja dream ranboo tommyinnit stableronaldo jasontheween theburntpeanut brendaniel hutchmf swagg".split()
print("| channel | fresh lists pulled (20 Nov) | older 24hr list (19 Nov) | unique clips seen | title grep matches | strong matches (bigfoot/skunk/kirk/swamp/creature...) | note |")
print("|---|---|---|---|---|---|---|")
for ch in CH:
    fr = {}
    for f in glob.glob(f"lists/r-{ch}-*.json"):
        rng = re.search(r"-(24hr|7d|all)\.json$", f).group(1)
        try: j = json.load(open(f, encoding="utf-8"))
        except Exception: continue
        fr[rng] = j.get("entries") or []
    old = []
    for f in glob.glob(f"../twitch/r-{ch}.json") + (glob.glob("../twitch/kai-7d.json") if ch == "kaicenat" else []):
        try: old += json.load(open(f, encoding="utf-8")).get("entries") or []
        except Exception: pass
    allc = {}
    for rng, es in fr.items():
        for e in es: allc[e["id"]] = e
    for e in old: allc[e["id"]] = e
    m = [e for e in allc.values() if KW.search(e.get("title") or "")]
    s = [e for e in m if STRONG.search(e["title"])]
    frs = ", ".join(f"{r}={len(es)}" for r, es in sorted(fr.items())) or "NOT PULLED (lane busy)"
    note = ""
    if fr and all(len(es) == 0 for es in fr.values()): note = "list came back EMPTY: unreliable, treat as a failed pull"
    if ch == "kaicenat": note = "7d list returned only 20 entries (98 yesterday): unreliable"
    print(f"| {ch} | {frs} | {len(old)} | {len(allc)} | {len(m)} | {len(s)} | {note} |")
