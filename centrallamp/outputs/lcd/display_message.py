from lcdlib import LCDCommonCommands

import serial
from time import strftime
from datetime import datetime

class LCDDisplay:
    BAUD_RATE = 9600
    com = LCDCommonCommands()

    def __init__(self):
        self.ser = serial.Serial('/dev/serial0', self.BAUD_RATE)

    def write_msg_to_screen(self, msg):
        self.com.CLEAR(self.ser)
        self.ser.write(msg)

    def write_time_to_screen(self):
        self.com.CLEAR(self.ser)
        self.ser.write(datetime.now().strftime('%H:%M'))
