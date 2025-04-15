# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:27:17 2023

@author: Fabio Zangari
Scrivere una funzione che ordina una lista di tuple (str,int).
L'ordinamento viene fatto in riferimento al valore intero
"""

def OrdinaListaTuple(a, func=(lambda x: x[1])):
    n = len(a)
    i = 0
    
    while n>=2:
        for i in range(len(a[:n-1])):
            if func(a[i]) > func(a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
            
        n -= 1
    
a=[('a',9),('b',4),('c',0),('d',2)]

print('Prima di essere ordinata -> ',a)
OrdinaListaTuple(a)
print('Dopo aver ordinato la lista -> ',a)