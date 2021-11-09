# Min distance sensor example
import qwiic
import time

def runExample():
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

runExample()
