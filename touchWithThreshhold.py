import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import touchio


touch_pad = board.A0 # the ~1 pin
high_threshold = 4059
low_threshold = 3400
touch = touchio.TouchIn(touch_pad)


pixel_pin = board.D2
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.999, auto_write=False)

RED = (255, 0, 0)
ORANGE = (255, 45, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
WHITE = (255,255,255)
MODERN = (70,50,10)
OFF = (0,0,0)

colors = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE,MODERN,WHITE,OFF]
now=0

while True:
    time.sleep(0.15)
    if touch.raw_value < high_threshold and touch.raw_value > low_threshold:
        now=now+1
        print(now)
        print("touched")
        if (now >= len(colors)): #check to see if we exceed our list of colors
            now=0
        pixels.fill(colors[now])
        pixels.show()
    
