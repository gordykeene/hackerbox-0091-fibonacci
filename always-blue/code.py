# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Welcome_to_CircuitPython/code.py

import time
import board
import neopixel

num_pixels = 64
pixels = neopixel.NeoPixel(board.D10, num_pixels)
pixels.brightness = 0.2

pixelOnBoard = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    pixelOnBoard.fill((0, 0, 255))
    pixels.fill((0, 0, 255))

    time.sleep(0.5)

    pixelOnBoard.fill((0, 0, 0))
    pixels.fill((0, 0, 128))

    time.sleep(0.5)
