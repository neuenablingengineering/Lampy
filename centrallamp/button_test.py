from inputs.button import Button
from timekeeping.alarm import Alarm
from outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time

testAlarm = Alarm(20,55)
display = LCDDisplay()
toggleFlag = False

def callback_hour(self):
    global testAlarm
    global alarmToggle
    if(alarmToggle.get_state()):
        testAlarm.inc_hour()
def callback_min(self):
    global testAlarm
    global alarmToggle
    if(alarmToggle.get_state()):
        testAlarm.inc_min()
#def callback_toggle(self):
#    global display
#    global toggleFlag
#    toggleFlag = True

# define buttons and map them to GPIO pins
alarmToggle = Button(11)
hourButton = Button(29)
minButton = Button(31)

# add events that listen for rising or falling edges on hourButton and minButton
# set up with a debounce time in MILLISECONDS
GPIO.add_event_detect(hourButton.get_pin(),GPIO.BOTH,bouncetime=750)
GPIO.add_event_detect(minButton.get_pin(),GPIO.BOTH,bouncetime=750)
#GPIO.add_event_detect(alarmToggle.get_pin(),GPIO.RISING,bouncetime=750)

# add callbacks to buttons so something happens when the event happens
GPIO.add_event_callback(hourButton.get_pin(), callback_hour)
GPIO.add_event_callback(minButton.get_pin(), callback_min)
GPIO.add_event_callback(alarmToggle.get_pin(), callback_toggle)

display.write_msg_to_screen("Button Demo")
time.sleep(3)
while(True):
    if(toggleFlag):
        display.write_msg_to_screen("Alarm Set Mode")
        toggleFlag = False
        time.sleep(5)
    display.write_msg_to_screen("Alarm: %s" % testAlarm.get_alarm())
    time.sleep(0.5)    
