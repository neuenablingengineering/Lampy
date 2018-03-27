from centrallamp.inputs.button import *
from centrallamp.outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time

# Default 12:00 PM for user to increment time from
HOUR = 12
MINUTE = 00
ISDONE = False
PERIOD = "PM"

# Initialize LCD
display = LCDDisplay()

# Initialize buttons
hourButton = Button(29)
minButton = Button(31)
setButton = Button(11)

# Define callbacks to increment & set time with buttons
def callback_min(channel):
    global MINUTE
    MINUTE = (MINUTE + 1) % 60

def callback_hour(channel):
    global HOUR
    HOUR = (HOUR + 1) % 24

def callback_set(channel):
    global ISDONE
    ISDONE = True

# Return a string with the current time to be set
def get_time():
    
    # Set PM for hours 12-23 and AM for hours 0-11
    if HOUR > 11:
        PERIOD = "PM"
    else:
        PERIOD = "AM"

    # If the hour is 0 or 12, use "12" as the hour instead of 0
    if HOUR % 12 == 0:
        return("12:%02d %s" % (MINUTE, PERIOD))
    else:
        return("%02d:%02d %s" % (HOUR % 12, MINUTE, PERIOD))

# Set up button event detects
GPIO.add_event_detect(hourButton.get_pin(), GPIO.BOTH, callback=callback_hour, bouncetime=750)
GPIO.add_event_detect(minButton.get_pin(), GPIO.BOTH, callback=callback_min, bouncetime=750)
GPIO.add_event_detect(setButton.get_pin(), GPIO.BOTH, callback=callback_set, bouncetime=1000)

# Alert user to set the time
display.write_msg_to_screen("Set Clock Time")
time.sleep(3)

# Until the 'set' button is pressed
while not ISDONE:
    # Display current "new time" to LCD screen & wait so we're not constantly refreshing
    display.write_msg_to_screen(get_time())
    time.sleep(0.5)

# Clear the screen
display.write_msg_to_screen(" ")

# Return new time string to bash script
print get_time()

# Cleanup the GPIO
GPIO.cleanup()
