from button import Button
import time

testButton = Button(29)
while(True):
	print testButton.getState()
	time.sleep(5)
