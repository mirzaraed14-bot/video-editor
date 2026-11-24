"""build_seq3.py: build_seq.py (reactions/tools) for the batch-3 reactions, where one job can have SEVERAL camera files or a STEPPED offset.

  PYTHONUTF8=1 python build_seq3.py <job>/seq.json --import | --create | --place [--clear] [--resume] [--nearest] | --style | --verify

--nearest (2026-10-27, the reel builder's fix_v2.py generalised): Premiere floors a requested camera in-point TWICE (onto the
59.94 fps camera grid, then onto the 60 fps sequence grid), so `f(t) + 1e-4` lands up to ~33 ms early (measured -1..-32 ms on the
batch-5 v1 reactions). --nearest asks for the time r that the double floor turns into the 1/60 grid point NEAREST the sync line
(|error| <= 8.3 ms), for every camera clip; --verify then also prints the in-point error spread.

seq.json: {"sequence", "template", "bin", "obs", "fps": 60,
           "cameras": [{"path": <camera file>, "sync": <sync-dual-audio json> | "offset": <s>, "obs_from": a, "obs_to": b, "obs_shift": s}]}
For an OBS time t in [obs_from, obs_to): camera time = (t - obs_shift) + off(t - obs_shift), off = the line through that sync file's
windows (build_seq.offset_fn) or the constant. obs_shift is for a concatenated OBS file (Moonshots: part 2 starts at 545.516667 of
the concat, and its own sync json is in part-2 time). Why a copy: build_seq.py places ONE camera item with ONE line; Wellness needs
two camera files (C1381, then C1383 after a 54 s hole) and Moonshots needs a step at the concat join. Everything else (--style, the
template clone, batching, the resume rule) is build_seq.py's, imported. A segment that straddles a piece edge or sits in a camera
hole is a hard error (the face panel would go black).
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_seq as B   # noqa: E402

es, PRE = B.es, B.PRE


def pieces(C, job):
    out = []
    for p in C["cameras"]:
        if "sync" in p:
            f, how = B.offset_fn(os.path.join(job, p["sync"]) if not os.path.isabs(p["sync"]) else p["sync"])
        else:
            c = p["offset"]; f, how = (lambda t, c=c: c), f"constant {c:+.4f} s"
        sh = p.get("obs_shift", 0.0)
        out.append(dict(path=p["path"], a=p["obs_from"], b=p["obs_to"], f=(lambda t, f=f, sh=sh: (t - sh) + f(t - sh)), how=how,
                        sub=os.path.splitext(os.path.basename(p["path"]))[0] + " (video only)"))
    return out


CAM_FPS = 60000 / 1001.0


def nearest_in(w, seq_fps=60):
    """the in-point to REQUEST so Premiere's double floor (camera 59.94 grid, then the sequence grid) lands on the sequence-grid
    point nearest w; falls back to w + 1e-4 if no candidate maps exactly"""
    floor2 = lambda r: math.floor(math.floor(r * CAM_FPS + 1e-9) / CAM_FPS * seq_fps + 1e-9) / seq_fps
    best = None
    for k in (-1, 0, 1, 2):
        g = math.floor(w * seq_fps) / seq_fps + k / seq_fps
        r = math.ceil(g * CAM_FPS - 1e-9) / CAM_FPS + 2e-6
        if abs(floor2(r) - g) < 1e-7 and (best is None or abs(g - w) < abs(best[0] - w)): best = (g, r)
    return best[1] if best else w + 1e-4


def piece_at(P, t0, t1):
    for k, p in enumerate(P):
        if p["a"] - 1e-6 <= t0 and t1 <= p["b"] + 1e-6: return k
    raise SystemExit(f"segment {t0:.3f}-{t1:.3f} is not inside ONE camera piece ({[(p['a'], p['b']) for p in P]}): re-cut it")


def main():
    argv = list(sys.argv)
    cfg_path = argv[1]; C = json.load(open(cfg_path, encoding="utf-8")); job = os.path.dirname(os.path.abspath(cfg_path))
    fps = C.get("fps", 60); fr = 1 / fps
    P = pieces(C, job)
    if "--import" in argv:
        for p in P:
            r = es("(function(){" + PRE + f"""
