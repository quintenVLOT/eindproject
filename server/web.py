from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket

IP = socket.gethostbyname_ex(socket.gethostname())[-1][1]

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WebServer)
    print(f"Server is running on http://{IP}:{port}/")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()