# contains class and controls for a lightbulb

import RPi.GPIO as GPIO
import time

class Bulb:

    FREQUENCY = 1000

    def __init__(self
        , pinNum
        , maxDutyCycle=80
        , transitionSleepOn=0.2
        , transitionSleepOff=0.2):
        self.pinNum = pinNum
        self.maxDutyCycle = maxDutyCycle
        self.transitionSleepOn = transitionSleepOn
        self.transitionSleepOff = transitionSleepOff
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinNum,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pinNum,Bulb.FREQUENCY)
        self.pwm.stop()
        self.dutyCycle = 80
        self.isOn = False

    def transition_on(self):
        # gradually transition bulb from OFF to ON
        for x in range(self.maxDutyCycle):
            self.pwm.ChangeDutyCycle(x)
            self.dutyCycle = x
            time.sleep(self.transitionSleepOn)

    def transition_off(self):
        # gradualy transition bulb from ON to OFF
        for x in range(self.maxDutyCycle):
            self.pwm.ChangeDutyCycle(self.maxDutyCycle - x)
            self.dutyCycle = (self.maxDutyCycle - x)
            time.sleep(self.transitionSleepOff)

    def demo_transition_on(self):
        # a shorter transition on for short capstone demo
        for x in range(self.maxDutyCycle(x):
            self.pwm.ChangeDutyCycle(x)
            self.dutyCycle = x
            time.sleep(.1)

    def demo_transition_off(self):
        # a shorter transition off for short capstone demo
        for x in range(self.maxDutyCycle(x):
            self.pwm.ChangeDutyCycle(self.maxDutyCycle - x)
            self.dutyCycle = (self.maxDutyCycle - x)
            time.sleep(.1)

    # stop PWM
    def turn_off(self):
        self.pwm.stop()
        self.isOn = False

    # start PWM at current self.dutyCycle level
    def turn_on(self):
        self.pwm.start(self.dutyCycle)
        self.isOn = True

    # start PWM at a particular duty cycle
    def set_on(self, newCycle):
        self.pwm.start(newCycle)
        self.dutyCycle = newCycle
        self.isOn = True

    # change the currently set duty cycle
    def change_duty_cycle(self, dutyCycle):
        self.pwm.ChangeDutyCycle(dutyCycle)
        self.dutyCycle = dutyCycle

    # check current ON/OFF status
    def check_status(self):
        return self.isOn
