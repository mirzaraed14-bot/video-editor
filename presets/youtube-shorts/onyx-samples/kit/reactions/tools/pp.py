"""pp.py: a thin ExtendScript caller for the reaction sequences (ABW8, Sequences 33-35), same contract as lanes/premiere/face-nests.py es()."""
import json, subprocess, sys
from pathlib import Path
BRIDGE = Path(__file__).resolve().parents[4] / 'lanes' / 'premiere' / 'premiere-bridge.mjs'

_QUIET = Path(__file__).resolve().parents[4] / 'lanes' / 'premiere' / 'QUIET-MODE'


def es(script, timeout=170):
    """QUIET MODE (2026-11-14): while lanes/premiere/QUIET-MODE exists, writes wait until Affan is away from the machine
    (lanes/premiere/quietgate.py); reads pass at once. The gate fails closed: a write it cannot clear is refused."""
    if _QUIET.exists():
        try:
            if str(_QUIET.parent) not in sys.path: sys.path.insert(0, str(_QUIET.parent))
            import quietgate
            quietgate.gate(script)
        except Exception as e:
            return None, f'QUIET-MODE: write refused, cannot confirm Affan is away ({e})'
    return _es_raw(script, timeout)


_PAUSE = Path(__file__).resolve().parents[4] / 'lanes' / 'premiere' / 'PREMIERE-PAUSE'


def _es_raw(script, timeout=170):
    if _PAUSE.exists():                     # 2026-11-14: his Premiere hung; no call of ANY kind until the file is gone
        return None, 'PREMIERE-PAUSE: Premiere is paused for Affan (lanes/premiere/PREMIERE-PAUSE); no bridge calls, work offline'
    r = subprocess.run(['node', str(BRIDGE), 'execute_extendscript', json.dumps({'script': script})],
                       capture_output=True, text=True, timeout=timeout)
    try:
        j = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None, (r.stdout + r.stderr)[-600:]
    if isinstance(j, dict) and j.get('success') is False:
        return None, j.get('error') or j.get('status') or 'bridge error'
    d = j.get('data', j) if isinstance(j, dict) else j
    if isinstance(d, dict): d = d.get('result', d)
    return d, None

DUMP = r"""(function(){
function seqByName(n){ for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === n) return app.project.sequences[i]; return null; }
function motion(c){ var o = {}; for (var k = 0; k < c.components.numItems; k++) { var cm = c.components[k];
  if (cm.displayName === "Motion") for (var q = 0; q < cm.properties.numItems; q++) { var p = cm.properties[q]; try { var v = p.getValue(); o[p.displayName] = (v && v.length) ? [v[0], v[1]] : v; o[p.displayName + "_kf"] = p.isTimeVarying(); } catch(e){} } }
  var fx = []; for (var k = 0; k < c.components.numItems; k++) fx.push(c.components[k].displayName); o.fx = fx.join("|"); return o; }
var out = [];
var names = NAMES;
for (var n = 0; n < names.length; n++) {
  var s = seqByName(names[n]); if (!s) { out.push({name: names[n], missing: true}); continue; }
  var st = s.getSettings();
  var o = {name: s.name, w: st.videoFrameWidth, h: st.videoFrameHeight, fps: 1 / st.videoFrameRate.seconds, end: s.end / 254016000000, v: [], a: []};
  for (var t = 0; t < s.videoTracks.numTracks; t++) { var tr = s.videoTracks[t], cl = [];
    for (var i = 0; i < tr.clips.numItems; i++) { var c = tr.clips[i]; var path = ""; try { path = c.projectItem.getMediaPath(); } catch(e){}
      var m = DETAIL ? motion(c) : {};
      cl.push({n: c.name, s: +c.start.seconds.toFixed(3), e: +c.end.seconds.toFixed(3), i: +c.inPoint.seconds.toFixed(3), o: +c.outPoint.seconds.toFixed(3), p: path, m: m}); }
    o.v.push({t: tr.name, muted: tr.isMuted(), clips: cl}); }
  for (var t = 0; t < s.audioTracks.numTracks; t++) { var tr = s.audioTracks[t], cl = [];
    for (var i = 0; i < tr.clips.numItems; i++) { var c = tr.clips[i]; cl.push({n: c.name, s: +c.start.seconds.toFixed(3), e: +c.end.seconds.toFixed(3), i: +c.inPoint.seconds.toFixed(3)}); }
    o.a.push({t: tr.name, clips: cl}); }
  out.push(o); }
return JSON.stringify(out); })()"""

if __name__ == "__main__":
    names = sys.argv[1].split(",") if len(sys.argv) > 1 else ["Sequence 33", "Sequence 34", "Sequence 35"]
    detail = "--detail" in sys.argv
    d, err = es(DUMP.replace("NAMES", json.dumps(names)).replace("DETAIL", "true" if detail else "false"))
    if err: print("ERR", err); sys.exit(1)
    print(json.dumps(d if not isinstance(d, str) else json.loads(d), indent=1))
