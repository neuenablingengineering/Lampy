from lcdlib import LCDCommonCommands

import serial
from time import strftime
from datetime import datetime

class LCDDisplay:
    BAUD_RATE = 9600
    com = LCDCommonCommands()

    def __init__(self):
        self.ser = serial.Serial('/dev/serial0', self.BAUD_RATE)
        self.com.CLEAR(self.ser)

    def write_msg_to_screen(self, msg):
        if (self.ser.isOpen()):
            self.com.CLEAR(self.ser)
            self.ser.write(msg)

    def write_time_to_screen(self):
        if (self.ser.isOpen()):
            self.com.CLEAR(self.ser)
            #initial offset of 5 to center the time
            self.com.CURSOR_SET(self.ser, 5)
            self.ser.write(datetime.now().strftime('%H:%M'))
