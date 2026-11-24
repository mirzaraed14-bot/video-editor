"""build_plan.py <job dir>  (kit; replaces the 220-line hand-written build_plan.py of batch 9): plan.json from the beats table of <job>/CUT.md.

Reads: CUT.md (K table = spans.py format; '## Files'; '## Beats'), work/seqmap.json (cutchain.sh), work/dump-syn.json (syndump; DUMP=<path> to override), seq.json.
Writes: plan.json (+ work/sfx-events.json). Then: facev3.py plan.json --write, audchain3.sh, mgall3.sh ...   (KIT.md has the order.)

CUT.md grammar (everything not listed is ignored):
  | K3 | 60.96-71.41 | "words"        | keep |          K table rows: before '## Beats'. PLAY rows: | K4 | PLAY theirs file 0.00-9.70 (= OBS 79.09-88.79, ~9.7 s) | ... | ... |
  ## Files                                                  one 'key = value' per line
  theirs = <their Short file>   yt = <our YouTube sample>   ig = <our IG sample, optional>   handle = @Channel   avatar = work/avatar.jpg
  view = <cx>,<cy>,<z>      the ONE static screen view that sits in the top panel (source px centre + zoom; measure it once on a contact sheet)
  ## Beats                                                  | K | layout | menu item | exact copy |      layout = SPLIT | FACE
  | K1 | FACE  | channel_card | Their Channel ; @TheirChannel ; 835K subscribers |
  | K3 | SPLIT | cred_cards   | VIEWS ON *short form*@62.7 ; MY CLIENTS@65.6 ; I TEACH IT@66.96 |    first item = the label (@raw = when the rule draws), then chips
  | K4 | SPLIT | play_card    | theirs |                    (theirs | yt | ig; the K row must be a PLAY row)
  | K5 | SPLIT | side_by_side | theirs:THEIR SHORT ; yt:OUR EDIT |             (optional :still-seconds after the label)
  | K6 | SPLIT | number_card  | 87|THEIR SHORT@100.2 ; 0:43|OUR EDIT@103.0 |  (value = seconds counted up, or text | label @raw)
  | K7 | SPLIT | pointer_mark | THE TITLE@89.3 ; 1700,1240 |        (text@raw ; source px x,y on the view)
  '@raw' = OBS seconds (what tx.txt shows); the plan maps them to sequence seconds through seqmap.
MENU = channel_card, cred_cards, play_card, side_by_side, number_card, pointer_mark (8-12 graphics, nothing else); type sizes live in kindsmenu.py (labels 48-64, main 64-110, never < 40).
"""
import json, os, re, sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"): print(__doc__); raise SystemExit(0)
HERE = os.path.abspath(sys.argv[1]); TOOLS = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, TOOLS)
MENU = {"channel_card": "otn_hook", "cred_cards": "cred_chips", "play_card": "play_card", "side_by_side": "twin_cards", "number_card": "pair_count", "pointer_mark": "pointer_tag"}
r = lambda x: round(x, 3)
snap = lambda t: round(round(t * 60) / 60, 4)
SJ = json.load(open(os.path.join(HERE, "seq.json"), encoding="utf-8")); SEQ = SJ["sequence"]
DUMP = os.environ.get("DUMP") or "work/dump-syn.json"
SM = json.load(open(os.path.join(HERE, "work", "seqmap.json"), encoding="utf-8")); MAP = SM["map"]; PLAY_SEQ = [tuple(x[:2]) for x in SM["sample_seq"]]


def S(raw):
    for a, b, p in MAP:
        if a - 0.02 <= raw < b + 0.02: return p + max(0.0, raw - a)
    for a, b, p in MAP:                       # an anchor in a cut-out gap (a dropped take) lands on the next kept segment's start
        if raw < a: return p
    raise SystemExit(f"raw {raw} is after the end of the cut")


def E(raw):
    for a, b, p in MAP:                       # the kept segment that holds raw (its end may sit up to 0.3 s past the CUT.md span end: word-edge refinement)
        if a - 0.02 <= raw <= b + 0.3: return p + (min(raw, b) - a) if raw < b - 0.06 else p + (b - a)
    prev = [(b, p + b - a) for a, b, p in MAP if b <= raw]
    if prev: return max(prev)[1]
    raise SystemExit(f"no segment ends at raw {raw}")


