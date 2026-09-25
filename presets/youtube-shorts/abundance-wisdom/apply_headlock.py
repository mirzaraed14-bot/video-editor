#!/usr/bin/env python
"""track.json + the linked AE comps -> an ExtendScript that applies the creator's head lock.

What After Effects' own Stabilize Motion does, done by script: the layer's Anchor Point is keyed on
EVERY frame so the tracked nose stays where it sat on the clip's first frame (Position untouched),
keys are LINEAR (as in the creator's comps), and Motion Tile (Output Height 340, Mirror Edges on)
fills whatever edge the movement exposes. Output Width is raised only on a layer whose horizontal
travel would otherwise expose a side.

usage: python apply_headlock.py <job_dir> <map.json> <out.jsx>
  map.json: [{"comp": "...", "layer": n, "clip": "<track.json key>", "tl_offset": seconds}, ...]
"""
import json, os, sys

FW, FH = 1080, 1920


def main(job, map_path, out_jsx):
    tr = json.load(open(os.path.join(job, 'track.json'), encoding='utf-8'))
    mp = json.load(open(map_path, encoding='utf-8'))
    jobs, report = [], []
    for m in mp:
        t = tr[m['clip']]
        s = t['scale'] / 100.0
        W, H = t['W'], t['H']
        n0 = t['nose'][0]
        anchor0 = [W / 2.0, H / 2.0]
        times, vals = [], []
        xs = []
        for f, (nx, ny) in enumerate(t['nose']):
            dx, dy = nx - n0[0], ny - n0[1]
            times.append(round(t['tl_start'] - m['tl_offset'] + f / 60.0, 6))
            vals.append([round(anchor0[0] + dx, 3), round(anchor0[1] + dy, 3)])
            xs.append(dx)
        # horizontal coverage: layer centre sits at pos_x; image shifts by -dx*s
        pos_x = t['pos'][0] * FW
        half = W * s / 2
        worst = max(max(abs(pos_x - x * s - FW / 2) - (half - FW / 2), 0) for x in xs)
        out_w = 100 if worst <= 0 else min(300, int(100 * (1 + 2 * worst / (W * s))) + 10)
        jobs.append({'comp': m['comp'], 'layer': m['layer'], 'times': times, 'vals': vals, 'outW': out_w})
        report.append('%s L%d  clip %s  %d keys  travel x %.0f..%.0f  y %.0f..%.0f (comp px)  tile width %d' % (
            m['comp'], m['layer'], m['clip'], len(times),
            min(xs) * s, max(xs) * s,
            min(v[1] - anchor0[1] for v in vals) * s, max(v[1] - anchor0[1] for v in vals) * s, out_w))

    code = r'''(function () {
var OUT = "C:/Users/affan/AppData/Local/Temp/claude/E--Claude-Projects-video-editor-client-video-editor/7173e089-1e87-4811-944b-8e4043fa359d/scratchpad/ae/headlock.txt";
var JOBS = %s;
var L = [];
try {
  function comp(name) { for (var i = 1; i <= app.project.numItems; i++) { var it = app.project.item(i); if (it instanceof CompItem && it.name === name) return it; } return null; }
  app.beginUndoGroup("Head lock (Claude)");
  for (var j = 0; j < JOBS.length; j++) {
    var J = JOBS[j], c = comp(J.comp);
    if (!c) { L.push("MISSING COMP " + J.comp); continue; }
    var ly = c.layer(J.layer);
    var ap = ly.property("Transform").property("Anchor Point");
    while (ap.numKeys > 0) ap.removeKey(1);
    ap.setValuesAtTimes(J.times, J.vals);
    for (var k = 1; k <= ap.numKeys; k++) ap.setInterpolationTypeAtKey(k, KeyframeInterpolationType.LINEAR, KeyframeInterpolationType.LINEAR);
    var fx = ly.property("Effects"), tile = null;
    for (var e = 1; e <= fx.numProperties; e++) if (fx.property(e).matchName === "ADBE Tile") tile = fx.property(e);
    if (!tile) tile = fx.addProperty("ADBE Tile");
    tile.property("Output Height").setValue(340);
    tile.property("Output Width").setValue(J.outW);
    tile.property("Mirror Edges").setValue(1);
    L.push(J.comp + " L" + J.layer + " '" + ly.name.substring(0, 30) + "' keys " + ap.numKeys +
           " first " + ap.keyValue(1).join(",") + " @" + ap.keyTime(1).toFixed(3) +
           " last @" + ap.keyTime(ap.numKeys).toFixed(3) + " tileW " + J.outW);
  }
  app.endUndoGroup();
} catch (err) { L.push("ERROR " + err.toString() + (err.line ? " line " + err.line : "")); try { app.endUndoGroup(); } catch (e2) {} }
var f = new File(OUT); f.encoding = "UTF-8"; f.open("w"); f.write(L.join("\n")); f.close();
})();''' % json.dumps(jobs)
    open(out_jsx, 'w', encoding='utf-8').write(code)
    print('\n'.join(report))
    print('wrote', out_jsx, '(%d layers, %d keys)' % (len(jobs), sum(len(j['times']) for j in jobs)))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
