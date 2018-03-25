from global_config import *
from time_display import *
from set_alarm import *
from check_alarms import TriggerThread
from multiprocessing import Process
from shutdown import ShutdownThread

def main():
    timeProc = Process(target = time_display)
    timeProc.start()
    setAlarmThread = SetAlarmThread()
    setAlarmThread.start()
    triggerThread = TriggerThread()
    triggerThread.start()
    shutdownThread = ShutdownThread()
    shutdownThread.start()            
    

if __name__ == "__main__":
    main()

