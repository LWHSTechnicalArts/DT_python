#button_interruptable_chase 
#note time.sleep for the chasing sequence must be short for the button to feel responsive

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
 
pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)


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
RED = (255,0,0)


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
        for light in range(0,16,1):
            pixels[light]=RED
            pixels.show()
            time.sleep(.1)
            pixels[light]=OFF
            pixels.show()
            
            if (handleButton()):            # This needs to be INSIDE our for loop! 
                print("changing modes!")
                break                       # and we NEED to break inside the loop
                
    elif (mode == 1):
        pixels.fill(RED)
        pixels.show()
        
        if (handleButton()):                # We check the button during each mode! 
            print("changing modes!")
        
    time.sleep(0.2) # take a break from checking    
