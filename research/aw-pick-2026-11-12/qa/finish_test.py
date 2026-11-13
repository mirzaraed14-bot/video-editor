"""Anchor-test finish for an AW pick (12 Nov), the Son ABC recipe, as in projects/whitney-bobbi-last-day/qa_finish_test.py:
9:16 face crop -> 1080x1920 (Stage A equivalent) -> Iris 1.0 -> Proteus 1x (prob-4 details 0.6 blur 0.6). 2 s window.
Usage: python finish_test.py <src> <t0> <outdir> [crop_w_override]
Runs Topaz on the GPU: call it under lock.sh gpu. Nothing is played."""
import importlib.util, os, subprocess, tempfile, pathlib, sys, cv2
REPO = pathlib.Path('X:/Claude Projects/video-editor-client/video-editor')
spec = importlib.util.spec_from_file_location('tz', str(REPO/'workflows'/'topaz-iris.py')); tz = importlib.util.module_from_spec(spec); spec.loader.exec_module(tz)
env = dict(os.environ, TVAI_MODEL_DATA_DIR=tz.MODELS, TVAI_MODEL_DIR=tz.MODELS)
src = pathlib.Path(sys.argv[1]); t0 = float(sys.argv[2]); out = pathlib.Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
probe = subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',str(src)],capture_output=True,text=True).stdout.strip().split(',')
W,H = int(probe[0]), int(probe[1])
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(t0+1),'-i',str(src),'-frames:v','1',str(out/'f.png')],check=True)
img = cv2.imread(str(out/'f.png')); g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
casc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
fs = casc.detectMultiScale(g, 1.1, 5, minSize=(40,40))
cx = (max(fs, key=lambda r:r[2]*r[3])[0] + max(fs, key=lambda r:r[2]*r[3])[2]//2) if len(fs) else W//2
cw = int(sys.argv[4]) if len(sys.argv)>4 else int(round(H*9/16/2)*2)
x0 = min(max(cx-cw//2,0), W-cw)
print('src', W, 'x', H, 'faces', [tuple(f) for f in fs][:3], 'crop w', cw, 'x0', x0)
stageA = out/'stageA.mov'
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(t0),'-i',str(src),'-t','2','-an','-vf',f'crop={cw}:{H}:{x0}:0,scale=1080:1920:flags=lanczos','-c:v','ffv1',str(stageA)],check=True)
PROT = ("tvai_up=model=prob-4:scale=0:w=1080:h=1920:preblur=0:noise=0:details=0.6:halo=0:blur=0.6:compression=0:device=0:vram=1:instances=1,scale=out_color_matrix=bt709")
tz.enhance(str(stageA), str(out/'iris.mov'), 1.0, False, True, env, tempfile.gettempdir(), iris=True, mult=1)
r = subprocess.run([tz.TFFMPEG,'-hide_banner','-nostdin','-y','-nostats','-i',str(out/'iris.mov'),'-filter_complex',PROT,'-an','-c:v','prores_ks','-profile:v','3','-pix_fmt','yuv422p10le',str(out/'iris_prot.mov')],env=env,capture_output=True,text=True)
print('proteus rc', r.returncode, r.stderr[-300:] if r.returncode else '')
