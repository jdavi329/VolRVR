# EF230 base program
# make edits to this code and save as a different filename
# Objective:  drive, turn on LEDS, use OLEDs, get sensor readings

import spheroRVR
import time
# drive forward
spheroRVR.setDriveSpeed(0.75,0.75)  # leftwheel, rightwheel, Valid velocity values are [-127..127]
time.sleep(1)
# stop
spheroRVR.setDriveSpeed(0,0)  
# turn
spheroRVR.setDriveSpeed(-1.5,1,5)  
time.sleep(0.5)
spheroRVR.setDriveSpeed(0,0)  
