#!/bin/bash

# set system date/time to arbitrary date/time
date -s "01/01/2018 00:01"
sleep 1

# kill NTP (network time protocol) services 
pkill ntpd
# kill GPS service 
pkill gpsd

# configure GPS to write to storage
gpsd -b -n -D 2 [USB_DIRECTORY]
sleep 2

# get GPS date/time
GPSDATE='WRITEME'
echo $GPSDATE

# set system date/time to GPS/time
date -s "$GPSDATE"

# get local time
# (wait and see if we need to offset)

# restart NTP services
/usr/sbin/ntpd

