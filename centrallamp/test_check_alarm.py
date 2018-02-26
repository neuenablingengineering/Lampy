from multiprocessing import Process
from global_config import *
from time_display import *
from set_alarm import *
from check_alarms import *

def main():
    timeProc = Process(target = time_display)
    setAlarmProc = Process(target = set_alarm_main)
    checkAlarmProc = Process(target = check_alarms_main)
    timeProc.start()
    setAlarmProc.start()
    checkAlarmProc.start()
            
    

if __name__ == "__main__":
    main()

