#!/usr/bin/python

'''
Filename: SendEmail.py
Author: Fabio Zangari
Property: TIM S.p.A.
Version: 0.1beta
Description: Script utilizzato per inviare le email utilizzando i nuovi SMTP Server SmtpApplication.telecomitalia.local
             
'''

import smtplib
import sys
import base64

sender = "ga_opera@telecomitalia.it"
receivers = "fabio.zangari@telecomitalia.it"
username64="dGVsZWNvbWl0YWxpYVxDRDAyMDY0NQ=="
password64="MHBlcmEuMDUyMDE4"

#message="Hello World, Test di invio Email con Python!!!!"
message = """From: ga_opera <ga_opera@telecomitalia.it>
To: Fabio Zangari <fabio.zangari@telecomitalia.it>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    send = smtplib.SMTP("SmtpApplication.telecomitalia.local",25)
    send.starttls()
    send.login(base64.b64decode(username64),base64.b64decode(password64))
    send.sendmail(sender, receivers, message)
except:
    err = sys.exc_info()[0]
    print err

send.quit()
