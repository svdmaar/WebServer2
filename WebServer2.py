# About localhost:
#    https://pt.wikipedia.org/wiki/Localhost

import http.server
import socketserver

PORT = 8080

class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = "Hello from MyHttpHandler";
        self.wfile.write(bytes(html, "utf8"))

with socketserver.TCPServer(("", PORT), MyHttpHandler) as httpd:
    print("Serving at port: " + str(PORT))
    httpd.serve_forever()
