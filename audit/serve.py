import os,sys,time,threading,brotli,mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
ROOT=os.path.abspath('mirror')
KBPS=float(sys.argv[2])            # kilobits/sec, shared across all connections
PORT=int(sys.argv[1])
BYTES_PER_SEC=KBPS*1000/8
_lock=threading.Lock(); _tokens=[BYTES_PER_SEC]; _last=[time.time()]
def take(n):
    while n>0:
        with _lock:
            now=time.time(); _tokens[0]=min(BYTES_PER_SEC,_tokens[0]+(now-_last[0])*BYTES_PER_SEC); _last[0]=now
            g=min(n,_tokens[0]); _tokens[0]-=g; n-=g
        if n>0: time.sleep(0.005)
CACHE={}
def body(path):
    if path in CACHE: return CACHE[path]
    raw=open(path,'rb').read()
    ct=mimetypes.guess_type(path)[0] or 'application/octet-stream'
    if any(path.endswith(e) for e in ('.html','.css','.js','.svg')):
        enc='br'; data=brotli.compress(raw,quality=4)   # Cloudflare's measured level
    else:
        enc=None; data=raw
    CACHE[path]=(data,ct,enc); return CACHE[path]
class H(BaseHTTPRequestHandler):
    protocol_version='HTTP/1.1'
    def log_message(self,*a): pass
    def do_GET(self):
        p=self.path.split('?')[0]
        if p=='/': p='/index.html'
        fp=os.path.normpath(os.path.join(ROOT,p.lstrip('/')))
        if not fp.startswith(ROOT) or not os.path.isfile(fp):
            self.send_response(404); self.send_header('Content-Length','0'); self.end_headers(); return
        data,ct,enc=body(fp)
        self.send_response(200)
        self.send_header('Content-Type',ct)
        self.send_header('Content-Length',str(len(data)))
        if enc: self.send_header('Content-Encoding',enc)
        self.send_header('Cache-Control','no-store')
        self.end_headers()
        CH=2048
        for i in range(0,len(data),CH):
            chunk=data[i:i+CH]; take(len(chunk))
            try: self.wfile.write(chunk)
            except Exception: return
ThreadingHTTPServer(('127.0.0.1',PORT),H).serve_forever()
