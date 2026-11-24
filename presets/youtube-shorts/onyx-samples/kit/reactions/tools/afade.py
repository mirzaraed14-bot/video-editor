"""afade.py: a click-free edge where a reviewed video starts or stops at full level (VLC pause/resume, a sample cut at a hard
audio edge): a short Volume ramp on the A1 clips on each side of the edit, so the joint dips for ~25 ms instead of clicking.

  PYTHONUTF8=1 python afade.py <job>/plan.json t1 t2 ... [--ms 25] [--verify]

DOM only (no active sequence). The A1 clip ENDING at t gets keys (end - ms: its level, end - 1 ms: -60 dB); the clip STARTING at t
gets (in: -60 dB, in + ms: its level). Key times are the clip's source time (as the music bed's keys in apply.py). The clip's own
Level (normally 0 dB, untouched) is read first and kept as the plateau, so nothing else in his mix changes. Re-running is a no-op
(the same keys are set again); a clip that ramps at both ends keeps both.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A   # noqa: E402

a = sys.argv[1:]
plan, seq = A.load(a[0])
ms = float(a[a.index("--ms") + 1]) / 1000 if "--ms" in a else 0.025
ts = [float(x) for x in a[1:] if not x.startswith("--") and (a.index(x) == 0 or a[a.index(x) - 1] != "--ms")]
vmin = A.lvl_v(-60)
for t in ts:
    js = A.head(plan) + f"""var tr = s.audioTracks[0], T = {t:.4f}, D = {ms:.4f}, out = [];
for (var i = 0; i < tr.clips.numItems; i++) {{ var c = tr.clips[i], s0 = c.start.seconds, e0 = c.end.seconds;
  var ends = Math.abs(e0 - T) < 0.009, starts = Math.abs(s0 - T) < 0.009; if (!ends && !starts) continue;
  if (e0 - s0 < 3 * D) {{ out.push('short ' + s0.toFixed(3)); continue; }}
  var p = prop(c, 'Volume', 'Level'); if (!p) {{ out.push('nolevel'); continue; }}
  var k0 = c.inPoint.seconds, ke = k0 + (e0 - s0), v = p.isTimeVarying() ? p.getValueAtTime(k0 + (ke - k0) / 2) : p.getValue();
  if (!p.isTimeVarying()) {{ p.setTimeVarying(true); p.addKey(k0); p.setValueAtKey(k0, v, true); p.addKey(ke - 0.001); p.setValueAtKey(ke - 0.001, v, true); }}
  if (ends) {{ p.addKey(ke - D); p.setValueAtKey(ke - D, v, true); p.addKey(ke - 0.001); p.setValueAtKey(ke - 0.001, {vmin}, true); out.push('out ' + s0.toFixed(3) + '-' + e0.toFixed(3)); }}
  if (starts) {{ p.addKey(k0); p.setValueAtKey(k0, {vmin}, true); p.addKey(k0 + D); p.setValueAtKey(k0 + D, v, true); out.push('in ' + s0.toFixed(3) + '-' + e0.toFixed(3)); }}
}}
return out.join(', ') || 'NOEDGE'; }})()"""
    print(f"  edge {t:.3f}: {A.es(js)}")
