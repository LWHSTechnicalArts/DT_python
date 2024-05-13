# Interrupting custom fader immediately with switch

# This example updates the custom fader to also include switch input.
# This can be used to swap between two modes.

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# -------------------- Setting up our switch so we can read from it
switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

lastSwitchValue = False

# -------------------- Setting up the LEDs so we can write to them
pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

# -------------------- Color variables
REDORANGE = (255, 60, 0)
YELLOWORANGE = (255, 110, 0)
OFF = (0, 0, 0)

# detectSwitch checks if the switch is pressed, and changes mode if it is
# this function returns True if the switch was pressed.
def detectSwitch():
    global mode
    global lastSwitchValue
    switchWasPressed = False

    currentSwitchValue = switch.value
    if currentSwitchValue != lastSwitchValue:
        switchWasPressed = True

    lastSwitchValue = currentSwitchValue
    return switchWasPressed


# helper function for fading - do not touch
# This function will STOP and return True if the switch was pressed.
def fadeWithButtonInterrupt(c1, c2):
    diff = (c2[0] - c1[0], c2[1] - c1[1], c2[2] - c1[2])
    diffA = [1 if n == 0 else abs(n) for n in diff]
    maxDiff = max(diffA)
    index = diffA.index(maxDiff)
    cFade = list(c1)
    increment = [int(diff[i] / diffA[i]) for i in range(3)]

    for i in range(0, maxDiff):
        for n in range(3):
            if cFade[n] != c2[n]:
                cFade[n] += increment[n]
        pixels.fill(tuple(cFade))
        pixels.show()
        if detectSwitch():  # This needs to be INSIDE our for loop!
            print("switch detected in fade loop")
            return True
        time.sleep(0.01)  # debounce delay
    return False


# end helper function

while True:
    # Mode 1
    print(switch.value)
    if switch.value == True:
        pixels.fill(OFF)
        pixels.show()

        detectSwitch()
    # Mode 2
    elif switch.value == False:
        switchWasPressed = fadeWithButtonInterrupt(
            REDORANGE, YELLOWORANGE
        )  # fade 1, part of mode 2

        if not switchWasPressed:  # If the switch has not been pressed, proceed.
            switchWasPressed = fadeWithButtonInterrupt(
                YELLOWORANGE, REDORANGE
            )  # fade 2, part of mode 2

    time.sleep(0.2)  # take a break from checking
