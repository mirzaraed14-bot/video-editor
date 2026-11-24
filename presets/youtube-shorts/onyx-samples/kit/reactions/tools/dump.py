"""dump.py: read ABW8 sequences into the reaction toolkit's dump format (DOM only: no sequence is activated).

  PYTHONUTF8=1 python dump.py <out.json> "Sequence A" ["Sequence B" ...]

[{name, w, h, fps, end, v: [{t, muted, clips: [{n, s, e, i, o, p, m}]}], a: [{t, clips: [{n, s, e, i}]}]}]
m = the clip's Motion values (+ "<name>_kf" when keyframed, + "fx" = its component list): the restore record before any edit.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pp import es  # noqa: E402

JS = r"""(function(){
var N = %s, out = [];
function seqByName(n){ for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === n) return app.project.sequences[i]; return null; }
for (var q = 0; q < N.length; q++) {
  var s = seqByName(N[q]); if (!s) { out.push({name: N[q], missing: true}); continue; }
  var st = s.getSettings();
  var o = {name: s.name, w: s.frameSizeHorizontal, h: s.frameSizeVertical, fps: Math.round(1 / st.videoFrameRate.seconds * 1000) / 1000, end: s.end / 254016000000, v: [], a: []};
  for (var t = 0; t < s.videoTracks.numTracks; t++) {
    var tr = s.videoTracks[t], cl = [];
    for (var i = 0; i < tr.clips.numItems; i++) {
      var c = tr.clips[i], m = {}, fx = [];
      for (var k = 0; k < c.components.numItems; k++) {
        var cp = c.components[k]; fx.push(cp.displayName);
        if (cp.displayName === "Opacity") for (var p = 0; p < cp.properties.numItems; p++) {   // 2026-11-14: offgrab needs it
          var po = cp.properties[p]; try { m[po.displayName] = po.getValue(); m[po.displayName + "_kf"] = po.isTimeVarying(); } catch (e) {}
        }
        if (cp.displayName === "Motion") for (var p = 0; p < cp.properties.numItems; p++) {
          var pr = cp.properties[p]; try { m[pr.displayName] = pr.getValue(); m[pr.displayName + "_kf"] = pr.isTimeVarying(); } catch (e) {}
        }
      }
      m.fx = fx.join("|");
      cl.push({n: c.name, s: c.start.seconds, e: c.end.seconds, i: c.inPoint.seconds, o: c.outPoint.seconds, p: c.projectItem ? c.projectItem.getMediaPath() : null, d: c.disabled ? 1 : 0, m: m});
    }
    o.v.push({t: t, muted: tr.isMuted(), clips: cl});
  }
  for (var t = 0; t < s.audioTracks.numTracks; t++) {
    var tr = s.audioTracks[t], cl = [];
    for (var i = 0; i < tr.clips.numItems; i++) { var c = tr.clips[i]; cl.push({n: c.name, s: c.start.seconds, e: c.end.seconds, i: c.inPoint.seconds}); }
    o.a.push({t: t, clips: cl});
  }
  out.push(o);
}
return JSON.stringify(out); })()"""

if __name__ == "__main__":
    out, names = sys.argv[1], sys.argv[2:]
    d, err = es(JS % json.dumps(names), 170)
    if err: raise SystemExit(f"ES error: {err}")
    d = json.loads(d) if isinstance(d, str) else d
    json.dump(d, open(out, "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    for s in d:
        if s.get("missing"): print(f"{s['name']}: MISSING"); continue
        print(f"{s['name']}: {s['w']}x{s['h']} @ {s['fps']}  end {s['end']:.3f}  V " + " ".join(str(len(t['clips'])) for t in s["v"]) +
              "  A " + " ".join(str(len(t['clips'])) for t in s["a"]))
