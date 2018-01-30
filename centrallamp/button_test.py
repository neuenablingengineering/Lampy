from inputs.button import Button
from timekeeping.alarm import Alarm
import RPi.GPIO as GPIO
import time

testAlarm = Alarm(23,58)

def callback1(self):
    global testAlarm
    testAlarm.incHour()
    print testAlarm.getAlarm()

testButton = Button(29)
# add an event that listens for rising or falling edges on testButton
# set up with a debounce time in MILLISECONDS
GPIO.add_event_detect(testButton.getPin(),GPIO.BOTH,bouncetime=1000)
GPIO.add_event_callback(testButton.getPin(), callback1)



while(True):
	print testButton.getState()
	time.sleep(5)
