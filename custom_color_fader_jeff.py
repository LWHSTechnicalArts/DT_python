# Custom Color Fader

# Universal color fader helper function
# This will fade between two colors at an even rate.

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

YELLOW = (255, 150, 0)
PURPLE = (180, 0, 255)
RED = (255, 0, 0)

# helper functions for fading - advanced version
# start with the simpler version linked above this one — 
# it is less elegant but easier to read and understand —
# and then continue to this solution,
# which is more like what a programmer would actually do in Python
#
# to understand this version...
    # ...study functions
    # ...study zip —
    # https://docs.python.org/3.3/library/functions.html#zip
    # ...study list comprehensions —
    # https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

def crossfade(from_color, to_color, step_wait_time):
    print('-' * 10, 'FADING FROM', from_color, 'TO', to_color, '...', '-' * 10)
    time.sleep(1)
    # more advanced programmers use list comprehensions
    # to work with entire lists at a time in each line
    rgb_changes = [to_value - from_value for to_value, from_value in zip(to_color, from_color)]
    abs_changes = [abs(change) for change in rgb_changes]
    max_abs_change = max(abs_changes)
    rgb_increments = [int(change / abs(change)) for change in rgb_changes]
    now_color = from_color

    for i in range(0, max_abs_change):
        # increment the color
        incremented_color = []
        for now_color_value, to_color_value, increment in zip(now_color, to_color, rgb_increments):
            incremented_value = now_color_value if now_color_value == to_color_value else now_color_value + increment
            incremented_color.append(incremented_value)
        now_color = incremented_color
        # display the color
        print('now_color:', now_color)
        for i in range(len(pixels)):
            pixels[i] = tuple(now_color)
        pixels.show()
        # wait for the specified step wait time 
        time.sleep(step_wait_time)

while True:
    crossfade(PURPLE, YELLOW, 0)
    crossfade(YELLOW, PURPLE, 0)
