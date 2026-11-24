"""build_seq.py: build a reaction sequence in ABW8 from Affan's RAW recordings (batch 2: no rough cut handed over).

  PYTHONUTF8=1 python build_seq.py <job>/seq.json --import      # OBS + camera into the bin (skipped if already there) + a video-only camera subclip
  PYTHONUTF8=1 python build_seq.py <job>/seq.json --create      # a new 1080x1920 sequence cloned from an EMPTY template sequence of his, renamed
  PYTHONUTF8=1 python build_seq.py <job>/seq.json --place [--clear]   # the rough cut (transcript/cuts.json) onto V1+A1 (OBS) and V2 (camera, synced)
  PYTHONUTF8=1 python build_seq.py <job>/seq.json --style       # his split layout on every clip: screen Scale 71 at (0.4296, 0.2891), face 65 at (0.5, 0.7234)
  PYTHONUTF8=1 python build_seq.py <job>/seq.json --verify

seq.json: {"sequence": "<new name>", "template": "Sequence 48", "bin": "<bin name>", "obs": "<path>", "camera": "<path>",
           "sync": "<sync-dual-audio --json-out>", "fps": 60}
Camera time = OBS time + offset(t): the line through sync-dual-audio's per-window offsets (clock drift), evaluated per segment.
Each camera piece is placed 1 frame long so the next overwrite trims it (never a 1-frame gap where the screen shows through);
the last one is trimmed to V1's end. Everything is DOM work on a sequence that is never activated.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pp import es as _es  # noqa: E402


def es(js, timeout=170):
    d, err = _es(js, timeout)
    if err: raise SystemExit(f"ES error: {str(err)[:600]}")
    return d


PRE = r"""
function seqByName(n){ for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === n) return app.project.sequences[i]; return null; }
function findBin(p, n){ for (var i = 0; i < p.children.numItems; i++){ var c = p.children[i]; if (c.type === ProjectItemType.BIN && c.name === n) return c; } return null; }
function byPath(p, path){ for (var i = 0; i < p.children.numItems; i++){ var c = p.children[i];
  if (c.type === ProjectItemType.BIN){ var f = byPath(c, path); if (f) return f; }
  else { try { if (c.getMediaPath() === path && !c.isSequence()) return c; } catch(e){} } } return null; }
function byName(p, n){ for (var i = 0; i < p.children.numItems; i++){ var c = p.children[i]; if (c.name === n) return c;
  if (c.type === ProjectItemType.BIN){ var f = byName(c, n); if (f) return f; } } return null; }
"""


def offset_fn(sync):
    d = json.load(open(sync, encoding="utf-8"))
    w = d.get("windows") or []
    good = [x for x in w if x.get("peak", 99) >= 10] if sum(x.get("peak", 99) >= 10 for x in w) >= 3 else w   # a weak window (peak < 10x the
    pts = [(x["centre_s"] - x["offset_s"], x["offset_s"]) for x in good]    # noise) is an outlier: C1349's first one sat 40 ms off the other three
    # window centres are CAMERA time; the line runs in OBS time
    if len(pts) >= 2:
        n = len(pts); mx = sum(p[0] for p in pts) / n; my = sum(p[1] for p in pts) / n
        b = sum((p[0] - mx) * (p[1] - my) for p in pts) / sum((p[0] - mx) ** 2 for p in pts)
        return lambda t: my + b * (t - mx), f"line through {n} windows: {my:+.4f} s at {mx:.0f} s, {b * 1e6:+.1f} ppm"
    off = d["offset_s"]
    return lambda t: off, f"constant {off:+.4f} s"


def main():
    cfg_path = sys.argv[1]; C = json.load(open(cfg_path, encoding="utf-8")); job = os.path.dirname(os.path.abspath(cfg_path))
    fps = C.get("fps", 60); fr = 1 / fps
    sub = os.path.splitext(os.path.basename(C["camera"]))[0] + " (video only)"
    if "--import" in sys.argv:
        r = es("(function(){" + PRE + f"""
var root = app.project.rootItem, B = findBin(root, {json.dumps(C['bin'])}); if (!B) B = root.createBin({json.dumps(C['bin'])});
var want = [{json.dumps(C['obs'])}, {json.dumps(C['camera'])}], got = [];
for (var i = 0; i < want.length; i++){{ var it = byPath(root, want[i]); if (!it){{ app.project.importFiles([want[i]], true, B, false); it = byPath(root, want[i]); }} got.push(it ? it.name : null); }}
var cam = byPath(root, want[1]); if (!cam) return 'NOCAM';
var sc = byName(B, {json.dumps(sub)});
if (!sc){{ var end = cam.getOutPoint(); sc = cam.createSubClip({json.dumps(sub)}, 0, end.seconds, 0, 1, 0); if (sc) sc.moveBin(B); }}
return JSON.stringify({{items: got, subclip: sc ? sc.name : null}}); }})()""")
        print("import:", r)
    if "--create" in sys.argv:
        r = es("(function(){" + PRE + f"""
