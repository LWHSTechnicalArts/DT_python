# Created: 2024-03-21
# Written for CircuitPython 3.1.1
# Interrupting custom fader at once

# This example updates the custom foder to also include button input. 
# This can be used to interrupt a single fade, but it also includes an example 
# of how to track that button press and exit out of a multi-fade mode. 

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# -------------------- Setting up our button so we can read from it
button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

# -------------------- Setting up the LEDs so we can write to them
pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

# -------------------- Mode variables
# "modes" are how we determine what the LED should be doing
mode = 0
NUMBER_OF_MODES = 2
 
# -------------------- Color variables
OFF = (0,0,0)
YELLOW = (255, 150, 0)
PINK= (255,64,123)
ORANGE= (255, 83, 25)

# handleButton checks if the button is pressed, and changes mode if it is
# this function returns True if the button was pressed. 
def handleButton():
    global mode
    buttonWasPressed = False
   
    if (button.value == False): 
        mode += 1
        if mode >= NUMBER_OF_MODES:
            mode = 0
        buttonWasPressed = True
    
    return buttonWasPressed

 # helper function for fading - do not touch
 # This function will STOP and return True if the button was pressed. 
def fadeWithButtonInterrupt(c1, c2):
    diff = (c2[0]-c1[0], c2[1]-c1[1], c2[2]-c1[2])
    diffA = [1 if n==0 else abs(n) for n in diff]
    maxDiff = max(diffA)
    index = diffA.index(maxDiff)
    cFade = list(c1)
    increment = [int(diff[i]/diffA[i]) for i in range(3)]
    for i in range(0, maxDiff):
        for n in range(3):
            if(cFade[n] != c2[n]):
                cFade[n] += increment[n]
        pixels.fill(tuple(cFade))
        pixels.show()
        if (handleButton()):            # This needs to be INSIDE our for loop! 
            print("button detected in fade loop")
            return True
        time.sleep(0.01)  # debounce delay
    return False
#end helper function
    
while True:
    if (mode == 0):
        pixels.fill(OFF)
        pixels.show()
        
        if (handleButton()):                # We check the button during each mode! 
            print("changing modes!")
    elif (mode == 1):
        buttonWasPressed = False

        if (not buttonWasPressed):          # If the button has not been pressed, proceed.
            buttonWasPressed = fadeWithButtonInterrupt(PINK, YELLOW)

        if (not buttonWasPressed):          # If the button has not been pressed, proceed.
            buttonWasPressed = fadeWithButtonInterrupt(YELLOW, ORANGE)


    time.sleep(0.2) # take a break from checking