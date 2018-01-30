import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)

while(True):
    print(GPIO.input(29))
    time.sleep(5)

