import time
import board
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import touchio


touch_pad = board.A0 # the ~1 pin
touch = touchio.TouchIn(touch_pad)

pixel_pin = board.D2
num_pixels = 16
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
BLUE = (0,0,255)
OFF = (0,0,0)

colors = [RED,YELLOW,BLUE,OFF]
now=0

while True:
    if touch.value:
        now=now+1
        time.sleep(0.2) # debounce delay
        
        if(now<4): 
            pixels.fill(colors[now])
            pixels.show()
            
        if (now == 4):
            for COLOR in colors: 
                for i in range(0, 16, 1): 
                    pixels[i] = COLOR 
                    pixels.show() 
                    time.sleep(0.1)
                
                    if touch.value:
                        now = now+1
                        break
        if(now>4):
            now=0
            pixels.fill(RED)
            pixels.show()
    time.sleep(0.2) # Write your code here :-)

