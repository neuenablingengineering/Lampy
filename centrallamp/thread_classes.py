import threading
import time
import sys
import datetime as dt
import RPi.GPIO as GPIO
from inputs.button import Button
from global_config import *
from inputs.set_alarm_mode import SetAlarmMode

global TOGGLE_FLAG
hourButton = Button(29)
minButton = Button(31)

def callback_toggle(channel):
    global TOGGLE_FLAG
    TOGGLE_FLAG = not TOGGLE_FLAG
    print TOGGLE_FLAG 
    if (TOGGLE_FLAG == True):
        LCD_CONTROL_BOOL = True
        LCD.write_msg_to_screen("Set Alarm Mode")
        time.sleep(2)
        LCD.write_msg_to_screen("Alarm: %s" 
        % DAY_NIGHT_ALARM.get_morning_alarm())
        if 'hourEvent' not in locals():
            hourEvent = GPIO.add_event_detect(hourButton.get_pin()
                , GPIO.BOTH
                , callback = callback_hour
                , bouncetime=750)
        if 'minEvent' not in locals():
            minEvent = GPIO.add_event_detect(minButton.get_pin()
                , GPIO.BOTH
                , callback = callback_min
                , bouncetime=750)
        LCD_CONTROL_BOOL = False
    #TOGGLE_FLAG = not TOGGLE_FLAG 

def callback_hour(channel):
    if (TOGGLE_FLAG):
        print "CALLBACK HOUR"
        DAY_NIGHT_ALARM.increment_both_hour()
        LCD.write_msg_to_screen("Alarm: %s" 
            % DAY_NIGHT_ALARM.get_morning_alarm())
    
def callback_min(channel):
    if (TOGGLE_FLAG):
        print "CALLBACK MIN"
        DAY_NIGHT_ALARM.increment_both_min()
        LCD.write_msg_to_screen("Alarm: %s"
            % DAY_NIGHT_ALARM.get_morning_alarm())

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timenow = dt.datetime.now()
        currMin = timenow.minute
        LCD.write_time_to_screen()
        while (True):
            if ((currMin != dt.datetime.now().minute)
                &  (LCD_CONTROL_BOOL == False)):
                LCD.write_time_to_screen()
                currMin = dt.datetime.now().minute

class InputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        alarmToggle = Button(11) 
        global TOGGLE_FLAG
        TOGGLE_FLAG = False
        GPIO.add_event_detect(alarmToggle.get_pin()
            , GPIO.BOTH
            , callback = callback_toggle
            , bouncetime=750)

