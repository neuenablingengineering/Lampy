#!/bin/bash

# manual inputs should be either 'm' (to set time/date from prompts)
# or arg1 == 'mm/dd/yyyy' arg2 == 'hh:mm' (in 24 hr time)

# stop NTP services
pkill ntpd

# still need to modify this to set the date/time with  "date -s"
# and receive the new time/date arguments from user input

if [ "$1" == "m" ]
then
	read -p 'Hour: ' hour
	read -p 'Minute: ' minute
	read -p 'Numerical Month: ' month
	read -p 'Numerical Day: ' day
	read -p 'Year: ' year

	echo "You entered $month/$day/2018 $hour:$minute"

MANUALDATE="$month/$day/2018 $hour:$minute"
else
MANUALDATE="$1 $2"

fi
echo $MANUALDATE

date -s "$MANUALDATE"

date

# restart NTP services
/usr/sbin/ntpd
