# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:55:42 2023

@author: Fabio Zangari
Scrivere una funzione che prende una lista con valori di
qualsiasi tipo, sostituisca con le stringhe il valore
numerico della loro lunghezza e poi la ordini.
"""

def OrdinaLista(a,key=(lambda x: len(x) if type(x)==str else x)):
    n=len(a)
    
    while n>=2:
        for i in range(n-1):
            if key(a[i]) > key(a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                
        n -= 1

      
a=[3.14,'python',2,'programma',12,0,'corso']
print("Lista prima di essere ordinata ->", a)
OrdinaLista(a)
print("Lista dopo essere stata ordinata ->", a)