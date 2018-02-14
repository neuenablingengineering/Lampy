import threading
import time
import sys
import datetime as dt
import RPi.GPIO as GPIO
from inputs.button import Button
from global_config import *
from inputs.set_alarm_mode import SetAlarmMode

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

    def callback_toggle(self):
        toggleFlag = True

    def run(self):
        alarmToggle = Button(11) 
        GPIO.add_event_detect(alarmToggle.get_pin()
            , GPIO.RISING,bouncetime=750)
        GPIO.add_event_callback(alarmToggle.get_pin()
            , self.callback_toggle)
        while(True):
            if(alarmToggle):
                LCD_CONTROL_BOOL = True
                LCD.write_msg_to_screen("Alarm Set Mode")
                setAlarmMode = SetAlarmMode(DAY_NIGHT_ALARM)
                setAlarmMode.set_events()
                alarmToggle = False
            time.sleep(5)
            LCD.write_msg_to_screen("Alarm: %s" %
                DAY_NIGHT_ALARM.get_morning_alarm())
            LCD.write_time_to_screen()
            LCD_CONTROL_BOOL = False


