Vol RVR Sphero Toolbox

These files allow students to program and control Sphero RVR robots wirelessly via a Raspberry Pi using Python.

Files built from Sparkfun and Sphero github repositories (see below) for use in University of Tennessee's Engineering Fundamentals Program

Recommended Hardware
Raspberry Pi 3B+ (recommended), PiZero or Pi4
micro SD card 32 GB
Raspberry Pi Camera
Sparkfun Qwiic MicroOLED
Sparkfun Qwiic vl53l1x ToF Distance Sensor
(Optional) 2 servo Pan-Tilt camera mount
Sparkfun Servo pHat for Raspberry Pi (Qwiic I2C bus for Qwiic & 4-pin header for Sphero RVR)
note:
Sparkfun Autonomous Kit for the Sphero RVR includes most of these peripherals

Sphero RVR Hardware Setup

If using Sparkfun PiServo pHat, toggle servo pi hat switch to "RVR"
use a short, high-quality cable to connect raspberry pi USB 2.0 B micro power input to USB 2.0 A input on RVR
connect the four pin connector on the Servo pHAT to the 4 pin UART Connector on the RVR.

Raspberry Pi Software Setup Instructions
https://github.com/JoshFagan/sphero_toolbox/blob/master/pi_installation.md

Configure wi-fi  on the Raspberry Pi  - edit wpa_supplicant.conf to include your wi-fi network


Adapted from:

SparkFun Electronics sparkfun_autonomous_kit https://github.com/sparkfun/sparkfun_autonomous_kit
Copyright 2019 SparkFun Electronics Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Sphero, Inc.  sphero-sdk-raspberrypi-python  https://github.com/sphero-inc/sphero-sdk-raspberrypi-python
https://github.com/sphero-inc/sphero-sdk-raspberrypi-python/blob/master/LICENSE.md

