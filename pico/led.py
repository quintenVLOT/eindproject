from picozero import RGBLED
from time import sleep

class LED:
    def __init__(self,red,green,blue):
        self.rgb = RGBLED(red = red, green = green, blue = blue)
        
    def red(self):
        self.rgb.color = (255, 0, 0)
 
    def orange(self):
        self.rgb.color = (255,165,0)
        
    def pink(self):
        self.rgb.color = (255,20,147)
        
    def off(self):
        self.rgb.color = (0,0,0)