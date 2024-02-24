from paho.mqtt import client as mqtt
import time
import subprocess
import os
from constants import *
 
class MQTTBROKER():
    def run():
        os.system("taskkill /f /im  mosquitto.exe") # sluit eerst alle mqtt servers af
        
        # maak een mqtt server aan
        print(f"MQTT is running on mqtt://{IP}:{MQTT_PORT}/")
        subprocess.run(["C:\Program Files\mosquitto\mosquitto.exe", "-c", "C:\Program Files\mosquitto\mosquitto.conf", "-v", "-p", f"{MQTT_PORT}"], shell=True)

class MQTTCLIENT():
    def on_message(client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

    def run():
        client = mqtt.Client(MQTT_CLIENT_NAME) #create new instance
        client.connect(IP, port=MQTT_PORT, keepalive=60, bind_address="") #connect to broker
        client.subscribe(MQTT_TOPIC)
        client.on_message=MQTTCLIENT.on_message

        print("client is connected:", client.is_connected())
