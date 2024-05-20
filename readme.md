<img align="left" width="300" src="https://github.com/quintenVLOT/quintenVLOT/assets/144037167/11ecadb5-90d3-49b8-b31e-58abe571819a">
<br/><br/><br/><br/><br/><br/><br/>

# Eindproject: Intelligent sensorarray voor binnenklimaatmetingen

Dit is mijn eindproject genaamd: "Intelligent Sensor Systems". Het project bestaat uit een server en een aantal sensoren die met elkaar communiceren via het MQTT protocol. De server is verantwoordelijk voor het ontvangen van de data van de sensoren en het opslaan van deze data in een database en deze data weergeeft op een website. De sensoren zijn verantwoordelijk voor het meten van de temperatuur, luchtvochtigheid, luchtdruk en gas en het versturen van deze data naar de server.

## Inhoudsopgave
- [Voorbereiding](#voorbereiding)
  * [Server (Windows)](#server-windows)
  * [Sensors (Raspberry Pi Pico W)](#sensors-raspberry-pi-pico-w)
- [Gebruik](#gebruik)
    * [Server (Windows)](#server-windows-1)
    * [Sensors (Raspberry Pi Pico W)](#sensors-raspberry-pi-pico-w-1)
- [flowcharts](#flowcharts)
    * [sensor wifi.py](#sensor-wifipy)
    * [sensor mqtt.py](#sensor-mqttpy)
    * [sensor bme680.py](#sensor-bme680py)
    * [sensor main.py](#sensor-mainpy)
    * [server mqtt.py](#server-mqttpy)
    * [server database.py](#server-databasepy)
    * [server web.py](#server-webpy)
    * [server main.py](#server-mainpy)

## Voorbereiding

### Server (Windows)
- Installeer [mosquitto mqtt](https://mosquitto.org/download/)
- Kopieer het [mosquitto.conf](server/mosquitto.conf) bestand in de server map naar C:\Program Files\mosquitto
- Installeer python
- Installeer de benodigde python packages:
```powershell
pip install -d requirements.txt
```

### Sensors (Raspberry Pi Pico W)
- Installeer [Thonny](https://thonny.org/)
- Installeer Micropython op de pico W via Thonny.

## Gebruik

### Server (Windows)
Voor het starten van de server:
```powershell
python main.py
```

### Sensors (Raspberry Pi Pico W)

## flowcharts

### sensor wifi.py

- Functie : connect_wifi(ssid,password)
- Doel : Connectie maken met het wifi netwerk.
- Parameters : ssid (str), password (str)
- Returnwaarde : void
- Te installeren headers: network, time
- Flowchart: 

```mermaid
---
title: sensor wifi.py
---
flowchart TD
    A[connect_wifi] --> B(wifi activeren) 
    B --> C(wlan.connect)
    C --> D{wlan.isconnected}
    D -->|False| E(wacht 5 seconden) --> D
    D -->|True| F[return]
```

### sensor mqtt.py

- Functie : connect_mqtt(client_id,server,port)
- Doel : Connectie maken met de mqtt server.
- Parameters : client_id (str), server (str), port (int)
- Returnwaarde : client (mqtt.Client)
- Te installeren headers: umqtt.simple
- Flowchart: 

```mermaid
---
title: sensor mqqt.py
---
flowchart TD 
    A[connect_mqtt] --> B(client aanmaken) 
    B --> C(client.connect)
    C --> D(connected = True)
    D{connected == True} -->|False| E(wacht 5 seconden) --> C
    D -->|True| F[return client]
```

- Functie : publish_meeting(client,meeting,topic)
- Doel : Vezend een meeting naar de mqtt server.
- Parameters : client (mqtt.Client), meeting (Meeting), topic (str)
- Returnwaarde : void
- Te installeren headers: umqtt.simple
- Flowchart: 

```mermaid
---
title: sensor mqqt.py
---
flowchart TD 
    A[publish_meeting] --> B(client.publish) 
    B --> C[return]
```

### sensor bme680.py

- Klassen : Meeting, Sensor
- Doel : De Meeting klasse bevat de data van een meeting en de Sensor klasse bevat de data van een sensor.
- Parameters : Meeting: temperatuur (float), luchtvochtigheid (float), luchtdruk (float), gas (float), x (float), y (float), tijd (Time), sensor_id (str)
- Parameters : Sensor: x (float), y (float), sensor_id (str), i2c (i2c), bme (BME680_I2C), uart0 (UART)
- Returnwaarde : Meeting, Sensor
- Te installeren headers: bme680lib, machine, utime, time, json
- Flowchart: 

```mermaid
---
title: sensor BME680.py
---
classDiagram
    class Meeting
    Meeting : +Float temperatuur
    Meeting : +Float luchtvochtigheid
    Meeting : +Float luchtdruk
    Meeting : +Float gas
    Meeting : +Float x
    Meeting : +Float y
    Meeting : +Time tijd
    Meeting : +String sensor_id

    Meeting : +json toJson()

    class Sensor
    Sensor : +Float x
    Sensor : +Float y
    Sensor : +String sensor_id
    Sensor : +i2c i2c
    Sensor : +BME680_I2C bme
    Sensor : +UART uart0

    Sensor : +json get_sensor_data(self).toJson()
```

### sensor main.py

- Functie : main()
- Doel : De main functie van het programma.
- Parameters : void
- Returnwaarde : void
- Te installeren headers: time, wifi, mqtt, bme680
- Flowchart: 

```mermaid
---
title: sensor main.py
---
flowchart TD 
    A[main] --> B(connect_wifi) 
    B --> C(connect_mqtt)
    C --> D(Initializeer sensor)
    D{True} --> E(sensor.get_sensor_data)
    E --> F(publish_meeting)
    F --> G[wacht 1 seconde] --> D
```

### server mqtt.py
- Klassen : MQTTBROKER, MQTTCLIENT
- Doel : De MQTTBROKER klasse bevat de data van een mqtt broker en de MQTTCLIENT klasse bevat de data van een mqtt client.
- Parameters : void
- Returnwaarde : MQTTBROKER, MQTTCLIENT
- Te installeren headers: paho.mqtt, time, subprocess, os, json, constants, database
- Flowchart: 

```mermaid
---
title: server mqtt.py
---
classDiagram
    MQTTBROKER : +run()

    MQTTCLIENT : +on_message(client, userdata, message)
    MQTTCLIENT : +run()
```

```mermaid
---
title: server mqtt.py
---
flowchart TD 
    A[MQTTBROKER.run] --> B(sluit bestaande mqtt broker af) 
    B --> C(voer mosquitto uit) --> C

    D[MQTTCLIENT.run] --> E(maak mqtt client aan) 
    E --> F[connect client met mqtt broker]
    F --> G(subscribe op topic)
    G --> H(wacht op bericht en voer on_message uit) --> J
    H --> I[loop_forever] --> I

    J[MQTTCLIENT.on_message] --> K(decodeer bericht)
    K(Zet bericht om in json) --> L(voeg meeting toe aan database) --> return
```

### server database.py
- Klassen : Database
- Doel : De Database klasse bevat de functie om om te communiceren met de database.
- Parameters : db_file (str)
- Returnwaarde : Database
- Te installeren headers: time, sqlite3, json
- Flowchart: 

```mermaid
---
title: server database.py
---
classDiagram
    class Database
    Database : +String db_file
    Database : +sqlite3 conn

    Database : +create_meetingen_table(self)
    Database : +create_kalibreer_table(self)
    Database : +insert_reading(self,json)
    Database : +insert_kalibratie(self, json)
    Database : +get_readings(self, aantal, sensor_id)
    Database : +get_kalibratie(self, sensor_id)
    Database : +clear_meeetingen(self)
    Database : +clear_kalibratie(self)
    Database : +close_connection(self)
```

```mermaid
---
title: server database.py
---
flowchart TD 
    A[Database.create_meetingen_table] --> B[maak query] --> C[voer query uit] --> D(maak meetingen tabel aan als deze nog niet bestaat) --> E[return]

    F[Database.create_kalibreer_table] --> G[maak query] --> H[voer query uit] --> I(maak kalibreer tabel aan als deze nog niet bestaat) --> J[return]
```

```mermaid
---
title: server database.py
---
flowchart TD 
    A[Database.insert_reading] --> B[maak query] --> C[voer query uit] --> D(voeg meeting toe aan database) --> E[return]
    F[Database.insert_kalibratie] --> G[maak query] --> H[voer query uit] --> I(voeg kalibratie toe aan database) --> J[return]
```

```mermaid
---
title: server database.py
---
flowchart TD
    A[Database.get_readings] --> B[maak query] --> C[voer query uit] --> D(krijg all meetingen die de juiste sensor id hebben) --> E(zet meetingen om in json) --> F[return json]

    G[Database.get_kalibratie] --> H[maak query] --> I[voer query uit] --> J(krijg kalibratie die de juiste sensor id heeft) --> K(zet kalibratie om in json) --> L[return json]
```

```mermaid
---
title: server database.py
---
flowchart TD
    A[Database.clear_meeetingen] --> B[maak query] --> C[voer query uit] --> D(verwijder sensor_data tabel) --> E[return]

    F[Database.clear_kalibratie] --> G[maak query] --> H[voer query uit] --> I(verwijder kalibratie_data tabel) --> J[return]
```

### server web.py

- Klassen : WebServer
- Doel : De WebServer klasse bevat functies om een webserver te maken.
- Parameters : BaseHTTPRequestHandler
- Returnwaarde : WebServer
- Te installeren headers: http.server, time, json, constants, database
- Flowchart: 

```mermaid
---
title: server web.py
---
classDiagram
    class WebServer
    WebServer : +BaseHTTPRequestHandler handler

    WebServer : +do_GET(self)
    WebServer : +do_meeetingen(self)
    WebServer : +do_kalibratie(self)
    WebServer : +clear(self)
```


```mermaid
---
title: server web.py
---
flowchart TD
    A[WebServer.do_GET] --> B(check of request naar /meetingen gaat) --> C(voer do_meetingen uit) --> D(krijg meetingen uit database) --> E[return meetingen als json]
    A --> F(check of request naar /kalibratie gaat) --> G(voer do_kalibratie uit) --> H(krijg kalibratie uit database) --> I[return kalibratie als json]
    A --> J(check of request naar /clear gaat) --> K(voer clear uit) --> L(verwijder meetingen uit database) --> N[return]
```

- Functie : run_server()
- Doel : Start de webserver.
- Parameters : void
- Returnwaarde : void
- Te installeren headers:
- Flowchart: 

```mermaid
---
title: server web.py
---
flowchart TD
    A[run_server] --> B(maak webserver een WebServer klasse aan) --> C[voer webserver uit] --> C
```


### server main.py
- Functie : main()
- Doel : De main functie van het programma.
- Parameters : void
- Returnwaarde : void
- Te installeren headers: time, threading, web, mqtt
- Flowchart: 

```mermaid
---
title: server main.py
---
flowchart TD 
    A[main] --> B(maak mqtt en webserver threads aan) 
    B --> C(voer threads uit)
    C(wacht 1 seconde) --> D
    D(voer mqqt client uit) --> D
```
