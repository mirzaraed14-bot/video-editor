// Paste into javascript_tool on a /reel/<code>/ page. Mutes, then reads ONLY the first reel's action bar + og:description.
const mute=()=>document.querySelectorAll('video,audio').forEach(v=>{try{v.muted=true;v.pause()}catch(e){}});
mute(); await new Promise(r=>setTimeout(r,3000)); mute();
const likes=[...document.querySelectorAll('svg[aria-label="Like"]')];
const first=likes[0], second=likes[1];
let el=first, box=null;
for(let i=0;i<15&&el;i++){el=el.parentElement; if(!el) break; if(second && el.contains(second)) break; if(el.querySelector('svg[aria-label="Share"]')) box=el;}
const nums=box?box.innerText.split('\n').map(s=>s.trim()).filter(s=>/^\d[\d.,]*[KMBkmb]?$/.test(s)):[];
const md=((document.querySelector('meta[property="og:description"]')||{}).content||'').replace(/\s+/g,' ').slice(0,240);
'bar:['+nums.join(', ')+'] || md: '+md
