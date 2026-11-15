"""CPU ASR of a long podcast to locate a passage. usage: python -I asr_find.py <audio> <model> <out.txt> [start_s] [end_s]"""
import sys, subprocess, numpy as np, whisperx
src, model, out = sys.argv[1], sys.argv[2], sys.argv[3]
ss = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
to = float(sys.argv[5]) if len(sys.argv) > 5 else None
cmd = ['ffmpeg', '-v', 'error', '-ss', str(ss)] + (['-to', str(to)] if to else []) + ['-i', src, '-vn', '-ac', '1', '-ar', '16000', '-f', 's16le', '-']
x = np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.int16).astype(np.float32) / 32768
m = whisperx.load_model(model, 'cpu', compute_type='int8', language='en')
r = m.transcribe(x, batch_size=8, language='en')
with open(out, 'w', encoding='utf-8') as f:
    for s in r['segments']:
        f.write('%8.2f-%8.2f %s\n' % (s['start'] + ss, s['end'] + ss, s['text'].strip()))
print('done', len(r['segments']))
