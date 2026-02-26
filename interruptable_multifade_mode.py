# Created: 2024-03-21
# Written for CircuitPython 3.1.1
# interruptable_multifade_mode
# Interrupting multiple fades at once

# In this example, we have a mode that does two fades (one on, and one off). 
# We build a variable to keep track of whether a button has been pressed during this mode. 
# If we press the button anytime during the mode, we change modes.

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

# handleButton checks if the button is pressed, and changes mode if it is
def handleButton():
    global mode
    buttonWasPressed = False
    
    if (button.value == False): 
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
        buttonWasPressed = False

        if (not buttonWasPressed):          # If the button has not been pressed, proceed.
            for num in range(0,255,1):
                color = (num,num,num)
                pixels.fill(color)
                pixels.show()
                
                buttonWasPressed = handleButton()   # Check for the button and save the result
                if (buttonWasPressed):            # This needs to be INSIDE our for loop! 
                    print("changing modes!")
                    break                       # and we NEED to break inside the loop
        
        if (not buttonWasPressed):          # If the button has not been pressed, proceed.
            for num in range(255,0,-1):
                color = (num,num,num)
                pixels.fill(color)
                pixels.show()

                buttonWasPressed = handleButton()   # Check for the button and save the result
                if (buttonWasPressed):            # This needs to be INSIDE our for loop! 
                    print("changing modes!")
                    break           

    time.sleep(0.2) # take a break from checking


