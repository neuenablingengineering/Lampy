#common commands
def CLEAR(ser):
    ser.write(chr(0xFE)) 
    ser.write(chr(0x51))

def DISPLAY_ON(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x41))

def DISPLAY_OFF(ser):
    ser.write(chr(0XFE))
    ser.write(chr(0x42))

def CURSOR_HOME(ser):
    ser.write(chr(0XFE))
    ser.write(chr(0x46))

def CURSOR_UNDERLINE_ON(ser):
    ser.write(chr(0XFE))
    ser.write(chr(0x47))

def CURSOR_UNDERLINE_OFF(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x48))

def CURSOR_LEFT(ser):
   ser.write(chr(0XFE))
    ser.write(chr(0x49))

def CURSOR_RIGHT(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x4A))

def CURSOR_BLINK_ON(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x4B))

def CURSOR_BLINK_OFF(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x4C))

def BACKSPACE(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x4E))

def SCROLL_LEFT(ser):
    ser.write(chr(0xFE))
    ser.write(chr(0x55))

