#!/usr/bin/python

import pip
import time
import threading
import os
import sys
import subprocess

def import_or_install(module):
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

#import_or_install('random')
#import random

# Start of obtain ac_status

#Full
#Discharging
#Not charging
#Charging


ac_get_status_command = os.popen("cat /sys/class/power_supply/BAT*/uevent | grep -i 'POWER_SUPPLY_STATUS='")
ac_get_status_command_output = ac_get_status_command.read()

#print(ac_get_status_command_output)

def get_ac_status(current_status):
    ac_aviable_status = {
        'POWER_SUPPLY_STATUS=Full\n' : True,
        'POWER_SUPPLY_STATUS=Charging\n' : True,
        'POWER_SUPPLY_STATUS=Not charging\n' : True,
        'POWER_SUPPLY_STATUS=Discharging\n' : False,
    }
    #print(ac_aviable_status.get(current_status, "Invalid status"))
    return (ac_aviable_status.get(current_status, "Invalid status"))

#ac_status = get_ac_status(ac_get_status_command_output)

def get_ac_status_ftask():
    global ac_status
    ac_status = get_ac_status(ac_get_status_command_output)

get_ac_status_ftask()

#print(ac_status)

# end of obtain ac_status

#conservative 
#ondemand 
#userspace 
#powersave 
#performance 
#schedutil

def change_governor():
    if ac_status == False:
        os.system("echo powersave | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        os.system("echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo")
        os.system("echo  | sudo tee /home/d4t4/.config/governor")
    elif ac_status == True:
        os.system("echo schedutil | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        os.system("echo 0 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo")
        os.system("echo  | sudo tee /home/d4t4/.config/governor")


change_governor()
