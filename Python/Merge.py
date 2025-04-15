# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:52:21 2022

ALGORITMO: Merge

Precondizione: a e b due liste numeriche ordinate in modo non decrescente
Restituisce una lista c ordinata ottenuta dalla fusione di a e b

@author: fabio
"""

def merge( a, b ):
    n_a, n_b = len(a), len(b)
    i, j = 0, 0 # indice in a ed in b rispettivamente
    c = [] # lista di output
    
    while i < n_a and j < n_b:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    c += a[i:] + b[j:]
    
    return c

a = [2, 6, 7, 7, 11]
b = [0, 1, 8,10, 13, 21, 29, 30]
c = merge(a, b)
print(c)

