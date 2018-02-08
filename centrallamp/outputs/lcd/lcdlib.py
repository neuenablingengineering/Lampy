class LCDCommonCommands:
#common commands
    #Clears the screen and resets cursor to position 0
    def CLEAR(self, ser):
        ser.write(chr(0xFE)) 
        ser.write(chr(0x51))
    
    #turns on the display
    def DISPLAY_ON(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x41))

    #turns off the display
    def DISPLAY_OFF(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x42))

    #moves the cursor to position 0
    def CURSOR_HOME(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x46))

    #turns on underline for the cursor
    def CURSOR_UNDERLINE_ON(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x47))

    #turns off underline for the cursor
    def CURSOR_UNDERLINE_OFF(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x48))

    #moves the cursor one position to the left
    def CURSOR_LEFT(self, ser):
        ser.write(chr(0XFE))
        ser.write(chr(0x49))

    #moves the cursor one position to the right
    def CURSOR_RIGHT(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4A))

    #turns on cursor blink
    def CURSOR_BLINK_ON(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4B))

    #turns off cursor blink
    def CURSOR_BLINK_OFF(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4C))

    #backspaces one position
    def BACKSPACE(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x4E))

    def SCROLL_LEFT(self, ser):
        ser.write(chr(0xFE))
        ser.write(chr(0x55))

    #sets the cursor to the specified position
    def CURSOR_SET(self, ser, pos):
        ser.write(chr(0xFE))
        ser.write(chr(0x45))
        ser.write(chr(pos))
    
    #Range of 1 - 50, default is 40
    def CONTRAST_SET(self, ser, contrast):
        ser.write(chr(0xFE))
        ser.write(chr(0x52))
        ser.write(chr(contrast))

    #Range of 1-8, default is 5
    def BRIGHTNESS_SET(self, ser, brightness):
        ser.write(chr(0xFE))
        ser.write(chr(0x53))
        ser.write(chr(brightness))

