#Adapted from Adafruit NeoPixel animations:
#https://learn.adafruit.com/qt-py-and-neopixel-leds/basic-animations-for-qt-py

import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D10
num_pixels = 64

spiral_translate = [33,26,42,25,27,41,19,43,34,18,49,20,32,40,11,48,24,17,53,10,44,39,12,54,21,28,52,5,47,35,13,59,9,31,50,4,55,23,16,60,6,45,38,3,58,8,29,61,1,56,36,14,63,7,30,51,2,57,22,15,62,0,46,37]

spiral_arms_91translate= [11,11,5,5,6,6,7,33,26,19,10,9,8,22,20,21,21,23,36,36,37,24,24,35,35,38,51,51,25,34,39,39,50,61,62,40,40,52,60,60,63,63,41,53,53,59,58,58,57,42,49,54,54,55,56,46,48,48,47,47,45,45,30,43,44,44,31,29,29,15,32,32,28,28,16,14,14,27,17,17,13,3,3,2,18,12,12,4,1,1,0]

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
pixels.brightness = 0.2

def rainbow_stripes():
    for i in range(5):
      for color_index in range(255,0,-1):
        for pixel in range(num_pixels):
          pixel_index = (pixel * 256 // num_pixels) + color_index
          pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()

def rainbow_concentric():
    for i in range(5):
      for color_index in range(255):
        for pixel in range(num_pixels):
          pixel_index = (pixel * 256 // num_pixels) + color_index
          pixels[spiral_translate[pixel]] = colorwheel(pixel_index & 255)
        pixels.show()

def rainbow_spirals():
    for i in range(5):
      for color_index in range(255):
        for pixel in range(91):
          pixel_index = (pixel * 256 // 91) + color_index
          pixels[spiral_arms_91translate[pixel]] = colorwheel(pixel_index & 255)
        pixels.show()

while True:
   rainbow_spirals()
   rainbow_stripes()
   rainbow_concentric()