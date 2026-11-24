"""tlread7.py: READ-ONLY readback of everything audio on a NAMED sequence (never activates it, never writes).
read_audio(seq_name) -> dict(tracks=[{i,name,muted,solo?,clips=[{s,e,in,out,path,name,disabled,comps=[{name,props=[{n,v,tv,keys:[[t,v]]}]}]}]}]).
Premiere ExtendScript value scales (see AUDIO-ROOT-CAUSE.md): Volume>Level = 10**((dB-15)/20); Amplify L/R = (dB+96)/144; keys are in the
clip's MEDIA time (inPoint-relative)."""
import json, os, subprocess, sys
from pathlib import Path
BRIDGE = Path(__file__).resolve().parents[4] / "lanes" / "premiere" / "premiere-bridge.mjs"

def es(script, timeout=240):
    r = subprocess.run(["node", str(BRIDGE), "execute_extendscript", json.dumps({"script": script})], capture_output=True, text=True, timeout=timeout)
    try: j = json.loads(r.stdout)
    except json.JSONDecodeError: raise SystemExit("bridge: " + (r.stdout + r.stderr)[-600:])
    if isinstance(j, dict) and j.get("success") is False: raise SystemExit("ES error: " + str(j.get("error") or j))
    d = j.get("data", j) if isinstance(j, dict) else j
    if isinstance(d, dict): d = d.get("result", d)
    return d

JS = r"""(function(){
var N = SEQNAME, S = null;
for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === N) S = app.project.sequences[i];
if (!S) return 'NOSEQ';
function sv(x){ try { if (x && x.length !== undefined && typeof x !== 'string') { var a = []; for (var i = 0; i < x.length; i++) a.push(x[i]); return a; } return x; } catch(e){ return null; } }
var o = {tracks: [], seq: S.name, end: S.end / 254016000000};
for (var t = 0; t < S.audioTracks.numTracks; t++) { var tr = S.audioTracks[t];
  var T = {i: t, name: tr.name, muted: tr.isMuted(), clips: []};
  try { T.solo = tr.isSolo ? tr.isSolo() : null; } catch(e){ T.solo = 'ERR'; }
  try { T.locked = tr.isLocked(); } catch(e){}
  for (var i = 0; i < tr.clips.numItems; i++) { var c = tr.clips[i]; var path = ''; try { path = c.projectItem.getMediaPath(); } catch(e){}
    var C = {name: c.name, s: c.start.seconds, e: c.end.seconds, i: c.inPoint.seconds, o: c.outPoint.seconds, path: path, disabled: c.isDisabled ? c.isDisabled() : c.disabled, comps: []};
    try { C.speed = c.getSpeed ? c.getSpeed() : null; } catch(e){}
    for (var k = 0; k < c.components.numItems; k++) { var cm = c.components[k]; var M = {name: cm.displayName, props: []};
      for (var q = 0; q < cm.properties.numItems; q++) { var p = cm.properties[q]; var P = {n: p.displayName};
        try { P.v = sv(p.getValue()); } catch(e){ P.v = 'ERR'; }
        try { P.tv = p.isTimeVarying(); } catch(e){}
        if (P.tv) { P.keys = []; try { var ks = p.getKeys(); for (var z = 0; z < ks.length; z++) P.keys.push([ks[z].seconds, sv(p.getValueAtKey(ks[z]))]); } catch(e){ P.keyerr = String(e); } }
        M.props.push(P); }
      C.comps.push(M); }
    T.clips.push(C); }
  o.tracks.push(T); }
return JSON.stringify(o); })()"""

FADER = r"""(function(){ var N = SEQNAME; app.enableQE(); var q = qe.project.getActiveSequence(); if (!q || q.name !== N) return JSON.stringify({err: 'QE active sequence is ' + (q ? q.name : 'none') + ', not ' + N});
var o = []; for (var i = 0; i < q.numAudioTracks; i++) { var t = q.getAudioTrackAt(i), v = null; try { for (var k = 0; k < t.numComponents; k++) { var cm = t.getComponentAt(k); if (cm.name === 'Track') v = cm.getParamValue('Volume'); } } catch(e){} o.push(v); } return JSON.stringify({faders: o}); })()"""

def read_audio(name):
    d = es(JS.replace("SEQNAME", json.dumps(name)))
    if d == "NOSEQ": raise SystemExit("sequence not found: " + name)
    TL = json.loads(d) if isinstance(d, str) else d
    try:    # the track faders are only readable through QE, which sees the ACTIVE sequence: read them only when that is this one (never switches anything)
        f = es(FADER.replace("SEQNAME", json.dumps(name))); f = json.loads(f) if isinstance(f, str) else f
        for t, v in zip(TL["tracks"], f.get("faders", [])): t["fader"] = v
        if f.get("err"): TL["fader_note"] = f["err"]
    except SystemExit as e: TL["fader_note"] = str(e)
    return TL

if __name__ == "__main__":
    out = read_audio(sys.argv[1]); json.dump(out, open(sys.argv[2], "w"), indent=1); print(len(out["tracks"]), "tracks", sum(len(t["clips"]) for t in out["tracks"]), "clips")
