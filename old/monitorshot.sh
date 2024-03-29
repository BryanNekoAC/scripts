#!/bin/bash

MONITORS=$(xrandr | grep -o '[0-9]*x[0-9]*[+-][0-9]*[+-][0-9]*')
# Get the location of the mouse
XMOUSE=$(xdotool getmouselocation | awk -F "[: ]" '{print $2}')
YMOUSE=$(xdotool getmouselocation | awk -F "[: ]" '{print $4}')

for mon in ${MONITORS}; do
  # Parse the geometry of the monitor
  MONW=$(echo ${mon} | awk -F "[x+]" '{print $1}')
  MONH=$(echo ${mon} | awk -F "[x+]" '{print $2}')
  MONX=$(echo ${mon} | awk -F "[x+]" '{print $3}')
  MONY=$(echo ${mon} | awk -F "[x+]" '{print $4}')
  # Use a simple collision check
  if (( ${XMOUSE} >= ${MONX} )); then
    if (( ${XMOUSE} <= ${MONX}+${MONW} )); then
      if (( ${YMOUSE} >= ${MONY} )); then
        if (( ${YMOUSE} <= ${MONY}+${MONH} )); then
          # We have found our monitor!
          maim -u -B -m 2 -g "${MONW}x${MONH}+${MONX}+${MONY}" ~/Pictures/screenshots/Screenshot_$(date '+%F_%T').png  
          exit 0
        fi
      fi
    fi
  fi
done
exit 1
