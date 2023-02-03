#!/bin/sh

count=0
end=30

i1=15
i2=30
i3=45

while [ $end -ge $count ]
do

  sleep 15

  let count=$count+15

  if [[ "$count" == "$i1" ]]
  then
    #paste here runs at 15 seccond
    #python /home/d4t4/scripts/auto_power_state.py
  fi  

  if [[ "$count" == "$i2" ]]
  then
    #paste here runs at 30 seccond
    #python /home/d4t4/scripts/auto_power_state.py
  fi

  if [[ "$count" == "$i3" ]]
  then
    #paste here runs at 45 seccond
    #python /home/d4t4/scripts/auto_power_state.py
  fi
  
done

exit 0
