# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:18:57 2022

ALGORITMO: MERGE (ottimizzato)

Precondizione: a lista e a[lx:cx] e a[cx:rx] ordinate in modo non decrescente
Modifica a fondendo le due sottoliste in modo che a[lx:rx] risulti ordinata
    
Sia n = len(a), e k = rx-lx
    
Costo: lineare in k

@author: fabio
"""

def merge( a, lx, cx, rx ):
    i, j = lx, cx # indice in a[lx:cx] ed in a[cx:rx] rispettivamente
    c = [] # lista di output
    
    # Costo O(k) 
    while i < cx and j < rx:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    
    # Costo O(k)
    c += a[i:cx] + a[j:rx]
    
    #a = a[:lx] + c + a[rx:] Costo lx + (rx-lx) + (n-rx) = O(n)

    # Costo O(k)
    for i in range(len(c)):
        a[lx+i] = c[i]