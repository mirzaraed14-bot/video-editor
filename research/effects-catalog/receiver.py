"""Local receiver for frames captured in the browser: POST http://127.0.0.1:8765/save?path=<relative path> with the
JPEG as the body. Writes under research/effects-catalog/ only. Stop it when the capture is done."""
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.abspath(__file__))


class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Private-Network', 'true')

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_POST(self):
        q = parse_qs(urlparse(self.path).query)
        rel = (q.get('path') or [''])[0].replace('\\', '/')
        dest = os.path.normpath(os.path.join(ROOT, rel))
        if not rel or not dest.startswith(ROOT + os.sep) or not dest.lower().endswith(('.jpg', '.json')):
            self.send_response(400); self._cors(); self.end_headers(); return
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        n = int(self.headers.get('Content-Length', 0))
        with open(dest, 'wb') as f:
            f.write(self.rfile.read(n))
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b'ok')

    def log_message(self, *a):
        pass


ThreadingHTTPServer(('127.0.0.1', 8765), H).serve_forever()
