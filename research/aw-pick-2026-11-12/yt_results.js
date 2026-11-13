// Read a YouTube search-results page without extra requests (walks window.ytInitialData). Mutes all media first.
// Returns "S|id|views|title" for Shorts and "V|id|views|duration|channel|title" for videos, top 30.
(()=>{document.querySelectorAll('video,audio').forEach(v=>{v.muted=true;v.volume=0;v.pause();});
const out=[];const seen=new Set();
const walk=o=>{if(!o||typeof o!=='object')return;
 if(o.shortsLockupViewModel){const s=o.shortsLockupViewModel;const id=(s.onTap?.innertubeCommand?.reelWatchEndpoint?.videoId)||'';const t=s.overlayMetadata?.primaryText?.content||'';const v=s.overlayMetadata?.secondaryText?.content||'';if(id&&!seen.has(id)){seen.add(id);out.push('S|'+id+'|'+v+'|'+t.replace(/[^\x20-\x7E]/g,'').slice(0,60));}}
 if(o.reelItemRenderer){const r=o.reelItemRenderer;const id=r.videoId;if(id&&!seen.has(id)){seen.add(id);out.push('S|'+id+'|'+(r.viewCountText?.simpleText||'')+'|'+(r.headline?.simpleText||'').replace(/[^\x20-\x7E]/g,'').slice(0,60));}}
 if(o.videoRenderer){const r=o.videoRenderer;const id=r.videoId;if(id&&!seen.has(id)){seen.add(id);out.push('V|'+id+'|'+(r.viewCountText?.simpleText||'').replace(' views','')+'|'+(r.lengthText?.simpleText||'')+'|'+(r.ownerText?.runs?.[0]?.text||'').slice(0,18)+'|'+(r.publishedTimeText?.simpleText||'')+'|'+(r.title?.runs?.[0]?.text||'').replace(/[^\x20-\x7E]/g,'').slice(0,55));}}
 for(const k in o){if(k!=='frameworkUpdates')walk(o[k]);}};
walk(window.ytInitialData);return out.length+'\n'+out.slice(0,30).join('\n');})()
