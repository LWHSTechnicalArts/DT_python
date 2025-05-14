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

# helper functions for fading
# first, to understand this code...
    # ...study zip —
    # https://docs.python.org/3.3/library/functions.html#zip
    # ...study list comprehensions —
    # https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

def crossfade(from_color, to_color, step_wait_time):
    # setup - How much do we change r, g, and b with each step?
    rgb_diffs = [to_value - from_value for to_value, from_value in zip(to_color, from_color)]
    abs_diffs = [abs(diff) for diff in rgb_diffs]
    max_diff = max(abs_diffs)
    rgb_increments = [int(diff/abs(diff)) for diff in rgb_diffs] # choose 1 or -1 for r g and b

    # perform the fade
    now_color = from_color
    for i in range(0, max_diff):
        now_color = increment_color(now_color, to_color, rgb_increments)
        fill_pixels(now_color, num_pixels)
        pixels.show()
        time.sleep(step_wait_time)

def fill_pixels(color, num_pixels):
    for i in range(len(pixels)):
        pixels[i] = tuple(color)

def increment_color(now_color, to_color, rgb_increments):
    incremented_color = []
    for now_color_value, to_color_value, increment in zip(now_color, to_color, rgb_increments):
        incremented_value = now_color_value if now_color_value == to_color_value else now_color_value + increment
        incremented_color.append(incremented_value)
    return incremented_color

while True:
    crossfade(PURPLE, YELLOW, 0)
    crossfade(YELLOW, PURPLE, 0)
