import ujson as json
import time
from machine import Pin
time.sleep(0.1) # Wait for USB to become ready

class Eeprom():
    def __init__(self, fileName):
        self.fileName = fileName
 
    def write(self,jsonData):
        try:
            with open(self.fileName, 'w') as f:
                json.dump(jsonData, f)
        except:
            print("Could not save.")

    def read(self):
        with open(self.fileName, 'r') as f:
            return json.load(f)

def main():
    jsonData = {"stateKey": 1}
    eeprom = Eeprom('savedata.json')

    eeprom.write(jsonData)
    print(eeprom.read())

main()