var root = app.project.rootItem, B = findBin(root, {json.dumps(C['bin'])}); if (!B) B = root.createBin({json.dumps(C['bin'])});
var want = [{json.dumps(C['obs'])}, {json.dumps(p['path'])}], got = [];
for (var i = 0; i < want.length; i++){{ var it = byPath(root, want[i]); if (!it){{ app.project.importFiles([want[i]], true, B, false); it = byPath(root, want[i]); }} got.push(it ? it.name : null); }}
var cam = byPath(root, want[1]); if (!cam) return 'NOCAM';
var sc = byName(B, {json.dumps(p['sub'])});
if (!sc){{ var end = cam.getOutPoint(); sc = cam.createSubClip({json.dumps(p['sub'])}, 0, end.seconds, 0, 1, 0); if (sc) sc.moveBin(B); }}
return JSON.stringify({{items: got, subclip: sc ? sc.name : null}}); }})()""")
            print("import:", r)
    if "--create" in argv:
        sys.argv = [sys.argv[0], cfg_path, "--create"]; tmp = dict(C, camera=C["cameras"][0]["path"], sync="")
        json.dump(tmp, open(cfg_path + ".b.json", "w", encoding="utf-8"))
        sys.argv[1] = cfg_path + ".b.json"; B.main(); os.remove(cfg_path + ".b.json")
    if "--place" in argv:
        segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
        for p in P: print(f"camera {p['sub']}: OBS {p['a']}-{p['b']}: {p['how']}")
        rows, pos = [], 0.0
        for s in segs:
            d = round(round((s["end"] - s["start"]) * fps) / fps, 6)
            k = piece_at(P, s["start"], s["start"] + d)
            cin = nearest_in(P[k]["f"](s["start"]), fps) if "--nearest" in argv else P[k]["f"](s["start"]) + 1e-4
            rows.append([round(pos, 6), s["start"] + 1e-4, s["start"] + d + 1e-4, cin, d, k])
            pos += d
        if "--clear" in argv:
            print("clear:", es("(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}); var n = 0;
var T = [S.videoTracks[0], S.videoTracks[1], S.audioTracks[0]];
for (var t = 0; t < T.length; t++) for (var i = T[t].clips.numItems - 1; i >= 0; i--) {{ T[t].clips[i].remove(false, false); n++; }}
return n; }})()"""))
        head = "(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}); if (!S) return 'NOSEQ';
var root = app.project.rootItem, obs = byPath(root, {json.dumps(C['obs'])}), CAM = [{", ".join(f"byName(root, {json.dumps(p['sub'])})" for p in P)}];
for (var q = 0; q < CAM.length; q++) if (!CAM[q]) return 'NOCAM ' + q; if (!obs) return 'NOOBS'; var FR = {fr};"""
        have = es(head + "return S.videoTracks[0].clips.numItems + '/' + S.videoTracks[1].clips.numItems + '/' + S.audioTracks[0].clips.numItems; })()")
        n1, n2, na = (int(x) for x in str(have).split("/"))
        start = 0
        if n1 or n2 or na:
            if n1 == n2 == na and "--resume" in argv and abs(float(es(head + "return S.videoTracks[0].clips[S.videoTracks[0].clips.numItems - 1].end.seconds; })()")) - (rows[n1 - 1][0] + rows[n1 - 1][4])) < 1e-3:
                start = n1; print(f"  resuming after {n1} placed segments")
            else:
                raise SystemExit(f"the sequence is not empty ({have}): --clear first, or --resume")
        for a in range(start, len(rows), 16):
            R = rows[a:a + 16]
            r = es(head + f"""var R = {json.dumps(R)};
for (var k = 0; k < R.length; k++){{ var cam = CAM[R[k][5]];
  obs.setInPoint(R[k][1], 4); obs.setOutPoint(R[k][2], 4); S.videoTracks[0].overwriteClip(obs, R[k][0]);
  cam.setInPoint(R[k][3], 4); cam.setOutPoint(R[k][3] + R[k][4] + FR, 4); S.videoTracks[1].overwriteClip(cam, R[k][0]); }}
