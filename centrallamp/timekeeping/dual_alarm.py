from alarm import Alarm
HOUR = 8
MINUTE = 30
OFFSET = 9

class DualAlarm:
    # Initiate DualAlarm with a morning and dusk simulation alarm
    # Takes as an input the hour and minute of the morning alarm
    def __init__(self, hour=HOUR, minute=MINUTE):
        self.morningAlarm = Alarm(hour%24,minute%60)
        self.duskAlarm = Alarm((hour-OFFSET)%24, minute%60)

    # Sets the morning alarm to specified time
    # Dusk alarm is set 9 hours before morning
    def set_morning_dusk_sim_alarms(self, hour, minute):
        self.morningAlarm.set_alarm(hour%24,minute%60)
        self.duskAlarm.set_alarm((hour-OFFSET)%24,minute%60)

    # Returns a string with the current morning alarm time
    def get_morning_alarm(self):
        return self.morningAlarm.get_alarm()

    # Returns a string with the current dusk alarm time
    def get_dusk_sim_alarm(self):
        return self.duskAlarm.get_alarm()

    # Returns true if morning alarm matches system time
    def check_morning_alarm(self):
        return self.morningAlarm.check_time()

    # Returns true if dusk alarm matches system time
    def check_dusk_sim_alarm(self):
        return self.duskAlarm.check_time()

    # Increments the morning and dusk alarms by one hour
    def increment_both_hour(self):
        self.morningAlarm.inc_hour()
        self.duskAlarm.inc_hour()

    # Increments the morning and dusk alarms by one minute
    def increment_both_min(self):
        self.morningAlarm.inc_min()
        self.duskAlarm.inc_min()

    # Reset alarm times with morning 8:30 alarm
    def reset(self):
        self.morningAlarm.set_alarm(HOUR,MINUTE)
        self.duskAlarm.set_alarm((HOUR-OFFSET)%24,MINUTE)
