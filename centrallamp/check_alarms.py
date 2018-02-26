from global_config import *
import time
from pygame import mixer

def check_alarms_main():
    mixer.init()
    # Alarm sound courtesy FoolBoyMedia (c) Creative Commons Attribution Non-Commercial 3.0 License
    # https://freesound.org/people/FoolBoyMedia/sounds/246390/
    # https://creativecommons.org/licenses/by-nc/3.0/
    mixer.music.load('outputs/sound/chiming-out_foolboymedia.mp3')
    while(True):
        if DAY_NIGHT_ALARM.check_morning_alarm():
            LAMP_BULBS.morning_sequence()
            # TODO placeholder for sound
            mixer.music.play()
            # TODO placeholder for BLE communication with mat
            # TODO placeholder for BLE communication with panel
        if DAY_NIGHT_ALARM.check_dusk_sim_alarm():
            LAMP_BULBS.evening_sequence()
        if PANEL_STAY_AWAKE.check_time():
            # TODO placeholder for BLE communication with panel
        # sleep for a while
        time.sleep(60)
 
