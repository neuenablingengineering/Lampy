from inputs.button import *
from outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time

HOUR = 12
MINUTE = 00
ISDONE = False
PERIOD = "PM"

display = LCDDisplay()

hourButton = Button(29)
minButton = Button(31)
setButton = Button(11)

def callback_min(channel):
    MINUTE = (MINUTE + 1) % 60

def callback_hour(channel):
    HOUR = (HOUR + 1) % 24

def callback_set(channel):
    ISDONE = True

def get_time():
    if HOUR > 11:
        PERIOD = "PM"
    else
        PERIOD = "AM"
    if HOUR % 12 == 0:
        tempHour = 12
        return("%02d:%02d %s" % (tempHour, MINUTE, PERIOD))
    else
        return("%02d:%02d %s" % (HOUR % 12, MINUTE, PERIOD))

GPIO.add_event_detect(hourButton.get_pin(), GPIO.BOTH, callback=callback_hour, bouncetime=1000)
GPIO.add_event_detect(minButton.get_pin(), GPIO.BOTH, callback=callback_min, bouncetime=1000)
GPIO.add_event_detect(setButton.get_pin(), GPIO.BOTH, callback=callback_set, bouncetime=100)

display.write_msg_to_screen("Set Clock Time")
time.sleep(3)

while !ISDONE:
    # display current "new time" to LCD screen
    display.write_msg_to_screen(get_time())
    # wait a bit
    time.sleep(0.5)


print get_time()
