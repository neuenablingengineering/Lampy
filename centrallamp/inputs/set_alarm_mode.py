from inputs.button import Button
from timekeeping.alarm import Alarm
from outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time

# define buttons and map them to GPIO pins
hourButton = Button(29)
minButton = Button(31)

class SetAlarmMode:
    
    def __init__(self, dualAlarm):
        self.dualAlarm = dualAlarm

    def callback_hour(self, channel):
        self.dualAlarm.increment_both_hour()
    
    def callback_min(self,channel):
        self.dualAlarm.increment_both_min()



    def set_events(self):
        # add events that listen for rising or falling edges on hourButton and minButton
        # set up with a debounce time in MILLISECONDS
        GPIO.add_event_detect(hourButton.get_pin(),GPIO.BOTH,bouncetime=750)
        GPIO.add_event_detect(minButton.get_pin(),GPIO.BOTH,bouncetime=750)

        # add callbacks to buttons so something happens when the event happens
        GPIO.add_event_callback(hourButton.get_pin(), self.callback_hour)
        GPIO.add_event_callback(minButton.get_pin(), self.callback_hour)
