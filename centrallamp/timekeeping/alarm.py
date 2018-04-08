# Contains Alarm class

import datetime

class Alarm:
    
    #default chosen based on the afternoon bright light alarm
    def __init__(self, hour=16, minute=0):
        if hour in range(0,24) and minute in range(0,60):
            self.hour = hour
            self.minute = minute
        else:
            print("Error: Not in range. Default 12:00 alarm set")
            self.hour = 12
            self.minute = 0
    # setter -- should not allow setting outside of specified ranges
    def set_alarm(self, hour, minute):
        if hour in range(0,24) and minute in range(0,60):
            self.hour = hour
            self.minute = minute
        else:
            print("Error: Not in range")
    # getter -- return string of alarm time
    def get_alarm(self):
        # set the correct AM/PM to display on clock
        if self.hour > 11:
            self.period = "PM"
        else:
            self.period = "AM"
        if self.hour % 12 == 0:
            # use a temp variable to print "12" instead of "00"
            tempHour = 12
            return("%02d:%02d %s" % (tempHour, self.minute, self.period))
        else:
            return("%02d:%02d %s" % ((self.hour % 12), self.minute, self.period))
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

    # get the minute for demo testing purposes
    def get_min(self):
        return self.minute
