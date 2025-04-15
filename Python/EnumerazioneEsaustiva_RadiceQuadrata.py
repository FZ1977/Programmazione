# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 08:39:25 2022

ALGORITMO: Enumerazione Esaustiva
Utilizzando l'algoritmo di Enumerazione Esaustiva
verifico se x intero positivo è un quadrato perfetto.

@author: fabio
"""

def radice_quadrata(x):
    i = 0
    while i*i < abs(x):
        i += 1
    return i
    
x = int(input('Iserisci un numero intero positivo: '))
res = radice_quadrata(x)

if res*res != x:
    print(x, 'non è un quadrato perfetto.')
else:
    print(res, 'è la radice quadrata di', x)