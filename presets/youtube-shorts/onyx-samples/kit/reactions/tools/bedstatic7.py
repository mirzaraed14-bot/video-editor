"""bedstatic7.py <plan.json> [--verify]: REACTIONS-V3 recipe 2: the pre-rendered bed STEM sits on A3 at a STATIC level (plan music bed_db, 0 dB) with NO keys.
apply.py --overlays places the bed with its three flat keys; this removes the time-varying state (setStatic) and reads the level back. DOM only (sequence not activated)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A   # noqa: E402
plan, seq = A.load(sys.argv[1]); name = os.path.basename(plan["music"]["file"]); v = A.lvl_v(plan["music"].get("bed_db", 0.0))
js = A.head(plan) + f"""var tr = s.audioTracks[2], n = 0, out = [];
for (var i = 0; i < tr.clips.numItems; i++) {{ var c = tr.clips[i]; if (c.name !== {json.dumps(name)}) {{ out.push('OTHER ' + c.name + ' ' + c.start.seconds.toFixed(2)); continue; }}
  var p = prop(c, 'Volume', 'Level'); if (!{str('--verify' in sys.argv).lower()}) setStatic(p, {v}); n++;
  out.push(c.start.seconds.toFixed(3) + '-' + c.end.seconds.toFixed(3) + ' tv=' + p.isTimeVarying() + ' v=' + p.getValue()); }}
return n + ' bed clip(s): ' + out.join(' | '); }})()"""
print("bedstatic7:", A.es(js, timeout=300))
