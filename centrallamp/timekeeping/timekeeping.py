import time
import datetime

def print_manual_time(manualTime, manualTimeStamp):
	print manualTime + datetime.timedelta(datetime.datetime.now()-manualTimeStamp)

y = input("Year: ")
m = input("Month: ")
d = input("Day: ")
h = input("Hour: ")
mm = input("Minute: ")
manualTime = datetime.datetime(y, m, d, h, mm)
manualTimeStamp = datetime.datetime.now()
print(manualTime)
