import threading
import time
from outputs.lcd.display_message import LCDDisplay


def main():
    lcd = LCDDisplay()
    displayTime = threading.Thread(group=None, target=keepTime(lcd), name=Time)
    getInput = threading.Thread(group=None, target=getIn(lcd),
name=Input)


def keepTime(lcd):
    while (True):
        lcd.write_time_to_screen() 
        time.sleep(60)

def getIn(lcd):
    in = input("Input: ")
    lcd.write_msg_to_screen(in)
    time.sleep(30)

if __name__ == "__main__":
    main()
