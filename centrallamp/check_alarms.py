from global_config import *
import time
import subprocess
import threading

class TriggerThread(threading.Thread):
    isTriggeredMorning = False
    isTriggeredNight = False
    isTriggeredStayAwake = False

    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # Alarm sound courtesy FoolBoyMedia (c) Creative Commons Attribution Non-Commercial 3.0 License
        # https://freesound.org/people/FoolBoyMedia/sounds/246390/
        # https://creativecommons.org/licenses/by-nc/3.0/
        while(True):
            if not DAY_NIGHT_ALARM.get_alarm_mode():
                if (DAY_NIGHT_ALARM.check_morning_alarm() and not isTriggeredMorning):
                    isTriggeredMorning = True
                    print "Morning alarm triggered"
                    LAMP_BULBS.morning_sequence()
                    # TODO stop the music from playing with BLE mat input
                    # TODO add '--loop' arg once BLE mat stop is enabled
                    subprocess.Popen(['omxplayer','--no-keys',  '--amp', '1000', 'outputs/sound/chiming-out_foolboymedia.mp3'])
                    # TODO placeholder for BLE communication with mat
                    # TODO placeholder for BLE communication with panel
                if not DAY_NIGHT_ALARM.check_morning_alarm():
                    isTriggeredMorning = False
                if (DAY_NIGHT_ALARM.check_dusk_sim_alarm() and not isTriggeredNight):
                    isTriggeredNight = True
                    print "Evening alarm triggered"
                    LAMP_BULBS.evening_sequence()
                if not DAY_NIGHT_ALARM.check_dusk_sim_alarm():
                    isTriggeredNight = False
                if (PANEL_STAY_AWAKE.check_time() and not isTriggeredStayAwake):
                    isTriggeredStayAwake = True
                    print "LED Panel alarm triggered"
                    # TODO placeholder for BLE communication with panel
                    time.sleep(1)
                if not PANEL_STAY_AWAKE.check_time():
                    isTriggeredStayAwake = False
                # sleep for a while
                print "Sleeping for twenty seconds..."
                DAY_NIGHT_ALARM.print_both()
                time.sleep(20)
     
