import os
from http.server import BaseHTTPRequestHandler, HTTPServer


PORT = int(os.getenv("PORT", "3000"))


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Todo application is running")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)

    print(f"Server started in port {PORT}", flush=True)

    server.serve_forever()