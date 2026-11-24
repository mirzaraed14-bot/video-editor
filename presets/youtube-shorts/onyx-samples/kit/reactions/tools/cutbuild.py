"""cutbuild.py <job> (kit; from HPP batch 9): the EDL straight from keep.json + words.json + the 10 ms envelope (replaces polish/tight6/cutv3 for a FRESH cut).
Per talk row: words in the row (KILL = fillers dropped inside a row) are grouped into spans; a gap <= 0.21 s (or inside PROTECT, a counted number) stays continuous; a bigger gap becomes ONE joint that
keeps a 0.20 s pause (the cutv3 relax rule: 0.07 + 2x, x <= 0.065, reduced while loud frames sit in the way). Row edges: first loud frame - 0.03 / last loud frame + 0.04 (tight6), never
into the neighbouring raw word. Plays (kind S) are pinned. Writes %LOCALAPPDATA%/Temp/video-editor/<job>/cuts.json (all no_refine) for RENDER=0 splice.sh and work/cutbuild.json (joint list)."""
import json, os, subprocess, sys
import numpy as np
job = sys.argv[1].rstrip("/"); TH = float(os.environ.get("TH", "-47.1")); PAUSE = 0.20; NAT = 0.25
K = json.load(open(f"{job}/keep.json", encoding="utf-8")); ws = json.load(open(f"{job}/transcript/words.json", encoding="utf-8"))["clips"][0]["words"]
envp = f"{job}/work/env10.npy"
if os.path.exists(envp): e = np.load(envp)
else:
    raw = os.path.join(job, "raw", K["clip"]); SR = 16000
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", raw, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(float)
    h = SR // 100; n = len(x) // h; e = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9); np.save(envp, e)
g60 = lambda t: round(round(t * 60) / 60, 4)
fr = lambda t: int(round(t * 100))
import re as _re
KILL = {i for i, w in enumerate(ws) if _re.fullmatch(r"(uh+|um+|umm+|erm?|ah+|hmm+|mm+)[,.?!]*", w["w"].lower())}   # fillers: always dropped inside a row (a held tail of a word is NOT a filler token)
KILL |= {int(x) for x in os.environ.get("KILL_EXTRA", "").split(",") if x.strip()}
EDGE = json.load(open(f"{job}/work/edge-overrides.json", encoding="utf-8")) if os.path.exists(f"{job}/work/edge-overrides.json") else {}   # {"s:<word idx>": t, "e:<word idx>": t}
prot = set()
for i, w in enumerate(ws):
    if _re.fullmatch(r"[\d.,]+", w["w"].strip(",.")) and i + 1 < len(ws) and ws[i + 1]["w"].lower().strip(",.") .startswith(("million", "billion", "thousand", "percent", "k")): prot.add(i)   # a counted number stays continuous
def loud_first(a, b):          # first frame of a run of >= 2 loud frames (a lone click is not speech; the clash test below still sees it)
    for i in range(fr(a), fr(b)):
        if e[i] > TH and e[i + 1] > TH: return i / 100
    return None
def loud_last(a, b):
    for i in range(fr(b) - 1, fr(a) - 1, -1):
        if e[i] > TH and e[i - 1] > TH: return (i + 1) / 100
    return None
