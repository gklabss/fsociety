import socket
import threading
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Forward the request to the target server
        self.forward_request()

    def do_POST(self):
        # Forward the request to the target server
        self.forward_request()

    def forward_request(self):
        try:
            # Parse the URL
            parsed_url = urllib.parse.urlparse(self.path)

            # Create a connection to the target server
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((parsed_url.netloc, 80))

            # Send the request
            request_line = f"{self.command} {self.path} {self.request_version}\r\n"
            conn.send(request_line.encode())

            # Forward headers
            for key, value in self.headers.items():
                header_line = f"{key}: {value}\r\n"
                conn.send(header_line.encode())

            conn.send(b"\r\n")

            # Get response
            response = conn.recv(4096)
            self.wfile.write(response)
            conn.close()

        except Exception as e:
            self.send_error(500, str(e))

class ProxyServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = None
        self.is_running = False

    def start(self):
        """Start the proxy server"""
        try:
            self.server = HTTPServer((self.host, self.port), ProxyHandler)
            self.is_running = True
            print(f"Proxy server started on {self.host}:{self.port}")

            # Start server in a separate thread
            server_thread = threading.Thread(target=self.server.serve_forever)
            server_thread.daemon = True
            server_thread.start()

            return self.server
        except Exception as e:
            print(f"Failed to start proxy server: {e}")
            return None

    def stop(self):
        """Stop the proxy server"""
        if self.server:
            self.server.shutdown()
            self.is_running = False
            print("Proxy server stopped")

def create_proxy(host='localhost', port=8080):
    """Factory function to create a proxy server instance"""
    return ProxyServer(host, port)