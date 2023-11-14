#by Ethan Dunn
import time 
import board 
import neopixel

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

RED = (255, 0, 0) 
YELLOW = (255, 150, 0) 
GREEN = (0, 255, 0) 
CYAN = (0, 255, 255) 
BLUE = (0, 0, 255) 
PURPLE = (180, 0, 255) 
WHITE = (255, 255, 255) 
OFF = (0, 0, 0) 
COLOR = WHITE

while True: 
    for c in range(0, 5, 1): 
        if (c == 0): 
            COLOR = RED 
        if (c == 1): 
            COLOR = YELLOW 
        if (c == 2): 
            COLOR = GREEN 
        if (c == 3): 
            COLOR = CYAN 
        if (c == 4): 
            COLOR = BLUE 
        if (c == 5): 
            COLOR = PURPLE 
        for i in range(0, 16, 1): 
            pixels[i] = COLOR 
            pixels.show() 
            time.sleep(0.1)
