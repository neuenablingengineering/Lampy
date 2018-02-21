from global_config import *
from time_thread import *
from set_alarm_thread import *

def main():
    timeProc = Process(target = time_thread)
    setAlarmProc = Process(target = set_alarm_thread)
            
    

if __name__ == "__main__":
    main()

