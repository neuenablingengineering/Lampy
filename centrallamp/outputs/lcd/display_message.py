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

    def write_msg_to_screen(self, msg, offset=0):
        if (self.ser.isOpen()):
            self.com.CLEAR(self.ser)
            self.com.CURSOR_SET(self.ser, offset)
            self.ser.write(msg)

    def write_time_to_screen(self):
        if (self.ser.isOpen()):
            self.com.CLEAR(self.ser)
            #initial offset of 5 to center the time
            self.com.CURSOR_SET(self.ser, 5)
            self.ser.write(datetime.now().strftime('%H:%M'))

    #this is prob not the best way to clear the second row
    #we should look into a different method
    def write_msg_to_bottom_screen(self, msg, offset=16):
        if (self.ser.isOpen()):
            self.com.CURSOR_SET(self.ser, offset)
            self.ser.write("                ")
            self.com.CURSOR_SET(self.ser, offset)
            self.ser.write(msg)
