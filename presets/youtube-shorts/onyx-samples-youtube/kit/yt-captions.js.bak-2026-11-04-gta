/* =========================================================================================
 * yt-captions.js  ·  the YouTube-Shorts caption system (README.md section 5) for HyperFrames.
 * Plain browser JS (no modules, no build step). Needs GSAP (global `gsap`) and yt-captions.css.
 *
 *   ytCaptions(tl, container, chunks, opts)  ->  { root, chunks: [{ el, k0, k1, chunk }] }
 *
 *   tl         the composition's paused gsap.timeline(); register it AFTER this call
 *   container  element or selector of a full-canvas layer (position:absolute; inset:0) above the picture
 *   chunks     [{ text, start, end, voice, wipe }]
 *                text   one line, ALL CAPS, <= ~19 characters
 *                start  seconds: the chunk's first on-screen frame (already ~3-4 frames before its first word)
 *                end    seconds: when it leaves (with fillGaps the next chunk's start wins: never blank)
 *                voice  "main"   -> plain = white,        wipe = white -> red
 *                       "purple" | "yellow" | "cyan" | a key of opts.palette
 *                                -> plain = SOLID colour, wipe = white -> colour
 *                wipe   true = one linear left-to-right colour wipe across the whole line
 *   opts       { fps } is REQUIRED and must be the RENDER fps (24000/1001 or 30): every step lands on that grid.
 *              Everything else defaults to the measured reference (DEFAULTS below), e.g. { x: 540, y: 1071 }.
 *              The SVG filters are shared by every call on the page: the first call's outline/shadow/blur win.
 *
 *   const tl = gsap.timeline({ paused: true });
 *   ytCaptions(tl, "#caps", [
 *     { text: "THERE'S A CEMETERY", start: 10.260, end: 11.094, voice: "main",   wipe: true  },
 *     { text: "ON IT",              start: 11.094, end: 11.720, voice: "main",   wipe: false },
 *     { text: "WORRY ABOUT IT",     start: 12.137, end: 13.013, voice: "purple", wipe: true  },
 *   ], { fps: 24000 / 1001 });
 *   window.__timelines[compositionId] = tl;   // compositionId = the root's data-composition-id
 *   (Keep that key a variable in this comment: `hyperframes lint` reads string keys even in comments.)
 *
 * What it builds per chunk (measured frame by frame on the reference Short):
 *   - visibility: autoAlpha steps; the next chunk hard-replaces it (no exit animation);
 *   - entrance: 5 discrete frames (tl.set at frame boundaries, not a tween), horizontal stretch only,
 *     the height never changes. Each frame shows the scale range the reference's motion blur covers:
 *     0.765-0.855, 0.89-1.01, 1.09-1.04, 1.045-1.01, then 1.00 sharp. A range is drawn as `ghosts`
 *     copies averaged in linear light (plus-lighter at 1/N) + a light horizontal-only SVG blur, so the
 *     centre stays sharp and the ends streak, like the reference;
 *   - wipe: --ytc-p tweened 0 -> 1 with ease "none" (constant speed, ~58 px soft edge): the colour edge
 *     enters on the chunk's first frame (visible from the 2nd) and covers the line at 88 % of its
 *     screen time, then holds;
 *   - outline + soft drop shadow: SVG filter #ytc-fx (dilate + blur + offset), applied after the
 *     horizontal squeeze, so it is even on all sides and the same under white and colour.
 * ========================================================================================= */
