import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import string

fromaddr="watcher@dfnplus.com"
#toaddr="feed.alerts@gtngroup.com"
toaddr="p.ashan@gtngroup.com"
#toaddr="t.pulendran@gtngroup.com"
#toaddr="s.daminda@theglobalmarketaccess.com"





def mail_send(processname):
 msg = MIMEMultipart()
 msg['From'] = fromaddr
 msg['To'] = toaddr
 msg['Subject'] = " UAT- %s COMPONENT IS DOWN" % processname

 body = """172.18.29.151 - %s COMPONENT IS DOWN""" % processname
 msg.attach(MIMEText(body, 'plain'))

 server = smtplib.SMTP('172.18.41.71')
 server.starttls()
 text = msg.as_string()
 server.sendmail(fromaddr, toaddr, text)
 server.quit()

