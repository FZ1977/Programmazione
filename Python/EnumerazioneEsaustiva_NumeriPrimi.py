# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:04:33 2022

ALGORITMO: Enumerazione Esaustiva
Dato un numero x in input verifica se questo è un numero primo.

@author: fabio
"""

def numeri_primi(x):
    i = 1
    c = 0
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
            
x = int(input('Inserisci un numero: '))
res = numeri_primi(x)
if res == True:
    print(x, 'è un numero primo.')
else:
    print(x, 'non è un numero primo.')