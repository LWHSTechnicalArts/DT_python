# button_and_potentiometer 

import time
import analogio
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import math

dial_pin = board.A2 #pin 0 is Analog input 2 
dial = analogio.AnalogIn(dial_pin)

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.D2
num_pixels = 16
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
YELLOW = (255, 150, 0)
OFF = (0,0,0)

now=0

while True:
    time.sleep(0.05)
    if (switch.value==False):    #detect the button press
        now=now+1 
        if (now >1): 
            now=0
    if(now == 0):
        pixels.fill(OFF)
        pixels.show()
    if(now == 1):
        val = int(math.sqrt(dial.value)-20) #scale down potentiometer values to fit within color range
        print(val)
        pixels.fill((val,val,val))
        pixels.show()
    
    time.sleep(0.12)  # debounce delay
    
