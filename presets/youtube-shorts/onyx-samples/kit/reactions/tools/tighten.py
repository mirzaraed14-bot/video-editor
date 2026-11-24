"""tighten.py: cut filler words / long pauses out of Affan's rough-cut reaction sequence, on HIS timeline, every track in sync.

  PYTHONUTF8=1 python tighten.py <job>/tighten.json --apply      # backup, razor (one locked active window), lift, close gaps, micro-fades
  PYTHONUTF8=1 python tighten.py <job>/tighten.json --verify     # read back against the plan

tighten.json "cuts" come from fillercuts.py (frame-snapped, edges measured on the A1 rebuild, proven by cutcheck.py).
1. Backup: the sequence's per-clip state (work/pre-tighten.json) + an FCP XML (work/pre-tighten.xml), before anything moves.
2. Razor: QE razors every video and audio track at every cut edge where a clip spans it (a razor that already carried a
   linked track is not repeated). This is the ONLY step that makes the sequence active: one window, the cross-session lock
   (apply.active_window), his previous sequence restored in a finally.
3. Close: lift every piece inside a cut (no ripple), then move every later clip left by exactly the time removed before it,
   earliest first (a left move never collides). A clip already carried by its linked partner's move reads delta 0 and is
   skipped. Positions are read fresh before every move.
4. Micro-fades: each new A1 joint gets a 10 ms Level fade-out / fade-in (DOM keyframes), so no cut can click.
"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from apply import es, PRE, active_window, lvl_v      # noqa: E402

FADE = 0.010


def seq_js(name, body):
    return "(function(){" + PRE + "var s = seqByName(" + json.dumps(name) + "); if (!s) return 'NOSEQ';" + body + "})()"


def state(name):
    d = es(seq_js(name, """var o = {end: s.end / 254016000000, v: [], a: []};
for (var t = 0; t < s.videoTracks.numTracks; t++){ var tr = s.videoTracks[t], L = []; for (var i = 0; i < tr.clips.numItems; i++){ var c = tr.clips[i];
  L.push([c.name, c.start.seconds, c.end.seconds, c.inPoint.seconds, c.disabled ? 1 : 0]); } o.v.push(L); }
for (var t = 0; t < s.audioTracks.numTracks; t++){ var tr = s.audioTracks[t], L = []; for (var i = 0; i < tr.clips.numItems; i++){ var c = tr.clips[i];
  var lv = prop(c, 'Volume', 'Level'); L.push([c.name, c.start.seconds, c.end.seconds, c.inPoint.seconds, lv ? (lv.isTimeVarying() ? 'kf' : lv.getValue()) : null]); } o.a.push(L); }
