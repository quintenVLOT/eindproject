import time
from wifi import connect_wifi
from mqtt import connect_mqtt, publish_meeting
from bme680 import Sensor
from led import LED

# wifi
wifi_ssid = "bokkie"
wifi_password = "papabokkie"

# mqtt
mqtt_client_id = "A103S2"
mqtt_server = "10.16.0.12"
mqtt_port = 1884
mqtt_topic = "A103/picos"

def main():
    connect_wifi(wifi_ssid,wifi_password)
    client = connect_mqtt(mqtt_client_id,mqtt_server,mqtt_port)
    sensor = Sensor(0,0)

    while(True):
        meeting = sensor.get_sensor_data()
            
        publish_meeting(client,meeting,mqtt_topic)
        print("test")
        time.sleep(1)

main()


