#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""Prove a head lock from what After Effects ACTUALLY holds, without a face detector.

The comp can't be rendered by script here (saveFrameToPng writes nothing on these comps), so the
proof rebuilds each comp frame from the source file plus the Anchor Point values READ BACK from AE:
    comp = Position + (source - Anchor(t)) * scale
and crops around the point where the nose sat on frame 1. Row LOCK = what AE plays; row raw = the
same frames with the anchor frozen at frame 1. Locked = the nose stays on the crosshair.

Do NOT measure the lock by re-detecting the nose on the comp frame: a face blown up 180-270 % is far
above YuNet's anchor sizes, its landmarks wander by 100+ px and a perfect lock looks broken.

usage:
  python headlock_proof.py jsx   <job> <map.json> <read.jsx> <read.json> [comp:layer,...]
  (run read.jsx with AfterFX -r; it writes read.json)
  python headlock_proof.py sheet <job> <map.json> <read.json> <out.jpg>
"""
import json, os, subprocess, sys

FW, FH, C, N = 1080, 1920, 240, 8


def make_jsx(job, map_path, out_jsx, out_json, pick=None):
    mp = json.load(open(map_path, encoding='utf-8'))
    sel = [(m['comp'], m['layer']) for m in mp]
    if pick:
        want = {(p.rsplit(':', 1)[0], int(p.rsplit(':', 1)[1])) for p in pick.split(',')}
        sel = [s for s in sel if s in want]
    code = r'''(function () {
  var OUT = %s, PICK = %s, N = %d, R = [], err = "";
  try {
    function comp(name) { for (var i = 1; i <= app.project.numItems; i++) { var it = app.project.item(i); if (it instanceof CompItem && it.name === name) return it; } return null; }
    for (var p = 0; p < PICK.length; p++) {
      var c = comp(PICK[p][0]), ly = c.layer(PICK[p][1]), tr = ly.property("Transform");
      var ap = tr.property("Anchor Point"), pos = tr.property("Position").value, sc = tr.property("Scale").value;
      var smp = [];
      for (var j = 0; j < N; j++) {
        var t = Math.round((ly.inPoint + j * (ly.outPoint - 1 / c.frameRate - ly.inPoint) / (N - 1)) * c.frameRate) / c.frameRate;
        var a = ap.valueAtTime(t, false);
        smp.push('{"t":' + t + ',"src":' + (t - ly.startTime) + ',"ax":' + a[0] + ',"ay":' + a[1] + '}');
      }
      var pre = [100, 100], fx = ly.property("Effects");
      for (var e = 1; e <= fx.numProperties; e++) if (fx.property(e).name === "Border out (Claude)")
        pre = [fx.property(e).property("ADBE Geometry2-0004").value, fx.property(e).property("ADBE Geometry2-0003").value];
      R.push('{"comp":"' + c.name + '","layer":' + PICK[p][1] + ',"file":"' + ly.source.mainSource.file.fsName.replace(/\\/g, "/") +
             '","pos":[' + pos[0] + ',' + pos[1] + '],"scale":' + sc[0] + ',"scaleY":' + sc[1] + ',"pre":[' + pre[0] + ',' + pre[1] + ']' +
             ',"samples":[' + smp.join(",") + ']}');
    }
  } catch (e) { err = e.toString(); }
  var f = new File(OUT); f.encoding = "UTF-8"; f.open("w");
  f.write(err ? '{"error":"' + err + '"}' : "[" + R.join(",") + "]"); f.close();
})();''' % (json.dumps(out_json.replace('\\', '/')), json.dumps(sel), N)
    open(out_jsx, 'w', encoding='utf-8').write(code)
    print('wrote', out_jsx, '(%d layers)' % len(sel))


def sheet(job, map_path, read_path, out_jpg):
    import cv2
    import numpy as np
    tr = json.load(open(os.path.join(job, 'track.json'), encoding='utf-8'))
    clip = {(m['comp'], m['layer']): m['clip'] for m in json.load(open(map_path, encoding='utf-8'))}
    R = json.load(open(read_path, encoding='utf-8'))

    def grab(path, t):
        raw = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', '%.4f' % t, '-i', path,
                              '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        return cv2.imdecode(np.frombuffer(raw, np.uint8), cv2.IMREAD_COLOR)

    blocks = []
    for L in R:
        t = tr[clip[(L['comp'], L['layer'])]]
        sx, sy, (px, py) = L['scale'] / 100.0, L.get('scaleY', L['scale']) / 100.0, L['pos']
        kx, ky = [v / 100.0 for v in L.get('pre', [100, 100])]
        W, H = t['W'], t['H']
        a0, n0 = L['samples'][0], t['nose'][0]
        lx, ly_ = W / 2 + kx * (n0[0] - W / 2), H / 2 + ky * (n0[1] - H / 2)   # nose in LAYER px
        cx, cy = px + (lx - a0['ax']) * sx, py + (ly_ - a0['ay']) * sy
        rows = [[], []]
        for smp in L['samples']:
            img = grab(L['file'], smp['src'])
            if (kx, ky) != (1.0, 1.0):      # the in-layer Transform effect: scale about the layer centre, clipped to the layer
                img = cv2.warpAffine(img, np.float32([[kx, 0, W / 2 * (1 - kx)], [0, ky, H / 2 * (1 - ky)]]), (W, H),
                                     flags=cv2.INTER_CUBIC)
            for r, (ax, ay) in enumerate([(smp['ax'], smp['ay']), (a0['ax'], a0['ay'])]):
                M = np.float32([[sx, 0, px - ax * sx], [0, sy, py - ay * sy]])
                comp = cv2.warpAffine(img, M, (FW, FH), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
                comp = cv2.copyMakeBorder(comp, C, C, C, C, cv2.BORDER_CONSTANT)
                x0, y0 = int(cx), int(cy)
                crop = comp[y0:y0 + 2 * C, x0:x0 + 2 * C].copy()
                cv2.line(crop, (C, 0), (C, 2 * C), (255, 0, 255), 1)
                cv2.line(crop, (0, C), (2 * C, C), (255, 0, 255), 1)
                crop = cv2.resize(crop, (200, 200))
                cv2.putText(crop, ('LOCK ' if r == 0 else 'raw ') + '%.2f' % smp['t'], (4, 16),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
                rows[r].append(crop)
        w = 200 * len(L['samples'])
        blocks.append(np.vstack([np.hstack(rows[0]), np.hstack(rows[1]), np.full((8, w, 3), 255, np.uint8)]))
    cv2.imwrite(out_jpg, np.vstack(blocks), [cv2.IMWRITE_JPEG_QUALITY, 88])
    print('wrote', out_jpg, '(%d layers)' % len(blocks))


if __name__ == '__main__':
    if sys.argv[1] == 'jsx':
        make_jsx(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6] if len(sys.argv) > 6 else None)
    else:
        sheet(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
