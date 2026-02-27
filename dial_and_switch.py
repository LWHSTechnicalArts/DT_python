# Created: 2021-06-07
# Written for CircuitPython 3.1.1
# dial_and_switch

import time
import board
import neopixel
import math
import analogio

def range_map(value, from_min, from_max, to_min, to_max):
    from_range = from_max - from_min
    to_range = to_max - to_min
    value_scaled = (value - from_min) / from_range
    return value_scaled * to_range + to_min

def smooth(new_value, previous_smoothed, smoothing_factor):
    weight_of_new = smoothing_factor * new_value
    weight_of_old = (1 - smoothing_factor) * previous_smoothed
    return weight_of_new + weight_of_old
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

dial_pin = board.A2  # pin 0 is Analog input 2
dial = analogio.AnalogIn(dial_pin)

pixel_pin = board.D2
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels,
                           brightness=0.3, auto_write=False)

now = 0

dial_min = 1300 # needs to be close but a little higher than the actual min value you observe
dial_max = 65000 # needs to be close but a little lower than the actual max value you observe
smoothed_dial_value = 0

while True:
    time.sleep(0.01)
    smoothed_dial_value = smooth(dial.value, smoothed_dial_value, 0.1)
    if smoothed_dial_value < 0.01:
        smoothed_dial_value = 0
    print("raw: ", dial.value)
    if dial_max > dial_min:
        normalized_dial_value = range_map(smoothed_dial_value, dial_min, dial_max, 0, 1)
    else:
        normalized_dial_value = 0
    if smoothed_dial_value < 0.01:
        smoothed_dial_value = 0
    print("normed value:", normalized_dial_value)
    color_val = int(255 * normalized_dial_value)
    if (switch.value == 0):  # detect the button press, 0 means pressed
        now = now+1
        if (now >= len(colors)):  # check to see if we exceed our list of colors
            now = 0
        time.sleep(0.2)  # debounce delay

    RED = (color_val, 0, 0)
    YELLOW = (color_val, int(color_val/2), 0)
    GREEN = (0, color_val, 0)
    CYAN = (0, color_val, color_val)
    BLUE = (0, 0, color_val)
    PURPLE = (int(color_val/3), 0, color_val)
    WHITE = (color_val, color_val, color_val)
    OFF = (0, 0, 0)

    colors = [OFF, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

    dialcolor = colors[now]
    print(dialcolor[0], dialcolor[1], dialcolor[2])

    pixels.fill(dialcolor)
    pixels.show()
    time.sleep(0.1)
