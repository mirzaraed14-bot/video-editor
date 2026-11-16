"""Fit the glow to the reference halo: composite one cue over a flat L=40 plate, measure the luminance excess by distance from the ink."""
import json, sys, numpy as np
from PIL import Image
from scipy import ndimage
f=sys.argv[1]
cap=np.array(Image.open(f)).astype(float)/255
a=cap[...,3:4]; rgb=cap[...,:3]
plate=np.full(rgb.shape,40/255)
comp=rgb*a+plate*(1-a)   # screenshot PNGs are straight alpha
L=(0.299*comp[...,0]+0.587*comp[...,1]+0.114*comp[...,2])*255
core=cap[...,3]>0.8
d=ndimage.distance_transform_edt(~core)
out=[]
for r in [4,8,12,16,20,24,28]:
    m=(d>r-1)&(d<=r+1); out.append(f"d{r}:{L[m].mean()-40:.1f}")
print(' '.join(out), '| core L', round(L[core].mean(),1))
