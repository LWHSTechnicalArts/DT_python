# Created: 2024-02-15
# Written for CircuitPython 3.1.1
# random_color

import board
import neopixel
import time
import random
 
pixel_pin = board.D2   #the ring data is connected to this pin
num_pixels = 16        #number of leds pixels on the ring
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
 
while True:
    pixels[0] = (random.randint(150,250),random.randint(50,150),0)
    pixels.show()     #required to update pixels
    time.sleep(.5)
    
  
