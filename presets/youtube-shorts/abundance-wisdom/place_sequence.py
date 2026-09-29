#!/usr/bin/env python
"""placement.json -> an ExtendScript that lays the cut onto an EMPTY Premiere sequence.

Per row: set the project item's in/out (out over-trimmed 0.2 s, because Premiere quantises to the
SOURCE frame grid), overwriteClip onto V1 (linked audio lands on A1), then pin both the video and
the audio item's end to the planned frame, and set Motion scale/position. A head row and the 'join'
rows after it (a camera cut inside one continuous source) are laid as ONE clip and razored (QE) at
each join, so the audio stays continuous. 'track': 2 rows (covers) go on V2, picture only: their
linked audio is removed. Afterwards the project items' in/out marks are cleared again and one
sequence marker per beat is written.
Refuses to run on a sequence that already has clips — it never overwrites the creator's work.

usage: python place_sequence.py <job_dir> <sequence name> <bin name> <out.jsx> [extra_import_path ...]
"""
import json, os, sys


def js(v):
    return json.dumps(v, ensure_ascii=False)


def main(job, seq_name, bin_name, out_jsx, extra):
    plan = json.load(open(os.path.join(job, 'placement.json'), encoding='utf-8'))
    rows = [[r['source'].replace('/', '\\'), r['src_in'], r['src_out'], r['tl_in'], r['tl_out'],
             r['scale'], r['pos'][0], r['pos'][1],
             ('B%d.cover%d' if r.get('track') == 2 else 'B%d.%d.%d') % (
                 (r['beat'], r['piece']) if r.get('track') == 2 else (r['beat'], r['seg'], r['piece'])),
             r.get('track', 1), bool(r.get('join')), r.get('cut'), r.get('to_src')]
            for r in plan['rows']]
    marks = [[m['t'], m['name'], m['comment']] for m in plan['markers']]
    imports = [p.replace('/', '\\') for p in extra]
    code = r'''(function () {
var SEQ = %s, BIN = %s, ROWS = %s, MARKS = %s, IMPORTS = %s;
var log = [];
try {
  var sep = String.fromCharCode(92);
  function norm(p) { return (p || "").toLowerCase().split(sep).join("/"); }
  function findBin(b, name) {
    for (var i = 0; i < b.children.numItems; i++) {
      var it = b.children[i];
      if (it.type === 2) { if (it.name === name) return it; var r = findBin(it, name); if (r) return r; }
    }
    return null;
  }
  var items = {};
  function index(b) {
    for (var i = 0; i < b.children.numItems; i++) {
      var it = b.children[i];
      if (it.type === 2) { index(it); continue; }
      var mp = ""; try { mp = it.getMediaPath(); } catch (e) {}
      if (mp) items[norm(mp)] = it;
    }
  }
  var seq = null;
  for (var s = 0; s < app.project.sequences.numSequences; s++) if (app.project.sequences[s].name === SEQ) seq = app.project.sequences[s];
  if (!seq) return "sequence not found: " + SEQ;
  var existing = 0;
  for (var t = 0; t < seq.videoTracks.numTracks; t++) existing += seq.videoTracks[t].clips.numItems;
  for (var a = 0; a < seq.audioTracks.numTracks; a++) existing += seq.audioTracks[a].clips.numItems;
  if (existing > 0) return "REFUSED: " + SEQ + " already has " + existing + " clip(s)";
  app.project.openSequence(seq.sequenceID);
  app.project.activeSequence = seq;

  var bin = findBin(app.project.rootItem, BIN) || app.project.rootItem;
  index(app.project.rootItem);
  for (var m = 0; m < IMPORTS.length; m++) {
    if (!items[norm(IMPORTS[m])]) {
      log.push("import " + IMPORTS[m].split(sep).pop() + ": " + app.project.importFiles([IMPORTS[m]], true, bin, false));
    }
  }
  index(app.project.rootItem);

  var vt = seq.videoTracks[0], at = seq.audioTracks[0];
  function mkTime(sec) { var x = new Time(); x.seconds = sec; return x; }
  function clipAt(track, sec) {
    for (var c = 0; c < track.clips.numItems; c++) if (Math.abs(track.clips[c].start.seconds - sec) < 0.01) return track.clips[c];
    return null;
  }
  function comp(clip, name) {
    for (var k = 0; k < clip.components.numItems; k++) if (clip.components[k].displayName === name) return clip.components[k];
    return null;
  }
  function prop(cmp, name) {
    for (var p = 0; p < cmp.properties.numItems; p++) if (cmp.properties[p].displayName === name) return cmp.properties[p];
    return null;
  }
  var used = {};
  function motion(clip, R) {
    var mo = clip ? comp(clip, "Motion") : null;
    if (mo) { prop(mo, "Scale").setValue(R[5], true); prop(mo, "Position").setValue([R[6], R[7]], true); }
    return !!mo;
  }
  function lay(track, R, last) {             // one overwrite from R's in to last's out, ends pinned
    var item = items[norm(R[0])];
    if (!item) { log.push(R[8] + " MISSING SOURCE " + R[0]); return false; }
    item.setInPoint(R[1], 4);
    item.setOutPoint(last[2] + 0.2, 4);
    track.overwriteClip(item, R[3]);
    used[norm(R[0])] = item;
    return true;
  }
  // 1. covers (picture-only V2 inserts) FIRST: if the linked audio lands on A1 instead of A2, the
  //    dialogue laid next overwrites it; whatever lands on A2 under a cover is removed afterwards.
  var covers = [];
  for (var r = 0; r < ROWS.length; r++) if (ROWS[r][9] === 2) covers.push(ROWS[r]);
  if (covers.length && (seq.videoTracks.numTracks < 2 || seq.audioTracks.numTracks < 2)) return "REFUSED: covers need V2 and A2";
  for (var c0 = 0; c0 < covers.length; c0++) {
    var C = covers[c0];
    if (!lay(seq.videoTracks[1], C, C)) continue;
    var cv = clipAt(seq.videoTracks[1], C[3]);
    if (cv) { cv.end = mkTime(C[4]); motion(cv, C); }
    log.push(C[8] + " @" + C[3].toFixed(2) + " on V2" + (cv ? "" : " NO-VIDEO"));
  }
  // 2. V1 runs: a head row plus the 'join' rows after it is ONE continuous clip, laid once and then
  //    razored at each join (one shared boundary, audio sample-continuous, no in-point flooring).
  var runs = [];
  for (var r2 = 0; r2 < ROWS.length; r2++) {
    if (ROWS[r2][9] === 2) continue;
    if (ROWS[r2][10] && runs.length) runs[runs.length - 1].push(ROWS[r2]); else runs.push([ROWS[r2]]);
  }
  var joins = [], startOf = {}, runInfo = [];
  var fps = 254016000000 / parseInt(seq.timebase, 10);
  for (var q0 = 0; q0 < runs.length; q0++) {
    var H = runs[q0][0], Z = runs[q0][runs[q0].length - 1];
    if (!lay(vt, H, Z)) continue;
    var v = clipAt(vt, H[3]), au = clipAt(at, H[3]);
    if (v) v.end = mkTime(Z[4]);
    if (au) au.end = mkTime(Z[4]);
    // Premiere floors the in-point (to the SEQUENCE grid on a 60 fps timeline, 2026-09-29), so the
    // razor frame comes from the in-point it actually took: the first frame whose source time
    // reaches the camera cut. A plan-time guess put two razors 4-5 ms before their cuts.
    var ain = v ? v.inPoint.seconds : H[1];
    runInfo.push([H[3], Z[4], ain]);
    for (var j0 = 1; j0 < runs[q0].length; j0++) {
      var JR = runs[q0][j0];
      var jt = JR[11] !== null ? H[3] + Math.ceil((JR[11] - ain) * fps - 1e-6) / fps : JR[3];
      joins.push([JR, jt]); startOf[JR[8] + "@" + JR[3]] = jt;
    }
    log.push(H[8] + " @" + H[3].toFixed(2) + (runs[q0].length > 1 ? " (+" + (runs[q0].length - 1) + " razor)" : "")
             + (v ? "" : " NO-VIDEO") + (au ? "" : " NO-AUDIO"));
  }
  if (joins.length) {
    app.enableQE();
    var qs = qe.project.getActiveSequence();
    if (!qs || qs.name !== SEQ) { log.push("ERROR QE sequence is " + (qs ? qs.name : "none") + ", not " + SEQ); }
    else {
      if (Math.abs(fps - Math.round(fps)) > 1e-6) { log.push("ERROR razor needs an integer-fps sequence (lab-notes: fractional timecode cuts late); " + fps); joins = []; }
      function tc(sec) {
        var f = Math.round(sec * fps), ff = f %% fps, s = (f - ff) / fps;
        function p(n) { return (n < 10 ? "0" : "") + n; }
        return p(Math.floor(s / 3600)) + ":" + p(Math.floor(s / 60) %% 60) + ":" + p(s %% 60) + ":" + p(ff);
      }
      for (var j1 = 0; j1 < joins.length; j1++) {
        qs.getVideoTrackAt(0).razor(tc(joins[j1][1]));
        qs.getAudioTrackAt(0).razor(tc(joins[j1][1]));
        if (Math.abs(joins[j1][1] - joins[j1][0][3]) > 1e-3)
          log.push(joins[j1][0][8] + " razor at " + joins[j1][1].toFixed(4) + " (plan " + joins[j1][0][3].toFixed(4) + ")");
      }
    }
  }
  for (var r3 = 0; r3 < ROWS.length; r3++) {
    if (ROWS[r3][9] === 2) continue;
    var st = startOf[ROWS[r3][8] + "@" + ROWS[r3][3]];
    var pv = clipAt(vt, st === undefined ? ROWS[r3][3] : st);
    if (!motion(pv, ROWS[r3])) log.push(ROWS[r3][8] + " NO CLIP AT " + ROWS[r3][3].toFixed(3) + " (razor missed?)");
  }
  // 3. a cover that ends on a source time of the footage under it ('to_src', e.g. the podcast's own
  //    cut) is re-pinned from that footage's ACTUAL in-point, like the razors, so the covered shot
  //    never shows through for a frame.
  for (var c3 = 0; c3 < covers.length; c3++) {
    var CR = covers[c3];
    if (CR[12] === null) continue;
    for (var ri = 0; ri < runInfo.length; ri++) {
      if (CR[4] < runInfo[ri][0] - 1e-3 || CR[4] > runInfo[ri][1] + 1e-3) continue;
      var ce = runInfo[ri][0] + Math.ceil((CR[12] - runInfo[ri][2]) * fps - 1e-6) / fps;
      var cvc = clipAt(seq.videoTracks[1], CR[3]);
      if (cvc && Math.abs(ce - CR[4]) > 1e-3) { cvc.end = mkTime(ce); log.push(CR[8] + " end re-pinned to " + ce.toFixed(4) + " (plan " + CR[4].toFixed(4) + ")"); }
      break;
    }
  }
  // 4. the covers' own audio: removed from A2 (picture only)
  if (covers.length) {
    var a2 = seq.audioTracks[1];
    for (var c1 = a2.clips.numItems - 1; c1 >= 0; c1--) {
      var ac2 = a2.clips[c1];
      for (var c2 = 0; c2 < covers.length; c2++)
        if (Math.abs(ac2.start.seconds - covers[c2][3]) < 0.01) { ac2.remove(false, false); log.push(covers[c2][8] + " audio removed from A2"); break; }
    }
  }
  for (var u in used) { try { used[u].clearInPoint(); used[u].clearOutPoint(); } catch (e) {} }
  for (var q = 0; q < MARKS.length; q++) {
    var mk = seq.markers.createMarker(MARKS[q][0]);
    mk.name = MARKS[q][1]; mk.comments = MARKS[q][2];
  }
  var vc = [], ac = 0;
  for (var z = 0; z < vt.clips.numItems; z++) vc.push(vt.clips[z].start.seconds.toFixed(3) + "-" + vt.clips[z].end.seconds.toFixed(3));
  ac = at.clips.numItems;
  log.push("V1 clips " + vt.clips.numItems + " | A1 clips " + ac + " | markers " + MARKS.length
           + (covers.length ? " | V2 clips " + seq.videoTracks[1].clips.numItems + " | A2 clips " + seq.audioTracks[1].clips.numItems : ""));
  log.push("V1 spans: " + vc.join(" "));
} catch (err) { log.push("ERROR " + err.toString() + (err.line ? " line " + err.line : "")); }
return log.join("\n");
})()''' % (js(seq_name), js(bin_name), js(rows), js(marks), js(imports))
    open(out_jsx, 'w', encoding='utf-8').write(code)
    print('wrote', out_jsx, '(%d rows, %d markers)' % (len(rows), len(marks)))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
