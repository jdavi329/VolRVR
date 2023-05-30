# Oct 29
# Python Example for Drive, set LED, and set LCD
# Fall EF230
# Dr Amy Biegalskiimport os
def setDriveSpeed( speed ):
    print ("Moving forward at ", speed)
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
    sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
    import os
    # allow pull files from two layers above and append path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    # time related functions
    import time
    # import sphero sdk functions
    # allow for Observer mode or Await/Async
    import asyncio # allow concurrent commands
    from sphero_sdk import SpheroRvrObserver

    # initialize global variables
    speed = 0
    heading = 0
    flags = 0 # flag 1 is backward flag 0 is forward
    green1 = [0, 255, 0]
    green2 = [0, 128, 0]

    rvr = SpheroRvrObserver()

    # drive forward, 50% speed
    rvr.drive_tank_si_units(
        left_velocity=0.75,  # Valid velocity values are [-1.555..1.555]
        right_velocity=0.75
    )
    # Delay to allow RVR to drive
    time.sleep(1)
    # stop
    rvr.drive_tank_si_units(
        left_velocity=0.75,  # Valid velocity values are [-1.555..1.555]
        right_velocity=0.75
    )
    return
