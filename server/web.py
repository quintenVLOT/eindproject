from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import re
from constants import *
from database import DataBase

database = DataBase()

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if re.search('/api/waarde/*',self.path):
            sensor_id = self.path.split('/')[-1]
            self.do_meetingen(sensor_id)
            
        elif re.search('/api/kalibratie/*',self.path):
            sensor_id = self.path.split('/')[-1]
            self.get_kalibratie(sensor_id)
            
        elif re.search('/api/clear',self.path):
            self.clear()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
            
    def do_meetingen(self,sensor_id):
        meetingen = database.get_readings(20,sensor_id)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(meetingen.encode())
        
    def get_kalibratie(self,sensor_id):
        kalibratie = database.get_kalibratie(sensor_id)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(kalibratie.encode())        
        
    def clear(self):
        database.clear_meetingen()
        meetingen = database.get_readings(20,sensor_id)
        self.send_response(200)

def run_server():
    server_address = ('', WEBSITE_PORT)
    httpd = HTTPServer(server_address, WebServer)
    print(f"[SERVER] Server is running on http://{IP}:{WEBSITE_PORT}/")
        
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    