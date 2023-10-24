# A.Biegalski Oct 2020  Color detection example
#
# For raspberry pi controlled Sphero RVR
# detects riding surface color and prints output to control computer
# For hardware specifications refer to github readme at https://github.com/abiegals/VolRVR/
# 
#
# Adapted from:
# SparkFun Electronics sparkfun_autonomous_kit https://github.com/sparkfun/sparkfun_autonomous_kit
# Sphero, Inc. sphero-sdk-raspberrypi-python https://github.com/sphero-inc/sphero-sdk-raspberrypi-python

# Do necessary imports
import os
import sys
import time
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices

# Put in Observer mode
rvr = SpheroRvrObserver()

R_int, B_int, G_int = 0,0,0

# Function handle for what to do with color data (useful for printing)
def color_detected_handler(color_detected_data):
    global R_int, B_int, G_int
    print('Color detection data response: ', color_detected_data)
    R_int = color_detected_data["ColorDetection"]["R"]
    B_int = color_detected_data["ColorDetection"]["B"]
    G_int = color_detected_data["ColorDetection"]["G"]

# Main def
def main():

    global B_int, R_int, G_int

    rvr.wake()

    # Give RVR time to wake up
    time.sleep(1)

    # Get color
    rvr.enable_color_detection(is_enabled=True)
    rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.color_detection,
        handler=color_detected_handler
    )

    # Sample every 250 ms
    rvr.sensor_control.start(interval=250)

    # Index color data out of dict
    print("Red value if: ", R_int)

    # Allow this program to run for 10 seconds
    time.sleep(1)
    rvr.sensor_control.clear()

    # Delay to allow RVR issue command before closing
    time.sleep(.5)
    rvr.close()


main()
