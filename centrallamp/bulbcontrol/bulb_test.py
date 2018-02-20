from bulb import Bulb
import time

testBulb = Bulb(12,70)

testBulb.transition_on()
time.sleep(10)
testBulb.transition_off()