import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.D2
num_pixels = 16
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

colors = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]
now = 0

# ---- NEW: fade helper function and settings ----
FADE_STEPS = 50
FADE_DELAY = 0.02

def map_range(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def fade(start_color, end_color, steps):
    for step in range(steps + 1):
        r = int(map_range(step, 0, steps, start_color[0], end_color[0]))
        g = int(map_range(step, 0, steps, start_color[1], end_color[1]))
        b = int(map_range(step, 0, steps, start_color[2], end_color[2]))
        pixels.fill((r, g, b))
        pixels.show()
        time.sleep(FADE_DELAY)
# ---- END OF NEW STUFF ----

while True:
    print(switch.value)
    if (switch.value == False):    #detect the button press
        old = now              # NEW: remember where we are before changing
        now = now + 1 
        if (now >= 7): #7 colors in the list
            now = 0
        fade(colors[old], colors[now], FADE_STEPS)  # CHANGED: fade instead of fill
        pixels.show()
    time.sleep(0.12)  # debounce delay
