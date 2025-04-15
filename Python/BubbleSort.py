# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:00:27 2022

ALGORITMO: BUBBLE-SORT
pre: a e' una lista di numeri
sposta il massimo di a in fondo alla lista, gli
altri elementi occuperanno le posizioni precedenti

@author: fabio
"""

def ordina_lista(a):
    n = len(a)
    
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        
    return a
    
a = [11,4,2,8,5,4,3,9,1,2,3,9,6,3,1,2,3]
print(a)
res = ordina_lista(a)
print(res)