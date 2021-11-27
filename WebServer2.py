# About localhost:
#    https://pt.wikipedia.org/wiki/Localhost

import http.server
import socketserver
import datetime

PORT = 8080

class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        timeStr = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        html = "<p>Hello from MyHttpHandler: " + timeStr + "</p>"
        self.wfile.write(bytes(html, "utf8"))

with socketserver.TCPServer(("", PORT), MyHttpHandler) as httpd:
    print("Serving at port: " + str(PORT))
    httpd.serve_forever()
