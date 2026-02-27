# Created: 2024-02-16
# Written for CircuitPython 3.1.1
#button_interruptable_fade

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# -------------------- Setting up the LEDs so we can write to them
pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

# -------------------- Setting up our switch so we can read from it
switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# -------------------- Mode variables
# "modes" are how we determine what the LED should be doing
mode = 0
NUMBER_OF_MODES = 2

# -------------------- Color variables
OFF = (0,0,0)


# handleButton checks if the button is pressed, and changes mode if it is
def handleButton():
    global mode
    buttonWasPressed = False
    
    if (switch.value == False): 
        mode += 1
        if mode >= NUMBER_OF_MODES:
            mode = 0
        buttonWasPressed = True
    
    return buttonWasPressed

while True:
    if (mode == 0):
        pixels.fill(OFF)
        pixels.show()
        
        if (handleButton()):                # We check the button during each mode! 
            print("changing modes!")
    elif (mode == 1):
        for num in range(0,255,1):
            color = (num,num,num)
            pixels.fill(color)
            pixels.show()
            
            if (handleButton()):            # This needs to be INSIDE our for loop! 
                print("changing modes!")
                break                       # and we NEED to break inside the loop
                
    time.sleep(0.2) # take a break from checking


