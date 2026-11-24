"""syndump.py <job>: the sequence dump (dump.py format) that build_seq3.py --place --style --nearest WILL produce, computed OFFLINE from
transcript/cuts.json + seq.json, so the whole plan, the captions and every graphic can be built before the Premiere lock is taken (R3,
batch-6 v2). After the real placement, `syndump.py <job> --compare work/dump-real.json` proves the real sequence equals it (clip edges,
in-points, end) before anything is laid on top. Writes work/dump-raw.json (+ a copy work/dump-syn.json)."""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_seq3 as B3   # noqa: E402
job = sys.argv[1]; C = json.load(open(os.path.join(job, "seq.json"), encoding="utf-8")); fps = C.get("fps", 60)
P = B3.pieces(C, job)
segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
M1 = {"Position": [0.42962962388992, 0.2890625], "Scale": 71, "Crop Left": 0, "Crop Top": 0, "Crop Right": 0, "Crop Bottom": 0, "fx": "Opacity|Motion"}
M2 = {"Position": [0.5, 0.72343748807907], "Scale": 65, "Crop Left": 0, "Crop Top": 0, "Crop Right": 0, "Crop Bottom": 0, "fx": "Opacity|Motion"}
CAM = 60000 / 1001.0
floor2 = lambda r: math.floor(math.floor(r * CAM + 1e-9) / CAM * fps + 1e-9) / fps
v1, v2, a1, pos = [], [], [], 0.0
for s in segs:
    d = round(round((s["end"] - s["start"]) * fps) / fps, 6)
    k = B3.piece_at(P, s["start"], s["start"] + d)
    cin = floor2(B3.nearest_in(P[k]["f"](s["start"]), fps))
    i1 = math.floor((s["start"] + 1e-4) * fps + 1e-9) / fps
    v1.append(dict(n=os.path.basename(C["obs"]), s=round(pos, 6), e=round(pos + d, 6), i=i1, o=i1 + d, p=C["obs"], d=0, m=M1))
    v2.append(dict(n=P[k]["sub"], s=round(pos, 6), e=round(pos + d, 6), i=cin, o=cin + d, p=P[k]["path"], d=0, m=M2))
    a1.append(dict(n=os.path.basename(C["obs"]), s=round(pos, 6), e=round(pos + d, 6), i=i1))
    pos += d
dump = [dict(name=C["sequence"], w=1080, h=1920, fps=fps, end=round(pos, 6), v=[dict(t=0, muted=False, clips=v1), dict(t=1, muted=False, clips=v2), dict(t=2, muted=False, clips=[])],
             a=[dict(t=0, clips=a1)] + [dict(t=k, clips=[]) for k in (1, 2, 3)])]
if "--compare" in sys.argv:
    R = next(s for s in json.load(open(sys.argv[sys.argv.index("--compare") + 1], encoding="utf-8")) if s["name"] == C["sequence"])
    bad = []
    if abs(R["end"] - pos) > 1 / fps / 2: bad.append(f"end {R['end']:.4f} vs {pos:.4f}")
    for t in (0, 1):
        r, s_ = R["v"][t]["clips"], dump[0]["v"][t]["clips"]
        if len(r) != len(s_): bad.append(f"V{t + 1} count {len(r)} vs {len(s_)}"); continue
        for x, y in zip(r, s_):
            for key in ("s", "e", "i"):
                if abs(x[key] - y[key]) > 0.6 / fps: bad.append(f"V{t + 1} @{y['s']:.3f} {key} {x[key]:.4f} vs {y[key]:.4f}")
    print("compare:", "IDENTICAL (within half a frame)" if not bad else f"{len(bad)} DIFFS"); [print("  ", b) for b in bad[:20]]
    sys.exit(1 if bad else 0)
for name in ("dump-raw.json", "dump-syn.json"):
    json.dump(dump, open(os.path.join(job, "work", name), "w", encoding="utf-8"), indent=1)
print(f"syndump: {len(segs)} segments, end {pos:.4f} s; cameras: " + "; ".join(f"{p['sub']} OBS {p['a']}-{p['b']} {p['how']}" for p in P))
