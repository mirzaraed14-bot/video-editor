#!/usr/bin/env python3
"""Read-only dialogue dead-air gate, independent of music and no_refine pins.
Usage: uv run workflows/dead-air-qa.py projects/JOB [--cuts PATH] [--json PATH]
Flags >=0.65s quiet runs using 10ms RMS and a speech-relative threshold.
Bridges isolated <40ms noise spikes; never changes cuts automatically.
"""
import argparse,array,json,math,subprocess
from pathlib import Path
HOP=.01

def quiet_mask(values,floor):
    peak=max(values)
    threshold=max(peak-28,min(floor+14,peak-18))
    mask=[v<threshold for v in values];i=0
    while i<len(mask):
        if mask[i]:i+=1;continue
        j=i
        while j<len(mask) and not mask[j]:j+=1
        if i>0 and j<len(mask) and j-i<4:mask[i:j]=[True]*(j-i)
        i=j
    return mask,threshold

def quiet_runs(mask):
    i=0
    while i<len(mask):
        if not mask[i]:i+=1;continue
        j=i
        while j<len(mask) and mask[j]:j+=1
        if (j-i)*HOP>=.65:yield i,j
        i=j

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('job',type=Path);ap.add_argument('--cuts',type=Path);ap.add_argument('--json',type=Path);args=ap.parse_args()
    cuts=json.loads((args.cuts or args.job/'transcript/cuts.json').read_text())['segments'];cache={};findings=[];timeline=0;allmask=[];times=[]
    for index,c in enumerate(cuts):
        path=args.job/'raw'/Path(c['clip']).name
        if path not in cache:
            r=subprocess.run(['ffmpeg','-v','error','-i',str(path),'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True)
            pcm=array.array('h',r.stdout);hop=160
            envelope=[20*math.log10(math.sqrt(sum(x*x for x in pcm[i:i+hop])/len(pcm[i:i+hop]))/32768+1e-9) for i in range(0,len(pcm),hop)]
            cache[path]=(envelope,sorted(envelope)[len(envelope)//10])
        a=round(c['start']/HOP);b=round(c['end']/HOP);envelope,floor=cache[path];values=envelope[a:b]
        if values:
            mask,threshold=quiet_mask(values,floor)
            allmask.extend(mask);times.extend((timeline+k*HOP,index,c['start']+k*HOP,threshold) for k in range(len(mask)))
        timeline+=c['end']-c['start']
    for i,j in quiet_runs(allmask):
        t,seg,source,thr=times[i];end=times[j-1][0]+HOP
        findings.append(dict(start=round(t,3),end=round(end,3),duration=round(end-t,3),segment=seg,source_start=round(source,3),threshold_db=round(thr,1)))
    report={'duration':timeline,'segments':len(cuts),'dead_air':findings,'passed':not findings}
    if args.json:args.json.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2));return bool(findings)
if __name__=='__main__':raise SystemExit(main())
