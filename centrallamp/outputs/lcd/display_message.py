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

    def write_two_line_msg(self, line1, line2):
        if (self.ser.isOpen()):
            self.com.CLEAR(self.ser)
            self.ser.write(line1)
            self.com.CURSOR_SET(self.ser, 16)
            self.ser.write(line2)

    def write_to_second_line(self, msg, offset=0):
        if (self.ser.isOpen()):
            self.com.clear_second_line(self.ser)
            self.com.CURSOR_SET(self.ser, 16 + offset)
            self.ser.write(msg)
    
    def clear_first_line(self):
        if (self.ser.isOpen()):
            self.com.CURSOR_SET(self.ser, 15)
            for x in range(0, 15):
                self.com.BACKSPACE(self.ser)

    def clear_second_line(self):
        if (self.ser.isOpen()):
            self.com.CURSOR_SET(self.ser, 31)
            for x in range(0, 15):
                self.com.BACKSPACE(self.ser)

    def write_time_to_screen(self):
        if (self.ser.isOpen()):
            self.com.CLEAR(self.ser)
            #initial offset of 5 to center the time
            self.com.CURSOR_SET(self.ser, 5)
            self.ser.write(datetime.now().strftime('%H:%M'))
