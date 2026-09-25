#!/usr/bin/env python
"""placement.json -> an ExtendScript that lays the cut onto an EMPTY Premiere sequence.

Per row: set the project item's in/out (out over-trimmed 0.2 s, because Premiere quantises to the
SOURCE frame grid), overwriteClip onto V1 (linked audio lands on A1), then pin both the video and
the audio item's end to the planned frame, and set Motion scale/position. Afterwards the project
items' in/out marks are cleared again and one sequence marker per beat is written.
Refuses to run on a sequence that already has clips — it never overwrites the creator's work.

usage: python place_sequence.py <job_dir> <sequence name> <bin name> <out.jsx> [extra_import_path ...]
"""
import json, os, sys


def js(v):
    return json.dumps(v, ensure_ascii=False)


def main(job, seq_name, bin_name, out_jsx, extra):
    plan = json.load(open(os.path.join(job, 'placement.json'), encoding='utf-8'))
    rows = [[r['source'].replace('/', '\\'), r['src_in'], r['src_out'], r['tl_in'], r['tl_out'],
             r['scale'], r['pos'][0], r['pos'][1], 'B%d.%d.%d' % (r['beat'], r['seg'], r['piece'])]
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
  for (var r = 0; r < ROWS.length; r++) {
    var R = ROWS[r];
    var item = items[norm(R[0])];
    if (!item) { log.push(R[8] + " MISSING SOURCE " + R[0]); continue; }
    item.setInPoint(R[1], 4);
    item.setOutPoint(R[2] + 0.2, 4);
    vt.overwriteClip(item, R[3]);
    used[norm(R[0])] = item;
    var v = clipAt(vt, R[3]), au = clipAt(at, R[3]);
    if (v) v.end = mkTime(R[4]);
    if (au) au.end = mkTime(R[4]);
    if (v) {
      var mo = comp(v, "Motion");
      if (mo) { prop(mo, "Scale").setValue(R[5], true); prop(mo, "Position").setValue([R[6], R[7]], true); }
    }
    log.push(R[8] + " @" + R[3].toFixed(2) + (v ? "" : " NO-VIDEO") + (au ? "" : " NO-AUDIO"));
  }
  for (var u in used) { try { used[u].clearInPoint(); used[u].clearOutPoint(); } catch (e) {} }
  for (var q = 0; q < MARKS.length; q++) {
    var mk = seq.markers.createMarker(MARKS[q][0]);
    mk.name = MARKS[q][1]; mk.comments = MARKS[q][2];
  }
  var vc = [], ac = 0;
  for (var z = 0; z < vt.clips.numItems; z++) vc.push(vt.clips[z].start.seconds.toFixed(3) + "-" + vt.clips[z].end.seconds.toFixed(3));
  ac = at.clips.numItems;
  log.push("V1 clips " + vt.clips.numItems + " | A1 clips " + ac + " | markers " + MARKS.length);
  log.push("V1 spans: " + vc.join(" "));
} catch (err) { log.push("ERROR " + err.toString() + (err.line ? " line " + err.line : "")); }
return log.join("\n");
})()''' % (js(seq_name), js(bin_name), js(rows), js(marks), js(imports))
    open(out_jsx, 'w', encoding='utf-8').write(code)
    print('wrote', out_jsx, '(%d rows, %d markers)' % (len(rows), len(marks)))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
