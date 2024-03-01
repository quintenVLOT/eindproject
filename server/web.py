from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from constants import *
from database import DataBase

database = DataBase()

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())

def run_server():
    server_address = ('', WEBSITE_PORT)
    httpd = HTTPServer(server_address, WebServer)
    print(f"[SERVER] Server is running on http://{IP}:{WEBSITE_PORT}/")
        
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()