#!/usr/bin/env python
"""Editable captions for a Premiere sequence the creator already cut: read the live sequence, rebuild
its voice on the sequence clock (for transcribe.sh), turn a hand-chunked captions.txt into a .srt, and
put it on the sequence as a caption track.

  python workflows/sequence-captions.py read   <job> "<Sequence name>"   # brief/tracks.txt + raw/<seq>-reference.mov
  bash .claude/skills/rough-cut/scripts/transcribe.sh <job>               # -> transcript/words.json (sequence clock)
  #  write <job>/captions.txt: one caption per line, words in transcript order
  python workflows/sequence-captions.py srt    <job> --max-words 3        # -> outputs/<seq>-captions.srt
  python workflows/sequence-captions.py import <job>                      # importFiles + createCaptionTrack

srt rules: the build FAILS past --max-words or on any word that doesn't match the transcript
(`f*cking` matches `fucking`; punctuation is ignored in the match). Wall-to-wall; a caption start
within -0.12/+0.05 s of a picture cut moves onto the cut; a shot with no speech gets no caption;
the last caption ends on the last clip; every boundary snaps to the sequence frame grid.
Premiere has no caption READ API: verify on screen (lanes/premiere/window-grab.ps1).
"""
import argparse, json, os, re, subprocess, sys, wave
import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIDGE = os.path.join(REPO, 'lanes', 'premiere', 'premiere-bridge.mjs')
TICKS = 254016000000


def es(script):
    r = subprocess.run(['node', BRIDGE, 'execute_extendscript', json.dumps({'script': script})],
                       capture_output=True, text=True, encoding='utf-8')
    d = json.loads(r.stdout)
    while isinstance(d, dict):
        d = d.get('result', d.get('data'))
    return d


def slug(name):
    return re.sub(r'[^a-z0-9]+', '', name.lower().replace('sequence', 'seq'))


