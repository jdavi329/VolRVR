# EF 230 Python Project
# Team members: Baylor White, Colton Brainard, Maria Lopez, Elle Street, Megan Hurley
# Date Created: November 28, 2023

# Problem Description: The rover ....

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
    if distance<500: # object close
        print(distance)
        print("obstacle")
        turnRight()

def setLEDsfunc():
    rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)
    
def setOLEDfunc():  
    # Display message on lcd
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)  #  Clear display
    myOLED.set_font_type(0)
    myOLED.set_cursor(0,0)
    myOLED.print("Go VOLS")
    myOLED.display()
    time.sleep(1)

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

# turn Right Function
# turns the rover 90 degrees and continues to move forward
def turnRight():
    time.sleep(1)
    print("turning right")
    # sets new orientation index to 0 and stops the rover's movement
    rvr.reset_yaw()
    rvr.drive_with_heading(speed=30,heading=90,flags=0)

# Main function
def mainfunc():
    global speed
    global heading
    global flags
    rvr.wake()
    time.sleep(1)
        # Initialize sensors
    ToF=qwiic.QwiicVL53L1X()
    ToF.sensor_init()
    ToF.start_ranging()
    rvr.reset_yaw()
    # sets current time as 0 and creates variable for current relative time
    distance = 501
    while distance > 200:
        distance = ToF.get_distance()
        print(distance)
        rvr.drive_with_heading(speed=20,heading=0,flags=0)
        time.sleep(.1)
    time.sleep(1)
    setLEDsfunc()
    print("TOO CLOSE!")
        

# Calls main function
mainfunc()