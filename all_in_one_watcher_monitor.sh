#!/bin/sh

numproc=`ps x | grep -ai all_in_one_watcher.py | grep -v "grep" | wc -l`
if [ $numproc -lt 1 ]
then
cd /home/directfn/app/all_in_one_watcher
nohup python3 all_in_one_watcher.py > logs/all_in_one_watcher.out 2> logs/all_in_one_watcher.err &
fi

