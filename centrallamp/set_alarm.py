#Contains functions for setting the alarm. 
# - Callbacks for the hour and minute button
# - The function that sets up the callbacks and displays to the LCD

from global_config import *
import RPi.GPIO as GPIO
from inputs.button import Button

global TOGGLE_FLAG
global LCD_CONTROL_BOOL
TOGGLE_FLAG = False

def callback_toggle(channel):
    global TOGGLE_FLAG
    global LCD_CONTROL_BOOL
    TOGGLE_FLAG = not TOGGLE_FLAG 
    LCD_CONTROL_BOOL = TOGGLE_FLAG 
    print "CALLBACK: " + str(LCD_CONTROL_BOOL)
    if (LCD_CONTROL_BOOL == False):
        LCD.write_time_to_screen()
            
def callback_hour(channel):
    if (TOGGLE_FLAG):
        print "hour increment"
        DAY_NIGHT_ALARM.increment_both_hour()
    
def callback_min(channel):
    if (TOGGLE_FLAG):
        print "min increment"
        DAY_NIGHT_ALARM.increment_both_min()

def set_alarm_main():
    global TOGGLE_FLAG
    global LCD_CONTROL_BOOL

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
        if (LCD_CONTROL_BOOL):
            LCD.write_msg_to_screen("Set Alarm Mode")
            time.sleep(2)
            while (LCD_CONTROL_BOOL):
                LCD.write_msg_to_screen("Alarm: %s" %
                    DAY_NIGHT_ALARM.get_morning_alarm())
                time.sleep(0.5)
 

