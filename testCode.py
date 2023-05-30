# EF230 base program
# make edits to this code and save as a different filename
# Objective:  drive, turn on LEDS, use OLEDs, get sensor readings

import spheroRVR
import time
# drive forward
spheroRVR.setDriveSpeed(90,90)  # leftwheel, rightwheel, Valid velocity values are [-127..127]
time.sleep(1)
# stop
spheroRVR.setDriveSpeed(0,0)
# spin
spheroRVR.setDriveSpeed(-85,85)
time.sleep(0.1)
# stop
spheroRVR.setDriveSpeed(0,0)
spheroRVR.getDistance
spheroRVR.clearOLED
spheroRVR.setOLED("hello") # by default print on line 1
time.sleep(3)
spheroRVR.setOLED("friend",2) # print on line 2
