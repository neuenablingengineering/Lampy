import threading
import time
import sys
import datetime as dt
from outputs.lcd.display_message import LCDDisplay

lcd = LCDDisplay()

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timenow = dt.datetime.now()
        currMin = timenow.minute
        lcd.write_time_to_screen()
        while (True):
            if (currMin != dt.datetime.now().minute):
                lcd.write_time_to_screen()
                currMin = dt.datetime.now().minute 

class InputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        inp = raw_input("Give input:")
        lcd.write_msg_to_screen(inp)
        time.sleep(20)
        sys.exit() 

def main():
    lcd_lock = threading.Lock();

    
    t_thread = TimeThread()
    inp_thread = InputThread()
    t_thread.start()
    inp_thread.start()

    

if __name__ == "__main__":
    main()

