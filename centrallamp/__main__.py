import threading
import time
from outputs.lcd.display_message import LCDDisplay


def main():
    lcd = LCDDisplay()
    displayTime = threading.Thread(group=None, target=keepTime(lcd), name=Time)

def keepTime(lcd):
    while (True):
        lcd.write_time_to_screen() 
        time.sleep(60)
        

if __name__ == "__main__":
    main()