return JSON.stringify(o);"""))
    return json.loads(d) if isinstance(d, str) else d


def removed_before(cuts, t, tol=0.004):
    return sum(b - a for a, b in cuts if b <= t + tol)


def apply(T, job):
    name, cuts = T["sequence"], T["cuts"]
    pre = state(name)
    json.dump(pre, open(os.path.join(job, "work", "pre-tighten.json"), "w"), indent=0)
    xml = os.path.join(job, "work", "pre-tighten.xml").replace("\\", "/")
    print("  backup xml:", es(seq_js(name, f"var f = new File({json.dumps(xml)}); s.exportAsFinalCutProXML(f.fsName, 1); return new File(f.fsName).exists ? 'ok' : 'NOFILE';")))   # needs the NATIVE path
    edges = sorted({t for c in cuts for t in c})
    # 2. razors (active window)
    with active_window(f"reactions/tighten.py {name}"):
        st = es("(function(){" + PRE + "var prev = app.project.activeSequence; var s = seqByName(" + json.dumps(name) + ");"
                "app.project.openSequence(s.sequenceID); return JSON.stringify({prev: prev ? prev.sequenceID : null, active: app.project.activeSequence.name}); })()")
        st = json.loads(st) if isinstance(st, str) else st
        print("  window open:", st)
        try:
            r = es("(function(){" + PRE + "var s = app.project.activeSequence; if (s.name !== " + json.dumps(name) + ") return 'WRONG ' + s.name;"
                   "app.enableQE(); var q = qe.project.getActiveSequence(); var fps = 254016000000 / parseInt(s.timebase, 10), base = Math.round(fps);"
                   "function p(n){ return n < 10 ? '0' + n : '' + n; }"
                   "function tc(T){ var f = Math.round(T * fps); return p(Math.floor(f / (base * 3600))) + ':' + p(Math.floor(f / (base * 60)) % 60) + ':' + p(Math.floor(f / base) % 60) + ':' + p(f % base); }"
                   "function inside(tr, t){ for (var k = 0; k < tr.clips.numItems; k++){ var c = tr.clips[k]; if (c.start.seconds < t - 0.004 && c.end.seconds > t + 0.004) return true; } return false; }"
                   "var E = " + json.dumps(edges) + ", n = 0;"
                   "for (var e = 0; e < E.length; e++){ var t = E[e];"
                   "  for (var v = 0; v < s.videoTracks.numTracks; v++) if (inside(s.videoTracks[v], t)) { q.getVideoTrackAt(v).razor(tc(t)); n++; }"
                   "  for (var a = 0; a < s.audioTracks.numTracks; a++) if (inside(s.audioTracks[a], t)) { q.getAudioTrackAt(a).razor(tc(t)); n++; } }"
                   "return 'razors ' + n + ' at ' + E.length + ' edges, fps ' + fps; })()", timeout=600)
            print("  ", r)
            if not str(r).startswith("razors"): raise SystemExit(r)
        finally:
            if st.get("prev"):
                print("  restored active sequence:", es("(function(){ app.project.openSequence(" + json.dumps(st["prev"]) + "); return app.project.activeSequence.name; })()"))
    # 3a. lift the pieces inside the cuts
    r = es(seq_js(name, "var C = " + json.dumps(cuts) + ", n = 0, tol = 0.004;"
                  "function lift(tr){ for (var i = tr.clips.numItems - 1; i >= 0; i--){ var c = tr.clips[i];"
                  "  for (var k = 0; k < C.length; k++) if (c.start.seconds >= C[k][0] - tol && c.end.seconds <= C[k][1] + tol) { c.remove(false, false); n++; break; } } }"
                  "for (var v = 0; v < s.videoTracks.numTracks; v++) lift(s.videoTracks[v]);"
                  "for (var a = 0; a < s.audioTracks.numTracks; a++) lift(s.audioTracks[a]);"
                  "return 'lifted ' + n;"), timeout=600)
    print("  ", r)
    # 3b. close the gaps: targets from a snapshot, deltas from fresh reads, earliest first, video tracks then audio
    snap = state(name)
    tgt = {"v": [[round(c[1] - removed_before(cuts, c[1]), 4) for c in tr] for tr in snap["v"]],
           "a": [[round(c[1] - removed_before(cuts, c[1]), 4) for c in tr] for tr in snap["a"]]}
    for kind, coll in (("v", "videoTracks"), ("a", "audioTracks")):
        for ti, targets in enumerate(tgt[kind]):
            if not targets: continue
            r = es(seq_js(name, f"var tr = s.{coll}[{ti}], G = {json.dumps(targets)}, n = 0, skip = 0;"
                          "for (var i = 0; i < tr.clips.numItems && i < G.length; i++){ var c = tr.clips[i], d = G[i] - c.start.seconds;"
                          "  if (Math.abs(d) > 0.0005) { c.move(d); n++; } else skip++; }"
                          "return 'moved ' + n + ' kept ' + skip;"), timeout=600)
            print(f"   {kind}{ti + 1}: {r}")
    # 4. micro-fades at every new A1 joint (the joint = a cut's start mapped onto the new timeline)
    joints = [round(a - removed_before(cuts, a), 4) for a, b in cuts]
    r = es(seq_js(name, f"var tr = s.audioTracks[0], J = {json.dumps(joints)}, F = {FADE}, lo = {lvl_v(-96)}, n = 0;"
                  "for (var j = 0; j < J.length; j++) for (var i = 0; i < tr.clips.numItems; i++){ var c = tr.clips[i], p = prop(c, 'Volume', 'Level'); if (!p) continue;"
                  "  var dur = c.end.seconds - c.start.seconds, k0 = c.inPoint.seconds, v0 = p.isTimeVarying() ? p.getValueAtKey(p.getKeys()[0]) : p.getValue();"
                  "  if (Math.abs(c.end.seconds - J[j]) < 0.004 && dur > 3 * F) { if (!p.isTimeVarying()) { p.setTimeVarying(true); p.addKey(k0); p.setValueAtKey(k0, v0, true); }"
                  "    p.addKey(k0 + dur - F); p.setValueAtKey(k0 + dur - F, v0, true); p.addKey(k0 + dur - 0.0005); p.setValueAtKey(k0 + dur - 0.0005, lo, true); n++; }"
                  "  if (Math.abs(c.start.seconds - J[j]) < 0.004 && dur > 3 * F) { if (!p.isTimeVarying()) { p.setTimeVarying(true); }"
                  "    p.addKey(k0); p.setValueAtKey(k0, lo, true); p.addKey(k0 + F); p.setValueAtKey(k0 + F, v0, true); n++; } }"
                  "return 'fades ' + n;"), timeout=600)
    print("  ", r)
    print("   save:", es("(function(){ app.project.save(); return 'saved'; })()"))


def verify(T, job):
    name, cuts = T["sequence"], T["cuts"]
    pre = json.load(open(os.path.join(job, "work", "pre-tighten.json")))
    now = state(name); bad = []
    rem = sum(b - a for a, b in cuts)
    if abs((pre["end"] - now["end"]) - rem) > 0.02: bad.append(f"end {pre['end']:.3f} -> {now['end']:.3f}, expected -{rem:.3f}")
    for kind in ("v", "a"):
        for ti, tr in enumerate(now[kind]):
            for x, y in zip(tr, tr[1:]):
                if y[1] < x[2] - 0.002: bad.append(f"{kind}{ti + 1} overlap at {y[1]:.3f}")
            # every surviving piece of every original clip lands at its mapped position
            for c in pre[kind][ti]:
                for (lo, hi) in [(c[1], c[2])]:
                    keep = [(lo, hi)]
                    for a, b in cuts:
                        keep = [seg for s0, s1 in keep for seg in ([(s0, s1)] if b <= s0 or a >= s1 else [(s0, a), (b, s1)]) if seg[1] - seg[0] > 0.004]
                    for s0, s1 in keep:
                        want = s0 - removed_before(cuts, s0)
                        if not any(abs(y[1] - want) < 0.003 and y[0] == c[0] for y in tr):
                            bad.append(f"{kind}{ti + 1} {c[0]} piece {s0:.3f}-{s1:.3f} not at {want:.3f}")
    for b in bad[:20]: print("  ✗", b)
    print(f"verify {name}: {len(bad)} problem(s); end {pre['end']:.3f} -> {now['end']:.3f} (-{rem:.3f} planned)")
    json.dump(now, open(os.path.join(job, "work", "post-tighten.json"), "w"), indent=0)
    return not bad


if __name__ == "__main__":
    path = sys.argv[1]; job = os.path.dirname(os.path.abspath(path)); T = json.load(open(path, encoding="utf-8"))
    if "--apply" in sys.argv: apply(T, job)
    if "--verify" in sys.argv: sys.exit(0 if verify(T, job) else 1)
