#!/bin/bash

echo "hciconfig"
hciconfig hci0 up

echo "Setting time"
sudo date -s "04/01/2018 10:00"

echo "Starting main"
python /home/cap/Lampy/centrallamp/__main__.py
