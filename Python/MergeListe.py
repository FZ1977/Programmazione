# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:27:18 2023

@author: Fabio Zangari
Scrivere una funzione che prende due liste in ingresso di 
lunghezza uguale e crei una lista che contenga le tuple 
contenente i valori delle due liste nella stessa posizione.
"""

def MergeLista(a,b):
    n = len(a)
    c=[]
    
    for i in range(n):
        c.append((a[i],b[i]))
        
    return c

a=[1,2,3,4]
b=['uno','due','tre','quattro']

print(MergeLista(a, b))