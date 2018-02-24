from bulb import Bulb
import time

class DualBulb:
    
    def __init__(self, maxDutyCycle):
        self.maxDutyCycle = maxDutyCycle
        self.dayBulb = Bulb(29, 80, 0.1, 10)
        self.nightBulb = Bulb(31, 80, 10, 0.1)

    def morning_sequence(self):
        self.dayBulb.transition_on()

    def evening_sequence(self):
        for x in range(self.maxDutyCycle):
            self.dayBulb.change_duty_cycle(self.maxDutyCycle - x)
            self.nightBulb.change_duty_cycle(x)
            time.sleep(10)
