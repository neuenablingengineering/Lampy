# contains classes for the clock alarm

class Alarm:

	def __init__(self, hour, minute):
		if hour in range(0,23) and minute in range(0,59):
			self.hour = hour
			self.minute = minute
		else:
			print("Error: Not in range")
	# setter -- should not allow setting outside of specified ranges
	def setAlarm(self, hour, minute):
		if hour in range(0,23) and minute in range(0,59):
			self.hour = hour
			self.minute = minute
		else:
			print("Error: Not in range")
	# getter -- return string of alarm time
	def getAlarm(self):
		return("%s:%s" % (self.hour, self.minute))
	
