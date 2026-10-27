import os
import time
import uuid
import threading

from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer


PORT = int(os.getenv("PORT", "3000"))

random_string = str(uuid.uuid4())


def current_status():
    timestamp = datetime.now(timezone.utc).isoformat()
    return f"{timestamp}: {random_string}"


def print_logs():
    while True:
        print(current_status(), flush=True)
        time.sleep(5)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404, "Not Found")
            return

        response = current_status().encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)


if __name__ == "__main__":
    logging_thread = threading.Thread(target=print_logs, daemon=True)
    logging_thread.start()

    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)

    print(f"HTTP server started in port {PORT}", flush=True)
    server.serve_forever()