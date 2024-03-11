from bme680lib import *
import machine
from machine import Pin, I2C
import utime
import time
import json

class Meeting():
    def __init__(self,bme680,x,y,sensor_id):
        self.temperatuur = str(round(bme680.temperature, 2))
        self.luchtvochtigheid = str(round(bme680.humidity, 2))
        self.luchtdruk = str(round(bme680.pressure, 2))
        self.gas = str(round(bme680.gas/1000, 2))
        self.x = x
        self.y = y
        self.tijd = utime.time()
        self.sensor_id = sensor_id
       
    def toJson(self):
        meeting = {
            "temperatuur": self.temperatuur,
            "luchtvochtigheid": self.luchtvochtigheid,
            "luchtdruk": self.luchtdruk,
            "gas": self.gas,
            "x": self.x,
            "y": self.y,
            "tijd": self.tijd,
            "sensor_id": self.sensor_id
        }
        
        return json.dumps(meeting)
       
class Sensor():
    def __init__(self,x,y,sensor_id):
        self.x = x
        self.y = y
        self.sensor_id = sensor_id
        self.i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)    #initializing the I2C method 
        self.bme = BME680_I2C(i2c=self.i2c)
        uart0 = machine.UART(0, baudrate=115200)

    def get_sensor_data(self):
        return Meeting(self.bme,self.x,self.y,self.sensor_id).toJson()


