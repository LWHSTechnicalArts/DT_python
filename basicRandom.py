# Created: 2026-02-12
# Written for CircuitPython 3.1.1
import board
import neopixel
import random

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

while True:
    pixels[0] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pixels.show()
