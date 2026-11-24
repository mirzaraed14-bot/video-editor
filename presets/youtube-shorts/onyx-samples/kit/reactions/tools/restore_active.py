"""restore_active.py "<sequence name>": reopen that sequence as the active one (by id) inside ACTIVE-WINDOW.lock and prove it with DOM + QE
(after a bridge drop left OUR sequence active mid-window, 2026-10-27)."""
import os
import json, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A
name = sys.argv[1]
cur = A.es("(function(){ var a = app.project.activeSequence; return a ? a.name : ''; })()")
if "reaction" not in str(cur).lower():                  # 2026-11-14 QUIET MODE: never yank him off a sequence he picked
    print("his view untouched:", cur); raise SystemExit(0)
with A.active_window("batch5 restore_active " + name):
    r = A.es("(function(){" + A.PRE + "var s = seqByName(" + json.dumps(name) + "); if (!s) return 'NOSEQ'; app.project.openSequence(s.sequenceID); return 'opened'; })()")
    time.sleep(2)
    c = A.es("(function(){ var a = app.project.activeSequence; app.enableQE(); var q = qe.project.getActiveSequence(); return JSON.stringify({dom: a ? a.name : null, qe: q ? q.name : null}); })()")
    c = c if isinstance(c, dict) else json.loads(c); print(r, c, "OK" if c["dom"] == name and c["qe"] == name else "NOT RESTORED")
