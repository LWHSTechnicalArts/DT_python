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
lastSwitchValue = True # we'll use this variable to tell whether we need change modes

# -------------------- Color variables
OFF = (0,0,0)
color_number = 0    # 
max_color_number = 254

# MODE 0: Off 
def mode_0(): 
    pixels.fill(OFF)
    pixels.show()

# MODE 1: Fade Up
def mode_1():
    # The next 4 lines work kinda like our "for loop"
    # You can imagine we've set it up like this: 
    # for (let color_number = 0, color_number < max_color_number, color_number += 5)
    global color_number                     # global tells the code to look outside the function
    color_number += 5                       # increment our color_number 
    if (color_number > max_color_number):   # if the color_number is too high, set it back to 0
        color_number = 0
    
    # We use our changed color_number to build a color, and show it
    current_color = (color_number, color_number, color_number)
    pixels.fill(current_color)
    pixels.show()

# handleMode runs the code for whatever mode we're on 
def handleMode():
    global mode
    if (mode == 0):
        mode_0()
    elif (mode == 1):
        mode_1()

# handleButton checks if the button is pressed, and changes mode if it is
def handleButton():
    global mode
    global lastSwitchValue
    
    currentSwitchValue = switch.value
    if (currentSwitchValue == False and lastSwitchValue == True): # Only true if we JUST pressed the button
        mode += 1
        if mode >= NUMBER_OF_MODES:
            mode = 0
    
    lastSwitchValue = currentSwitchValue

while True:
    handleButton()
    handleMode()
    time.sleep(0.1) # take a break from checking


