# EF 230 Python Project
# Team members: Calvin Schaerer, Dyana Lacross, Jefferson Schmitt, Luka Strepacki, Paige Annen, Patrick Clingan
# Date Created: 28 November 2023

# Problem Description: The rover .........

import sys
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
import os
# allow pull files from two layers above and append path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# time related functions
import time
# import sphero sdk functions
# allow for Observer mode or Await/Async
import asyncio 
from sphero_sdk import RawMotorModesEnum
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices

# import qwiic functions
import qwiic_micro_oled
import qwiic


# Initialize sensors
ToF=qwiic.QwiicVL53L1X()
ToF.sensor_init()

# initialize global variables
speed = 0
heading = 0
flags = 0

rvr = SpheroRvrObserver()

# Sensor handling functions 
def color_detected_handler(color_detected_data):
    print('Color detection data response: ', color_detected_data)

def imu_handler(imu_data):
    print('IMU data response: ', imu_data)

def accelerometer_handler(accelerometer_data):
    print('Accelerometer data response: ', accelerometer_data)

# Obstacle avoidance function
def obstaclefunc():
    ToF.start_ranging()
    time.sleep(.005) # use .005 for drive mode
    distance = ToF.get_distance()    # Get the result of the measurement
    time.sleep(.005) # use .005 for drive mode
    ToF.stop_ranging()
    print("checking for obstacle")
    if distance<25: # object close
        print(distance)
        print("obstacle")
        rvr.reset_yaw()
        rvr.drive_with_heading(speed=30,heading=180,flags=0)
    else 


def sensorstreamfunc():
    rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.color_detection,
        handler=color_detected_handler
    )
    rvr.sensor_control.add_sensor_data_handler(
    service=RvrStreamingServices.imu,
    handler=imu_handler
    )
    rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.accelerometer,
        handler=accelerometer_handler
    )
    rvr.sensor_control.start(interval=250)

    # Delay to allow RVR to stream sensor data
    time.sleep(2)
    rvr.sensor_control.clear()


# Main function
def mainfunc():
    global speed
    global heading
    global flags
    rvr.wake()
    time.sleep(1)
    rvr.reset_yaw()
    # sets current time as 0 and creates variable for current relative time
    start_time = time.time()
    elapsed_time = time.time() - start_time
    rvr.drive_with_heading(speed=30,heading=0,flags=0)
    while elapsed_time <= 10:
        # sets rover drive speed/direction
        time.sleep(.5)
        # Calculate current elapsed time
        elapsed_time = time.time() - start_time
        # Call other functions here
        obstaclefunc()
    rvr.drive_with_heading(speed=0,heading=180,flags=0)
    sensorstreamfunc()
    rvr.close()
    print("All done")

# Calls main function
mainfunc()