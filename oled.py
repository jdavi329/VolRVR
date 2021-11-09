# Min example of OLED Display
import qwiic_micro_oled
import sys
import qwiic
import qwiic_vl53l1x
import time

# Function def line
def runExample():

    # Initialize display
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    myOLED.begin()

    # Clear anything that might be displayed
    myOLED.clear(myOLED.PAGE)
    myOLED.clear(myOLED.ALL)

    # Set default font and screen position
    myOLED.set_font_type(0)
    myOLED.set_cursor(0,0)

    # Print text to buffer
    myOLED.print("TEXT HERE")

    # Change screen position for multiple lines of text
    myOLED.set_cursor(0,15)
    myOLED.print("MOAR TEXT")

    # Actually push data to OLED display
    myOLED.display()

    # Set a while true loop for continuous display update
    i = 0
    while True:

        # Incremental variable
        i = i + 1

        # Reset cursor to 30 or it will print to next line of the OLED
        myOLED.set_cursor(0,30)

        # More complex printing (like sprintf in matlab)
        # (use %f for floating point, %i for intergers, %s for text)
        myOLED.print("Count to: %3i" % (i))
        myOLED.display()

        # Use this so that robot comunication isn't too fast
        time.sleep(0.005)

runExample()
