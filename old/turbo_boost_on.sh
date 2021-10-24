#!/bin/bash

now=`date`

echo 0 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo && echo "Turbo boost on fue ejecutado en: $now/" >> $HOME/.shlogs.txt

exit 0