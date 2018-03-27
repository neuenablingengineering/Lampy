#function that displays the current time to the LCD
import time
from global_config import LCD
import datetime as dt

def time_display():
    timenow = dt.datetime.now()
    currMin = timenow.minute
    LCD.write_time_to_screen()
    while (True):
        if (currMin != dt.datetime.now().minute):
            LCD.write_time_to_screen()
            currMin = dt.datetime.now().minute
            time.sleep(45)


