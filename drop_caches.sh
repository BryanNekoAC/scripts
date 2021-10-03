#!/bin/bash

now=`date`

sync && echo 1 | sudo tee /proc/sys/vm/drop_caches && sync && echo 2 | sudo tee  /proc/sys/vm/drop_caches && sync && echo 3 | sudo tee  /proc/sys/vm/drop_caches && echo "Drop chaches fue ejecutado en: $now/" >> $HOME/.shlogs.txt

exit 0