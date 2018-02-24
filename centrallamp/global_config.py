import time
import datetime as dt
from outputs.lcd.display_message import LCDDisplay
from timekeeping.dual_alarm import DualAlarm
from timekeeping.alarm import Alarm
from bulbcontrol.bulb import Bulb

LCD = LCDDisplay()
LCD_CONTROL_BOOL = False
DAY_NIGHT_ALARM = DualAlarm()
PANEL_STAY_AWAKE = Alarm()
DAY_BULB = Bulb(12, 80, 0.1, 10)
NIGHT_BULB = Bulb(13, 80, 10, 0.1)

