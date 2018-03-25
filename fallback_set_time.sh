#!/bin/bash

# Fallback script to manually set time if no radio signal can be found

# Call Python script to interact with LCD/Buttons
NEWTIME=$(python /home/cap/Lampy/fallback_set_time.py)

# For debugging print variable value to command line
echo "$NEWTIME"

# Set new time
date -s "$NEWTIME"

