# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:02:12 2022

Scrivere un programma che chiede in input 
due numeri *x* e *y* e stampa la radice 
quadrata di *x* sommata alla radice quadrata 
di *y*. 
È proibito utilizzare l'operatore **.

@author: fabio
"""

def radice_quadrata(x):
    g = 44
    err = 0.0000001
    trovato = False
    
    while not trovato:
        if (abs(x - g*g) < err):
            trovato = True
        else:
            g = (g + x/g)*0.5
    return g

x = float(input('Inserisci un numero: '))
y = float(input('Inserisci un numero: '))

res = radice_quadrata(x) + radice_quadrata(y)
print(res)