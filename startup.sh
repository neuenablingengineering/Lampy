#!/bin/bash

echo "hciconfig"
hciconfig hci0 up

echo "Setting time"
sudo sh /home/cap/Lampy/set_time.sh

echo "Starting main"
python /home/cap/Lampy/centrallamp/__main__.py
