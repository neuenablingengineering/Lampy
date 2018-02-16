from global_config import *
from time_thread import TimeThread
from set_alarm_thread import SetAlarmThread

def main():
    tThread = TimeThread()
    tThread.start()
    setAlarmThread = SetAlarmThread()
    setAlarmThread.start()
            
    

if __name__ == "__main__":
    main()

