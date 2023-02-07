#!/usr/bin/python

# make a script to take screenshots, there are a tree modes:
# 1. take a screenshot of a selected area with the mouse and store in the clipboard, use maim and xclip maim -u -q -b 2 -s -n -m 2 -c 0.3,0.9,0.6 | xclip -selection clipboard -t image/png
# 2. take a screenshot entire screen and store in the $home/Pictures/screenshots directory with the name of the date and time, use maim, get the mouse location and get the geometry of the monitor where the mouse is located, to pass to maim as the argument -g (maim -u -B -m 2 -g {here pass the geometry like x+} ~/Pictures/screenshots/Screenshot_$(date '+%F_%T').png
# 3. take a screenshot of a all screens and store in the $home/Pictures/screenshots directory with the name of the date and time, use maim (maim -u -B -m 2 ~/Pictures/screenshots/Screenshot_$(date '+%F_%T').png

# import modules
import os
import sys


# get the user home directory
home = os.path.expanduser("~")

# the script needs one parameter or argument, is the number of the option,
# if the parameter is not present, not is a number or is not in the range, or is the -h or --help, show the help message and exit
# if the parameter is a number, and is in the range 1 - 3, continue with the script and take the screenshot with the selected option

# check if the script has one parameter
if len(sys.argv) == 1:
    print("Usage: screenshots.py [OPTION]\nTake a screenshot of the selected area, entire screen or all screens\nOptions:\n-h, --help\tshow this help message and exit\n1\ttake a screenshot of the selected area\n2\ttake a screenshot of entire screen\n3\ttake a screenshot of all screens")
    sys.exit()
# check if the parameter is a number
elif sys.argv[1].isdigit() == False:
    print("Usage: screenshots.py [OPTION]\nTake a screenshot of the selected area, entire screen or all screens\nOptions:\n-h, --help\tshow this help message and exit\n1\ttake a screenshot of the selected area\n2\ttake a screenshot of entire screen\n3\ttake a screenshot of all screens")
    sys.exit()
# check if the parameter is -h or --help
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("Usage: screenshots.py [OPTION]\nTake a screenshot of the selected area, entire screen or all screens\nOptions:\n-h, --help\tshow this help message and exit\n1\ttake a screenshot of the selected area\n2\ttake a screenshot of entire screen\n3\ttake a screenshot of all screens")
    sys.exit()
# check if the parameter is in the range 1 - 3, if not, show the help message and exit
elif int(sys.argv[1]) < 1 or int(sys.argv[1]) > 3:
    print("Usage: screenshots.py [OPTION]\nTake a screenshot of the selected area, entire screen or all screens\nOptions:\n-h, --help\tshow this help message and exit\n1\ttake a screenshot of the selected area\n2\ttake a screenshot of entire screen\n3\ttake a screenshot of all screens")
    sys.exit()
# if the parameter is a number, and is in the range 1 - 3, continue with the script and take the screenshot with the selected option
else:
    # if the parameter is 1, take a screenshot of the selected area
    if sys.argv[1] == "1":
        # take a screenshot of the selected area and store in the clipboard
        os.system("maim -u -q -b 2 -s -n -m 2 -c 0.3,0.9,0.6 | xclip -selection clipboard -t image/png")
    # if the parameter is 2, take a screenshot of entire screen
    elif sys.argv[1] == "2":
        # get the geometry of the monitor where the mouse is located, store only the HEIGHT=, WIDTH=, X= and Y= values to the output to pass to maim as the argument -g like (-g "MONWxMONH+MONX+MONY") use simple colision test
        # get the mouse location
        mouse = os.popen("xdotool getmouselocation").read()
        # get the geometry of the monitor where the mouse is located
        monitor = os.popen("xrandr | grep -w connected | grep -w primary | awk '{print $4}'").read()
        # get the geometry of the monitor where the mouse is located, store only the HEIGHT=, WIDTH=, X= and Y= values to the output to pass to maim as the argument -g like (-g "MONWxMONH+MONX+MONY")
        # get the HEIGHT= value
        height = monitor.split("x")[0]
        # get the WIDTH= value
        width = monitor.split("x")[1].split("+")[0]
        # get the X= value
        x = monitor.split("x")[1].split("+")[1]
        # get the Y= value
        y = monitor.split("x")[1].split("+")[2]
        # store a string with the HEIGHT=, WIDTH=, X= and Y= values to pass to maim as the argument -g like (-g "MONWxMONH+MONX+MONY"), remove all breaklines
        geometry = height + "x" + width + "+" + x + "+" + y
        geometry = geometry.replace("\n", "")
        # take a screenshot of entire screen and store in the $home/Pictures/screenshots directory with the name of the date and time
        os.system("maim -u -B -m 2 -g " + geometry + " " + home + "/Pictures/screenshots/Screenshot_$(date '+%F_%T').png")
    # if the parameter is 3, take a screenshot of all screens
    elif sys.argv[1] == "3":
        # take a screenshot of all screens and store in the $home/Pictures/screenshots directory with the name of the date and time
        os.system("maim -u -B -m 2 " + home + "/Pictures/screenshots/Screenshot_$(date '+%F_%T').png")
