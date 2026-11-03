"""dialog-watch.py [--once] [--no-close]: keep Premiere's import-failure modals from locking the bridge (2026-11-02).

A failed importFiles / changeMediaPath opens a modal "File Import Failure" dialog. While it is up the CEP panel queues every
command and the bridge reads "MCP Bridge is not running", so the creator ends up clicking Cancel by hand. This watcher polls
Premiere's visible top-level windows once a second. It LOGS every dialog other than the main window (title, child texts, a
PrintWindow grab, the premiere.lock owner at that moment = whose call raised it) and CLOSES (WM_CLOSE = Cancel) only the
import-failure ones. Anything else (save prompts, export, missing media) is logged and left for the creator.

Log: projects/_onyx-batch6-2026-10/premiere-dialogs.log + grabs in projects/_onyx-batch6-2026-10/premiere-dialogs/.
"""
import ctypes, ctypes.wintypes as W, datetime, os, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGDIR = os.path.join(ROOT, "projects", "_onyx-batch6-2026-10")
LOG = os.path.join(LOGDIR, "premiere-dialogs.log")
GRABS = os.path.join(LOGDIR, "premiere-dialogs")
LOCK = os.path.join(ROOT, "projects", "_onyx-batch2-2026-10", ".locks", "premiere.lock")
CLOSE_IF = ("import failure", "importer reported", "generic error", "could not be imported", "unsupported format")

u, g = ctypes.windll.user32, ctypes.windll.gdi32
EnumProc = ctypes.WINFUNCTYPE(W.BOOL, W.HWND, W.LPARAM)


def pids():
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq Adobe Premiere Pro.exe", "/FO", "CSV", "/NH"],
                         capture_output=True, text=True).stdout
    return {int(p[1]) for p in (l.split('","') for l in out.splitlines()) if len(p) > 1}


def text(h):
    n = u.GetWindowTextLengthW(h); b = ctypes.create_unicode_buffer(n + 1); u.GetWindowTextW(h, b, n + 1); return b.value


def kids(h):
    out = []
    def cb(c, _):
        t = text(c)
        if t and t not in out: out.append(t)
        return True
    u.EnumChildWindows(h, EnumProc(cb), 0)
    return out


def grab(h, path):
    try:
        from PIL import Image
        r = W.RECT(); u.GetWindowRect(h, ctypes.byref(r)); w, hh = r.right - r.left, r.bottom - r.top
        if w <= 0 or hh <= 0: return
        dc = u.GetWindowDC(h); mdc = g.CreateCompatibleDC(dc); bmp = g.CreateCompatibleBitmap(dc, w, hh); g.SelectObject(mdc, bmp)
        u.PrintWindow(h, mdc, 2)
        class BIH(ctypes.Structure):
            _fields_ = [("biSize", W.DWORD), ("biWidth", W.LONG), ("biHeight", W.LONG), ("biPlanes", W.WORD), ("biBitCount", W.WORD),
                        ("biCompression", W.DWORD), ("biSizeImage", W.DWORD), ("biXPelsPerMeter", W.LONG), ("biYPelsPerMeter", W.LONG),
                        ("biClrUsed", W.DWORD), ("biClrImportant", W.DWORD)]
        bi = BIH(ctypes.sizeof(BIH), w, -hh, 1, 32, 0, 0, 0, 0, 0, 0); buf = ctypes.create_string_buffer(w * hh * 4)
        g.GetDIBits(mdc, bmp, 0, hh, buf, ctypes.byref(bi), 0)
        Image.frombuffer("RGB", (w, hh), buf, "raw", "BGRX", 0, 1).save(path)
        g.DeleteObject(bmp); g.DeleteDC(mdc); u.ReleaseDC(h, dc)
    except Exception as e:
        log(f"  grab failed: {e}")


def log(line):
    os.makedirs(LOGDIR, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f: f.write(line + "\n")
    print(line, flush=True)


def owner():
    try: return open(os.path.join(LOCK, "owner"), encoding="utf-8").read().strip()[:160]
    except OSError: return "(lock free)" if not os.path.isdir(LOCK) else "(lock held, no owner file)"


def scan(close, seen):
    P = pids(); found = []
    def cb(h, _):
        pid = W.DWORD(); u.GetWindowThreadProcessId(h, ctypes.byref(pid))
        if pid.value in P and u.IsWindowVisible(h) and not text(h).startswith("Adobe Premiere Pro 20"): found.append(h)
        return True
    u.EnumWindows(EnumProc(cb), 0)
    for h in found:
        t, k = text(h), kids(h)
        blob = " ".join([t] + k).lower()
        hit = any(s in blob for s in CLOSE_IF)
        if h not in seen:
            seen.add(h); ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.makedirs(GRABS, exist_ok=True); png = os.path.join(GRABS, ts.replace(":", "").replace(" ", "_") + f"_{h:x}.png"); grab(h, png)
            log(f"{ts}  dialog {h:#x} {t!r}  texts={k[:8]}  lock={owner()}  grab={os.path.basename(png)}  {'CLOSE' if hit and close else 'left open'}")
        if hit and close: u.PostMessageW(h, 0x0010, 0, 0)     # WM_CLOSE = the dialog's Cancel


def main():
    close = "--no-close" not in sys.argv; seen = set()
    log(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}  watch start (close={close})")
    while True:
        try: scan(close, seen)
        except Exception as e: log(f"  scan error: {e}")
        if "--once" in sys.argv: break
        time.sleep(1)


if __name__ == "__main__":
    main()
