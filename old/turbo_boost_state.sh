#!/bin/bash

on="0"
off="1"

echo "Los estados disponibles son: "

echo "1- Turbo Boost On
2- Turbo Boost Off"

read -p "Introduce el estado que desea configurar: " choice

usr_choice=''

case $choice in 
1) usr_choice="$on";;
2) usr_choice="$off";;
esac

echo $usr_choice | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo 

echo "Listo"

exit 0
