from paho.mqtt import client as mqtt
import time
import subprocess
import socket
import os
 
IP = socket.gethostbyname_ex(socket.gethostname())[-1][1]
port = 1884
client_name = "SERVER"

class MQTTBROKER():
    def run():
        os.system("taskkill /f /im  mosquitto.exe") # sluit eerst alle mqtt servers af
        
        # maak een mqtt server aan
        print(f"MQTT is running on mqtt://{IP}:{port}/")
        subprocess.run(["C:\Program Files\mosquitto\mosquitto.exe", "-c", "C:\Program Files\mosquitto\mosquitto.conf", "-v", "-p", f"{port}"], shell=True)

class MQTTCLIENT():
    def on_message(client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

    def run():
        client = mqtt.Client(client_name) #create new instance
        client.connect(IP, port=port, keepalive=60, bind_address="") #connect to broker
        client.subscribe("A103/picos")
        client.on_message=MQTTCLIENT.on_message

        print("client is connected:", client.is_connected())
