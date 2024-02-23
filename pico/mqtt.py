import time
from umqtt.simple import MQTTClient

def connect(client_id,server,port):
    client = MQTTClient(client_id, server, port=port, keepalive=3600)
    client.connect()
    print(f'Connected to mqtt://{server}:{port} MQTT Broker as {client_id}')
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    
def connect_mqtt(client_id,server,port):
    connected = False
    
    while (connected is False):
        try:
            client = connect(client_id,server,port)
            connected = True
            return client
        except OSError as e:
            reconnect()
            
def publish_meeting(client,meeting,topic):
    client.publish(topic,meeting)
    
