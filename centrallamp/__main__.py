from global_config import *
from time_display import *
from set_alarm import *
from check_alarms import TriggerThread
from bulb_control import BulbControlThread
from multiprocessing import Process

def main():
    timeProc = Process(target = time_display)
    timeProc.start()
    setAlarmThread = SetAlarmThread()
    setAlarmThread.start()
    triggerThread = TriggerThread()
    triggerThread.start()
    bulbControlThread = BulbControlThread()
    bulbControlThread.start()
            
    

if __name__ == "__main__":
    main()

