"""bedride6.py <plan.json> [--verify]: the music bed's RIDE (audio6.py writes plan["music"]["ride"] = [[t, dB offset], ...] every 1 s:
the bed held ~8 LU under whatever is on A1, +-4 dB) as Volume Level keys on the bed clip (A3), on top of apply.py's three keys (first
key, the tail-fade start, the end): the first key and the tail start take the ride's first / last offset, the end key stays silent.
DOM only. Run AFTER apply.py --overlays (which places the bed and its three keys). --verify reads every key back."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A   # noqa: E402
plan, seq = A.load(sys.argv[1]); VER = "--verify" in sys.argv
m = plan["music"]; ride = m.get("ride") or []
if not ride: raise SystemExit("no ride in the plan (run audio6.py --write)")
name = os.path.basename(m["file"]); bd = m["bed_db"]
keys = [[0.0, A.lvl_v(bd + ride[0][1])]] + [[t, A.lvl_v(bd + c)] for t, c in ride] + [["TAIL", A.lvl_v(bd + ride[-1][1])]]
js = A.head(plan) + f"""var tr = s.audioTracks[2], c = null; for (var i = 0; i < tr.clips.numItems; i++) if (tr.clips[i].name === {json.dumps(name)} && tr.clips[i].start.seconds < 0.01) c = tr.clips[i];
if (!c) return 'NOBED'; var p = prop(c, 'Volume', 'Level'); if (!p.isTimeVarying()) return 'NOT TIME-VARYING (run --overlays first)';
var k0 = c.inPoint.seconds, ke = k0 + (c.end.seconds - c.start.seconds), K = {json.dumps(keys)}, bad = [], n = 0;
for (var i = 0; i < K.length; i++) {{ var kt = K[i][0] === 'TAIL' ? ke - {A.TAIL} : k0 + K[i][0];
  if (!{str(VER).lower()}) {{ p.addKey(kt); p.setValueAtKey(kt, K[i][1], true); }}
  var v = p.getValueAtKey(kt); if (Math.abs(v - K[i][1]) > 1e-4) bad.push(kt.toFixed(2) + ':' + v); else n++; }}
var e = p.getValueAtKey(ke - 0.001);
return JSON.stringify({{keys: n, of: K.length, bad: bad.slice(0, 8), end: e}}); }})()"""
r = A.es(js, timeout=300); print("bedride6:", r)
d = r if isinstance(r, dict) else (json.loads(r) if isinstance(r, str) and r.startswith("{") else None)   # es() may hand back parsed JSON
if not d or d["bad"] or d["keys"] != d["of"]: sys.exit(1)
