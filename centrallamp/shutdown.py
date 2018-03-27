from global_config import *
import RPi.GPIO as GPIO
import threading
from inputs.button import Button
import time
import os

def shutdown(channel):
    print("Shutdown should be called")
    LCD.write_msg_to_screen("  ")
    GPIO.cleanup()
    os.system("shutdown now -h")

class ShutdownThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        shutdownButton = Button(19) 
        GPIO.add_event_detect(shutdownButton.get_pin()
           , GPIO.BOTH
           , callback = shutdown
           , bouncetime = 750)