(function (global) {
  "use strict";

  var DEFAULTS = {
    fps: null,
    x: null,                 // px horizontal centre; null = CSS --ytc-x (540)
    y: null,                 // px glyph centre (middle of the caps); null = CSS --ytc-y (1071)
    fillGaps: true,          // hold each chunk until the next one starts (the screen is never blank)
    pop: [                   // one entry per entrance frame; s = scaleX, or [from, to] = smeared over that range;
                             // blur = 0..3 (#ytc-hbN). Keep the last entry { s: 1 }: it is the settled state.
      { s: [0.765, 0.855], blur: 1 },
      { s: [0.89, 1.01], blur: 1 },
      { s: [1.09, 1.04], blur: 1 },
      { s: [1.045, 1.01], blur: 1 },
      { s: 1 }
    ],
    ghosts: 4,               // copies averaged on a smeared frame (1 = mean scale + SVG blur only)
    hblur: [1.5, 4, 10],     // stdDeviation X of #ytc-hb1, #ytc-hb2, #ytc-hb3 (blur: 1 | 2 | 3 in `pop`)
    smearGamma: 2.2,         // ghosts are averaged in linear light (like a real motion blur); 1 = plain sRGB average
    wipeStart: 0,            // frames after the first frame when the colour edge reaches the line's left edge
    wipeEnd: 0.88,           // share of the chunk's screen time when the colour covers the whole line
    outline: { r: 3, soft: 2, gain: 2 },                     // dilate radius px, edge softness, alpha gain
    shadow: { dx: 6, dy: 8, blur: 4, opacity: 1 },           // soft black drop shadow, down-right
    palette: null            // extra voices: { name: { grad: "linear-gradient(180deg, ...)", top: "#..", bot: "#..", white: false } }
  };

  var SVGNS = "http://www.w3.org/2000/svg";

  function merge(base, over) {
    var out = {}, k;
    for (k in base) out[k] = base[k];
    for (k in over) {
      if (over[k] === undefined) continue;
      if (base[k] && typeof base[k] === "object" && !Array.isArray(base[k]) && over[k] && typeof over[k] === "object") {
        out[k] = merge(base[k], over[k]);
      } else {
        out[k] = over[k];
      }
    }
    return out;
  }

  function el(doc, tag, cls) {
    var e = doc.createElement(tag);
    if (cls) e.className = cls;
    return e;
  }

  function svg(doc, tag, attrs, parent) {
    var e = doc.createElementNS(SVGNS, tag);
    for (var k in attrs) e.setAttribute(k, String(attrs[k]));
    if (parent) parent.appendChild(e);
    return e;
  }

  function gammaRGB(doc, parent, exponent, input) {
    var ct = svg(doc, "feComponentTransfer", input ? { "in": input } : {}, parent);
    ["feFuncR", "feFuncG", "feFuncB"].forEach(function (fn) {
      svg(doc, fn, { type: "gamma", amplitude: 1, exponent: exponent, offset: 0 }, ct);
    });
  }

  // The filters live inside the caption layer (so they are part of the composition) and are shared.
  //   #ytc-fx   outline + drop shadow (every line)
  //   #ytc-fxl  the same, then sRGB -> linear (smear ghosts, so their average is a linear-light blur)
  //   #ytc-hbN  horizontal-only Gaussian blur N (CSS blur() is isotropic)
  //   #ytc-smN  blur N + linear -> sRGB (the smear group, on top of its averaged ghosts)
  function makeDefs(doc, o) {
    var s = svg(doc, "svg", { "class": "ytc-defs", width: 0, height: 0, "aria-hidden": "true", focusable: "false" });
    if (doc.getElementById("ytc-fx")) return s;            // a second call reuses the first call's filters
    var defs = svg(doc, "defs", {}, s);
    ["ytc-fx", "ytc-fxl"].forEach(function (id) {
      var f = svg(doc, "filter", { id: id, x: "-30%", y: "-80%", width: "160%", height: "260%",
        "color-interpolation-filters": "sRGB" }, defs);
      svg(doc, "feMorphology", { "in": "SourceAlpha", operator: "dilate", radius: o.outline.r, result: "d" }, f);
      svg(doc, "feGaussianBlur", { "in": "d", stdDeviation: o.outline.soft, result: "ds" }, f);
      var ct = svg(doc, "feComponentTransfer", { "in": "ds", result: "ol" }, f);
      svg(doc, "feFuncA", { type: "linear", slope: o.outline.gain }, ct);
      svg(doc, "feGaussianBlur", { "in": "d", stdDeviation: o.shadow.blur, result: "sb" }, f);
      svg(doc, "feOffset", { "in": "sb", dx: o.shadow.dx, dy: o.shadow.dy, result: "so" }, f);
      var st = svg(doc, "feComponentTransfer", { "in": "so", result: "sh" }, f);
      svg(doc, "feFuncA", { type: "linear", slope: o.shadow.opacity }, st);
      var m = svg(doc, "feMerge", { result: "lit" }, f);
      svg(doc, "feMergeNode", { "in": "sh" }, m);
      svg(doc, "feMergeNode", { "in": "ol" }, m);
      svg(doc, "feMergeNode", { "in": "SourceGraphic" }, m);
      if (id === "ytc-fxl") gammaRGB(doc, f, o.smearGamma, "lit");
    });
    for (var i = 0; i <= o.hblur.length; i++) {
      // #ytc-hbN: horizontal-only blur (CSS blur() is isotropic). #ytc-smN: the same blur + the smear lift.
      if (i > 0) {
        var h = svg(doc, "filter", { id: "ytc-hb" + i, x: "-15%", y: "-10%", width: "130%", height: "120%",
          "color-interpolation-filters": "sRGB" }, defs);
        svg(doc, "feGaussianBlur", { stdDeviation: o.hblur[i - 1] + " 0" }, h);
      }
      var sm = svg(doc, "filter", { id: "ytc-sm" + i, x: "-15%", y: "-10%", width: "130%", height: "120%",
        "color-interpolation-filters": "sRGB" }, defs);
      if (i > 0) svg(doc, "feGaussianBlur", { stdDeviation: o.hblur[i - 1] + " 0" }, sm);
      gammaRGB(doc, sm, 1 / o.smearGamma);
    }
    return s;
  }

  function makeLine(doc, text, extra) {
    var line = el(doc, "div", "ytc-line" + (extra ? " " + extra : ""));
    var fx = el(doc, "div", "ytc-fx");
    var sq = el(doc, "div", "ytc-sq");
    var tx = el(doc, "span", "ytc-text");
    tx.textContent = text;
    tx.setAttribute("data-text", text);                  // the masked colour layer of a wiped chunk repeats the text (::after)
    if (extra === "ytc-ghost") tx.setAttribute("data-layout-allow-overlap", "");   // ghosts overlap by design
    sq.appendChild(tx);
    fx.appendChild(sq);
    line.appendChild(fx);
    line.setAttribute("data-layout-allow-overflow", "");
    return line;
  }

  function blurOf(level) {
    return level ? "url(#ytc-hb" + level + ")" : "none";
  }

  function smearOf(level, gamma) {
    return gamma === 1 ? blurOf(level) : "url(#ytc-sm" + (level || 0) + ")";
  }

  function spread(a, b, n) {                           // scaleX of ghost g (function-based value for tl.set)
    return function (g) { return n > 1 ? a + (b - a) * g / (n - 1) : (a + b) / 2; };
  }

  function ytCaptions(tl, container, chunks, opts) {
    var o = merge(DEFAULTS, opts || {});
    if (!tl || typeof tl.set !== "function") throw new Error("ytCaptions: pass the composition's gsap timeline");
    if (!(o.fps > 0)) throw new Error("ytCaptions: opts.fps is required (e.g. 24000 / 1001)");
    var doc = global.document;
    var host = typeof container === "string" ? doc.querySelector(container) : container;
    if (!host) throw new Error("ytCaptions: container not found");

    var root = el(doc, "div", "ytc");
    root.setAttribute("data-layout-allow-overflow", "");
    if (o.x != null) root.style.setProperty("--ytc-x", o.x + "px");
    if (o.y != null) root.style.setProperty("--ytc-y", o.y + "px");
    root.appendChild(makeDefs(doc, o));
    host.appendChild(root);

    var fps = o.fps;
    var K = Math.max(1, Math.round(o.ghosts));
    var frameOf = function (t) { return Math.round(t * fps + 1e-6); };
    // A step that must be on screen from frame k on sits a quarter frame early: safe against float error
    // and against renderers that sample at the frame start or the frame middle.
    var at = function (k) { return Math.max(0, (k - 0.25) / fps); };
    var needsSmear = o.pop.some(function (p) { return Array.isArray(p.s) && p.s[0] !== p.s[1]; });

    var list = chunks.slice().sort(function (a, b) { return a.start - b.start; });
    var made = [];
    list.forEach(function (c, i) {
      var k0 = frameOf(c.start);
      var k1 = frameOf(c.end);
      var next = list[i + 1];
      if (next) {
        var kn = frameOf(next.start);
        if (o.fillGaps || k1 > kn) k1 = kn;               // hard replace; and no blank gap when fillGaps
      }
      if (k1 <= k0) return;

      var voice = c.voice || "main";
      var custom = o.palette && o.palette[voice];
      var chunk = el(doc, "div", "ytc-chunk ytc-v-" + (custom ? "custom" : voice));
      chunk.setAttribute("data-layout-allow-overflow", "");
      chunk.setAttribute("data-ytc-index", String(i));
      if (c.y != null) chunk.style.setProperty("--ytc-y", c.y + "px");   // per-chunk glyph centre (ig_capy.py: just under the lips)
      if (custom) {
        chunk.style.setProperty("--ytc-grad", custom.grad);
        chunk.style.setProperty("--ytc-grad-top", custom.top);
        chunk.style.setProperty("--ytc-grad-bot", custom.bot);
      }
      var whitePlain = custom ? !!custom.white : voice === "main";
      chunk.style.setProperty("--ytc-p", c.wipe || whitePlain ? "0" : "1");
      // fill model (QA 2026-10-05: white stacked over the gradient in ONE clipped layer bled red at anti-aliased edges):
      // a plain white chunk is one solid white fill; a wiped chunk is solid white with the colour on a masked layer above
      if (c.wipe) chunk.classList.add("ytc-wipe");
      else if (whitePlain) chunk.classList.add("ytc-solid");

      var main = makeLine(doc, c.text, "ytc-main");
      chunk.appendChild(main);
      var smear = null, ghosts = [];
      if (needsSmear && K > 1) {
        smear = el(doc, "div", "ytc-smear");
        smear.setAttribute("aria-hidden", "true");
        smear.setAttribute("data-layout-allow-overflow", "");
        for (var g = 0; g < K; g++) {
          var gl = makeLine(doc, c.text, "ytc-ghost");
          gl.style.opacity = String(1 / K);
          smear.appendChild(gl);
          ghosts.push(gl);
        }
        chunk.appendChild(smear);
      }
      root.appendChild(chunk);

      // on / off
      tl.set(chunk, { autoAlpha: 1 }, at(k0));
      tl.set(chunk, { autoAlpha: 0 }, at(k1));
      (c.moves || []).forEach(function (m) {              // [frame, y]: a new shot's lip line, applied ON the cut frame (ig_capy.py)
        tl.set(chunk, { "--ytc-y": m[1] + "px" }, at(m[0]));
      });

      // entrance: one discrete state per frame
      for (var j = 0; j < o.pop.length && k0 + j < k1; j++) {
        var step = o.pop[j], s = step.s, T = at(k0 + j);
        var smeared = Array.isArray(s) && s[0] !== s[1];
        if (smeared && smear) {
          tl.set(main, { autoAlpha: 0 }, T);
          tl.set(smear, { autoAlpha: 1, filter: smearOf(step.blur, o.smearGamma) }, T);
          tl.set(ghosts, { scaleX: spread(s[0], s[1], K) }, T);
        } else {
          var sc = Array.isArray(s) ? (s[0] + s[1]) / 2 : s;
          if (smear) tl.set(smear, { autoAlpha: 0 }, T);
          tl.set(main, { autoAlpha: 1, scaleX: sc, filter: blurOf(step.blur || 0) }, T);
        }
      }

      // emphasis wipe: constant speed, then hold
      if (c.wipe) {
        var t0 = (k0 + o.wipeStart) / fps;
        var t1 = (k0 + o.wipeEnd * (k1 - k0)) / fps;
        if (t1 > t0) {
          tl.fromTo(chunk, { "--ytc-p": 0 }, { "--ytc-p": 1, duration: t1 - t0, ease: "none", immediateRender: false }, t0);
        } else {
          chunk.style.setProperty("--ytc-p", "1");
        }
      }
      made.push({ el: chunk, k0: k0, k1: k1, chunk: c });
    });
    return { root: root, chunks: made };
  }

  ytCaptions.DEFAULTS = DEFAULTS;
  global.ytCaptions = ytCaptions;
})(window);
