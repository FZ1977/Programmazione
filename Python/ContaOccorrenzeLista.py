# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:24:21 2022

Sia a una lista lunga n, scrivere un programma che 
chiede all'utente di digitare m stringhe e per ognuna 
di queste il programma deve stampare quante volte 
compare in a ed in che posizione si trova l'ultima 
occorrenza (se il numero di occorrenze è >0). 
Il costo della soluzione deve essere O(n+m)

@author: fabio
"""

a = ['s0','s1','s2','s0','s0','s2','s3','s3','s4']
c = 4

d = {}    
for n in range(len(a)):
    if a[n] in d.keys():
        d[a[n]] = (d[a[n]][0] + 1, n)
    else:
        d[a[n]] = (1, n)
        
for m in range(c):
    s = input('Inserisci una stringa: ')
    if s in d:
        print(s, 'compare', d[s][0], 'volte, ultima occorrenza in', d[s][1])
    else:
        print(s, 'non compare nella lista.')