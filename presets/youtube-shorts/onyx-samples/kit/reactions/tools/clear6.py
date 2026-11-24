"""clear6.py <plan.json>: remove EVERY clip from the plan's frame / MG / caption video tracks (and every .wav on its SFX tracks A2/A4) of its sequence (DOM, the sequence is not
activated), so apply.py --overlays re-places the r2 graphics from a clean slate (it skips a same-name clip at a graphic's start and only
removes the clip AT each start: a graphic that moved, shrank or was dropped would leave its old clip behind). These three tracks hold
nothing but this job's own overlays (the sequence was created by build_seq3 for this reaction). Prints what it removed."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seq import es   # noqa: E402
plan = json.load(open(sys.argv[1], encoding="utf-8"))
T = sorted({plan["frame_track"], plan["mg_track"], plan["cap_track"]})
AT = plan.get("sfx_tracks", [1, 3])                  # the SFX tracks (A2/A4): only this job's cues live there too
if min(T) <= max(plan["face_track"], plan["screen_track"]): raise SystemExit(f"refusing: overlay tracks {T} overlap the footage tracks")
js = """(function(){
var N = %s, T = %s, AT = %s, S = null;
for (var i = 0; i < app.project.sequences.numSequences; i++) if (app.project.sequences[i].name === N) S = app.project.sequences[i];
if (!S) return 'NOSEQ';
var out = [];
for (var k = 0; k < T.length; k++) { var tr = S.videoTracks[T[k]], n = 0, names = [];
  for (var i = tr.clips.numItems - 1; i >= 0; i--) { names.push(tr.clips[i].name); tr.clips[i].remove(false, false); n++; }
  out.push('V' + (T[k] + 1) + ': ' + n + ' [' + names.reverse().join(', ') + ']'); }
for (var k = 0; k < AT.length; k++) { var tr = S.audioTracks[AT[k]], n = 0;
  for (var i = tr.clips.numItems - 1; i >= 0; i--) { if (/[.]wav$/i.test(tr.clips[i].name)) { tr.clips[i].remove(false, false); n++; } }
  out.push('A' + (AT[k] + 1) + ': ' + n + ' sfx'); }
return out.join(' | '); })()""" % (json.dumps(plan["sequence"]), json.dumps(T), json.dumps(AT))
print("clear6:", es(js, timeout=300))
