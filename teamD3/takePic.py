import sys
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python/')
sys.path.append('/home/pi/sphero_toolbox/')
import picamera
import time

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')