def read(job, seq_name):
    js = r'''(function () {
      var seq = null;
      for (var s = 0; s < app.project.sequences.numSequences; s++)
        if (app.project.sequences[s].name === %s) seq = app.project.sequences[s];
      if (!seq) return "ERR no sequence";
      var L = [app.project.name, "FPS|" + (%d / seq.timebase)];
      function dump(tracks, tag) {
        for (var t = 0; t < tracks.numTracks; t++) for (var c = 0; c < tracks[t].clips.numItems; c++) {
          var cl = tracks[t].clips[c], mp = "";
          try { mp = cl.projectItem ? cl.projectItem.getMediaPath() : ""; } catch (e) {}
          L.push(tag + (t + 1) + "|" + cl.start.seconds + "|" + cl.end.seconds + "|" + cl.inPoint.seconds
                 + "|" + cl.outPoint.seconds + "|" + mp);
        }
      }
      dump(seq.videoTracks, "V"); dump(seq.audioTracks, "A");
      return L.join("\n");
    })()''' % (json.dumps(seq_name), TICKS)
    out = es(js)
    if not out or out.startswith('ERR'):
        sys.exit('read failed: %s' % out)
    lines = out.split('\n')
    os.makedirs(os.path.join(job, 'brief'), exist_ok=True)
    os.makedirs(os.path.join(job, 'raw'), exist_ok=True)
    open(os.path.join(job, 'brief', 'tracks.txt'), 'w', encoding='utf-8').write('\n'.join(lines[2:]) + '\n')
    fps = float(lines[1].split('|')[1])
    json.dump({'project': lines[0], 'sequence': seq_name, 'fps': fps},
              open(os.path.join(job, 'brief', 'sequence.json'), 'w', encoding='utf-8'), indent=1)

    a1 = sorted([l.split('|') for l in lines[2:] if l.startswith('A1|')], key=lambda r: float(r[1]))
    sr, audio = 48000, {}
    for src in {r[5] for r in a1}:                      # one decode per source; A1 may mix several
        pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vn', '-ac', '1', '-ar', str(sr),
                              '-f', 's16le', '-'], capture_output=True, check=True).stdout
        audio[src] = np.frombuffer(pcm, np.int16)
    segs, short, t_prev = [], [], 0.0
    for r in a1:
        st, en, sin = float(r[1]), float(r[2]), float(r[3])
        if st > t_prev + 1e-3:                          # a gap on A1 plays silence
            segs.append(np.zeros(int(round(st * sr)) - int(round(t_prev * sr)), np.int16))
        t_prev = en
        a = audio[r[5]]
        n, i0 = int(round(en * sr)) - int(round(st * sr)), int(round(sin * sr))
        seg = a[i0:i0 + n]
        if len(seg) < n:
            short.append('%.3f-%.3f (source %.3f s, file ends %.3f s)' % (st, en, sin, len(a) / sr))
            seg = np.concatenate([seg, np.zeros(n - len(seg), np.int16)])
        segs.append(seg)
    out_wav = os.path.join(job, 'raw', '_ref.wav')
    w = wave.open(out_wav, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes(np.concatenate(segs).tobytes()); w.close()
    ref = os.path.join(job, 'raw', slug(seq_name) + '-reference.mov')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', out_wav, '-c:a', 'pcm_s16le', ref], check=True)
    os.remove(out_wav)
    print('%s / %s: %d A1 clips, %.3f s at %g fps -> %s' % (lines[0], seq_name, len(a1), float(a1[-1][2]), fps, ref))
    for s in short:
        print('  ! A1 clip past the end of its media (plays silent): ' + s)


def norm(w):
    return re.sub(r'[^a-z0-9*]', '', w.lower())


def ts(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return '%02d:%02d:%02d,%03d' % (h, m, s, ms)


def corrected(words, out_path):
    """transcript-corrections.json + <job>/corrections.local.json, applied exactly as export-transcript.py does."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'export_transcript', os.path.join(REPO, '.claude', 'skills', 'rough-cut', 'scripts', 'export-transcript.py'))
    et = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(et)
    auto, flag = et.load_corrections(out_path, None)
    for w in words:
        w['w'], note = et.fix_word(w['w'], auto, flag)
        if note:
            print('  correction %s at %.2f s: %s' % (note[0], w['start'], ' -> '.join(note[1:])))
    return words


def srt(job, max_words):
    meta = json.load(open(os.path.join(job, 'brief', 'sequence.json'), encoding='utf-8'))
    fps = meta['fps']
    out = os.path.join(job, 'outputs', slug(meta['sequence']) + '-captions.srt')
    tw = json.load(open(os.path.join(job, 'transcript', 'words.json'), encoding='utf-8'))['clips'][0]['words']
    tw = corrected(tw, out)
    clips = [tuple(float(x) for x in l.split('|')[1:3])
             for l in open(os.path.join(job, 'brief', 'tracks.txt'), encoding='utf-8') if l.startswith('A1|')]
    end = max(b for _, b in clips)
    cuts = sorted({a for a, _ in clips} | {b for _, b in clips})
    silent = [(a, b) for a, b in clips if not any(a <= w['start'] < b for w in tw)]

    lines = [l.strip() for l in open(os.path.join(job, 'captions.txt'), encoding='utf-8')
             if l.strip() and not l.startswith('#')]
    caps, wi, over = [], 0, []
    for line in lines:
        parts = line.split()
        if len(parts) > max_words:
            over.append(line)
        chunk = tw[wi:wi + len(parts)]
        if len(chunk) < len(parts):
            sys.exit('ran past the transcript at: %s' % line)
        for p, t in zip(parts, chunk):
            a, b = norm(p), norm(t['w'])
            if a != b and not ('*' in a and re.fullmatch(a.replace('*', '.'), b)):
                sys.exit('MISMATCH %r vs transcript %r at %.2f s (line: %s)' % (p, t['w'], t['start'], line))
        caps.append({'start': chunk[0]['start'], 'last': chunk[-1]['end'], 'text': line})
        wi += len(parts)
    if over:
        sys.exit('over %d words:\n  %s' % (max_words, '\n  '.join(over)))
    if wi != len(tw):
        sys.exit('%d transcript words uncaptioned, from %r at %.2f s' % (len(tw) - wi, tw[wi]['w'], tw[wi]['start']))

    caps[0]['start'] = min(caps[0]['start'], cuts[0])
    for c in caps:
        near = [k for k in cuts if c['start'] - 0.12 <= k <= c['start'] + 0.05]
        if near:
            c['start'] = min(near, key=lambda k: abs(k - c['start']))
    for i, c in enumerate(caps):
        c['end'] = caps[i + 1]['start'] if i + 1 < len(caps) else end
        for a, b in silent:
            if c['last'] <= a < c['end']:
                c['end'] = a
    for c in caps:
        c['start'], c['end'] = round(c['start'] * fps) / fps, round(c['end'] * fps) / fps

    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8-sig').write(
        '\n'.join('%d\n%s --> %s\n%s\n' % (i, ts(c['start']), ts(c['end']), c['text']) for i, c in enumerate(caps, 1)))
    lens = sorted(c['end'] - c['start'] for c in caps)
    n = [len(c['text'].split()) for c in caps]
    print('%d captions -> %s' % (len(caps), out))
    print('words/caption: max %d, mean %.2f | seconds: min %.2f median %.2f max %.2f'
          % (max(n), sum(n) / len(n), lens[0], lens[len(lens) // 2], lens[-1]))
    if silent:
        print('silent shots left uncaptioned: ' + ', '.join('%.3f-%.3f' % s for s in silent))
    for c in caps:
        print('  %6.3f-%6.3f  %s' % (c['start'], c['end'], c['text']))


def import_(job):
    meta = json.load(open(os.path.join(job, 'brief', 'sequence.json'), encoding='utf-8'))
    path = os.path.abspath(os.path.join(job, 'outputs', slug(meta['sequence']) + '-captions.srt')).replace('\\', '/')
    js = r'''(function () {
      var PATH = %s, SEQ = %s, PROJ = %s, log = [];
      if (app.project.name !== PROJ) return "open project is " + app.project.name + ", expected " + PROJ + ": stopped";
      var seq = null;
      for (var s = 0; s < app.project.sequences.numSequences; s++)
        if (app.project.sequences[s].name === SEQ) seq = app.project.sequences[s];
      if (!seq) return "sequence not found";
      app.project.activeSequence = seq;
      var sep = String.fromCharCode(92);
      function norm(p) { return (p || "").toLowerCase().split(sep).join("/"); }
      var item = null;
      function walk(bin) {
        for (var i = 0; i < bin.children.numItems; i++) {
          var it = bin.children[i];
          if (it.type === 2) { walk(it); continue; }
          var mp = ""; try { mp = it.getMediaPath(); } catch (e) {}
          if (norm(mp) === norm(PATH)) item = it;
        }
      }
      walk(app.project.rootItem);
      if (item) log.push("srt already in project");
      else { log.push("import " + app.project.importFiles([PATH], true, app.project.rootItem, false)); walk(app.project.rootItem); }
      if (!item) return log.join(" | ") + " | SRT IMPORT FAILED";
      try { log.push("createCaptionTrack " + seq.createCaptionTrack(item, 0)); }
      catch (e) { log.push("createCaptionTrack threw " + e); }
      return SEQ + " | " + log.join(" | ");
    })()''' % (json.dumps(path), json.dumps(meta['sequence']), json.dumps(meta['project']))
    print(es(js))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['read', 'srt', 'import'])
    ap.add_argument('job')
    ap.add_argument('sequence', nargs='?')
    ap.add_argument('--max-words', type=int, default=3)
    a = ap.parse_args()
    if a.cmd == 'read':
        read(a.job, a.sequence or sys.exit('read needs the sequence name'))
    elif a.cmd == 'srt':
        srt(a.job, a.max_words)
    else:
        import_(a.job)