# ---------- CUT.md ----------
cut = open(os.path.join(HERE, "CUT.md"), encoding="utf-8").read(); sec = None; ktab, files, beats = {}, {}, []
for line in cut.split("\n"):
    if line.startswith("## "): sec = line[3:].strip().lower(); continue
    if sec == "files":
        m = re.match(r"^\s*([a-z_0-9]+)\s*=\s*(.+?)\s*$", line)
        if m: files[m.group(1)] = m.group(2)
        continue
    m = re.match(r"^\| (K\d+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
    if not m: continue
    if sec == "beats": beats.append(m.groups())
    elif sec is None or not sec.startswith("beats"): ktab[m.group(1)] = (m.group(2), m.group(3), m.group(4))
if not beats: raise SystemExit("CUT.md has no '## Beats' rows")
for need in ("view", "handle"):
    if need not in files: raise SystemExit(f"CUT.md ## Files needs '{need} = ...'")
vx, vy, vz = [float(x) for x in files["view"].split(",")]
PROJ_ABS = lambda p: p if re.match(r"^[A-Za-z]:|^/", p) else os.path.join(HERE, p).replace("\\", "/")
FILE = {k: PROJ_ABS(files[k]) for k in ("theirs", "yt", "ig") if k in files}
HANDLE = files["handle"]; AV = files.get("avatar", "work/avatar.jpg")

# K rows -> sequence spans; PLAY rows -> (play index, file key, file start)
plays_k = [k for k in sorted(ktab, key=lambda s: int(s[1:])) if ktab[k][0].startswith("PLAY")]
if len(plays_k) != len(PLAY_SEQ): raise SystemExit(f"{len(plays_k)} PLAY rows in the K table but seqmap has {len(PLAY_SEQ)} sample spans")
PLAYINFO = {}
for i, k in enumerate(plays_k):
    sp = ktab[k][0]; head = sp.lower().split("file")[0].split(); who = head[1] if len(head) > 1 else "theirs"; fk = {"theirs": "theirs", "ours": "yt"}.get(who, who)
    if "ig" in head: fk = "ig"
    m = re.search(r"file\s+([\d.]+)\s*-\s*([\d.]+)", sp)
    PLAYINFO[k] = dict(i=i, seq=PLAY_SEQ[i], fk=fk, src_t0=float(m.group(1)) if m else 0.0)


def span_of(k):
    if k in PLAYINFO: return PLAYINFO[k]["seq"]
    parts = re.findall(r"([\d.]+)-([\d.]+)", ktab[k][0])
    if not parts: raise SystemExit(f"{k}: no span")
    return S(float(parts[0][0])), E(float(parts[-1][1]))


def first_item(copy): return [x.strip() for x in copy.split(";")]


def item_at(x, a0):
    """'text@raw' -> (text, seconds after a0 (the beat start) or None, raw)"""
    m = re.match(r"^(.*?)\s*@\s*([\d.]+)$", x)
    if not m: return x, None, None
    return m.group(1).strip(), r(S(float(m.group(2))) - a0), S(float(m.group(2)))


seq_json = next(s for s in json.load(open(os.path.join(HERE, DUMP), encoding="utf-8")) if s["name"] == SEQ)
END = round(max(c["e"] for c in seq_json["v"][0]["clips"]), 4)
BN = sorted({round(p, 4) for a, b, p in MAP} | {round(p + b - a, 4) for a, b, p in MAP})
F_ = lambda t0, t1, why, scale=132: dict(t0=snap(t0), t1=snap(t1), scale=scale, why=why)
face, graphics, ev = [], [], []
for k, layout, item, copy in beats:
    if item not in MENU: raise SystemExit(f"{k}: menu item '{item}' is not on the MENU {sorted(MENU)}")
    a, b = span_of(k); a0 = 0.0 if a < 0.05 else a; its = first_item(copy); gid = f"{item.replace('_', '-')}-{k.lower()}"
    if layout.strip().upper() == "FACE": face.append(F_(a0, b, f"{k}: {item}"))
    g = dict(id=gid, kind=MENU[item], t0=snap(a0), t1=snap(b))
    if item == "channel_card":
        nm, at, _ = item_at(its[0], a0); g.update(name=nm, handle=its[1] if len(its) > 1 else HANDLE, subs=its[2] if len(its) > 2 else "", avatar=AV, y=1325, sweep_dur=0.35)
        if at is not None: g["sweep_at"] = at
    elif item == "cred_cards":
        lab, at, _ = item_at(its[0], a0); g.update(label=lab, y=1370, chips=[[r(S(raw)), t] for t, _, raw in (item_at(x, a0) for x in its[1:]) if raw is not None] or [])
        if at is not None: g["rule_at"] = at
        if len(g["chips"]) != len(its) - 1: raise SystemExit(f"{k}: every cred chip needs @raw")
    elif item == "play_card":
        if k not in PLAYINFO: raise SystemExit(f"{k}: play_card needs a PLAY row in the K table")
        pi = PLAYINFO[k]; fk = its[0] if its[0] in FILE else pi["fk"]
        g.update(t0=pi["seq"][0], t1=pi["seq"][1], file=FILE[fk], src_t0=pi["src_t0"], handle=HANDLE, muted=True, push=0.0)
        if fk != "theirs": g["tag"] = "OUR EDIT · " + {"yt": "YOUTUBE", "ig": "INSTAGRAM"}.get(fk, fk.upper()) + " LOOK"
    elif item == "side_by_side":
        cards, labels = [], []
        for x in its[:2]:
            fk, lab, *st = x.split(":"); cards.append(dict(file=FILE[fk.strip()], t=float(st[0]) if st else 2.0)); labels.append(lab.strip())
        g.update(cards=cards, labels=labels, cy=650)
    elif item == "number_card":
        A, B = its[0], its[1]; va, la = A.split("|", 1); vb, lb = B.split("|", 1); la, ta, _ = item_at(la, a0); lb, tb, _ = item_at(lb, a0)
        sec_a = float(va) if re.fullmatch(r"[\d.]+", va.strip()) else (lambda m_, s_: int(m_) * 60 + int(s_))(*va.strip().split(":"))
        g.update(a_sec=sec_a, a_label=la, a_at=ta if ta is not None else 0.4, b_text=vb.strip(), b_label=lb, b_at=tb if tb is not None else 1.2, chips=[], y=560)
    elif item == "pointer_mark":
        tx, at, _ = item_at(its[0], a0); x, y = [float(v) for v in its[1].split(",")]; g.update(text=tx, view="main", point=[x, y])
    graphics.append(g)
views_named = {"main": dict(cx=vx, cy=vy, z=vz)}
for g in graphics:
    if g["kind"] == "pointer_tag": g["view"] = "main"
views = [dict(t0=0.0, t1=END, view="main")]
cuts = sorted({f[k] for f in face for k in ("t0", "t1")}); split = []
for v in views:
    a = dict(v)
    for c in cuts:
        if a["t0"] + 1e-6 < c < a["t1"] - 1e-6: split.append(dict(a, t1=c)); a = dict(a, t0=c)
    split.append(a)
views = [dict(v, t0=snap(v["t0"]), t1=snap(v["t1"])) for v in split if v["t1"] - v["t0"] > 1e-6]
for f in face:
    for a, b in PLAY_SEQ:
        if f["t0"] < b - 0.02 and f["t1"] > a + 0.02: raise SystemExit(f"face beat {f['t0']}-{f['t1']} over a play {a}-{b}")

# ---------- safety: edges, overlaps, minimum lengths ----------
EDGES = sorted({f[k] for f in face for k in ("t0", "t1")} | {a for a, b in PLAY_SEQ} | {b for a, b in PLAY_SEQ} | set(BN))


def land(t):
    t = snap(t); e = min(EDGES, key=lambda x: abs(x - t)); return e if abs(e - t) < 0.08 else t


for g in graphics: g["t0"], g["t1"] = land(g["t0"]), land(g["t1"])
graphics.sort(key=lambda g: g["t0"])
for a, b in zip(graphics, graphics[1:]):
    if 0 < b["t0"] - a["t1"] < 0.25: a["t1"] = b["t0"]
for a, b in zip(graphics, graphics[1:]):
    if b["t0"] < a["t1"] - 1e-3: raise SystemExit(f"MG overlap: {a['id']} {a['t0']}-{a['t1']} / {b['id']} {b['t0']}-{b['t1']}")
for g in graphics:
    if g["t1"] - g["t0"] < 0.6 - 1e-6: raise SystemExit(f"graphic too short: {g['id']} {g['t1'] - g['t0']:.2f} s")
if not 8 <= len(graphics) <= 12: print(f"  WARN: {len(graphics)} graphics; the MENU is 8-12")

# ---------- SFX: ONE soft cue per entrance (exits silent); sfxassign3.py picks the sound + peak against the carved bed ----------
SL = json.load(open(os.path.join(HERE, "sfx", "slices.json"), encoding="utf-8")) if os.path.exists(os.path.join(HERE, "sfx", "slices.json")) else {}
DEFAULT = {"otn_hook": ("v3x-card-slide", -18.0), "cred_chips": ("v3x-pop-lid", -19.0), "play_card": ("v3x-card-slide", -18.0), "twin_cards": ("v3x-cloth-soft", -18.0),
           "pair_count": ("v3x-swish-classic", -20.0), "pointer_tag": ("v3x-pop-squeeze", -19.0)}
sfx_events = []
for g in graphics:
    nm, pk = DEFAULT[g["kind"]]; off = min(SL.get(nm, {}).get("offset", 0.18), 0.18)
    g["cues"] = [[r(max(0.0, g["t0"] - off)), nm, round(pk + 1.0, 1)]]; sfx_events.append(dict(gid=g["id"], k=0, t=g["t0"], fam="F1"))
G = {g["id"]: g for g in graphics}
for k, pi in PLAYINFO.items():
    gid = next((g["id"] for g in graphics if g["kind"] == "play_card" and abs(g["t0"] - pi["seq"][0]) < 0.05), None)
    if gid: G[gid]["cues"].append([r(pi["seq"][0]), f"play-v3-p{pi['i'] + 1}", 0.0])      # the play's own audio stem (audio3.py writes sfx/play-v3-<id>.wav)
os.makedirs(os.path.join(HERE, "work"), exist_ok=True)
json.dump(dict(events=sfx_events, fams={"F1": "card slide"}), open(os.path.join(HERE, "work", "sfx-events.json"), "w"), indent=1)

AUD = json.load(open(os.path.join(HERE, "work", "audio.json"), encoding="utf-8")) if os.path.exists(os.path.join(HERE, "work", "audio.json")) else {}
obs = SJ["obs"].replace("\\", "/")
PL = [(f"p{pi['i'] + 1}", pi["seq"], FILE[pi["fk"]], pi["src_t0"]) for pi in sorted(PLAYINFO.values(), key=lambda p: p["i"])]
plan = dict(job=os.path.basename(HERE), sequence=SEQ, dump=DUMP, captions_file="captions-v3.mov", screen_track=0, face_track=1, frame_track=2, mg_track=3, cap_track=4,
            box=[0, 227, 1080, 1038], seam=1038, seam_line=dict(w=4, draw=0.22), entrance="slab", card_style="glass", anim_kps=60, mouth_y=950,
            accent_font="C:/Windows/Fonts/PTSerif-BoldItalic.ttf", sfx_dir="sfx", end=END, views_named=views_named, face=face, views=views, video=[list(p) for p in PLAY_SEQ],
            boxes={}, plays=[dict(id=i, t0=P[0], t1=P[1], file=f, src_t0=s0) for i, P, f, s0 in PL], graphics=graphics, obs_file=obs, obs_audio=obs,
            caption_fixes=[], glue=[], caption_emph=[], voice_gain=AUD.get("voice_gain", 10), voice_gain_ranges=AUD.get("ranges", []), clip_gains=AUD.get("clip_gains", []),
            music=AUD.get("music", {"file": "audio/bed.wav", "source_in": 0.0, "gaps": []}), sfx_gated=bool(AUD))
json.dump(plan, open(os.path.join(HERE, "plan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
try:
    from planlib import seqwords
    n = seqwords(HERE, os.path.join(HERE, DUMP), SEQ)
except Exception as e:      # planlib needs the finished cut's words; a dry run without them still proves the plan
    n = f"skipped ({type(e).__name__})"
fo = sum(f["t1"] - f["t0"] for f in face)
print(f"plan: end {END}, {len(face)} face pieces ({fo:.1f} s), {len(graphics)} MG, {len(graphics)} SFX cues, {len(PLAY_SEQ)} plays; seqwords {n}")
for g in graphics: print(f"  {g['t0']:8.3f} {g['t1']:8.3f} {g['id']:22s} {g['kind']}")
