import threading
import time
import sys
import datetime as dt
from outputs.lcd.display_message import LCDDisplay

lcd = LCDDisplay()
lcdBool = False

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timenow = dt.datetime.now()
        currMin = timenow.minute
        lcd.write_time_to_screen()
        while (True):
            if ((currMin != dt.datetime.now().minute) 
                &  (lcdBool == False)):
                lcd.write_time_to_screen()
                currMin = dt.datetime.now().minute 

class InputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        inp = raw_input("Give input:")
        lcdBool = True
        lcd.write_msg_to_screen(inp)
        time.sleep(20)
        print "Releasing the lock"
        lcd.write_time_to_screen()
        lcdBool = False
        sys.exit() 

def main():
    tThread = TimeThread()
    tThread.start()
    inpThread = InputThread()
    inpThread.start()
            
    

if __name__ == "__main__":
    main()

