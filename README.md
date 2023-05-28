# HackerBox #0091 - Fibonacci

HackerBox #0091 can be [purchased here](https://hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0091-fibonacci) and [built from the instructions](https://www.instructables.com/HackerBox-0091-Fibonacci/).

This repo collects the kit's sketches and dependencies into a single place, with varying success.

## Setup

Pre-requisites:

* [VSCode](https://code.visualstudio.com/download)
* [PlatformIO for VSCode](https://platformio.org/install/ide?install=vscode)

After cloning this repo, open the `hackerbox-0091.code-workspace` file in VSCode.

In VSCode, select the desired Default Environment from the PlatformIO toolbar. See [Multi-root Workspaces](https://code.visualstudio.com/docs/editor/multi-root-workspaces) for more information about MultiRoot Workspaces in VS Code.

## Contents

The VSCode workspace file (`.code-workspace`) contains the following projects.

### Welcome to CircuitPython

An attempt to get the CircuitPython and Raspberry Pi Pico to work in via Platform IO.

So far, no luck. A key reason I want to use Platform IO is the library management, but in the end, I just used the [Code with Mu](https://codewith.mu/) editor to get the CircuitPython code running on the Pico, which overall is a great experience for the experimenting, however the library management is all manual.

After some searching, I see this is an ongoing discussion:
* GitHub Issues [Support for Raspberry Pi Pico](https://github.com/platformio/platformio-core/issues/728)
* _missing?_ The PlatformIO [CircuitPython on Raspberry PI Pico](https://community.platformio.org/t/circuitpython-on-raspberry-pi-pico/19887/2).
* The PlatformIO [official PlatformIO Arduino ide support for the Raspberry Pi Pico is now available](https://community.platformio.org/t/official-platformio-arduino-ide-support-for-the-raspberry-pi-pico-is-now-available/20792/8)

Some other resources:
https://docs.platformio.org/en/stable/boards/atmelsam/adafruit_circuitplayground_m0.html
https://docs.platformio.org/en/stable/boards/index.html#raspberry-pi-rp2040

### Always Blue

A slight modification of the original where now the LED is always blue, but alternates between two brightness. It also includes parts of the Welcome to CircuitPython project. This version made it somewhat easier to test while soldering the LEDs.

### Rainbow Demo

Renamed, otherwise unchanged.

### Badge Demo 

Renamed, otherwise unchanged.
