#!/usr/bin/python3.9
import datetime
import configparser
from send_mail import mail_send 
import time
import subprocess
import logging
import os
parser = configparser.ConfigParser()
logging.basicConfig(filename='./logs/warning.log', format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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
   parser.read('./config/config.ini')    
   for section_name in parser.sections():
      value = parser.items(section_name)
      tag = value[0][1]
      starttime = value[1][1]
      stoptime = value[2][1]
      weekday =value[3][1]
      name = value[4][1]
      needToUp = value[5][1]
      
      currenttime = datetime.datetime.now().strftime("%H:%M:%S")
      weekdaytime = datetime.datetime.now().weekday()

      if (str(weekdaytime) in str(weekday)):
         if starttime < currenttime and currenttime < stoptime:
            if checkIfProcessNotRunning(tag):
                  if needToUp == 'Yes':
                     try:
                        runScriptPath = value[6][1]
                        runScript = value[7][1]
                     except:
                        logger.error( f":{name} : runScriptPath and runScript is not defined")
                     logger.debug( f":{name} is not running. Restarting the component")
                     mail_send(name)
                     try:
                        os.chdir(runScriptPath)
                     except:
                        logger.error( f":{name} : {runScriptPath} directory not found")
                     try:
                        output = subprocess.check_output(['sh', runScript])
                        logger.debug( f":{name} Successfully restarted the component")
                     except:
                        logger.error( f":{name} : ./{runScript} cannot execute")
                     time.sleep(18)
                  else:
                     logger.debug( f":  {name}   is not running")
                     time.sleep(3)
                     try:
                        mail_send(name)
                     except Exception as e:
                        logger.error(f":{name} : {e}")
      time.sleep(2)
    
        
