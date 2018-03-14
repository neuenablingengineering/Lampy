#!/bin/bash

##### 1.  
#   Attempt to get system time from WWVB
# TODO sh ./radio_set_time.sh &
#       If successful 
#           continue
#       If not successful within TIMEOUT
#           run fallback script
sh ./fallback_set_time.sh &

# 2. 
# TODO flush serial? has to be done within Python

#3.turn on Bluetooth
sudo hciconfig hci0 up

#4.    
python __main__.py &

# 4.5 listen for TURN_OFF signal (GPIO)
#       TODO shutdown.py
#           turn off bulbs
#           close BLE
#           close GPIO
#           flush serial

python shutdown.py &
