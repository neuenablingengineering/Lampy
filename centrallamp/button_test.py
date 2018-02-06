from inputs.button import Button
from timekeeping.alarm import Alarm
from outputs.lcd.display_message import LCDDisplay
import RPi.GPIO as GPIO
import time

testAlarm = Alarm(23,58)
display = LCDDisplay()

def callbackHour(self):
	global testAlarm
	global display
	testAlarm.inc_hour()
def calbackMin(self):
	global testAlarm
	global display
	testAlarm.inc_min()

hourButton = Button(29)
minButton = Button(31)
# add events that listen for rising or falling edges on hourButton and minButton
# set up with a debounce time in MILLISECONDS
GPIO.add_event_detect(hourButton.get_pin(),GPIO.BOTH,bouncetime=500)
GPIO.add_event_detect(minButton.get_pin(),GPIO.BOTH,bouncetime=500)

GPIO.add_event_callback(hourButton.get_pin(), callbackHour)
GPIO.add_event_callback(minButton.get_pin(), callbackMin)

display.write_msg_to_screen("Button Demo")
time.sleep(10)
while(True):
    display.write_msg_to_screen("Alarm: %s" % testAlarm.get_alarm())
    time.sleep(0.5)    
