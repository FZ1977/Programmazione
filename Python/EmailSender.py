import smtplib
import base64
import sys

username64="dGVsZWNvbWl0YWxpYVxDRDAyMDY0NQ=="
password64="MHBlcmEuMDUyMDE4"
Sender = 'ga_opera@telecomitalia.it'
Recipients = ['fabio.zangari@telecomitalia.it']

message = """From: ga_opera@telecomitalia.it
To: fabio.zangari@telecomitalia.it
Subject: Prova invio mail da Python.

Python e' super!!!!!
Ciao da Fabio.

Saluti
GA OPERA
"""
try:
    s = smtplib.SMTP("SmtpApplication.telecomitalia.local",25)
    s.starttls()
    s.login(base64.b64decode(username64),base64.b64decode(password64))
    s.sendmail(Sender, Recipients, message)
    print ('Successfully sent email!!!')
    s.quit()
except:
    print(sys.exc_info()[0])
