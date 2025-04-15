# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:14:31 2022

scrivere un programma che, data una lista 
contenente numeri, porta il valore massimo 
in ultima posizione e gli altri elementi 
nelle posizioni precedenti.

@author: fabio
"""

def ordina_lista(a):
    a_copy = a[:]
    n = len(a_copy)
    
    for i in range(n-1):
        if a_copy[i] > a_copy[i+1]:
            a_copy[i], a_copy[i+1] = a_copy[i+1], a_copy[i]
        
    return a_copy
    
a = [11,4,2,8,5,4,3,9,1,2,3,9,6,3,1,2,3]
print(a)
res = ordina_lista(a)
print(res)