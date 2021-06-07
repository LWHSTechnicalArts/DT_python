import time
import board
import neopixel
import math
import analogio
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

dial_pin = board.A2  # pin 0 is Analog input 2
dial = analogio.AnalogIn(dial_pin)

pixel_pin = board.D2
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels,
                           brightness=0.3, auto_write=False)

now = 0

while True:
    if (switch.value == 0):  # detect the button press, 0 means pressed
        now = now+1
        if (now >= len(colors)):  # check to see if we exceed our list of colors
            now = 0
        time.sleep(0.2)  # debounce delay
    # scale down potentiometer values to fit within color range
    val = int(math.sqrt(dial.value)-20)
    print(val)

    RED = (val, 0, 0)
    YELLOW = (val, int(val/2), 0)
    GREEN = (0, val, 0)
    CYAN = (0, val, val)
    BLUE = (0, 0, val)
    PURPLE = (int(val/3), 0, val)
    WHITE = (val, val, val)
    OFF = (0, 0, 0)

    colors = [OFF, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

    dialcolor = colors[now]
    print(dialcolor[0], dialcolor[1], dialcolor[2])

    pixels.fill(dialcolor)
    pixels.show()
    time.sleep(0.1)
