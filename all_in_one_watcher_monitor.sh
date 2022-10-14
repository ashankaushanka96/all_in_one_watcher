#!/bin/sh

numproc=`ps x | grep -ai all_in_one_watcher.py | grep -v "grep" | wc -l`
if [ $numproc -lt 1 ]
then
cd /home/directfn/app/all_in_one_watcher
./all_in_one_watcher_run.sh
fi

