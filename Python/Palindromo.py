# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:48:10 2022

Scrivere un programma che stampa Vero 
se la parola inserita è palindroma.

@author: fabio
"""

a = input('Inserisci la parola da verifica:')
n = len(a)
i = 0
pal = ''
test = True

try:
    while i < n and test:
        if a[i] == a[n-1]:
            n -= 1
            i += 1
            test = True
        else:
            test = False
            n -= 1
            i += 1
    
    if test == True:
        print('Vero')
except NameError:
    print('Inserire una parola da verificare.')    
        