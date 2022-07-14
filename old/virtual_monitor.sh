#!/bin/bash

on="0"
off="1"

function startVirtualMonitor () {
    xrandr --addmode VIRTUAL1 1366x768
    xrandr --output VIRTUAL1 --mode 1366x768 --left-of HDMI1
    x11vnc -usepw -display :0 -clip 1366x768+0+0 -forever -multiptr -bg -q &
    echo "Virtual monitor Iniciado"
}

function stopVirtualMonitor () {
    killall x11vnc
    xrandr --output VIRTUAL1 --off
    #xrandr --delmode VIRTUAL1 1366x768
    echo "Virtual monitor Detenido"
}

echo "Preciona la opcion que desee para Virtual Monitor: "

echo "1- Iniciar Virtual Monitor
2- Detener Virtual Monitor"

read -p "Introducir la opcion deseada: " choice

usr_choice=''

case $choice in 
1) usr_choice="$on";;
2) usr_choice="$off";;
esac

if [ "$usr_choice" == "0" ]
then
  startVirtualMonitor 
else
  stopVirtualMonitor
fi

xdotool key "super+shift+r"

echo "Listo"

exit 0



