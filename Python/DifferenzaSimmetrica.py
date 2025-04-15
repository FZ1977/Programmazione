# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:00:02 2022

Scrivere una funzione che prende due dizionari in input a e b 
e restituisce un terzo dizionario c che ha per chiavi tutte 
quelle in a che non sono in b e tutte quelle in b che non sono 
in a. 
I valori associati a queste chiavi devono essere quelli del 
dizionario di partenza. La funzione deve chiamarsi 
differenza_simmetrica. 

Esempio se

a = {'k0': 'v0', 'k1': 'v1', 'k2': 'v0'}
b = {'k1': 'v7', 'k2': 'v1', 'k3': 'v3'}

allora differenza_simmetrica(a, b) deve restituire

{'k0': 'v0', 'k3': 'v3'}

Calcolare il costo computazionale della soluzione prodotta.

@author: fabio
"""

def differenza_simmetrica(a, b):
    c = {}
    for k, v in a.items():
        if k not in b:
            c[k] = v
    
    for k, v in b.items():
        if k not in a:
            c[k] = v
    
    return c
    
    
a = {'k0': 'v0', 'k1': 'v1', 'k2': 'v0'}
b = {'k1': 'v7', 'k2': 'v1', 'k3': 'v3'}

res = differenza_simmetrica(a, b)
print(res)