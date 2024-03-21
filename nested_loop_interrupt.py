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
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

COLORS = [RED, GREEN, BLUE]


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
    if (mode == 0):                         # Mode 0 is off
        pixels.fill(OFF)
        pixels.show()
        
        if (handleButton()):                # We check the button during each mode! 
            print("changing modes!")
    elif (mode == 1):                       # Mode 1 is spinning colors
        buttonWasPressed = False

        for currentColor in COLORS: 
            for pixel in range(0, num_pixels, 1):
                pixels[pixel] = currentColor
                pixels.show()

                buttonWasPressed = handleButton()
                if (buttonWasPressed):              # This needs to be INSIDE our deepest loop! 
                    ("The button was pressed! Gotta break out of this loop.")
                    break                           # Now we have to break out of this inside loop

                time.sleep(0.2)
            if buttonWasPressed:                    # Check if a button press was detected 
                break                               # If it was, we have to break out of the bigger loop too

    time.sleep(0.2);            # Take a break between loops and checking

