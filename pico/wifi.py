import network
import time

def connect_wifi(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    
    while(not wlan.isconnected()):
        print(f"trying to connect to {ssid} wifi")
        time.sleep(1)
