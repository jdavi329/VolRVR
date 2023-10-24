# A.Biegalski Oct 2020
# For raspberry pi controlled Sphero RVR
# Displays live distance sensor measurements on onboard OLED screen
# For hardware specifications refer to github readme at https://github.com/abiegals/VolRVR/
#
# Adapted from:
# SparkFun Electronics sparkfun_autonomous_kit https://github.com/sparkfun/sparkfun_autonomous_kit
# Sphero, Inc. sphero-sdk-raspberrypi-python https://github.com/sphero-inc/sphero-sdk-raspberrypi-python


import qwiic_micro_oled
import sys
import qwiic
import qwiic_vl53l1x
import time

def runExample():
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
            time.sleep(.5) # delete if using sensors for navigation
        except Exception as e:
            print("Ctrl-C terminated process") # will terminate if you use ctrl-c

runExample()
