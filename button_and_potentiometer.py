# Created: 2023-02-10
# Written for CircuitPython 3.1.1
# button_and_potentiometer

import time
import analogio
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import math

def range_map(value, from_min, from_max, to_min, to_max):
    from_range = from_max - from_min
    to_range = to_max - to_min
    value_scaled = (value - from_min) / from_range
    return value_scaled * to_range + to_min

def smooth(new_value, previous_smoothed, smoothing_factor):
    weight_of_new = smoothing_factor * new_value
    weight_of_old = (1 - smoothing_factor) * previous_smoothed
    return weight_of_new + weight_of_old

dial_pin = board.A2 #pin 0 is Analog input 2
dial = analogio.AnalogIn(dial_pin)

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

YELLOW = (255, 150, 0)
OFF = (0,0,0)

now = 0
dial_min = 1300 # needs to be close but a little higher than the actual min value you observe
dial_max = 65000 # needs to be close but a little lower than the actual max value you observe
smoothed_dial_value = 0

while True:
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
    if (switch.value==False):    #detect the button press
        now = now + 1
        if (now >1):
            now = 0
    if(now == 0):
        pixels.fill(OFF)
        pixels.show()
    if(now == 1):
        print(normalized_dial_value)
        color = (int(255 * normalized_dial_value), int(255 * normalized_dial_value), int(255 * normalized_dial_value))
        print("color: ", color)
        pixels.fill(color)
        pixels.show()
    time.sleep(0.12)  # debounce delay
