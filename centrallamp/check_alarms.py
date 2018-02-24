from global_config import *
import time
import subprocess

def check_alarms_main():
    # Alarm sound courtesy FoolBoyMedia (c) Creative Commons Attribution Non-Commercial 3.0 License
    # https://freesound.org/people/FoolBoyMedia/sounds/246390/
    # https://creativecommons.org/licenses/by-nc/3.0/
    while(True):
        if DAY_NIGHT_ALARM.check_morning_alarm():
            print "Morning alarm triggered"
            # LAMP_BULBS.morning_sequence()
            # TODO stop the music from playing with BLE mat input
            # TODO add '--loop' arg once BLE mat stop is enabled
            subprocess.Popen(['omxplayer','--no-keys',  '--amp', '1000', 'outputs/sound/chiming-out_foolboymedia.mp3'])
            # TODO placeholder for BLE communication with mat
            # TODO placeholder for BLE communication with panel
        if DAY_NIGHT_ALARM.check_dusk_sim_alarm():
            print "Evening alarm triggered"
            LAMP_BULBS.evening_sequence()
        if PANEL_STAY_AWAKE.check_time():
            print "LED Panel alarm triggered"
            # TODO placeholder for BLE communication with panel
            time.sleep(1)
        # sleep for a while
        print "Sleeping for twenty seconds..."
        time.sleep(20)
 
