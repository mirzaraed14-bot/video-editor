#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""music-dropouts.py — lift the music bed under every CUT ZOOM of a Premiere sequence.

The rule is both channels': the zoomed block plays voice only, so the point lands (Affan Afterhours facecam
PLAYBOOK § Music, 2026-09-30; AffanWiz STYLE § 4, 2026-09-28 / 2026-10-04).

  uv run lanes/premiere/music-dropouts.py "<sequence name>" [--music-track 2]            # plan, read-only
  uv run lanes/premiere/music-dropouts.py "<sequence name>" --apply --backup <job>/premiere-backup

A cut zoom = a clip whose Motion Scale is STATIC and > 100 %, on V1 or on any video track INSIDE a nest that sits on
V1 (mapped to sequence time and clipped to the nest clip's visible span). A KEYFRAMED scale is the gradual push
(100 -> 105/110) and is never a cut zoom. Overlapping or touching ranges merge.

--apply: saves the project, copies the .prproj and writes the music track's clips + levels into --backup (the undo),
makes the sequence active if it is not, QE-razors the music track at each range's first and last frame and lifts
(no ripple) the pieces inside, saves, reads back (0 music under any range, every surviving level unchanged, the video
tracks identical) and puts the previously active sequence back. Razoring keeps each piece's level and source offset.
Timecodes are frame indices at the sequence rate written with integer-rate labels (proven at 59.94 and 60).
"""
import json, os, shutil, subprocess, sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, 'premiere-bridge.mjs')
TICKS = 254016000000


def es(script, timeout=170):
    r = subprocess.run(['node', BRIDGE, 'execute_extendscript', json.dumps({'script': script})],
                       capture_output=True, text=True, timeout=timeout, encoding='utf-8')
    out = r.stdout.strip()
    d = json.loads(out[out.find('{'):out.rfind('}') + 1]) if '{' in out else out
    d = json.loads(d) if isinstance(d, str) else d
    if isinstance(d, dict) and d.get('success') is False:
        raise SystemExit('bridge: ' + str(d.get('error')))
    return d


# read-only: V1 (+ the nests on it) and the music track. Nothing before the IIFE (the bridge returns "undefined").
READ = r"""(function(){
  var NAME = %s, MT = %d, P = app.project, seq = null, i, j, k;
  for (i = 0; i < P.sequences.numSequences; i++) if (P.sequences[i].name === NAME) { seq = P.sequences[i]; break; }
  if (!seq) return JSON.stringify({ok:false, err:"no sequence named " + NAME});
  function r(x){ return Math.round(x * 100000) / 100000; }
  function scale(c){ for (var a = 0; a < c.components.numItems; a++) { var cp = c.components[a]; if (cp.displayName !== "Motion") continue;
      for (var b = 0; b < cp.properties.numItems; b++) { var pr = cp.properties[b]; if (pr.displayName !== "Scale") continue;
        try { return pr.isTimeVarying() ? "KF" : pr.getValue(); } catch (e) { return null; } } } return 100; }
  function level(c){ for (var a = 0; a < c.components.numItems; a++) { var cp = c.components[a]; if (cp.displayName !== "Volume") continue;
      try { return cp.properties[0].isTimeVarying() ? "KF" : r(cp.properties[0].getValue()); } catch (e) { return null; } } return null; }
  var v1 = [], ids = {}, t = seq.videoTracks[0];
  for (j = 0; j < t.clips.numItems; j++) { var c = t.clips[j], nid = null;
    try { if (c.projectItem && c.projectItem.isSequence()) { nid = c.projectItem.nodeId; ids[nid] = 1; } } catch (e) {}
    v1.push({n:c.name, s:r(c.start.seconds), e:r(c.end.seconds), ip:r(c.inPoint.seconds), sc:scale(c), nest:nid}); }
  var nests = {};
  for (i = 0; i < P.sequences.numSequences; i++) { var s2 = P.sequences[i]; if (!ids[s2.projectItem.nodeId]) continue;
    var cl = []; for (j = 0; j < s2.videoTracks.numTracks; j++) for (k = 0; k < s2.videoTracks[j].clips.numItems; k++) {
      var d = s2.videoTracks[j].clips[k]; cl.push({s:r(d.start.seconds), e:r(d.end.seconds), sc:scale(d)}); }
    nests[s2.projectItem.nodeId] = {name:s2.name, clips:cl}; }
  var vt = []; for (i = 0; i < seq.videoTracks.numTracks; i++) vt.push(seq.videoTracks[i].clips.numItems);
  var mt = seq.audioTracks[MT - 1], mus = [];
  for (j = 0; j < mt.clips.numItems; j++) { var m = mt.clips[j]; mus.push({n:m.name, s:r(m.start.seconds), e:r(m.end.seconds), ip:r(m.inPoint.seconds), lv:level(m)}); }
  var act = P.activeSequence;
  return JSON.stringify({ok:true, id:seq.sequenceID, tb:seq.timebase, path:P.path, active:act ? act.sequenceID : null,
                         vcounts:vt, v1:v1, nests:nests, music:mus});
})()"""

APPLY = r"""(function(){
  var ID = %s, MT = %d, R = %s, P = app.project, seq = null, i;
  for (i = 0; i < P.sequences.numSequences; i++) if (P.sequences[i].sequenceID === ID) { seq = P.sequences[i]; break; }
  if (!P.activeSequence || P.activeSequence.sequenceID !== ID) P.openSequence(ID);
  if (!P.activeSequence || P.activeSequence.sequenceID !== ID) return JSON.stringify({ok:false, err:"could not make the sequence active"});
  app.enableQE(); var qa = qe.project.getActiveSequence().getAudioTrackAt(MT - 1), A = seq.audioTracks[MT - 1];
  var fps = %s / parseInt(seq.timebase, 10), base = Math.round(fps);
  function p(n){ return n < 10 ? "0" + n : "" + n; }
  function tc(T){ var f = Math.round(T * fps); return p(Math.floor(f / (base * 3600))) + ":" + p(Math.floor(f / (base * 60)) %% 60) + ":" + p(Math.floor(f / base) %% 60) + ":" + p(f %% base); }
  function inside(t){ for (var k = 0; k < A.clips.numItems; k++) { var c = A.clips[k]; if (c.start.seconds < t - 0.004 && c.end.seconds > t + 0.004) return c; } return null; }
  var tol = 0.5 / fps, log = [];
  for (var r = R.length - 1; r >= 0; r--) { var a = R[r][0], b = R[r][1], cuts = 0, lifted = 0;
    if (inside(a)) { qa.razor(tc(a)); cuts++; }
    if (inside(b)) { qa.razor(tc(b)); cuts++; }
    for (var k = A.clips.numItems - 1; k >= 0; k--) { var c = A.clips[k]; if (c.start.seconds >= a - tol && c.end.seconds <= b + tol) { c.remove(false, false); lifted++; } }
    log.push([a, b, cuts, lifted]); }
  P.save();
  return JSON.stringify({ok:true, fps:fps, log:log});
})()"""

RESTORE = r"""(function(){ var ID = %s; if (ID && (!app.project.activeSequence || app.project.activeSequence.sequenceID !== ID)) app.project.openSequence(ID);
  return JSON.stringify({ok:true, active:app.project.activeSequence ? app.project.activeSequence.name : null}); })()"""


def read(name, mt):
    d = es(READ % (json.dumps(name), mt))
    if not d.get('ok'):
        raise SystemExit(d.get('err'))
    return d


def zoom_ranges(d):
    fr = TICKS / int(d['tb'])
    R = []
    for c in d['v1']:
        if c['nest']:
            for x in d['nests'].get(c['nest'], {}).get('clips', []):
                if isinstance(x['sc'], (int, float)) and x['sc'] > 100.01:
                    a = max(c['s'], c['s'] + x['s'] - c['ip']); b = min(c['e'], c['s'] + x['e'] - c['ip'])
                    if b - a > 0.5 / fr:
                        R.append([round(a, 5), round(b, 5), x['sc'], d['nests'][c['nest']]['name']])
        elif isinstance(c['sc'], (int, float)) and c['sc'] > 100.01:
            R.append([c['s'], c['e'], c['sc'], 'V1'])
    R.sort()
    M = []
    for a, b, sc, where in R:
        if M and a <= M[-1][1] + 0.002:
            M[-1][1] = max(M[-1][1], b); M[-1][2].append(sc)
        else:
            M.append([a, b, [sc], where])
    return M


def music_in(m, a, b):
    return sum(max(0.0, min(c['e'], b) - max(c['s'], a)) for c in m)


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith('--'):
        raise SystemExit(__doc__)
    name, mt = a[0], int(a[a.index('--music-track') + 1]) if '--music-track' in a else 2
    d = read(name, mt)
    R = zoom_ranges(d)
    todo = [r for r in R if music_in(d['music'], r[0], r[1]) > 0.004]
    print(f"{name}: {len(R)} cut-zoom ranges (static scale > 100 on V1 and inside {len(d['nests'])} nests; pushes excluded)")
    for r in R:
        mu = music_in(d['music'], r[0], r[1])
        print(f"  {r[0]:9.3f}-{r[1]:9.3f}  {r[1]-r[0]:5.2f}s  x{'/'.join(str(round(s)) for s in r[2])}  {r[3]:<20}  "
              f"{'music %.2fs -> lift' % mu if mu > 0.004 else 'already silent'}")
    print(f"music track A{mt}: {len(d['music'])} clips · to lift under {len(todo)} ranges")
    if '--apply' not in a or not todo:
        return
    if '--backup' not in a:
        raise SystemExit('--apply needs --backup <dir> (the undo: a .prproj copy + the music track record)')
    bk = a[a.index('--backup') + 1]; os.makedirs(bk, exist_ok=True)
    es('(function(){ app.project.save(); return JSON.stringify({ok:true}); })()')
    stem = name.replace(' ', '-').lower()
    shutil.copy2(d['path'], os.path.join(bk, f"{os.path.splitext(os.path.basename(d['path']))[0]}-before-music-dropouts-{stem}.prproj"))
    json.dump(d['music'], open(os.path.join(bk, f'music-before-dropouts-{stem}.json'), 'w', encoding='utf-8'), indent=1)
    res = es(APPLY % (json.dumps(d['id']), mt, json.dumps([[r[0], r[1]] for r in todo]), TICKS), timeout=300)
    if not res.get('ok'):
        raise SystemExit(res.get('err'))
    after = read(name, mt)
    es(RESTORE % json.dumps(d['active']))
    left = [r for r in R if music_in(after['music'], r[0], r[1]) > 0.004]
    lv0, lv1 = {str(c['lv']) for c in d['music']}, {str(c['lv']) for c in after['music']}
    same_v = after['vcounts'] == d['vcounts'] and after['v1'] == d['v1']
    print(f"applied: {sum(x[3] for x in res['log'])} pieces lifted, {sum(x[2] for x in res['log'])} razors · "
          f"A{mt} {len(d['music'])} -> {len(after['music'])} clips · music under a range: {len(left)} · "
          f"levels {'unchanged' if lv1 <= lv0 else 'CHANGED ' + str(lv1 - lv0)} · video tracks {'identical' if same_v else 'CHANGED'}")
    json.dump(after['music'], open(os.path.join(bk, f'music-after-dropouts-{stem}.json'), 'w', encoding='utf-8'), indent=1)
    if left or not same_v or not lv1 <= lv0:
        raise SystemExit('VERIFY FAILED: restore from ' + bk)


if __name__ == '__main__':
    main()
