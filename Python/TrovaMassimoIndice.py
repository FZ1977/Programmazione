# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:23:53 2023

@author: Fabio Zangari
Scrivere una funzione che data una lista ordinata in
ingresso questa ritorna la chiave maggiore in cui
e' presente il valore cercato.
"""

# %% Esercizio 
def BinSearch(a, v, sx, dx, k):
    if dx - sx > 1:
    
        k = ((dx - sx)//2) + sx
        
        if a[k] == v:
            test = True
            while test and k < dx:
                k += 1
                if a[k] != v:
                    k -= 1
                    test = False
            
            return k
        
        if a[k] < v:
            sx = k
            k = BinSearch(a, v, sx, dx, k)
            return k
        
        if a[k] > v:
            dx = k
            k = BinSearch(a, v, sx, dx, k)
            return k
    
    if dx - sx == 1:
        if a[k] == v:
            return k
        if a[k+1] == v:
            return k+1
        
        return -1

a=[1,1,1,1,1,1,1]

print(BinSearch(a, 0, sx=0, dx=len(a)-1, k=0)) # cerca in O(nlogn)

# %% Variazione dell'esercizio precedente.

"""
Created on Fri Nov 24 21:23:53 2023

@author: Fabio Zangari
Scrivere una funzione che data una lista ordinata in
ingresso questa ritorna la chiave maggiore in cui
e' p se non presente la chiave riporta l'indice in cui
dovrebbe trovarsi.
"""

def BinSearch(a, v, sx, dx, k):
    if dx - sx > 1:
    
        k = ((dx - sx)//2) + sx
        
        if a[k] == v:
            test = True
            while test and k < dx:
                k += 1
                if a[k] != v:
                    k -= 1
                    test = False
            
            return k
        
        if a[k] < v:
            sx = k
            k = BinSearch(a, v, sx, dx, k)
            return k
        
        if a[k] > v:
            dx = k
            k = BinSearch(a, v, sx, dx, k)
            return k
    
    if dx - sx == 1:
        if a[k] == v:
            return k
        if a[k+1] == v:
            return k+1
        
        if v < a[dx] and v > a[sx]:
            return sx + 1
        if v < a[sx]:
            return sx - 1
        if v > a[dx]:
            return dx + 1

a=[1,1,3]

print(BinSearch(a, 4, sx=0, dx=len(a)-1, k=0)) # cerca in O(nlogn)