#!/usr/bin/env node
// page-record.mjs — record a WEB PAGE headlessly for a `screen-rec` / `screenshot` cell whose
// capture source is a URL (step 5b, Stage 2). Never touches the user's own browser: it drives a
// separate headless Chrome (the installed Google Chrome binary, its own profile), so nothing is
// fronted, no tab switches mid-take, no extension banner in the frame (the 2026-09-11 take through
// the live Chrome caught a tab switch and a "started debugging" bar; that route is retired for URLs).
//
//   node workflows/page-record.mjs <url> <out.mp4|out.png> [--seconds 6] [--scroll 1200] [--dark]
//        [--width 1920] [--height 1080] [--scale 2] [--fps 30000/1001] [--wait 1500] [--hide "css,css"]
//
//   --seconds  length of the take (mp4 only)
//   --scroll   total pixels to scroll over the take, eased (0 = hold still)
//   --dark     prefers-color-scheme: dark (sites that follow the OS theme)
//   --scale    device scale factor: 2 = Retina-crisp (3840x2160 from a 1920x1080 viewport)
//   --wait     ms after load before the take starts (fonts, lazy images)
//   --hide     selectors to remove before the take (cookie bars, banners)
//   --force    overwrite an existing output (default: refuse — a placed capture keeps its name)
//   a .png output takes one still instead of a recording (--scroll then sets the scroll position first);
//   --full makes it a FULL-PAGE still (--full-screens N scrolls N screens first so lazy content loads), for a smooth pan
//   over one tall image in the comp instead of a stuttery screencast scroll (Onyx QA, 2026-10-05)
//
// Output: a CONSTANT-rate H.264 mp4 (conformed by ffmpeg from Chrome's screencast webm) or a png,
// at viewport x scale pixels. The comp frames and scales it (a screen-rec is a scene, never parked
// full-frame). The runtime is puppeteer-core out of HyperFrames' own npx cache, so nothing new is
// installed; the browser is the installed Google Chrome (CHROME_PATH overrides).
import { existsSync, readdirSync, readFileSync, mkdirSync, unlinkSync, statSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { homedir } from 'node:os';
import { pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';

const args = process.argv.slice(2);
if (args.length < 2 || args.includes('-h') || args.includes('--help')) {
  console.error(readFileSync(new URL(import.meta.url)).toString().split('\n').slice(1, 22).map(l => l.replace(/^\/\/ ?/, '')).join('\n'));
  process.exit(args.includes('-h') || args.includes('--help') ? 0 : 2);
}
const [url, outArg] = args;
if (!/^https?:\/\//i.test(url) || !outArg || outArg.startsWith('-')) { console.error('[page-record] usage: <http(s) url> <out.mp4|out.mov|out.png> [flags]'); process.exit(2); }
const opt = (k, d) => { const i = args.indexOf(k); return i > -1 ? args[i + 1] : d; };
const num = (k, d) => { const v = +opt(k, d); if (!Number.isFinite(v) || v < 0) { console.error(`[page-record] ${k} needs a number, got ${opt(k, d)}`); process.exit(2); } return v; };
const SECS = num('--seconds', 6), SCROLL = num('--scroll', 0), DARK = args.includes('--dark'), FORCE = args.includes('--force');
const W = num('--width', 1920), H = num('--height', 1080), SCALE = num('--scale', 2);
const FPS = opt('--fps', '30000/1001'), WAIT = num('--wait', 1500), HIDE = opt('--hide', '');
const FULL = args.includes('--full'), FULL_SCREENS = num('--full-screens', 3);   // .png only: a full-page still (lazy content loaded by scrolling N screens first)
if (!/^\d+(\/\d+)?$/.test(FPS)) { console.error(`[page-record] --fps wants a rational like 30000/1001, got ${FPS}`); process.exit(2); }
const out = resolve(outArg); const ext = out.toLowerCase().match(/\.(mp4|mov|png)$/)?.[1];
if (!ext) { console.error('[page-record] output must end in .mp4, .mov or .png'); process.exit(2); }
const still = ext === 'png';
if (existsSync(out) && !FORCE) { console.error(`[page-record] ${out} exists — a capture already in a comp keeps its name; write a new one or pass --force`); process.exit(2); }
if (!still && SECS <= 0) { console.error('[page-record] --seconds must be > 0 for a recording'); process.exit(2); }
mkdirSync(dirname(out), { recursive: true });

// puppeteer-core: the newest copy any hyperframes run left in the npx cache (the job pin is per job and bumps; a pin bonus here went stale on the next bump)
// Windows keeps the npm cache under %LOCALAPPDATA%\npm-cache, not ~/.npm (2026-09-19)
const npxDirs = [join(homedir(), '.npm', '_npx')];
if (process.env.npm_config_cache) npxDirs.unshift(join(process.env.npm_config_cache, '_npx'));
if (process.platform === 'win32' && process.env.LOCALAPPDATA) npxDirs.push(join(process.env.LOCALAPPDATA, 'npm-cache', '_npx'));
let pick = null;
for (const [npx, d] of npxDirs.flatMap(p => existsSync(p) ? readdirSync(p).map(d => [p, d]) : [])) {
  const nm = join(npx, d, 'node_modules');
  const pc = join(nm, 'puppeteer-core', 'package.json'); if (!existsSync(pc)) continue;
  const pcv = JSON.parse(readFileSync(pc)).version;
  const score = pcv.split('.').reduce((a, b, i) => a + (parseInt(b, 10) || 0) / 1000 ** i, 0);
  if (!pick || score > pick.score) pick = { score, nm, pcv };
}
if (!pick) { console.error('[page-record] no puppeteer-core in ~/.npm/_npx — run `npx hyperframes@0.8.16 --version` once'); process.exit(2); }
const entry = ['lib/puppeteer/puppeteer-core.js', 'lib/esm/puppeteer/puppeteer-core.js'].map(e => join(pick.nm, 'puppeteer-core', e)).find(existsSync);
const puppeteer = await import(pathToFileURL(entry).href);

const CHROME = process.env.CHROME_PATH || [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  'C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  process.env.LOCALAPPDATA ? join(process.env.LOCALAPPDATA, 'Google', 'Chrome', 'Application', 'chrome.exe') : '',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
].filter(Boolean).find(existsSync);
if (!CHROME) { console.error('[page-record] no Chrome found — set CHROME_PATH'); process.exit(2); }

const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--hide-scrollbars', '--force-device-scale-factor=' + SCALE] });
try {
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: SCALE });
  await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: DARK ? 'dark' : 'light' }]);
  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 45000 });
  } catch (e) {
    if (!/timeout/i.test(String(e))) throw new Error(`cannot load ${url}: ${String(e).split('\n')[0]}`);
    console.error('[page-record] network never went idle (a live page); continuing on load');   // goto already reached load
  }
  if (HIDE) await page.evaluate(sel => document.querySelectorAll(sel).forEach(e => e.remove()), HIDE);
  await new Promise(r => setTimeout(r, WAIT));
  // Chrome's screencast only emits a frame on PAINT: a static page yields an EMPTY take (measured on
  // example.com, 0-byte webm). A 1 px near-invisible ticker forces a repaint every tick of the take.
  await page.evaluate(() => { const t = document.createElement('div'); t.id = '__hf_tick'; t.style.cssText = 'position:fixed;left:0;top:0;width:2px;height:2px;opacity:0.01;background:#000;pointer-events:none;z-index:2147483647'; document.body.appendChild(t); });
  const tick = (n) => page.evaluate(n => { const t = document.getElementById('__hf_tick'); if (t) t.style.transform = `translateX(${n % 2}px)`; }, n);
  console.error(`[page-record] ${url}  ${W}x${H}@${SCALE}x  ${still ? 'still' : SECS + 's, scroll ' + SCROLL + 'px'}${DARK ? '  dark' : ''}`);

  if (still) {
    if (SCROLL > 0) { await page.evaluate(y => window.scrollTo(0, y), SCROLL); await new Promise(r => setTimeout(r, 300)); }
    await page.evaluate(() => document.getElementById('__hf_tick')?.remove());
    if (FULL) await page.evaluate(async (n) => { for (let i = 0; i < n; i++) { window.scrollBy(0, window.innerHeight); await new Promise(r => setTimeout(r, 700)); } window.scrollTo(0, 0); await new Promise(r => setTimeout(r, 500)); }, FULL_SCREENS);
    await page.screenshot({ path: out, fullPage: FULL });
  } else {
    const webm = out.replace(/\.(mp4|mov)$/i, '') + '.rec.webm';
    try {
      const rec = await page.screencast({ path: webm });
      const t0 = Date.now();
      // eased scroll over the whole take, driven from here so the timing is the take's, not the page's
      const ease = t => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      let n = 0, done = false;
      while (!done) {
        const t = Math.min(1, (Date.now() - t0) / (SECS * 1000)); done = t >= 1;
        if (SCROLL > 0) await page.evaluate(y => window.scrollTo(0, y), Math.round(ease(t) * SCROLL));
        await tick(n++);
        await new Promise(r => setTimeout(r, 16));
      }
      await rec.stop();
      const size = existsSync(webm) ? statSync(webm).size : 0;
      if (size < 1000) throw new Error(`the screencast captured nothing (${size} bytes): the page never painted a frame`);
      // Chrome's screencast is variable-rate: conform to the timeline's constant rate
      execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', webm, '-an', '-vf', `fps=${FPS}`, '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: 'inherit' });
    } finally {
      if (existsSync(webm)) unlinkSync(webm);
    }
  }
  const probe = execFileSync('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_entries', still ? 'stream=width,height' : 'stream=width,height:format=duration', '-of', 'csv=p=0', out]).toString().trim().replace(/\n/g, ' ');
  console.log(`[page-record] ${probe.replace(',', 'x')} -> ${out}`);
} catch (e) {
  console.error(`[page-record] failed: ${String(e.message || e).split('\n')[0]}`); process.exitCode = 1;
} finally {
  await browser.close();
}
