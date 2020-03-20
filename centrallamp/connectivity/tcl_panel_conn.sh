#!/usr/bin/expect -f

set prompt "#"
set message [lindex $argv 0]

spawn bluetoothctl
expect $prompt

#send -- "power on\r"
#expect "Agent registered"
#expect $prompt

send -- "agent on\r"
expect "Agent registered"
expect $prompt

send -- "trust C0:0F:3E:A9:48:2C\r"
expect "trust succeeded"
expect $prompt

send -- "connect C0:0F:3E:A9:48:2C\r"
expect "Connection successful"
expect $prompt

send -- "menu gatt\r"
expect "Menu gatt"
expect $prompt

send -- "select-attribute /org/bluez/hci0/dev_C0_0F_3E_A9_48_2C/service0009/char000a\r"
sleep 1
expect $prompt

#Currently sends an M
send -- "write $message\r"
expect $prompt

send -- "back\r"
expect $prompt

send -- "disconnect C0:0F:3E:A9:48:2C\r"
expect "eof"
