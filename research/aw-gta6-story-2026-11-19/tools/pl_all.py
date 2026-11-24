# pl_all.py <playlistId> <out.json> [max_pages] : page through a channel's uploads via yt_api.py (1 unit per page)
import json, subprocess, sys
pl, out = sys.argv[1], sys.argv[2]; maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 12
items, tok = [], None
for _ in range(maxp):
    args = [sys.executable, '-I', 'research/deep-research-2026-11-14/yt_api.py', 'gta6-story', 'playlistItems',
            'part=snippet,contentDetails', f'playlistId={pl}', 'maxResults=50'] + ([f'pageToken={tok}'] if tok else [])
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8')
    d = json.loads(r.stdout); items += d.get('items', []); tok = d.get('nextPageToken')
    if not tok: break
json.dump(items, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
print(len(items), 'items')
