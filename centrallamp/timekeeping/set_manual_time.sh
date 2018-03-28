#!/bin/bash

# manual inputs should be either 'm' (to set time/date from prompts)
# or arg1 == 'mm/dd/yyyy' arg2 == 'hh:mm' (in 24 hr time)

timedatectl set-ntp 0

if [ "$1" == "m" ]
then
	echo "Please enter dates in mm/dd/yyyy or hh/mm format when prompted."
	read -p 'Hour: ' hour
	read -p 'Minute: ' minute
	read -p 'Numerical Month: ' month
	read -p 'Numerical Day: ' day

	echo "You entered $month/$day/2018 $hour:$minute"

MANUALDATE="$month/$day/2018 $hour:$minute"
else
MANUALDATE="$1 $2"
fi

read -p "You have entered $MANUALDATE. Set this time? [y/n] " confirm
if [ "$confirm" == "y" ]
then
	date -s "$MANUALDATE"
fi

sleep 1
#timedatectl set-ntp 1
