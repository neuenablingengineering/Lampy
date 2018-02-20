import threading
import time
import datetime as dt
from outputs.lcd.display_message import LCDDisplay
from timekeeping.dual_alarm import DualAlarm
from timekeeping.alarm import Alarm


LCD = LCDDisplay()
LCD_CONTROL_BOOL = False
DAY_NIGHT_ALARM = DualAlarm()
PANEL_STAY_AWAKE = Alarm()

