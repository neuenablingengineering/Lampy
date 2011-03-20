from global_config import *
import time
import subprocess
import threading
from subprocess import call

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
                    # TODO stop the music from playing with BLE mat input
                    # TODO add '--loop' arg once BLE mat stop is enabled
                    subprocess.Popen(['omxplayer','--no-keys',  '--amp', '1000', 'outputs/sound/chiming-out_foolboymedia.mp3'])
                    # TODO placeholder for BLE communication with mat
                    
                    #BLE communication with panel -- light on
                    subprocess.Popen(['expect', 'connectivity/tcl_panel_conn.sh', '0x4D'])

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
     
