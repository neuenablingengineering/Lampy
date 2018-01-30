import threading
import time
from outputs.lcd.display_message import LCDDisplay

def main():
    lcd_lock = threading.Lock();

    lcd = LCDDisplay()

    getInput = threading.Thread(group=None
        , target=getIn(lcd, lcd_lock))
    displayTime = threading.Thread(group=None
        , target=keepTime(lcd, lcd_lock))

def keepTime(lcd, lcd_lock):
    while (True):
 #       if (lcd_lock.locked() == False):
        lcd.write_time_to_screen() 
        time.sleep(60)

def getIn(lcd, lcd_lock):
    inp = raw_input('Input: ')
#    lcd_lock.acquire()
#    print('Lock acquired')
    lcd.write_msg_to_screen(inp)
    time.sleep(15)
#    lcd_lock.release()
#    print('Lock released')

if __name__ == "__main__":
    main()
