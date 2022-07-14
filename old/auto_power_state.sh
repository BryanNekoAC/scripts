#!/bin/bash

ac_status=$(cat /sys/class/power_supply/BAT*/uevent | grep -i 'POWER_SUPPLY_STATUS=')
# cat /sys/class/power_supply/BAT*/uevent | grep -i 'POWER_SUPPLY_STATUS='


echo "$ac_status"



exit 0
