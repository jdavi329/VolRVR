# A.Biegalski Oct 2020
# For raspberry pi controlled Sphero RVR
# Driving command examples:  straight, drive with heading, and turning 
# For hardware specifications refer to github readme at https://github.com/abiegals/VolRVR/
# 
#
# Adapted from:
# Sphero, Inc. sphero-sdk-raspberrypi-python https://github.com/sphero-inc/sphero-sdk-raspberrypi-python

import sys
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
import os

# allow pull files from two layers above and append path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# time related functions
import time

# import sphero sdk functions
# allow for Observer mode or Await/Async
import asyncio # allow concurrent code using async/await
from sphero_sdk import SerialAsyncDal
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import RawMotorModesEnum
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

# import qwiic functions
import qwiic_micro_oled
import qwiic

# Initial settings
speed = 0
heading = 0
flags = 0

rvr = SpheroRvrObserver()

def main():

    # Runs the main control loop
    global speed
    global heading
    global flags
    rvr.wake()

    # Give RVR time to wake up
    time.sleep(1)

    # set current heading as zero
    rvr.reset_yaw()
    time.sleep(1)

    # check time
    start_time = time.time()
    elapsed_time = time.time() - start_time

    # go straight for 2 seconds
    rvr.drive_with_heading(speed=90,heading=0,flags=0)

    # Delay to allow RVR to drive
    time.sleep(2)
    rvr.drive_with_heading(speed=0,heading=0,flags=0)

    time.sleep(0.5)
    # Just turn
    rvr.drive_control.turn_left_degrees(heading=0,amount=90)

    time.sleep(0.5)
    # Stop and close
    rvr.drive_with_heading(speed=0,heading=0,flags=0)
    rvr.close()


main()
