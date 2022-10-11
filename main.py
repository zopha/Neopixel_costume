from neopixel import Neopixel
from time import sleep

## Setup
NUM_LEDS = 32
LED_PIN = 16
pixels = Neopixel(NUM_LEDS, 0, LED_PIN, "GRB")

## Constants
red = pixels.colorHSV(0, 255, 255)
green = pixels.colorHSV(21845, 255, 255)
blue = pixels.colorHSV(43691, 255, 255)

## Loop #1 
#while True:
#    for color in [red, green, blue]:
#        pixels. fill(color)
#        pixels.show()
#        sleep(0.5)

## Loop #2
while True:
    for hue in range(0, 65535, 100):
        color = pixels.colorHSV(hue, 255, 25)
        pixels.fill(color)
        pixels.show()
        sleep(0.1)