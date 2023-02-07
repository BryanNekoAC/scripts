#!/usr/bin/python

import os
import sys

# get the hostname
hostname = os.uname()[1]

# define the xrandr command
xrandr = "xrandr"

# the script needs one parameter or argument, is the number of the option,
# if the parameter is not present, not is a number or is not in the range, or is the -h or --help, show the help message and exit
# if the parameter is a number, and is in the range, execute the command xrandr with the option selected
# aditionaly, use the vars xedp, xhdmi and xvga to turn off the screens

if hostname == "node":
    primary = " --primary"
    edp = " --output eDP1 --mode 1600x900"
    hdmi = " --output HDMI1 --mode 1920x1080"
    vga = " --output VGA1 --mode 1366x768"
    htmi_alt = " --output HDMI1 --mode 1280x720"
    xedp = " --output eDP1 --off"
    xhdmi = " --output HDMI1 --off"
    xvga = " --output VGA1 --off"
    loedp = " --left-of eDP1"
    roedp = " --right-of eDP1"
    message = "1- eDP (only)\n2- VGA (only)\n3- HDMI (only)\n4- eDP + VGA\n5- eDP + HDM1\n6- eDP + HMDI + VGA\n7- HDMI GAMES"
    if len(sys.argv) == 1:
        print(message)
        sys.exit(0)
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(message)
        sys.exit(0)
    elif sys.argv[1].isdigit() and int(sys.argv[1]) in range(1,8):
        if sys.argv[1] == "1":
            os.system(xrandr + edp + primary + xhdmi + loedp + xvga + roedp)
        elif sys.argv[1] == "2":
            os.system(xrandr + xedp + xhdmi + loedp + vga + primary + roedp)
        elif sys.argv[1] == "3":
            os.system(xrandr + xedp + hdmi + primary + loedp + xvga + roedp)
        elif sys.argv[1] == "4":
            os.system(xrandr + edp + primary + xhdmi + loedp + vga + roedp)
        elif sys.argv[1] == "5":
            os.system(xrandr + edp + primary + hdmi + loedp + xvga + roedp)
        elif sys.argv[1] == "6":
            os.system(xrandr + edp + primary + hdmi + loedp + vga + roedp)
        elif sys.argv[1] == "7":
            os.system(xrandr + xedp + htmi_alt + primary + loedp + xvga + roedp)
    else:
        print(message)
        sys.exit(0)
elif hostname == "DC-BR":
    primary = " --primary"
    edp = " --output eDP-1 --mode 1366x768"
    hdmi = " --output HDMI-1 --mode 1920x1080 --rate 144.00"
    xedp = " --output eDP-1 --off"
    xhdmi = " --output HDMI-1 --off"
    loedp = " --left-of eDP-1"
    message = "1- eDP (only)\n2- HDMI (only)\n3- eDP + HDMI"
    if len(sys.argv) == 1:
        print(message)
        sys.exit(0)
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(message)
        sys.exit(0)
    elif sys.argv[1].isdigit() and int(sys.argv[1]) in range(1,4):
        if sys.argv[1] == "1":
            os.system(xrandr + edp + primary + xhdmi + loedp)
        elif sys.argv[1] == "2":
            os.system(xrandr + xedp + hdmi + primary + loedp)
        elif sys.argv[1] == "3":
            os.system(xrandr + edp + primary + hdmi + loedp)
    else:
        print(message)
        sys.exit(0)
else:
    print("Hostname not found")
    sys.exit(0)

# simulate the key combination Win+Shift+r to reload the wm configuration
os.system("xdotool keydown Super_L keydown Shift_L key r keyup Shift_L keyup Super_L")
sys.exit(0)
