import time
import threading
from web import run_server
from mqtt import MQTTBROKER, MQTTCLIENT
    
if __name__ == "__main__":        
    webServerThread = threading.Thread(target=run_server)
    mqttServerThread = threading.Thread(target=MQTTBROKER.run)
    webServerThread.start()
    mqttServerThread.start()
    time.sleep(1)
    MQTTCLIENT.run()
