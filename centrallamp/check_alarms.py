from global_config import *
import time
import subprocess
import threading
import os
import pygatt

class TriggerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.isTriggeredMorning = False
        self.isTriggeredNight = False
        self.isTriggeredStayAwake = False

    def run(self):
        # Alarm sound courtesy FoolBoyMedia (c) Creative Commons Attribution Non-Commercial 3.0 License
        # https://freesound.org/people/FoolBoyMedia/sounds/246390/
        # https://creativecommons.org/licenses/by-nc/3.0/
        while(True):
            if not DAY_NIGHT_ALARM.get_alarm_mode():
                if (DAY_NIGHT_ALARM.check_morning_alarm() and not self.isTriggeredMorning):
                    isTriggeredMorning = True
                    print "Morning alarm triggered"
                    th = threading.THREAD(target = LAMP_BULBS.morning_sequence())
                    th.start()
                    
                    #BLE communication with panel -- light on
                    subprocess.Popen(['expect', 'connectivity/tcl_panel_conn.sh', '0x4D'])
   
                    MATTY_ADDR = "CC:5A:BC:A3:05:6F"
                    ADDR_TYPE = pygatt.BLEAddressType.random
                    time.sleep(5)

                    soundSubProc = subprocess.Popen(['omxplayer','--no-keys'
                        , '--amp', '1000', '--loop', 'outputs/sound/chiming-out_foolboymedia.mp3'])


                    mat_detected = 0
                    while mat_detected != 1:
                        #call the command and write to scan.txt file and then fill the process.
                        #loop to find if the MAC address given is available
                        os.system("hcitool lescan> scan.txt & pkill --signal SIGINT hcitool")
                        scan = open("scan.txt","r")
                        readscan = scan.read()
                        if MATTY_ADDR in readscan:
                            print "Matty detected!"
                            mat_detected = 1
                        else:
                            print "Couldn't find Matty in range"
                            time.sleep(1)


                    if mat_detected == 1:
                        subprocess.Popen(['expect', 'connectivity/tcl_panel_conn.sh', '0x4E'])
                        print "attempt to kill subproc"
                        subprocess.call(["pkill", "omx"])
                        self.isTriggeredMorning = False

                        
                if (DAY_NIGHT_ALARM.check_dusk_sim_alarm() and not self.isTriggeredNight):
                    self.isTriggeredNight = True
                    print "Evening alarm triggered"
                    LAMP_BULBS.evening_sequence()
                if not DAY_NIGHT_ALARM.check_dusk_sim_alarm():
                    self.isTriggeredNight = False
                if (PANEL_STAY_AWAKE.check_time() and not self.isTriggeredStayAwake):
                    self.isTriggeredStayAwake = True
                    print "LED Panel alarm triggered"
                    
                    #BLE communication with panel -- light on
                    subprocess.Popen(['expect', 'connectivity/tcl_panel_conn.sh', '0x4D'])
                    
                    time.sleep(1)
                if not PANEL_STAY_AWAKE.check_time():
                    self.isTriggeredStayAwake = False
                # sleep for a while
                print "Sleeping for twenty seconds..."
                DAY_NIGHT_ALARM.print_both()
                time.sleep(20)
     
