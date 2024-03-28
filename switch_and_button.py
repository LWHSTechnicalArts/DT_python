# switch_and_button.py
# In this example, we use both a slide switch and a button. 
# The switch turns the whole light on and off. 
# The button switches between colors. 

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# -------------------- Setting up the LEDs so we can write to them
pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

# -------------------- Setting up our switch so we can read from it
switch = DigitalInOut(board.D4)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

# -------------------- Mode variables
# "modes" are how we determine what the LED should be doing
mode = 0
number_of_modes = 2

# -------------------- Color variables
OFF = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def check_button():
    global mode
    if (button.value==False):
        mode +=1
        if mode >= number_of_modes:
            mode =0
        time.sleep(0.3)
    print(mode)

while True: 
    if (switch.value == True):      # If the switch is turned on
        check_button()              # check our button

        if (mode == 0):      # Mode 0
            pixels.fill(RED)
            pixels.show()
        elif (mode == 1):    # Mode 1
            pixels.fill(GREEN)
            pixels.show()
    else:                           # If the switch is turned off
        pixels.fill(OFF)            # turn LEDS off
        pixels.show()