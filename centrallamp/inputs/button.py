import RPi.GPIO as GPIO

class Button:

	def __init__(self, pinNum):
		# set GPIO mode and set selected pin for input
		self.GPIO.setmode(GPIO.BOARD)
		self.GPIO.setup(pinNum, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.pinNum=pinNum

	def getState(self):
		# return whether pin is "ON" or "OFF"
		return self.GPIO.input(pinNum)
	
	#def detectEdge(self):
