from inputs.button import Button
from timekeeping.alarm import Alarm
from outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time
from global_config import DAY_NIGHT_ALARM
from global_config import LCD

# define buttons and map them to GPIO pins
hourButton = Button(29)
minButton = Button(31)

def callback_hour(channel):
    DAY_NIGHT_ALARM.increment_both_hour()
    LCD.write_msg_to_screen("Alarm: %s" 
        % DAY_NIGHT_ALARM.get_morning_alarm())
    
def callback_min(channel):
    DAY_NIGHT_ALARM.increment_both_min()
    LCD.write_msg_to_screen("Alarm: %s"
        % DAY_NIGHT_ALARM.get_morning_alarm())


class SetAlarmMode:
    
    def __init__(self):
        x = 0



    def set_events(self):
        # add events that listen for rising or falling edges on hourButton and minButton
        # set up with a debounce time in MILLISECONDS
        GPIO.add_event_detect(hourButton.get_pin()
            , GPIO.BOTH
            , callback = callback_hour
            , bouncetime=750)
        GPIO.add_event_detect(minButton.get_pin()
            , GPIO.BOTH
            , callback = callback_min
            , bouncetime=750)

        # add callbacks to buttons so something happens when the event happens
        #GPIO.add_event_callback(hourButton.get_pin(), self.callback_hour)
        #GPIO.add_event_callback(minButton.get_pin(), self.callback_hour)
