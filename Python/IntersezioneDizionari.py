# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:11:28 2023

@author: Fabio Zangari
Scrivere una funzione che riceve in ingresso due dizionari e ritorna in uscita
un dizionario che è l'intersezione delle chiavi e che ha come valore la somma
dei loro valori.
"""

def IntersezioneDizionari(d1, d2):
    d = {}
    for k in d1.keys():
        if k in d2:
            d[k] = d1[k] + d2[k]
            
    return d

d1 = {'f':1, 'a':2, 'b':3, 'i':4, 'o':5}
d2 = {'e':5, 'l':6, 'i':7, 's':8, 'a':9}

print(d1)
print(d2)
print(IntersezioneDizionari(d1, d2))