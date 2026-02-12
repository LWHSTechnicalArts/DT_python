import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D2
num_pixels = 16

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

mode = 0
NUMBER_OF_MODES = 2

YELLOW = (255, 150, 0)
GREEN = (20, 210, 100)
ORANGE = (235, 150, 35)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def handleButton():
    global mode
    buttonWasPressed = False

    if switch.value == False:
        mode += 1
        if mode >= NUMBER_OF_MODES:
            mode = 0
        # Wait for button release so one press = one mode change
        while switch.value == False:
            time.sleep(0.01)
        buttonWasPressed = True
        print("changing modes!")

    return buttonWasPressed

def mode0():
    print("in mode 0")
    pixels[0] = GREEN
    pixels.show()
    pixels[2] = GREEN
    pixels.show()
    pixels[1] = ORANGE
    pixels.show()
    pixels[3] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[0] = ORANGE
    pixels.show()
    pixels[2] = ORANGE
    pixels.show()
    pixels[1] = GREEN
    pixels.show()
    pixels[3] = GREEN
    pixels.show()
    if handleButton(): return

    pixels[4] = GREEN
    pixels.show()
    pixels[5] = GREEN
    pixels.show()
    pixels[6] = ORANGE
    pixels.show()
    pixels[7] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[4] = ORANGE
    pixels.show()
    pixels[5] = ORANGE
    pixels.show()
    pixels[6] = GREEN
    pixels.show()
    pixels[7] = GREEN
    pixels.show()
    if handleButton(): return

    pixels[8] = GREEN
    pixels.show()
    pixels[9] = GREEN
    pixels.show()
    pixels[10] = ORANGE
    pixels.show()
    pixels[11] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[8] = ORANGE
    pixels.show()
    pixels[9] = ORANGE
    pixels.show()
    pixels[10] = GREEN
    pixels.show()
    pixels[11] = GREEN
    pixels.show()
    if handleButton(): return

    pixels[12] = GREEN
    pixels.show()
    pixels[13] = GREEN
    pixels.show()
    pixels[14] = ORANGE
    pixels.show()
    pixels[15] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[12] = ORANGE
    pixels.show()
    pixels[13] = ORANGE
    pixels.show()
    pixels[14] = GREEN
    pixels.show()
    pixels[15] = GREEN
    pixels.show()
    if handleButton(): return


def mode1():
    print("in mode 1")
    pixels[0] = YELLOW
    pixels.show()
    pixels[2] = YELLOW
    pixels.show()
    pixels[1] = ORANGE
    pixels.show()
    pixels[3] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[0] = ORANGE
    pixels.show()
    pixels[2] = ORANGE
    pixels.show()
    pixels[1] = YELLOW
    pixels.show()
    pixels[3] = YELLOW
    pixels.show()
    if handleButton(): return

    pixels[4] = YELLOW
    pixels.show()
    pixels[5] = YELLOW
    pixels.show()
    pixels[6] = ORANGE
    pixels.show()
    pixels[7] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[4] = ORANGE
    pixels.show()
    pixels[5] = ORANGE
    pixels.show()
    pixels[6] = YELLOW
    pixels.show()
    pixels[7] = YELLOW
    pixels.show()
    if handleButton(): return

    pixels[8] = YELLOW
    pixels.show()
    pixels[9] = YELLOW
    pixels.show()
    pixels[10] = ORANGE
    pixels.show()
    pixels[11] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[8] = ORANGE
    pixels.show()
    pixels[9] = ORANGE
    pixels.show()
    pixels[10] = YELLOW
    pixels.show()
    pixels[11] = YELLOW
    pixels.show()
    if handleButton(): return

    pixels[12] = YELLOW
    pixels.show()
    pixels[13] = YELLOW
    pixels.show()
    pixels[14] = ORANGE
    pixels.show()
    pixels[15] = ORANGE
    pixels.show()
    if handleButton(): return

    pixels[12] = ORANGE
    pixels.show()
    pixels[13] = ORANGE
    pixels.show()
    pixels[14] = YELLOW
    pixels.show()
    pixels[15] = YELLOW
    pixels.show()
    if handleButton(): return


while True:
    if mode == 0:
        mode0()
    elif mode == 1:
        mode1()
