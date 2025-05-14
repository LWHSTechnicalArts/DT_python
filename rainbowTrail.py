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

colors = [RED, YELLOW, GREEN, OFF]

# Main loop
while True:
    print("running")
    for offset in range(0,num_pixels,1):
        pixels.fill((0, 0, 0))  # Turn off all pixels
        for i in range(0,4,1):
            index = (offset + i) % num_pixels
            pixels[index] = colors[i]
        pixels.show()
        time.sleep(0.1)
