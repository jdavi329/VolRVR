# Oct 29
# Python Example for Drive, set LED, and set LCD
# Fall EF230
# Dr Amy Biegalski
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
    await asyncio.sleep(2)
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
    myOLED.print("Hi DrB")
    myOLED.display()
    # Delay
    await asyncio.sleep(1)
    # check time
    start_time = time.time()
    elapsed_time = time.time() - start_time
    # go straight for 10 seconds
    while elapsed_time <=10:
        await rvr.drive_with_heading(speed=90,heading=0,flags=0)
        # Delay to allow RVR to drive
        await asyncio.sleep(1)
        elapsed_time = time.time() - start_time
    # after 10 second drive, turn right.
    # raw_motors inputs are (left_mode, left_speed, right_mode, right_speed
    await rvr.raw_motors(2,255,1,255)  # Valid speed values are 0-255
    print("turning right")
    await rvr.reset_yaw()
    # Delay
    await asyncio.sleep(1)
    # Stop and close
    await rvr.drive_with_heading(speed=0,heading=0,flags=DriveFlagsBitmask.none.value)
    await rvr.close()

    if __name__ == '__main__':
        try:
            loop.run_until_complete(
                main()
            )

        except KeyboardInterrupt:
            print('Program terminated by Keyboard Interrupt')
            time.sleep(.1)
            rvr.close()
