# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:43:00 2022

Scrivere un programma che chiede in input due stringhe 
*a* e *b*. Se *b* e' sottostringa di *a* il programma 
stampa la posizione di *a* a partire da cui compare *b*. 
Altrimenti il programma deve stampare -1. Ad esempio 
se *a* e' la stringa 'rinoceronte' e *b* e' la stringa 
'noce', il programma deve stampare 2. 

@author: fabio
"""

a = input('Inserisci una stringa: ')
b = input('Inserisci una stringa: ')

n = len(a)
m = len(b)

i = 0
j = 0

trovato = False

if b in a:
    while i<n and not trovato:
        if a[i] == b[0]:
            trovato = True
            print(i)
        i += 1
else:
    print('-1')