# A.Biegalski
# May 30 2023 
# Problem:  Test Servos on Pi Servo Hat
# Solution: use move_servo_position command.  
# After any pan or tilt motion, rotate in opposite direction to reset servo position for the next user.
#
# Adapted from
# SparkFun Electronics, November 2019, Author: Wes Furuya
# https://github.com/sparkfun/PiServoHat_Py/blob/main/examples/ex3_get_position_180_deg_servo.py
#
# For raspberry pi controlled Sphero RVR
# For hardware specifications refer to github readme at https://github.com/abiegals/VolRVR/
#
import pi_servo_hat
import time

# Initialize Constructor
test = pi_servo_hat.PiServoHat()

# Restart Servo Hat (in case Hat is frozen/locked)
test.restart()

# Test Run
#########################################
# look left and right  Channel 1
# sweep left 20 degrees, right 40, left 20
for i in range(0,20):
    test.move_servo_position(1, i, 90)
    print("Position: ", end = '')
    print(test.get_servo_position(0,90))
for i in range(20, -20, -1):
    test.move_servo_position(1, i, 90)
for i in range(0,20):
    test.move_servo_position(1, i, 90)

# look up and down  Channel 0
for i in range(30, 0, -1):
    test.move_servo_position(0, i, 90)
for i in range(0, 30):
    test.move_servo_position(0, i, 90)


# Tilt up 15 degrees, channel 0
# test.move_servo_position(0, 15)

# Pause 1 sec
time.sleep (1)

# Pan servo position 15 degrees right, Channel 1
# test.move_servo_position(1, -15)

# Pause 1 sec
time.sleep (1)
