"""relink7.py <project item name> <new media path>: ProjectItem.changeMediaPath on the item in ABW11 (every clip that uses it follows; layout, gains and overlays untouched). Run under premiere.lock."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A
name, path = sys.argv[1], sys.argv[2].replace("\\", "/")
js = "(function(){" + A.PRE + """function walk(p){ for (var i = 0; i < p.children.numItems; i++){ var c = p.children[i]; if (c.type === 2){ var r = walk(c); if (r) return r; } else if (c.name === %s) return c; } return null; }
var it = walk(app.project.rootItem); if (!it) return 'NOITEM'; var before = it.getMediaPath(); var ok = it.changeMediaPath(%s, true); return JSON.stringify({before: before, ok: ok, after: it.getMediaPath()}); })()""" % (json.dumps(name), json.dumps(path))
print(A.es(js, timeout=300))
