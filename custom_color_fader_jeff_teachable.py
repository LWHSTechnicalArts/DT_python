# Created: 2025-05-15
# Written for CircuitPython 3.1.1
# Custom Color Fader

# Universal color fader helper function
# Start with this version to understand the process,
# and then have a look at the more Pythonic solution linked below this one,
# to see how an experienced programmer would solve this problem in Python.
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


def crossfade(from_color, to_color, step_wait_time):
    print('-' * 10, 'FADING FROM', from_color, 'TO', to_color, '...', '-' * 10)
    time.sleep(1)
    # How can we fade between any two given colors, no matter their red, green, and blue values?
    # We need to answer a few questions about our two colors first.

    # Because we want to change red, green, and blue separately,
    # let's pull out red, green, and blue separately from our from_color and our to_color.
    from_r, from_g, from_b = from_color
    to_r, to_g, to_b = to_color

    # How much do red, green, and blue increase or decrease as we move from from_color to to_color?
    change_r = to_r - from_r
    change_g = to_g - from_g
    change_b = to_b - from_b

    # Which color changes the most on the way from from_color to to_color, no matter whether decreasing or increasing in value?
    # We use the abs() function to get the absolute value of our changes, and we choose the largest value.
    max_abs_change = max([abs(change_r), abs(change_g), abs(change_b)])

    # Should red, green, and blue increase or decrease on the way from from_color to to_color?
    # We compare the absolute value of each change against the true value to arrive at a 1 or a -1 for each color.
    # An increment of -1 will decrease the color's value, while an increment of 1 will increase the color's value.
    increment_r = int(change_r / abs(change_r)) if change_r !=0 else 0
    increment_g = int(change_g / abs(change_g))if change_g !=0 else 0
    increment_b = int(change_b / abs(change_b)) if change_b !=0 else 0

    # We'll start our fade at from_color,
    # and keep track of the in-between colors with now_color.
    # This means we want to start with now_color equal to from_color.
    now_color = from_color
    # perform the fade
    for i in range(0, max_abs_change): # The number of steps in our change is the number of values in the largest change (see line 41).
        now_r, now_g, now_b = now_color
        # If we have not arrived at the to_color value, increment the value.
        new_r = now_r if to_r == now_r else now_r + increment_r
        new_g = now_g if to_g == now_g else now_g + increment_g
        new_b = now_b if to_b == now_b else now_b + increment_b
        
        now_color = (new_r, new_g, new_b) # We overwrite now_color with our new color,
        # and then we light up and log the new color
        print('now_color:', now_color)
        for i in range(len(pixels)):
            pixels[i] = tuple(now_color)
        pixels.show()
        time.sleep(step_wait_time) # Wait this long before the next step in our change.

while True:
    crossfade(PURPLE, YELLOW, 0)
    crossfade(YELLOW, PURPLE, 0)
