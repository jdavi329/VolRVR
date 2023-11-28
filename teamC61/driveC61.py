# EF 230 Python RVR Project 
# November 11, 2021
# Isabella Macher, Kailyn Hoaglund, John-Dalton Drake
# Fall EF230
# Problem: 
# Solution: 

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
from sphero_sdk import RvrLedGroups 
# import qwiic functions
import qwiic_micro_oled
import sys
import qwiic
import time 
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
    await rvr.led_control.set_all_leds_rgb(red=127, green=0, blue=255)
    # Display message on lcd
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)  #  Clear display
    myOLED.set_font_type(0)
    myOLED.set_cursor(0,0)
    myOLED.print("Hi Isabella, Kailyn, and John-Dalton")
    myOLED.display()
  # Inilialize Senors 
    ToF=qwiic.QwiicVL53L1X()
    ToF.sensor_init()
    # Delay
    await asyncio.sleep(1)
    # check time
    start_time = time.time()
    elapsed_time = time.time() - start_time
    # go straight for 2 seconds
    while elapsed_time <=2:
        await rvr.drive_with_heading(speed=90,heading=0,flags=0)
        # Delay to allow RVR to drive
        await asyncio.sleep(1)
        elapsed_time = time.time() - start_time
    # after 2 second drive, turn right.
    # raw_motors inputs are (left_mode, left_speed, right_mode, right_speed
    await rvr.drive_with_heading(speed=60,heading=180,flags=0)  # Valid speed values are 0-255
    await asyncio.sleep(1)
    print("turning around")
    await rvr.reset_yaw()  # adjust current heading to 0 degrees
    # Delay 
    await asyncio.sleep(1)
    start_time = time.time()
    elapsed_time = time.time() - start_time
    # go straight for 2 seconds 
    while elapsed_time <=10:
        ToF.start_ranging()
        time.sleep(.005)
        distance = ToF.get_distance()
        time.sleep(.005)  
        if distance <=350:
            await rvr.drive_with_heading(speed=0,heading=0,flags=0)
            await asyncio.sleep(1)
            break
        await rvr.drive_with_heading(speed=90,heading=0,flags=0)
        # Delay to allow RVR to drive
        await asyncio.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

    # Delay
    await asyncio.sleep(1)
    # Change LEDs
    await rvr.led_control.set_multiple_leds_with_enums(
        leds=[
           RvrLedGroups.headlight_left,
           RvrLedGroups.headlight_right
        ],
        colors=[
           Colors.yellow,
           Colors.pink
        ]
   )
    # Stop and Close
    await rvr.drive_with_heading(speed=0,heading=0,flags=0)
    await rvr.close()
if __name__ == '__main__':
    try:
        loop.run_until_complete(
            main()
        )

    except KeyboardInterrupt:
        rvr.close()
