#!/usr/bin/python3.9
from curses import echo
import datetime
import configparser
from send_mail import mail_send 
import time
import subprocess
import logging
from time import sleep
import os
parser = configparser.ConfigParser()
parser.read('config.ini')
logging.basicConfig(filename='warning.log', level=logging.DEBUG)
def checkIfProcessNotRunning(processname):
   process = subprocess.Popen("ps x|grep -ai {} |grep -v grep |wc -l".format(processname),
                           shell=True, stdout=subprocess.PIPE,
                           universal_newlines=True)
   output=int(process.stdout.read())
   if output > 0:
    return False
   else:
    return True

while True:    
 for section_name in parser.sections():
    value = parser.items(section_name)
    name = value[0][1]
    starttime = value[1][1]
    stoptime = value[2][1]
    weekday =value[3][1]
    description = value[4][1]
    needToUp = value[5][1]
    try:
        runScriptPath = value[6][1]
        runScript = value[7][1]
    except:
        continue
    currenttime = datetime.datetime.now().strftime("%H:%M:%S")
    weekdaytime = datetime.datetime.now().weekday()

    if (str(weekdaytime) in str(weekday)):
        if starttime < currenttime and currenttime < stoptime:
            if checkIfProcessNotRunning(name):
                if needToUp == 'Yes':
                     mail_send(name)
                     os.chdir(runScriptPath)
                     subprocess.call(['sh', runScript])
                     time.sleep(20) 
                     with open('watcher-log.txt', 'a') as f:
                        f.write(currenttime + ":" + name + " is not running")
                        f.write('\n')
                else:
                     mail_send(name)
                     with open('watcher-log.txt', 'a') as f:
                        f.write(currenttime + ":" + name + " is not running")
                        f.write('\n')

    
        
