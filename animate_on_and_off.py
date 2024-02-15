import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# Setting up the LEDs so we can write to them 
pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

# Setting up our switch so we can read from it 
switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# "modes" will be how we tell if we're turning on and off
mode=0
number_of_modes=2
lastSwitchValue = True # we'll use this variable to tell whether we need change modes 

WHITE = (255,255,255)
OFF = (0,0,0)

def handleMode(mode): 
    if (mode == 0):
        animateOn()
    elif (mode == 1):
        animateOff()


# this function runs an animation that animates all LEDs on
# when it's done, the LEDs will stay on until we tell them to do something else. 
def animateOn(): 
    for i in range(0, num_pixels, 1):   
        pixels[i] = WHITE
        pixels.show()
        time.sleep(0.1)
    
# this function runs an animation that animates all LEDs off 
# when it's done, the LEDs will stay off until we tell them to do something else. 
def animateOff(): 
    for i in range(0, num_pixels, 1):   
        pixels[i] = OFF
        pixels.show()
        time.sleep(0.1)

while True:
    currentSwitchValue = switch.value # check our switch! 
    if (currentSwitchValue == False and lastSwitchValue == True): # If our switch JUST got pressed
        # The next 4 lines ONLY RUN ONCE after the switch is pressed!
        mode += 1 # change our mode 
        if mode >= number_of_modes: 
            mode = 0
        handleMode(mode) # go do something with our new mode

    lastSwitchValue = currentSwitchValue 
    time.sleep(0.1) # take a break from checking
    


