#!/bin/bash

# Script to manually set time

# Call Python script to interact with LCD/Buttons
NEWTIME=$(python /home/cap/Lampy/set_time.py)

# For debugging print variable value to command line
echo "$NEWTIME"

# Set new time
date -s "$NEWTIME"

