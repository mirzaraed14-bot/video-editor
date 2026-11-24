"""addtracks.py <sequence> <video tracks needed>: ABW11 template is V3/A4; the plan needs V5 (screen, face, frame, mg, captions). QE addTracks appends, nothing moves. Run under premiere.lock (premo3.sh phase addtracks)."""
import os
import json, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A
name, need = sys.argv[1], int(sys.argv[2])
with A.active_window("hpp addtracks " + name):
    r = A.es("(function(){" + A.PRE + "var s = seqByName(" + json.dumps(name) + "); if (!s) return 'NOSEQ'; app.project.openSequence(s.sequenceID); return 'opened'; })()")
    print(r); time.sleep(2)
    out = A.es("(function(){ var seq = app.project.activeSequence; app.enableQE(); var tries = 0, before = seq.videoTracks.numTracks; while (seq.videoTracks.numTracks < %d && tries++ < 6) qe.project.getActiveSequence().addTracks(1, seq.videoTracks.numTracks, 0, 0, 0, 0, 0); return JSON.stringify({name: seq.name, before: before, after: seq.videoTracks.numTracks, a: seq.audioTracks.numTracks}); })()" % need)
    print(out)
