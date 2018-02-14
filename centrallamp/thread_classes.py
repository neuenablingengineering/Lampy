import threading
import time
import sys
import datetime as dt
from inputs.button import Button
from global_config import *

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timenow = dt.datetime.now()
        currMin = timenow.minute
        lcd.write_time_to_screen()
        while (True):
            if ((currMin != dt.datetime.now().minute)
                &  (lcdControlBool == False)):
                lcd.write_time_to_screen()
                currMin = dt.datetime.now().minute

class InputThread(threading.Thread):
    alarmToggle = Button(11) 

    def __init__(self):
        threading.Thread.__init__(self)

    def callback_toggle(self):
        toggleFlag = True

    def run(self):
        GPIO.add_event_detect(alarmToggle.get_pin()
            , GPIO.RISING,bouncetime=750)
        GPIO.add_event_callback(alarmToggle.get_pin()
            , callback_toggle)
        while(True):
            if(alarmToggle.get_state()):
                LCD_CONTROL_BOOL = True
                LCD.write_msg_to_screen("Alarm Set Mode")
                setAlarmMode = SetAlarmMode(DAY_NIGHT_ALARM)
            time.sleep(5)
            LCD.write_msg_to_screen("Alarm: %s" %
                DAY_NIGHT_ALARM.get_morning_alarm())
            LCD.write_time_to_screen()
            LCD_CONTROL_BOOL = False


