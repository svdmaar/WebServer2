# About localhost:
#    https://pt.wikipedia.org/wiki/Localhost

import http.server
import socketserver
import datetime

PORT = 8080

class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/sum.html"):
            fields = self.path.split("?")
            sum = 0
            addedHtml = ""
            if (len(fields) > 1):
                args = fields[1].split("&")
                for arg in args:
                    nameValue = arg.split("=")
                    addedHtml += "<p>" + nameValue[0] + "</p>"
                    addedHtml += "<p>" + nameValue[1] + "</p>"
                    sum += int(nameValue[1])
            addedHtml += "<p>sum: " + str(sum) + "</p>"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            timeStr = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
            html = "<p>Hello from MyHttpHandler: " + timeStr + "</p>"
            html += "<p>" + self.path + "</p>"
            html += addedHtml
            self.wfile.write(bytes(html, "utf8"))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHttpHandler) as httpd:
    print("Serving at port: " + str(PORT))
    httpd.serve_forever()
