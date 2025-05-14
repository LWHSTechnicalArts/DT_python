import time
import analogio
import board
import neopixel
import math


dial_pin = board.A2 #pin 0 is Analog input 2
dial = analogio.AnalogIn(dial_pin)

pixel_pin = board.D2
num_pixels = 16
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

while True:
    time.sleep(0.2)
    #print((math.sqrt(dial.value,)))
    val = int(math.sqrt(dial.value) - 30) #scale down potentiometer values to fit within color range
    if(val<10):
        val=0
    greenVal = int(val/2)
    print(val)
    pixels.fill((val, greenVal, 0))
    pixels.show()
