"""screenoff.py <plan.json> <t0>:<t1> [<t0>:<t1> ...]  (polish-2, 2026-11-09)
For each span: QE-razor the screen track (V1) at t0 and t1 (frame-snapped, only where a clip spans the time), then DISABLE the screen piece(s) lying inside
[t0, t1]. The panel then shows the window background (dark) instead of his raw screen between a full-panel graphic's exit and the next one's first opaque frame.
ONE locked active window (apply.active_window), the previous sequence restored; the caller holds premiere.lock (premo.sh screenoff). Saves ABW11."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A  # noqa: E402
plan, seq = A.load(sys.argv[1]); si = plan["screen_track"]
spans = [tuple(round(round(float(x) * 60) / 60, 4) for x in a.split(":")) for a in sys.argv[2:]]
undo = "--enable" in sys.argv
spans = [tuple(round(round(float(x) * 60) / 60, 4) for x in a.split(":")) for a in sys.argv[2:] if not a.startswith("--")]
with A.active_window(f"hpp screenoff {plan['sequence']}"):
    st = A.open_window(plan)
    try:
        T = sorted({t for s in spans for t in s})
        r = A.es("(function(){" + A.PRE + "var s = app.project.activeSequence; if (s.name !== " + json.dumps(plan["sequence"]) + ") return 'WRONG ' + s.name;"
                 "app.enableQE(); var q = qe.project.getActiveSequence(); if (q.name !== " + json.dumps(plan["sequence"]) + ") return 'WRONG QE ' + q.name;"
                 "var fps = 254016000000 / parseInt(s.timebase, 10), base = Math.round(fps);"
                 "function p(n){ return n < 10 ? '0' + n : '' + n; }"
                 "function tc(T){ var f = Math.round(T * fps); return p(Math.floor(f / (base * 3600))) + ':' + p(Math.floor(f / (base * 60)) % 60) + ':' + p(Math.floor(f / base) % 60) + ':' + p(f % base); }"
                 "function inside(tr, t){ for (var k = 0; k < tr.clips.numItems; k++){ var c = tr.clips[k]; if (c.start.seconds < t - 0.004 && c.end.seconds > t + 0.004) return true; } return false; }"
                 f"var T = {json.dumps(T)}, n = 0; for (var i = 0; i < T.length; i++) if (inside(s.videoTracks[{si}], T[i])) {{ q.getVideoTrackAt({si}).razor(tc(T[i])); n++; }}"
                 "return 'razors ' + n + ' of ' + T.length; })()", timeout=300)
        print("  ", r)
        if str(r).startswith("WRONG"): raise SystemExit(r)
        js = "(function(){" + A.PRE + "var s = app.project.activeSequence; var tr = s.videoTracks[" + str(si) + "]; var out = [];"
        for a, b in spans:
            js += (f"for (var i = 0; i < tr.clips.numItems; i++) {{ var c = tr.clips[i]; if (c.start.seconds > {a - 0.004} && c.end.seconds < {b + 0.004}) {{ c.disabled = {'false' if undo else 'true'}; "
                   "out.push(c.start.seconds.toFixed(3) + '-' + c.end.seconds.toFixed(3) + ' ' + (c.disabled ? 'OFF' : 'on')); } }")
        js += "return out.join(' | '); })()"
        print("  ", A.es(js, timeout=120))
    finally:
        A.close_window(st)
A.safe_save()
