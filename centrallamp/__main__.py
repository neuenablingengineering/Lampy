from global_config import *
from time_display import *
from set_alarm import *
from check_alarms import TriggerThread

def main():
    tThread = TimeThread()
    tThread.start()
    setAlarmThread = SetAlarmThread()
    setAlarmThread.start()
    triggerThread = TriggerThread()
    triggerThread.start()
            
    

if __name__ == "__main__":
    main()

