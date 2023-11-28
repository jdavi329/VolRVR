# Nov 16, 2021
# Python code that makes Rover Look both ways before crossing the road
# Fall EF230
# Levi Matthews, David Dabkowski, and Robert Lyszczarczyk
# Purpose: To make a unique python code that programs our rover
# Method: We used while loops to make our Rover move foward, and we used other python commands to make our rover at a specified angle.

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
import sys
import qwiic
# initialize global variables
speed = 0
heading = 0
flags = 0
green1 = [0, 255, 0]
green2 = [0, 128, 0]

# this example will use async/await
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

async def main():
#  Runs the main control loop
    global speed
    global heading
    global flags
    await rvr.wake()
    # Give RVR time to wake up
    await asyncio.sleep(1)
    # set current heading as zero
    await rvr.reset_yaw()
    # change all LED Colors
    await rvr.led_control.set_all_leds_rgb(red=255, green=130, blue=0)
    # Display message on lcd
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)  #  Clear display
    myOLED.set_font_type(0)
    myOLED.set_cursor(0,0)
    myOLED.print("Look both ways before crossing the street") #Displays the text "Moving Foward" on the Rover's display screen 
    myOLED.display()
    # Delay
    await asyncio.sleep(1)
    # check time
    start_time = time.time()
    elapsed_time = time.time() - start_time
    # go straight for 3 seconds
    while elapsed_time <=3:
        await rvr.drive_with_heading(speed=90,heading=0,flags=0) # Rover Drives foward for 3 seconds
        # Delay to allow RVR to drive
        await asyncio.sleep(1)
        elapsed_time = time.time() - start_time
    # raw_motors inputs are (left_mode, left_speed, right_mode, right_speed
    # Valid speed values are 0-255
    await asyncio.sleep(1)
    print("turning right") # Displays text "turning right" in terminal
    await rvr.drive_control.turn_right_degrees(heading=0,amount=90) #Robot turns 90 degrees right
    await asyncio.sleep(1)
    await rvr.reset_yaw()  # adjust current heading to 0 degrees
    print("turning left") # Displays text "turning left" in terminal
    await rvr.drive_control.turn_left_degrees(heading=0,amount=90)
    await asyncio.sleep(1)
    await rvr.reset_yaw() # adjust current heading to 0 degrees
    print("turning left") # Displays text "turning left" in termianl
    await rvr.drive_control.turn_left_degrees(heading=0,amount=90)
    await asyncio.sleep(1)
    await rvr.reset_yaw() # adjust current heading to 0 degrees
    print("turning right") # Displays text "turning right" on Rover's display screen
    await rvr.drive_control.turn_right_degrees(heading=0,amount=90) #Robot turns 90 degrees right
    await asyncio.sleep(1)
    print("Moving Foward") # Displays text "Moving Foward" on Rover's display screen
    await rvr.reset_yaw() # adjust current heading to 0 degrees
    start_time = time.time()
    elapsed_time = time.time() - start_time
    # go straight for 2.5 seconds
    if elapsed_time <=2.5:
        await rvr.drive_with_heading(speed=90,heading=0,flags=0)
        # Delay to allow RVR to drive
        await asyncio.sleep(2)
        # elapsed_time = time.time() - start_time

    # Stop and close
    await rvr.drive_with_heading(speed=0,heading=0,flags=0)
    await rvr.close()

if __name__ == '__main__':
    try:
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        rvr.close()
