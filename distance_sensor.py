# A.Biegalski Aug 2021
# For raspberry pi controlled Sphero RVR
# prints live distance sensor measurements to control computer 
# For hardware specifications refer to github readme at https://github.com/abiegals/VolRVR/
# 
#
# Adapted from:
# SparkFun Electronics sparkfun_autonomous_kit https://github.com/sparkfun/sparkfun_autonomous_kit
# Sphero, Inc. sphero-sdk-raspberrypi-python https://github.com/sphero-inc/sphero-sdk-raspberrypi-python

import qwiic
import time

def printDist():
    # Initialize sensors
    ToF=qwiic.QwiicVL53L1X()
    ToF.sensor_init()

    # Use while true loop to continously get distance data
    while True:
        ToF.start_ranging()
        time.sleep(.005) # use .005 for drive mode
        distance = ToF.get_distance()    # Get the result of the measurement
        time.sleep(.005) # use .005 for drive mode
        ToF.stop_ranging()
        print("Distance sensor reads: %f" % (distance))

printDist()
