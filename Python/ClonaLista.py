# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:59:57 2023

@author: Fabio Zangari
Creo una funzione che clona una lista.
"""

def clona(a):
    b = []
    n = len(a)
    i = 0
    
    while i < n:
        if type(a[i]) == int:
            b.append(a[i])
        else:
            b.append(clona(a[i]))
        
        i += 1
    
    return b



# lista da clonare
a=[0,1,[2,3],4,[5,[6,7],8],9]

a_clonato=clona(a)
print(a_clonato)