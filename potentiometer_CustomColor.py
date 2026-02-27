# Created: 2025-05-14
# Written for CircuitPython 3.1.1
import time
import analogio
import board
import neopixel
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

pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

red = 100
green = 150
blue = 200

dial_min = 1300 # needs to be close but a little higher than the actual min value you observe
dial_max = 65000 # needs to be close but a little lower than the actual max value you observe
smoothed_dial_value = 0

while True:
    time.sleep(0.01)
    smoothed_dial_value = smooth(dial.value, smoothed_dial_value, 0.2)
    print("raw: ", dial.value)
    if dial_max > dial_min:
        normalized_dial_value = range_map(smoothed_dial_value, dial_min, dial_max, 0, 1)
    else:
        normalized_dial_value = 0
    if normalized_dial_value < 0.02:
        normalized_dial_value = 0
    print("normed value:", normalized_dial_value)
    pixels.fill((int(red * normalized_dial_value), int(green * normalized_dial_value), int(blue * normalized_dial_value)))
    pixels.show()
