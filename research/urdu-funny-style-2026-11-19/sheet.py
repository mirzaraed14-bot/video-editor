import sys,subprocess,io
from PIL import Image,ImageDraw
vid,out,cols,tw=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
ts=[float(x) for x in sys.argv[5:]]
ims=[]
for t in ts:
    r=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',vid,'-frames:v','1','-vf',f'scale={tw}:-1','-f','image2pipe','-vcodec','png','-'],capture_output=True)
    try: im=Image.open(io.BytesIO(r.stdout)).convert('RGB')
    except Exception: im=Image.new('RGB',(tw,tw*9//16))
    d=ImageDraw.Draw(im); lab=f"{int(t//60)}:{t%60:05.2f}"
    d.rectangle([0,0,60,13],fill=(0,0,0)); d.text((2,1),lab,fill=(255,255,0))
    ims.append(im)
w,h=ims[0].size; rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(w*cols,h*rows))
for i,im in enumerate(ims): S.paste(im,((i%cols)*w,(i//cols)*h))
S.save(out)
print(out,S.size)
