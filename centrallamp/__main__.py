import threading
import time
from outputs.lcd.display_message import LCDDisplay


def main():
    lcd_lock = thread.allocate_lock();
    lcd = LCDDisplay()
    displayTime = threading.Thread(group=None
        , target=keepTime(lcd, lcd_lock)
        , name=Time)
    getInput = threading.Thread(group=None
        , target=getIn(lcd, lcd_lock)
        , name=Input)

def keepTime(lcd, lcd_lock):
    while (True):
        if (!lcd_lock.locked()):
            lcd.write_time_to_screen() 
            time.sleep(60)

def getIn(lcd, lcd_lock):
    inp = input("Input: ")
    lcd_lock.aquire()
    lcd.write_msg_to_screen(inp)
    time.sleep(30)
    lcd_lock.release()

if __name__ == "__main__":
    main()
