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
import qwiic_vl53l1x
import qwiic_micro_oled
# import sphero sdk functions Observer mode 
from sphero_sdk import SpheroRvrObserver
rvr = SpheroRvrObserver()
    
    
def setDriveSpeed( speedleft, speedright=None):  # Valid velocity values are [-127..127]
    if speedright is None:
        speedright = speedleft
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
    print("Distance: %f" % (distance))
    return distance

def setOLED( thistuple ):  
    # Initialize display
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()
    # Clear anything that might be displayed
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)
    # Set default font and screen position
    myOLED.set_font_type(0)
    for i in range(len(thistuple)):
        myOLED.set_cursor(0,i*15) 
        # Print text to buffer
        myOLED.print(thistuple[i])
    # Actually push data to OLED display
    myOLED.display()
    return

def setLEDs( colorleft,colorright=None ):  # e g  green
    if colorright is None:
        colorright = colorleft
    rvr.wake()
    # Give RVR time to wake up
    time.sleep(0.5)
    rvr.led_control.turn_leds_off()
    rvr.led_control.set_multiple_leds_with_enums(
        leds=[
            RvrLedGroups.headlight_left,
            RvrLedGroups.headlight_right
        ],
        colors=[
            Colors.colorleft,
            Colors.colorright
        ]
    )
#   or         colors=[
#                255, 0, 0,
#                0, 255, 0
#           ]
    rvr.close()
    return
