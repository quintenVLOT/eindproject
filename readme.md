<img align="left" width="300" src="https://github.com/quintenVLOT/quintenVLOT/assets/144037167/11ecadb5-90d3-49b8-b31e-58abe571819a">
<br/><br/><br/><br/><br/><br/><br/>

# Eindproject: Intelligent sensorarray voor binnenklimaatmetingen

Dit is mijn eindproject genaamd: "Intelligent Sensor Systems". Het project bestaat uit een server en een aantal sensoren die met elkaar communiceren via het MQTT protocol. De server is verantwoordelijk voor het ontvangen van de data van de sensoren en het opslaan van deze data in een database en deze data weergeeft op een website. De sensoren zijn verantwoordelijk voor het meten van de temperatuur, luchtvochtigheid, luchtdruk en gas en het versturen van deze data naar de server.

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
