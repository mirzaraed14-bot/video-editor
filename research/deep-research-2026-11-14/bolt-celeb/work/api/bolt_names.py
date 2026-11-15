import json
import re
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")
rows = json.load(open(sys.argv[1], encoding="utf-8"))
NAMES = [
    "michael jackson", "jackson", "bieber", "ronaldo", "messi", "mrbeast", "mr beast", "speed", "ishowspeed", "ali ",
    "muhammad", "eminem", "drake", "taylor swift", "the rock", "dwayne", "will smith", "kobe", "lebron", "jordan",
    "elon", "musk", "gaga", "tony bennett", "celine", "adele", "beyonce", "rihanna", "kanye", "tom holland",
    "tom cruise", "brad pitt", "dicaprio", "leonardo", "johnny depp", "jackie chan", "bruce lee", "arnold",
    "schwarzenegger", "stallone", "jim carrey", "robin williams", "morgan freeman", "denzel", "oprah", "ellen",
    "fallon", "kevin hart", "shaq", "tiger woods", "federer", "nadal", "djokovic", "ronaldinho", "neymar",
    "mbappe", "haaland", "usain", "phelps", "biles", "serena", "tyson", "mcgregor", "khabib", "cena",
    "undertaker", "keanu", "harvey specter", "gabriel macht", "henry cavill", "ryan reynolds", "zendaya",
    "billie eilish", "ed sheeran", "justin timberlake", "snoop", "50 cent", "tupac", "biggie", "jay-z",
    "steve jobs", "bill gates", "zuckerberg", "obama", "trump", "manning", "brady", "mahomes", "kelce",
    "steph curry", "curry", "kai cenat", "pewdiepie", "markiplier", "jimmy", "chris pratt", "hemsworth",
    "robert downey", "rdj", "scarlett", "margot", "pedro pascal", "kardashian", "selena", "ariana",
    "post malone", "travis scott", "lil wayne", "weeknd", "bad bunny", "shakira", "jennifer lopez",
    "jlo", "pharrell", "stevie wonder", "elvis", "prince", "whitney", "amy winehouse", "freddie mercury",
    "john lennon", "beatles", "paul mccartney", "mick jagger", "bon jovi", "ozzy", "dolly", "garth",
    "pitbull", "conor", "floyd", "mayweather", "pacquiao", "canelo", "jake paul", "logan paul", "ksi",
    "beckham", "zidane", "pele", "maradona", "kroos", "modric", "salah", "kane", "rooney", "pogba",
    "chris rock", "dave chappelle", "jerry seinfeld", "conan", "letterman", "kimmel", "simon cowell",
    "gordon ramsay", "ramsay", "nick walker", "cbum", "chris bumstead", "arnold", "ronnie coleman",
]
def text(r):
    return (r["title"] + " " + r.get("desc", "") + " " + " ".join(r.get("tags", []))).lower()

for r in rows:
    t = text(r)
    r["hits"] = sorted({n.strip() for n in NAMES if n in t})

vs = [r["views"] for r in rows if r["views"] is not None]
print("all uploads %d, median %s, mean %s" % (len(vs), "{:,}".format(int(statistics.median(vs))), "{:,}".format(int(statistics.mean(vs)))))
for yr in ("2023", "2024", "2025", "2026"):
    v = [r["views"] for r in rows if r["published"].startswith(yr) and r["views"] is not None]
    if v:
        print("  %s: n %d, median %s, p75 %s, max %s" % (yr, len(v), "{:,}".format(int(statistics.median(v))),
              "{:,}".format(int(sorted(v)[int(len(v) * .75)])), "{:,}".format(max(v))))
last = sorted(rows, key=lambda r: r["published"], reverse=True)[:60]
v = [r["views"] for r in last if r["views"] is not None]
print("latest 60 uploads (%s to %s): median %s" % (last[-1]["published"], last[0]["published"], "{:,}".format(int(statistics.median(v)))))
print()
celeb = [r for r in rows if r["hits"]]
print("uploads naming a famous person (title/desc/tags): %d" % len(celeb))
cv = [r["views"] for r in celeb if r["views"] is not None]
nv = [r["views"] for r in rows if not r["hits"] and r["views"] is not None]
print("  median celeb %s vs others %s" % ("{:,}".format(int(statistics.median(cv))), "{:,}".format(int(statistics.median(nv)))))
print()
mode = sys.argv[2] if len(sys.argv) > 2 else "celeb"
if mode == "celeb":
    for r in sorted(celeb, key=lambda r: -(r["views"] or 0))[:70]:
        print("%s | %s | %ss | %s | %s | %s" % (r["id"], r["published"], r["seconds"], "{:,}".format(r["views"]),
              ",".join(r["hits"])[:40], r["title"][:70]))
elif mode == "grep":
    pat = re.compile(sys.argv[3], re.I)
    for r in sorted(rows, key=lambda r: -(r["views"] or 0)):
        if pat.search(text(r)):
            print("%s | %s | %ss | %s | %s | %s" % (r["id"], r["published"], r["seconds"], "{:,}".format(r["views"]),
                  r["title"][:80], (r.get("desc", "")[:160]).replace("\n", " ")))

# --- The named-vs-hidden split quoted in the report (added 23:40 PKT so the figure can be reproduced) ---
# Run: python -I bolt_names.py bolt_uploads.json split
if mode == "split":
    def in_title(r):
        t = r["title"].lower()
        return any(n in t for n in NAMES)
    for label, pick in (("all-time", lambda r: True), ("2026", lambda r: r["published"].startswith("2026"))):
        named = [r["views"] for r in celeb if pick(r) and in_title(r)]
        hidden = [r["views"] for r in celeb if pick(r) and not in_title(r)]
        print("%s: name in title n %d median %s | name only in desc/tags n %d median %s" % (
            label, len(named), "{:,}".format(int(statistics.median(named))),
            len(hidden), "{:,}".format(int(statistics.median(hidden)))))
