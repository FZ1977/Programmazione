#!/usr/bin/python

import smtplib
import base64

filename = "/tmp/test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

# Define username and password in base64 encode.
username64="dGVsZWNvbWl0YWxpYVxDRDAyMDY0NQ=="
password64="MHBlcmEuMDUyMDE4"

sender = 'ga_opera@telecomitalia.it'
reciever = 'fabio.zangari@telecomitalia.it; fabio.zangari@it.telecomitalia.it'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: GA OPERA <ga_opera@telecomitalia.it>
To: Fabio Zangari <fabio.zangari@telecomitalia.it>; Fabio Zangari <fabio.zangari@it.telecomitalia.it>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
    send = smtplib.SMTP("SmtpApplication.telecomitalia.local",25)
    send.starttls()
    send.login(base64.b64decode(username64),base64.b64decode(password64))
    send.sendmail(sender, reciever, message)
    print "Successfully sent email"
except Exception:
    print "Error: unable to send email"

