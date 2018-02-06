# contains classes for the clock alarm

import datetime

class Alarm:

	def __init__(self, hour, minute):
		if hour in range(0,24) and minute in range(0,60):
			self.hour = hour
			self.minute = minute
		else:
			print("Error: Not in range. Default 12:00 alarm set")
			self.hour = 12
			self.minute = 0
	# setter -- should not allow setting outside of specified ranges
	def set_alarm(self, hour, minute):
		if hour in range(0,23) and minute in range(0,59):
			self.hour = hour
			self.minute = minute
		else:
			print("Error: Not in range")
	# getter -- return string of alarm time
	def get_alarm(self):
		return("%02d:%02d" % (self.hour, self.minute))
	# compare alarm time to system time and return true or false
	def check_time(self):
		now = datetime.datetime.now()
		if self.hour == now.hour and self.minute == now.minute:
			return True
		else:
			return False
	# increment the stored hour, don't allow hour outside of [0..23] 
	def inc_hour(self):
		self.hour += 1
		if self.hour >23:
			self.hour = 0
	# increment the stored minute, don't allow min outside of [0..59]
	def inc_min(self):
		self.minute += 1
		if self.minute > 59:
			self.minute = 0
