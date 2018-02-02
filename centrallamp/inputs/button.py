import RPi.GPIO as GPIO

class Button:

	def __init__(self, pinNum):
		# set GPIO mode and set selected pin for input
		self.pinNum=pinNum
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pinNum, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		# add event to detect rising and falling edges
		GPIO.add_event_detect(self.pinNum,GPIO.BOTH)
		GPIO.add_event_callback(self.pinNum, self.my_callback)

	def getState(self):
		# return whether pin is "ON" or "OFF"
		return GPIO.input(self.pinNum)
	
	#def detectEdge(self):
	#	print "Button changed"
	#	return True

	def my_callback():
		print "Button pressed"
