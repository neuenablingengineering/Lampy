from bulb import Bulb
import time

class DualBulb:
    
    def __init__(self, maxDutyCycle):
        self.maxDutyCycle = maxDutyCycle
        self.dayBulb = Bulb(12, maxDutyCycle, 0.1, 10)
        self.nightBulb = Bulb(13, maxDutyCycle, 10, 0.1)
        self.dayBulb.change_duty_cycle(maxDutyCycle)
        self.nightBulb.change_duty_cycle(0)

    def morning_sequence(self):
        self.set_bulbs_on(0,0)
        self.dayBulb.transition_on()

    def evening_sequence(self):
        for x in range(self.maxDutyCycle):
            self.dayBulb.change_duty_cycle(self.maxDutyCycle - x)
            self.nightBulb.change_duty_cycle(x)
            time.sleep(1)

    def turn_on(self):
        # set the bulbs to ON mode
        self.dayBulb.turn_on()
        self.nightBulb.turn_on()

    def turn_off(self):
        # set the bulbs to OFF mode
        self.dayBulb.turn_off()
        self.nightBulb.turn_off()

    def set_bulbs_on(self, morningDuty, nightDuty):
        # set the duty cycles for morning and night bulbs, then turn on
        self.dayBulb.set_on(morningDuty)
        self.nightBulb.set_on(nightDuty)

    def check_bulb_status(self):
        # returns true if any bulbs are on, false otherwise
        return (self.dayBulb.check_status() or self.nightBulb.check_status())
