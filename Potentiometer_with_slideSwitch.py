import time
import analogio
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import math
 
pixel_pin = board.D2
num_pixels = 16

dial_pin = board.A2 #pin 0 is Analog input 2 
dial = analogio.AnalogIn(dial_pin)

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

PURPLE = (180, 0, 255)
OFF = (0,0,0)

while True:
    print(switch.value)
    if (switch.value==True):
        time.sleep(0.2)
        #print((math.sqrt(dial.value,)))
        if(int(math.sqrt(dial.value)-20)>0):
            val = int(math.sqrt(dial.value)-20) #scale down potentiometer values to fit within color range
        else:
            val=0
        print(val)
        pixels.fill((val,val,val))
        pixels.show()

    else:
        pixels.fill(OFF)
        pixels.show()
        time.sleep(1)  # debounce delay
