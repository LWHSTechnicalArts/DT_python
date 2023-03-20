import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D2
num_pixels = 16
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255,255,255)
OFF = (0,0,0)

# helper function for fading - do not touch
def fade(c1, c2):
    diff = (c2[0]-c1[0], c2[1]-c1[1], c2[2]-c1[2])
    diffA = [1 if n==0 else abs(n) for n in diff]
    maxDiff = max(diffA)
    index = diffA.index(maxDiff)
    cFade = list(c1)
    increment = [int(diff[i]/diffA[i]) for i in range(3)]
    for i in range(0, maxDiff):
        for n in range(3):
            if(cFade[n] != c2[n]):
                cFade[n] += increment[n]
        pixels.fill(tuple(cFade))
        pixels.show()
        time.sleep(0.01)  # debounce delay
#end helper function

while True:
    fade(PURPLE, YELLOW)
    fade(YELLOW, PURPLE)
    time.sleep(0.5)  # debounce delay

