# contains class and controls for a lightbulb

import RPi.GPIO as GPIO
import time

class Bulb:

    FREQUENCY = 1000

    def __init__(self, pinNum, maxDutyCycle=80, transitionSleep=0.2):
        self.pinNum = pinNum
        self.maxDutyCycle = maxDutyCycle
        self.transitionSleep = transitionSleep
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinNum,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pinNum,Bulb.FREQUENCY)
        self.pwm.start(0)

    def transition_on(self):
        for x in range(self.maxDutyCycle):
            self.pwm.ChangeDutyCycle(x)
            time.sleep(self.transitionSleep)

    def transition_off(self):
        for x in range(self.maxDutyCycle):
            self.pwm.ChangeDutyCycle(self.maxDutyCycle - x)
            time.sleep(self.transitionSleep)

    def turn_off(self):
        self.pwm.stop()
