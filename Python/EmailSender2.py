import smtplib
import base64
import sys

from email.mime.text import MIMEText

username64="dGVsZWNvbWl0YWxpYVxDRDAyMDY0NQ=="
password64="MHBlcmEuMDUyMDE4"
Sender = 'ga_opera@telecomitalia.it'
Recipients = ['fabio.zangari@telecomitalia.it']

body = "Ciao,\nQuesta e' una mail inviata con Python!!!\n\nSaluti.\nGA OPERA"
msg = MIMEText(body, 'plain', 'utf-8')
msg['From'] = Sender
msg['To'] = ','.join(Recipients)
msg['Subject'] = "Test invio mail.".encode()

try:
    s = smtplib.SMTP("SmtpApplication.telecomitalia.local",25)
    s.starttls()
    s.login(base64.b64decode(username64),base64.b64decode(password64))
    s.sendmail(Sender, Recipients, msg.as_string())
    print ('Successfully sent email!!!')
    s.quit()
except:
    print(sys.exc_info())
