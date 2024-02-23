from bme680lib import *
import machine
from machine import Pin, I2C
import utime
import time
import json

class Meeting():
    def __init__(self,bme680,x,y):
        self.temperatuur = str(round(bme680.temperature, 2))
        self.luchtvochtigheid = str(round(bme680.humidity, 2))
        self.luchtdruk = str(round(bme680.pressure, 2))
        self.gas = str(round(bme680.gas/1000, 2))
        self.x = x
        self.y = y
        self.tijd = utime.time()
       
    def toJson(self):
        meeting = {
            "temperatuur": self.temperatuur,
            "luchtvochtigheid": self.luchtvochtigheid,
            "luchtdruk": self.luchtdruk,
            "gas": self.gas,
            "x": self.x,
            "y": self.y,
            "tijd": self.tijd
        }
        
        return json.dumps(meeting)
       
    def __str__ (self):
        return "temperatuur: "+self.temperatuur+" °C\nluchtvochtigheid: "+self.luchtvochtigheid+" %\nluchtdruk: "+self.luchtdruk+" hPa\ngas: "+self.gas+" Kohm\nx: "+str(self.x)+"\ny: "+str(self.y)+"\ntijd: "+str(self.tijd)
class Sensor():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)    #initializing the I2C method 
        self.bme = BME680_I2C(i2c=self.i2c)
        uart0 = machine.UART(0, baudrate=115200)

    def get_sensor_data(self):
        return Meeting(self.bme,self.x,self.y).toJson()
