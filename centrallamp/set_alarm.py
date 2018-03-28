# For setting the alarm
# Contains: 
# - Callbacks for the toggle, hour, and minute button
# - Thread Class SetAlarmThread
from global_config import *
import RPi.GPIO as GPIO
from inputs.button import Button
import threading
import time
import datetime

global TOGGLE_FLAG
global DAY_NIGHT_ALARM
TOGGLE_FLAG = False

#Toggles Set Alarm Mode
def callback_toggle(channel):
    global TOGGLE_FLAG
    global LCD_CONTROL_BOOL
    global DAY_NIGHT_ALARM
    TOGGLE_FLAG = not TOGGLE_FLAG 
    print "CALLBACK: " + str(TOGGLE_FLAG)
    if (TOGGLE_FLAG == True):
        DAY_NIGHT_ALARM.enter_set_mode()
    if (TOGGLE_FLAG == False):
        DAY_NIGHT_ALARM.exit_set_mode()
        LCD.write_time_to_screen()
            
def callback_hour(channel):
    global DAY_NIGHT_ALARM
    if (TOGGLE_FLAG):
        print "hour increment"
        DAY_NIGHT_ALARM.increment_both_hour()

def callback_min(channel):
    global DAY_NIGHT_ALARM
    if (TOGGLE_FLAG):
        print "min increment"
        DAY_NIGHT_ALARM.increment_both_min()
    else:
        # FOR DEMO PURPOSES ONLY
        # When not in Set Alarm Mode, pressing MINUTE button will set alarm to current time
        now = datetime.datetime.now()
        DAY_NIGHT_ALARM.set_morning_dusk_sim_alarms(now.hour, now.minute)

class SetAlarmThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    #Sets up callbacks, displays alarm information to LCD 
    def run(self):
        global TOGGLE_FLAG

        alarmToggle = Button(11) 
        hourButton = Button(29)
        minButton = Button(31)

        #callback for the toggle button
        GPIO.add_event_detect(alarmToggle.get_pin()
            , GPIO.BOTH
            , callback = callback_toggle
            , bouncetime=1000)
        #callback for the hour button
        GPIO.add_event_detect(hourButton.get_pin()
            , GPIO.BOTH
            , callback = callback_hour
            , bouncetime=750)
        #callback for the minute button
        GPIO.add_event_detect(minButton.get_pin()
            , GPIO.BOTH
            , callback = callback_min
            , bouncetime=750)
            
        while (True):
            global DAY_NIGHT_ALARM
            if (TOGGLE_FLAG):
                LCD.write_msg_to_screen("Set Alarm Mode")
                time.sleep(2)
                while (TOGGLE_FLAG):
                    LCD.write_msg_to_screen("Alarm: %s" %
                        DAY_NIGHT_ALARM.get_morning_alarm())
                    time.sleep(0.5)
     