if (seqByName({json.dumps(C['sequence'])})) return 'EXISTS';
var T = seqByName({json.dumps(C['template'])}); if (!T) return 'NOTEMPLATE';
var n = 0; for (var t = 0; t < T.videoTracks.numTracks; t++) n += T.videoTracks[t].clips.numItems;
for (var t = 0; t < T.audioTracks.numTracks; t++) n += T.audioTracks[t].clips.numItems;
if (n) return 'TEMPLATE NOT EMPTY (' + n + ' clips)';
var before = {{}}; for (var i = 0; i < app.project.sequences.numSequences; i++) before[app.project.sequences[i].sequenceID] = 1;
var ok = T.clone(); var S = null;
for (var i = 0; i < app.project.sequences.numSequences; i++) if (!before[app.project.sequences[i].sequenceID]) S = app.project.sequences[i];
if (!S) return 'CLONE FAILED ' + ok;
S.name = {json.dumps(C['sequence'])};
var B = findBin(app.project.rootItem, {json.dumps(C['bin'])}); if (B && S.projectItem) S.projectItem.moveBin(B);
var st = S.getSettings();
return JSON.stringify({{name: S.name, w: st.videoFrameWidth, h: st.videoFrameHeight, fps: 1 / st.videoFrameRate.seconds, v: S.videoTracks.numTracks, a: S.audioTracks.numTracks}}); }})()""")
        print("create:", r)
    if "--place" in sys.argv:
        segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
        off, how = offset_fn(C["sync"]); print("sync:", how)
        rows, pos = [], 0.0
        for s in segs:
            d = round(round((s["end"] - s["start"]) * fps) / fps, 6)
            rows.append([round(pos, 6), s["start"] + 1e-4, s["start"] + d + 1e-4, s["start"] + off(s["start"]) + 1e-4, d])
            pos += d
        if "--clear" in sys.argv:                    # wipe OUR placement (V1, V2, A1) before a re-place; never his sequences (the name is ours)
            print("clear:", es("(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}); var n = 0;
var T = [S.videoTracks[0], S.videoTracks[1], S.audioTracks[0]];
for (var t = 0; t < T.length; t++) for (var i = T[t].clips.numItems - 1; i >= 0; i--) {{ T[t].clips[i].remove(false, false); n++; }}
return n; }})()"""))
        head = "(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}); if (!S) return 'NOSEQ';
var root = app.project.rootItem, obs = byPath(root, {json.dumps(C['obs'])}), cam = byName(root, {json.dumps(sub)});
if (!obs || !cam) return 'NOITEM ' + !!obs + ' ' + !!cam; var FR = {fr};"""
        have = es(head + "return S.videoTracks[0].clips.numItems + '/' + S.videoTracks[1].clips.numItems + '/' + S.audioTracks[0].clips.numItems; })()")
        n1, n2, na = (int(x) for x in str(have).split("/"))
        start = 0
        if n1 or n2 or na:                           # a batch that died with the bridge: resume ONLY if what is there is exactly
            if n1 == n2 == na and "--resume" in sys.argv and abs(float(es(head + "return S.videoTracks[0].clips[S.videoTracks[0].clips.numItems - 1].end.seconds; })()")) - (rows[n1 - 1][0] + rows[n1 - 1][4])) < 1e-3:
                start = n1; print(f"  resuming after {n1} placed segments")     # the first n1 segments, end to end
            else:
                raise SystemExit(f"the sequence is not empty ({have}): --clear first, or --resume")
        for a in range(start, len(rows), 16):        # batched: one 104-segment call outlived the bridge's reply window (2026-10-12)
            R = rows[a:a + 16]
            r = es(head + f"""var R = {json.dumps(R)};
for (var k = 0; k < R.length; k++){{
  obs.setInPoint(R[k][1], 4); obs.setOutPoint(R[k][2], 4); S.videoTracks[0].overwriteClip(obs, R[k][0]);
  cam.setInPoint(R[k][3], 4); cam.setOutPoint(R[k][3] + R[k][4] + FR, 4); S.videoTracks[1].overwriteClip(cam, R[k][0]); }}
obs.clearInPoint(4); obs.clearOutPoint(4); cam.clearInPoint(4); cam.clearOutPoint(4);
return S.videoTracks[0].clips.numItems + '/' + S.videoTracks[1].clips.numItems; }})()""")
            print(f"  segments {a}-{a + len(R) - 1}: V1/V2 {r}")
        r = es(head + """var v2 = S.videoTracks[1], last = v2.clips[v2.clips.numItems - 1], v1 = S.videoTracks[0], endV1 = v1.clips[v1.clips.numItems - 1].end;
