# About localhost:
#    https://pt.wikipedia.org/wiki/Localhost

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port: " + str(PORT))
    httpd.serve_forever();
