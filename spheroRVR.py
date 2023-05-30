# 30 May 2023
# EF230 with A Biegalski

import sys
import os
# allow pull files from two layers above and append path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# time related functions
import time
# get sparkfun qwiic sensor functions
import qwiic
import qwiic_micro_oled
# import sphero sdk functions Observer mode 
from sphero_sdk import SpheroRvrObserver
rvr = SpheroRvrObserver()
    
    
def setDriveSpeed( speedleft, speedright ):  # Valid velocity values are [-127..127]
    print ("Driving at wheelspeed ", speedleft, " and ", speedright)
    rvr.wake()
    time.sleep(0.2)
    rvr.drive_tank_normalized(
        left_velocity=speedleft,
        right_velocity=speedright
    )
    rvr.close()
    return

def getDistance():
    # Initialize sensors
    ToF=qwiic.QwiicVL53L1X()
    ToF.sensor_init()
    # Use while true loop to continously get distance data
    ToF.start_ranging()
    time.sleep(.005)
    distance = ToF.get_distance()    # Get the result of the measurement
    time.sleep(.005)
    ToF.stop_ranging()
    print("Distance sensor reads: %f" % (distance))
    return

def setOLED( mytext, line=0 ):  # by default print on first line
    # Initialize display
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()
    # Clear anything that might be displayed
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)
    # Set default font and screen position
    myOLED.set_font_type(0)
    myOLED.set_cursor(0,line*15) 
    # Print text to buffer
    myOLED.print(mytext)
    # Actually push data to OLED display
    myOLED.display()
    return
