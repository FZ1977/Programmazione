# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:06:02 2023

@author: Fabio Zangari
Converto una stringa in float.
Non e' permesso iniziare con un punto o avere più punti nella stringa
"""

punto = 0 # numero di punti inseriti nella stringa

s = input("Inserisci una stringa numeri da convertire in float: ")

i = 0 # indice della stringa
n = len(s)

while i<n and punto <= 1:
    if s[i] == '.':
        punto += 1
    
    i += 1

if s[0] != '.' and punto <= 1:
    print(float(s)," - ", type(float(s)))
else:
    print("Non posso convertire il numero.")