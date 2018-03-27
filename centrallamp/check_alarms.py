from global_config import *
import time
import subprocess
import threading
from subprocess import call
#from connectivity.find_pair_mat import mat_detected
import os
import pygatt
import logging
from binascii import hexlify

class TriggerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # Alarm sound courtesy FoolBoyMedia (c) Creative Commons Attribution Non-Commercial 3.0 License
        # https://freesound.org/people/FoolBoyMedia/sounds/246390/
        # https://creativecommons.org/licenses/by-nc/3.0/
        while(True):
            if not DAY_NIGHT_ALARM.get_alarm_mode():
                if DAY_NIGHT_ALARM.check_morning_alarm():
                    print "Morning alarm triggered"
                    LAMP_BULBS.morning_sequence()
                    
                    soundSubProc = subprocess.Popen(['omxplayer','--no-keys'
                        , '--amp', '1000', '--loop', 'outputs/sound/chiming-out_foolboymedia.mp3'])
                    
                    #BLE communication with panel -- light on
                    subprocess.Popen(['expect', 'connectivity/tcl_panel_conn.sh', '0x4D'])
                    #subprocess.Popen(['python', 'connectivity/alarm_with_hush.py'])
    
                    #time.sleep(15)
                    MATTY_ADDR = "CC:5A:BC:A3:05:6F"
                    ADDR_TYPE = pygatt.BLEAddressType.random
                    time.sleep(5)

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
                        #soundSubProc.terminate()
                        subprocess.call(["pkill", "omx"])
                    

                if DAY_NIGHT_ALARM.check_dusk_sim_alarm():
                    print "Evening alarm triggered"
                    LAMP_BULBS.evening_sequence()
                if PANEL_STAY_AWAKE.check_time():
                    print "LED Panel alarm triggered"
                    
                    #BLE communication with panel -- light on
                    subprocess.Popen(['expect', 'connectivity/tcl_panel_conn.sh', '0x4D'])
                    
                    time.sleep(1)
                # sleep for a while
                print "Sleeping for twenty seconds..."
                DAY_NIGHT_ALARM.print_both()
                time.sleep(20)
     
