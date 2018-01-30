from inputs.button import Button
from timekeeping.alarm import Alarm
from outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time

testAlarm = Alarm(23,58)
display = LCDDisplay()

def callback1(self):
	global testAlarm
	global display
	testAlarm.inc_hour()

testButton = Button(29)
# add an event that listens for rising or falling edges on testButton
# set up with a debounce time in MILLISECONDS
GPIO.add_event_detect(testButton.get_pin(),GPIO.BOTH,bouncetime=500)
GPIO.add_event_callback(testButton.get_pin(), callback1)

display.write_msg_to_screen("Button Demo")
time.sleep(10)
while(True):
    display.write_msg_to_screen("Alarm: %s" % testAlarm.get_alarm())
    time.sleep(0.5)    
