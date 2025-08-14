# Write your code here :-)
import board
import time
import digitalio
import neopixel
import math
import analogio 

# ============================
NEOPIXEL_PIN = board.D2        
NUM_PIXELS = 16                
BUTTON_PIN = board.D3          
POTENTIOMETER_PIN = board.A2  
# ============================


pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NUM_PIXELS, brightness=1.0, auto_write=False)


button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


potentiometer = analogio.AnalogIn(POTENTIOMETER_PIN)

def hsv_to_rgb(h, s, v):
    i = int(h * 6)
    f = (h * 6) - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)


MODE_RAINBOW = 0
MODE_ALTERNATE = 1
mode = MODE_RAINBOW
last_button_state = True

hue = 0.0
step = 0.005

while True:
    
    pot_value = potentiometer.value 
    print(pot_value)
    scaled_brightness = pot_value / 65535.0

    
    current_button_state = button.value
    if not current_button_state and last_button_state:
        mode = MODE_ALTERNATE if mode == MODE_RAINBOW else MODE_RAINBOW
        print("Mode:", "ALT" if mode == MODE_ALTERNATE else "RAINBOW")
        time.sleep(0.2) 
    last_button_state = current_button_state

   
    if mode == MODE_RAINBOW:
        rgb = hsv_to_rgb(hue, 1.0, 1.0)
        hue += step
        if hue > 1.0:
            hue = 0.0
    elif mode == MODE_ALTERNATE:
        wave = (math.sin(time.monotonic()) + 1) / 2
        rgb = hsv_to_rgb(wave * 0.66, 1.0, 1.0)

    
    scaled_rgb = tuple(int(c * scaled_brightness) for c in rgb)

    
    for i in range(NUM_PIXELS):
        pixels[i] = scaled_rgb
    pixels.show()

    time.sleep(0.01)