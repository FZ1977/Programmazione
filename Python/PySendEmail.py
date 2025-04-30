# -*- coding: cp1252 -*-
'''
Filename: PySendEmail.py
Author: Fabio Zangari
Property: TIM S.p.A.
Data: 2020-04-07
Version: 0.1
Description: Invio delle email utilizzando i nuovi SMTP Server SmtpApplication.telecomitalia.local
'''

import sys
import os
import smtplib
import base64

BasePathName = os.path.abspath(os.getcwd())
fo = open(sys.argv[4], "rb") # Devo verificare a quale parametro corrisponde il nome file.

def ComeSiUsa():
    print("#### PySendEmail.py ####")
    print("######################################")
    print("ATTENZIONE: Il requisito minimo per poter eseguire lo script è la presenza di python 2.6.6")
    print("\n")
    print("E' possibile eseguire lo script in questo modo:")
    print("python PySendEmail.py option <nome_allegato>")
    print("./PySendEmail.py option <nome_allegato>")

def FromAddr():
    try:
        FileFromAddr = open(BasePathName"/FileFromAddr.lst","r")
        ListFromAddr = list(FileFromAddr.read().split(" "))
        FileFromAddr.close()
    except:
        print("Errore nella lettura del file FileFromAddr.lst")

def ToAddr():
    try:
        FileToAddr = open(BasePathName"/FileToAddr.lst","r")
        ListToAddr = list(FileToAddr.read().split(" "))
        FileToAddr.close()
    except:
        print("Errore nella lettura del file FileToAddr.lst")

def CcAddr():
    try:
        FileCcAddr = open(BasePathName"/FileCcAddr.lst","r")
        ListCcAddr = list(FileCcAddr.read().split(" "))
        FileCcAddr.close()
    except:
        print("Errore nella lettura del file FileCcAddr.lst")

def InviaEmail(fromaddr, toaddr, message):
    try:
        send = smtplib.SMTP("SmtpApplication.telecomitalia.local",25)
        send.starttls()
        send.login(base64.b64decode(username64),base64.b64decode(password64))
        send.sendmail(fromaddr, toaddr, message)
        print "Successfully sent email"
    except:
        err = sys.exc_info()[0]
        print "Error: unable to send email"
        print err
def InviaEmailAttach(fromaddr, toaddr, message):
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64
    marker = "AUNIQUEMARKER"
    body = """ %s """ % (message)

    # Define the main headers.
    part1 = """ From: %s
    To: %s
    Subject: %s
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=%s
    --%s
    """ % (fromaddr, toaddr, subject, marker,  marker)

    part2 = """Content-Type: text/plain
    Content-Transfer-Encoding:8bit

    %s
    --%s""" % (body, marker)

    # Define the attachment section
    part3 = """Content-Type: multipart/mixed; name=\"%s\"
    Content-Transfer-Encoding:base64
    Content-Disposition: attachment; filename=%s

    %s
    --%s--
    """ % (filename, filename, encodedcontent, marker)

try:
    if len(sys.argv) - 1 == 0:
       print("Invio la m ail senza allegato.")
    elif len(sys.argv) - 1 == 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "-help":
            ComeSiUsa()
        else:
            print("Invio la mail con l'allegato.")
except:
    print("Utilizzare l'option -h o -help per vedere come si usa.")
