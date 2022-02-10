import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.D2
num_pixels = 12
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

press_count=0

red=(255,0,0)
yellow=(255,255,0)

def press_check():
    global press_count
    if (switch.value==False):
        press_count+=1
        if press_count>2:
            press_count=0
        time.sleep(0.3)
    print(press_count)


while True:
    
    press_check()
    if press_count==0:
        pixels.fill(red)
        pixels.show()
        
    if press_count==1:
        pixels.fill(yellow)
        pixels.show()

    if press_count==2:
        for num in range(0,254,2):   #fade in loop
            COLOR=(num,0,num)
            if (switch.value==False):
                press_check()
            for i in range(0,12,1):
                pixels[i]=COLOR
            pixels.show()
        for num in range(254,0,-2):   #fade out loop
            COLOR=(num,0,num)
            for i in range(0,12,1):
                pixels[i]=COLOR
            pixels.show()
