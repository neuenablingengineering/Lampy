import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(12,IO.OUT)
IO.setup(13,IO.OUT)

p=IO.PWM(12,1000)
q=IO.PWM(13,1000)

p.start(0)
q.start(0)

for x in range(70):
    p.ChangeDutyCycle(x)
    time.sleep(0.2)

time.sleep(5)

for x in range(70):
    p.ChangeDutyCycle(70-x)
    time.sleep(0.1)
