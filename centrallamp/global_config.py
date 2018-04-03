from outputs.lcd.display_message import LCDDisplay
from timekeeping.dual_alarm import DualAlarm
from timekeeping.alarm import Alarm
from bulbcontrol.dual_bulb import DualBulb
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
LCD = LCDDisplay()
DAY_NIGHT_ALARM = DualAlarm()
PANEL_STAY_AWAKE = Alarm()
LAMP_BULBS = DualBulb(80)

