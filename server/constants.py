import socket

IP = socket.gethostbyname_ex(socket.gethostname())[-1][1]
WEBSITE_PORT = 8000
MQTT_PORT = 1884
MQTT_CLIENT_NAME = "SERVER"
MQTT_TOPIC = "A103/picos"
