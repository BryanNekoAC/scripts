#!/bin/bash

current_state=$(cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor | sort -u)

aviable_states=$(cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors | sort -u)


#var=$( cat foo.txt )

echo "El estado actual es: $current_state"

echo "Los estados disponibles son: $aviable_states"

echo "Lista de estados: 
1- conservative 
2- ondemand 
3- userspace 
4- powersave 
5- performance 
6- schedutil"

read -p "Introduce el estado que desea configurar: " choice

usr_choice=''

case $choice in 
1) usr_choice="conservative";;
2) usr_choice="ondemand";;
3) usr_choice="userspace";;
4) usr_choice="powersave";;
5) usr_choice="performance";;
6) usr_choice="schedutil";;
esac

echo $usr_choice | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

current_state=$(cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor | sort -u)

echo "El estado fue configurado a: $current_state"

exit 0
