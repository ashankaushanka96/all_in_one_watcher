#!/bin/sh

cd /home/directfn/app/all_in_one_watcher
nohup python3 all_in_one_watcher.py > logs/all_in_one_watcher.out 2> logs/all_in_one_watcher.err &
