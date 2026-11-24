import sys, json, os, subprocess, concurrent.futures as cf
# usage: thumbs.py sel.json  -> curls thumb (480w via PIL later) into thumbs/<ch>-<id>.jpg
sel = json.load(open(sys.argv[1], encoding="utf-8"))
os.makedirs("thumbs", exist_ok=True)
def get(r):
    p = f"thumbs/{r['ch']}-{r['id']}.jpg"
    if os.path.exists(p) and os.path.getsize(p) > 2000: return 0
    if not r.get("thumb"): return 1
    u = r["thumb"].replace("1920x1080", "640x360") if "1920x1080" in r["thumb"] else r["thumb"]
    rc = subprocess.run(["curl", "-s", "-f", "-m", "25", "-o", p, u]).returncode
    if rc != 0 or not os.path.exists(p):
        rc = subprocess.run(["curl", "-s", "-f", "-m", "25", "-o", p, r["thumb"]]).returncode
    return rc
with cf.ThreadPoolExecutor(6) as ex:
    res = list(ex.map(get, sel["rows"]))
print("ok", res.count(0), "fail", len(res) - res.count(0))
