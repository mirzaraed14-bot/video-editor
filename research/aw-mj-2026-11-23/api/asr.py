"""Windowed CPU ASR under the machine-wide .asr-lock (silent). Run with the whisperx venv python."""
import ctypes, json, os, subprocess, sys, time
REPO = r"X:\Claude Projects\video-editor-client\video-editor"
LOCK = os.path.join(REPO, 'projects', '_onyx-batch9-2026-11', 'reactions', '.asr-lock')
OUT = os.path.join(REPO, 'research', 'aw-mj-2026-11-23', 'asr')
H = r"E:\Bullshit Folder\Henry"
WIN = [
 ('birth', 'X:/Claude Projects/video-editor-client/video-editor/research/aw-mj-2026-11-23/dl/PWbbycMFC9U.mp4', 0.0, 25.0),
]
DONE2 = [
 ('bashir_p11', H + r"\LIVING WITH MICHAEL JACKSON PART 11 4K Upscale.mp4", 0.0, 278.0),
 ('bashir_p15', H + r"\LIVING WITH MICHAEL JACKSON PART 15 4K Upscale.mp4", 0.0, 299.5),
 ('bashir_p16', H + r"\LIVING WITH MICHAEL JACKSON PART 16 4K Upscale.mp4", 0.0, 269.5),
]
DONE = [
 ('daddy', REPO + r"\research\aw-mj-2026-11-23\dl\GIUcLQE9fUQ.mp4", 0.0, 18.7),
 ('reading', REPO + r"\research\aw-mj-2026-11-23\dl\2TLt2Ko2Kj4.mp4", 0.0, 71.9),
]
OLDWIN = [
 ('oprah_dontknow', H + r"\Michael Jackson - OPRAH WINFREY Interview (1993) 4K 50FPS UPSCALE.mp4", 1080.0, 1115.0),
 ('hotbox_daddy', H + r"\Prince Jackson, Philanthropist and Producer - Hotboxin' with Mike Tyson.mp4", 2835.0, 2868.0),
 ('sunrise_roof', REPO + r"\projects\mj-son-red-armband\sources\uNF0GMRPO1w\uNF0GMRPO1w.mp4", 138.0, 168.0),
 ('kiis_toys', H + "\Prince Jackson Opens Up_ Michael Jackson\u2019s Legacy, the Michael Movie _ Moments Fans Never Knew.mp4", 1430.0, 1452.0),
]
def free_gb():
    class MS(ctypes.Structure):
        _fields_ = [('l', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [(n, ctypes.c_ulonglong) for n in ('tp','ap','tpf','apf','tv','av','aev')]
    m = MS(); m.l = ctypes.sizeof(MS); ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)); return m.ap / 2**30
if free_gb() < 4.0: sys.exit('free RAM %.1f GB < 4: not running' % free_gb())
os.makedirs(OUT, exist_ok=True)
wavs = []
for n, f, a, b in WIN:
    w = os.path.join(OUT, n + '.16k.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-t', str(b - a), '-i', f, '-ac', '1', '-ar', '16000', w], check=True)
    wavs.append((n, w, a))
t = time.time()
while True:
    try: os.makedirs(LOCK); break
    except FileExistsError:
        if time.time() - t > 900: sys.exit('.asr-lock held > 900 s')
        time.sleep(5)
try:
    open(os.path.join(LOCK, 'owner'), 'w').write('mj-short research %s' % time.strftime('%F %T'))
    from faster_whisper import WhisperModel
    m = WhisperModel('medium.en', device='cpu', compute_type='int8', cpu_threads=4)
    for n, w, a in wavs:
        segs, _ = m.transcribe(w, language='en', word_timestamps=True, beam_size=5, condition_on_previous_text=False)
        words, lines = [], []
        for s in segs:
            lines.append('%8.2f %8.2f %s' % (s.start + a, s.end + a, s.text.strip()))
            for x in (s.words or []): words.append({'w': x.word.strip(), 's': round(x.start + a, 3), 'e': round(x.end + a, 3), 'p': round(x.probability, 3)})
        json.dump(words, open(os.path.join(OUT, n + '.medium.words.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        open(os.path.join(OUT, n + '.medium.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        print('== ' + n); print('\n'.join(lines))
finally:
    try: os.remove(os.path.join(LOCK, 'owner'))
    except OSError: pass
    os.rmdir(LOCK)
