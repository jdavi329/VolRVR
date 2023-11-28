# Autonomous RVR
# EF230 Section F(3)
# Christian Ramsey, Jacob McClaren
# Created: November 9th, 2021
# Project Description:
# Make a python script that controls an RVR using at least one loop and at least one conditional
# Project Method:
# The RVR uses the distance sensor to determine whether or not it is within 12 inches of an object. If it is not then the LEDs turn green and the RVR drives forward. If it is then the LEDs turn red and the OLED screen displays "too close" and the RVR turns 30 degrees
# until it is no longer within 12 inches of an object.
import qwiic_micro_oled
import sys
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))
import qwiic
import qwiic_vl53l1x
import qwiic_micro_oled
import time
import asyncio

from sphero_sdk import SerialAsyncDal
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import RawMotorModesEnum
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

# creates an async/await loop for timing
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
     dal=SerialAsyncDal(
                      loop
     )
)

async def main():
# Runs the main control loop
    # Initialize global variables
    global speed
    global heading
    global flags

    await rvr.wake()
    await asyncio.sleep(1)
    await rvr.reset_yaw()

    ToF=qwiic.QwiicVL53L1X()
    ToF.sensor_init()
    print("\nReady to Roll\n")
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)  #  Clear display
    myOLED.set_font_type(0)
    myOLED.set_cursor(0,0)
    myOLED.print("Vol RVR")
    myOLED.set_cursor(0,15)
    myOLED.print("Dist(mm)")
    myOLED.display()

    if(ToF.sensor_init()==None):
        print("Sensor online\n")
    while True:
        try:
            ToF.start_ranging()
            time.sleep(.005) # use .005 for drive mode
            distance = ToF.get_distance()    # Get the result of the measuremen$
            time.sleep(.005) # use .005 for drive mode
            ToF.stop_ranging()
            distI = distance / 25.4
            distF = distI / 12.0
            print("Distance(mm): %5.0f Distance(in): %5.3f" % (distance, distI))
            myOLED.set_cursor(0,30)
            myOLED.print("    ")
            myOLED.display()
            myOLED.print("%5.0f" % distance)
            myOLED.display()
            # If case for when the RVR is within 12 inches of an object (gives plenty of time to complete turn because the sensors are delayed)
            if(distI < 12):
               # OLED screen prints "Too Close"
               myOLED.print(" Too Close")
               # Turns the RVRs LEDs red
               await rvr.led_control.set_all_leds_rgb(red=255,green=0,blue=0)
               # Turns the RVR in 15 degree intervals until it is no longer within 12 inches of an object
               await rvr.drive_with_heading(speed=0,heading=15,flags=0)
               # Pauses allowing the RVR to drive
               await asyncio.sleep(0.5)
               # Resets heading so RVR drives straight again
               await rvr.reset_yaw()
            # IF case for when the RVR is not within 12 inches of an object
            if(distI > 12):
               # Clears the OLED panel
               myOLED.print("                               ")
               # Turns the LEDs green
               await rvr.led_control.set_all_leds_rgb(red=0, green=255, blue=0)
               # Sets the drive speed to 50 and heading to 0 so forward
               await rvr.drive_with_heading(speed=50,heading=0,flags=0)
        except Exception as e:
            print("Ctrl-C terminated process") # will terminate if you use ctrl-c
# Calls the main loop
if __name__ == '__main__':
   try:
      loop.run_until_complete(
          main()
      )
   except KeyboardInterrupt:
      rvr.close()
