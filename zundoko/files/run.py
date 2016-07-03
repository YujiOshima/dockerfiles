from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

hostname = socket.gethostname()

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        uri = self.path
        body = ""
        if uri == "/zun":
            body = b"zun"
        elif uri == "/doko":
            body = b"doko"
        elif uri == "/kiyoshi":
            body = b"__kiyoshi__"
        else :
            body = judge_reponce(hostname).encode('utf-8')

        self.send_response(200)
        self.end_headers()
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.wfile.write(body)

def judge_reponce(cid):
    intid = int(hostname, 16)
    if intid % 5 == 0:
        return "**kiyoshi**"
    elif intid % 5 == 1:
        return "doko"
    else:
        return "zun"

host = '0.0.0.0'
port = 8000
httpd = HTTPServer((host, port), MyHandler)
print('serving at port', port)
httpd.serve_forever()
