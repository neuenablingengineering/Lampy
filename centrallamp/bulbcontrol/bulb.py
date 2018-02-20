# contains class and controls for a lightbulb

import RPi.GPIO as GPIO
import time

class Bulb:

	FREQENCY = 1000
	SLEEP_DURING_TRANSITION_ON = 0.2
	SLEEP_DURING_TRANSITION_OFF = 0.1

	def __init__(self,pinNum,maxDutyCycle):
		self.pinNum = pinNum
		self.maxDutyCycle = maxDutyCycle
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pinNum,GPIO.OUT)
		self.pwm = GPIO.PWM(self.pinNum,FREQENCY)
		self.pwm.start(0)

	def transition_on(self):
		for x in range(maxDutyCycle):
    		self.pwm.ChangeDutyCycle(x)
    		time.sleep(SLEEP_DURING_TRANSITION_ON)

    def transition_off(self):
    	for x in range(maxDutyCycle):
    		self.pwm.ChangeDutyCycle(maxDutyCycle-x)
    		time.sleep(SLEEP_DURING_TRANSITION_OFF)