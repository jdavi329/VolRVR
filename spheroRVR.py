# 30 May 2023
# Python toolbox for Drive with tank, set LED, and set LCD
# EF230
# A Biegalski
def setDriveSpeed( speedleft, speedright ):   # Valid velocity values are [-1.555..1.555]
    print ("Driving at wheelspeed ", speedleft, " and ", speedright)
    import sys
    import os
    # allow pull files from two layers above and append path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
    sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    # time related functions
    import time
    # import sphero sdk functions Observer mode 
    from sphero_sdk import SpheroRvrObserver
    rvr = SpheroRvrObserver()
    rvr.wake()
    time.sleep(0.2)
    rvr.drive_tank_si_units(
        left_velocity=speedleft,  
        right_velocity=speedright
    )
    rvr.close()
    return
