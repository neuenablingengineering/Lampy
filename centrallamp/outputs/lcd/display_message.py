import lcdlib
import serial

class display:
    BAUD_RATE = 9600

    def __init__(self):
        self.ser = serial.Serial('/dev/serial0', BAUD_RATE)

        
