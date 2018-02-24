from global_config import *
import time

def check_alarms_main():
    while(True):
        if DAY_NIGHT_ALARM.check_morning_alarm():
            LAMP_BULBS.morning_sequence()
            # TODO placeholder for sound
            # TODO placeholder for BLE communication with mat
            # TODO placeholder for BLE communication with panel
        if DAY_NIGHT_ALARM.check_dusk_sim_alarm():
            LAMP_BULBS.evening_sequence()
        if PANEL_STAY_AWAKE.check_time():
            # TODO placeholder for BLE communication with panel
    # sleep for a while
    time.sleep(60)
 
