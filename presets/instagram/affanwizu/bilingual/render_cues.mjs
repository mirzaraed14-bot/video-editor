// Two-layer @affanwizu caption test (2026-11-16): Urdu script (Noto Nastaliq Urdu) over Roman Urdu, gold, soft glow.
// One transparent PNG per cue (the caption band only), rendered by headless Chrome so Nastaliq is shaped by HarfBuzz.
// usage: node render_cues.mjs <job dir> <out dir> <json params>
import { existsSync, readdirSync, readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { homedir } from 'node:os';
import { pathToFileURL } from 'node:url';

const [jobArg, outArg, pjson] = process.argv.slice(2);
const job = resolve(jobArg), out = resolve(outArg); mkdirSync(out, { recursive: true });
const P = Object.assign({
  bandY: 1080, bandH: 420,                 // the PNG covers y bandY..bandY+bandH of the 1080x1920 frame
  urSize: 64, urBase: 1268,                // Urdu font px and baseline y (frame coordinates)
  roSize: 48, roBase: 1338, roFont: 'UbuntuLight', roWeight: 300,
  color: '#FFD700',
  glow: '0 0 3px rgba(255,215,0,0.55), 0 0 10px rgba(255,215,0,0.40), 0 0 22px rgba(255,200,0,0.22)',
  shadow: '',                              // drawn ABOVE the glow; yellow-style hard shadow = '3.75px 4.25px 1px rgba(0,0,0,1)'
  roCase: 'none',                          // 'uppercase' = Roman line in ALL CAPS (his call 2026-11-16, Seq 10 v2)
  hide: null,                              // 'ur' or 'ro': render one line only (ink measurements)
  only: null,                              // render only these cue indexes (probe)
}, pjson ? JSON.parse(pjson) : {});

const ro = readFileSync(join(job, 'captions.txt'), 'utf8').split('\n').filter(l => l.startsWith('@')).map(l => { const [t, x] = l.split('|'); return { t: +t.slice(1), ro: x.trim() }; });
const ur = readFileSync(join(job, 'captions.ur.txt'), 'utf8').split('\n').filter(l => l.startsWith('@')).map(l => { const [t, x] = l.split('|'); return { t: +t.slice(1), ur: x.trim() }; });
if (ro.length !== ur.length || ro.some((c, i) => Math.abs(c.t - ur[i].t) > 1e-6)) { console.error('captions.txt and captions.ur.txt do not pair up'); process.exit(2); }
const cues = ro.map((c, i) => ({ ...c, ur: ur[i].ur.replace(/“/g, '\u0001').replace(/”/g, '“').replace(/\u0001/g, '”') })); // RTL: the opening mark is the right-hand one

const npxDirs = [join(homedir(), '.npm', '_npx')]; if (process.env.LOCALAPPDATA) npxDirs.push(join(process.env.LOCALAPPDATA, 'npm-cache', '_npx'));
let pick = null;
for (const [npx, d] of npxDirs.flatMap(p => existsSync(p) ? readdirSync(p).map(d => [p, d]) : [])) {
  const pc = join(npx, d, 'node_modules', 'puppeteer-core', 'package.json'); if (!existsSync(pc)) continue;
  const v = JSON.parse(readFileSync(pc)).version, s = v.split('.').reduce((a, b, i) => a + (parseInt(b, 10) || 0) / 1000 ** i, 0);
  if (!pick || s > pick.s) pick = { s, nm: join(npx, d, 'node_modules') };
}
const entry = ['lib/puppeteer/puppeteer-core.js', 'lib/esm/puppeteer/puppeteer-core.js'].map(e => join(pick.nm, 'puppeteer-core', e)).find(existsSync);
const puppeteer = await import(pathToFileURL(entry).href);
const CHROME = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'].find(existsSync);

const FONTS = 'file:///X:/Claude%20Projects/video-editor-client/video-editor/assets/fonts/';
const html = `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face { font-family: 'NotoNastaliq'; src: url('${FONTS}NotoNastaliqUrdu-wght.ttf'); font-weight: 400 700; }
@font-face { font-family: 'UbuntuLight'; src: url('${FONTS}Ubuntu-Light.ttf'); font-weight: 300; }
html,body { margin:0; width:1080px; height:${P.bandH}px; background:transparent; overflow:hidden; }
.l { position:absolute; left:0; top:0; width:1080px; text-align:center; white-space:nowrap; color:${P.color};
     text-shadow: ${[P.shadow, P.glow].filter(Boolean).join(', ')}; }
.pb { display:inline-block; width:0; height:0; vertical-align:baseline; }
#ur { font: 400 ${P.urSize}px 'NotoNastaliq'; direction:rtl; }
#ro { font: ${P.roWeight} ${P.roSize}px ${P.roFont === 'UbuntuLight' ? "'UbuntuLight'" : `'${P.roFont}'`}; text-transform: ${P.roCase}; }
${P.hide ? `#${P.hide} { visibility: hidden; }` : ''}
</style></head><body>
<div class="l" id="ur"><span id="urs"></span><span class="pb" id="urp"></span></div><div class="l" id="ro"><span id="ros"></span><span class="pb" id="rop"></span></div>
</body></html>`;

const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--hide-scrollbars', '--force-device-scale-factor=1', '--allow-file-access-from-files'] });
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: P.bandH, deviceScaleFactor: 1 });
  writeFileSync(join(out, 'page.html'), html);
  await page.goto(pathToFileURL(join(out, 'page.html')).href, { waitUntil: 'load' });
  const idx = P.only ?? cues.map((_, i) => i);
  const meta = [];
  for (const i of idx) {
    const c = cues[i];
    const m = await page.evaluate(async (u, r, yu, yr) => {
      document.getElementById('urs').textContent = u; document.getElementById('ros').textContent = r;
      await document.fonts.ready;
      // a zero-size inline-block sits ON the baseline: move each line so its baseline lands on the target y
      for (const [d, pb, y] of [['ur', 'urp', yu], ['ro', 'rop', yr]]) {
        const el = document.getElementById(d); el.style.top = '0px';
        const b = document.getElementById(pb).getBoundingClientRect().bottom; el.style.top = (y - b) + 'px';
      }
      const a = document.getElementById('urs').getBoundingClientRect(), b = document.getElementById('ros').getBoundingClientRect();
      return { urW: a.width, roW: b.width, fonts: [...document.fonts].map(f => f.family + ':' + f.status).join(',') };
    }, c.ur, c.ro, P.urBase - P.bandY, P.roBase - P.bandY);
    const f = join(out, `cue_${String(i).padStart(3, '0')}.png`);
    await page.screenshot({ path: f, omitBackground: true, clip: { x: 0, y: 0, width: 1080, height: P.bandH } });
    meta.push({ i, t: c.t, ro: c.ro, ur: c.ur, file: f, ...m });
  }
  writeFileSync(join(out, 'cues.json'), JSON.stringify({ params: P, cues: meta }, null, 1));
  console.log(`rendered ${meta.length} cue(s) -> ${out}  fonts: ${meta[0]?.fonts}`);
} finally { await browser.close(); }
