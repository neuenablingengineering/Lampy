import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(18,IO.OUT)
p = IO.PWM(18,1000)
p.start(0)
while 1:
    for x in range(50):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    for x in range(50):
        p.ChangeDutyCycle(50-x)
        time.sleep(0.1)
