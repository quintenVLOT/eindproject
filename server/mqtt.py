from paho.mqtt import client as mqtt
import time
import subprocess
import os
import json
from constants import *
from database import DataBase
 
database = DataBase() 
 
class MQTTBROKER():
    def run():
        os.system("taskkill /f /im  mosquitto.exe") # sluit eerst alle mqtt servers af
        
        # maak een mqtt server aan
        print(f"[SERVER] MQTT is running on mqtt://{IP}:{MQTT_PORT}/")
        subprocess.run(["C:\Program Files\mosquitto\mosquitto.exe", "-c", "C:\Program Files\mosquitto\mosquitto.conf", "-v", "-p", f"{MQTT_PORT}"], shell=True)

class MQTTCLIENT():
    def on_message(client, userdata, message):
        decoded_message=str(message.payload.decode("utf-8"))
        msg=json.loads(decoded_message)
        database.insert_reading(msg)
        
    def run():
        client = mqtt.Client(MQTT_CLIENT_NAME) #create new instance
        client.connect(IP, port=MQTT_PORT, bind_address="") #connect to broker
        client.subscribe(MQTT_TOPIC)
        client.on_message=MQTTCLIENT.on_message
        client.loop_forever()