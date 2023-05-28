import time
import board
import neopixel
import random
import touchio
from rainbowio import colorwheel

pixel_pin = board.D10
num_pixels = 64

spiral_arms_91translate= [11,11,5,5,6,6,7,33,26,19,10,9,8,22,20,21,21,23,36,36,37,24,24,35,35,38,51,51,25,34,39,39,50,61,62,40,40,52,60,60,63,63,41,53,53,59,58,58,57,42,49,54,54,55,56,46,48,48,47,47,45,45,30,43,44,44,31,29,29,15,32,32,28,28,16,14,14,27,17,17,13,3,3,2,18,12,12,4,1,1,0]

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
pixels.brightness = 0.2
touch1 = touchio.TouchIn(board.D7)

def sparkle():
    num_leds_on = 20
    leds_on = [0] * num_leds_on
    while True:
      next_led_on = random.randint(0, 63)
      next_color = random.randint(0, 255)
      next_pos_off = random.randint(0, (num_leds_on-1))
      pixels[next_led_on] = colorwheel(next_color)
      pixels[leds_on[next_pos_off]] = (0,0,0)
      leds_on[next_pos_off] = next_led_on
      pixels.show()
      if touch1.value:
        time.sleep(0.5)
        return

def rainbow_spirals():
    while True:
      for color_index in range(255):
        for pixel in range(91):
          pixel_index = (pixel * 256 // 91) + color_index
          pixels[spiral_arms_91translate[pixel]] = colorwheel(pixel_index & 255)
        pixels.show()
        if touch1.value:
          time.sleep(0.5)
          return

while True:
    sparkle()
    rainbow_spirals()