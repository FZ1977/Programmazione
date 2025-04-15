#!/usr/bin/env python

import sys
import os

def crea_file(file_name):
    print "Stai creando il file " + file_name
    fd=file(file_name,'w')
    fd.write("Ciao!!!!!\n")
    fd.close()

def cancella_file(file_name):
    print "Prima di rimuovere il file ti faccio vedere cosa contiene..."
    fd=file(file_name,'r')
    print fd.read()
    print "Stai cancellando il file " + file_name
    os.remove(file_name)

file_name=sys.argv[1]

crea_file(file_name)
domanda=raw_input("Vuoi cancellare il file "+ file_name + " (s/n): ")
if ( domanda == "s" ):
    cancella_file(file_name)
else:
    print "Hai deciso di non cancellare il file...."
