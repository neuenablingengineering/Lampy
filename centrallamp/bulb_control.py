# For manually turning the lamp bulbs ON/OFF
# Contains:
# - Callback for lamp switch
# - Thread Class BulbControlThread

from global_config import *
import RPi.GPIO as GPIO
from inputs.button import Button
import threading
import time

def callback_bulb(channel):
    if LAMP_BULBS.check_bulb_status():
        # if lamp is on, turn it off
        LAMP_BULBS.turn_off()
    else:
        # if lamp is off, turn it on
        LAMP_BULBS.turn_on()

class BulbControlThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        bulbSwitch = Button(15)
        GPIO.add_event_detect(bulbSwitch.get_pin()
            , GPIO.BOTH
            , callback=callback_bulb
            , bouncetime = 750)
