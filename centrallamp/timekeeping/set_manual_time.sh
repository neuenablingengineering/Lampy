#!/bin/bash

# stop NTP services
#pkill ntpd

# still need to modify this to set the date/time with  "date -s"
# and receive the new time/date arguments from user input

if [ "$1" == "m" ]
then
	read -p 'Hour: ' hour
	read -p 'Minute: ' minute
	read -p 'Numerical Month: ' month
	read -p 'Numerical Day: ' day

	echo "You entered $month/$day/2018 $hour:$minute"

MANUALDATE="$month/$day/2018 $hour:$minute"
else
MANUALDATE="02/03/2017 18:13"

fi
echo $MANUALDATE

# restart NTP services
#/usr/sbin/ntpd
