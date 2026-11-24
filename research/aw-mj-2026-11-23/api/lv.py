import subprocess,sys,numpy as np
f,a,b=sys.argv[1],float(sys.argv[2]),float(sys.argv[3])
raw=subprocess.run(['ffmpeg','-v','error','-ss',str(a),'-t',str(b-a),'-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
x=np.frombuffer(raw,dtype=np.float32)
n=800; fr=x[:len(x)//n*n].reshape(-1,n); db=20*np.log10(np.sqrt((fr**2).mean(1))+1e-9)
ii=subprocess.run(['ffmpeg','-v','info','-ss',str(a),'-t',str(b-a),'-i',f,'-af','ebur128','-f','null','-'],capture_output=True,text=True,encoding='utf-8',errors='replace').stderr
I=[l for l in ii.splitlines() if l.strip().startswith('I:')][-1].strip()
print('%-10s %7.1f-%7.1f  %s  p5 %.1f  p50 %.1f  p90 %.1f  spread(p90-p5) %.1f dB'%(sys.argv[4] if len(sys.argv)>4 else '',a,b,I,np.percentile(db,5),np.percentile(db,50),np.percentile(db,90),np.percentile(db,90)-np.percentile(db,5)))
