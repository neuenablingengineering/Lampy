import threading
import time
import sys
from outputs.lcd.display_message import LCDDisplay
lcd = LCDDisplay()

class TimeThread(threading.Thread):
    def __init__(self, lcd):
        threading.Thread.__init__(self)
        lcd = lcd
    def run(self):
        while (True):
            lcd.write_time_to_screen()
            time.sleep(60)

class InputThread(threading.Thread):
    def __init__(self, lcd):
        threading.Thread.__init__(self)
        lcd = lcd
    def run(self):
        inp = raw_input("Give input:")
        lcd.write_msg_to_screen(inp)
        time.sleep(30)
        sys.exit() 

def main():
    lcd_lock = threading.Lock();

    
    t_thread = TimeThread(lcd)
    inp_thread = InputThread(lcd)
    t_thread.start()
    inp_thread.start()

    

if __name__ == "__main__":
    main()



