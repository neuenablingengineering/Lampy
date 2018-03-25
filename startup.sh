#!/bin/bash

echo "Setting time"
sudo sh /home/cap/Lampy/fallback_set_time.sh

echo "hciconfig"
hciconfig hci0 up

echo "starting"
python /home/cap/Lampy/centrallamp/__main__.py


