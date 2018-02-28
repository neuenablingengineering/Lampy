#!/bin/bash

##### 1.  
#   Attempt to get system time from WWVB
# TODO sh ./radio_set_time.sh &
#       If successful 
#           continue
#       If not successful within TIMEOUT
#           run fallback script
# sh ./fallback_set_time.sh &
#
##### 2. 
# TODO flush serial? has to be done within Python
#
##### 3.    
# python __main__.py &
#
#   main process - global config
#
#   child process - time display
#
#   thread - alarm set
#
#   thread - alarm trigger check
#       bulb control
#       sound control
#       BLE - panel control
#       BLE - mat control 
#
#   TODO thread - manual lightbulb control signal (GPIO)
#
##### 3.5  TODO thread - listen for TURN_OFF signal (GPIO)
#       TODO shutdown.py
#           turn off bulbs
#           close BLE
#           close GPIO
#           flush serial
#   TODO python shutdown.py &
# sudo shutdown -h now &
