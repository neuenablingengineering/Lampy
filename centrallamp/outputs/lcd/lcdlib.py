class LCDCommonCommands:
#common commands
    def CLEAR(self, ser):
        ser.write(chr(0xFE)) 
        ser.write(chr(0x51))

    def DISPLAY_ON(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x41))

    def DISPLAY_OFF(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x42))

    def CURSOR_HOME(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x46))

    def CURSOR_UNDERLINE_ON(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x47))

    def CURSOR_UNDERLINE_OFF(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x48))

    def CURSOR_LEFT(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x49))

    def CURSOR_RIGHT(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4A))

    def CURSOR_BLINK_ON(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4B))

    def CURSOR_BLINK_OFF(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4C))

    def BACKSPACE(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4E))

    def SCROLL_LEFT(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x55))

    def CURSOR_SET(self, ser, pos):
        ser.write(chr(0xFE))
        ser.write(chr(0x45))
        ser.writei(chr(float.hex(pos)))
    
    def CONTRAST_SET(self, ser, contrast):
        ser.write(chr(0xFE))
        ser.write(chr(0x52))
        ser.write(chr(float.hex(contrast)))

    def BRIGHTNESS_SET(self, ser, brightness):
        ser.write(chr(0xFE))
        ser.write(chr(0x53))
        ser.write(chr(float.hex(brightness)))

