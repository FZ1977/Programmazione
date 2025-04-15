# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 10:30:52 2022

Scrivere una funzione denominata inverti_dizionario che 
prende in input un dizionario d e restituisce un dizionario 
d_inv che ha per chiavi i valori in d e d_inv[v] è la lista 
di chiavi che d mappa in v. Esempio se

d = { 'k0': 'v0', 'k1': 'v1', 'k2': 'v0' }

allora

d_inv = { 'v0': ['k0', 'k2'], 'v1': ['k1'] }


@author: fabio
"""

def inverti_dizionario(d):
    d_inv = {}
    a 
    for k, v in d.items():
        if v in d_inv:
            d_inv[v].append(k)
        else:
            d_inv[v] = [k]
    return d_inv
    
    
d = { 'k0': 'v0', 'k1': 'v1', 'k2': 'v0' }
res = inverti_dizionario(d)
print(res)