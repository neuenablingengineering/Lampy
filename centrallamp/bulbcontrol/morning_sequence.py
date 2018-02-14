import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(18,IO.OUT)
IO.setup(27,IO.OUT)

p=IO.PWM(18,1000)
q=IO.PWM(27,1000)

p.start(0)
q.start(0)

for x in range(70):
    p.ChangeDutyCycle(x)
    time.sleep(0.2)

time.sleep(5)

for x in range(70):
    p.ChangeDutyCycle(70-x)
    time.sleep(0.1)
