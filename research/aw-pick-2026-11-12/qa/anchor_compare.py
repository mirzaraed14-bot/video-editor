"""1:1 face crops at 1080x1920 delivery scale: candidate finish tests vs the SOFTEST approved footage (Prince ABC panels in
the Son Short at ~25 s and ~32.5 s; Bieber's Oslo phone shot). Same method as projects/whitney-bobbi-last-day/qa_anchor_compare.py.
Usage: python anchor_compare.py <out.jpg> <label>=<file.mov>@<frame or t> ...   (frame numbers for ffv1/prores finish files)"""
import subprocess, pathlib, sys, cv2, tempfile
from PIL import Image, ImageDraw
EX = pathlib.Path('X:/Claude Projects/Exports'); tmp = pathlib.Path(tempfile.gettempdir())/'aw_anchor_a.png'
casc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def grab(f, t, frame=False):
    args = ['ffmpeg','-nostdin','-v','error','-y'] + (['-i',str(f),'-vf',f'select=eq(n\,{int(t)})','-vframes','1'] if frame else ['-ss',str(t),'-i',str(f),'-frames:v','1']) + [str(tmp)]
    subprocess.run(args, check=True); return cv2.imread(str(tmp))
def facecrop(img, label):
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); fs = casc.detectMultiScale(g, 1.1, 5, minSize=(60,60))
    if len(fs)==0: return None, label+' (no face found)'
    x,y,w,h = max(fs, key=lambda r:r[2]*r[3]); cx,cy = x+w//2, y+h//2
    x0 = min(max(cx-270,0), img.shape[1]-540); y0 = min(max(cy-270,0), img.shape[0]-540)
    return img[y0:y0+540, x0:x0+540], f'{label}  face {w}px'
items = [('APPROVED Son: Prince ABC panel', EX/"Why Michael Jackson's Son Had To Step Outside.mov", 25.0, False),
         ('APPROVED Son: Prince ABC full', EX/"Why Michael Jackson's Son Had To Step Outside.mov", 32.5, False),
         ('APPROVED Bieber: Oslo phone', EX/'Why Justin Bieber Walked Off His Own Stage.mov', 1.5, False)]
for a in sys.argv[2:]:
    lab, rest = a.split('=',1); f, t = rest.rsplit('@',1); items.append((lab, pathlib.Path(f), float(t), f.endswith('.mov') and '/finish' in f.replace(chr(92),'/')))
tiles=[]
for lab,f,t,fr in items:
    img = grab(f,t,fr); c,l = facecrop(img, lab)
    if c is None: c = cv2.resize(img,(540,int(540*img.shape[0]/img.shape[1])))[:540]
    im = Image.fromarray(cv2.cvtColor(c, cv2.COLOR_BGR2RGB)).resize((540,540)); d = ImageDraw.Draw(im); d.rectangle((0,0,540,22),fill='black'); d.text((6,5),l,fill='yellow'); tiles.append(im)
cols=3; rows=(len(tiles)+cols-1)//cols
sheet = Image.new('RGB',(540*cols,540*rows)); [sheet.paste(im,((k%cols)*540,(k//cols)*540)) for k,im in enumerate(tiles)]
sheet.save(sys.argv[1], quality=92); print('ok', len(tiles))