segs, joints, rows = [], [], []
for ent in K["keep"]:
    if ent[0] == "t":
        _, a, b, kind, note = ent; segs.append(dict(clip=K["clip"], start=round(a, 4), end=round(b, 4), transcript=note, kind="S", no_refine=True)); continue
    i0, i1, kind, note = ent; idx = [i for i in range(i0, i1 + 1) if i not in KILL]
    def probe(ga, gb):
        """-> (la, lb, x) the loud extents either side of the pause and the half-widening that keeps a 0.20 s pause, or None when the pause is natural (<= 0.21 s between loud extents) or has no quiet frames"""
        wa, wb = ws[ga[-1]], ws[gb[0]]
        if gb[0] - ga[-1] > 1:                 # a killed word (filler) sits between: always a joint, edges kept clear of it
            k0, k1 = ws[ga[-1] + 1]["start"], ws[gb[0] - 1]["end"]
            la = loud_last(wa["end"] - 0.12, k0 - 0.005) or wa["end"]; lb = loud_first(k1 + 0.005, wb["start"] + 0.12) or wb["start"]
            return la, lb, 0.02
        la = loud_last(wa["end"] - 0.12, min(wa["end"] + 0.30, wb["start"] - 0.02)) or wa["end"]
        lb = loud_first(max(wb["start"] - 0.40, wa["end"] + 0.02, la + 0.05), wb["start"] + 0.12) or wb["start"]
        if lb - la <= NAT + 1e-9: return None
        x = (PAUSE - 0.07) / 2
        def clash(x):
            a_end, b_st = la + 0.04 + x, lb - 0.03 - x
            return a_end >= b_st or any(e[i] > TH and e[i + 1] > TH for i in range(fr(la), fr(a_end))) or any(e[i] > TH and e[i + 1] > TH for i in range(fr(b_st), fr(lb)))
        while x > 0.0 and clash(x): x -= 0.005
        if 0.07 + 2 * x < 0.15: return None
        return la, lb, max(x, 0.0)
    groups = [[idx[0]]]
    for a_, b_ in zip(idx, idx[1:]):
        if a_ in prot: groups[-1].append(b_); continue
        groups.append([b_])
    gi = 0
    while gi < len(groups) - 1:
        if probe(groups[gi], groups[gi + 1]) is None: groups[gi] += groups.pop(gi + 1)
        else: gi += 1
    def nat(ga, gb):
        wa, wb = ws[ga[-1]], ws[gb[0]]; la = loud_last(wa["end"] - 0.12, min(wa["end"] + 0.30, wb["start"] - 0.02)) or wa["end"]
        return (loud_first(max(wb["start"] - 0.40, wa["end"] + 0.02, la + 0.05), wb["start"] + 0.12) or wb["start"]) - la
    gi = 0
    while len(groups) > 1 and gi < len(groups):      # staccato guard: a piece shorter than 0.22 s joins the neighbour with the SHORTER natural pause (<= 0.6 s), never across a killed filler
        dur = ws[groups[gi][-1]]["end"] - ws[groups[gi][0]]["start"]
        if dur < 0.80:
            cand = []
            if gi > 0 and groups[gi][0] - groups[gi - 1][-1] == 1: cand.append((nat(groups[gi - 1], groups[gi]), -1))
            if gi + 1 < len(groups) and groups[gi + 1][0] - groups[gi][-1] == 1: cand.append((nat(groups[gi], groups[gi + 1]), 1))
            cand = [c for c in cand if c[0] <= 0.30]
            if cand:
                _, d_ = min(cand)
                if d_ < 0: groups[gi - 1] += groups.pop(gi)
                else: groups[gi] += groups.pop(gi + 1)
                continue
        gi += 1
    out = []
    for gi, gr in enumerate(groups):
        fa, fb = ws[gr[0]], ws[gr[-1]]
        if gi == 0:
            prev_end = ws[gr[0] - 1]["end"] if gr[0] > 0 else 0.0
            lf = loud_first(max(fa["start"] - 0.10, prev_end), fa["start"] + 0.12) or fa["start"]
            st = max(lf - 0.03, prev_end + 0.005)
        else: st = None
        if gi == len(groups) - 1:
            nxt_start = ws[gr[-1] + 1]["start"] if gr[-1] + 1 < len(ws) else fb["end"] + 1.0
            ll = loud_last(fb["end"] - 0.12, min(fb["end"] + 0.10, nxt_start)) or fb["end"]
            en = min(ll + 0.04, nxt_start - 0.005)
        else: en = None
        out.append([st, en, gr])
    for gi in range(len(groups) - 1):
        la, lb, x = probe(groups[gi], groups[gi + 1]); wa, wb = ws[groups[gi][-1]], ws[groups[gi + 1][0]]
        out[gi][1] = la + 0.04 + x; out[gi + 1][0] = lb - 0.03 - x
        joints.append(dict(after=wa["w"], before=wb["w"], at=round(wa["end"], 2), gap=round(wb["start"] - wa["end"], 2), kept=round(0.07 + 2 * x, 3), x=round(x, 3)))
    for st, en, gr in out:
        a, b = ws[gr[0]], ws[gr[-1]]
        for k_, v_ in EDGE.items():            # "s@<word start>" / "e@<word end>": the override of the span that starts on / ends on that word
            if k_.startswith("s@") and abs(a["start"] - float(k_[2:])) < 0.01: st = v_
            if k_.startswith("e@") and abs(b["end"] - float(k_[2:])) < 0.01: en = v_
        st = EDGE.get(f"s:{gr[0]}", st); en = EDGE.get(f"e:{gr[-1]}", en)
        segs.append(dict(clip=K["clip"], start=g60(st), end=g60(en), transcript=" ".join(ws[i]["w"] for i in gr), kind="A", no_refine=True))
    rows.append(note[:3])
SPL = json.load(open(f"{job}/work/splits.json")) if os.path.exists(f"{job}/work/splits.json") else []      # R9: a repeat inside a span ("it's it's"): cut [a, b] out of the segment that holds it (raw seconds, both inside quiet frames)
for a_, b_ in SPL:
    k_ = next(i for i, s in enumerate(segs) if s["start"] < a_ and s["end"] > b_)
    s0 = segs[k_]; w_ = s0["transcript"].split(" ")
    segs[k_:k_ + 1] = [dict(s0, end=g60(a_), transcript=" ".join(w_[:max(1, len(w_) // 2)])), dict(s0, start=g60(b_), transcript=" ".join(w_[max(1, len(w_) // 2):]))]
    joints.append(dict(after="(repeat cut)", before="", at=a_, gap=round(b_ - a_, 2), kept=round(b_ - a_, 2), x=0))
for s in segs:
    if s["end"] - s["start"] < 0.06: raise SystemExit(f"tiny segment {s}")
for p, q in zip(segs, segs[1:]):
    if q["start"] > p["start"] and q["start"] < p["end"] - 1e-6: raise SystemExit(f"overlap {p['start']}-{p['end']} / {q['start']}-{q['end']}")
tmp = os.path.join(os.environ["LOCALAPPDATA"], "Temp", "video-editor", os.path.basename(os.path.abspath(job))); os.makedirs(tmp, exist_ok=True)
for f in ("cuts.refined.json", "cuts.snapped.json"):
    if os.path.exists(os.path.join(tmp, f)): os.remove(os.path.join(tmp, f))
json.dump(dict(segments=[{k: v for k, v in s.items() if k in ("clip", "start", "end", "transcript", "no_refine")} for s in segs]), open(os.path.join(tmp, "cuts.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(dict(segments=[dict(s) for s in segs]), open(f"{job}/transcript/cuts.draft.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(dict(joints=joints), open(f"{job}/work/cutbuild.json", "w", encoding="utf-8"), indent=1)
tot = sum(s["end"] - s["start"] for s in segs)
print(f"{len(segs)} segments ({sum(1 for s in segs if s['kind']=='S')} plays), {len(joints)} internal joints, raw sum {tot:.2f} s -> {tmp}/cuts.json")
for j in joints: print(f"  joint after '{j['after']}' @{j['at']} gap {j['gap']} -> kept {j['kept']} (x {j['x']})")
