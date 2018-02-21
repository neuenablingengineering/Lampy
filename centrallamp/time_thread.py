#Class for the Thread that displays time to the LCD
from global_config import *

def time_thread():
    timenow = dt.datetime.now()
    currMin = timenow.minute
    LCD.write_time_to_screen()
    while (True):
        if ((currMin != dt.datetime.now().minute)
            &  (LCD_CONTROL_BOOL == False)):
            LCD.write_time_to_screen()
            currMin = dt.datetime.now().minute
            time.sleep(45)


