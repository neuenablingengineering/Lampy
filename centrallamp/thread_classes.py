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
    toggleFlag = False
    alarmToggle = Button(11) 
    def __init__(self):
        threading.Thread.__init__(self)
    def callback_toggle(self):
        toggleFlag = True
    def run(self):
        time.sleep(3)
        while(True):
            if(toggleFlag):
                lcdControlBool = True
                lcd.write_msg_to_screen("Alarm Set Mode")
                GPIO.add_event_detect(alarmToggle.get_pin()
                    ,GPIO.RISING,bouncetime=750)
                GPIO.add_event_callback(alarmToggle.get_pin()
                    ,callback_toggle)
                #call set alarm logic
                toggleFlag = False
                time.sleep(5)
        lcd.write_msg_to_screen("Alarm: %s" % dualAlarm.get_alarm())
        lcd.write_time_to_screen()
        lcdControlBool = False
        sys.exit()