obs.clearInPoint(4); obs.clearOutPoint(4); for (var q = 0; q < CAM.length; q++){{ CAM[q].clearInPoint(4); CAM[q].clearOutPoint(4); }}
return S.videoTracks[0].clips.numItems + '/' + S.videoTracks[1].clips.numItems; }})()""")
            print(f"  segments {a}-{a + len(R) - 1}: V1/V2 {r}")
        r = es(head + """var v2 = S.videoTracks[1], last = v2.clips[v2.clips.numItems - 1], v1 = S.videoTracks[0], endV1 = v1.clips[v1.clips.numItems - 1].end;
if (last.end.seconds > endV1.seconds + 1e-4) last.end = endV1;
var na = []; for (var t = 0; t < S.audioTracks.numTracks; t++) na.push(S.audioTracks[t].clips.numItems);
return JSON.stringify({v1: v1.clips.numItems, v2: v2.clips.numItems, a: na, end: endV1.seconds}); })()""")
        print("place:", r, f"(expected {len(segs)} segments, {pos:.3f} s)")
    if "--style" in argv:
        tmp = dict(C, camera=C["cameras"][0]["path"], sync="")
        json.dump(tmp, open(cfg_path + ".b.json", "w", encoding="utf-8"))
        sys.argv = [sys.argv[0], cfg_path + ".b.json", "--style"]; B.main(); os.remove(cfg_path + ".b.json")
    if "--verify" in argv:
        segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
        d = es("(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}); var o = [];
for (var t = 0; t < 2; t++){{ var tr = S.videoTracks[t], c = []; for (var i = 0; i < tr.clips.numItems; i++){{ var x = tr.clips[i]; c.push([x.start.seconds, x.end.seconds, x.inPoint.seconds, x.projectItem ? x.projectItem.name : '']); }} o.push(c); }}
var a = S.audioTracks[0], ac = []; for (var i = 0; i < a.clips.numItems; i++){{ var x = a.clips[i]; ac.push([x.start.seconds, x.end.seconds, x.inPoint.seconds]); }} o.push(ac);
return JSON.stringify(o); }})()""")
        v1, v2, a1 = json.loads(d) if isinstance(d, str) else d
        bad = []; errs = []
        if len(v1) != len(segs) or len(a1) != len(segs): bad.append(f"count V1 {len(v1)} A1 {len(a1)} vs {len(segs)}")
        for k, (s, c) in enumerate(zip(segs, v1)):
            if abs(c[2] - s["start"]) > 0.6 * fr: bad.append(f"V1 seg {k}: in {c[2]:.4f} vs {s['start']:.4f}")
        gaps = [(round(a[1], 4), round(b[0], 4)) for a, b in zip(v2, v2[1:]) if b[0] - a[1] > 1e-3]
        if gaps: bad.append(f"V2 gaps {gaps[:5]}")
        if abs(v2[0][0]) > 1e-3 or abs(v2[-1][1] - v1[-1][1]) > 1e-3: bad.append(f"V2 span {v2[0][0]:.3f}-{v2[-1][1]:.3f} vs V1 end {v1[-1][1]:.3f}")
        for c in v2:
            k = max(i for i, x in enumerate(v1) if x[0] <= c[0] + 1e-4); x = v1[k]
            t = x[2] + (c[0] - x[0]); q = piece_at(P, t, t)
            want = P[q]["f"](t)
            if not c[3].startswith(P[q]["sub"].split(" (")[0]): bad.append(f"V2 @{c[0]:.3f}: item {c[3]} vs {P[q]['sub']}")
            if abs(c[2] - want) > 0.035: bad.append(f"V2 @{c[0]:.3f}: cam in {c[2]:.4f} vs {want:.4f}")
            errs.append((c[2] - want) * 1000)
        if errs: print(f"camera in-point vs the sync line: {min(errs):+.1f} .. {max(errs):+.1f} ms over {len(errs)} clips (median {sorted(errs)[len(errs) // 2]:+.1f})")
        print("verify:", "OK" if not bad else "PROBLEMS"); [print("  ", b) for b in bad[:20]]


if __name__ == "__main__":
    main()
