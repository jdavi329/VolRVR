import pi_servo_hat
import time



# Initialize Constructor
test = pi_servo_hat.PiServoHat()

# Restart Servo Hat (in case Hat is frozen/locked)
test.restart()

# Test Run
#########################################
# look left and right  Channel 1
# sweep left 30 degrees, right 60, left 30
for i in range(0,30):
    test.move_servo_position(1, i, 90)
    print('Position: ", end = '')
    print(test.get_servo_position(0,90))
for i in range(30, -30, -1):
    test.move_servo_position(1, i, 90)
for i in range(0,30):
    test.move_servo_position(1, i, 90)

# look up and down  Channel 0
for i in range(30, 0, -1):
    test.move_servo_position(0, i, 90)
for i in range(0, 30):
    test.move_servo_position(0, i, 90)


# write 30 degrees
# test.move_servo_position(2, 30)

# Pause 1 sec
time.sleep (1)

# Moves servo position to 85 degrees, Channel 1
# test.move_servo_position(1, -85)

# Pause 1 sec
time.sleep (1)
