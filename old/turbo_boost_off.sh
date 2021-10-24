#!/bin/bash

now=`date`

echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo && echo "Turbo boost off fue ejecutado en: $now/" >> $HOME/.shlogs.txt

exit 0