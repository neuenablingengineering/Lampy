from button import Button
import RPi.GPIO as GPIO
import time

testNum = 12

def callback1(self, testNum):
	testNum += 1
	if testNum > 23:
		testNum = 0
	print testNum

testButton = Button(29)
# add an event that listens for rising or falling edges on testButton
# set up with a debounce time in MILLISECONDS
GPIO.add_event_detect(testButton.getPin(),GPIO.BOTH,bouncetime=1000)
GPIO.add_event_callback(testButton.getPin(), callback1)



while(True):
	print testButton.getState()
	time.sleep(5)
