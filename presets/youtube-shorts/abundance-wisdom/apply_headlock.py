#!/usr/bin/env python
"""track.json + the linked AE comps -> an ExtendScript that applies the creator's head lock.

What After Effects' own Stabilize Motion does, done by script: the layer's Anchor Point is keyed on
EVERY frame so the tracked nose stays where it sat on the clip's first frame (Position untouched),
keys are LINEAR (as in the creator's comps), and Motion Tile (Output Height 340, Mirror Edges on)
fills whatever edge the movement exposes. Output Width is raised only on a layer whose horizontal
travel would otherwise expose a side.

usage: python apply_headlock.py <job_dir> <map.json> <out.jsx> [--hold median|first]
  --hold median (default since 2026-09-26) holds the nose where the creator's crop framed it
  map.json: [{"comp": "...", "layer": n, "clip": "<track.json key>", "tl_offset": seconds}, ...]
"""
import json, os, sys

FW, FH = 1080, 1920
HOLD = 'median'


def main(job, map_path, out_jsx):
    tr = json.load(open(os.path.join(job, 'track.json'), encoding='utf-8'))
    mp = json.load(open(map_path, encoding='utf-8'))
    jobs, report = [], []
    for m in mp:
        t = tr[m['clip']]
        s = t['scale'] / 100.0
        W, H = t['W'], t['H']
        # "prescale": [kx, ky] pushes a frame BAKED INTO THE SOURCE (a channel's border) out of the
        # layer with a Transform effect before Motion Tile, so the mirror copies clean pixels; the
        # layer's Scale drops by the same factor, so the framing at rest is unchanged.
        kx, ky = m.get('prescale', [1.0, 1.0])
        sx, sy = s / kx, s / ky
        # where the nose is HELD: 'first' = where it sat on frame 1 (AE Stabilize's default);
        # 'median' = its median position, i.e. where the creator's crop (set on the playing clip)
        # framed it. A head that moves early parks off-centre under 'first' (comp 10 L1: x 180 vs 421).
        if HOLD == 'median':
            n0 = [sorted(p[0] for p in t['nose'])[len(t['nose']) // 2], sorted(p[1] for p in t['nose'])[len(t['nose']) // 2]]
        else:
            n0 = t['nose'][0]
        anchor0 = [W / 2.0, H / 2.0]
        times, vals = [], []
        xs = []
        for f, (nx, ny) in enumerate(t['nose']):
            dx, dy = nx - n0[0], ny - n0[1]
            times.append(round(t['tl_start'] - m['tl_offset'] + f / 60.0, 6))
            vals.append([round(anchor0[0] + kx * dx, 3), round(anchor0[1] + ky * dy, 3)])
            xs.append(dx)
        # horizontal coverage: layer centre sits at pos_x; image shifts by -dx*s; layer half-width W*sx/2
        pos_x = t['pos'][0] * FW
        half = W * sx / 2
        worst = max(max(abs(pos_x - x * s - FW / 2) - (half - FW / 2), 0) for x in xs)
        out_w = 100 if worst <= 0 else min(300, int(100 * (1 + 2 * worst / (W * sx))) + 10)
        job = {'comp': m['comp'], 'layer': m['layer'], 'times': times, 'vals': vals, 'outW': out_w}
        if (kx, ky) != (1.0, 1.0):
            job.update({'pre': [round(kx * 100, 3), round(ky * 100, 3)], 'scale': [round(sx * 100, 4), round(sy * 100, 4)]})
        jobs.append(job)
        report.append('%s L%d  clip %s  %d keys  travel x %.0f..%.0f  y %.0f..%.0f (comp px)  tile width %d' % (
            m['comp'], m['layer'], m['clip'], len(times),
            min(xs) * s, max(xs) * s,
            min(v[1] - anchor0[1] for v in vals) * s, max(v[1] - anchor0[1] for v in vals) * s, out_w))

    log = os.path.splitext(os.path.abspath(out_jsx))[0] + '.txt'    # AE writes its report next to the jsx
    code = r'''(function () {
var OUT = %s;
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
    // AE invalidates held property references whenever an effect is added or moved: look every
    // one up again after each structural change (the first run died on a stale reference).
    function fxFind(test) { var fx = ly.property("Effects"); for (var e = 1; e <= fx.numProperties; e++) if (test(fx.property(e))) return fx.property(e); return null; }
    var isBord = function (p) { return p.name === "Border out (Claude)"; };
    var isTile = function (p) { return p.matchName === "ADBE Tile"; };
    if (J.pre) {                                   // absolute values: re-running never compounds
      if (!fxFind(isBord)) ly.property("Effects").addProperty("ADBE Geometry2").name = "Border out (Claude)";
      var bord = fxFind(isBord);
      bord.property("ADBE Geometry2-0011").setValue(0);          // Uniform Scale off
      bord.property("ADBE Geometry2-0004").setValue(J.pre[0]);   // Scale Width
      bord.property("ADBE Geometry2-0003").setValue(J.pre[1]);   // Scale Height
      try { bord.property("ADBE Geometry2-0012").setValue(2); } catch (eS) {}   // Sampling: bicubic
      ly.property("Transform").property("Scale").setValue([J.scale[0], J.scale[1], 100]);
      fxFind(isBord).moveTo(1);
    }
    if (!fxFind(isTile)) ly.property("Effects").addProperty("ADBE Tile");
    if (J.pre) fxFind(isTile).moveTo(2);
    var tile = fxFind(isTile);
    tile.property("Output Height").setValue(340);
    tile.property("Output Width").setValue(J.outW);
    tile.property("Mirror Edges").setValue(1);
    ap = ly.property("Transform").property("Anchor Point");
    var fxs = ly.property("Effects"), order = [];
    for (var o = 1; o <= fxs.numProperties; o++) order.push(fxs.property(o).name);
    var b2 = fxFind(isBord);
    L.push(J.comp + " L" + J.layer + " '" + ly.name.substring(0, 30) + "' keys " + ap.numKeys +
           " first " + ap.keyValue(1).join(",") + " @" + ap.keyTime(1).toFixed(3) +
           " last @" + ap.keyTime(ap.numKeys).toFixed(3) + " tileW " + fxFind(isTile).property("Output Width").value +
           " fx [" + order.join(" > ") + "]" +
           (b2 ? " scale " + ly.property("Transform").property("Scale").value.join(",") + " border-out " +
            b2.property("ADBE Geometry2-0004").value + "/" + b2.property("ADBE Geometry2-0003").value : ""));
  }
  app.endUndoGroup();
} catch (err) { L.push("ERROR " + err.toString() + (err.line ? " line " + err.line : "")); try { app.endUndoGroup(); } catch (e2) {} }
var f = new File(OUT); f.encoding = "UTF-8"; f.open("w"); f.write(L.join("\n")); f.close();
})();''' % (json.dumps(log.replace('\\', '/')), json.dumps(jobs))
    open(out_jsx, 'w', encoding='utf-8').write(code)
    print('\n'.join(report))
    print('wrote', out_jsx, '(%d layers, %d keys) -> AE report lands at %s' % (len(jobs), sum(len(j['times']) for j in jobs), log))


if __name__ == '__main__':
    if '--hold' in sys.argv:
        HOLD = sys.argv[sys.argv.index('--hold') + 1]
    main(sys.argv[1], sys.argv[2], sys.argv[3])
