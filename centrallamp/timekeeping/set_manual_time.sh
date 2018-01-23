#!/bin/bash

# stop NTP services
#pkill ntpd

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
