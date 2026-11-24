"""clipgain6.py <plan.json> [--verify]: set every A1 clip's Amplify to its OWN measured gain (plan["clip_gains"] [[seq start, dB, kind]],
audio6.py: each clip's loud words at -6 dBFS into the -6 dBFS Hard Limiter), DOM only (the sequence is not activated). Run AFTER
apply.py --window (audio-polish.py put Amplify + Hard Limiter on every A1 clip). A mono clip gets +3 dB (Premiere's centre pan law)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seq import es   # noqa: E402
plan = json.load(open(sys.argv[1], encoding="utf-8")); VERIFY = "--verify" in sys.argv
G = [[round(s, 4), round((g + 96) / 144, 6), round((g + 3 + 96) / 144, 6), round(g, 2)] for s, g, k in plan["clip_gains"]]
js = """(function(){
var N = %s, Gs = %s, VER = %s; var S = null;
for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === N) S = app.project.sequences[i];
if (!S) return 'NOSEQ';
function comp(c, n){ for (var k = 0; k < c.components.numItems; k++) if (c.components[k].displayName === n) return c.components[k]; return null; }
function prop(cm, n){ for (var q = 0; q < cm.properties.numItems; q++) if (cm.properties[q].displayName === n) return cm.properties[q]; return null; }
var tr = S.audioTracks[0], ok = 0, bad = [], mono = 0;
for (var i = 0; i < tr.clips.numItems; i++) {
  var c = tr.clips[i], s0 = c.start.seconds, g = null;
  for (var j = 0; j < Gs.length; j++) if (Math.abs(Gs[j][0] - s0) < 0.006) { g = Gs[j]; break; }
  if (!g) { bad.push('nogain ' + s0.toFixed(3)); continue; }
  var a = comp(c, 'Amplify'); if (!a) { bad.push('noamp ' + s0.toFixed(3)); continue; }
  var L = prop(a, 'Left'), R = prop(a, 'Right'), Gn = prop(a, 'Gain');
  if (L && R) { if (!VER) { L.setValue(g[1], true); R.setValue(g[1], true); } if (Math.abs(L.getValue() - g[1]) > 1e-4 || Math.abs(R.getValue() - g[1]) > 1e-4) bad.push('L/R ' + s0.toFixed(3)); else ok++; }
  else if (Gn) { mono++; if (!VER) Gn.setValue(g[2], true); if (Math.abs(Gn.getValue() - g[2]) > 1e-4) bad.push('G ' + s0.toFixed(3)); else ok++; }
  else bad.push('noprop ' + s0.toFixed(3));
}
return JSON.stringify({clips: tr.clips.numItems, ok: ok, mono: mono, bad: bad.slice(0, 12)}); })()""" % (json.dumps(plan["sequence"]), json.dumps(G), "true" if VERIFY else "false")
r = es(js); print("clipgain6:", r)
d = json.loads(r) if isinstance(r, str) and r.startswith("{") else r
if not isinstance(d, dict) or d.get("bad") or d.get("ok") != d.get("clips"): sys.exit(1)
