import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.getenv("PORT", "3000"))

counter = 0


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter

        if self.path != "/pingpong":
            self.send_error(404)
            return

        response = f"pong {counter}\n"
        counter += 1

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)

    print(f"Ping-pong server started in port {PORT}", flush=True)

    server.serve_forever()