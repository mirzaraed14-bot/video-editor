"""Anchor-test finish (PITCH-CHECKLIST 2): the Son build's ABC recipe on a 2 s window, as Whitney's qa_finish_test.py did.
9:16 crop around the chosen face -> 1080x1920 lanczos (stage A) -> Iris 1.0 -> Proteus prob-4 (details 0.6, blur 0.6).
usage (under the GPU lock): python -I finish_test.py <src> <t0> <out_dir> [left|right|largest]
"""
import importlib.util, os, subprocess, tempfile, pathlib, sys
import cv2, numpy as np

REPO = pathlib.Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('tz', str(REPO / 'workflows' / 'topaz-iris.py'))
tz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tz)
env = dict(os.environ, TVAI_MODEL_DATA_DIR=tz.MODELS, TVAI_MODEL_DIR=tz.MODELS)

src, t0, out = sys.argv[1], float(sys.argv[2]), pathlib.Path(sys.argv[3])
pick = sys.argv[4] if len(sys.argv) > 4 else 'largest'
out.mkdir(parents=True, exist_ok=True)

png = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', str(t0 + 1), '-i', src, '-frames:v', '1', '-f', 'image2pipe',
                      '-vcodec', 'png', '-'], capture_output=True).stdout
img = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_COLOR)
H, W = img.shape[:2]
det = cv2.FaceDetectorYN_create(str(REPO / 'assets' / 'models' / 'face_detection_yunet_2023mar.onnx'), '', (W, H),
                                score_threshold=0.6)
_, faces = det.detect(img)
if pick.startswith('x='):                      # an explicit crop centre (profiles the detector can't see, e.g. the hug)
    f, cx = [int(pick[2:]) - 1, 0, 2, 0], int(pick[2:])
else:
    fs = sorted([f[:4] for f in faces], key=lambda r: r[0])
    f = fs[0] if pick == 'left' else fs[-1] if pick == 'right' else max(fs, key=lambda r: r[2] * r[3])
    cx = int(f[0] + f[2] / 2)
cw = int(round(H * 9 / 16 / 2)) * 2
x0 = min(max(cx - cw // 2, 0), W - cw)
print('face', [int(v) for v in f], 'crop', cw, 'x', x0)
stageA = out / 'stageA.mov'
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', str(t0), '-i', src, '-t', '2', '-an', '-vf',
                f'crop={cw}:{H}:{x0}:0,scale=1080:1920:flags=lanczos', '-c:v', 'ffv1', str(stageA)], check=True)
PROT = ("tvai_up=model=prob-4:scale=0:w=1080:h=1920:preblur=0:noise=0:details=0.6:halo=0:blur=0.6:compression=0:device=0:"
        "vram=1:instances=1,scale=out_color_matrix=bt709")
tz.enhance(str(stageA), str(out / 'iris.mov'), 1.0, False, True, env, tempfile.gettempdir(), iris=True, mult=1)
r = subprocess.run([tz.TFFMPEG, '-hide_banner', '-nostdin', '-y', '-nostats', '-i', str(out / 'iris.mov'), '-filter_complex', PROT,
                    '-an', '-c:v', 'prores_ks', '-profile:v', '3', '-pix_fmt', 'yuv422p10le', str(out / 'iris_prot.mov')],
                   env=env, capture_output=True, text=True)
print('proteus rc', r.returncode, r.stderr[-300:] if r.returncode else '')
