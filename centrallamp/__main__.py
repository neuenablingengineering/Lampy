import threading
import time
import sys
import datetime as dt
from outputs.lcd.display_message import LCDDisplay

lcd = LCDDisplay()
lcd_lock = threading.Lock();

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timenow = dt.datetime.now()
        currMin = timenow.minute
        lcd.write_time_to_screen()
        while (True):
            if ((currMin != dt.datetime.now().minute) 
                && !lcd_lock.locked()):
                lcd.write_time_to_screen()
                currMin = dt.datetime.now().minute 

class InputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        inp = raw_input("Give input:")
        lcd_lock.aquire()
        lcd.write_msg_to_screen(inp)
        time.sleep(20)
        release_lock()
        sys.exit() 

def release_lock():
    print "Releasing the lock"
    lcd_lock.release()
    lcd.write_time_to_screen()

def main():
    t_thread = TimeThread()
    inp_thread = InputThread()
    t_thread.start()
    inp_thread.start()

    

if __name__ == "__main__":
    main()

