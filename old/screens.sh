#!/bin/bash

primary=" --primary"

edp=" --output eDP1 --mode 1600x900"
vga=" --output VGA1 --mode 1366x768"
hdmi=" --output HDMI1 --mode 1920x1080"
hdmialt=" --output HDMI1 --mode 1280x720"

xedp=" --output eDP1 --off"
xvga=" --output VGA1 --off"
xhdmi=" --output HDMI1 --off"

#wall="feh --bg-fill --randomize $HOME/Pictures/walls/*"
lofedp=" --left-of eDP1"
rofedp=" --right-of eDP1"

echo "Los estados disponibles son: "

echo "1- eDP (only) 
2- VGA (only) 
3- HDMI (only) 
4- eDP + VGA 
5- eDP + HDM1 
6- eDP + HMDI + VGA
7- HDMI GAMES"

read -p "Introduce el estado que desea configurar: " choice

usr_choice=''

case $choice in 
1) usr_choice="$edp$primary$xhdmi$xvga";;
2) usr_choice="$xedp$xhdmi$vga$primary";;
3) usr_choice="$xedp$hdmi$primary$xvga";;
4) usr_choice="$edp$primary$xhdmi$vga$rofedp";;
5) usr_choice="$edp$primary$hdmi$lofedp$xvga";;
6) usr_choice="$edp$primary$hdmi$lofedp$vga$rofedp";;
7) usr_choice="$xedp$hdmialt$primary$xvga";;
esac

xrandr $usr_choice

#echo $usr_choice


#$wall

#killall compton
#killall picom

#xdotool key "super+shift+r"

i3-msg restart &>/dev/null &

echo "Listo"

exit 0
