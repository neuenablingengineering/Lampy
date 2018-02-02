# contains classes for the clock alarm

import datetime

class Alarm:

	def __init__(self, hour, minute):
		if hour in range(0,23) and minute in range(0,59):
			self.hour = hour
			self.minute = minute
		else:
			print("Error: Not in range. Default 12:00 alarm set")
			self.hour = 12
			self.minute = 0
	# setter -- should not allow setting outside of specified ranges
	def setAlarm(self, hour, minute):
		if hour in range(0,23) and minute in range(0,59):
			self.hour = hour
			self.minute = minute
		else:
			print("Error: Not in range")
	# getter -- return string of alarm time
	def getAlarm(self):
		return("%02d:%02d" % (self.hour, self.minute))
	# compare alarm time to system time and return true or false
	def checkTime(self):
		now = datetime.datetime.now()
		if self.hour == now.hour and self.minute == now.minute:
			return True
		else:
			return False
	# increment the stored hour, don't allow hour outside of 
	def incHour(self):
		self.hour += 1
		if self.hour >23:
			self.hour = 0
	def incMin(self):
		self.minute += 1
		if self.minute > 59:
			self.minute = 0
