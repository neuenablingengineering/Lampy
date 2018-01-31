from global_config import *
from thread_classes import *

def main():
    #instantiate bright alarm? or just control in own thread
    tThread = TimeThread()
    tThread.start()
    inpThread = InputThread()
    inpThread.start()
            
    

if __name__ == "__main__":
    main()

