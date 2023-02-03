#!/usr/bin/python

import os
import sys

# get the hostname
hostname = os.uname()[1]

if hostname == "node":
    edp = " --output eDP1 --mode 1600x900"
    hdmi = " --output HDMI1 --mode 1920x1080"
    vga = " --output VGA1 --mode 1366x768"
    htmi_alt = " --output HDMI1 --mode 1280x720"
    xedp = " --output eDP1 --off"
    xhdmi = " --output HDMI1 --off"
    xvga = " --output VGA1 --off"
    message = "1. Laptop only\n2. "
elif hostname == "DC-BR":
    edp = " --output eDP1 --mode 1366x768"
    hdmi = " --output HDMI1 --mode 1920x1080"
    xedp = " --output eDP1 --off"
    xhdmi = " --output HDMI1 --off"

# get the parameter passed to the script, if is -h or --help, print the help
# message
if len(sys.argv) > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: screens.py [OPTION]")
        print("Options:")
        print("  -h, --help\t\tPrint this help message")
        print("  -e, --edp\t\tTurn on the laptop screen")