if (last.end.seconds > endV1.seconds + 1e-4) last.end = endV1;
var na = []; for (var t = 0; t < S.audioTracks.numTracks; t++) na.push(S.audioTracks[t].clips.numItems);
return JSON.stringify({v1: v1.clips.numItems, v2: v2.clips.numItems, a: na, end: endV1.seconds}); })()""")
        print("place:", r, f"(expected {len(segs)} segments, {pos:.3f} s)")
    if "--style" in sys.argv:                        # his Seq 33-35 split (screen V1 under, face V2 on top, seam y 1038), batched: a single
        import geom as G                              # 208-clip call outlived the bridge's reply window (2026-10-12)
        jobs = [(0, 71, G.DEFAULT_POS), (1, G.FACE_SPLIT["scale"], G.FACE_SPLIT["pos"])]
        for ti, sc, ps in jobs:
            n = es("(function(){" + PRE + f"var S = seqByName({json.dumps(C['sequence'])}); return S.videoTracks[{ti}].clips.numItems; }})()")
            n = int(n)
            for a in range(0, n, 24):
                r = es("(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}), tr = S.videoTracks[{ti}], k = 0;
function prop(c, cn, pn){{ for (var i = 0; i < c.components.numItems; i++){{ var m = c.components[i]; if (m.displayName !== cn) continue;
  for (var q = 0; q < m.properties.numItems; q++) if (m.properties[q].displayName === pn) return m.properties[q]; }} return null; }}
for (var i = {a}; i < Math.min({a + 24}, tr.clips.numItems); i++){{ var c = tr.clips[i];
  var s = prop(c, 'Motion', 'Scale'), p = prop(c, 'Motion', 'Position');
  if (s.isTimeVarying()) s.setTimeVarying(false); s.setValue({sc}, true);
  if (p.isTimeVarying()) p.setTimeVarying(false); p.setValue([{ps[0]}, {ps[1]}], true); k++; }}
return k; }})()""")
                print(f"  V{ti + 1} clips {a}-{a + int(r) - 1}: scale {sc}")
    if "--verify" in sys.argv:
        segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
        off, _ = offset_fn(C["sync"])
        d = es("(function(){" + PRE + f"""var S = seqByName({json.dumps(C['sequence'])}); var o = [];
for (var t = 0; t < 2; t++){{ var tr = S.videoTracks[t], c = []; for (var i = 0; i < tr.clips.numItems; i++){{ var x = tr.clips[i]; c.push([x.start.seconds, x.end.seconds, x.inPoint.seconds]); }} o.push(c); }}
var a = S.audioTracks[0], ac = []; for (var i = 0; i < a.clips.numItems; i++){{ var x = a.clips[i]; ac.push([x.start.seconds, x.end.seconds, x.inPoint.seconds]); }} o.push(ac);
return JSON.stringify(o); }})()""")
        v1, v2, a1 = json.loads(d) if isinstance(d, str) else d
        bad = []
        if len(v1) != len(segs) or len(a1) != len(segs): bad.append(f"count V1 {len(v1)} A1 {len(a1)} vs {len(segs)}")
        for k, (s, c) in enumerate(zip(segs, v1)):
            if abs(c[2] - s["start"]) > 0.6 * fr: bad.append(f"V1 seg {k}: in {c[2]:.4f} vs {s['start']:.4f}")
        gaps = [(round(a[1], 4), round(b[0], 4)) for a, b in zip(v2, v2[1:]) if b[0] - a[1] > 1e-3]
        if gaps: bad.append(f"V2 gaps {gaps[:5]}")
        if abs(v2[0][0]) > 1e-3 or abs(v2[-1][1] - v1[-1][1]) > 1e-3: bad.append(f"V2 span {v2[0][0]:.3f}-{v2[-1][1]:.3f} vs V1 end {v1[-1][1]:.3f}")
        for c in v2:                                   # each camera piece's source time = the OBS time under it + offset
            k = max(i for i, x in enumerate(v1) if x[0] <= c[0] + 1e-4); x = v1[k]
            want = x[2] + (c[0] - x[0]) + off(x[2] + (c[0] - x[0]))
            if abs(c[2] - want) > 0.035: bad.append(f"V2 @{c[0]:.3f}: cam in {c[2]:.4f} vs {want:.4f}")
            # Premiere lands a 59.94 camera's in-point on the 60 fps sequence grid: measured 1-31 ms EARLY (mean 16 ms, Harbinger
            # 2026-10-12), inside lip-sync tolerance; anything past 35 ms is a real placement error
        print("verify:", "OK" if not bad else "PROBLEMS"); [print("  ", b) for b in bad[:20]]


if __name__ == "__main__":
    main()
